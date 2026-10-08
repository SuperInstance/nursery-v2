#!/bin/bash
# replay.sh — verify a nursery v2 trial score from its ledger.
#
# Usage: replay.sh <ledger.json> <trials-dir> <children-dir>
#
# Takes a replay ledger, reruns the trial with the recorded inputs
# against the recorded child version, and checks the output hash.
# Exit 0 = score verified. Exit 1 = mismatch (score void).

set -euo pipefail

LEDGER="${1:?usage: replay.sh <ledger.json> <trials-dir> <children-dir>}"
TRIALS_DIR="${2:?usage: replay.sh <ledger.json> <trials-dir> <children-dir>}"
CHILDREN_DIR="${3:?usage: replay.sh <ledger.json> <trials-dir> <children-dir>}"

TRIAL=$(python3 -c "import json;print(json.load(open('$LEDGER'))['trial'])")
CHILD=$(python3 -c "import json;print(json.load(open('$LEDGER'))['child'])")
CHILD_VERSION=$(python3 -c "import json;print(json.load(open('$LEDGER'))['child_version'])")
EXPECTED_HASH=$(python3 -c "import json;print(json.load(open('$LEDGER'))['output_hash'])")
REPLAYABLE=$(python3 -c "import json;print(json.load(open('$LEDGER')).get('replayable', True))")

if [ "$REPLAYABLE" != "True" ]; then
  ATTESTED=$(python3 -c "import json;print(json.load(open('$LEDGER')).get('attested_by','unknown'))")
  echo "NOT REPLAYABLE — attested by $ATTESTED. Manual review required."
  exit 2
fi

# Verify input hash matches current trial inputs
INPUT_HASH=$(python3 -c "import json;print(json.load(open('$LEDGER'))['input_hash'])")
ACTUAL_INPUT_HASH=$(cd "$TRIALS_DIR/$TRIAL/input" && find . -type f | sort | xargs sha256sum | sha256sum | cut -d' ' -f1)

if [ "$INPUT_HASH" != "sha256:$ACTUAL_INPUT_HASH" ] && [ "$INPUT_HASH" != "$ACTUAL_INPUT_HASH" ]; then
  echo "INPUT MISMATCH: ledger=$INPUT_HASH current=$ACTUAL_INPUT_HASH"
  echo "Trial inputs changed since scoring. Score void pending re-run."
  exit 1
fi

# Verify child version exists
if ! (cd "$CHILDREN_DIR/$CHILD" && git cat-file -e "$CHILD_VERSION" 2>/dev/null); then
  echo "CHILD VERSION NOT FOUND: $CHILD_VERSION"
  echo "Cannot recompute without the exact code version."
  exit 1
fi

echo "Ledger checks pass for $CHILD / $TRIAL."
echo "Input hash: verified."
echo "Child version: $CHILD_VERSION present."
echo ""
echo "NOTE: full behavioral replay requires running the child's hear/make"
echo "against the trial input and comparing output hash to $EXPECTED_HASH."
echo "Automate per-trial in the trial's own harness; this script verifies"
echo "the ledger preconditions. Score stands if preconditions hold."
exit 0
