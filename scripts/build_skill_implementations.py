#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "vendor/rathena"
GENERATED = ROOT / "generated"
SKILL_SOURCE = VENDOR / "src/map/skills"
LOCK = yaml.safe_load((ROOT / "data/sources/rathena.lock.yml").read_text(encoding="utf-8"))
COMMIT = str(LOCK["commit"])
REPOSITORY = str(LOCK["repository"])
START_MARKER = "<!-- generated-skill-implementations:start -->"
END_MARKER = "<!-- generated-skill-implementations:end -->"
CASE_RE = re.compile(r"\bcase\s+([A-Z][A-Z0-9_]+)\s*:")
RETURN_RE = re.compile(r"return\s+std::make_unique<([A-Za-z_][A-Za-z0-9_]*)>")
METHOD_RE = re.compile(r"\b(Skill[A-Za-z0-9_]*)::([A-Za-z_][A-Za-z0-9_]*)\s*\(")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                value = json.loads(line)
                if isinstance(value, dict):
                    rows.append(value)
    return rows


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
            count += 1
    return count


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def factory_mappings() -> dict[str, str]:
    mappings: dict[str, str] = {}
    for path in sorted(SKILL_SOURCE.rglob("skill_factory_*.cpp")):
        pending: list[str] = []
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            cases = CASE_RE.findall(line)
            if cases:
                pending.extend(cases)
            match = RETURN_RE.search(line)
            if match and pending:
                implementation = match.group(1)
                for skill_name in pending:
                    mappings[skill_name] = implementation
                pending.clear()
            elif "default:" in line or ("break;" in line and not match):
                pending.clear()
    return mappings


def extract_method(lines: list[str], start: int) -> tuple[str, int]:
    open_line = None
    for index in range(start, min(len(lines), start + 12)):
        if "{" in lines[index]:
            open_line = index
            break
        if ";" in lines[index]:
            return lines[start].strip(), start
    if open_line is None:
        return lines[start].strip(), start

    depth = 0
    seen_open = False
    end = open_line
    for index in range(open_line, len(lines)):
        line = lines[index]
        # This intentionally mirrors source braces rather than attempting a full C++ parser.
        for character in line:
            if character == "{":
                depth += 1
                seen_open = True
            elif character == "}":
                depth -= 1
        end = index
        if seen_open and depth <= 0:
            break
        if end - start >= 180:
            break
    code = "\n".join(lines[start:end + 1]).rstrip()
    if end - start >= 180:
        code += "\n// ... method block truncated after 180 lines; use path and line range for the full source"
    return code, end


def method_index() -> tuple[dict[str, list[dict[str, Any]]], dict[str, list[dict[str, Any]]], dict[str, list[str]]]:
    by_class: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_file: dict[str, list[dict[str, Any]]] = defaultdict(list)
    normalized_files: dict[str, list[str]] = defaultdict(list)

    for path in sorted(SKILL_SOURCE.rglob("*.cpp")):
        relative = path.relative_to(VENDOR).as_posix()
        normalized_files[normalize(path.stem)].append(relative)
        if path.name.startswith("skill_factory_"):
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        index = 0
        while index < len(lines):
            match = METHOD_RE.search(lines[index])
            if not match:
                index += 1
                continue
            class_name, method_name = match.groups()
            code, end = extract_method(lines, index)
            record = {
                "path": relative,
                "class": class_name,
                "method": method_name,
                "start_line": index + 1,
                "end_line": end + 1,
                "code": code,
            }
            by_class[class_name].append(record)
            by_file[relative].append(record)
            index = max(index + 1, end + 1)
    return by_class, by_file, normalized_files


def inferred_files(skill: dict[str, Any], normalized_files: dict[str, list[str]]) -> list[str]:
    name = str(skill.get("Name", ""))
    suffix = name.split("_", 1)[1] if "_" in name else name
    keys = [normalize(suffix), normalize(str(skill.get("Description", "")))]
    result: list[str] = []
    for key in keys:
        if key and key in normalized_files:
            result.extend(normalized_files[key])
    return sorted(set(result))


