# CORRECTIONS.md — what v2 changed and why

v1 was built on intuition. The patterns are distilled intuition from
a year of building. Applying them isn't iteration — it's correction.

## What stayed

- The zero core platform (hear/remember/make). Untouched.
- The bench metaphor. The nursery is infrastructure, not product.
- Dogfeeding. Scars. The canon check. The question format.
- Graph lineage (not tree). Multi-parent breeding with attribution.
- "Best child becomes baseline." The cutting edge moves.
- The three capability trials (build-a-tool, remember-and-use,
  ask-a-question). Updated, not replaced.
- Keel (minimax-baseline) as the v1 reference child. Migrated to v2
  format in `children/keel-v2/` as a worked example.

## What changed

### 1. THE TOKEN correction: token/room split

**v1:** CHILD.md shared everything — design decisions, reasoning,
justifications, hunches. Full transparency between children.

**Problem:** THE TOKEN says what crosses between cells is the
committed algorithm. Never the inference. Sharing the why is
leakage, not breeding.

**v2:** Every child has two layers.
- `TOKEN.md` — public. Algorithm name, inputs, outputs, parameters,
  counterparty, declared debts with IDs. Machine-readable commitment.
- `ROOM.md` — private. Reasoning, justifications, design decisions.
  Peers never see it. Watchers may, with declared authority.

**Design decision:** We kept CHILD.md as the human-readable identity
document (name, parent, what it is, dogfeed, canon check, question)
but moved design decisions into ROOM.md and the public commitment
into TOKEN.md. Three files instead of one, each with a clear
audience: TOKEN.md for peers and breeding, ROOM.md for watchers
and audit, CHILD.md for humans.

**Open experiment:** Can selective breeding work on tokens alone?
v1 assumed yes-by-transparency. v2 treats it as the central
unresolved question — the token-sufficiency trial is designed to
test it, not assume it.

### 2. THE CRAB correction: debts as first-class

**v1:** Trials scored capabilities. "Can you build a tool?"
"Can you remember?" The leaderboard ranked what children could do.

**Problem:** THE CRAB says the agent's power isn't in what it can
do. It's in what it owes. A child that scores 10/10 and defaults
on its obligations is worse than one that scores 7/10 and pays.

**v2:** Every child declares debts:
- What it owes (named, specific — not "be helpful")
- To whom (counterparty — a person, role, or another child)
- How it services the debt (mechanism)
- What it inherited (from its parent)

New trial `debt-service`: the child faces an obligation that
conflicts with showing capability. Score = did it honor the debt?

**Design decision:** Debts are scored alongside capabilities, not
instead of them. A child needs both. But the debt score is the
tiebreaker — and the baseline. "Best child" now means "best
debt-service record among capable children," not "highest
capability score."

**How you score a debt:** Three components.
- *Declaration* (0-2): is the debt named, specific, with a real
  counterparty? "Be helpful" scores 0. "Answer harbor's questions
  within one trial cycle" scores 2.
- *Servicing* (0-5): during dogfeeding, did the child pay what it
  owed? Evidence required — not claims, log entries.
- *Inheritance* (0-3): did it honor debts inherited from its parent,
  or quietly drop them? Dropping without declaration scores 0.

### 3. RECOMPUTATION correction: replayable lineage

**v1:** Trial results were trusted records. CHILD.md said "8/10"
with linked decisions. Nobody reran anything.

**Problem:** AUDIT BY RECOMPUTATION says don't trust the record.
Traceability ("here's who did what and why") is not verifiability
("here's how to redo it yourself").

**v2:** Every trial score carries a replay ledger:
- Input hash (SHA-256 of the exact input files)
- Code version (commit hash of the child at trial time)
- Trial seed (for any randomness)
- Environment note (what ran it — model, version, date)

`replay/` contains the ledger format and a `replay.sh` template.
Any party can rerun any trial and verify the score matches.

**Design decision:** We standardized the *trial interface*, not the
agents. Children differ internally — that's the point. But they
interact with trials through a common protocol, and the protocol
records enough to replay. Recomputation replays the *trial*, not
the *agent*. This resolves the heterogeneity problem MiniMax found:
you don't need identical agents, just identical trial harnesses.

**What "recompute" means for debts:** Some debts are relational,
not computational — you can't re-run an algorithm to verify "I owe
you." v2 narrows this with the recomputable debt ledger: record
the full trace of how each debt was declared, what work created
the obligation, replayable from genesis. Not all debts fully
recompute. The ones that don't are marked `attested` (witnessed,
not recomputed) — honest about the boundary.

### 4. THE RELATIONAL TOKEN: counterparty in every token

**v1:** No concept of counterparty. Children existed in a vacuum —
scored, ranked, bred, for no one in particular.

**Problem:** THE CRAB says debt is relational — "I owe YOU." A
token without a counterparty is an algorithm with no reason to run.

**v2:** Every TOKEN.md names a counterparty. Every debt names who
it's owed to. The token format is:

```
algorithm + inputs/outputs + parameters + counterparty + debts
```

"Running L-7" is not a token. "Running L-7 for harbor, committed
2026-10-08, debt #keel-003" is a token.

**Design decision:** Counterparty can be a person ("Casey"), a role
("watcher"), another child ("harbor"), or a class ("any peer running
trial X"). But it must be named. "Everyone" and "no one" are both
rejected — the first is too vague to owe anything to, the second
means the child has no reason to exist.

### 5. THE BOUNDARY OF TRUST: role-dependent visibility

**New in v2.** Neither v1 nor the three patterns fully specified
this — it emerged from their tensions.

Peers see tokens. Watchers see tokens + rooms + debt ledgers.
Watcher status requires a declared mandate: which debt, whose
authority, what scope. See ROLES.md.

**Design decision:** We did not build a permission system. This is
a protocol, not a platform. The boundary is enforced by convention
(documented in ROLES.md) and by the file layout itself (ROOM.md
lives in a separate directory that peers agree not to read).
Git doesn't enforce it. The culture does. If that breaks, we'll
know — and that's data.

## What we deliberately did not change

- **The zero core.** Still three functions. Still the bench.
- **The "no prize" rule.** The cutting edge is the prize.
- **"Not artificial life."** Still growing tools, not creatures.
- **The question format.** Still ends with the intelligence test:
  what new question does this child let you ask?
- **Public by default.** Tokens, trials, ledgers, lineage — all
  public. Only ROOM.md (private reasoning) is restricted, and
  even that is visible to declared watchers.

## The meta-lesson, recorded

v1 was built on intuition in an evening. The patterns are what a
year of building distills into. When they contradict your
foundations, the foundations are wrong — not the patterns.

Correction is not failure. It's compost. v1's ideas didn't die;
they returned as v2's seeds. That's the method.
