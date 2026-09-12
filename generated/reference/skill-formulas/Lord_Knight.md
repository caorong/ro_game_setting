# Lord_Knight 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 355 | `LK_AURABLADE` / Aura Blade | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 356 | `LK_PARRYING` / Parrying | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 357 | `LK_CONCENTRATION` / Concentration | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 358 | `LK_TENSIONRELAX` / Relax | `exact-class-methods` | `SkillRelax` | src/map/skills/swordman/relax.cpp |
| 359 | `LK_BERSERK` / Frenzy | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 397 | `LK_SPIRALPIERCE` / Spiral Pierce | `exact-class-methods` | `SkillSpiralPierce` | src/map/skills/swordman/spiralpierce.cpp |
| 398 | `LK_HEADCRUSH` / Traumatic Blow | `exact-class-methods` | `SkillTraumaticBlow` | src/map/skills/swordman/traumaticblow.cpp |
| 399 | `LK_JOINTBEAT` / Vital Strike | `exact-class-methods` | `SkillVitalStrike` | src/map/skills/swordman/vitalstrike.cpp |

## 详细公式与效果实现

### Aura Blade (`LK_AURABLADE`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：Lv1=40000; Lv2=60000; Lv3=80000; Lv4=100000; Lv5=120000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=18; Lv2=26; Lv3=34; Lv4=42; Lv5=50；武器 Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Bow, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；关联状态：AuraBlade。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skills/swordman/skill_factory_swordman.cpp:222
case LG_REFLECTDAMAGE:
// src/map/skills/swordman/skill_factory_swordman.cpp:234
case LK_CONCENTRATION:
```

### Parrying (`LK_PARRYING`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：Lv1=15000; Lv2=20000; Lv3=25000; Lv4=30000; Lv5=35000; Lv6=40000; Lv7=45000; Lv8=50000; Lv9=55000; Lv10=60000 ms；伤害标记：NoDamage；消耗/限制：SP 50；武器 2hSword；关联状态：Parrying。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:1580
status_change_end(target, SC_LIGHTNINGWALK);
// src/map/battle.cpp:1591
clif_skill_nodamage(target, *target, LK_PARRYING, sce->val1);
// src/map/battle.cpp:1592
unit_set_attackdelay(*target, gettick(), DELAY_EVENT_PARRY);
// src/map/battle.cpp:1601
clif_skill_nodamage(target, *target, TK_DODGE, 1);
// src/map/battle.cpp:1602
sc_start4(src, target, SC_COMBO, 100, TK_JUMPKICK, src->id, 1, 0, 2000);
// src/map/skills/swordman/skill_factory_swordman.cpp:234
case LK_CONCENTRATION:
```

### Concentration (`LK_CONCENTRATION`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：Lv1=25000; Lv2=30000; Lv3=35000; Lv4=40000; Lv5=45000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=14; Lv2=18; Lv3=22; Lv4=26; Lv5=30；关联状态：Concentration。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skills/swordman/skill_factory_swordman.cpp:222
case LG_REFLECTDAMAGE:
// src/map/skills/swordman/skill_factory_swordman.cpp:234
case LK_CONCENTRATION:
```

### Relax (`LK_TENSIONRELAX`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 15；关联状态：TensionRelax。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRelax`
- 实现文件：`src/map/skills/swordman/relax.cpp`

#### `SkillRelax::SkillRelax`

来源：`src/map/skills/swordman/relax.cpp:9-10`

```cpp
SkillRelax::SkillRelax() : SkillImpl(LK_TENSIONRELAX) {
}
```

#### `SkillRelax::castendNoDamageId`

来源：`src/map/skills/swordman/relax.cpp:12-18`

```cpp
void SkillRelax::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start4(src,target,type,100,skill_lv,0,0,skill_get_time2(getSkillId(),skill_lv),
			skill_get_time(getSkillId(),skill_lv)));
}
```

