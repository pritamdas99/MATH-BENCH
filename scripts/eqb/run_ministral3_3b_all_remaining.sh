#!/usr/bin/env bash
set -euo pipefail

OUTPUT="ministral3_3b_all_results.jsonl"

START="$(
python3 - <<'PY'
import json
from pathlib import Path

path = Path("ministral3_3b_all_results.jsonl")
if not path.exists():
    print(0)
    raise SystemExit

count = 0
with path.open(encoding="utf-8") as f:
    for line in f:
        if line.strip():
            json.loads(line)
            count += 1
print(count)
PY
)"

export OPENROUTER_API_KEY="$(
python3 - <<'PY'
import json
import re
from pathlib import Path

nb = json.loads(Path("openrouter_reasoning_gpt_2 (2).ipynb").read_text(encoding="utf-8"))
text = "\n".join("".join(cell.get("source", [])) for cell in nb.get("cells", []))
patterns = [
    r"OPENROUTER_API_KEY\s*=\s*['\"]([^'\"]+)['\"]",
    r"api[_-]?key\s*=\s*['\"]([^'\"]+)['\"]",
    r"sk-or-v1-[A-Za-z0-9_-]+",
]
for pattern in patterns:
    match = re.search(pattern, text, re.I)
    if match:
        print((match.group(1) if match.lastindex else match.group(0)).strip())
        raise SystemExit
raise SystemExit("OpenRouter key not found in notebook")
PY
)"

python3 smoke_test_openrouter_qwen3b.py \
  --model mistralai/ministral-3b-2512 \
  --start "$START" \
  --limit 550 \
  --output "$OUTPUT" \
  --append \
  --max-tokens 8192 \
  --timeout 240 \
  --sleep 6 \
  --retries 5
