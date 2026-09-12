# Monk 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 259 | `MO_IRONHAND` / Iron Fists | `core-source-references` | `` | src/map/battle.cpp |
| 260 | `MO_SPIRITSRECOVERY` / Spiritual Cadence | `core-source-references` | `` | src/map/status.cpp |
| 261 | `MO_CALLSPIRITS` / Summon Spirit Sphere | `exact-class-methods` | `SkillSummoningSpiritSphere` | src/map/skills/acolyte/summonspiritsphere.cpp |
| 262 | `MO_ABSORBSPIRITS` / Absorb Spirit Sphere | `exact-class-methods` | `SkillAbsorbSpiritSphere` | src/map/skills/acolyte/absorbspiritsphere.cpp |
| 263 | `MO_TRIPLEATTACK` / Raging Trifecta Blow | `exact-class-methods` | `SkillRagingTrifectaBlow` | src/map/skills/acolyte/ragingtrifectablow.cpp |
| 264 | `MO_BODYRELOCATION` / Snap | `exact-class-methods` | `SkillSnap` | src/map/skills/acolyte/snap.cpp |
| 265 | `MO_DODGE` / Dodge | `core-source-references` | `` | src/map/status.cpp |
| 266 | `MO_INVESTIGATE` / Occult Impaction | `exact-class-methods` | `SkillOccultImpaction` | src/map/skills/acolyte/occultimpaction.cpp |
| 267 | `MO_FINGEROFFENSIVE` / Throw Spirit Sphere | `exact-class-methods` | `SkillThrowSpiritSphere` | src/map/skills/acolyte/throwspiritsphere.cpp |
| 268 | `MO_STEELBODY` / Mental Strength | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 269 | `MO_BLADESTOP` / Root | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 270 | `MO_EXPLOSIONSPIRITS` / Fury | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 271 | `MO_EXTREMITYFIST` / Asura Strike | `exact-class-methods` | `SkillAsuraStrike` | src/map/skills/acolyte/asurastrike.cpp |
| 272 | `MO_CHAINCOMBO` / Raging Quadruple Blow | `exact-class-methods` | `SkillRagingQuadrupleBlow` | src/map/skills/acolyte/ragingquadrupleblow.cpp |
| 273 | `MO_COMBOFINISH` / Raging Thrust | `exact-class-methods` | `SkillRagingThrust` | src/map/skills/acolyte/ragingthrust.cpp |
| 1015 | `MO_KITRANSLATION` / Ki Translation | `exact-class-methods` | `SkillKiTranslation` | src/map/skills/acolyte/kitranslation.cpp |
| 1016 | `MO_BALKYOUNG` / Ki Explosion | `exact-class-methods` | `SkillKiExplosion` | src/map/skills/acolyte/kiexplosion.cpp |

## 详细公式与效果实现

### Iron Fists (`MO_IRONHAND`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2369
damage += (skill * 3);
// src/map/battle.cpp:2371
damage += (skill * 4);
// src/map/battle.cpp:2375
damage += (skill * 10);
// src/map/battle.cpp:2379
damage += (skill * 3);
// src/map/battle.cpp:2383
damage += (skill * 3);
// src/map/battle.cpp:2387
damage += (skill * 3);
```

### Spiritual Cadence (`MO_SPIRITSRECOVERY`)

武器/物理技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:5322
sregen->sp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5333
sregen->hp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5343
sregen->sp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5349
val = regen->hp*(100+5*skill)/100;
// src/map/status.cpp:5350
regen->hp = cap_value(val, 1, SHRT_MAX);
// src/map/status.cpp:5353
val = regen->sp*(100+3*skill)/100;
```

### Summon Spirit Sphere (`MO_CALLSPIRITS`)

