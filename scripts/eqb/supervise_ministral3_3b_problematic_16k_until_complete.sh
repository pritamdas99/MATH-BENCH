#!/usr/bin/env bash
set -euo pipefail

OUTPUT="ministral3_3b_problematic_rerun_16k.jsonl"
RUN_PID_FILE="ministral3_3b_problematic_rerun_16k.pid"
SUPERVISOR_LOG="ministral3_3b_problematic_rerun_16k_supervisor.log"

count_records() {
  python3 - <<'PY'
import json
from pathlib import Path

path = Path("ministral3_3b_problematic_rerun_16k.jsonl")
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

target_records() {
  python3 - <<'PY'
import json

records = [
    json.loads(line)
    for line in open("ministral3_3b_all_results.jsonl", encoding="utf-8")
    if line.strip()
]
print(sum(1 for record in records if record.get("finish_reason") != "stop"))
PY
}

is_running() {
  [[ -s "$RUN_PID_FILE" ]] && kill -0 "$(cat "$RUN_PID_FILE")" 2>/dev/null
}

TOTAL="$(target_records)"
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

  echo "$(date -Is) runner not active; restarting from completed count $COUNT" >> "$SUPERVISOR_LOG"
  ./rerun_ministral3_3b_problematic_16k.py >> ministral3_3b_problematic_rerun_16k.log 2>&1 || true
  sleep 10
done
