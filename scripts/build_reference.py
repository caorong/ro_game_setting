#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import shutil
from collections import OrderedDict, defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "vendor/rathena"
GENERATED = ROOT / "generated"
LOCK = yaml.safe_load((ROOT / "data/sources/rathena.lock.yml").read_text(encoding="utf-8"))
COMMIT = str(LOCK["commit"])
REPOSITORY = str(LOCK["repository"])

CORE_SOURCE_PATHS = (
    "src/map/battle.cpp",
    "src/map/skill.cpp",
    "src/map/status.cpp",
    "src/map/pc.cpp",
    "src/map/itemdb.cpp",
    "src/map/mob.cpp",
)
SOURCE_INTEREST = re.compile(
    r"skillratio|damage|\.damage|ratio|skill_lv|status_change|sc_start|duration|"
    r"rate|chance|heal|\bhp\b|\bsp\b|\batk\b|matk|\bdef\b|mdef|\bhit\b|"
    r"flee|\bcri\b|aspd|cast|delay|knockback|skill_get_time|skill_get_time2",
    re.IGNORECASE,
)
SKILL_TOKEN = re.compile(r"\b[A-Z][A-Z0-9]*_[A-Z0-9_]+\b")

TYPE_ZH = {
    "Weapon": "武器/物理",
    "Magic": "魔法",
    "Misc": "特殊",
    "None": "非伤害",
}
TARGET_ZH = {
    "Passive": "被动",
    "Attack": "敌方目标",
    "Self": "自身",
    "Support": "友方目标",
    "Ground": "地面区域",
    "Trap": "陷阱",
}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = yaml.safe_load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"expected mapping in {path}")
    return value


def require(path: str) -> Path:
    value = VENDOR / path
    if not value.exists():
        raise FileNotFoundError(f"missing {value}; run scripts/sync_rathena.py first")
    return value


def body(path: str) -> list[dict[str, Any]]:
    value = load_yaml(require(path)).get("Body", [])
    if not isinstance(value, list):
        raise ValueError(f"Body is not a list in {path}")
    return [row for row in value if isinstance(row, dict)]


def provenance(source: str) -> dict[str, str]:
    return {
        "repository": REPOSITORY,
        "commit": COMMIT,
        "mode": "PRERE",
        "path": source,
    }


def add_provenance(records: Iterable[dict[str, Any]], source: str) -> list[dict[str, Any]]:
    source_info = provenance(source)
    return [{**record, "_source": source_info} for record in records]


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
            count += 1
    return count


def write_csv(path: Path, rows: Iterable[dict[str, Any]], fieldnames: list[str]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
            count += 1
    return count


def clean_generated() -> None:
    if GENERATED.exists():
        shutil.rmtree(GENERATED)
    GENERATED.mkdir(parents=True, exist_ok=True)


def first_value_key(row: dict[str, Any]) -> str | None:
    for key in row:
        if key != "Level":
            return key
    return None


def compact_level_value(value: Any) -> str:
    if value is None:
        return ""
    if not isinstance(value, list):
        if isinstance(value, dict):
            enabled = [str(key) for key, child in value.items() if child]
            return ", ".join(enabled) if enabled else json.dumps(value, ensure_ascii=False)
        return str(value)

    points: list[tuple[int, Any]] = []
    for row in value:
        if not isinstance(row, dict) or "Level" not in row:
            continue
        key = first_value_key(row)
        if key is None:
            continue
        try:
            level = int(row["Level"])
        except (TypeError, ValueError):
            continue
        points.append((level, row[key]))
    if not points:
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))

    points.sort(key=lambda pair: pair[0])
    groups: list[tuple[int, int, Any]] = []
    start = previous = points[0][0]
    current = points[0][1]
    for level, child in points[1:]:
        if child == current and level == previous + 1:
            previous = level
            continue
        groups.append((start, previous, current))
        start = previous = level
        current = child
    groups.append((start, previous, current))
    rendered = []
    for start, end, child in groups:
        prefix = f"Lv{start}" if start == end else f"Lv{start}-{end}"
        rendered.append(f"{prefix}={child}")
    return "; ".join(rendered)


def render_map(value: Any) -> str:
    if not isinstance(value, dict):
        return compact_level_value(value)
    return ", ".join(str(key) for key, child in value.items() if child)