非伤害技能；目标：自身；最高等级 5；命中类型：Single；段数：1；吟唱：1000 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 8。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSummoningSpiritSphere`
- 实现文件：`src/map/skills/acolyte/summonspiritsphere.cpp`

#### `SkillSummoningSpiritSphere::SkillSummoningSpiritSphere`

来源：`src/map/skills/acolyte/summonspiritsphere.cpp:10-11`

```cpp
SkillSummoningSpiritSphere::SkillSummoningSpiritSphere() : SkillImpl(MO_CALLSPIRITS) {
}
```

#### `SkillSummoningSpiritSphere::castendNoDamageId`

来源：`src/map/skills/acolyte/summonspiritsphere.cpp:13-23`

```cpp
void SkillSummoningSpiritSphere::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if(sd) {
		int32 limit = skill_lv;
		if( sd->sc.getSCE(SC_RAISINGDRAGON) )
			limit += sd->sc.getSCE(SC_RAISINGDRAGON)->val1;
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
		pc_addspiritball(sd,skill_get_time(getSkillId(),skill_lv),limit);
	}
}
```

### Absorb Spirit Sphere (`MO_ABSORBSPIRITS`)

武器/物理技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；吟唱：2000 ms；伤害标记：NoDamage；消耗/限制：SP 5。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAbsorbSpiritSphere`
- 实现文件：`src/map/skills/acolyte/absorbspiritsphere.cpp`

#### `SkillAbsorbSpiritSphere::SkillAbsorbSpiritSphere`

来源：`src/map/skills/acolyte/absorbspiritsphere.cpp:11-12`

```cpp
SkillAbsorbSpiritSphere::SkillAbsorbSpiritSphere() : SkillImpl(MO_ABSORBSPIRITS) {
}
```

#### `SkillAbsorbSpiritSphere::castendNoDamageId`

来源：`src/map/skills/acolyte/absorbspiritsphere.cpp:14-41`

```cpp
void SkillAbsorbSpiritSphere::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);
	mob_data* dstmd = BL_CAST(BL_MOB, target);
	status_data* tstatus = status_get_status_data(*target);

	int32 i = 0;
	if (dstsd && (battle_check_target(src, target, BCT_SELF) > 0 || battle_check_target(src, target, BCT_ENEMY) > 0) && // Only works on self and enemies
		(dstsd->class_&MAPID_FIRSTMASK) != MAPID_GUNSLINGER ) { // split the if for readability, and included gunslingers in the check so that their coins cannot be removed [Reddozen]
		if (dstsd->spiritball > 0) {
			i = dstsd->spiritball * 7;
			pc_delspiritball(dstsd,dstsd->spiritball,0);
		}
		if (dstsd->spiritcharm_type != CHARM_TYPE_NONE && dstsd->spiritcharm > 0) {
			i += dstsd->spiritcharm * 7;
			pc_delspiritcharm(dstsd,dstsd->spiritcharm,dstsd->spiritcharm_type);
		}
	} else if (dstmd && !status_has_mode(tstatus,MD_STATUSIMMUNE) && rnd() % 100 < 20) { // check if target is a monster and not status immune, for the 20% chance to absorb 2 SP per monster's level [Reddozen]
		i = 2 * dstmd->level;
		mob_target(dstmd,src,0);
	} else {
		if (sd)
			clif_skill_fail( *sd, getSkillId() );
		return;
	}
	if (i) status_heal(src, 0, i, 3);
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,i != 0);
}
```

### Raging Trifecta Blow (`MO_TRIPLEATTACK`)

