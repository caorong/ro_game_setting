# RO Pre-Renewal 可量化规则参考库

本仓库整理 **Ragnarok Online（RO）Pre-Renewal / 经典规则**的职业、属性、战斗、技能、装备、卡片、精炼、怪物、状态异常、经验与生产等可量化设定。

它的目标不是写一篇攻略，而是维护一套能够被人阅读、被程序校验、被 AI 引用、被游戏设计项目复用的**带版本号规则基线**。

> 当前规则基线：rAthena commit [`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`](https://github.com/rathena/rathena/commit/2fe6ab3dc4d830b11d93fb44c3b48436571890bd)，按 `PRERE` 构建口径解释。

## 范围

**包含：**

- 初心者、六大一转、十二条二转、转生体系及经典扩展职业；
- STR / AGI / VIT / INT / DEX / LUK 与派生属性；
- ATK、MATK、HIT、FLEE、CRI、Perfect Flee、ASPD；
- 普通攻击、物理技能、魔法技能、命中、暴击、防御、属性、体型、种族与阶级修正；
- 吟唱、后摇、冷却、多段、状态异常、HP/SP、自然恢复；
- 装备、卡片、精炼、弹药、双持、怪物、掉落、经验、宠物、人工生命体、佣兵、生产与经济数据；
- rAthena Pre-Renewal 的完整静态数据库和技能源码索引生成流程。

**明确排除：**

- Renewal 战斗公式；
- 三转、四转与 Renewal 特性属性；
- jRO、iRO、台服、国服等地区专属改动；
- 私服自定义公式；
- 世界观、美术、地图剧情的百科式复述。

## 可信度说明

Gravity 官方服务端源码并未公开。本仓库把 rAthena 的 Pre-Renewal 实现作为**可执行、可追踪的工程参考**，而不是宣称它等同于某一历史时期官方服务器的绝对真值。

每条核心公式都应带：

```text
ruleset + source_commit + source_path + rounding + unit + exceptions
```

遇到资料冲突时，优先级为：

1. 本仓库锁定提交中的实际 C++ 执行路径；
2. 同提交的 `db/pre-re`、公共 DB 与 battle config；
3. rAthena 自带文档；
4. 外部 Wiki/攻略仅作为交叉验证，不直接覆盖源码口径。

## 目录

```text
docs/                       中文规则文档
data/formulas/              可机器读取的公式定义
data/jobs/                  经典职业路线
data/tables/                属性、体型等矩阵
data/rules/                 默认 battle config 摘要
data/sources/               来源锁与同步清单
src/ro_pre_re/              可执行公式与生成工具
scripts/                    同步、构建、校验命令
tests/                      公式边界与表格回归测试
vendor/rathena/             同步后的上游文件（默认不提交）
generated/                  从上游生成的完整索引（默认不提交）
```

## 快速开始

```bash
python -m pip install -e '.[dev]'

# 1. 从锁定提交同步完整 Pre-Renewal 数据、核心源码和技能实现
python scripts/sync_rathena.py

# 2. 生成技能、职业、装备、怪物、状态和来源索引
python scripts/build_reference.py

# 3. 校验规则范围、YAML、公式边界和来源锁
python scripts/validate_reference.py
pytest
```

同步命令支持 `GITHUB_TOKEN`，未配置时使用 GitHub 公共 API：

```bash
GITHUB_TOKEN=... python scripts/sync_rathena.py --include-skill-source
```

## 文档入口

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

## “完整”的定义

RO 的技能效果不是一张公式表可以完整表达的。一个技能通常由以下部分共同决定：

```text
skill_tree.yml        职业、前置、最大等级
skill_db.yml          目标、范围、段数、属性、吟唱、消耗、持续时间
skills/**/*.cpp       技能倍率、命中修正、状态概率和例外
battle.cpp            通用伤害与命中管线
status.cpp            面板属性与状态变化
item/status/config    装备脚本、异常状态和服务器开关
```

因此本仓库同时维护：

- **人工审校公式**：适合直接理解和实现；
- **完整上游快照与索引生成器**：保证没有因为“暂时没翻译成代数式”就丢掉技能逻辑；
- **明确的覆盖状态**：`verified`、`source-indexed`、`table-driven`、`uncertain`。

## 许可证

本仓库原创文档与工具使用 MIT License。rAthena 及同步得到的上游文件遵循其 GPL-3.0 许可证；详情见 [NOTICE.md](NOTICE.md)。