### Frenzy (`LK_BERSERK`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：300000 ms；持续时间2：10000 ms；伤害标记：NoDamage；消耗/限制：SP 200；关联状态：Berserk。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skills/swordman/skill_factory_swordman.cpp:222
case LG_REFLECTDAMAGE:
// src/map/skills/swordman/skill_factory_swordman.cpp:234
case LK_CONCENTRATION:
// src/map/status.cpp:13720
status_change_end(bl, SC_ENDURE);
// src/map/status.cpp:13723
if(status->hp > 200 && sc && sc->getSCE(SC__BLOODYLUST)) {
// src/map/status.cpp:13724
status_percent_heal(bl, 100, 0);
// src/map/status.cpp:13725
status_change_end(bl, SC__BLOODYLUST);
// src/map/status.cpp:13726
} else if (status->hp > 100 && val2) // If val2 is removed, no HP penalty (dispelled?) [Skotlex]
// src/map/status.cpp:13730
status_change_end(bl, SC_ENDURE);
// src/map/status.cpp:13732
sc_start4(bl, bl, SC_REGENERATION, 100, 10,0,0,(RGN_HP|RGN_SP), skill_get_time(LK_BERSERK, val1));
```

### Spiral Pierce (`LK_SPIRALPIERCE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：4；命中类型：Multi_Hit；段数：5；属性：Weapon；吟唱：Lv1=300; Lv2=500; Lv3=700; Lv4=900; Lv5=1000 ms；技能后摇：Lv1=1200; Lv2=1400; Lv3=1600; Lv4=1800; Lv5=2000 ms；持续时间2：1000 ms；伤害标记：IgnoreDefense；消耗/限制：SP Lv1=18; Lv2=21; Lv3=24; Lv4=27; Lv5=30；武器 1hSpear, 2hSpear；关联状态：Ankle。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiralPierce`
- 实现文件：`src/map/skills/swordman/spiralpierce.cpp`

#### `SkillSpiralPierce::SkillSpiralPierce`

来源：`src/map/skills/swordman/spiralpierce.cpp:12-13`

```cpp
SkillSpiralPierce::SkillSpiralPierce() : WeaponSkillImpl(LK_SPIRALPIERCE) {
}
```

#### `SkillSpiralPierce::modifyDamageData`

来源：`src/map/skills/swordman/spiralpierce.cpp:15-20`

```cpp
void SkillSpiralPierce::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const map_session_data* sd = BL_CAST(BL_PC, &src);

	if (sd == nullptr)
		dmg.flag = (dmg.flag&~(BF_RANGEMASK|BF_WEAPONMASK))|BF_LONG|BF_MISC;
}
```

#### `SkillSpiralPierce::calculateSkillRatio`

来源：`src/map/skills/swordman/spiralpierce.cpp:22-31`

```cpp
void SkillSpiralPierce::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
#ifdef RENEWAL
	const status_change *sc = status_get_sc(src);

	skillratio += 50 + 50 * skill_lv;
	RE_LVL_DMOD(100);
	if (sc && sc->getSCE(SC_CHARGINGPIERCE_COUNT) && sc->getSCE(SC_CHARGINGPIERCE_COUNT)->val1 >= 10)
		skillratio *= 2;
