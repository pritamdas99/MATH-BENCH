#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../.."

if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
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
key = str(payload.get("gemma3_4b", "")).strip()
if not key.startswith("sk-or-v1-") or "PASTE_" in key or "REPLACE_" in key:
    raise SystemExit(f"Missing or invalid 'gemma3_4b' key in {path}")
print(key)
PY
)"
  export OPENROUTER_API_KEY

  echo "[$(date '+%Y-%m-%d %H:%M:%S')] Loaded dedicated Gemma-3-4B key from $KEY_FILE"
fi

# Allow temporary shared-provider overloads to clear before giving up.
export AKS_HTTP_RETRIES="${AKS_HTTP_RETRIES:-12}"
export AKS_REQUEST_SLEEP="${AKS_REQUEST_SLEEP:-15}"

scripts/aks/_run_aks_model.sh \
  google/gemma-3-4b-it \
  results/aks/final_model_outputs/final_gemma3_4b_results.jsonl \
  4096
