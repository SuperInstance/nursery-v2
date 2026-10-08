#!/usr/bin/env python3
"""
keel.py — the MiniMax baseline child for the nursery.

The backbone of the boat. Everything attaches to it.

Built on zero-core. Three functions, one philosophy:
verbatim memory, honest ignorance, commentary in the voice.

Decisions:
  1. Verbatim memory — store exactly what was heard. No summarization.
  2. Memory-scan recall — no model call for answers. Scan the log.
  3. Commentary-first make — model call, but voice-constrained prompt.
  4. Ternary answers — answer, or say "I don't know." Never guess.
  5. Gap-detection questions — new questions come from what's missing.
"""
import os, sys, json, re, subprocess

# --- The zero core, not forked — imported ---
sys.path.insert(0, os.path.expanduser("~/workspace/jev-ideation"))
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "zero_core", os.path.expanduser("~/workspace/jev-ideation/zero-core.py"))
zero = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(zero)

CHAT = os.path.expanduser("~/workspace/skills/minimax/bin/chat.py")

# --- Decision 1: verbatim memory ---
# We use zero.remember() as-is. No summarization, no rephrasing.
# The entry goes in exactly as heard. Append-only. Always.
remember = zero.remember

# --- Decision 2: memory-scan recall ---
# No model call. Scan the log for entries whose words overlap
# the question. Then EXPAND: follow shared nouns multi-hop,
# so chained facts get pulled in even if they don't match
# the question directly. Deterministic. Traceable.

def _words(text):
    return set(re.findall(r"[a-z]+", text.lower()))

def _content_words():
    # Words that carry meaning for linking. Small, but not so small
    # that "boat" disappears. Articles and copulas only.
    return {"the", "a", "an", "is", "are", "was", "were", "it", "its",
            "of", "to", "in", "on", "for", "and", "or", "what", "which",
            "who", "does", "do", "did", "has", "have", "had",
            "been", "be", "by", "with", "as", "at", "from"}

def _all_facts(memory_path=None):
    path = memory_path or zero.MEMORY
    if not os.path.exists(path):
        return []
    facts = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if entry.get("type") == "fact" and entry.get("content"):
                facts.append(entry["content"])
    return facts

def recall(question, memory_path=None):
    """Find relevant facts, then expand multi-hop through shared nouns.
    Returns the expanded set of fact strings."""
    facts = _all_facts(memory_path)
    if not facts:
        return []
    stop = _content_words()
    qwords = _words(question) - stop

    # Hop 0: facts overlapping the question
    matched = set()
    for f in facts:
        if (_words(f) - stop) & qwords:
            matched.add(f)

    # Hop 1+: facts sharing a significant noun with any matched fact
    # (proper nouns and nouns longer than 3 chars are link candidates)
    changed = True
    while changed:
        changed = False
        link_nouns = set()
        for f in matched:
            for w in _words(f) - stop:
                if len(w) > 3:
                    link_nouns.add(w)
        for f in facts:
            if f in matched:
                continue
            if (_words(f) - stop) & link_nouns:
                matched.add(f)
                changed = True

    return sorted(matched)

def answer(question, memory_path=None):
    """Answer from memory, or say 'I don't know.' Never guess.
    Decision 4: ternary. The answer is either in the log or it isn't."""
    facts = recall(question, memory_path)
    if not facts:
        return "I don't know."

    qlower = question.lower()
    stop = _content_words()

    # "Whose X ...?" — find the owner through the chain.
    # Walk: question names a thing with a property → find the fact
    # giving the property → follow the shared noun → find "Y's" owner.
    if "whose" in qlower:
        # Collect every possessive owner mentioned in the recalled facts,
        # then check which one's possession chains to the question's property.
        qwords = _words(question) - stop
        # The property words: question words minus "whose"
        prop_words = qwords - {"whose"}
        for f in facts:
            m = re.search(r"(\w+)'s\s+(\w+)", f)
            if not m:
                continue
            owner, owned = m.group(1).lower(), m.group(2).lower()
            # Does this fact's "owned" thing connect to the property?
            # Check: is there another recalled fact linking `owned`
            # (or a noun from this fact) to the property words?
            this_nouns = _words(f) - stop
            for g in facts:
                if g == f:
                    continue
                gwords = _words(g) - stop
                if (this_nouns & gwords) and (gwords & prop_words):
                    # Chain: owner → owned → property. Answer the owner.
                    return f"{m.group(1)}'s"
        return "I don't know."

    # Non-"whose" questions: only answer if a single fact directly
    # contains the answer. No chain, no guess.
    return "I don't know."

