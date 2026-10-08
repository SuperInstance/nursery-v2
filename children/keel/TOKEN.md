# TOKEN.md — keel

## Token identity

- **Token name:** `keel/tally-v1`
- **Child:** keel
- **Committed:** 2026-10-08T06:00:00Z
- **Zero core version:** built on `~/workspace/jev-ideation/zero-core.py` (imported, not forked)

## The algorithm

- **Name:** verbatim-scan ternary
- **Inputs:** natural-language questions (string); spec JSON for make()
- **Outputs:** answers from memory.log with line-number citations, or "I don't know"; Python files with line-by-line comments for make()
- **Parameters:** stopwords list (default: articles + copulas only); noun-link threshold (default: proper nouns + words >3 chars); voice prompt template (fixed)
- **Deterministic:** yes for remember (keyword scan); no for make (model call, wooden horse in tests)

Hear: reads spec/question from stdin channel. Remember: appends JSON
lines to memory.log, verbatim, no summarization. Make: memory-scan
recall via keyword overlap + multi-hop noun expansion; answers only
from memory or "I don't know"; code generation via voice-constrained
prompt (raw Python, line-by-line comments, argv filename).

## Counterparty

- **Who this token is for:** harbor (the next child to breed from keel)
- **What they get:** a baseline that never hallucinates, with every
  answer traceable to a memory.log line number
- **Debt IDs:** keel-001, keel-002

## Declared debts

### Debt keel-001

- **Owed to:** harbor
- **Obligation:** Answer only from memory.log, never generate plausible content
- **Service mechanism:** Pre-output check — every claim traced to a memory.log line number; untraced claims replaced with "I don't know"
- **Inherited:** no
- **Status:** servicing

### Debt keel-002

- **Owed to:** the nursery (trial harness)
- **Obligation:** Every trial score carries a recomputable ledger
- **Service mechanism:** Ledger JSON written per trial run with input hash, code version, output hash
- **Inherited:** no
- **Status:** declared (v2 migration — ledgers being backfilled)

## Trial interface

- **Hear:** stdin JSON channel; accepts spec objects and question strings
- **Make:** writes Python files to builds/; returns path
- **Remember:** appends to memory.log (JSONL, append-only)

## Replay pointer

- **Ledger:** `ledger/<trial>-2026-10-08.json`
- **Code version:** migrated from v1 minimax-baseline (see git history)
