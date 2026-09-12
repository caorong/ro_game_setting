# Sniper 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 380 | `SN_SIGHT` / Falcon Eyes | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 381 | `SN_FALCONASSAULT` / Falcon Assault | `exact-class-methods` | `SkillFalconAssault` | src/map/skills/archer/falconassault.cpp |
| 382 | `SN_SHARPSHOOTING` / Focused Arrow Strike | `exact-class-methods` | `SkillFocusedArrowStrike` | src/map/skills/archer/focusedarrowstrike.cpp |
| 383 | `SN_WINDWALK` / Wind Walker | `exact-class-methods` | `SkillWindWalker` | src/map/skills/archer/windwalker.cpp |

## 详细公式与效果实现

### Falcon Eyes (`SN_SIGHT`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-2=20; Lv3-4=25; Lv5-6=30; Lv7-8=35; Lv9-10=40；关联状态：TrueSight。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Falcon Assault (`SN_FALCONASSAULT`)

特殊技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：1；吟唱：1000 ms；技能后摇：3000 ms；伤害标记：IgnoreFlee；消耗/限制：SP Lv1=30; Lv2=34; Lv3=38; Lv4=42; Lv5=46；状态 Falcon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFalconAssault`
- 实现文件：`src/map/skills/archer/falconassault.cpp`

#### `SkillFalconAssault::SkillFalconAssault`

来源：`src/map/skills/archer/falconassault.cpp:6-7`

```cpp
SkillFalconAssault::SkillFalconAssault() : SkillImpl(SN_FALCONASSAULT) {
}
```

#### `SkillFalconAssault::castendDamageId`

来源：`src/map/skills/archer/falconassault.cpp:9-11`

```cpp
void SkillFalconAssault::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_attack(skill_get_type(getSkillId()),src,src,target,getSkillId(),skill_lv,tick,flag);
}
```

### Focused Arrow Strike (`SN_SHARPSHOOTING`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：1；属性：Weapon；范围：1；吟唱：2000 ms；技能后摇：1500 ms；伤害标记：Critical；消耗/限制：SP Lv1=18; Lv2=21; Lv3=24; Lv4=27; Lv5=30；弹药数 1；武器 Bow；弹药 Arrow。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFocusedArrowStrike`
- 实现文件：`src/map/skills/archer/focusedarrowstrike.cpp`

#### `SkillFocusedArrowStrike::SkillFocusedArrowStrike`

来源：`src/map/skills/archer/focusedarrowstrike.cpp:10-11`

```cpp
SkillFocusedArrowStrike::SkillFocusedArrowStrike() : SkillImplRecursiveDamageSplash(SN_SHARPSHOOTING) {
}
```

#### `SkillFocusedArrowStrike::calculateSkillRatio`

来源：`src/map/skills/archer/focusedarrowstrike.cpp:13-27`

```cpp
void SkillFocusedArrowStrike::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
	if (src->type == BL_MOB) { // TODO: Did these formulas change in the renewal balancing?
		if (wd->miscflag & 2) // Splash damage bonus
			skillratio += -100 + 140 * skill_lv;
		else
			skillratio += 100 + 50 * skill_lv;
		return;
	}
#ifdef RENEWAL
	skillratio += -100 + 300 + 300 * skill_lv;
	RE_LVL_DMOD(100);
#else
	skillratio += 100 + 50 * skill_lv;
#endif
}
```

#### `SkillFocusedArrowStrike::castendDamageId`

来源：`src/map/skills/archer/focusedarrowstrike.cpp:29-55`

```cpp
void SkillFocusedArrowStrike::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	SkillImplRecursiveDamageSplash::castendDamageId(src, target, skill_lv, tick, flag);

	if( flag&1 ) {
		status_change_end(src, SC_CAMOUFLAGE);
	}
#else
	flag |= 2; // Flag for specific mob damage formula
	skill_area_temp[1] = target->id;
	if (battle_config.skill_eightpath_algorithm) {
		//Use official AoE algorithm
		if (!(map_foreachindir(skill_attack_area, src->m, src->x, src->y, target->x, target->y,
		   skill_get_splash(getSkillId(), skill_lv), skill_get_maxcount(getSkillId(), skill_lv), 0, splash_target(src),
		   skill_get_type(getSkillId()), src, src, getSkillId(), skill_lv, tick, flag, BCT_ENEMY))) {
			flag &= ~2; // Only targets in the splash area are affected

			//These skills hit at least the target if the AoE doesn't hit
			skill_attack(skill_get_type(getSkillId()), src, src, target, getSkillId(), skill_lv, tick, flag);
		}
	} else {
		map_foreachinpath(skill_attack_area, src->m, src->x, src->y, target->x, target->y,
			skill_get_splash(getSkillId(), skill_lv), skill_get_maxcount(getSkillId(), skill_lv), splash_target(src),
			skill_get_type(getSkillId()), src, src, getSkillId(), skill_lv, tick, flag, BCT_ENEMY);
	}
#endif
}
```

### Wind Walker (`SN_WINDWALK`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；范围：-1；吟唱：Lv1=2000; Lv2=2400; Lv3=2800; Lv4=3200; Lv5=3600; Lv6=4000; Lv7=4400; Lv8=4800; Lv9=5200; Lv10=5600 ms；技能后摇：2000 ms；持续时间1：Lv1=130000; Lv2=160000; Lv3=190000; Lv4=220000; Lv5=250000; Lv6=280000; Lv7=310000; Lv8=340000; Lv9=370000; Lv10=400000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=46; Lv2=52; Lv3=58; Lv4=64; Lv5=70; Lv6=76; Lv7=82; Lv8=88; Lv9=94; Lv10=100；关联状态：WindWalk。

- 覆盖：`exact-class-methods`
- 实现类：`SkillWindWalker`
- 实现文件：`src/map/skills/archer/windwalker.cpp`

#### `SkillWindWalker::SkillWindWalker`

来源：`src/map/skills/archer/windwalker.cpp:11-12`

```cpp
SkillWindWalker::SkillWindWalker() : SkillImpl(SN_WINDWALK) {
}
```

#### `SkillWindWalker::castendNoDamageId`

来源：`src/map/skills/archer/windwalker.cpp:14-24`

```cpp
void SkillWindWalker::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sd == nullptr || sd->status.party_id == 0 || (flag & 1) )
		clif_skill_nodamage(target, *target, getSkillId(), skill_lv, sc_start(src,target,type,100,skill_lv,skill_get_time(getSkillId(),skill_lv)));
	else if (sd)
	{
		party_foreachsamemap(skill_area_sub, sd, skill_get_splash(getSkillId(), skill_lv), src, getSkillId(), skill_lv, tick, flag|BCT_PARTY|1, skill_castend_nodamage_id);
	}
}
```
