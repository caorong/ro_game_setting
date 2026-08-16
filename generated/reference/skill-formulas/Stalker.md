# Stalker 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 389 | `ST_CHASEWALK` / Stealth | `exact-class-methods` | `SkillStealth` | src/map/skills/thief/stealth.cpp |
| 390 | `ST_REJECTSWORD` / Counter Instinct | `exact-class-methods` | `SkillCounterInstinct` | src/map/skills/thief/counterinstinct.cpp |
| 475 | `ST_PRESERVE` / Preserve | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 476 | `ST_FULLSTRIP` / Divest All | `exact-class-methods` | `SkillDivestAll` | src/map/skills/thief/divestall.cpp |

## 详细公式与效果实现

### Stealth (`ST_CHASEWALK`)

非伤害技能；目标：自身；最高等级 5；命中类型：Single；段数：1；吟唱：1200 ms；持续时间1：10000 ms；持续时间2：30000 ms；伤害标记：NoDamage；消耗/限制：SP 10；关联状态：ChaseWalk。

- 覆盖：`exact-class-methods`
- 实现类：`SkillStealth`
- 实现文件：`src/map/skills/thief/stealth.cpp`

#### `SkillStealth::SkillStealth`

来源：`src/map/skills/thief/stealth.cpp:9-10`

```cpp
SkillStealth::SkillStealth() : SkillImpl(ST_CHASEWALK) {
}
```

#### `SkillStealth::castendNoDamageId`

来源：`src/map/skills/thief/stealth.cpp:12-24`

```cpp
void SkillStealth::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	status_change *tsc = status_get_sc(target);
	status_change_entry *tsce = (tsc && type != SC_NONE)?tsc->getSCE(type):nullptr;

	if (tsce)
	{
		clif_skill_nodamage(src,*target,getSkillId(),-1,status_change_end(target, type)); //Hide skill-scream animation.
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}
	clif_skill_nodamage(src,*target,getSkillId(),-1,sc_start(src,target,type,100,skill_lv,skill_get_time(getSkillId(),skill_lv)));
}
```

### Counter Instinct (`ST_REJECTSWORD`)

武器/物理技能；目标：自身；最高等级 5；段数：1；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=10; Lv2=15; Lv3=20; Lv4=25; Lv5=30；关联状态：RejectSword。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCounterInstinct`
- 实现文件：`src/map/skills/thief/counterinstinct.cpp`

#### `SkillCounterInstinct::SkillCounterInstinct`

来源：`src/map/skills/thief/counterinstinct.cpp:8-9`

```cpp
SkillCounterInstinct::SkillCounterInstinct() : StatusSkillImpl(ST_REJECTSWORD) {
}
```

#### `SkillCounterInstinct::applyAdditionalEffects`

来源：`src/map/skills/thief/counterinstinct.cpp:11-13`

```cpp
void SkillCounterInstinct::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src,target,SC_AUTOCOUNTER,(skill_lv*15),skill_lv,skill_get_time(getSkillId(),skill_lv));
}
```

### Preserve (`ST_PRESERVE`)

非伤害技能；目标：自身；最高等级 1；段数：1；吟唱：1000 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 30；关联状态：Preserve。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Divest All (`ST_FULLSTRIP`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：1；命中类型：Single；段数：1；技能后摇：1000 ms；持续时间1：Lv1=75000; Lv2=90000; Lv3=105000; Lv4=120000; Lv5=135000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=22; Lv2=24; Lv3=26; Lv4=28; Lv5=30。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDivestAll`
- 实现文件：`src/map/skills/thief/divestall.cpp`

#### `SkillDivestAll::SkillDivestAll`

来源：`src/map/skills/thief/divestall.cpp:10-11`

```cpp
SkillDivestAll::SkillDivestAll() : SkillImpl(ST_FULLSTRIP) {
}
```

#### `SkillDivestAll::castendNoDamageId`

来源：`src/map/skills/thief/divestall.cpp:13-32`

```cpp
void SkillDivestAll::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_change *tsc = status_get_sc(target);
	map_session_data* sd = BL_CAST( BL_PC, src );

	bool i;

	//Special message when trying to use strip on FCP [Jobbie]
	if( sd && tsc && tsc->getSCE(SC_CP_WEAPON) && tsc->getSCE(SC_CP_HELM) && tsc->getSCE(SC_CP_ARMOR) && tsc->getSCE(SC_CP_SHIELD))
	{
		clif_gospel_info( *sd, 0x28 );
		return;
	}

	if( i = skill_strip_equip(src, target, getSkillId(), skill_lv) )
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv,i);

	//Nothing stripped.
	if( sd && !i )
		clif_skill_fail( *sd, getSkillId() );
}
```
