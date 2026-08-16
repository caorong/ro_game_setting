# RO Pre-Renewal 可量化规则参考库

本仓库整理 **Ragnarok Online（RO）Pre-Renewal / 经典规则**的职业、属性、战斗、技能、装备、卡片、精炼、怪物、状态异常、经验与生产等可量化设定。

它不是一篇攻略，而是一套能被人阅读、程序校验、AI 引用和游戏设计项目复用的**带版本号规则基线**。

> 当前规则基线：rAthena commit [`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`](https://github.com/rathena/rathena/commit/2fe6ab3dc4d830b11d93fb44c3b48436571890bd)，按 `PRERE` 构建口径解释。

## 范围

**包含：**

- 初心者、六大一转、十二条二转、转生体系及经典扩展职业；
- STR / AGI / VIT / INT / DEX / LUK 与所有主要派生属性；
- 普通攻击、物理/魔法/特殊技能、命中、暴击、防御、属性、体型、种族与阶级修正；
- 吟唱、后摇、冷却、多段、状态异常、HP/SP、自然恢复；
- 全职业技能树、技能量化描述、源码公式定位；
- 完整怪物数值、掉落、怪物技能 AI；
- 完整武器、防具、卡片、弹药及装备脚本；
- 精炼、职业成长、经验、宠物、人工生命体和佣兵等支持数据。

**明确排除：** Renewal 公式、三转/四转、Renewal 特性属性、地区服专属改动和私服自定义公式。

## 完整数据入口

GitHub Actions 会从锁定的 rAthena 提交生成并提交 `generated/`。主要入口：

| 数据 | 入口 |
|---|---|
| 全职业技能目录 | [`generated/reference/jobs/README.md`](generated/reference/jobs/README.md) |
| 经典职业技能 JSONL | [`generated/skills/catalog.jsonl`](generated/skills/catalog.jsonl) |
| 全技能源码公式索引 | [`generated/skills/formulas.jsonl`](generated/skills/formulas.jsonl) |
| 怪物浏览目录 | [`generated/reference/monsters/README.md`](generated/reference/monsters/README.md) |
| 完整怪物数据 | [`generated/monsters/metadata.jsonl`](generated/monsters/metadata.jsonl) |
| 怪物掉落与技能 | [`generated/monsters/drops.jsonl`](generated/monsters/drops.jsonl) / [`skills.jsonl`](generated/monsters/skills.jsonl) |
| 装备与卡片目录 | [`generated/reference/items/README.md`](generated/reference/items/README.md) |
| 完整装备数据 | [`generated/items/equipment.jsonl`](generated/items/equipment.jsonl) |
| 武器 / 防具 / 卡片 | [`weapons.jsonl`](generated/items/weapons.jsonl) / [`armor.jsonl`](generated/items/armor.jsonl) / [`cards.jsonl`](generated/items/cards.jsonl) |
| 生成说明与数据规模 | [`generated/README.md`](generated/README.md) / [`summary.json`](generated/summary.json) |

### 技能“描述”和“公式”的口径

`skill_db.yml` 的 `Description` 主要是技能显示名，不是完整攻略说明。本仓库根据目标、类型、属性、射程、段数、范围、吟唱、后摇、冷却、持续时间、SP/HP/Zeny/弹药/道具消耗和关联状态生成结构化中文量化描述。

技能效果还分散在 `skills/**/*.cpp`、`battle.cpp`、`skill.cpp`、`status.cpp`、状态数据库和装备脚本中。因此 `formulas.jsonl` 保存：

- 技能常量的全部源码定位；
- 附近的原始 C++ 倍率、伤害、概率、持续时间和状态表达式；
- `dedicated-source`、`core-source`、`metadata-only` 覆盖状态；
- 来源提交、路径与行号。

复杂技能不会被静默猜成一行“看起来合理”的代数式。

## 目录

```text
docs/                       中文规则文档
data/formulas/              人工审校的可机器读取公式
data/jobs/                  经典职业路线与排除范围
data/tables/                属性、体型等矩阵
data/rules/                 默认 battle config 摘要
data/sources/               来源锁与同步清单
src/ro_pre_re/              可执行公式与生成工具
scripts/                    同步、构建、校验命令
tests/                      公式边界与表格回归测试
vendor/rathena/             临时同步的上游文件，不提交
generated/                  自动生成并提交的完整技能、怪物、装备目录
```

## 本地重新生成

```bash
python -m pip install -e '.[dev]'
python scripts/sync_rathena.py --clean --include-skill-source
python scripts/build_reference.py
python scripts/sync_rathena.py --verify-only
python scripts/validate_reference.py
pytest
```

## 中文规则文档

| 主题 | 文档 |
|---|---|
| 版本与口径 | [00-scope-and-version.md](docs/00-scope-and-version.md) |
| 等级、属性点、转生 | [01-character-progression.md](docs/01-character-progression.md) |
| 完整经典职业路线 | [02-job-tree.md](docs/02-job-tree.md) |
| 六维属性与派生属性 | [03-primary-and-derived-stats.md](docs/03-primary-and-derived-stats.md) |
| 攻击速度 | [04-attack-speed.md](docs/04-attack-speed.md) |
| 命中、回避、暴击 | [05-hit-flee-critical.md](docs/05-hit-flee-critical.md) |
| 物理伤害管线 | [06-physical-damage.md](docs/06-physical-damage.md) |
| 魔法伤害管线 | [07-magic-damage.md](docs/07-magic-damage.md) |
| DEF / MDEF | [08-defense.md](docs/08-defense.md) |
| 属性、体型、种族、阶级 | [09-element-size-race-class.md](docs/09-element-size-race-class.md) |
| 吟唱、后摇、冷却 | [10-cast-delay-cooldown.md](docs/10-cast-delay-cooldown.md) |
| HP、SP、恢复 | [11-hp-sp-regeneration.md](docs/11-hp-sp-regeneration.md) |
| 状态异常 | [12-status-effects.md](docs/12-status-effects.md) |
| 装备、卡片、精炼 | [13-equipment-refine-cards.md](docs/13-equipment-refine-cards.md) |
| 怪物、经验、掉落 | [14-monsters-exp-drops.md](docs/14-monsters-exp-drops.md) |
| 全技能覆盖方式 | [15-skills.md](docs/15-skills.md) |
| 源码与数据索引 | [16-source-index.md](docs/16-source-index.md) |
| 不确定项与边界 | [17-known-uncertainties.md](docs/17-known-uncertainties.md) |
| 队伍、公会、PvP/GvG | [18-party-guild-pvp.md](docs/18-party-guild-pvp.md) |
| 宠物、人工生命体、佣兵 | [19-pets-homunculus-mercenary.md](docs/19-pets-homunculus-mercenary.md) |
| 生产与经济数据 | [20-production-economy.md](docs/20-production-economy.md) |
| 维护与扩展规范 | [21-maintenance.md](docs/21-maintenance.md) |

## 可信度和版本边界

Gravity 官方服务端源码并未公开。本仓库把 rAthena 的 Pre-Renewal 实现作为**可执行、可追踪的工程参考**，不宣称它等同于某一历史时期官方服务器的绝对真值。

这里是“锁定 rAthena 提交的 Pre-Renewal 数据集”，不是单一 Episode 的博物馆快照。`db/pre-re` 中可能存在后来加入、但按 Pre-Renewal 机制运行的内容；每条生成记录都保留提交号和来源路径，后续可以再增加 Episode 过滤层。

## 许可证

本仓库原创文档与工具使用 MIT License。rAthena 及其衍生生成数据遵循上游 GPL-3.0 许可证和来源声明；详情见 [NOTICE.md](NOTICE.md)。
