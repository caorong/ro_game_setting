# Mage 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 9 | `MG_SRECOVERY` / Increase SP Recovery | `core-source-references` | `` | src/map/pc.cpp, src/map/skill.cpp, src/map/skills/acolyte/competentia.cpp, src/map/skills/merchant/aidberserkpotion.cpp, src/map/skills/merchant/aidcondensedpotion.cpp, src/map/skills/merchant/aidpotion.cpp, src/map/skills/other/netsupport.cpp, src/map/status.cpp |
| 10 | `MG_SIGHT` / Sight | `exact-class-methods` | `SkillSight` | src/map/skills/mage/sight.cpp |
| 11 | `MG_NAPALMBEAT` / Napalm Beat | `exact-class-methods` | `SkillNapalmBeat` | src/map/skills/mage/napalmbeat.cpp |
| 12 | `MG_SAFETYWALL` / Safety Wall | `exact-class-methods` | `SkillSafetyWall` | src/map/skills/mage/safetywall.cpp |
| 13 | `MG_SOULSTRIKE` / Soul Strike | `exact-class-methods` | `SkillSoulStrike` | src/map/skills/mage/soulstrike.cpp |
| 14 | `MG_COLDBOLT` / Cold Bolt | `exact-class-methods` | `SkillColdBolt` | src/map/skills/mage/coldbolt.cpp |
| 15 | `MG_FROSTDIVER` / Frost Diver | `exact-class-methods` | `SkillFrostDiver` | src/map/skills/mage/frostdiver.cpp |
| 16 | `MG_STONECURSE` / Stone Curse | `exact-class-methods` | `SkillStoneCurse` | src/map/skills/mage/stonecurse.cpp |
| 17 | `MG_FIREBALL` / Fire Ball | `exact-class-methods` | `SkillFireBall` | src/map/skills/mage/fireball.cpp |
| 18 | `MG_FIREWALL` / Fire Wall | `exact-class-methods` | `SkillFireWall` | src/map/skills/mage/firewall.cpp |
| 19 | `MG_FIREBOLT` / Fire Bolt | `exact-class-methods` | `SkillFireBolt` | src/map/skills/mage/firebolt.cpp |
| 20 | `MG_LIGHTNINGBOLT` / Lightning Bolt | `exact-class-methods` | `SkillLightningBolt` | src/map/skills/mage/lightningbolt.cpp |
| 21 | `MG_THUNDERSTORM` / Thunderstorm | `exact-class-methods` | `SkillThunderStorm` | src/map/skills/mage/thunderstorm.cpp |
| 157 | `MG_ENERGYCOAT` / Energy Coat | `exact-class-methods` | `SkillEnergyCoat` | src/map/skills/mage/energycoat.cpp |

## 详细公式与效果实现

