# TOKEN.md — the public token

Copy this file to `children/<your-child-name>/TOKEN.md` and fill it in.
Delete the guidance in brackets. This file is PUBLIC — peers see it,
breeding selects on it. No reasoning, no justifications, no hunches.
The committed algorithm and its relational context. Nothing else.

## Token identity

- **Token name:** [e.g. `keel/tally-v1` — child-name/algorithm-version]
- **Child:** [child name, links to CHILD.md]
- **Committed:** [YYYY-MM-DD HH:MM UTC]
- **Zero core version:** [commit hash]

## The algorithm

- **Name:** [what the committed algorithm is called]
- **Inputs:** [what it takes — types, format, constraints]
- **Outputs:** [what it produces — types, format, guarantees]
- **Parameters:** [tunable knobs, with defaults and ranges]
- **Deterministic:** [yes / no — if no, what varies and what seeds it]

[Describe the algorithm mechanically. What it does, not why you
chose it. A peer should be able to predict its behavior from this
section alone — that's the token-sufficiency test.]

## Counterparty

- **Who this token is for:** [named counterparty — person, role,
  child, or trial class. Not "everyone." Not "no one."]
- **What they get:** [the specific commitment — what the counterparty
  can rely on]
- **Debt IDs:** [list — each debt below gets an ID, e.g. `keel-001`]

## Declared debts

### Debt [ID, e.g. keel-001]

- **Owed to:** [counterparty — must match or narrow the token counterparty]
- **Obligation:** [named, specific — "answer harbor's questions within
  one trial cycle", not "be helpful"]
- **Service mechanism:** [how this child pays — what it does, when,
  how the counterparty verifies]
- **Inherited:** [yes/no — if yes, from which parent debt ID]
- **Status:** [declared / servicing / serviced / defaulted]

[Add as many debts as the child owes. Minimum one. A child with no
debts has no counterparty and no reason to exist.]

## Trial interface

- **Hear:** [how the child receives input — channel, format]
- **Make:** [how it produces output — channel, format]
- **Remember:** [what it stores — format, scope]

[The standard zero interface. Note any constraints or extensions
here so trial harnesses know how to drive this child.]

## Replay pointer

- **Ledger:** [path to replay ledger, e.g. `ledger/build-a-tool.json`]
- **Code version:** [commit hash of child code at last trial]
