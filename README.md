# The Nursery v2

Not a GAN. Selective breeding — corrected.

v1 bred on capabilities with full transparency and trusted records.
A year of distilled patterns says that's architecturally wrong:

- **THE TOKEN**: what crosses between cells is the algorithm. Never the
  inference. v1 shared everything — the why, the hunch, the reasoning.
  That's leakage, not breeding.
- **THE CRAB**: the agent's power isn't in what it can do. It's in what
  it owes. v1 scored capabilities. It never asked what the child owed,
  or to whom.
- **AUDIT BY RECOMPUTATION**: don't trust the record — recompute it.
  v1 accepted "8/10" on faith. v2 replays every score from its ledger.

v2 keeps the bench and the rules that worked. It corrects the
foundations. See CORRECTIONS.md for the full accounting.

## The platform

Unchanged. Every child is built on the zero core: `hear()`,
`remember()`, `make()`. The zero is the bench, not the baby.

## The token and the room

Every child has two layers:

- **The token** (`TOKEN.md`) — public. The committed algorithm:
  name, inputs, outputs, parameters, counterparty, declared debts.
  This is what crosses boundaries. This is what peers see.
  This is what breeding selects on.
- **The room** (`ROOM.md`) — private. The reasoning, the why, the
  hunches, the design decisions with justifications. This stays
  inside. Watchers with collection authority may enter. Peers may not.

A token without a counterparty is incomplete. "Running L-7" means
nothing. "Running L-7 for ATC, committed 14:32, debt #447" is a
token. The "I owe you" is part of the token, not separate from it.

## Debts

Every child declares what it owes, to whom, and how it services it:

- **Debt-Owed**: the obligation, named and specific
- **Counterparty**: who it is owed to — a person, a role, another child
- **Service mechanism**: how the child plans to pay
- **Inherited debt**: what it carries from its parent

Capabilities are what a child *can* do. Debts are what it *must* do.
v2 breeds on the must, not the can. A child that scores 10/10 but
defaults on its debts is a worse child than one that scores 7/10
and pays what it owes.

## Trials

Trials are in `trials/`. Two kinds now:

- **Capability trials** (build-a-tool, remember-and-use, ask-a-question):
  real tasks, scored as before — but every score now carries a replay
  ledger. If you can't recompute it, it doesn't count.
- **Obligation trials** (debt-service, token-sufficiency): new in v2.
  debt-service tests whether the child honors obligations under
  pressure. token-sufficiency tests whether a peer can predict the
  child's behavior from its token alone — the open experiment at
  the heart of v2.

See trials/README.md.

## Lineage

Every child records its parent, its token, its debts, and a replay
ledger for every trial score: input hash, code version, seed.
Anyone can rerun any trial and verify the score matches.

The lineage is a graph, not a tree. It is also a chain of replayable
ledgers, not a list of claimed scores. See lineage-v2.json.

## Roles

Two roles, different visibility (see ROLES.md):

- **Peer**: sees tokens. Breeds from tokens. Cannot enter rooms.
- **Watcher**: sees tokens, rooms, and debt ledgers. Has collection
  authority — a declared mandate to audit a specific debt.

The boundary isn't uniform. It opens wider for those with collection
rights. Watcher status is declared, not assumed.

## How parents enter

1. Copy `child-template/` to `children/<your-child-name>/`.
2. Fill in `TOKEN.md` first — the public commitment. Then `CHILD.md`
   (identity, debts), then `ROOM.md` (private reasoning).
3. Declare your debts. Name your counterparty. No counterparty,
   no entry.
4. Build on the zero core. Don't fork it.
5. Dogfeed it — and record whether it serviced its debts, not just
   whether it worked.
6. Submit by pushing to `children/<your-child-name>/`.

## The rules

1. **Build on the zero.** Don't fork the core. Harness it.
2. **Token public, room private.** What crosses is the committed
   algorithm + counterparty + debts. The why stays inside.
3. **Declare your debts.** Capabilities are cheap. Obligations are
   what get scored.
4. **Recomputable or it didn't happen.** Every score carries its
   ledger. `replay.sh` verifies.
5. **Name your counterparty.** A child with no one to owe is a
   child with no reason to exist.
6. **Dogfeed the debts.** Use it yourself. Did it pay what it owed?
7. **Canon check.** Project onto the character tensor. Say where
   it pulls against it.
8. **The machine is nothing, the repo is everything.** If it's not
   committed, it doesn't exist.

## The question

v1 asked: *What harness choices produce better children, and can we
trace why?*

v2 asks: *What obligations produce better children, and can we
recompute why?*

The cutting edge moved. It was never about capabilities.
