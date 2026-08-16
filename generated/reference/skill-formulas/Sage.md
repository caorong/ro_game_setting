# Sage 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 93 | `WZ_ESTIMATION` / Sense | `exact-class-methods` | `SkillSense` | src/map/skills/mage/sense.cpp |
| 90 | `WZ_EARTHSPIKE` / Earth Spike | `exact-class-methods` | `SkillEarthSpike` | src/map/skills/mage/earthspike.cpp |
| 91 | `WZ_HEAVENDRIVE` / Heaven's Drive | `exact-class-methods` | `SkillHeavensDrive` | src/map/skills/mage/heavensdrive.cpp |
| 274 | `SA_ADVANCEDBOOK` / Study | `core-source-references` | `` | src/map/battle.cpp, src/map/status.cpp |
| 275 | `SA_CASTCANCEL` / Cast Cancel | `exact-class-methods` | `SkillCastCancel` | src/map/skills/mage/castcancel.cpp |
| 276 | `SA_MAGICROD` / Magic Rod | `exact-class-methods` | `SkillMagicRod` | src/map/skills/mage/magicrod.cpp |
| 277 | `SA_SPELLBREAKER` / Spell Breaker | `exact-class-methods` | `SkillSpellBreaker` | src/map/skills/mage/spellbreaker.cpp |
| 278 | `SA_FREECAST` / Free Cast | `core-source-references` | `` | src/map/skill.cpp, src/map/status.cpp |
| 279 | `SA_AUTOSPELL` / Hindsight | `exact-class-methods` | `SkillHindsight` | src/map/skills/mage/hindsight.cpp |
| 280 | `SA_FLAMELAUNCHER` / Endow Blaze | `exact-class-methods` | `SkillEndowBlaze` | src/map/skills/mage/endowblaze.cpp |
| 281 | `SA_FROSTWEAPON` / Endow Tsunami | `exact-class-methods` | `SkillEndowTsunami` | src/map/skills/mage/endowtsunami.cpp |
| 282 | `SA_LIGHTNINGLOADER` / Endow Tornado | `exact-class-methods` | `SkillEndowTornado` | src/map/skills/mage/endowtornado.cpp |
| 283 | `SA_SEISMICWEAPON` / Endow Quake | `exact-class-methods` | `SkillEndowQuake` | src/map/skills/mage/endowquake.cpp |
| 284 | `SA_DRAGONOLOGY` / Dragonology | `core-source-references` | `` | src/map/status.cpp |
| 285 | `SA_VOLCANO` / Volcano | `exact-class-methods` | `SkillVolcano` | src/map/skills/mage/volcano.cpp |
| 286 | `SA_DELUGE` / Deluge | `exact-class-methods` | `SkillDeluge` | src/map/skills/mage/deluge.cpp |
| 287 | `SA_VIOLENTGALE` / Whirlwind | `exact-class-methods` | `SkillWhirlwind` | src/map/skills/mage/whirlwind.cpp |
| 288 | `SA_LANDPROTECTOR` / Magnetic Earth | `exact-class-methods` | `SkillMagneticEarth` | src/map/skills/mage/magneticearth.cpp |
| 289 | `SA_DISPELL` / Dispell | `exact-class-methods` | `SkillDispell` | src/map/skills/mage/dispell.cpp |
| 290 | `SA_ABRACADABRA` / Hocus-pocus | `exact-class-methods` | `SkillHocusPocus` | src/map/skills/mage/hocuspocus.cpp |
| 1007 | `SA_CREATECON` / Create Elemental Converter | `exact-class-methods` | `SkillCreateElementalConverter` | src/map/skills/mage/createelementalconverter.cpp |
| 1008 | `SA_ELEMENTWATER` / Elemental Change Water | `exact-class-methods` | `SkillElementalChangeWater` | src/map/skills/mage/elementalchangewater.cpp |
| 1017 | `SA_ELEMENTGROUND` / Elemental Change Earth | `exact-class-methods` | `SkillElementalChangeEarth` | src/map/skills/mage/elementalchangeearth.cpp |
| 1018 | `SA_ELEMENTFIRE` / Elemental Change Fire | `exact-class-methods` | `SkillElementalChangeFire` | src/map/skills/mage/elementalchangefire.cpp |
| 1019 | `SA_ELEMENTWIND` / Elemental Change Wind | `exact-class-methods` | `SkillElementalChangeWind` | src/map/skills/mage/elementalchangewind.cpp |

## 详细公式与效果实现

### Sense (`WZ_ESTIMATION`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 10。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSense`
- 实现文件：`src/map/skills/mage/sense.cpp`

#### `SkillSense::SkillSense`

来源：`src/map/skills/mage/sense.cpp:10-11`

```cpp
SkillSense::SkillSense() : SkillImpl(WZ_ESTIMATION) {
}
```

#### `SkillSense::castendNoDamageId`

来源：`src/map/skills/mage/sense.cpp:13-30`

```cpp
void SkillSense::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);
	mob_data* dstmd = BL_CAST(BL_MOB, target);

	if( sd == nullptr )
		return;
	if( dstsd )
	{ // Fail on Players
		clif_skill_fail( *sd, getSkillId() );
		return;
	}

	if (dstmd != nullptr)
		clif_skill_estimation( *sd, *dstmd );

	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
}
```

### Earth Spike (`WZ_EARTHSPIKE`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；属性：Earth；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEarthSpike`
- 实现文件：`src/map/skills/mage/earthspike.cpp`

#### `SkillEarthSpike::SkillEarthSpike`

来源：`src/map/skills/mage/earthspike.cpp:10-11`

