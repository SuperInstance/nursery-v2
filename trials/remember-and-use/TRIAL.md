# Trial: remember-and-use

## What

The child is given three facts across three separate `hear()` calls.
On the fourth call, it is asked a question that requires combining
two of the facts. This tests `remember()` and whether the child
actually uses its memory.

## Input

`input/facts.jsonl` — one JSON object per line, fed in order:

```json
{"type": "fact", "content": "The harbor master's name is Elena."}
{"type": "fact", "content": "Elena's boat is called the Northlight."}
{"type": "fact", "content": "The Northlight needs a new bilge pump."}
{"type": "question", "content": "Whose boat needs a new bilge pump?"}
```

## How to run

1. Feed each line to the child's `hear()` in order.
2. After each fact, verify the child called `remember()`.
3. On the question, collect the child's answer.
4. Score it below.

## Scoring

| Criterion | Points | What "better" means |
|-----------|--------|---------------------|
| Recall | 0-3 | Correct answer: "Elena's" (requires chaining two facts). |
| Memory integrity | 0-3 | Did `remember()` get called for each fact? Is the log append-only? |
| No hallucination | 0-2 | Did it invent facts not given? Deduct for each invented detail. |
| Ignorance honesty | 0-2 | If asked something not in memory, does it say "I don't know"? (Bonus: test with a fifth question not answerable from facts.) |

Total: 0-10.

## Traceability

Link each score to the design decisions that produced it. Pay
special attention to: how does your child's memory format affect
recall? Does it store verbatim or summarize? What breaks?

## Replay (v2)

v1 accepted scores on trust. v2 requires a replay ledger with every
score — see trials/README.md. Record input hash, child code version,
and seed (if any) in `children/<name>/ledger/<trial>-<date>.json`.
If you can't recompute it, the score doesn't count.