def requirement_summary(requires: Any) -> str:
    if not isinstance(requires, dict):
        return ""
    parts: list[str] = []
    labels = {
        "HpCost": "HP",
        "SpCost": "SP",
        "ApCost": "AP",
        "HpRateCost": "HP%",
        "SpRateCost": "SP%",
        "ZenyCost": "Zeny",
        "AmmoAmount": "弹药数",
        "SpiritSphereCost": "气弹",
    }
    for key, label in labels.items():
        if key in requires:
            parts.append(f"{label} {compact_level_value(requires[key])}")
    for key, label in (("Weapon", "武器"), ("Ammo", "弹药"), ("State", "状态"), ("Status", "前置状态"), ("Equipment", "装备")):
        if key in requires:
            rendered = render_map(requires[key])
            if rendered:
                parts.append(f"{label} {rendered}")
    item_cost = requires.get("ItemCost")
    if isinstance(item_cost, list):
        items = []
        for row in item_cost:
            if not isinstance(row, dict):
                continue
            item = row.get("Item", "?")
            amount = row.get("Amount", 1)
            level = row.get("Level")
            suffix = f"@Lv{level}" if level is not None else ""
            items.append(f"{item}×{amount}{suffix}")
        if items:
            parts.append("道具 " + ", ".join(items))
    return "；".join(parts)


def structured_skill_description(skill: dict[str, Any]) -> str:
    target = str(skill.get("TargetType", "Passive"))
    skill_type = str(skill.get("Type", "None"))
    parts = [f"{TYPE_ZH.get(skill_type, skill_type)}技能", f"目标：{TARGET_ZH.get(target, target)}"]
    if "MaxLevel" in skill:
        parts.append(f"最高等级 {skill['MaxLevel']}")
    for key, label in (
        ("Range", "射程"),
        ("Hit", "命中类型"),
        ("HitCount", "段数"),
        ("Element", "属性"),
        ("SplashArea", "范围"),
        ("Knockback", "击退"),
        ("CastTime", "吟唱"),
        ("AfterCastActDelay", "技能后摇"),
        ("AfterCastWalkDelay", "移动后摇"),
        ("Cooldown", "冷却"),
        ("Duration1", "持续时间1"),
        ("Duration2", "持续时间2"),
    ):
        if key in skill:
            rendered = compact_level_value(skill[key])
            if rendered:
                unit = " ms" if key in {"CastTime", "AfterCastActDelay", "AfterCastWalkDelay", "Cooldown", "Duration1", "Duration2"} else ""
                parts.append(f"{label}：{rendered}{unit}")
    if skill.get("DamageFlags"):
        parts.append("伤害标记：" + render_map(skill["DamageFlags"]))
    requirements = requirement_summary(skill.get("Requires"))
    if requirements:
        parts.append("消耗/限制：" + requirements)
    if skill.get("Status"):
        parts.append(f"关联状态：{skill['Status']}")
    return "；".join(parts) + "。"


def collect_allowed_jobs(job_paths: dict[str, Any], available_jobs: set[str]) -> set[str]:
    allowed: set[str] = set()
    for family in job_paths.get("routes", []):
        if not isinstance(family, dict):
            continue
        for path in family.get("paths", []):
            if isinstance(path, list):
                allowed.update(str(job) for job in path)
        for value in family.get("rebirth_bridge", []):
            if isinstance(value, str):
                allowed.update(part for part in value.split("|") if part)
    for path in job_paths.get("expanded_routes", []):
        if isinstance(path, list):
            allowed.update(str(job) for job in path)
    technical = job_paths.get("technical_variants", {})
    if isinstance(technical, dict):
        for key in ("mounted", "high_first"):
            value = technical.get(key, [])
            if isinstance(value, list):
                allowed.update(str(job) for job in value)

    # Include technical Baby variants only when their canonical job is in scope.
    for job in available_jobs:
        canonical = job
        if job == "Baby":
            canonical = "Novice"
        elif job == "Super_Baby":
            canonical = "Super_Novice"
        elif job.startswith("Baby_"):
            canonical = job[len("Baby_"):]
        if canonical in allowed:
            allowed.add(job)
    return allowed & available_jobs


