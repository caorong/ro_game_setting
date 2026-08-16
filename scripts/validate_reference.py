#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = [
    "00-scope-and-version.md", "01-character-progression.md", "02-job-tree.md",
    "03-primary-and-derived-stats.md", "04-attack-speed.md", "05-hit-flee-critical.md",
    "06-physical-damage.md", "07-magic-damage.md", "08-defense.md",
    "09-element-size-race-class.md", "10-cast-delay-cooldown.md",
    "11-hp-sp-regeneration.md", "12-status-effects.md",
    "13-equipment-refine-cards.md", "14-monsters-exp-drops.md",
    "15-skills.md", "16-source-index.md", "17-known-uncertainties.md",
]

FORBIDDEN_JOBS = {
    "Rune_Knight", "Royal_Guard", "Warlock", "Sorcerer", "Ranger", "Minstrel", "Wanderer",
    "Arch_Bishop", "Sura", "Mechanic", "Genetic", "Guillotine_Cross", "Shadow_Chaser",
    "Dragon_Knight", "Imperial_Guard", "Arch_Mage", "Elemental_Master",
}

GENERATED_REQUIRED = [
    "README.md",
    "summary.json",
    "source-manifest.json",
    "skills/all_metadata.jsonl",
    "skills/catalog.jsonl",
    "skills/tree.jsonl",
    "skills/formulas.jsonl",
    "reference/jobs/README.md",
    "monsters/metadata.jsonl",
    "monsters/index.csv",
    "monsters/drops.jsonl",
    "monsters/skills.jsonl",
    "reference/monsters/README.md",
    "items/equipment.jsonl",
    "items/equipment.csv",
    "reference/items/README.md",
]


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def walk_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, child in value.items():
            yield from walk_strings(key)
            yield from walk_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_strings(child)


def validate_generated(root: Path, lock: dict, errors: list[str]) -> None:
    generated = root / "generated"
    if not generated.exists():
        # The hand-written reference can be validated before the generated catalog job runs.
        return
    for relative in GENERATED_REQUIRED:
        path = generated / relative
        if not path.is_file():
            errors.append(f"missing generated file: generated/{relative}")

    summary_path = generated / "summary.json"
    if summary_path.is_file():
        try:
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"invalid generated/summary.json: {exc}")
        else:
            if summary.get("ruleset") != "pre-renewal" or summary.get("build_mode") != "PRERE":
                errors.append("generated summary must be pre-renewal / PRERE")
            if summary.get("commit") != lock.get("commit"):
                errors.append("generated summary and source lock commit differ")
            counts = summary.get("counts", {})
            for key in ("skills_all_metadata", "skills_classic_catalog", "skill_formula_records", "classic_jobs"):
                value = counts.get(key, 0)
                if not isinstance(value, int) or value <= 0:
                    errors.append(f"generated count {key} must be positive")

    manifest_path = generated / "source-manifest.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"invalid generated/source-manifest.json: {exc}")
        else:
            if manifest.get("commit") != lock.get("commit") or manifest.get("mode") != "PRERE":
                errors.append("generated source manifest lock mismatch")
            for item in manifest.get("files", []):
                path = str(item.get("path", ""))
                if path.startswith("db/re/") or path.startswith("npc/re/"):
                    errors.append(f"Renewal source leaked into generated manifest: {path}")
                    break

    # JSONL integrity check without loading the complete catalogs into memory.
    for relative in ("skills/catalog.jsonl", "skills/formulas.jsonl", "monsters/metadata.jsonl", "items/equipment.jsonl"):
        path = generated / relative
        if not path.is_file():
            continue
        with path.open("r", encoding="utf-8") as handle:
            first = next((line for line in handle if line.strip()), None)
        if first is None:
            errors.append(f"generated catalog is empty: generated/{relative}")
            continue
        try:
            json.loads(first)
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSONL in generated/{relative}: {exc}")


def main() -> int:
    errors: list[str] = []
    manifest = load_yaml(ROOT / "manifest.yml")
    lock = load_yaml(ROOT / "data/sources/rathena.lock.yml")
    jobs = load_yaml(ROOT / "data/jobs/job_paths.yml")

    if manifest.get("ruleset") != "pre-renewal" or manifest.get("build_mode") != "PRERE":
        errors.append("manifest must be pre-renewal / PRERE")
    if lock.get("mode") != "PRERE":
        errors.append("source lock mode must be PRERE")
    if manifest.get("source_commit") != lock.get("commit"):
        errors.append("manifest and source lock commit differ")

    active_job_values = {"routes": jobs.get("routes", []), "expanded_routes": jobs.get("expanded_routes", [])}
    strings = set(walk_strings(active_job_values))
    leaked_jobs = sorted(FORBIDDEN_JOBS & strings)
    if leaked_jobs:
        errors.append("forbidden Renewal jobs in active job data: " + ", ".join(leaked_jobs))

    for path in ROOT.rglob("*.yml"):
        if "vendor/rathena" in path.as_posix():
            continue
        try:
            load_yaml(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"invalid YAML {path.relative_to(ROOT)}: {exc}")

    for name in REQUIRED_DOCS:
        if not (ROOT / "docs" / name).exists():
            errors.append(f"missing doc: docs/{name}")

    normalized_paths = [
        ROOT / "data/formulas", ROOT / "data/jobs", ROOT / "data/rules",
        ROOT / "data/skills", ROOT / "data/tables",
    ]
    for directory in normalized_paths:
        for path in directory.rglob("*"):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            if re.search(r"db/re/|npc/re/", text):
                errors.append(f"Renewal source path found in {path.relative_to(ROOT)}")

    validate_generated(ROOT, lock, errors)

    if errors:
        print("reference validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("reference validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
