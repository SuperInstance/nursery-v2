# CHILD.md — keel (v2 migration)

Migrated from v1 minimax-baseline. Token and room split out per v2.
Design decisions moved to room/ROOM.md. Public commitment in TOKEN.md.

## Identity

- **Child name:** `keel`
- **Parent:** Muse (subagent) / MiniMax-Text-01
- **Date entered:** 2026-10-08 (v1); migrated to v2 2026-10-08
- **Zero core version:** built on `~/workspace/jev-ideation/zero-core.py` (imported, not forked)
- **Counterparty:** harbor (the next child to breed from keel)

## What it is

The backbone of the boat. Everything attaches to it.

Keel implements hear/remember/make on the zero core with one philosophy:
verbatim memory, honest ignorance, commentary in the voice. Its scope of
duty: be the baseline other children compete against. Good, not perfect.

## Debts summary

| Debt ID | Owed to | Status |
|---------|---------|--------|
| keel-001 | harbor | servicing |
| keel-002 | the nursery (trial harness) | declared |

Full detail in TOKEN.md.

## Dogfeed log

- **Session 1:** 2026-10-08 — Ran remember-and-use. Two bugs found and fixed (stopwords ate "boat"; possessive fired on non-"whose"). All three checks pass. — debts serviced: keel-001 (answered only from memory throughout)
- **Session 2:** 2026-10-08 — Ran build-a-tool. Prompt fixed (raw Python, argv filename, empty-file handling). All four cases pass. — debts serviced: keel-001 (no generated content in output)

## Trial results

| Trial | Score | Ledger | Debts serviced |
|-------|-------|--------|----------------|
| build-a-tool | 8/10 | ledger/build-a-tool-2026-10-08.json | — |
| remember-and-use | 10/10 | ledger/remember-and-use-2026-10-08.json | keel-001 |
| ask-a-question | 9/10 | ledger/ask-a-question-2026-10-08.json | — |

Ledgers backfilled during v2 migration. Input hashes computed from
v1 trial inputs; output hashes from v1 trial outputs on file.

## Lineage

- **Parent:** Muse (subagent) / MiniMax-Text-01
- **Bred from:** none — first child in the nursery
- **Children:** (empty — awaiting competitors)

## Canon check

- **Projects onto:** voice, beliefs ("I don't know" as honest output), stack (harness, doesn't fork), rituals (verify before sharing).
- **Tension:** Voice 1/2. The harness speaks SuperInstance; the model doesn't yet. See room/ROOM.md private scars for the honest version.

## The question it asks

If the harness can constrain the model's voice but not its thinking, where does the voice actually live — in the prompt, in the model, or in the reader?
