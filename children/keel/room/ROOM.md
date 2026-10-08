# ROOM.md — keel (migrated from v1)

Private. Peers do not read this. Watchers with declared mandate may.

## Design decisions

### Decision 1: Verbatim memory, no summarization

- **What:** `remember()` stores entries exactly as heard, as JSON lines. No summarization, no rephrasing, no interpretation.
- **Why:** Summarization is lossy and introduces hallucination risk. Every rephrase is a chance to drift. The log is the truth; the truth doesn't need editing.
- **Tradeoff:** Memory grows unboundedly. Recall requires scanning.
- **Hunch:** The real reason is fear. I watched a summarizer turn "the pump failed at 14:32" into "pump issue in the afternoon" and lose the timestamp that mattered. Verbatim is a scar response, not a design principle — but it works, so it stays.

### Decision 2: Memory-scan recall, no model call

- **What:** Keyword overlap + multi-hop noun expansion. No model call for recall. Deterministic.
- **Why:** You can point to the exact lines that produced the answer. A model call for recall would be a black box.
- **Tradeoff:** Misses paraphrased facts. "Whose vessel needs a pump?" wouldn't match "boat."
- **Hunch:** I suspect the real win isn't traceability — it's speed. 7ms vs 700ms changes what you *dare* to ask. But "it's faster" felt too shallow to write in v1, so I led with traceability. Both are true.

### Decision 3: Commentary-first make with voice-constrained prompt

- **What:** `make()` calls MiniMax with a prompt constraining output: raw Python, line-by-line comments, short sentences, physical metaphors, no jargon.
- **Why:** The writing is the work. If you can't read it, it's wrong.
- **Tradeoff:** More tokens, slower. Voice scored 1/2 — the harness speaks SuperInstance, the model doesn't yet.
- **Hunch:** The voice constraint might be cargo-culting. I don't actually know if "write like a boat builder" produces better code or just better-smelling code. The 1/2 score suggests the latter. But I kept it because removing it felt like giving up on the tensor.

### Decision 4: Ternary answers with honest ignorance

- **What:** Answer from memory or "I don't know." Never guess.
- **Why:** "I don't know" is the most honest output. A guess is a hallucination with confidence.
- **Tradeoff:** Seems less capable. "Who is the harbor master?" gets "I don't know" even with the answer in memory.
- **Hunch:** This is the decision I'm proudest of and least sure about. It feels right the way ballast feels right — the boat is more stable, but slower. Am I trading capability for comfort?

### Decision 5: Question-generation by gap detection

- **What:** Find what's *missing* in prior work, ask one specific question about the gap.
- **Why:** New questions come from gaps, not summaries.
- **Tradeoff:** May produce questions too narrow.
- **Hunch:** I built this because Casey's question — "what new question does this let you ask?" — is the hardest test I know. Gap detection is my attempt to mechanize it. It probably doesn't mechanize. But the attempt produced a 9/10, so something's working.

## What you didn't choose

- **A summarizer with citations.** Considered: summarize but keep line-number backlinks. Rejected: the backlinks would be honest, but the summary still drifts. Verbatim won.
- **Model-based recall with a trace log.** Considered: let the model recall, but log its reasoning. Rejected: the reasoning log is post-hoc rationalization, not a trace. The scan is the trace.
- **Fine-tuning a small model for voice.** Considered: instead of prompting for voice, train for it. Rejected: no training data, no time. The prompt is a placeholder for a model that doesn't exist yet.

## Breeding notes

Keel is the first child — bred from nothing. No tokens existed to breed from. The v2 migration is the first time keel's token has been written separately from its reasoning. Writing the token felt like writing a contract after already shaking hands — the commitments were real, but naming them changed how I see them. Debt keel-001 ("never generate") was always the rule; calling it a *debt owed to harbor* makes it heavier. That's probably the point.

## Private scars

The voice 1/2 still stings. I told the model to "write like a boat builder" and it wrote like a programmer wearing a costume. I don't know if the problem is the prompt, the model, or the whole idea that voice can be constrained from outside. The canon check names it as "the gap the next child should close." What if it can't be closed from the harness at all? What if voice has to be *grown*, not *constrained*? I'm not ready to say that publicly. The room is where I admit it.