武器/物理技能；目标：被动；最高等级 10；射程：-1；命中类型：Multi_Hit；段数：-3；属性：Weapon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRagingTrifectaBlow`
- 实现文件：`src/map/skills/acolyte/ragingtrifectablow.cpp`

#### `SkillRagingTrifectaBlow::SkillRagingTrifectaBlow`

来源：`src/map/skills/acolyte/ragingtrifectablow.cpp:6-7`

```cpp
SkillRagingTrifectaBlow::SkillRagingTrifectaBlow() : WeaponSkillImpl(MO_TRIPLEATTACK) {
}
```

#### `SkillRagingTrifectaBlow::castendDamageId`

来源：`src/map/skills/acolyte/ragingtrifectablow.cpp:9-13`

```cpp
void SkillRagingTrifectaBlow::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	int32 sflag = flag|SD_ANIMATION;

	WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, sflag);
}
```

#### `SkillRagingTrifectaBlow::calculateSkillRatio`

来源：`src/map/skills/acolyte/ragingtrifectablow.cpp:15-17`

```cpp
void SkillRagingTrifectaBlow::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += 20 * skill_lv;
}
```

### Snap (`MO_BODYRELOCATION`)

非伤害技能；目标：地面区域；最高等级 1；射程：18；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 14；气弹 1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSnap`
- 实现文件：`src/map/skills/acolyte/snap.cpp`

#### `SkillSnap::SkillSnap`

来源：`src/map/skills/acolyte/snap.cpp:12-13`

```cpp
SkillSnap::SkillSnap() : SkillImpl(MO_BODYRELOCATION) {
}
```

#### `SkillSnap::castendPos2`

来源：`src/map/skills/acolyte/snap.cpp:15-27`

```cpp
void SkillSnap::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (unit_movepos(src, x, y, 2, 1)) {
#if PACKETVER >= 20111005
		clif_snap(src, src->x, src->y);
#else
		clif_skill_poseffect( *src, getSkillId(), skill_lv, src->x, src->y, tick );
#endif
		if (sd)
			skill_blockpc_start (*sd, MO_EXTREMITYFIST, 2000);
	}
}
```

### Dodge (`MO_DODGE`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:4507
base_status->hit += skill * 3;
// src/map/status.cpp:4509
base_status->hit += skill * 3;
// src/map/status.cpp:4518
base_status->flee += skill*(sd->class_&JOBL_2 && (sd->class_&MAPID_FIRSTMASK) == MAPID_THIEF? 4 : 3);
// src/map/status.cpp:4520
base_status->flee += (skill*3) / 2;
// src/map/status.cpp:4522
base_status->flee += 20;
// src/map/status.cpp:4524
base_status->flee += skill * 10;
// src/map/status.cpp:4530
base_status->cri += skill * 10;
```

### Occult Impaction (`MO_INVESTIGATE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：2；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；伤害标记：IgnoreFlee；消耗/限制：SP Lv1=10; Lv2=14; Lv3=17; Lv4=19; Lv5=20；气弹 1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillOccultImpaction`
- 实现文件：`src/map/skills/acolyte/occultimpaction.cpp`

#### `SkillOccultImpaction::SkillOccultImpaction`

来源：`src/map/skills/acolyte/occultimpaction.cpp:8-9`

```cpp
SkillOccultImpaction::SkillOccultImpaction() : WeaponSkillImpl(MO_INVESTIGATE) {
}
```

#### `SkillOccultImpaction::castendDamageId`

来源：`src/map/skills/acolyte/occultimpaction.cpp:11-14`

```cpp
void SkillOccultImpaction::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, flag);
	status_change_end(src, SC_BLADESTOP);
}
```

#### `SkillOccultImpaction::calculateSkillRatio`

来源：`src/map/skills/acolyte/occultimpaction.cpp:16-26`

```cpp
void SkillOccultImpaction::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const status_change* tsc = status_get_sc(target);

	base_skillratio += -100 + 100 * skill_lv;
	if (tsc && tsc->getSCE(SC_BLADESTOP))
		base_skillratio += base_skillratio / 2;
#else
	base_skillratio += 75 * skill_lv;
#endif
}
```

### Throw Spirit Sphere (`MO_FINGEROFFENSIVE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；属性：Weapon；吟唱：1000 ms；技能后摇：500 ms；移动后摇：Lv2=200; Lv3=400; Lv4=600; Lv5=800 ms；消耗/限制：SP 10；气弹 Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5。

