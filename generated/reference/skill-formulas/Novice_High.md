# Novice_High 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 143 | `NV_TRICKDEAD` / Play Dead | `generic-or-class-mapped` | `StatusSkillImpl` |  |

## 详细公式与效果实现

### Play Dead (`NV_TRICKDEAD`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 5；关联状态：TrickDead。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:2108
if (flag != 1) // Can't cast, casted stuff can't damage.
// src/map/status.cpp:2110
if (skill_get_casttype(skill_id) == CAST_DAMAGE)
// src/map/status.cpp:2111
return false; // Damage spells stop casting.
```
