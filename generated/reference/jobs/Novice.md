# Novice 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Novice` 公式页](../skill-formulas/Novice.md)

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 是 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 是 | — | None / Self |
| 143 | `NV_TRICKDEAD` | Play Dead | 1 | Novice | 是 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 是 | — | None / Self |

## 技能详情

### Basic Skill (`NV_BASIC`)

非伤害技能；目标：被动；最高等级 9。

- 技能树最高等级：`9`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:3430
status_change *sc = status_get_sc(bl);
// src/map/status.cpp:3447
} else if (type == STATUS_BONUS_RATE) {
// src/map/status.cpp:3448
status_change *sc = status_get_sc(bl);
```

### First Aid (`NV_FIRSTAID`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 3。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skills/novice/firstaid.cpp`, `src/map/skills/novice/skill_factory_novice.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/novice/firstaid.cpp:12
void SkillFirstAid::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/novice/firstaid.cpp:13
clif_skill_nodamage(src, *target, getSkillId(), 5);
// src/map/skills/novice/firstaid.cpp:14
status_heal(target, 5, 0, 0);
```

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

### Call Baby (`WE_CALLBABY`)

非伤害技能；目标：自身；最高等级 1；射程：9；命中类型：Single；段数：1；范围：3；持续时间1：20000 ms；伤害标记：NoDamage；消耗/限制：SP 1。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/other/callbaby.cpp`, `src/map/skills/other/skill_factory_other.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:892
return false; // gonna be checked in 'skill_castend_nodamage_id'
// src/map/skill.cpp:5981
val1 = 55 + skill_lv*5;	//Elemental Resistance
// src/map/skill.cpp:5982
val2 = skill_lv*10;	//Status ailment resistance
// src/map/skill.cpp:5998
val2 = (skill_lv+1)/2 + 4;
// src/map/skills/other/callbaby.cpp:9
void SkillCallBaby::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/other/callbaby.cpp:11
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/other/skill_factory_other.cpp:121
case RETURN_TO_ELDICASTES:
// src/map/skills/other/skill_factory_other.cpp:122
return std::make_unique<SkillReturnToEldicastes>();
```