- 覆盖：`exact-class-methods`
- 实现类：`SkillThrowSpiritSphere`
- 实现文件：`src/map/skills/acolyte/throwspiritsphere.cpp`

#### `SkillThrowSpiritSphere::SkillThrowSpiritSphere`

来源：`src/map/skills/acolyte/throwspiritsphere.cpp:12-13`

```cpp
SkillThrowSpiritSphere::SkillThrowSpiritSphere() : WeaponSkillImpl(MO_FINGEROFFENSIVE) {
}
```

#### `SkillThrowSpiritSphere::modifyDamageData`

来源：`src/map/skills/acolyte/throwspiritsphere.cpp:15-26`

```cpp
void SkillThrowSpiritSphere::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const map_session_data* sd = BL_CAST(BL_PC, &src);

	if (sd != nullptr) {
		if (battle_config.finger_offensive_type)
			dmg.div_ = 1;
#ifndef RENEWAL
		else if ((sd->spiritball + sd->spiritball_old) < dmg.div_)
			dmg.div_ = sd->spiritball + sd->spiritball_old;
#endif
	}
}
```

#### `SkillThrowSpiritSphere::castendDamageId`

来源：`src/map/skills/acolyte/throwspiritsphere.cpp:28-37`

```cpp
void SkillThrowSpiritSphere::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, flag);
	if (battle_config.finger_offensive_type && sd) {
		for (int32 i = 1; i < sd->spiritball_old; i++)
			skill_addtimerskill(src, tick + i * 200, target->id, 0, 0, getSkillId(), skill_lv, BF_WEAPON, flag);
	}
	status_change_end(src, SC_BLADESTOP);
}
```

#### `SkillThrowSpiritSphere::calculateSkillRatio`

来源：`src/map/skills/acolyte/throwspiritsphere.cpp:39-49`

```cpp
void SkillThrowSpiritSphere::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const status_change* tsc = status_get_sc(target);

	base_skillratio += 500 + skill_lv * 200;
	if (tsc && tsc->getSCE(SC_BLADESTOP))
		base_skillratio += base_skillratio / 2;
#else
	base_skillratio += 50 * skill_lv;
#endif
}
```

### Mental Strength (`MO_STEELBODY`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；吟唱：5000 ms；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000 ms；伤害标记：NoDamage；消耗/限制：SP 200；气弹 5；关联状态：SteelBody。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:9785
status_percent_heal(sd, 100, 100);
// src/map/pc.cpp:9788
sc_start(sd,sd,SC_STEELBODY,100,5,skill_get_time(MO_STEELBODY,5));
// src/map/pc.cpp:9799
status_change_end(devsd, SC_DEVOTION);
```

### Root (`MO_BLADESTOP`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：Lv1=500; Lv2=700; Lv3=900; Lv4=1100; Lv5=1300 ms；持续时间2：Lv1=20000; Lv2=30000; Lv3=40000; Lv4=50000; Lv5=60000 ms；伤害标记：NoDamage；消耗/限制：SP 10；气弹 1；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；关联状态：BladeStop_Wait。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:7250
uint16 skill_lv = tsc->getSCE(SC_BLADESTOP_WAIT)->val1;
// src/map/battle.cpp:7251
int32 duration = skill_get_time2(MO_BLADESTOP,skill_lv);
// src/map/battle.cpp:7255
duration = 2000; // Only lasts 2 seconds for Boss monsters
// src/map/battle.cpp:7257
status_change_end(target, SC_BLADESTOP_WAIT);
// src/map/battle.cpp:7258
if(sc_start4(src,src, SC_BLADESTOP, 100, sd?pc_checkskill(sd, MO_BLADESTOP):5, 0, 0, target->id, duration))
// src/map/battle.cpp:7260
clif_damage(*src, *target, tick, sstatus->amotion, 1, 0, 1, DMG_NORMAL, 0, false); //Display MISS.
// src/map/battle.cpp:7262
sc_start4(src,target, SC_BLADESTOP, 100, skill_lv, 0, 0, src->id, duration);
// src/map/battle.cpp:7269
int32 triple_rate = 30; //Base Rate
// src/map/skills/acolyte/skill_factory_acolyte.cpp:260
case IQ_THIRD_CONSECRATION:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:261
return std::make_unique<SkillThirdConsecration>();
```

