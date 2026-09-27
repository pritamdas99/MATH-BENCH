import glob
import json
import os
import pandas as pd

pattern = "research*cropped.jsonl"
files = sorted(glob.glob(pattern))

if not files:
    print(f"No JSONL files found matching '{pattern}' in {os.getcwd()}")
    raise SystemExit(1)

for jsonl_file in files:
    records = []
    with open(jsonl_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))

    if not records:
        print(f"Skipping empty file: {jsonl_file}")
        continue

    df = pd.json_normalize(records)
    csv_file = os.path.splitext(jsonl_file)[0] + ".csv"
    df.to_csv(csv_file, index=False, encoding="utf-8-sig")
    print(f"Converted {jsonl_file} -> {csv_file}")

print("Conversion complete.")