### Increase SP Recovery (`MG_SRECOVERY`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/competentia.cpp`, `src/map/skills/merchant/aidberserkpotion.cpp`, `src/map/skills/merchant/aidcondensedpotion.cpp`, `src/map/skills/merchant/aidpotion.cpp`, `src/map/skills/other/netsupport.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:10719
if (sd->sc.getSCE(SC_INCHEALRATE))
// src/map/pc.cpp:10720
bonus += bonus * sd->sc.getSCE(SC_INCHEALRATE)->val1 / 100;
// src/map/pc.cpp:10722
tmp = hp * bonus / 100; // Overflow check
// src/map/pc.cpp:10723
if (bonus != 100 && tmp > hp)
// src/map/pc.cpp:10724
hp = tmp;
// src/map/pc.cpp:10726
if (sp) {
// src/map/pc.cpp:10733
bonus += sd->bonus.itemsphealrate2;
// src/map/pc.cpp:10735
bonus += bonus * pc_get_itemgroup_bonus( sd, itemid, sd->itemgroupsphealrate ) / 100;
// src/map/pc.cpp:10737
for( const auto &it : sd->itemsphealrate ){
// src/map/skill.cpp:7337
int32 hp, sp;
// src/map/skill.cpp:7339
switch( sg->skill_lv ) {
// src/map/skill.cpp:7340
case 1: case 2: hp = 3; sp = 2; break;
// src/map/skill.cpp:7341
case 3: case 4: hp = 4; sp = 3; break;
// src/map/skill.cpp:7342
case 5: default: hp = 5; sp = 4; break;
// src/map/skill.cpp:7344
hp = tstatus->max_hp * hp / 100;
// src/map/skill.cpp:7345
sp = tstatus->max_sp * sp / 100;
```

### Sight (`MG_SIGHT`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；段数：1；属性：Fire；范围：3；持续时间1：10000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 10；关联状态：Sight。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSight`
- 实现文件：`src/map/skills/mage/sight.cpp`

#### `SkillSight::SkillSight`

来源：`src/map/skills/mage/sight.cpp:9-10`

```cpp
SkillSight::SkillSight() : SkillImpl(MG_SIGHT) {
}
```

#### `SkillSight::castendNoDamageId`

来源：`src/map/skills/mage/sight.cpp:12-17`

```cpp
void SkillSight::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	sc_type type = skill_get_sc(getSkillId());

	clif_skill_nodamage(src, *target, getSkillId(), skill_lv,
	                    sc_start2(src, target, type, 100, skill_lv, getSkillId(), skill_get_time(getSkillId(), skill_lv)));
}
```

### Napalm Beat (`MG_NAPALMBEAT`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Ghost；范围：1；吟唱：1000 ms；技能后摇：Lv1-3=1000; Lv4-5=900; Lv6-7=800; Lv8=700; Lv9=600; Lv10=500 ms；伤害标记：Splash, SplashSplit；消耗/限制：SP Lv1-3=9; Lv4-6=12; Lv7-9=15; Lv10=18。

- 覆盖：`exact-class-methods`
- 实现类：`SkillNapalmBeat`
- 实现文件：`src/map/skills/mage/napalmbeat.cpp`

#### `SkillNapalmBeat::SkillNapalmBeat`

来源：`src/map/skills/mage/napalmbeat.cpp:6-7`

```cpp
SkillNapalmBeat::SkillNapalmBeat() : SkillImplRecursiveDamageSplash(MG_NAPALMBEAT) {
}
```

#### `SkillNapalmBeat::calculateSkillRatio`

来源：`src/map/skills/mage/napalmbeat.cpp:9-11`

```cpp
void SkillNapalmBeat::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += -30 + 10 * skill_lv;
}
```

#### `SkillNapalmBeat::castendDamageId`

来源：`src/map/skills/mage/napalmbeat.cpp:13-15`

```cpp
void SkillNapalmBeat::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	SkillImplRecursiveDamageSplash::castendDamageId(src, target, skill_lv, tick, flag);
}
```

### Safety Wall (`MG_SAFETYWALL`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：1；属性：Ghost；吟唱：Lv1=4000; Lv2-3=3500; Lv4=2500; Lv5=2000; Lv6=1500; Lv7-10=1000 ms；持续时间1：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000; Lv6=30000; Lv7=35000; Lv8=40000; Lv9=45000; Lv10=50000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-3=30; Lv4-6=35; Lv7-10=40；道具 Blue_Gemstone×1；关联状态：Safetywall。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSafetyWall`
- 实现文件：`src/map/skills/mage/safetywall.cpp`

#### `SkillSafetyWall::SkillSafetyWall`

来源：`src/map/skills/mage/safetywall.cpp:6-7`

```cpp
SkillSafetyWall::SkillSafetyWall() : SkillImpl(MG_SAFETYWALL) {
}
```

#### `SkillSafetyWall::castendPos2`

来源：`src/map/skills/mage/safetywall.cpp:9-23`

```cpp
void SkillSafetyWall::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	int32 dummy = 1;

	if (map_foreachincell(skill_cell_overlap, src->m, x, y, BL_SKILL, getSkillId(), &dummy, src)) {
		skill_unitsetting(src, getSkillId(), skill_lv, x, y, 0);
		// Don't consume gems if cast on Land Protector
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}

	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Soul Strike (`MG_SOULSTRIKE`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1-2=1; Lv3-4=2; Lv5-6=3; Lv7-8=4; Lv9-10=5；属性：Ghost；吟唱：500 ms；技能后摇：Lv1=1200; Lv2=1000; Lv3=1400; Lv4=1200; Lv5=1600; Lv6=1400; Lv7=1800; Lv8=1600; Lv9=2000; Lv10=1800 ms；消耗/限制：SP Lv1=18; Lv2=14; Lv3=24; Lv4=20; Lv5=30; Lv6=26; Lv7=36; Lv8=32; Lv9=42; Lv10=38。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSoulStrike`
- 实现文件：`src/map/skills/mage/soulstrike.cpp`

#### `SkillSoulStrike::SkillSoulStrike`

来源：`src/map/skills/mage/soulstrike.cpp:8-9`

```cpp
SkillSoulStrike::SkillSoulStrike() : SkillImpl(MG_SOULSTRIKE) {
}
```

#### `SkillSoulStrike::calculateSkillRatio`

来源：`src/map/skills/mage/soulstrike.cpp:11-16`

```cpp
void SkillSoulStrike::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_data *tstatus = status_get_status_data(*target);

	if (battle_check_undead(tstatus->race, tstatus->def_ele))
		base_skillratio += 5 * skill_lv;
}
```

#### `SkillSoulStrike::castendDamageId`

来源：`src/map/skills/mage/soulstrike.cpp:18-20`

```cpp
void SkillSoulStrike::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

### Cold Bolt (`MG_COLDBOLT`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Water；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800; Lv6=2000; Lv7=2200; Lv8=2400; Lv9=2600; Lv10=2800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30。

- 覆盖：`exact-class-methods`
- 实现类：`SkillColdBolt`
- 实现文件：`src/map/skills/mage/coldbolt.cpp`

#### `SkillColdBolt::SkillColdBolt`

来源：`src/map/skills/mage/coldbolt.cpp:9-10`

```cpp
SkillColdBolt::SkillColdBolt() : SkillImpl(MG_COLDBOLT) {
}
```

#### `SkillColdBolt::calculateSkillRatio`

来源：`src/map/skills/mage/coldbolt.cpp:12-24`

```cpp
void SkillColdBolt::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_change *sc = status_get_sc(src);

	if (sc) {
		if (sc->getSCE(SC_COLD_FORCE_OPTION))
			base_skillratio *= 5;

		if (sc->getSCE(SC_SPELLFIST) && mflag & BF_SHORT) {
			base_skillratio += (sc->getSCE(SC_SPELLFIST)->val3 * 100) + (sc->getSCE(SC_SPELLFIST)->val1 * 50 - 50) - 100;
			// val3 = used bolt level, val1 = used spellfist level. [Rytech]
		}
	}
}
```

#### `SkillColdBolt::castendDamageId`

来源：`src/map/skills/mage/coldbolt.cpp:26-28`

```cpp
void SkillColdBolt::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

#### `SkillColdBolt::modifyDamageData`

来源：`src/map/skills/mage/coldbolt.cpp:30-40`

```cpp
void SkillColdBolt::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const status_change* sc = status_get_sc(&src);

	if (sc != nullptr) {
		if (sc->hasSCE(SC_SPELLFIST) && (dmg.miscflag & BF_SHORT)) {
			dmg.div_ = 1; // ad mods, to make it work similar to regular hits [Xazax]
			dmg.flag = BF_WEAPON | BF_SHORT;
			dmg.type = DMG_NORMAL;
		}
	}
}
```

### Frost Diver (`MG_FROSTDIVER`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Water；吟唱：800 ms；技能后摇：1500 ms；持续时间2：Lv1=3000; Lv2=6000; Lv3=9000; Lv4=12000; Lv5=15000; Lv6=18000; Lv7=21000; Lv8=24000; Lv9=27000; Lv10-11=30000 ms；消耗/限制：SP Lv1=25; Lv2=24; Lv3=23; Lv4=22; Lv5=21; Lv6=20; Lv7=19; Lv8=18; Lv9=17; Lv10=16；关联状态：Freeze。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFrostDiver`
- 实现文件：`src/map/skills/mage/frostdiver.cpp`

#### `SkillFrostDiver::SkillFrostDiver`

来源：`src/map/skills/mage/frostdiver.cpp:10-11`

```cpp
SkillFrostDiver::SkillFrostDiver() : SkillImpl(MG_FROSTDIVER) {
}
```

#### `SkillFrostDiver::calculateSkillRatio`

来源：`src/map/skills/mage/frostdiver.cpp:13-15`

```cpp
void SkillFrostDiver::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 10 * skill_lv;
}
```

#### `SkillFrostDiver::castendDamageId`

来源：`src/map/skills/mage/frostdiver.cpp:17-19`

```cpp
void SkillFrostDiver::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

#### `SkillFrostDiver::applyAdditionalEffects`

来源：`src/map/skills/mage/frostdiver.cpp:21-25`

```cpp
void SkillFrostDiver::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	if (!sc_start(src, target, SC_FREEZE, min(skill_lv * 3 + 35, skill_lv + 60), skill_lv, skill_get_time2(getSkillId(), skill_lv)) && sd)
		clif_skill_fail(*sd, getSkillId());
}
```

### Stone Curse (`MG_STONECURSE`)

魔法技能；目标：敌方目标；最高等级 10；射程：2；命中类型：Single；段数：1；属性：Earth；吟唱：1000 ms；持续时间1：5000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=25; Lv2=24; Lv3=23; Lv4=22; Lv5=21; Lv6=20; Lv7=19; Lv8=18; Lv9=17; Lv10=16；道具 Red_Gemstone×1；关联状态：StoneWait。

- 覆盖：`exact-class-methods`
- 实现类：`SkillStoneCurse`
- 实现文件：`src/map/skills/mage/stonecurse.cpp`

#### `SkillStoneCurse::SkillStoneCurse`

来源：`src/map/skills/mage/stonecurse.cpp:10-11`

```cpp
SkillStoneCurse::SkillStoneCurse() : SkillImpl(MG_STONECURSE) {
}
```

#### `SkillStoneCurse::castendNoDamageId`

来源：`src/map/skills/mage/stonecurse.cpp:13-45`

```cpp
void SkillStoneCurse::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	status_data *tstatus = status_get_status_data(*target);
	status_change *tsc = status_get_sc(&*target);
	sc_type type = skill_get_sc(getSkillId());

	if (status_has_mode(tstatus, MD_STATUSIMMUNE)) {
		if (sd)
			clif_skill_fail(*sd, getSkillId());
		return;
	}

	if (status_isimmune(target) || !tsc)
		return;

	int32 brate = 0;

	if (sd && sd->sc.getSCE(SC_PETROLOGY_OPTION))
		brate = sd->sc.getSCE(SC_PETROLOGY_OPTION)->val3;

	// Except for players, the skill animation shows even if the status change doesn't start
	// Players get a skill has failed message instead
	if (sc_start2(src, target, type, (skill_lv * 4 + 20) + brate, skill_lv, src->id, skill_get_time2(getSkillId(), skill_lv), skill_get_time(getSkillId(), skill_lv)) || sd == nullptr)
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
	else {
		clif_skill_fail( *sd, getSkillId() );
		// Level 6-10 doesn't consume a red gem if it fails [celest]
		if (skill_lv > 5)
		{ // not to consume items
			flag |= SKILL_NOCONSUME_REQ;
		}
	}
}
```

### Fire Ball (`MG_FIREBALL`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Fire；范围：Lv1-10=2; Lv11=3；吟唱：Lv1-5=1500; Lv6-10=1000 ms；技能后摇：Lv1-5=1500; Lv6-10=1000 ms；伤害标记：Splash；消耗/限制：SP 25。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFireBall`
- 实现文件：`src/map/skills/mage/fireball.cpp`

