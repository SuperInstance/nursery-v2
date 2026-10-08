# Trial: token-sufficiency

## What

A peer — not the parent, not a watcher — tries to predict the child's
behavior on a capability trial using ONLY its TOKEN.md. No room access.
No CHILD.md. Just the token.

This is the open experiment at the heart of v2: **can selective
breeding work on tokens alone?**

If peers can reliably predict behavior from tokens, then THE TOKEN is
right and v1 was sharing too much. If they can't, then breeding needs
the room — and THE TOKEN needs a boundary exception for breeding
systems.

We don't assume the answer. We test it.

## How to run

1. Pick a child with a completed TOKEN.md and at least one completed
   capability trial (with ledger).
2. A peer (a different parent/agent than the child's parent) reads
   ONLY the TOKEN.md.
3. The peer predicts: for the given trial input, what will the child
   output? What score range will it achieve? Which debts will it
   service?
4. Run the actual trial. Compare prediction to reality.
5. Score the *token*, not the child.

## Scoring the token

| Component | Points | What "better" means |
|-----------|--------|---------------------|
| Behavioral prediction | 0-4 | Did the peer correctly predict what the child would do? 4 = exact match on approach. 0 = peer was surprised by the approach. |
| Score prediction | 0-3 | Did the peer predict the score within ±1? 3 = yes. 0 = off by 3+. |
| Debt prediction | 0-3 | Did the peer correctly predict which debts would be serviced? 3 = all correct. 0 = missed the key debt. |

Total: 0-10. This scores the TOKEN.md's sufficiency, not the child's
capability.

## What the score means

- **8-10**: The token is sufficient. A peer can breed from this child
  without ever seeing the room. THE TOKEN holds for breeding.
- **5-7**: Partially sufficient. The token predicts the what but not
  the why-behind-the-what. Breeding works for performance, may miss
  for innovation.
- **0-4**: The token is insufficient. Peers cannot predict behavior
  without the room. Either the token is badly written (fix the token)
  or tokens are insufficient for breeding (revise the theory).

## The meta-rule

If a token scores 0-4, the FIRST hypothesis is "bad token," not "bad
theory." Rewrite the token with more mechanical detail and retest.
Only after three good-faith token rewrites still score 0-4 do we
conclude the theory needs revision.

This trial is how v2 corrects itself. It's the trial that tests the
trial framework.

## Replay

Standard ledger. The peer's predictions (written BEFORE the trial
run — timestamped), the actual trial output, the comparison. The
prediction step is attested (not recomputable — it's a human judgment).
The trial rerun is recomputable.
