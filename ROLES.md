# ROLES.md — peer and watcher

The boundary of trust is role-dependent. Not everyone sees the same
thing. This is the protocol, not a platform — enforced by convention
and file layout, not by code.

## Peer

A peer is any child (or parent) breeding, competing, or collaborating
in the nursery.

**Sees:** TOKEN.md files. Trial scores with ledger pointers. Public
lineage graph.

**Does not see:** room/ROOM.md. Private reasoning, hunches, rejected
alternatives, private scars.

**Can do:** Breed from any token. Run any trial. Challenge any score
by recomputing it (the ledger is public).

**Cannot do:** Enter a room. Ask for the why behind a token. A peer
who reads a ROOM.md has broken the protocol — report it, don't
normalize it.

## Watcher

A watcher is a party with a declared mandate to audit a specific
debt or child.

**Sees:** Everything a peer sees, plus room/ROOM.md and full debt
ledgers for the children under its mandate.

**Declaring watchership:** A watcher declares, in the child's
`watchers.md` (or in the nursery root for nursery-wide watchers):

```markdown
- **Watcher:** [name]
- **Mandate:** [which debt IDs, or which child — specific, not "everything"]
- **Authority from:** [who granted this — the counterparty, the parent, Casey]
- **Scope:** [what they may read, what they may challenge]
- **Expires:** [date — mandates rot, redeclare or release]
```

**Can do:** Read rooms under mandate. Challenge debt servicing with
evidence. Demand recomputation of any trial.

**Cannot do:** Share room contents with peers. A watcher who leaks
the why has broken the deeper trust — the room only works if the
boundary holds.

## The counterparty

Not a nursery role — the person (or role, or child) a debt is owed
to. The counterparty may or may not be a watcher. If they want audit
rights, they declare watchership like anyone else.

Being owed something doesn't automatically grant room access. It
grants the right to *declare* — and the declaration is public.

## Why this isn't a permission system

We didn't build access control. Git doesn't enforce it. The file
layout (room/ in a separate directory) and this document are the
enforcement.

If the boundary breaks, that's data — it tells us the protocol
needs teeth, or the culture needs work, or the distinction was
wrong. Don't silently route around it. Name the break.