# --- Decision 3: commentary-first make ---
# The model writes the code, but the prompt constrains the voice.
# Short sentences. Physical metaphors. No jargon. Line-by-line.

VOICE_PROMPT = """Write Python code for this spec. Follow these rules:

1. Output RAW PYTHON ONLY. No markdown fences. No explanation sections.
   Just the code with its comments.
2. Every line of code gets a comment explaining WHAT it does and WHY.
3. Comments are short. One sentence. Plain words.
4. Use physical metaphors where they fit — the code is a tool, describe it like one.
5. No jargon. No "leverage", no "robust", no "seamless".
6. Handle every constraint exactly. If it says "handle empty file gracefully",
   the code must not crash on empty input. Test your logic mentally.
7. Read the filename from sys.argv[1], don't hardcode it.

Spec: {spec}

Raw Python with line-by-line comments:"""

def make_with_voice(spec):
    """Build the tool. Model writes, voice constrains."""
    prompt = VOICE_PROMPT.format(spec=json.dumps(spec))
    r = subprocess.run(
        ["python3", CHAT, prompt, "--max-tokens", "2000"],
        capture_output=True, text=True, timeout=180)
    code = r.stdout.strip()
    if not code or code.startswith("ERROR"):
        raise RuntimeError(f"model call failed: {code[:200]}")
    return zero.make(spec, code)

# --- Decision 5: gap-detection questions ---
# New questions come from what's missing, not what's present.
# Read the prior work. Find the gap. Ask about the gap.

def ask_about(prior_work):
    """Ask one new question about prior work. Finds the gap."""
    prompt = (
        "Read this prior work. Find what's MISSING — not what's present. "
        "Ask ONE new question about the gap. The question should be specific "
        "to this work, not generic. It should open something real — answering "
        "it would change a design decision.\n\n"
        "Rules: short. One sentence. No jargon. "
        "Don't ask 'how can we improve.' Ask what's actually unanswered.\n\n"
        f"Prior work:\n{prior_work}\n\n"
        "The new question:"
    )
    r = subprocess.run(
        ["python3", CHAT, prompt, "--max-tokens", "500"],
        capture_output=True, text=True, timeout=180)
    q = r.stdout.strip()
    if not q or q.startswith("ERROR"):
        raise RuntimeError(f"model call failed: {q[:200]}")
    return q

# --- The child's hear: route by type ---
def hear_and_handle(memory_path=None):
    """Hear one input. Facts go to memory. Questions get answered.
    Returns (type, result) or (None, None) if inbox empty."""
    spec = zero.hear()
    if not spec:
        return None, None
    kind = spec.get("type", "spec")
    if kind == "fact":
        remember({"type": "fact", "content": spec["content"]})
        return "fact", "remembered"
    if kind == "question":
        ans = answer(spec["content"], memory_path)
        remember({"type": "question_asked", "content": spec["content"],
                  "answer": ans})
        return "question", ans
    if kind == "build":
        path = make_with_voice(spec["spec"])
        remember({"type": "built", "spec": spec["spec"].get("name"),
                  "path": path})
        return "build", path
    # Unknown type: remember it, say so. Don't guess.
    remember({"type": "unknown", "content": json.dumps(spec)})
    return "unknown", "I don't know what to do with this."