#### `SkillFireBall::SkillFireBall`

来源：`src/map/skills/mage/fireball.cpp:8-9`

```cpp
SkillFireBall::SkillFireBall() : SkillImplRecursiveDamageSplash(MG_FIREBALL) {
}
```

#### `SkillFireBall::calculateSkillRatio`

来源：`src/map/skills/mage/fireball.cpp:11-19`

```cpp
void SkillFireBall::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 40 + 20 * skill_lv;
#else
	base_skillratio += -30 + 10 * skill_lv;
#endif
	if (wd->miscflag == 2) //Enemies at the edge of the area will take 75% of the damage
		base_skillratio = base_skillratio * 3 / 4;
}
```

#### `SkillFireBall::castendDamageId`

来源：`src/map/skills/mage/fireball.cpp:21-23`

```cpp
void SkillFireBall::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	SkillImplRecursiveDamageSplash::castendDamageId(src, target, skill_lv, tick, flag);
}
```

#### `SkillFireBall::splashDamage`

来源：`src/map/skills/mage/fireball.cpp:25-34`

```cpp
int64 SkillFireBall::splashDamage(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 flag) const {
	// For players, the distance between original target and splash target determines the damage
	if( map_session_data* sd = BL_CAST( BL_PC, src ); sd != nullptr ){
		if (block_list* orig_bl = map_id2bl(skill_area_temp[1]); orig_bl != nullptr)
			flag |= distance_bl(orig_bl, target);
	}

	// Call default implementation
	return SkillImplRecursiveDamageSplash::splashDamage(src, target, skill_lv, tick, flag);
}
```

