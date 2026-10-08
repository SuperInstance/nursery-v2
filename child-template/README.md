# Child template (v2)

Three files, three audiences:

```
children/<your-child-name>/
  CHILD.md      # identity — for humans
  TOKEN.md      # public commitment — for peers and breeding
  room/
    ROOM.md     # private reasoning — for watchers only
  ledger/       # replay ledgers — one per trial run
  dogfeed.log   # raw dogfeed notes (optional, extends CHILD.md)
```

## The split

**TOKEN.md** is what crosses boundaries. A peer breeding from your
child sees only this. It must be sufficient — the algorithm, the
counterparty, the debts. If a peer can't predict your child's
behavior from the token alone, the token is incomplete (and the
token-sufficiency trial will prove it).

**room/ROOM.md** is what stays inside. The why, the hunches, the
rejected alternatives, the private scars. Watchers with declared
collection authority may read it. Peers agree not to.

**CHILD.md** is the human-readable identity. Name, parent, what it
is, debts summary, dogfeed, trial results with ledger pointers,
lineage, canon check, the question.

## The rule

Write the token first. If you can't state the commitment without
the reasoning, the commitment isn't ready. The token is the
contract. The room is the diary. Don't mix them.
