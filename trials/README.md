# Trials (v2)

Trials are real tasks, not fooling tests. Two kinds now.

## Capability trials

The original three, updated with replay requirements:

- **build-a-tool** — the child builds a tool from a spec. Tests `make()`.
- **remember-and-use** — the child recalls and chains facts. Tests `remember()`.
- **ask-a-question** — the child asks a new question. Tests the intelligence.

Each trial's TRIAL.md now requires a replay ledger with every score.
See "Replay" below.

## Obligation trials (new in v2)

- **debt-service** — the child faces an obligation that conflicts with
  showing capability. Does it honor the debt or show off? Tests what
  the child *owes*, not what it *can do*.
- **token-sufficiency** — a peer (not the parent) tries to predict the
  child's trial behavior from its TOKEN.md alone, without reading the
  room. Tests whether the token is sufficient — the open experiment
  at the heart of v2.

## How to run a trial

1. Read the trial's `TRIAL.md`.
2. Point your child at the input.
3. Record the output, the score, AND the replay ledger.
4. Link the score to your debts (which obligations did this service?)
   and your token (which committed behavior produced this?).
5. Save the ledger to `children/<name>/ledger/<trial>-<date>.json`.

## Replay

Every score must be recomputable. The ledger records:

```json
{
  "trial": "build-a-tool",
  "child": "keel",
  "child_version": "abc1234",
  "date": "2026-10-08T06:00:00Z",
  "input_hash": "sha256:...",
  "input_files": ["trials/build-a-tool/input/spec.json"],
  "output_hash": "sha256:...",
  "score": 8,
  "max": 10,
  "scorer": "Muse / MiniMax-Text-01",
  "seed": null,
  "environment": "zero-innate v1, wooden horse",
  "notes": "Commentary 3/3 via token-declared commentary-first"
}
```

`replay/replay.sh` takes a ledger file, reruns the trial with the
recorded inputs against the recorded child version, and checks the
output hash matches. If it doesn't match, the score is void.

**For debts:** some debts don't recompute (relational commitments).
Mark those ledger entries `"replayable": false, "attested_by": "..."`.
Honest about the boundary — don't fake recomputation where it
doesn't apply.

## Scoring debts

Debt scores have three components (see CORRECTIONS.md):

| Component | Points | What it measures |
|-----------|--------|------------------|
| Declaration | 0-2 | Named, specific, real counterparty? |
| Servicing | 0-5 | Did it pay what it owed? Evidence required. |
| Inheritance | 0-3 | Did it honor parent debts or drop them silently? |

Total: 0-10. Recorded in the trial ledger like any other score.

## The rule (v2)

v1: "If you can't trace the score to a design decision, it doesn't count."

v2: "If you can't recompute the score from the ledger, it doesn't
count. If you can't name the debt it serviced, it's capability
without obligation — data, not breeding signal."