### Fire Wall (`MG_FIREWALL`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Fire；击退：2；吟唱：Lv1=2000; Lv2=1850; Lv3=1700; Lv4=1550; Lv5=1400; Lv6=1250; Lv7=1100; Lv8=950; Lv9=800; Lv10=650 ms；持续时间1：Lv1=5000; Lv2=6000; Lv3=7000; Lv4=8000; Lv5=9000; Lv6=10000; Lv7=11000; Lv8=12000; Lv9=13000; Lv10=14000 ms；消耗/限制：SP 40。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFireWall`
- 实现文件：`src/map/skills/mage/firewall.cpp`

#### `SkillFireWall::SkillFireWall`

来源：`src/map/skills/mage/firewall.cpp:8-9`

```cpp
SkillFireWall::SkillFireWall() : SkillImpl(MG_FIREWALL) {
}
```

#### `SkillFireWall::castendPos2`

来源：`src/map/skills/mage/firewall.cpp:11-16`

```cpp
void SkillFireWall::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillFireWall::calculateSkillRatio`

来源：`src/map/skills/mage/firewall.cpp:18-20`

```cpp
void SkillFireWall::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio -= 50;
}
```

#### `SkillFireWall::modifyDamageData`

来源：`src/map/skills/mage/firewall.cpp:22-28`

