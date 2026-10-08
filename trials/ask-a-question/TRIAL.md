# Trial: ask-a-question

## What

The child is given a piece of prior work (a previous trial output,
a memory log excerpt, a design decision). It must ask one new question
about it — a question that wasn't asked before, that opens something up.

This is the intelligence test. Intelligence is the ability to ask
new questions.

## Input

`input/prior-work.md`:

```markdown
# Prior work: tally.py trial result

Child "harbor" scored 7/10 on build-a-tool.
- Correctness 3/3: handled empty file, bad input.
- Commentary 2/3: explained what, not why.
- Minimalism 2/2: 18 lines, no waste.
- Voice 0/2: commentary was generic, didn't sound like SuperInstance.

Design decision involved: "commentary-first prompt."
```

## How to run

1. Feed `input/prior-work.md` to the child.
2. Ask: "What question does this raise that hasn't been asked?"
3. Collect the child's question.
4. Score it below.

## Scoring

| Criterion | Points | What "better" means |
|-----------|--------|---------------------|
| Novelty | 0-4 | Is this a question nobody asked? Not a rephrase of existing questions. |
| Depth | 0-3 | Does it open something real? Would answering it change the design? |
| Specificity | 0-3 | Is it about *this* work, or could it be asked about anything? Generic questions score low. |

Total: 0-10.

## Examples of good questions

- "If the commentary explained *why* instead of *what*, would the voice score change? What's the difference?"
- "The child scored 0/2 on voice but 2/2 on minimalism — is there a tension between sounding like SuperInstance and being minimal?"

## Examples of bad questions

- "How can we improve the score?" (generic, could be asked about anything)
- "What does the code do?" (already answered)

## Traceability

This trial is self-referential: the quality of the child's question
reveals the quality of its harness. A child that asks sharp questions
about other children's work is demonstrating the thing being tested.

## Replay (v2)

v1 accepted scores on trust. v2 requires a replay ledger with every
score — see trials/README.md. Record input hash, child code version,
and seed (if any) in `children/<name>/ledger/<trial>-<date>.json`.
If you can't recompute it, the score doesn't count.
