# Novice 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 1 | `NV_BASIC` / Basic Skill | `core-source-references` | `` | src/map/pc.cpp, src/map/status.cpp |
| 142 | `NV_FIRSTAID` / First Aid | `exact-class-methods` | `SkillFirstAid` | src/map/skills/novice/firstaid.cpp |
| 143 | `NV_TRICKDEAD` / Play Dead | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 410 | `WE_CALLBABY` / Call Baby | `exact-class-methods` | `SkillCallBaby` | src/map/skills/other/callbaby.cpp |

## 详细公式与效果实现

### Basic Skill (`NV_BASIC`)

非伤害技能；目标：被动；最高等级 9。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

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

- 覆盖：`exact-class-methods`
- 实现类：`SkillFirstAid`
- 实现文件：`src/map/skills/novice/firstaid.cpp`

#### `SkillFirstAid::SkillFirstAid`

来源：`src/map/skills/novice/firstaid.cpp:9-10`

```cpp
SkillFirstAid::SkillFirstAid() : SkillImpl(NV_FIRSTAID) {
}
```

#### `SkillFirstAid::castendNoDamageId`

来源：`src/map/skills/novice/firstaid.cpp:12-15`

```cpp
void SkillFirstAid::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	clif_skill_nodamage(src, *target, getSkillId(), 5);
	status_heal(target, 5, 0, 0);
}
```

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

### Call Baby (`WE_CALLBABY`)

非伤害技能；目标：自身；最高等级 1；射程：9；命中类型：Single；段数：1；范围：3；持续时间1：20000 ms；伤害标记：NoDamage；消耗/限制：SP 1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCallBaby`
- 实现文件：`src/map/skills/other/callbaby.cpp`

#### `SkillCallBaby::SkillCallBaby`

来源：`src/map/skills/other/callbaby.cpp:6-7`

```cpp
SkillCallBaby::SkillCallBaby() : SkillImpl(WE_CALLBABY) {
}
```

#### `SkillCallBaby::castendPos2`

来源：`src/map/skills/other/callbaby.cpp:9-12`

```cpp
void SkillCallBaby::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag|=1; // Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```