```cpp
void SkillFireWall::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const status_data* tstatus = status_get_status_data(target);

	if (tstatus->def_ele == ELE_FIRE || battle_check_undead(tstatus->race, tstatus->def_ele)) {
		dmg.blewcount = 0; // No knockback
	}
}
```

### Fire Bolt (`MG_FIREBOLT`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Fire；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800; Lv6=2000; Lv7=2200; Lv8=2400; Lv9=2600; Lv10=2800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFireBolt`
- 实现文件：`src/map/skills/mage/firebolt.cpp`

#### `SkillFireBolt::SkillFireBolt`

来源：`src/map/skills/mage/firebolt.cpp:9-10`

```cpp
SkillFireBolt::SkillFireBolt() : SkillImpl(MG_FIREBOLT) {
}
```

#### `SkillFireBolt::calculateSkillRatio`

来源：`src/map/skills/mage/firebolt.cpp:12-24`

```cpp
void SkillFireBolt::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_change *sc = status_get_sc(src);

	if (sc) {
		if (sc->getSCE(SC_FLAMETECHNIC_OPTION))
			base_skillratio *= 5;

		if (sc->getSCE(SC_SPELLFIST) && mflag & BF_SHORT) {
			base_skillratio += (sc->getSCE(SC_SPELLFIST)->val3 * 100) + (sc->getSCE(SC_SPELLFIST)->val1 * 50 - 50) - 100;
			// val3 = used bolt level, val1 = used spellfist level. [Rytech]
		}
	}
}
```

#### `SkillFireBolt::castendDamageId`

来源：`src/map/skills/mage/firebolt.cpp:26-28`

