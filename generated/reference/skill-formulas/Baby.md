# Baby 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 1 | `NV_BASIC` / Basic Skill | `core-source-references` | `` | src/map/pc.cpp, src/map/status.cpp |
| 142 | `NV_FIRSTAID` / First Aid | `exact-class-methods` | `SkillFirstAid` | src/map/skills/novice/firstaid.cpp |
| 143 | `NV_TRICKDEAD` / Play Dead | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 408 | `WE_BABY` / Baby | `exact-class-methods` | `SkillBaby` | src/map/skills/other/baby.cpp |
| 409 | `WE_CALLPARENT` / Call Parent | `exact-class-methods` | `SkillCallParent` | src/map/skills/other/callparent.cpp |

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

### Baby (`WE_BABY`)

非伤害技能；目标：自身；最高等级 1；射程：9；命中类型：Single；段数：1；吟唱：3000 ms；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP 1；SP% -10；关联状态：ProtectExp。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBaby`
- 实现文件：`src/map/skills/other/baby.cpp`

#### `SkillBaby::SkillBaby`

来源：`src/map/skills/other/baby.cpp:11-12`

```cpp
SkillBaby::SkillBaby() : SkillImpl(WE_BABY) {
}
```

#### `SkillBaby::castendNoDamageId`

来源：`src/map/skills/other/baby.cpp:14-53`

```cpp
void SkillBaby::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd == nullptr)
		return;

	map_session_data* f_sd = pc_get_father(sd);
	map_session_data* m_sd = pc_get_mother(sd);

	// Neither was found
	if (f_sd == nullptr && m_sd == nullptr) {
		clif_skill_fail(*sd, getSkillId());
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}

	// Not in same party
	// TODO : no check if sd->status.party_id == 0 ?
	if (sd->status.party_id != 0 && (f_sd == nullptr || sd->status.party_id != f_sd->status.party_id) && (m_sd == nullptr || sd->status.party_id != m_sd->status.party_id)) {
		clif_skill_fail(*sd, getSkillId());
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}

	// Not in same screen
	if ((f_sd == nullptr || !check_distance_bl(sd, f_sd, AREA_SIZE)) && (m_sd == nullptr || !check_distance_bl(sd, m_sd, AREA_SIZE))) {
		clif_skill_fail(*sd, getSkillId());
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}

	status_change_start(src, target, SC_STUN, 10000, skill_lv, 0, 0, 0, skill_get_time2(getSkillId(), skill_lv), SCSTART_NORATEDEF);

	sc_type type = skill_get_sc(getSkillId());

	if (f_sd != nullptr)
		sc_start(src, f_sd, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
	if (m_sd != nullptr)
		sc_start(src, m_sd, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
}
```

### Call Parent (`WE_CALLPARENT`)

非伤害技能；目标：自身；最高等级 1；射程：9；命中类型：Single；段数：1；范围：3；持续时间1：20000 ms；伤害标记：NoDamage；消耗/限制：SP 1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCallParent`
- 实现文件：`src/map/skills/other/callparent.cpp`

#### `SkillCallParent::SkillCallParent`

来源：`src/map/skills/other/callparent.cpp:6-7`

```cpp
SkillCallParent::SkillCallParent() : SkillImpl(WE_CALLPARENT) {
}
```

#### `SkillCallParent::castendPos2`

来源：`src/map/skills/other/callparent.cpp:9-12`

```cpp
void SkillCallParent::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag|=1; // Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```