```cpp
SkillEarthSpike::SkillEarthSpike() : SkillImpl(WZ_EARTHSPIKE) {
}
```

#### `SkillEarthSpike::castendDamageId`

来源：`src/map/skills/mage/earthspike.cpp:13-15`

```cpp
void SkillEarthSpike::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_attack(BF_MAGIC,src,src,target,getSkillId(),skill_lv,tick,flag);
}
```

#### `SkillEarthSpike::calculateSkillRatio`

来源：`src/map/skills/mage/earthspike.cpp:17-25`

```cpp
void SkillEarthSpike::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const status_change* sc = status_get_sc(src);

	base_skillratio += 100;
	if (sc && sc->getSCE(SC_EARTH_CARE_OPTION))
		base_skillratio += base_skillratio * 800 / 100;
#endif
}
```

### Heaven's Drive (`WZ_HEAVENDRIVE`)

魔法技能；目标：地面区域；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；属性：Earth；吟唱：Lv1=1000; Lv2=2000; Lv3=3000; Lv4=4000; Lv5=5000 ms；技能后摇：1000 ms；持续时间1：100 ms；消耗/限制：SP Lv1=28; Lv2=32; Lv3=36; Lv4=40; Lv5=44。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHeavensDrive`
- 实现文件：`src/map/skills/mage/heavensdrive.cpp`

#### `SkillHeavensDrive::SkillHeavensDrive`

来源：`src/map/skills/mage/heavensdrive.cpp:10-11`

```cpp
SkillHeavensDrive::SkillHeavensDrive() : SkillImpl(WZ_HEAVENDRIVE) {
}
```

#### `SkillHeavensDrive::castendPos2`

来源：`src/map/skills/mage/heavensdrive.cpp:13-18`

```cpp
void SkillHeavensDrive::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag|=1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillHeavensDrive::calculateSkillRatio`

来源：`src/map/skills/mage/heavensdrive.cpp:20-24`

```cpp
void SkillHeavensDrive::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 25;
#endif
}
```

#### `SkillHeavensDrive::applyAdditionalEffects`

来源：`src/map/skills/mage/heavensdrive.cpp:26-28`

```cpp
void SkillHeavensDrive::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	status_change_end(target, SC_SV_ROOTTWIST);
}
```

### Study (`SA_ADVANCEDBOOK`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2379
damage += (skill * 3);
// src/map/battle.cpp:2383
damage += (skill * 3);
// src/map/battle.cpp:2387
damage += (skill * 3);
// src/map/battle.cpp:2391
damage += (skill * 3);
// src/map/battle.cpp:2395
damage += (skill * 3);
// src/map/battle.cpp:2399
return damage;
// src/map/battle.cpp:2402
/** Calculates overrefine damage bonus and weapon related bonuses (unofficial)
// src/map/status.cpp:2381
temp_aspd = status->dex * status->dex / 7.0f + status->agi * status->agi * 0.5f;
// src/map/status.cpp:2384
temp_aspd = status->dex * status->dex / 5.0f + status->agi * status->agi * 0.5f;
// src/map/status.cpp:2387
temp_aspd = (float)(sqrt(temp_aspd) * 0.25f) + 196;
// src/map/status.cpp:2388
if ((skill_lv = pc_checkskill(sd,SA_ADVANCEDBOOK)) > 0 && sd->status.weapon == W_BOOK)
// src/map/status.cpp:2389
val += (skill_lv - 1) / 2 + 1;
// src/map/status.cpp:2390
if ((skill_lv = pc_checkskill(sd, SG_DEVIL)) > 0 && ((sd->class_&MAPID_THIRDMASK) == MAPID_STAR_EMPEROR || pc_is_maxjoblv(sd)))
// src/map/status.cpp:2391
val += 1 + skill_lv;
// src/map/status.cpp:2392
if ((skill_lv = pc_checkskill(sd,GS_SINGLEACTION)) > 0 && (sd->status.weapon >= W_REVOLVER && sd->status.weapon <= W_GRENADE))
// src/map/status.cpp:2393
val += ((skill_lv + 1) / 2);
```

### Cast Cancel (`SA_CASTCANCEL`)

魔法技能；目标：自身；最高等级 5；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 2。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCastCancel`
- 实现文件：`src/map/skills/mage/castcancel.cpp`

#### `SkillCastCancel::SkillCastCancel`

来源：`src/map/skills/mage/castcancel.cpp:11-12`

```cpp
SkillCastCancel::SkillCastCancel() : SkillImpl(SA_CASTCANCEL) {
}
```

#### `SkillCastCancel::castendNoDamageId`

来源：`src/map/skills/mage/castcancel.cpp:14-25`

```cpp
void SkillCastCancel::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
	unit_skillcastcancel(src,1);
	if(sd) {
		int32 sp = skill_get_sp(sd->skill_id_old,sd->skill_lv_old);
		sp = sp * (90 - (skill_lv-1)*20) / 100;
		if(sp < 0) sp = 0;
		status_zap(src, 0, sp);
	}
}
```

### Magic Rod (`SA_MAGICROD`)

魔法技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：Lv1=400; Lv2=600; Lv3=800; Lv4=1000; Lv5=1200 ms；伤害标记：NoDamage；消耗/限制：SP 2；关联状态：MagicRod。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMagicRod`
- 实现文件：`src/map/skills/mage/magicrod.cpp`

#### `SkillMagicRod::SkillMagicRod`

来源：`src/map/skills/mage/magicrod.cpp:11-12`

```cpp
SkillMagicRod::SkillMagicRod() : SkillImpl(SA_MAGICROD) {
}
```

#### `SkillMagicRod::castendNoDamageId`

