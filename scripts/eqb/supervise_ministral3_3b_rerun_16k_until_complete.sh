#!/usr/bin/env bash
set -euo pipefail

OUTPUT="ministral3_3b_all_results_rerun_16k.jsonl"
RUN_PID_FILE="ministral3_3b_rerun_16k.pid"
SUPERVISOR_LOG="ministral3_3b_rerun_16k_supervisor.log"

count_records() {
  python3 - <<'PY'
import json
from pathlib import Path

path = Path("ministral3_3b_all_results_rerun_16k.jsonl")
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
}

total_records() {
  python3 - <<'PY'
from pathlib import Path
from smoke_test_openrouter_qwen3b import read_inline_xlsx

print(len(read_inline_xlsx(Path("eqb.xlsx"))))
PY
}

is_running() {
  [[ -s "$RUN_PID_FILE" ]] && kill -0 "$(cat "$RUN_PID_FILE")" 2>/dev/null
}

TOTAL="$(total_records)"
echo "$(date -Is) supervisor started; target records=$TOTAL" >> "$SUPERVISOR_LOG"

while true; do
  COUNT="$(count_records)"
  echo "$(date -Is) records=$COUNT/$TOTAL" >> "$SUPERVISOR_LOG"

  if (( COUNT >= TOTAL )); then
    echo "$(date -Is) complete" >> "$SUPERVISOR_LOG"
    exit 0
  fi

  if is_running; then
    sleep 60
    continue
  fi

  echo "$(date -Is) runner not active; restarting from record count $COUNT" >> "$SUPERVISOR_LOG"
  ./run_ministral3_3b_rerun_16k_remaining.sh >> ministral3_3b_rerun_16k.log 2>&1 || true
  sleep 10
done
