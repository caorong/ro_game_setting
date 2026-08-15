#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "vendor/rathena"
GENERATED = ROOT / "generated"
LOCK = yaml.safe_load((ROOT / "data/sources/rathena.lock.yml").read_text(encoding="utf-8"))
COMMIT = LOCK["commit"]

from ro_pre_re.reference_builder import add_provenance, body, write_jsonl  # noqa: E402


def require(path: str) -> Path:
    value = VENDOR / path
    if not value.exists():
        raise FileNotFoundError(f"missing {value}; run scripts/sync_rathena.py first")
    return value


def build_jsonl(source: str, output: str) -> int:
    records = add_provenance(body(require(source)), source, COMMIT)
    return write_jsonl(GENERATED / output, records)


def build_skill_source_index() -> int:
    root = VENDOR / "src/map/skills"
    index: dict[str, list[str]] = {}
    if root.exists():
        for path in sorted(root.rglob("*.cpp")):
            relative = path.relative_to(VENDOR).as_posix()
            family = path.parent.name
            index.setdefault(family, []).append(relative)
    destination = GENERATED / "skills/source_index.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps({"commit": COMMIT, "families": index}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return sum(len(paths) for paths in index.values())


def main() -> int:
    GENERATED.mkdir(parents=True, exist_ok=True)
    counts = {
        "skills": build_jsonl("db/pre-re/skill_db.yml", "skills/metadata.jsonl"),
        "skill_tree": build_jsonl("db/pre-re/skill_tree.yml", "skills/tree.jsonl"),
        "job_stats": build_jsonl("db/pre-re/job_stats.yml", "jobs/stats.jsonl"),
        "job_aspd": build_jsonl("db/pre-re/job_aspd.yml", "jobs/aspd.jsonl"),
        "job_exp": build_jsonl("db/pre-re/job_exp.yml", "jobs/exp.jsonl"),
        "job_basepoints": build_jsonl("db/pre-re/job_basepoints.yml", "jobs/basepoints.jsonl"),
        "monsters": build_jsonl("db/pre-re/mob_db.yml", "monsters/metadata.jsonl"),
        "equipment": build_jsonl("db/pre-re/item_db_equip.yml", "items/equipment.jsonl"),
        "usable_items": build_jsonl("db/pre-re/item_db_usable.yml", "items/usable.jsonl"),
        "etc_items": build_jsonl("db/pre-re/item_db_etc.yml", "items/etc.jsonl"),
        "statuses": build_jsonl("db/pre-re/status.yml", "statuses/metadata.jsonl"),
        "refine_groups": build_jsonl("db/pre-re/refine.yml", "items/refine.jsonl"),
        "pets": build_jsonl("db/pre-re/pet_db.yml", "companions/pets.jsonl"),
        "homunculus": build_jsonl("db/pre-re/homunculus_db.yml", "companions/homunculus.jsonl"),
        "mercenaries": build_jsonl("db/pre-re/mercenary_db.yml", "companions/mercenaries.jsonl"),
        "skill_source_files": build_skill_source_index(),
    }
    summary = {"ruleset": "pre-renewal", "commit": COMMIT, "counts": counts}
    (GENERATED / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