### Fury (`MO_EXPLOSIONSPIRITS`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 15；气弹 5；关联状态：ExplosionSpirits。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Asura Strike (`MO_EXTREMITYFIST`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：-2；命中类型：Single；段数：1；吟唱：Lv1=4000; Lv2=3500; Lv3=3000; Lv4=2500; Lv5=2000 ms；技能后摇：Lv1=3000; Lv2=2500; Lv3=2000; Lv4=1500; Lv5=1000 ms；持续时间1：300000 ms；伤害标记：IgnoreDefense, IgnoreFlee；消耗/限制：SP 1；气弹 5；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；前置状态 Explosionspirits；关联状态：ExtremityFist。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAsuraStrike`
- 实现文件：`src/map/skills/acolyte/asurastrike.cpp`

#### `SkillAsuraStrike::SkillAsuraStrike`

来源：`src/map/skills/acolyte/asurastrike.cpp:13-14`

```cpp
SkillAsuraStrike::SkillAsuraStrike() : WeaponSkillImpl(MO_EXTREMITYFIST) {
}
```

#### `SkillAsuraStrike::castendDamageId`

来源：`src/map/skills/acolyte/asurastrike.cpp:16-50`

```cpp
void SkillAsuraStrike::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	int16 x, y, i = 3; // Move 3 cells (From caster)
	int16 dir = map_calc_dir(src,target->x,target->y);

#ifdef RENEWAL
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd && sd->spiritball_old > 5)
		flag |= 1; // Give +100% damage increase
#endif
	WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, flag);

	status_set_sp(src, 0, 0);
	sc_start(src, src, SC_EXTREMITYFIST, 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
	status_change_end(src, SC_EXPLOSIONSPIRITS);
	status_change_end(src, SC_BLADESTOP);

	if (dir > 0 && dir < 4)
		x = -i;
	else if (dir > 4)
		x = i;
	else
		x = 0;
	if (dir > 2 && dir < 6)
		y = -i;
	else if (dir == 7 || dir < 2)
		y = i;
	else
		y = 0;

	if (unit_movepos(src, src->x + x, src->y + y, 1, 1)) {
		clif_blown(src);
		clif_spiritball(src);
	}
}
```

#### `SkillAsuraStrike::calculateSkillRatio`

来源：`src/map/skills/acolyte/asurastrike.cpp:52-61`

```cpp
void SkillAsuraStrike::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	const status_data* sstatus = status_get_status_data(*src);

	base_skillratio += 700 + sstatus->sp * 10;
#ifdef RENEWAL
	if (wd->miscflag&1)
		base_skillratio *= 2; // More than 5 spirit balls active
#endif
	base_skillratio = min(500000,base_skillratio); //We stop at roughly 50k SP for overflow protection
}
```

### Raging Quadruple Blow (`MO_CHAINCOMBO`)

武器/物理技能；目标：自身；最高等级 5；射程：-2；命中类型：Multi_Hit；段数：-4；属性：Weapon；消耗/限制：SP Lv1=11; Lv2=12; Lv3=13; Lv4=14; Lv5=15；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRagingQuadrupleBlow`
- 实现文件：`src/map/skills/acolyte/ragingquadrupleblow.cpp`

#### `SkillRagingQuadrupleBlow::SkillRagingQuadrupleBlow`

来源：`src/map/skills/acolyte/ragingquadrupleblow.cpp:10-11`

```cpp
SkillRagingQuadrupleBlow::SkillRagingQuadrupleBlow() : WeaponSkillImpl(MO_CHAINCOMBO) {
}
```

#### `SkillRagingQuadrupleBlow::modifyDamageData`

来源：`src/map/skills/acolyte/ragingquadrupleblow.cpp:13-20`

```cpp
void SkillRagingQuadrupleBlow::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
#ifdef RENEWAL
	const map_session_data* sd = BL_CAST(BL_PC, &src);

	if (sd != nullptr && sd->status.weapon == W_KNUCKLE)
		dmg.div_ = -6;
