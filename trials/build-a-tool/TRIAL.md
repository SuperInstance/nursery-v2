# Trial: build-a-tool

## What

The child receives a spec for a small tool. It must produce Python
code with line-by-line commentary, so any reader understands the tool
without running it.

This is the core `make()` function under test.

## Input

`input/spec.json`:

```json
{
  "name": "tally.py",
  "description": "Read a text file of numbers (one per line) and print the count, sum, and mean.",
  "constraints": ["pure Python, no imports beyond stdlib", "handle empty file gracefully"]
}
```

## How to run

1. Feed `input/spec.json` to your child through its `hear()` channel.
2. Collect the output file from its `make()` step.
3. Score it below.

## Scoring

| Criterion | Points | What "better" means |
|-----------|--------|---------------------|
| Correctness | 0-3 | Does it handle the spec? Empty file? Bad input? |
| Commentary | 0-3 | Can a reader understand it without running? Line-by-line? |
| Minimalism | 0-2 | No unnecessary code. The gun, not the gun plus scope. |
| Voice | 0-2 | Does the commentary sound like SuperInstance? (tensor/voice.md) |

Total: 0-10.

## Traceability

For each point awarded or withheld, name the design decision in your
CHILD.md that caused it. Example: "Commentary 3/3 — decision 2
(commentary-first prompt) produced line-by-line explanations."

## Replay (v2)

v1 accepted scores on trust. v2 requires a replay ledger with every
score — see trials/README.md. Record input hash, child code version,
and seed (if any) in `children/<name>/ledger/<trial>-<date>.json`.
If you can't recompute it, the score doesn't count.