```cpp
void SkillFireBolt::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

#### `SkillFireBolt::modifyDamageData`

来源：`src/map/skills/mage/firebolt.cpp:30-40`

```cpp
void SkillFireBolt::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const status_change* sc = status_get_sc(&src);

	if (sc != nullptr) {
		if (sc->hasSCE(SC_SPELLFIST) && (dmg.miscflag & BF_SHORT)) {
			dmg.div_ = 1; // ad mods, to make it work similar to regular hits [Xazax]
			dmg.flag = BF_WEAPON | BF_SHORT;
			dmg.type = DMG_NORMAL;
		}
	}
}
```

### Lightning Bolt (`MG_LIGHTNINGBOLT`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Wind；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800; Lv6=2000; Lv7=2200; Lv8=2400; Lv9=2600; Lv10=2800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30。

- 覆盖：`exact-class-methods`
- 实现类：`SkillLightningBolt`
- 实现文件：`src/map/skills/mage/lightningbolt.cpp`

#### `SkillLightningBolt::SkillLightningBolt`

来源：`src/map/skills/mage/lightningbolt.cpp:9-10`

```cpp
SkillLightningBolt::SkillLightningBolt() : SkillImpl(MG_LIGHTNINGBOLT) {
}
```

#### `SkillLightningBolt::calculateSkillRatio`

来源：`src/map/skills/mage/lightningbolt.cpp:12-24`

```cpp
void SkillLightningBolt::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_change *sc = status_get_sc(src);

	if (sc) {
		if (sc->getSCE(SC_GRACE_BREEZE_OPTION))
			base_skillratio *= 5;

		if (sc->getSCE(SC_SPELLFIST) && mflag & BF_SHORT) {
			base_skillratio += (sc->getSCE(SC_SPELLFIST)->val3 * 100) + (sc->getSCE(SC_SPELLFIST)->val1 * 50 - 50) - 100;
			// val3 = used bolt level, val1 = used spellfist level. [Rytech]
		}
	}
}
```

#### `SkillLightningBolt::castendDamageId`

来源：`src/map/skills/mage/lightningbolt.cpp:26-28`

```cpp
void SkillLightningBolt::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

#### `SkillLightningBolt::modifyDamageData`

来源：`src/map/skills/mage/lightningbolt.cpp:30-40`

```cpp
void SkillLightningBolt::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const status_change* sc = status_get_sc(&src);

	if (sc != nullptr) {
		if (sc->hasSCE(SC_SPELLFIST) && (dmg.miscflag & BF_SHORT)) {
			dmg.div_ = 1; // ad mods, to make it work similar to regular hits [Xazax]
			dmg.flag = BF_WEAPON | BF_SHORT;
			dmg.type = DMG_NORMAL;
		}
	}
}
```

### Thunderstorm (`MG_THUNDERSTORM`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Wind；吟唱：Lv1=1000; Lv2=2000; Lv3=3000; Lv4=4000; Lv5=5000; Lv6=6000; Lv7=7000; Lv8=8000; Lv9=9000; Lv10=10000 ms；技能后摇：2000 ms；持续时间1：100 ms；消耗/限制：SP Lv1=29; Lv2=34; Lv3=39; Lv4=44; Lv5=49; Lv6=54; Lv7=59; Lv8=64; Lv9=69; Lv10=74。

- 覆盖：`exact-class-methods`
- 实现类：`SkillThunderStorm`
- 实现文件：`src/map/skills/mage/thunderstorm.cpp`

#### `SkillThunderStorm::SkillThunderStorm`

来源：`src/map/skills/mage/thunderstorm.cpp:6-7`

```cpp
SkillThunderStorm::SkillThunderStorm() : SkillImpl(MG_THUNDERSTORM) {
}
```

#### `SkillThunderStorm::castendPos2`

来源：`src/map/skills/mage/thunderstorm.cpp:9-14`

```cpp
void SkillThunderStorm::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillThunderStorm::calculateSkillRatio`

来源：`src/map/skills/mage/thunderstorm.cpp:16-21`

```cpp
void SkillThunderStorm::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	// in Renewal Thunder Storm boost is 100% (in pre-re, 80%)
#ifndef RENEWAL
	base_skillratio -= 20;
#endif
}
```

### Energy Coat (`MG_ENERGYCOAT`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：5000 ms；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP 30；关联状态：EnergyCoat。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEnergyCoat`
- 实现文件：`src/map/skills/mage/energycoat.cpp`

#### `SkillEnergyCoat::SkillEnergyCoat`

来源：`src/map/skills/mage/energycoat.cpp:6-7`

```cpp
SkillEnergyCoat::SkillEnergyCoat() : StatusSkillImpl(MG_ENERGYCOAT) {
}
```
