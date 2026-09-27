#!/usr/bin/env python3
"""Convert the EQB workbook to the repository's dataset JSON format.

This uses only the Python standard library and supports the inline strings used
by ``data/eqb.xlsx``.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from xml.etree import ElementTree
from zipfile import ZipFile


INPUT_PATH = Path("data/eqb.xlsx")
OUTPUT_PATH = Path("data/eqb.json")
EXPECTED_COLUMNS = (
    "id",
    "ChapterName",
    "Question",
    "DetailedAnswer",
    "FinalAnswer",
    "Source",
)
XML_NAMESPACE = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def cell_text(cell: ElementTree.Element) -> str:
    inline_string = cell.find("main:is", XML_NAMESPACE)
    if inline_string is not None:
        return "".join(
            text.text or ""
            for text in inline_string.iterfind(".//main:t", XML_NAMESPACE)
        )

    value = cell.find("main:v", XML_NAMESPACE)
    return "" if value is None else value.text or ""


def read_records(path: Path) -> list[dict[str, str]]:
    with ZipFile(path) as workbook:
        sheet = ElementTree.fromstring(workbook.read("xl/worksheets/sheet1.xml"))

    rows: list[dict[str, str]] = []
    for row in sheet.findall(".//main:sheetData/main:row", XML_NAMESPACE):
        values: dict[str, str] = {}
        for cell in row.findall("main:c", XML_NAMESPACE):
            reference = cell.attrib["r"]
            column = re.match(r"[A-Z]+", reference)
            if column is None:
                raise ValueError(f"Invalid cell reference: {reference}")
            values[column.group()] = cell_text(cell)
        rows.append(values)

    columns = tuple(rows[0].get(column, "") for column in "ABCDEF")
    if columns != EXPECTED_COLUMNS:
        raise ValueError(f"Unexpected columns: {columns}")

    records = [
        {name: row.get(column, "") for name, column in zip(columns, "ABCDEF")}
        for row in rows[1:]
    ]
    if any(not record[field] for record in records for field in EXPECTED_COLUMNS):
        raise ValueError("The workbook contains an empty required field")
    if any(record["Source"] != "eqb" for record in records):
        raise ValueError("Every record must have Source set to 'eqb'")
    return records


def main() -> None:
    records = read_records(INPUT_PATH)
    OUTPUT_PATH.write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(records)} records to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