来源：`src/map/skills/mage/magicrod.cpp:14-21`

```cpp
void SkillMagicRod::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());

#ifdef RENEWAL
	clif_skill_nodamage(src,*src,SA_MAGICROD,skill_lv);
#endif
	sc_start(src,target,type,100,skill_lv,skill_get_time(getSkillId(),skill_lv));
}
```

### Spell Breaker (`SA_SPELLBREAKER`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：700 ms；伤害标记：NoDamage；消耗/限制：SP 10。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpellBreaker`
- 实现文件：`src/map/skills/mage/spellbreaker.cpp`

#### `SkillSpellBreaker::SkillSpellBreaker`

来源：`src/map/skills/mage/spellbreaker.cpp:12-13`

```cpp
SkillSpellBreaker::SkillSpellBreaker() : SkillImpl(SA_SPELLBREAKER) {
}
```

#### `SkillSpellBreaker::castendNoDamageId`

来源：`src/map/skills/mage/spellbreaker.cpp:15-60`

```cpp
void SkillSpellBreaker::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);
	status_change *tsc = status_get_sc(target);
	map_session_data* sd = BL_CAST( BL_PC, src );
	map_session_data* dstsd = BL_CAST( BL_PC, target );

	int32 sp;
	if (dstsd && tsc && tsc->getSCE(SC_MAGICROD)) {
		// If target enemy player has Magic Rod, then 20% of your SP is transferred to that player
		sp = status_percent_damage(target, src, 0, -20, false);
		status_heal(target, 0, sp, 2);
	}
	else {
		struct unit_data* ud = unit_bl2ud(target);
		if (!ud || ud->skilltimer == INVALID_TIMER)
			return; //Nothing to cancel.
		int32 hp = 0;
		if (status_has_mode(tstatus, MD_STATUSIMMUNE)) { //Only 10% success chance against status immune. [Skotlex]
			if (rnd_chance(90, 100))
			{
				if (sd) clif_skill_fail( *sd, getSkillId() );
				return;
			}
		}
#ifdef RENEWAL
		else // HP damage does not work on bosses in renewal
#endif
			if (skill_lv >= 5 && (!dstsd || map_flag_vs(target->m))) //HP damage only on pvp-maps when against players.
				hp = tstatus->max_hp / 50; //Siphon 2% HP at level 5

		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
		unit_skillcastcancel(target, 0);
		sp = skill_get_sp(ud->skill_id, ud->skill_lv);
		status_zap(target, 0, sp);
		// Recover some of the SP used
		status_heal(src, 0, sp * (25 * (skill_lv - 1)) / 100, 2);

		// If damage would be lethal, it does not deal damage
		if (hp && hp < tstatus->hp) {
			clif_damage(*src, *target, tick, 0, 0, hp, 0, DMG_NORMAL, 0, false);
			status_zap(target, hp, 0);
			// Recover 50% of damage dealt
			status_heal(src, hp / 2, 0, 2);
		}
	}
}
```

### Free Cast (`SA_FREECAST`)

