# 生成的 Pre-Renewal 完整数据集

本目录由 `scripts/sync_rathena.py` 与 `scripts/build_reference.py` 从固定提交自动生成：

- 上游：`rathena/rathena`
- 提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`
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
{
  "skills_all_metadata": 1228,
  "skills_classic_catalog": 457,
  "skill_tree_records": 77,
  "skill_formula_records": 1228,
  "classic_jobs": 73,
  "job_pages": 73,
  "monsters": {
    "records": 1004,
    "csv_rows": 1004,
    "drops": 5019,
    "skill_rules": 5494,
    "pages": 11
  },
  "equipment": {
    "records": 2017,
    "csv_rows": 2017,
    "pages": 22,
    "category_armor": 1216,
    "category_petarmor": 38,
    "category_petegg": 56,
    "category_weapons": 707
  },
  "supporting": {
    "jobs/stats.jsonl": 42,
    "jobs/aspd.jsonl": 25,
    "jobs/exp.jsonl": 11,
    "jobs/basepoints.jsonl": 51,
    "items/refine.jsonl": 4,
    "items/combos.jsonl": 105,
    "statuses/metadata.jsonl": 699,
    "companions/pets.jsonl": 57,
    "companions/homunculus.jsonl": 8,
    "companions/mercenaries.jsonl": 0
  }
}
```

## 重要边界

这里是“锁定 rAthena 提交的 Pre-Renewal 运行数据集”，不是某一个历史 Episode 的博物馆快照。`db/pre-re` 中可能包含后来加入、但在 Pre-Renewal 计算模式下可用的内容；所有记录都保留来源路径和提交号，便于后续按 Episode 再做筛选。

<!-- generated-cards:start -->
## 卡片数据

- 卡片记录：**538**
- 浏览分页：**4**
- 机器数据：`items/cards.jsonl` / `items/cards.csv`
- 浏览入口：`reference/items/cards/README.md`
- 每张卡片保留完整 rAthena `Script`，用于还原属性、种族、体型、状态和触发效果。
<!-- generated-cards:end -->

<!-- generated-skill-implementations:start -->
## 技能精确实现索引

- 经典职业技能记录：**457**
- 职业公式页：**73**
- 覆盖分布：`{"core-source-references": 80, "exact-class-methods": 332, "generic-or-class-mapped": 43, "metadata-only": 2}`
- 机器数据：`skills/classic_implementations.jsonl`
- 浏览入口：`reference/skill-formulas/README.md`
- 优先使用技能工厂映射后的完整类方法；没有独立实现类时再回退到通用战斗源码定位。
<!-- generated-skill-implementations:end -->