def skill_tree_catalog(
    skills: list[dict[str, Any]], trees: list[dict[str, Any]], job_paths: dict[str, Any]
) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]], set[str]]:
    skill_by_name = {str(row.get("Name")): row for row in skills if row.get("Name")}
    tree_by_job = {str(row.get("Job")): row for row in trees if row.get("Job")}
    allowed_jobs = collect_allowed_jobs(job_paths, set(tree_by_job))
    by_job: dict[str, list[dict[str, Any]]] = {}
    global_jobs_direct: dict[str, list[str]] = defaultdict(list)
    global_jobs_effective: dict[str, list[str]] = defaultdict(list)

    for job in sorted(allowed_jobs):
        node = tree_by_job[job]
        merged: OrderedDict[str, dict[str, Any]] = OrderedDict()
        inherit = node.get("Inherit", {})
        if isinstance(inherit, dict):
            for parent, enabled in inherit.items():
                if not enabled or parent not in tree_by_job:
                    continue
                for entry in tree_by_job[parent].get("Tree", []) or []:
                    if not isinstance(entry, dict) or entry.get("Exclude") or not entry.get("Name"):
                        continue
                    name = str(entry["Name"])
                    merged[name] = {**entry, "origin_job": parent, "direct": False}
        for entry in node.get("Tree", []) or []:
            if not isinstance(entry, dict) or not entry.get("Name"):
                continue
            name = str(entry["Name"])
            if int(entry.get("MaxLevel", 1) or 0) <= 0:
                merged.pop(name, None)
                continue
            merged[name] = {**entry, "origin_job": job, "direct": True}
            global_jobs_direct[name].append(job)

        rows: list[dict[str, Any]] = []
        for name, tree_entry in merged.items():
            metadata = skill_by_name.get(name, {"Name": name})
            row = {
                "job": job,
                "origin_job": tree_entry["origin_job"],
                "direct": tree_entry["direct"],
                "tree": {key: value for key, value in tree_entry.items() if key not in {"origin_job", "direct"}},
                "skill": metadata,
                "structured_description_zh": structured_skill_description(metadata),
            }
            rows.append(row)
            global_jobs_effective[name].append(job)
        by_job[job] = rows

    catalog = []
    for skill in sorted(skills, key=lambda row: int(row.get("Id", 0) or 0)):
        name = str(skill.get("Name", ""))
        if name not in global_jobs_effective:
            continue
        catalog.append({
            **skill,
            "jobs_direct": sorted(global_jobs_direct.get(name, [])),
            "jobs_effective": sorted(global_jobs_effective.get(name, [])),
            "structured_description_zh": structured_skill_description(skill),
            "_source": provenance("db/pre-re/skill_db.yml"),
        })
    return catalog, by_job, allowed_jobs


def source_files() -> list[Path]:
    files: list[Path] = []
    skill_root = VENDOR / "src/map/skills"
    if skill_root.exists():
        files.extend(skill_root.rglob("*.cpp"))
        files.extend(skill_root.rglob("*.hpp"))
    for relative in CORE_SOURCE_PATHS:
        path = VENDOR / relative
        if path.exists():
            files.append(path)
    return sorted(set(files))