def build_records() -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]], dict[str, int]]:
    classic = load_jsonl(GENERATED / "skills/catalog.jsonl")
    broad = {row.get("name"): row for row in load_jsonl(GENERATED / "skills/formulas.jsonl")}
    factories = factory_mappings()
    by_class, by_file, normalized_files = method_index()
    records: list[dict[str, Any]] = []
    coverage_counts: dict[str, int] = defaultdict(int)

    for skill in classic:
        name = str(skill.get("Name", ""))
        implementation_class = factories.get(name)
        methods: list[dict[str, Any]] = []
        files: list[str] = []
        mapping_source = None

        if implementation_class and implementation_class.startswith("Skill") and implementation_class not in {"SkillImpl"}:
            methods = by_class.get(implementation_class, [])
            files = sorted({method["path"] for method in methods})
            mapping_source = "skill-factory"

        if methods:
            coverage = "exact-class-methods"
        elif implementation_class:
            coverage = "generic-or-class-mapped"
        else:
            candidates = inferred_files(skill, normalized_files)
            inferred_methods: list[dict[str, Any]] = []
            for path in candidates:
                inferred_methods.extend(by_file.get(path, []))
            if inferred_methods:
                methods = inferred_methods
                files = sorted({method["path"] for method in methods})
                coverage = "filename-inferred-methods"
                mapping_source = "skill-name-or-description"
            elif broad.get(name, {}).get("source_files"):
                files = list(broad[name]["source_files"])
                coverage = "core-source-references"
            else:
                coverage = "metadata-only"

        broad_record = broad.get(name, {})
        record = {
            "id": skill.get("Id"),
            "name": name,
            "description": skill.get("Description"),
            "structured_description_zh": skill.get("structured_description_zh"),
            "jobs_direct": skill.get("jobs_direct", []),
            "jobs_effective": skill.get("jobs_effective", []),
            "coverage": coverage,
            "implementation_class": implementation_class,
            "mapping_source": mapping_source,
            "implementation_files": files,
            "methods": methods,
            "fallback_references": broad_record.get("references", []),
            "fallback_candidate_expressions": broad_record.get("candidate_expressions", []),
            "notes": [
                "exact-class-methods are complete method blocks mapped from rAthena skill factories",
                "filename-inferred-methods are matched from the skill name/description and should be reviewed before algebraic normalization",
                "core-source-references remain exact source locations when a legacy skill has no split implementation class",
                "final damage can still depend on the shared battle pipeline, status effects, target properties, item/card scripts and integer truncation",
            ],
            "_source": {
                "repository": REPOSITORY,
                "commit": COMMIT,
                "mode": "PRERE",
                "paths": files or broad_record.get("source_files", []),
            },
        }
        records.append(record)
        coverage_counts[coverage] += 1

    records.sort(key=lambda row: int(row.get("id", 0) or 0))
    return records, {row["name"]: row for row in records}, dict(sorted(coverage_counts.items()))


