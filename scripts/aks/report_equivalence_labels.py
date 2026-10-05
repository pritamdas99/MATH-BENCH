#!/usr/bin/env python3
"""Report existing equivalence labels and export GPT label-0 cases for review."""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / 'results/aks/equivalence_labels'
OUTPUT = ROOT / 'reports/aks/equivalence_labels'
DATASET = ROOT / 'data/aks_eqb_style_merged.json'


def indexed(rows, source):
    result = {}
    for row in rows:
        key = str(row['id'])
        if key in result:
            raise ValueError(f'Duplicate ID {key} in {source}')
        result[key] = row
    return result


def is_judge_error(row):
    return str(row.get('judge_reason', '')).startswith('judge_error:')


def stats(model, rows, **extra):
    counts = Counter(row['label'] for row in rows)
    total = len(rows)
    return dict(model=model, **extra, total=total, correct=counts[1],
                incorrect=counts[0], judge_errors=sum(is_judge_error(row) for row in rows), accuracy=counts[1] / total,
                accuracy_percent=round(100 * counts[1] / total, 4))


def write_table(name, rows):
    (OUTPUT / f'{name}.json').write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with (OUTPUT / f'{name}.csv').open('w', encoding='utf-8', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    dataset = indexed(json.loads(DATASET.read_text(encoding='utf-8')), DATASET)
    overall, chapters, review = [], [], []
    raw_path = ROOT / 'results/aks/final_model_outputs/final_gpt_5_6_results.jsonl'
    raw_gpt = indexed([json.loads(line) for line in raw_path.read_text(encoding='utf-8').splitlines() if line.strip()], raw_path)
    paths = sorted(INPUT.glob('*.jsonl'))
    if not paths:
        raise ValueError('No label files found')
    for path in paths:
        rows = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
        by_id = indexed(rows, path)
        if set(by_id) != set(dataset):
            raise ValueError(f'Dataset ID coverage mismatch in {path}')
        grouped = defaultdict(list)
        for key, row in by_id.items():
            if type(row.get('label')) is not int or row['label'] not in (0, 1):
                raise ValueError(f'Invalid label in {path}, ID {key}')
            source = dataset[key]
            if row['expected_final_answer'] != source['FinalAnswer']:
                raise ValueError(f'Reference answer mismatch in {path}, ID {key}')
            chapter = source['ChapterName']
            if not chapter:
                raise ValueError(f'Missing chapter for ID {key}')
            grouped[chapter].append(row)
            if path.stem == 'gpt_5_6' and row['label'] == 0:
                review.append(dict(problem_id=key, question=source['Question'],
                    detailed_answer=source['DetailedAnswer'],
                    predicted_answer=row['predicted_answer'] if 'predicted_answer' in row else raw_gpt[key]['predicted_answer'], final_answer=source['FinalAnswer'],
                    chaptername=chapter, predicted_final_answer=row['predicted_final_answer'], label=0, judge_error=is_judge_error(row)))
        overall.append(stats(path.stem, rows))
        for chapter, items in grouped.items():
            chapters.append(stats(path.stem, items, chaptername=chapter))
    overall.sort(key=lambda row: row['accuracy'], reverse=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_table('overall_accuracy', overall)
    write_table('chapter_accuracy', chapters)
    with (OUTPUT / 'gpt_5_6_label_0_review.jsonl').open('w', encoding='utf-8') as out:
        for row in review:
            out.write(json.dumps(row, ensure_ascii=False) + '\n')
    lines = ['# AKS equivalence-label accuracy report', '',
        'Source: `results/aks/equivalence_labels/*.jsonl`. Chapters and reference solutions: '
        '`data/aks_eqb_style_merged.json`.', '',
        'Accuracy = label-1 count / total labeled results. Label 0 means incorrect according '
        'to the current equivalence labels. Judge-error repairs, when present, are included. All model files cover '
        f'the same {len(dataset):,} unique problems. Counts include every label, including any truncated responses.', '',
        'Any remaining judge errors retain their saved labels and are counted separately and flagged in the review export. They are not confirmed model mistakes. Repair backups and audit logs are under `repair_runs/`.', '', '## Overall accuracy', '', '| Model | Total | Correct | Incorrect | Judge errors | Accuracy |',
        '| --- | ---: | ---: | ---: | ---: | ---: |']
    for row in overall:
        lines.append(f"| {row['model']} | {row['total']} | {row['correct']} | {row['incorrect']} | {row['judge_errors']} | {row['accuracy_percent']:.2f}% |")
    models = [row['model'] for row in overall]
    chapter_names = list(dict.fromkeys(source['ChapterName'] for source in dataset.values()))
    chapter_stats = {(row['chaptername'], row['model']): row for row in chapters}
    lines += ['', '## Chapter accuracy by model', '',
              '| Chapter | ' + ' | '.join(models) + ' |',
              '| --- | ' + ' | '.join('---:' for _ in models) + ' |']
    for chapter in chapter_names:
        cells = [f"{chapter_stats[(chapter, model)]['accuracy_percent']:.2f}%" for model in models]
        lines.append('| ' + chapter.replace('|', '\\|') + ' | ' + ' | '.join(cells) + ' |')
    lines += ['', '## Chapter accuracy', '']
    for model in [row['model'] for row in overall]:
        lines += [f'### {model}', '', '| Chapter | Total | Correct | Incorrect | Judge errors | Accuracy |',
                  '| --- | ---: | ---: | ---: | ---: | ---: |']
        for row in chapters:
            if row['model'] == model:
                lines.append(f"| {row['chaptername']} | {row['total']} | {row['correct']} | {row['incorrect']} | {row['judge_errors']} | {row['accuracy_percent']:.2f}% |")
        lines.append('')
    lines += ['## Manual review export', '',
        f'`gpt_5_6_label_0_review.jsonl` contains all {len(review)} GPT label-0 cases in source order.', '',
        '- `problem_id`: original problem ID.',
        '- `question`: dataset question.',
        '- `detailed_answer`: dataset reference worked solution.',
        '- `predicted_answer`: complete model response, preserved verbatim.',
        '- `final_answer`: dataset reference final answer.',
        '- `chaptername`: dataset chapter name.',
        '- `predicted_final_answer`: extracted model final answer from the label file.',
        '- `label`: current equivalence label (0).',
        '- `judge_error`: whether the label resulted from a judge error.', '',
        'Missing full responses are recovered by ID from `results/aks/final_model_outputs/final_gpt_5_6_results.jsonl`.', '',
        'CSV and JSON reports contain accuracy as both a fraction and a percentage. '
        'Regenerate with `python3 scripts/aks/report_equivalence_labels.py`.', '']
    (OUTPUT / 'accuracy_report.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps(dict(overall=overall, chapter_rows=len(chapters), review_cases=len(review)), indent=2))


if __name__ == '__main__':
    main()
