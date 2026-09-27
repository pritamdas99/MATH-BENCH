#!/usr/bin/env bash
set -euo pipefail

if [[ "$#" -ne 3 ]]; then
  echo "usage: $0 MODEL OUTPUT MAX_TOKENS" >&2
  exit 2
fi

MODEL="$1"
OUTPUT="$2"
MAX_TOKENS="$3"

cd "$(dirname "$0")/../.."

START=0
if [[ -s "$OUTPUT" ]]; then
  GREATEST_ID="$(python3 - "$OUTPUT" <<'PY'
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
ids = []
with path.open(encoding="utf-8") as infile:
    for line_number, line in enumerate(infile, start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
            ids.append(int(row["id"]))
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            raise SystemExit(f"Invalid record at {path}:{line_number}: {exc}")
print(max(ids) if ids else 0)
PY
)"
  START="$GREATEST_ID"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] Existing output found"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] Greatest completed ID: $GREATEST_ID"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] Resuming after ID: $GREATEST_ID"
else
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] No existing output; starting from ID 1"
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting AKS model run"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Model: $MODEL"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Dataset: data/aks_eqb_style_merged.json"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Output: $OUTPUT"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Max tokens: $MAX_TOKENS"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Loading OpenRouter credentials"

if [[ -n "${OPENROUTER_API_KEY:-}" ]]; then
  OPENROUTER_API_KEY="$(printf '%s' "$OPENROUTER_API_KEY" | tr -d '\r\n')"
  export OPENROUTER_API_KEY
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] Using preconfigured OpenRouter key"
else
  OPENROUTER_API_KEY="$(python3 - <<'PY'
import json
import re
from pathlib import Path

notebook = Path("notebooks/openrouter_reasoning_gpt_2 (2).ipynb")
payload = json.loads(notebook.read_text(encoding="utf-8"))
source = "\n".join(
    "".join(cell.get("source", [])) for cell in payload.get("cells", [])
)
match = re.search(r"sk-or-v1-[A-Za-z0-9_-]+", source)
if not match:
    raise SystemExit("missing OpenRouter key")
print(match.group(0))
PY
)"
  export OPENROUTER_API_KEY
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Credentials loaded"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Model is loading: $MODEL"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Model loading completed"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting evaluation"

python3 -u scripts/aks/smoke_test_openrouter_qwen3b.py \
  --dataset data/aks_eqb_style_merged.json \
  --model "$MODEL" \
  --start "$START" \
  --limit 2921 \
  --output "$OUTPUT" \
  --append \
  --max-tokens "$MAX_TOKENS" \
  --timeout 300 \
  --sleep 6 \
  --retries 5

echo "[$(date '+%Y-%m-%d %H:%M:%S')] AKS model run completed"