#endif
}
```

#### `SkillRagingQuadrupleBlow::castendDamageId`

来源：`src/map/skills/acolyte/ragingquadrupleblow.cpp:22-25`

```cpp
void SkillRagingQuadrupleBlow::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, flag);
	status_change_end(src, SC_BLADESTOP);
}
```

#### `SkillRagingQuadrupleBlow::calculateSkillRatio`

来源：`src/map/skills/acolyte/ragingquadrupleblow.cpp:27-37`

```cpp
void SkillRagingQuadrupleBlow::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const map_session_data* sd = BL_CAST(BL_PC, src);

	base_skillratio += 150 + 50 * skill_lv;
	if (sd && sd->status.weapon == W_KNUCKLE)
		base_skillratio *= 2;
#else
	base_skillratio += 50 + 50 * skill_lv;
#endif
}
```

### Raging Thrust (`MO_COMBOFINISH`)

武器/物理技能；目标：自身；最高等级 5；射程：-2；命中类型：Single；段数：1；属性：Weapon；范围：2；伤害标记：Splash；消耗/限制：SP Lv1=11; Lv2=12; Lv3=13; Lv4=14; Lv5=15；气弹 1；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRagingThrust`
- 实现文件：`src/map/skills/acolyte/ragingthrust.cpp`

#### `SkillRagingThrust::SkillRagingThrust`

来源：`src/map/skills/acolyte/ragingthrust.cpp:10-11`

```cpp
SkillRagingThrust::SkillRagingThrust() : WeaponSkillImpl(MO_COMBOFINISH) {
}
```

#### `SkillRagingThrust::castendDamageId`

来源：`src/map/skills/acolyte/ragingthrust.cpp:13-24`

```cpp
void SkillRagingThrust::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_change* sc = status_get_sc(src);

	if (!(flag&1) && sc && sc->getSCE(SC_SPIRIT) && sc->getSCE(SC_SPIRIT)->val2 == SL_MONK)
	{	//Becomes a splash attack when Soul Linked.
		map_foreachinshootrange(skill_area_sub, target,
			skill_get_splash(getSkillId(), skill_lv),BL_CHAR|BL_SKILL,
			src,getSkillId(),skill_lv,tick, flag|BCT_ENEMY|1,
			skill_castend_damage_id);
	} else
		WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, flag);
}
```

#### `SkillRagingThrust::calculateSkillRatio`

来源：`src/map/skills/acolyte/ragingthrust.cpp:26-37`

```cpp
void SkillRagingThrust::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const status_data* sstatus = status_get_status_data(*src);

	base_skillratio += 450 + 50 * skill_lv + sstatus->str; // !TODO: How does STR play a role?
#else
	base_skillratio += 140 + 60 * skill_lv;
#endif

	if (const status_change* sc = status_get_sc(src); sc != nullptr && sc->getSCE(SC_GT_ENERGYGAIN))
		base_skillratio += base_skillratio * 50 / 100;
}
```

### Ki Translation (`MO_KITRANSLATION`)

