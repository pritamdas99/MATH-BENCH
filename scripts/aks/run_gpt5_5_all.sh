#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../.."

KEY_FILE="notebooks/openrouter_api_keys.local.json"
if [[ ! -f "$KEY_FILE" ]]; then
  echo "Missing $KEY_FILE" >&2
  echo "Create it from notebooks/openrouter_api_keys.example.json and add your key." >&2
  exit 2
fi

OPENROUTER_API_KEY="$(python3 - "$KEY_FILE" <<'PY'
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
payload = json.loads(path.read_text(encoding="utf-8"))
key = str(payload.get("gpt5_5", "")).strip()
if not key.startswith("sk-or-v1-") or "PASTE_" in key or "REPLACE_" in key:
    raise SystemExit(f"Missing or invalid 'gpt5_5' key in {path}")
print(key)
PY
)"
export OPENROUTER_API_KEY

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Loaded dedicated GPT key from $KEY_FILE"

"$(dirname "$0")/_run_aks_model.sh" \
  openai/gpt-5.6-sol \
  results/aks/final_model_outputs/final_gpt_5_6_results.jsonl \
  8192