def formula_index(skills: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    names = {str(skill.get("Name")) for skill in skills if skill.get("Name")}
    references: dict[str, list[dict[str, Any]]] = defaultdict(list)
    expressions: dict[str, list[dict[str, Any]]] = defaultdict(list)
    expression_seen: dict[str, set[tuple[str, int, str]]] = defaultdict(set)

    for path in source_files():
        relative = path.relative_to(VENDOR).as_posix()
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        line_tokens: dict[int, set[str]] = {}
        for number, line in enumerate(lines, 1):
            tokens = set(SKILL_TOKEN.findall(line)) & names
            if tokens:
                line_tokens[number] = tokens
                for name in tokens:
                    references[name].append({"path": relative, "line": number, "text": line.strip()})

        for number, tokens in line_tokens.items():
            start = max(1, number - 12)
            end = min(len(lines), number + 12)
            for candidate_number in range(start, end + 1):
                candidate = lines[candidate_number - 1].strip()
                if not candidate or candidate.startswith("//") or not SOURCE_INTEREST.search(candidate):
                    continue
                for name in tokens:
                    key = (relative, candidate_number, candidate)
                    if key in expression_seen[name]:
                        continue
                    expression_seen[name].add(key)
                    expressions[name].append({"path": relative, "line": candidate_number, "text": candidate})

    result: dict[str, dict[str, Any]] = {}
    for skill in skills:
        name = str(skill.get("Name", ""))
        refs = references.get(name, [])
        exprs = expressions.get(name, [])
        paths = sorted({item["path"] for item in refs})
        dedicated = [path for path in paths if path.startswith("src/map/skills/")]
        if dedicated:
            coverage = "dedicated-source"
        elif paths:
            coverage = "core-source"
        else:
            coverage = "metadata-only"
        result[name] = {
            "id": skill.get("Id"),
            "name": name,
            "description": skill.get("Description"),
            "coverage": coverage,
            "verification": "source-indexed" if paths else "metadata-only",
            "source_files": paths,
            "references": refs,
            "candidate_expressions": exprs,
            "notes": [
                "candidate_expressions are exact C++ source statements near references; they are not silently rewritten into algebra",
                "final behavior may also depend on battle.cpp, status.cpp, status effects, target type, equipment scripts and integer truncation",
            ],
            "_source": provenance("src/map/skills + src/map core battle files"),
        }
    return result


def render_prerequisites(tree: dict[str, Any]) -> str:
    requirements = tree.get("Requires")
    if not isinstance(requirements, list):
        return "—"
    parts = []
    for row in requirements:
        if isinstance(row, dict) and row.get("Name"):
            parts.append(f"{row['Name']} Lv{row.get('Level', 1)}")
    return ", ".join(parts) if parts else "—"


def markdown_escape(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def build_job_pages(by_job: dict[str, list[dict[str, Any]]], formulas: dict[str, dict[str, Any]]) -> int:
    directory = GENERATED / "reference/jobs"
    directory.mkdir(parents=True, exist_ok=True)
    index_lines = ["# Pre-Renewal 职业技能目录", "", f"> 数据基线：`{REPOSITORY}@{COMMIT}`，仅列入经典职业路线。", ""]
    for job, rows in sorted(by_job.items()):
        index_lines.append(f"- [{job}]({job}.md) — {len(rows)} 个有效技能（含继承）")
        lines = [
            f"# {job} 技能",
            "",
            f"> 规则集：Pre-Renewal / PRERE；来源提交：`{COMMIT}`。",
            "",
            "## 有效技能列表",
            "",
            "| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |",
            "|---:|---|---|---:|---|---|---|---|",
        ]
        for row in rows:
            skill = row["skill"]
            tree = row["tree"]
            lines.append(
                "| {id} | `{name}` | {desc} | {max_level} | {origin} | {direct} | {requires} | {kind} / {target} |".format(
                    id=skill.get("Id", ""),
                    name=markdown_escape(skill.get("Name", "")),
                    desc=markdown_escape(skill.get("Description", "")),
                    max_level=tree.get("MaxLevel", skill.get("MaxLevel", "")),
                    origin=row["origin_job"],
                    direct="是" if row["direct"] else "否",
                    requires=markdown_escape(render_prerequisites(tree)),
                    kind=markdown_escape(skill.get("Type", "None")),
                    target=markdown_escape(skill.get("TargetType", "Passive")),
                )
            )

        lines.extend(["", "## 技能详情", ""])
        for row in rows:
            if not row["direct"]:
                continue
            skill = row["skill"]
            name = str(skill.get("Name", ""))
            formula = formulas.get(name, {})
            lines.extend([
                f"### {skill.get('Description', name)} (`{name}`)",
                "",
                row["structured_description_zh"],
                "",
                f"- 技能树最高等级：`{row['tree'].get('MaxLevel', skill.get('MaxLevel', ''))}`",
                f"- 前置技能：{render_prerequisites(row['tree'])}",
                f"- 公式覆盖：`{formula.get('coverage', 'metadata-only')}` / `{formula.get('verification', 'metadata-only')}`",
            ])
            source_files_value = formula.get("source_files", [])
            if source_files_value:
                lines.append("- 实现文件：" + ", ".join(f"`{path}`" for path in source_files_value))
            candidates = formula.get("candidate_expressions", [])[:12]
            if candidates:
                lines.extend(["", "公式/效果候选源码（保持原始 C++ 表达式）：", "", "```cpp"])
                for candidate in candidates:
                    lines.append(f"// {candidate['path']}:{candidate['line']}")
                    lines.append(candidate["text"])
                lines.extend(["```", ""])
            else:
                lines.extend(["", "> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。", ""])
        (directory / f"{job}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    (directory / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    return len(by_job)


def flatten_monster(monster: dict[str, Any]) -> dict[str, Any]:
    drops = monster.get("Drops", []) if isinstance(monster.get("Drops"), list) else []
    mvp_drops = monster.get("MvpDrops", []) if isinstance(monster.get("MvpDrops"), list) else []
    return {
        "id": monster.get("Id"),
        "aegis_name": monster.get("AegisName"),
        "name": monster.get("Name"),
        "level": monster.get("Level", 1),
        "hp": monster.get("Hp", 1),
        "sp": monster.get("Sp", 1),
        "base_exp": monster.get("BaseExp", 0),
        "job_exp": monster.get("JobExp", 0),
        "attack_min": monster.get("Attack", 0),
        "attack_max": monster.get("Attack2", monster.get("Attack", 0)),
        "defense": monster.get("Defense", 0),
        "magic_defense": monster.get("MagicDefense", 0),
        "str": monster.get("Str", 1),
        "agi": monster.get("Agi", 1),
        "vit": monster.get("Vit", 1),
        "int": monster.get("Int", 1),
        "dex": monster.get("Dex", 1),
        "luk": monster.get("Luk", 1),
        "size": monster.get("Size", "Small"),
        "race": monster.get("Race", "Formless"),
        "element": monster.get("Element", "Neutral"),
        "element_level": monster.get("ElementLevel", 1),
        "attack_range": monster.get("AttackRange", 0),
        "walk_speed": monster.get("WalkSpeed"),
        "attack_delay": monster.get("AttackDelay", 0),
        "attack_motion": monster.get("AttackMotion", 0),
        "damage_motion": monster.get("DamageMotion", 0),
        "ai": monster.get("Ai", "06"),
        "class": monster.get("Class", "Normal"),
        "modes": render_map(monster.get("Modes", {})),
        "drop_count": len(drops),
        "mvp_drop_count": len(mvp_drops),
    }


def parse_mob_skills(path: Path) -> list[dict[str, Any]]:
    fields = [
        "mob_id", "label", "state", "skill_id", "skill_level", "rate", "cast_time", "delay",
        "cancelable", "target", "condition_type", "condition_value", "val1", "val2", "val3",
        "val4", "val5", "emotion", "chat",
    ]
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
        for raw in handle:
            stripped = raw.strip()
            if not stripped or stripped.startswith("//"):
                continue
            values = next(csv.reader([raw]))
            if len(values) < len(fields):
                values.extend([""] * (len(fields) - len(values)))
            record = dict(zip(fields, values[:len(fields)]))
            for key in ("mob_id", "skill_id", "skill_level", "rate", "cast_time", "delay"):
                try:
                    record[key] = int(str(record[key]).strip(), 0)
                except (TypeError, ValueError):
                    pass
            if isinstance(record.get("rate"), int):
                record["rate_percent"] = record["rate"] / 100
            record["_source"] = provenance("db/pre-re/mob_skill_db.txt")
            rows.append(record)
    return rows


def build_monsters(monsters: list[dict[str, Any]], mob_skills: list[dict[str, Any]]) -> dict[str, int]:
    source = "db/pre-re/mob_db.yml"
    raw_count = write_jsonl(GENERATED / "monsters/metadata.jsonl", add_provenance(monsters, source))
    flat = [flatten_monster(monster) for monster in monsters]
    csv_fields = list(flat[0].keys()) if flat else []
    csv_count = write_csv(GENERATED / "monsters/index.csv", flat, csv_fields) if csv_fields else 0
    skill_count = write_jsonl(GENERATED / "monsters/skills.jsonl", mob_skills)

    drops: list[dict[str, Any]] = []
    for monster in monsters:
        for kind, key in (("normal", "Drops"), ("mvp", "MvpDrops")):
            for drop in monster.get(key, []) or []:
                if not isinstance(drop, dict):
                    continue
                rate = drop.get("Rate", 0)
                drops.append({
                    "monster_id": monster.get("Id"),
                    "monster": monster.get("AegisName"),
                    "monster_name": monster.get("Name"),
                    "kind": kind,
                    "item": drop.get("Item"),
                    "rate": rate,
                    "rate_percent": (rate / 100) if isinstance(rate, (int, float)) else None,
                    "steal_protected": bool(drop.get("StealProtected", False)),
                    "random_option_group": drop.get("RandomOptionGroup"),
                    "_source": provenance(source),
                })
    drop_count = write_jsonl(GENERATED / "monsters/drops.jsonl", drops)

    skills_by_mob: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for row in mob_skills:
        mob_id = row.get("mob_id")
        if isinstance(mob_id, int):
            skills_by_mob[mob_id].append(row)

    pages: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for monster in monsters:
        monster_id = int(monster.get("Id", 0) or 0)
        pages[(monster_id // 100) * 100].append(monster)
    directory = GENERATED / "reference/monsters"
    directory.mkdir(parents=True, exist_ok=True)
    index_lines = ["# Pre-Renewal 怪物数据目录", "", f"> 完整数据：`generated/monsters/metadata.jsonl`；来源 `{REPOSITORY}@{COMMIT}`。", ""]
    for start, page_monsters in sorted(pages.items()):
        end = start + 99
        filename = f"{start:04d}-{end:04d}.md"
        index_lines.append(f"- [{start}-{end}]({filename}) — {len(page_monsters)} 个怪物")
        lines = [
            f"# 怪物 {start}-{end}", "",
            "| ID | 怪物 | Lv | HP | ATK | DEF/MDEF | 体型 | 种族 | 属性 | Base/Job EXP |",
            "|---:|---|---:|---:|---|---|---|---|---|---|",
        ]
        for monster in sorted(page_monsters, key=lambda row: int(row.get("Id", 0) or 0)):
            lines.append(
                f"| {monster.get('Id')} | {markdown_escape(monster.get('Name', ''))} (`{monster.get('AegisName', '')}`) | "
                f"{monster.get('Level', 1)} | {monster.get('Hp', 1)} | {monster.get('Attack', 0)}-{monster.get('Attack2', monster.get('Attack', 0))} | "
                f"{monster.get('Defense', 0)}/{monster.get('MagicDefense', 0)} | {monster.get('Size', 'Small')} | "
                f"{monster.get('Race', 'Formless')} | {monster.get('Element', 'Neutral')} {monster.get('ElementLevel', 1)} | "
                f"{monster.get('BaseExp', 0)}/{monster.get('JobExp', 0)} |"
            )
        lines.extend(["", "## 掉落与技能", ""])
        for monster in sorted(page_monsters, key=lambda row: int(row.get("Id", 0) or 0)):
            monster_id = int(monster.get("Id", 0) or 0)
            lines.append(f"### {monster.get('Name', monster.get('AegisName'))} (`{monster_id}`)")
            drops_value = monster.get("Drops", []) or []
            if drops_value:
                lines.append("")
                lines.append("掉落：")
                for drop in drops_value:
                    if isinstance(drop, dict):
                        rate = drop.get("Rate", 0)
                        percent = f"{rate / 100:.2f}%" if isinstance(rate, (int, float)) else str(rate)
                        lines.append(f"- `{drop.get('Item')}`：{rate}/10000（{percent}）")
            mob_skill_rows = skills_by_mob.get(monster_id, [])
            if mob_skill_rows:
                lines.append("")
                lines.append("技能 AI：")
                for row in mob_skill_rows:
                    lines.append(
                        f"- Skill `{row.get('skill_id')}` Lv{row.get('skill_level')}，状态 `{row.get('state')}`，"
                        f"概率 {row.get('rate')}/10000，吟唱 {row.get('cast_time')} ms，复用 {row.get('delay')} ms，"
                        f"目标 `{row.get('target')}`，条件 `{row.get('condition_type')}={row.get('condition_value')}`"
                    )
            lines.append("")
        (directory / filename).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    (directory / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    return {"records": raw_count, "csv_rows": csv_count, "drops": drop_count, "skill_rules": skill_count, "pages": len(pages)}


def item_category(item: dict[str, Any]) -> str:
    item_type = str(item.get("Type", "Etc"))
    if item_type == "Weapon":
        return "weapons"
    if item_type == "Armor":
        return "armor"
    if item_type == "Card":
        return "cards"
    if item_type == "Ammo":
        return "ammo"
    if item_type == "ShadowGear":
        return "shadow_gear"
    return item_type.lower()


def flatten_item(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": item.get("Id"),
        "aegis_name": item.get("AegisName"),
        "name": item.get("Name"),
        "type": item.get("Type", "Etc"),
        "sub_type": item.get("SubType"),
        "buy": item.get("Buy"),
        "sell": item.get("Sell"),
        "weight": item.get("Weight", 0),
        "attack": item.get("Attack", 0),
        "magic_attack": item.get("MagicAttack", 0),
        "defense": item.get("Defense", 0),
        "range": item.get("Range", 0),
        "slots": item.get("Slots", 0),
        "weapon_level": item.get("WeaponLevel"),
        "armor_level": item.get("ArmorLevel"),
        "equip_level_min": item.get("EquipLevelMin", 0),
        "equip_level_max": item.get("EquipLevelMax", 0),
        "refineable": bool(item.get("Refineable", False)),
        "jobs": render_map(item.get("Jobs", {"All": True})),
        "classes": render_map(item.get("Classes", {"All": True})),
        "gender": item.get("Gender", "Both"),
        "locations": render_map(item.get("Locations", {})),
        "script": item.get("Script", ""),
        "equip_script": item.get("EquipScript", ""),
        "unequip_script": item.get("UnEquipScript", ""),
    }


def build_items(items: list[dict[str, Any]]) -> dict[str, int]:
    source = "db/pre-re/item_db_equip.yml"
    raw_count = write_jsonl(GENERATED / "items/equipment.jsonl", add_provenance(items, source))
    categories: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in items:
        categories[item_category(item)].append(item)
    category_counts: dict[str, int] = {}
    for category, rows in sorted(categories.items()):
        category_counts[category] = write_jsonl(
            GENERATED / f"items/{category}.jsonl", add_provenance(rows, source)
        )
    flat = [flatten_item(item) for item in items]
    csv_fields = list(flat[0].keys()) if flat else []
    csv_count = write_csv(GENERATED / "items/equipment.csv", flat, csv_fields) if csv_fields else 0

    directory = GENERATED / "reference/items"
    directory.mkdir(parents=True, exist_ok=True)
    index_lines = ["# Pre-Renewal 装备与卡片目录", "", f"> 完整数据：`generated/items/equipment.jsonl`；来源 `{REPOSITORY}@{COMMIT}`。", ""]
    page_count = 0
    for category, rows in sorted(categories.items()):
        index_lines.append(f"- **{category}**：{len(rows)} 条")
        pages: dict[int, list[dict[str, Any]]] = defaultdict(list)
        for item in rows:
            item_id = int(item.get("Id", 0) or 0)
            pages[(item_id // 250) * 250].append(item)
        category_dir = directory / category
        category_dir.mkdir(parents=True, exist_ok=True)
        category_index = [f"# {category}", ""]
        for start, page_items in sorted(pages.items()):
            end = start + 249
            filename = f"{start:05d}-{end:05d}.md"
            category_index.append(f"- [{start}-{end}]({filename}) — {len(page_items)} 条")
            lines = [
                f"# {category} {start}-{end}", "",
                "| ID | 装备 | 类型 | ATK/MATK/DEF | 重量 | 洞 | 装备等级 | 可精炼 | 部位 |",
                "|---:|---|---|---|---:|---:|---|---|---|",
            ]
            for item in sorted(page_items, key=lambda row: int(row.get("Id", 0) or 0)):
                lines.append(
                    f"| {item.get('Id')} | {markdown_escape(item.get('Name', ''))} (`{item.get('AegisName', '')}`) | "
                    f"{item.get('Type', '')}/{item.get('SubType', '') or ''} | "
                    f"{item.get('Attack', 0)}/{item.get('MagicAttack', 0)}/{item.get('Defense', 0)} | "
                    f"{item.get('Weight', 0)} | {item.get('Slots', 0)} | "
                    f"{item.get('WeaponLevel', item.get('ArmorLevel', '')) or ''} | "
                    f"{'是' if item.get('Refineable') else '否'} | {markdown_escape(render_map(item.get('Locations', {})))} |"
                )
            lines.extend(["", "## 脚本效果", ""])
            for item in sorted(page_items, key=lambda row: int(row.get("Id", 0) or 0)):
                scripts = [("Script", item.get("Script")), ("EquipScript", item.get("EquipScript")), ("UnEquipScript", item.get("UnEquipScript"))]
                scripts = [(label, value) for label, value in scripts if value]
                if not scripts:
                    continue
                lines.append(f"### {item.get('Name', item.get('AegisName'))} (`{item.get('Id')}` / `{item.get('AegisName')}`)")
                lines.append("")
                for label, value in scripts:
                    lines.extend([f"**{label}**", "", "```text", str(value).strip(), "```", ""])
            (category_dir / filename).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
            page_count += 1
        (category_dir / "README.md").write_text("\n".join(category_index) + "\n", encoding="utf-8")
    (directory / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    return {"records": raw_count, "csv_rows": csv_count, "pages": page_count, **{f"category_{key}": value for key, value in category_counts.items()}}


def copy_source_manifest() -> None:
    source = VENDOR / "sync-manifest.json"
    if source.exists():
        destination = GENERATED / "source-manifest.json"
        destination.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")


def build_readme(summary: dict[str, Any]) -> None:
    counts = summary["counts"]
    text = f"""# 生成的 Pre-Renewal 完整数据集

本目录由 `scripts/sync_rathena.py` 与 `scripts/build_reference.py` 从固定提交自动生成：

- 上游：`{REPOSITORY}`
- 提交：`{COMMIT}`
- 构建模式：`PRERE`
- Renewal / 地区服覆盖：不包含

## 主要入口

- `skills/catalog.jsonl`：经典职业可学习技能，已合并职业归属和结构化中文描述。
- `skills/formulas.jsonl`：全部技能的源码定位与候选 C++ 公式/效果表达式。
- `reference/jobs/README.md`：按职业浏览技能、前置、消耗、持续时间和公式源码。
- `monsters/metadata.jsonl`：完整怪物记录。
- `monsters/drops.jsonl`：扁平化掉落表；`monsters/skills.jsonl`：怪物 AI 技能规则。
- `reference/monsters/README.md`：按 ID 分页浏览怪物数值、掉落和技能。
- `items/equipment.jsonl`：完整装备/卡片记录及脚本。
- `items/weapons.jsonl`、`items/armor.jsonl`、`items/cards.jsonl`：按类型拆分。
- `reference/items/README.md`：按类型与 ID 分页浏览装备和脚本效果。

## “技能描述”和“公式”的口径

rAthena 的 `Description` 字段主要是技能显示名，而不是完整攻略文本。因此这里的 `structured_description_zh` 是根据技能数据库中的目标、类型、属性、段数、范围、吟唱、后摇、持续时间、冷却、SP/HP/Zeny/弹药/道具消耗和关联状态自动生成的**量化描述**。

`formulas.jsonl` 不会把复杂技能强行猜成一行代数式。它保留技能常量在分技能实现、`battle.cpp`、`skill.cpp`、`status.cpp` 等文件中的精确行号和附近 C++ 表达式：

- `dedicated-source`：存在独立技能实现文件；
- `core-source`：公式位于通用战斗/技能管线；
- `metadata-only`：该技能主要由数据库、状态或脚本驱动，未找到独立源码表达式。

最终伤害仍可能同时依赖命中、DEF/MDEF、属性、体型、种族/阶级、装备卡片脚本、状态效果和 C++ 整数截断顺序。

## 数据规模

```json
{json.dumps(counts, ensure_ascii=False, indent=2)}
```

## 重要边界

这里是“锁定 rAthena 提交的 Pre-Renewal 运行数据集”，不是某一个历史 Episode 的博物馆快照。`db/pre-re` 中可能包含后来加入、但在 Pre-Renewal 计算模式下可用的内容；所有记录都保留来源路径和提交号，便于后续按 Episode 再做筛选。
"""
    (GENERATED / "README.md").write_text(text, encoding="utf-8")


def main() -> int:
    clean_generated()
    skills = body("db/pre-re/skill_db.yml")
    trees = body("db/pre-re/skill_tree.yml")
    job_paths = load_yaml(ROOT / "data/jobs/job_paths.yml")
    classic_skills, by_job, allowed_jobs = skill_tree_catalog(skills, trees, job_paths)
    formulas = formula_index(skills)

    counts: dict[str, Any] = {}
    counts["skills_all_metadata"] = write_jsonl(
        GENERATED / "skills/all_metadata.jsonl", add_provenance(skills, "db/pre-re/skill_db.yml")
    )
    counts["skills_classic_catalog"] = write_jsonl(GENERATED / "skills/catalog.jsonl", classic_skills)
    counts["skill_tree_records"] = write_jsonl(
        GENERATED / "skills/tree.jsonl", add_provenance(trees, "db/pre-re/skill_tree.yml")
    )
    counts["skill_formula_records"] = write_jsonl(
        GENERATED / "skills/formulas.jsonl", (formulas[name] for name in sorted(formulas))
    )
    for job, rows in sorted(by_job.items()):
        write_json(GENERATED / f"skills/by_job/{job}.json", {
            "job": job,
            "ruleset": "pre-renewal",
            "commit": COMMIT,
            "skills": rows,
        })
    counts["classic_jobs"] = len(allowed_jobs)
    counts["job_pages"] = build_job_pages(by_job, formulas)

    monsters = body("db/pre-re/mob_db.yml")
    mob_skills = parse_mob_skills(require("db/pre-re/mob_skill_db.txt"))
    counts["monsters"] = build_monsters(monsters, mob_skills)

    equipment = body("db/pre-re/item_db_equip.yml")
    counts["equipment"] = build_items(equipment)

    supporting = {
        "jobs/stats.jsonl": "db/pre-re/job_stats.yml",
        "jobs/aspd.jsonl": "db/pre-re/job_aspd.yml",
        "jobs/exp.jsonl": "db/pre-re/job_exp.yml",
        "jobs/basepoints.jsonl": "db/pre-re/job_basepoints.yml",
        "items/refine.jsonl": "db/pre-re/refine.yml",
        "items/combos.jsonl": "db/pre-re/item_combos.yml",
        "statuses/metadata.jsonl": "db/pre-re/status.yml",
        "companions/pets.jsonl": "db/pre-re/pet_db.yml",
        "companions/homunculus.jsonl": "db/pre-re/homunculus_db.yml",
        "companions/mercenaries.jsonl": "db/pre-re/mercenary_db.yml",
    }
    counts["supporting"] = {}
    for output, source in supporting.items():
        counts["supporting"][output] = write_jsonl(
            GENERATED / output, add_provenance(body(source), source)
        )

    copy_source_manifest()
    summary = {
        "ruleset": "pre-renewal",
        "build_mode": "PRERE",
        "repository": REPOSITORY,
        "commit": COMMIT,
        "counts": counts,
    }
    write_json(GENERATED / "summary.json", summary)
    build_readme(summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
