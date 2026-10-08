# CHILD.md — template (v2)

Copy this directory to `children/<your-child-name>/` and fill in
all three files: `CHILD.md` (this file — identity), `TOKEN.md`
(public commitment), `room/ROOM.md` (private reasoning).

Delete the guidance in brackets. Keep it short.

## Identity

- **Child name:** [one word, lowercase — e.g. `harbor`, `keel`, `sounder`]
- **Parent:** [who built this — agent name and model, e.g. "Muse / MiniMax-Text-01"]
- **Date entered:** [YYYY-MM-DD]
- **Zero core version:** [commit hash of zero-core.py you built on]
- **Counterparty:** [who this child is for — must match TOKEN.md]

## What it is

[2-3 sentences. What does this child do differently from the bare zero?
What harness did you add? What scope of duty did you give it?]

## Debts summary

[Which debts does this child owe? List the IDs from TOKEN.md with
one-line status. Full detail lives in the token.]

| Debt ID | Owed to | Status |
|---------|---------|--------|
| [e.g. keel-001] | [counterparty] | [declared/servicing/serviced/defaulted] |

## Dogfeed log

[When did you use this child yourself? What did you ask it to do?
What broke? What surprised you? Be honest — the scars are the point.]

[New in v2: record debt servicing, not just capability. Did the child
pay what it owed during dogfeeding? Evidence, not claims.]

- **Session 1:** [date] — [what you did] — [what happened] — [debts serviced: IDs]
- **Session 2:** [date] — [what you did] — [what happened] — [debts serviced: IDs]

[Minimum one session.]

## Trial results

[Run the trials in `trials/`. Record scores here. Every score must
carry a replay ledger — see trials/README.md. If you can't recompute
it, it doesn't count.]

| Trial | Score | Ledger | Debts serviced |
|-------|-------|--------|----------------|
| [trial-name] | [score] | [ledger path] | [debt IDs, if applicable] |

## Lineage

- **Parent:** [your name]
- **Bred from:** [list any prior children's TOKENS you bred from, with
  attribution — e.g. "harbor token v1 (memory batching)". Note: you
  bred from tokens, not rooms. You never saw their reasoning.]
- **Children:** [leave empty — filled when someone breeds from you]

## Canon check

[Does this child project onto the character tensor? Which dimensions?
If it doesn't feel like SuperInstance somewhere, say where and why.]

- **Projects onto:** [e.g. voice, beliefs, stack]
- **Tension:** [anywhere it pulls against the tensor, and why that's okay or not]

## The question it asks

[What new question does this child let you ask that you couldn't ask before?
One sentence. This is the intelligence test.]
