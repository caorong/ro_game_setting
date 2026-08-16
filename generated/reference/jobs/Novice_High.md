# Novice_High 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Novice_High` 公式页](../skill-formulas/Novice_High.md)

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 143 | `NV_TRICKDEAD` | Play Dead | 1 | Novice_High | 是 | — | None / Self |

## 技能详情

### Play Dead (`NV_TRICKDEAD`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 5；关联状态：TrickDead。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skills/novice/skill_factory_novice.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:2108
if (flag != 1) // Can't cast, casted stuff can't damage.
// src/map/status.cpp:2110
if (skill_get_casttype(skill_id) == CAST_DAMAGE)
// src/map/status.cpp:2111
return false; // Damage spells stop casting.
```