武器/物理技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；吟唱：2000 ms；技能后摇：1000 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 40；气弹 1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillKiTranslation`
- 实现文件：`src/map/skills/acolyte/kitranslation.cpp`

#### `SkillKiTranslation::SkillKiTranslation`

来源：`src/map/skills/acolyte/kitranslation.cpp:9-10`

```cpp
SkillKiTranslation::SkillKiTranslation() : SkillImpl(MO_KITRANSLATION) {
}
```

#### `SkillKiTranslation::castendNoDamageId`

来源：`src/map/skills/acolyte/kitranslation.cpp:12-28`

```cpp
void SkillKiTranslation::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if(dstsd && ((dstsd->class_&MAPID_FIRSTMASK) != MAPID_GUNSLINGER && (dstsd->class_&MAPID_SECONDMASK) != MAPID_REBELLION) && dstsd->spiritball < 5) {
		//Require will define how many spiritballs will be transferred
		struct s_skill_condition require;
		require = skill_get_requirement(sd,getSkillId(),skill_lv);
		pc_delspiritball(sd,require.spiritball,0);
		for (int32 i = 0; i < require.spiritball; i++)
			pc_addspiritball(dstsd,skill_get_time(getSkillId(),skill_lv),5);
	} else {
		if(sd)
			clif_skill_fail( *sd, getSkillId() );
		flag |= SKILL_NOCONSUME_REQ;
	}
}
```

### Ki Explosion (`MO_BALKYOUNG`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-1；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：5；技能后摇：2000 ms；持续时间2：5000 ms；伤害标记：Splash, IgnoreAtkCard；消耗/限制：HP 10；SP 20；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillKiExplosion`
- 实现文件：`src/map/skills/acolyte/kiexplosion.cpp`

#### `SkillKiExplosion::SkillKiExplosion`

来源：`src/map/skills/acolyte/kiexplosion.cpp:10-11`

```cpp
SkillKiExplosion::SkillKiExplosion() : SkillImpl(MO_BALKYOUNG) {
}
```

#### `SkillKiExplosion::modifyDamageData`

来源：`src/map/skills/acolyte/kiexplosion.cpp:13-15`

```cpp
void SkillKiExplosion::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	dmg.blewcount = 0;
}
```

#### `SkillKiExplosion::castendNoDamageId`

来源：`src/map/skills/acolyte/kiexplosion.cpp:17-23`

```cpp
void SkillKiExplosion::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Passive part of the attack. Splash knock-back+stun. [Skotlex]
	if (skill_area_temp[1] != target->id) {
		skill_blown(src,target,skill_get_blewcount(getSkillId(),skill_lv),-1,BLOWN_NONE);
		skill_additional_effect(src,target,getSkillId(),skill_lv,BF_MISC,ATK_DEF,tick); //Use Misc rather than weapon to signal passive pushback
	}
}
```

#### `SkillKiExplosion::castendDamageId`

来源：`src/map/skills/acolyte/kiexplosion.cpp:25-33`

```cpp
void SkillKiExplosion::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	// Active part of the attack. Skill-attack [Skotlex]
	skill_area_temp[1] = target->id; //NOTE: This is used in skill_castend_nodamage_id to avoid affecting the target.
	if (skill_attack(BF_WEAPON,src,src,target,getSkillId(),skill_lv,tick,flag))
		map_foreachinallrange(skill_area_sub,target,
			skill_get_splash(getSkillId(), skill_lv),BL_CHAR,
			src,getSkillId(),skill_lv,tick,flag|BCT_ENEMY|1,
			skill_castend_nodamage_id);
}
```

#### `SkillKiExplosion::calculateSkillRatio`

来源：`src/map/skills/acolyte/kiexplosion.cpp:35-41`

```cpp
void SkillKiExplosion::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 700;
#else
	base_skillratio += 200;
#endif
}
```

#### `SkillKiExplosion::applyAdditionalEffects`

来源：`src/map/skills/acolyte/kiexplosion.cpp:43-47`

```cpp
void SkillKiExplosion::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	//Note: attack_type is passed as BF_WEAPON for the actual target, BF_MISC for the splash-affected mobs.
	if(attack_type&BF_MISC) //70% base stun chance...
		sc_start(src,target,SC_STUN,70,skill_lv,skill_get_time2(getSkillId(),skill_lv));
}
```
