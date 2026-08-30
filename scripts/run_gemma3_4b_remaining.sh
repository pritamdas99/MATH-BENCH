#!/usr/bin/env bash
set -euo pipefail

export OPENROUTER_API_KEY="$(
python3 - <<'PY'
import json
import re

with open('openrouter_reasoning_gpt_2 (2).ipynb', encoding='utf-8') as f:
    nb = json.load(f)

source = '\n'.join(''.join(cell.get('source', [])) for cell in nb['cells'])
match = re.search(r'sk-or-v1-[A-Za-z0-9]+', source)
if not match:
    raise SystemExit('missing OpenRouter key')
print(match.group(0))
PY
)"

python3 smoke_test_openrouter_qwen3b.py \
  --model google/gemma-3-4b-it \
  --start 80 \
  --limit 448 \
  --output gemma3_4b_remaining_results.jsonl \
  --max-tokens 2048 \
  --timeout 180 \
  --sleep 6 \
  --retries 5