#endif
}
```

#### `SkillSpiralPierce::applyAdditionalEffects`

来源：`src/map/skills/swordman/spiralpierce.cpp:33-39`

```cpp
void SkillSpiralPierce::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	map_session_data *dstsd = BL_CAST(BL_PC, target);
	mob_data* dstmd = BL_CAST(BL_MOB, target);

	if( dstsd || ( dstmd && !status_bl_has_mode(target,MD_STATUSIMMUNE) ) ) //Does not work on status immune
		sc_start(src,target,SC_ANKLE,100,0,skill_get_time2(getSkillId(),skill_lv));
}
```

#### `SkillSpiralPierce::modifyElement`

来源：`src/map/skills/swordman/spiralpierce.cpp:41-44`

```cpp
void SkillSpiralPierce::modifyElement(const Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv, int32& element, int32 flag) const {
	if (src.type != BL_PC)
		element = ELE_NEUTRAL; // forced neutral for monsters
}
```

### Traumatic Blow (`LK_HEADCRUSH`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：4；命中类型：Single；段数：1；属性：Weapon；技能后摇：500 ms；持续时间2：120000 ms；消耗/限制：SP 23；关联状态：Bleeding。

- 覆盖：`exact-class-methods`
- 实现类：`SkillTraumaticBlow`
- 实现文件：`src/map/skills/swordman/traumaticblow.cpp`

#### `SkillTraumaticBlow::SkillTraumaticBlow`

来源：`src/map/skills/swordman/traumaticblow.cpp:10-11`

```cpp
SkillTraumaticBlow::SkillTraumaticBlow() : WeaponSkillImpl(LK_HEADCRUSH) {
}
```

#### `SkillTraumaticBlow::calculateSkillRatio`

来源：`src/map/skills/swordman/traumaticblow.cpp:13-15`

```cpp
void SkillTraumaticBlow::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 40 * skill_lv;
}
```

#### `SkillTraumaticBlow::castendDamageId`

来源：`src/map/skills/swordman/traumaticblow.cpp:17-27`

```cpp
void SkillTraumaticBlow::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	if (status_get_class_(target) == CLASS_BOSS) {
		if (sd)
			clif_skill_fail( *sd, getSkillId() );
		return;
	}

	WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, flag);
}
```

#### `SkillTraumaticBlow::applyAdditionalEffects`

来源：`src/map/skills/swordman/traumaticblow.cpp:29-35`

```cpp
void SkillTraumaticBlow::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	status_data* tstatus = status_get_status_data(*target);

	 // Headcrush has chance of causing Bleeding status, except on demon and undead element
	if (!(battle_check_undead(tstatus->race, tstatus->def_ele) || tstatus->race == RC_DEMON))
		sc_start2(src,target, SC_BLEEDING,50, skill_lv, src->id, skill_get_time2(getSkillId(),skill_lv));
}
```

### Vital Strike (`LK_JOINTBEAT`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：4；命中类型：Single；段数：1；属性：Weapon；技能后摇：Lv1-5=800; Lv6-10=1000 ms；持续时间2：30000 ms；消耗/限制：SP Lv1-2=12; Lv3-4=14; Lv5-6=16; Lv7-8=18; Lv9-10=20；武器 1hSpear, 2hSpear；关联状态：JointBeat。

- 覆盖：`exact-class-methods`
- 实现类：`SkillVitalStrike`
- 实现文件：`src/map/skills/swordman/vitalstrike.cpp`

#### `SkillVitalStrike::SkillVitalStrike`

来源：`src/map/skills/swordman/vitalstrike.cpp:8-9`

```cpp
SkillVitalStrike::SkillVitalStrike() : SkillImpl(LK_JOINTBEAT) {
}
```

#### `SkillVitalStrike::calculateSkillRatio`

来源：`src/map/skills/swordman/vitalstrike.cpp:11-19`

```cpp
void SkillVitalStrike::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_change *tsc = status_get_sc(target);

	base_skillratio += 10 * skill_lv - 50;

	// The 2x damage is only for the BREAK_NECK ailment.
	if (wd->miscflag & BREAK_NECK || (tsc && tsc->getSCE(SC_JOINTBEAT) && tsc->getSCE(SC_JOINTBEAT)->val2 & BREAK_NECK))
		base_skillratio *= 2;
}
```

#### `SkillVitalStrike::castendDamageId`

来源：`src/map/skills/swordman/vitalstrike.cpp:21-30`

```cpp
void SkillVitalStrike::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);
	status_change *tsc = status_get_sc(target);

	flag = 1 << rnd() % 6;
	if (flag != BREAK_NECK && tsc && tsc->getSCE(SC_JOINTBEAT) && tsc->getSCE(SC_JOINTBEAT)->val2 & BREAK_NECK)
		flag = BREAK_NECK; // Target should always receive double damage if neck is already broken
	if (skill_attack(BF_WEAPON, src, src, target, getSkillId(), skill_lv, tick, flag))
		status_change_start(src, target, SC_JOINTBEAT, (50 * (skill_lv + 1) - (270 * tstatus->str) / 100) * 10, skill_lv, flag & BREAK_FLAGS, src->id, 0, skill_get_time2(getSkillId(), skill_lv), SCSTART_NONE);
}
```
