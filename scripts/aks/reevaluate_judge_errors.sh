#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
status=0
python3 -u scripts/aks/reevaluate_judge_errors.py "$@" || status=$?
python3 scripts/aks/report_equivalence_labels.py
exit "$status"