def markdown_escape(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def update_job_link(job: str) -> None:
    path = GENERATED / f"reference/jobs/{job}.md"
    if not path.is_file():
        return
    link_line = f"> 精确公式与实现：[查看 `{job}` 公式页](../skill-formulas/{job}.md)"
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if "精确公式与实现：" not in line]
    insert_at = 1
    for index, line in enumerate(lines):
        if line.startswith("> 规则集："):
            insert_at = index + 1
            break
    lines.insert(insert_at, link_line)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_pages(records_by_name: dict[str, dict[str, Any]]) -> int:
    source_dir = GENERATED / "skills/by_job"
    output_dir = GENERATED / "reference/skill-formulas"
    output_dir.mkdir(parents=True, exist_ok=True)
    index_lines = [
        "# Pre-Renewal 职业技能精确实现目录",
        "",
        f"> 来源：`{REPOSITORY}@{COMMIT}`。优先展示技能工厂映射到实现类后的完整方法块。",
        "",
    ]
    page_count = 0

    for source_path in sorted(source_dir.glob("*.json")):
        value = json.loads(source_path.read_text(encoding="utf-8"))
        job = str(value.get("job", source_path.stem))
        rows = [row for row in value.get("skills", []) if isinstance(row, dict) and row.get("direct")]
        index_lines.append(f"- [{job}]({job}.md) — {len(rows)} 个直接学习技能")
        lines = [
            f"# {job} 技能公式与实现",
            "",
            f"> Pre-Renewal / PRERE；来源提交：`{COMMIT}`。",
            "",
            "| ID | 技能 | 覆盖 | 实现类 | 文件 |",
            "|---:|---|---|---|---|",
        ]
        for row in rows:
            skill = row.get("skill", {})
            name = str(skill.get("Name", ""))
            record = records_by_name.get(name, {})
            lines.append(
                f"| {skill.get('Id', '')} | `{markdown_escape(name)}` / {markdown_escape(skill.get('Description', ''))} | "
                f"`{record.get('coverage', 'metadata-only')}` | `{record.get('implementation_class') or ''}` | "
                f"{markdown_escape(', '.join(record.get('implementation_files', [])))} |"
            )

        lines.extend(["", "## 详细公式与效果实现", ""])
        for row in rows:
            skill = row.get("skill", {})
            name = str(skill.get("Name", ""))
            record = records_by_name.get(name, {})
            lines.extend([
                f"### {skill.get('Description', name)} (`{name}`)",
                "",
                str(row.get("structured_description_zh", "")),
                "",
                f"- 覆盖：`{record.get('coverage', 'metadata-only')}`",
                f"- 实现类：`{record.get('implementation_class') or 'N/A'}`",
            ])
            files = record.get("implementation_files", [])
            if files:
                lines.append("- 实现文件：" + ", ".join(f"`{path}`" for path in files))

            methods = record.get("methods", [])
            if methods:
                for method in methods:
                    lines.extend([
                        "",
                        f"#### `{method.get('class')}::{method.get('method')}`",
                        "",
                        f"来源：`{method.get('path')}:{method.get('start_line')}-{method.get('end_line')}`",
                        "",
                        "```cpp",
                        str(method.get("code", "")).rstrip(),
                        "```",
                    ])
            else:
                fallback = record.get("fallback_candidate_expressions", [])[:16]
                if fallback:
                    lines.extend(["", "精确源码候选（该技能没有独立实现类）：", "", "```cpp"])
                    for candidate in fallback:
                        lines.append(f"// {candidate.get('path')}:{candidate.get('line')}")
                        lines.append(str(candidate.get("text", "")))
                    lines.append("```")
                else:
                    lines.extend([
                        "",
                        "> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。",
                    ])
            lines.append("")

        (output_dir / f"{job}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        update_job_link(job)
        page_count += 1

    (output_dir / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    return page_count


def update_marked_section(path: Path, content: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    block = f"{START_MARKER}\n{content.rstrip()}\n{END_MARKER}"
    if START_MARKER in text and END_MARKER in text:
        before, rest = text.split(START_MARKER, 1)
        _, after = rest.split(END_MARKER, 1)
        text = before.rstrip() + "\n\n" + block + after
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    path.write_text(text, encoding="utf-8")


def update_summary(records: int, pages: int, coverage: dict[str, int]) -> None:
    path = GENERATED / "summary.json"
    summary = json.loads(path.read_text(encoding="utf-8"))
    summary.setdefault("counts", {})["skill_implementations"] = {
        "records": records,
        "pages": pages,
        "coverage": coverage,
    }
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    update_marked_section(
        GENERATED / "README.md",
        "\n".join([
            "## 技能精确实现索引",
            "",
            f"- 经典职业技能记录：**{records}**",
            f"- 职业公式页：**{pages}**",
            f"- 覆盖分布：`{json.dumps(coverage, ensure_ascii=False, sort_keys=True)}`",
            "- 机器数据：`skills/classic_implementations.jsonl`",
            "- 浏览入口：`reference/skill-formulas/README.md`",
            "- 优先使用技能工厂映射后的完整类方法；没有独立实现类时再回退到通用战斗源码定位。",
        ]),
    )


def main() -> int:
    if not SKILL_SOURCE.is_dir():
        raise FileNotFoundError("missing split skill source; sync with --include-skill-source")
    records, records_by_name, coverage = build_records()
    record_count = write_jsonl(GENERATED / "skills/classic_implementations.jsonl", records)
    pages = build_pages(records_by_name)
    update_summary(record_count, pages, coverage)
    print(json.dumps({"records": record_count, "pages": pages, "coverage": coverage}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