魔法技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:4885
if(ud->skill_id != SA_CASTCANCEL && ud->skill_id != SO_SPELLFIST) {// otherwise handled in unit_skillcastcancel()
// src/map/skill.cpp:4887
ShowError("skill_castend_id: Timer mismatch %d!=%d!\n", ud->skilltimer, tid);
// src/map/skill.cpp:4892
if( sd && ud->skilltimer != INVALID_TIMER && (pc_checkskill(sd,SA_FREECAST) > 0 || ud->skill_id == LG_EXEEDBREAK) )
// src/map/skill.cpp:4895
status_calc_bl(sd, { SCB_SPEED, SCB_ASPD });
// src/map/skill.cpp:5268
ShowError("skill_castend_pos: Timer mismatch %d!=%d\n", ud->skilltimer, tid);
// src/map/skill.cpp:5273
if( sd && ud->skilltimer != INVALID_TIMER && ( pc_checkskill(sd,SA_FREECAST) > 0 || ud->skill_id == LG_EXEEDBREAK ) )
// src/map/skill.cpp:5276
status_calc_bl(sd, { SCB_SPEED, SCB_ASPD });
// src/map/skill.cpp:5285
unit_set_attackdelay(*src, tick, DELAY_EVENT_CASTEND);
// src/map/status.cpp:6386
status->amotion = cap_value(amotion, MAX_ASPD_NOPC/AMOTION_DIVIDER_NOPC, MIN_ASPD/AMOTION_DIVIDER_NOPC);
// src/map/status.cpp:6388
status->adelay = AMOTION_DIVIDER_NOPC * status->amotion;
// src/map/status.cpp:6390
uint16 skill_lv;
// src/map/status.cpp:6393
#ifndef RENEWAL_ASPD
// src/map/status.cpp:6394
status->aspd_rate = status_calc_aspd_rate(&bl, sc, b_status->aspd_rate);
// src/map/status.cpp:6397
amotion = amotion * status->aspd_rate / 1000;
// src/map/status.cpp:6398
if (sd->ud.skilltimer != INVALID_TIMER && (skill_lv = pc_checkskill(sd, SA_FREECAST)) > 0)
// src/map/status.cpp:6399
#ifdef RENEWAL_ASPD
```

### Hindsight (`SA_AUTOSPELL`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；吟唱：3000 ms；持续时间1：Lv1=120000; Lv2=150000; Lv3=180000; Lv4=210000; Lv5=240000; Lv6=270000; Lv7=300000; Lv8=330000; Lv9=360000; Lv10=390000 ms；伤害标记：NoDamage；消耗/限制：SP 35；关联状态：AutoSpell。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHindsight`
- 实现文件：`src/map/skills/mage/hindsight.cpp`

#### `SkillHindsight::SkillHindsight`

来源：`src/map/skills/mage/hindsight.cpp:10-11`

```cpp
SkillHindsight::SkillHindsight() : SkillImpl(SA_AUTOSPELL) {
}
```

#### `SkillHindsight::castendNoDamageId`

来源：`src/map/skills/mage/hindsight.cpp:13-54`

```cpp
void SkillHindsight::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	// status_change *tsc = status_get_sc(target);
	map_session_data* sd = BL_CAST( BL_PC, src );

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
	if (sd) {
		sd->state.workinprogress = WIP_DISABLE_ALL;
		clif_autospell( *sd, skill_lv );
	} else {
		int32 maxlv=1,spellid=0;
		static const int32 spellarray[3] = { MG_COLDBOLT,MG_FIREBOLT,MG_LIGHTNINGBOLT };

		if(skill_lv >= 10) {
			spellid = MG_FROSTDIVER;
//			if (tsc && tsc->getSCE(SC_SPIRIT) && tsc->getSCE(SC_SPIRIT)->val2 == SA_SAGE)
//				maxlv = 10;
//			else
				maxlv = skill_lv - 9;
		}
		else if(skill_lv >=8) {
			spellid = MG_FIREBALL;
			maxlv = skill_lv - 7;
		}
		else if(skill_lv >=5) {
			spellid = MG_SOULSTRIKE;
			maxlv = skill_lv - 4;
		}
		else if(skill_lv >=2) {
			int32 i_rnd = rnd()%3;
			spellid = spellarray[i_rnd];
			maxlv = skill_lv - 1;
		}
		else if(skill_lv > 0) {
			spellid = MG_NAPALMBEAT;
			maxlv = 3;
		}

		if(spellid > 0)
			sc_start4(src,src,SC_AUTOSPELL,100,skill_lv,spellid,maxlv,0,
				skill_get_time(SA_AUTOSPELL,skill_lv));
	}
}
```

### Endow Blaze (`SA_FLAMELAUNCHER`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Fire；吟唱：3000 ms；持续时间1：Lv1-4=1200000; Lv5=1800000 ms；伤害标记：NoDamage；消耗/限制：SP 40；道具 Boody_Red×1；关联状态：FireWeapon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEndowBlaze`
- 实现文件：`src/map/skills/mage/endowblaze.cpp`

#### `SkillEndowBlaze::SkillEndowBlaze`

来源：`src/map/skills/mage/endowblaze.cpp:12-13`

```cpp
SkillEndowBlaze::SkillEndowBlaze() : SkillImpl(SA_FLAMELAUNCHER) {
}
```

#### `SkillEndowBlaze::castendNoDamageId`

来源：`src/map/skills/mage/endowblaze.cpp:15-40`

```cpp
void SkillEndowBlaze::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );
	map_session_data* dstsd = BL_CAST( BL_PC, target );

	if (dstsd && dstsd->status.weapon == W_FIST) {
		if (sd)
			clif_skill_fail( *sd, getSkillId() );
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv,false);
		return;
	}
#ifdef RENEWAL
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv, sc_start(src, target, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
#else
	// 100% success rate at lv4 & 5, but lasts longer at lv5
	if(!clif_skill_nodamage(src,*target,getSkillId(),skill_lv, sc_start(src,target,type,(60+skill_lv*10),skill_lv, skill_get_time(getSkillId(),skill_lv)))) {
		if (dstsd){
			int16 index = dstsd->equip_index[EQI_HAND_R];
			if (index != -1 && dstsd->inventory_data[index] && dstsd->inventory_data[index]->type == IT_WEAPON)
				pc_unequipitem(dstsd, index, 3); //Must unequip the weapon instead of breaking it [Daegaladh]
		}
		if (sd)
			clif_skill_fail( *sd, getSkillId() );
	}
#endif
}
```

### Endow Tsunami (`SA_FROSTWEAPON`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Water；吟唱：3000 ms；持续时间1：Lv1-4=1200000; Lv5=1800000 ms；伤害标记：NoDamage；消耗/限制：SP 40；道具 Crystal_Blue×1；关联状态：WaterWeapon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEndowTsunami`
- 实现文件：`src/map/skills/mage/endowtsunami.cpp`

#### `SkillEndowTsunami::SkillEndowTsunami`

来源：`src/map/skills/mage/endowtsunami.cpp:12-13`

```cpp
SkillEndowTsunami::SkillEndowTsunami() : SkillImpl(SA_FROSTWEAPON) {
}
```

#### `SkillEndowTsunami::castendNoDamageId`

来源：`src/map/skills/mage/endowtsunami.cpp:15-40`

```cpp
void SkillEndowTsunami::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );
	map_session_data* dstsd = BL_CAST( BL_PC, target );

	if (dstsd && dstsd->status.weapon == W_FIST) {
		if (sd)
			clif_skill_fail( *sd, getSkillId() );
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv,false);
		return;
	}
#ifdef RENEWAL
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv, sc_start(src, target, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
#else
	// 100% success rate at lv4 & 5, but lasts longer at lv5
	if(!clif_skill_nodamage(src,*target,getSkillId(),skill_lv, sc_start(src,target,type,(60+skill_lv*10),skill_lv, skill_get_time(getSkillId(),skill_lv)))) {
		if (dstsd){
			int16 index = dstsd->equip_index[EQI_HAND_R];
			if (index != -1 && dstsd->inventory_data[index] && dstsd->inventory_data[index]->type == IT_WEAPON)
				pc_unequipitem(dstsd, index, 3); //Must unequip the weapon instead of breaking it [Daegaladh]
		}
		if (sd)
			clif_skill_fail( *sd, getSkillId() );
	}
#endif
}
```

### Endow Tornado (`SA_LIGHTNINGLOADER`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Wind；吟唱：3000 ms；持续时间1：Lv1-4=1200000; Lv5=1800000 ms；伤害标记：NoDamage；消耗/限制：SP 40；道具 Wind_Of_Verdure×1；关联状态：WindWeapon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEndowTornado`
- 实现文件：`src/map/skills/mage/endowtornado.cpp`

#### `SkillEndowTornado::SkillEndowTornado`

来源：`src/map/skills/mage/endowtornado.cpp:12-13`

```cpp
SkillEndowTornado::SkillEndowTornado() : SkillImpl(SA_LIGHTNINGLOADER) {
}
```

#### `SkillEndowTornado::castendNoDamageId`

来源：`src/map/skills/mage/endowtornado.cpp:15-40`

```cpp
void SkillEndowTornado::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );
	map_session_data* dstsd = BL_CAST( BL_PC, target );

	if (dstsd && dstsd->status.weapon == W_FIST) {
		if (sd)
			clif_skill_fail( *sd, getSkillId() );
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv,false);
		return;
	}
#ifdef RENEWAL
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv, sc_start(src, target, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
#else
	// 100% success rate at lv4 & 5, but lasts longer at lv5
	if(!clif_skill_nodamage(src,*target,getSkillId(),skill_lv, sc_start(src,target,type,(60+skill_lv*10),skill_lv, skill_get_time(getSkillId(),skill_lv)))) {
		if (dstsd){
			int16 index = dstsd->equip_index[EQI_HAND_R];
			if (index != -1 && dstsd->inventory_data[index] && dstsd->inventory_data[index]->type == IT_WEAPON)
				pc_unequipitem(dstsd, index, 3); //Must unequip the weapon instead of breaking it [Daegaladh]
		}
		if (sd)
			clif_skill_fail( *sd, getSkillId() );
	}
#endif
}
```

### Endow Quake (`SA_SEISMICWEAPON`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Earth；吟唱：3000 ms；持续时间1：Lv1-4=1200000; Lv5=1800000 ms；伤害标记：NoDamage；消耗/限制：SP 40；道具 Yellow_Live×1；关联状态：EarthWeapon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEndowQuake`
- 实现文件：`src/map/skills/mage/endowquake.cpp`

#### `SkillEndowQuake::SkillEndowQuake`

来源：`src/map/skills/mage/endowquake.cpp:12-13`

```cpp
SkillEndowQuake::SkillEndowQuake() : SkillImpl(SA_SEISMICWEAPON) {
}
```

#### `SkillEndowQuake::castendNoDamageId`

来源：`src/map/skills/mage/endowquake.cpp:15-40`

```cpp
void SkillEndowQuake::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );
	map_session_data* dstsd = BL_CAST( BL_PC, target );

	if (dstsd && dstsd->status.weapon == W_FIST) {
		if (sd)
			clif_skill_fail( *sd, getSkillId() );
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv,false);
		return;
	}
#ifdef RENEWAL
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv, sc_start(src, target, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
#else
	// 100% success rate at lv4 & 5, but lasts longer at lv5
	if(!clif_skill_nodamage(src,*target,getSkillId(),skill_lv, sc_start(src,target,type,(60+skill_lv*10),skill_lv, skill_get_time(getSkillId(),skill_lv)))) {
		if (dstsd){
			int16 index = dstsd->equip_index[EQI_HAND_R];
			if (index != -1 && dstsd->inventory_data[index] && dstsd->inventory_data[index]->type == IT_WEAPON)
				pc_unequipitem(dstsd, index, 3); //Must unequip the weapon instead of breaking it [Daegaladh]
		}
		if (sd)
			clif_skill_fail( *sd, getSkillId() );
	}
#endif
}
```

### Dragonology (`SA_DRAGONOLOGY`)

武器/物理技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:4670
if(sd->hprecov_rate < 0)
// src/map/status.cpp:4671
sd->hprecov_rate = 0;
// src/map/status.cpp:4672
if(sd->sprecov_rate < 0)
// src/map/status.cpp:4673
sd->sprecov_rate = 0;
// src/map/status.cpp:4683
uint8 dragon_matk = skill * 2;
// src/map/status.cpp:4691
sd->indexed_bonus.magic_addrace[RC_DRAGON]+=dragon_matk;
```

### Volcano (`SA_VOLCANO`)

魔法技能；目标：地面区域；最高等级 5；射程：2；命中类型：Single；段数：1；属性：Fire；吟唱：5000 ms；持续时间1：Lv1=60000; Lv2=120000; Lv3=180000; Lv4=240000; Lv5=300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=48; Lv2=46; Lv3=44; Lv4=42; Lv5=40；道具 Yellow_Gemstone×1；关联状态：Volcano。

- 覆盖：`exact-class-methods`
- 实现类：`SkillVolcano`
- 实现文件：`src/map/skills/mage/volcano.cpp`

#### `SkillVolcano::SkillVolcano`

来源：`src/map/skills/mage/volcano.cpp:6-7`

```cpp
SkillVolcano::SkillVolcano() : SkillImpl(SA_VOLCANO) {
}
```

#### `SkillVolcano::castendPos2`

来源：`src/map/skills/mage/volcano.cpp:9-24`

```cpp
void SkillVolcano::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Does not consumes if the skill is already active. [Skotlex]
	std::shared_ptr<s_skill_unit_group> sg2;
	if ((sg2= skill_locate_element_field(src)) != nullptr && ( sg2->skill_id == SA_VOLCANO || sg2->skill_id == SA_DELUGE || sg2->skill_id == SA_VIOLENTGALE ))
	{
		if (sg2->limit - DIFF_TICK(gettick(), sg2->tick) > 0)
		{
			skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
			flag |= SKILL_NOCONSUME_REQ; // not to consume items
			return;
		}
		else
			sg2->limit = 0; //Disable it.
	}
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Deluge (`SA_DELUGE`)

魔法技能；目标：地面区域；最高等级 5；射程：2；命中类型：Single；段数：1；属性：Water；吟唱：5000 ms；持续时间1：Lv1=60000; Lv2=120000; Lv3=180000; Lv4=240000; Lv5=300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=48; Lv2=46; Lv3=44; Lv4=42; Lv5=40；道具 Yellow_Gemstone×1；关联状态：Deluge。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDeluge`
- 实现文件：`src/map/skills/mage/deluge.cpp`

#### `SkillDeluge::SkillDeluge`

来源：`src/map/skills/mage/deluge.cpp:6-7`

```cpp
SkillDeluge::SkillDeluge() : SkillImpl(SA_DELUGE) {
}
```

#### `SkillDeluge::castendPos2`

来源：`src/map/skills/mage/deluge.cpp:9-24`

```cpp
void SkillDeluge::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Does not consumes if the skill is already active. [Skotlex]
	std::shared_ptr<s_skill_unit_group> sg2;
	if ((sg2= skill_locate_element_field(src)) != nullptr && ( sg2->skill_id == SA_VOLCANO || sg2->skill_id == SA_DELUGE || sg2->skill_id == SA_VIOLENTGALE ))
	{
		if (sg2->limit - DIFF_TICK(gettick(), sg2->tick) > 0)
		{
			skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
			flag |= SKILL_NOCONSUME_REQ; // not to consume items
			return;
		}
		else
			sg2->limit = 0; //Disable it.
	}
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Whirlwind (`SA_VIOLENTGALE`)

魔法技能；目标：地面区域；最高等级 5；射程：2；命中类型：Single；段数：1；属性：Wind；吟唱：5000 ms；持续时间1：Lv1=60000; Lv2=120000; Lv3=180000; Lv4=240000; Lv5=300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=48; Lv2=46; Lv3=44; Lv4=42; Lv5=40；道具 Yellow_Gemstone×1；关联状态：ViolentGale。

- 覆盖：`exact-class-methods`
- 实现类：`SkillWhirlwind`
- 实现文件：`src/map/skills/mage/whirlwind.cpp`

#### `SkillWhirlwind::SkillWhirlwind`

来源：`src/map/skills/mage/whirlwind.cpp:6-7`

```cpp
SkillWhirlwind::SkillWhirlwind() : SkillImpl(SA_VIOLENTGALE) {
}
```

#### `SkillWhirlwind::castendPos2`

来源：`src/map/skills/mage/whirlwind.cpp:9-24`

```cpp
void SkillWhirlwind::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Does not consumes if the skill is already active. [Skotlex]
	std::shared_ptr<s_skill_unit_group> sg2;
	if ((sg2= skill_locate_element_field(src)) != nullptr && ( sg2->skill_id == SA_VOLCANO || sg2->skill_id == SA_DELUGE || sg2->skill_id == SA_VIOLENTGALE ))
	{
		if (sg2->limit - DIFF_TICK(gettick(), sg2->tick) > 0)
		{
			skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
			flag |= SKILL_NOCONSUME_REQ; // not to consume items
			return;
		}
		else
			sg2->limit = 0; //Disable it.
	}
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Magnetic Earth (`SA_LANDPROTECTOR`)

魔法技能；目标：地面区域；最高等级 5；射程：2；命中类型：Single；段数：1；吟唱：5000 ms；持续时间1：Lv1=165000; Lv2=210000; Lv3=255000; Lv4=300000; Lv5=345000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=66; Lv2=62; Lv3=58; Lv4=54; Lv5=50；道具 Blue_Gemstone×1, Yellow_Gemstone×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMagneticEarth`
- 实现文件：`src/map/skills/mage/magneticearth.cpp`

#### `SkillMagneticEarth::SkillMagneticEarth`

来源：`src/map/skills/mage/magneticearth.cpp:6-7`

```cpp
SkillMagneticEarth::SkillMagneticEarth() : SkillImpl(SA_LANDPROTECTOR) {
}
```

#### `SkillMagneticEarth::castendPos2`

来源：`src/map/skills/mage/magneticearth.cpp:9-12`

```cpp
void SkillMagneticEarth::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Dispell (`SA_DISPELL`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：2000 ms；伤害标记：NoDamage；消耗/限制：SP 1；道具 Yellow_Gemstone×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDispell`
- 实现文件：`src/map/skills/mage/dispell.cpp`

#### `SkillDispell::SkillDispell`

来源：`src/map/skills/mage/dispell.cpp:11-12`

```cpp
SkillDispell::SkillDispell() : SkillImpl(SA_DISPELL) {
}
```

#### `SkillDispell::castendNoDamageId`

来源：`src/map/skills/mage/dispell.cpp:14-79`

```cpp
void SkillDispell::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	mob_data* dstmd = BL_CAST(BL_MOB, target);
	status_change *tsc = status_get_sc(target);
	map_session_data* sd = BL_CAST( BL_PC, src );
	map_session_data* dstsd = BL_CAST( BL_PC, target );
	int32 i = 0;

	if (flag&1 || (i = skill_get_splash(getSkillId(), skill_lv)) < 1) {
		if (sd && dstsd && !map_flag_vs(sd->m) && (!sd->duel_group || sd->duel_group != dstsd->duel_group) && (!sd->status.party_id || sd->status.party_id != dstsd->status.party_id))
			return; // Outside PvP it should only affect party members and no skill fail message
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
		if((dstsd && (dstsd->class_&MAPID_SECONDMASK) == MAPID_SOUL_LINKER)
			|| (tsc && tsc->getSCE(SC_SPIRIT) && tsc->getSCE(SC_SPIRIT)->val2 == SL_ROGUE) //Rogue's spirit defends against dispel.
			|| rnd()%100 >= 50+10*skill_lv)
		{
			if (sd)
				clif_skill_fail( *sd, getSkillId() );
			return;
		}
		if(status_isimmune(target))
			return;

		//Remove bonus_script by Dispell
		if (dstsd)
			pc_bonus_script_clear(dstsd,BSF_REM_ON_DISPELL);
		// Monsters will unlock their target instead
		else if (dstmd)
			mob_unlocktarget(dstmd, tick);

		if(tsc == nullptr || tsc->empty())
			return;

		//Statuses that can't be Dispelled
		for (const auto &it : status_db) {
			sc_type status = static_cast<sc_type>(it.first);

			if (!tsc->getSCE(status))
				continue;

			if (it.second->flag[SCF_NODISPELL])
				continue;
			switch (status) {
				// bugreport:4888 these songs may only be dispelled if you're not in their song area anymore
				case SC_WHISTLE:		case SC_ASSNCROS:		case SC_POEMBRAGI:
				case SC_APPLEIDUN:		case SC_HUMMING:		case SC_DONTFORGETME:
				case SC_FORTUNE:		case SC_SERVICE4U:
					if (!battle_config.dispel_song || tsc->getSCE(status)->val4 == 0)
						continue; //If in song area don't end it, even if config enatargeted
					break;
				case SC_ASSUMPTIO:
					if( target->type == BL_MOB )
						continue;
					break;
			}
			if (status == SC_BERSERK || status == SC_SATURDAYNIGHTFEVER)
				tsc->getSCE(status)->val2 = 0; //Mark a dispelled berserk to avoid setting hp to 100 by setting hp penalty to 0.
			status_change_end(target, status);
		}
		return;
	}

	//Affect all targets on splash area.
	map_foreachinallrange(skill_area_sub, target, i, BL_CHAR,
		src, getSkillId(), skill_lv, tick, flag|1,
		skill_castend_damage_id);
}
```

### Hocus-pocus (`SA_ABRACADABRA`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 50；道具 Yellow_Gemstone×2。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHocusPocus`
- 实现文件：`src/map/skills/mage/hocuspocus.cpp`

#### `SkillHocusPocus::SkillHocusPocus`

来源：`src/map/skills/mage/hocuspocus.cpp:12-13`

```cpp
SkillHocusPocus::SkillHocusPocus() : SkillImpl(SA_ABRACADABRA) {
}
```

#### `SkillHocusPocus::castendNoDamageId`

来源：`src/map/skills/mage/hocuspocus.cpp:15-76`

```cpp
void SkillHocusPocus::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	if (abra_db.empty()) {
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
		return;
	}
	else {
		int32 abra_skill_id = 0, abra_skill_lv;
		size_t checked = 0, checked_max = abra_db.size() * 3;

		do {
			auto abra_spell = abra_db.random();

			abra_skill_id = abra_spell->skill_id;
			abra_skill_lv = min(skill_lv, skill_get_max(abra_skill_id));

			if( rnd() % 10000 < abra_spell->per[max(skill_lv - 1, 0)] ){
				break;
			}
		} while (checked++ < checked_max);

		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		if( sd )
		{// player-casted
			sd->state.abra_flag = 1;
			sd->skillitem = abra_skill_id;
			sd->skillitemlv = abra_skill_lv;
			sd->skillitem_keep_requirement = false;
			clif_item_skill(sd, abra_skill_id, abra_skill_lv);
		}
		else
		{// mob-casted
			struct unit_data *ud = unit_bl2ud(src);
			int32 inf = skill_get_inf(abra_skill_id);
			if (!ud) return;
			if (inf&INF_SELF_SKILL || inf&INF_SUPPORT_SKILL) {
				if (src->type == BL_PET)
					target = (block_list*)((TBL_PET*)src)->master;
				if (!target) target = src;
				unit_skilluse_id(src, target->id, abra_skill_id, abra_skill_lv);
			} else {	//Assume offensive skills
				int32 target_id = 0;
				if (ud->target)
					target_id = ud->target;
				else switch (src->type) {
					case BL_MOB: target_id = ((TBL_MOB*)src)->target_id; break;
					case BL_PET: target_id = ((TBL_PET*)src)->target_id; break;
				}
				if (!target_id)
					return;
				if (skill_get_casttype(abra_skill_id) == CAST_GROUND) {
					target = map_id2bl(target_id);
					if (!target) target = src;
					unit_skilluse_pos(src, target->x, target->y, abra_skill_id, abra_skill_lv);
				} else
					unit_skilluse_id(src, target_id, abra_skill_id, abra_skill_lv);
			}
		}
	}
}
```

### Create Elemental Converter (`SA_CREATECON`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；伤害标记：NoDamage；消耗/限制：SP 30。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCreateElementalConverter`
- 实现文件：`src/map/skills/mage/createelementalconverter.cpp`

#### `SkillCreateElementalConverter::SkillCreateElementalConverter`

来源：`src/map/skills/mage/createelementalconverter.cpp:9-10`

```cpp
SkillCreateElementalConverter::SkillCreateElementalConverter() : SkillImpl(SA_CREATECON) {
}
```

#### `SkillCreateElementalConverter::castendNoDamageId`

来源：`src/map/skills/mage/createelementalconverter.cpp:12-19`

```cpp
void SkillCreateElementalConverter::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sd != nullptr ){
		clif_elementalconverter_list( *sd );
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
	}
}
```

### Elemental Change Water (`SA_ELEMENTWATER`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Water；吟唱：2000 ms；技能后摇：1000 ms；持续时间1：1800000 ms；伤害标记：NoDamage；消耗/限制：SP 30；道具 Elemental_Water×1；关联状态：ElementalChange。

- 覆盖：`exact-class-methods`
- 实现类：`SkillElementalChangeWater`
- 实现文件：`src/map/skills/mage/elementalchangewater.cpp`

#### `SkillElementalChangeWater::SkillElementalChangeWater`

来源：`src/map/skills/mage/elementalchangewater.cpp:11-12`

```cpp
SkillElementalChangeWater::SkillElementalChangeWater() : SkillImpl(SA_ELEMENTWATER) {
}
```

#### `SkillElementalChangeWater::castendNoDamageId`

来源：`src/map/skills/mage/elementalchangewater.cpp:14-25`

```cpp
void SkillElementalChangeWater::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );
	mob_data* dstmd = BL_CAST( BL_MOB, target );

	if (sd && (!dstmd || status_has_mode(tstatus,MD_STATUSIMMUNE))) // Only works on monsters (Except status immune monsters).
		return;
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start2(src,target, type, 100, skill_lv, skill_get_ele(getSkillId(),skill_lv),
			skill_get_time(getSkillId(), skill_lv)));
}
```

### Elemental Change Earth (`SA_ELEMENTGROUND`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Earth；吟唱：2000 ms；技能后摇：1000 ms；持续时间1：1800000 ms；伤害标记：NoDamage；消耗/限制：SP 30；道具 Elemental_Earth×1；关联状态：ElementalChange。

- 覆盖：`exact-class-methods`
- 实现类：`SkillElementalChangeEarth`
- 实现文件：`src/map/skills/mage/elementalchangeearth.cpp`

#### `SkillElementalChangeEarth::SkillElementalChangeEarth`

来源：`src/map/skills/mage/elementalchangeearth.cpp:11-12`

```cpp
SkillElementalChangeEarth::SkillElementalChangeEarth() : SkillImpl(SA_ELEMENTGROUND) {
}
```

#### `SkillElementalChangeEarth::castendNoDamageId`

来源：`src/map/skills/mage/elementalchangeearth.cpp:14-25`

```cpp
void SkillElementalChangeEarth::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );
	mob_data* dstmd = BL_CAST( BL_MOB, target );

	if (sd && (!dstmd || status_has_mode(tstatus,MD_STATUSIMMUNE))) // Only works on monsters (Except status immune monsters).
		return;
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start2(src,target, type, 100, skill_lv, skill_get_ele(getSkillId(),skill_lv),
			skill_get_time(getSkillId(), skill_lv)));
}
```

### Elemental Change Fire (`SA_ELEMENTFIRE`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Fire；吟唱：2000 ms；技能后摇：1000 ms；持续时间1：1800000 ms；伤害标记：NoDamage；消耗/限制：SP 30；道具 Elemental_Fire×1；关联状态：ElementalChange。

- 覆盖：`exact-class-methods`
- 实现类：`SkillElementalChangeFire`
- 实现文件：`src/map/skills/mage/elementalchangefire.cpp`

#### `SkillElementalChangeFire::SkillElementalChangeFire`

来源：`src/map/skills/mage/elementalchangefire.cpp:11-12`

```cpp
SkillElementalChangeFire::SkillElementalChangeFire() : SkillImpl(SA_ELEMENTFIRE) {
}
```

#### `SkillElementalChangeFire::castendNoDamageId`

来源：`src/map/skills/mage/elementalchangefire.cpp:14-25`

```cpp
void SkillElementalChangeFire::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );
	mob_data* dstmd = BL_CAST( BL_MOB, target );

	if (sd && (!dstmd || status_has_mode(tstatus,MD_STATUSIMMUNE))) // Only works on monsters (Except status immune monsters).
		return;
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start2(src,target, type, 100, skill_lv, skill_get_ele(getSkillId(),skill_lv),
			skill_get_time(getSkillId(), skill_lv)));
}
```

### Elemental Change Wind (`SA_ELEMENTWIND`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Wind；吟唱：2000 ms；技能后摇：1000 ms；持续时间1：1800000 ms；伤害标记：NoDamage；消耗/限制：SP 30；道具 Elemental_Wind×1；关联状态：ElementalChange。

- 覆盖：`exact-class-methods`
- 实现类：`SkillElementalChangeWind`
- 实现文件：`src/map/skills/mage/elementalchangewind.cpp`

#### `SkillElementalChangeWind::SkillElementalChangeWind`

来源：`src/map/skills/mage/elementalchangewind.cpp:11-12`

```cpp
SkillElementalChangeWind::SkillElementalChangeWind() : SkillImpl(SA_ELEMENTWIND) {
}
```

#### `SkillElementalChangeWind::castendNoDamageId`

来源：`src/map/skills/mage/elementalchangewind.cpp:14-25`

```cpp
void SkillElementalChangeWind::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );
	mob_data* dstmd = BL_CAST( BL_MOB, target );

	if (sd && (!dstmd || status_has_mode(tstatus,MD_STATUSIMMUNE))) // Only works on monsters (Except status immune monsters).
		return;
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start2(src,target, type, 100, skill_lv, skill_get_ele(getSkillId(),skill_lv),
			skill_get_time(getSkillId(), skill_lv)));
}
```
