from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

import yaml


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as handle:
        data = yaml.safe_load(handle)
    return data or {}


def body(path: Path) -> list[dict[str, Any]]:
    data = load_yaml(path)
    value = data.get("Body", [])
    if not isinstance(value, list):
        raise ValueError(f"{path}: Body must be a list")
    return value


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
            count += 1
    return count


def add_provenance(records: Iterable[dict[str, Any]], source_path: str, source_commit: str) -> Iterable[dict[str, Any]]:
    for record in records:
        result = dict(record)
        result["_source"] = {"path": source_path, "commit": source_commit}
        yield result
