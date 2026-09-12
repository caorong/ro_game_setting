# Gunslinger 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 500 | `GS_GLITTERING` / Flip the Coin | `exact-class-methods` | `SkillGlittering` | src/map/skills/gunslinger/glittering.cpp |
| 501 | `GS_FLING` / Fling | `exact-class-methods` | `SkillFling` | src/map/skills/gunslinger/fling.cpp |
| 502 | `GS_TRIPLEACTION` / Triple Action | `exact-class-methods` | `SkillTripleAction` | src/map/skills/gunslinger/tripleaction.cpp |
| 503 | `GS_BULLSEYE` / Bulls Eye | `exact-class-methods` | `SkillBullseye` | src/map/skills/gunslinger/bullseye.cpp |
| 504 | `GS_MADNESSCANCEL` / Madness Canceller | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 505 | `GS_ADJUSTMENT` / Adjustment | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 506 | `GS_INCREASING` / Increasing Accuracy | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 507 | `GS_MAGICALBULLET` / Magical Bullet | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 508 | `GS_CRACKER` / Cracker | `exact-class-methods` | `SkillCracker` | src/map/skills/gunslinger/cracker.cpp |
| 509 | `GS_SINGLEACTION` / Single Action | `core-source-references` | `` | src/map/status.cpp |
| 510 | `GS_SNAKEEYE` / Snake Eye | `core-source-references` | `` | src/map/skill.cpp, src/map/status.cpp |
| 511 | `GS_CHAINACTION` / Chain Action | `exact-class-methods` | `SkillChainAction` | src/map/skills/gunslinger/chainaction.cpp |
| 512 | `GS_TRACKING` / Tracking | `exact-class-methods` | `SkillTracking` | src/map/skills/gunslinger/tracking.cpp |
| 513 | `GS_DISARM` / Disarm | `exact-class-methods` | `SkillDisarm` | src/map/skills/gunslinger/disarm.cpp |
| 514 | `GS_PIERCINGSHOT` / Piercing Shot | `exact-class-methods` | `SkillPiercingShot` | src/map/skills/gunslinger/piercingshot.cpp |
| 515 | `GS_RAPIDSHOWER` / Rapid Shower | `exact-class-methods` | `SkillRapidShower` | src/map/skills/gunslinger/rapidshower.cpp |
| 516 | `GS_DESPERADO` / Desperado | `exact-class-methods` | `SkillDesperado` | src/map/skills/gunslinger/desperado.cpp |
| 517 | `GS_GATLINGFEVER` / Gatling Fever | `exact-class-methods` | `SkillGatlingfever` | src/map/skills/gunslinger/gatlingfever.cpp |
| 518 | `GS_DUST` / Dust | `exact-class-methods` | `SkillDust` | src/map/skills/gunslinger/dust.cpp |
| 519 | `GS_FULLBUSTER` / Full Buster | `exact-class-methods` | `SkillFullBuster` | src/map/skills/gunslinger/fullbuster.cpp |
| 520 | `GS_SPREADATTACK` / Spread Attack | `exact-class-methods` | `SkillSpreadAttack` | src/map/skills/gunslinger/spreadattack.cpp |
| 521 | `GS_GROUNDDRIFT` / Ground Drift | `exact-class-methods` | `SkillGroundDrift` | src/map/skills/gunslinger/grounddrift.cpp |

## 详细公式与效果实现

### Flip the Coin (`GS_GLITTERING`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：600000 ms；伤害标记：NoDamage, IgnoreFlee；消耗/限制：SP 2；Zeny 1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillGlittering`
- 实现文件：`src/map/skills/gunslinger/glittering.cpp`

#### `SkillGlittering::SkillGlittering`

来源：`src/map/skills/gunslinger/glittering.cpp:9-10`

```cpp
SkillGlittering::SkillGlittering() : SkillImpl(GS_GLITTERING) {
}
```

#### `SkillGlittering::castendNoDamageId`

来源：`src/map/skills/gunslinger/glittering.cpp:12-22`

```cpp
void SkillGlittering::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);

	if (sd) {
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
		if (rnd() % 100 < (20 + 10 * skill_lv))
			pc_addspiritball(sd, skill_get_time(getSkillId(), skill_lv), 10);
		else if (sd->spiritball > 0 && !pc_checkskill(sd, RL_RICHS_COIN))
			pc_delspiritball(sd, 1, 0);
	}
}
```

### Fling (`GS_FLING`)

特殊技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Weapon；持续时间1：30000 ms；伤害标记：IgnoreElement, IgnoreFlee；消耗/限制：SP 10；气弹 5；关联状态：Fling。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFling`
- 实现文件：`src/map/skills/gunslinger/fling.cpp`

#### `SkillFling::SkillFling`

来源：`src/map/skills/gunslinger/fling.cpp:9-10`

```cpp
SkillFling::SkillFling() : SkillImpl(GS_FLING) {
}
```

#### `SkillFling::castendDamageId`

来源：`src/map/skills/gunslinger/fling.cpp:12-14`

```cpp
void SkillFling::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_attack(skill_get_type(getSkillId()), src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

#### `SkillFling::applyAdditionalEffects`

来源：`src/map/skills/gunslinger/fling.cpp:16-20`

```cpp
void SkillFling::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	map_session_data *sd = BL_CAST(BL_PC, src);

	sc_start(src, target, SC_FLING, 100, sd ? sd->spiritball_old : 5, skill_get_time(getSkillId(), skill_lv));
}
```

### Triple Action (`GS_TRIPLEACTION`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Multi_Hit；段数：3；属性：Weapon；消耗/限制：SP 20；弹药数 1；气弹 1；弹药 Arrow, Dagger, Bullet, Shell, Grenade, Shuriken, Kunai, Cannonball, Throwweapon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillTripleAction`
- 实现文件：`src/map/skills/gunslinger/tripleaction.cpp`

#### `SkillTripleAction::SkillTripleAction`

来源：`src/map/skills/gunslinger/tripleaction.cpp:6-7`

```cpp
SkillTripleAction::SkillTripleAction() : WeaponSkillImpl(GS_TRIPLEACTION) {
}
```

#### `SkillTripleAction::calculateSkillRatio`

来源：`src/map/skills/gunslinger/tripleaction.cpp:9-11`

```cpp
void SkillTripleAction::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 50 * skill_lv;
}
```

### Bulls Eye (`GS_BULLSEYE`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Single；段数：1；属性：Weapon；吟唱：500 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP 30；弹药数 1；气弹 1；弹药 Arrow, Dagger, Bullet, Shell, Grenade, Shuriken, Kunai, Cannonball, Throwweapon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBullseye`
- 实现文件：`src/map/skills/gunslinger/bullseye.cpp`

#### `SkillBullseye::SkillBullseye`

来源：`src/map/skills/gunslinger/bullseye.cpp:8-9`

```cpp
SkillBullseye::SkillBullseye() : WeaponSkillImpl(GS_BULLSEYE) {
}
```

#### `SkillBullseye::calculateSkillRatio`

来源：`src/map/skills/gunslinger/bullseye.cpp:11-18`

```cpp
void SkillBullseye::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_data *tstatus = status_get_status_data(*target);

	// Only works well against brute/demihumans non bosses.
	if ((tstatus->race == RC_BRUTE || tstatus->race == RC_DEMIHUMAN || tstatus->race == RC_PLAYER_HUMAN || tstatus->race == RC_PLAYER_DORAM) && !status_has_mode(
		    tstatus, MD_STATUSIMMUNE))
		base_skillratio += 400;
}
```

#### `SkillBullseye::applyAdditionalEffects`

来源：`src/map/skills/gunslinger/bullseye.cpp:20-26`

```cpp
void SkillBullseye::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	status_data *tstatus = status_get_status_data(*target);

	// 0.1% coma rate.
	if (tstatus->race == RC_BRUTE || tstatus->race == RC_DEMIHUMAN || tstatus->race == RC_PLAYER_HUMAN || tstatus->race == RC_PLAYER_DORAM)
		status_change_start(src, target, SC_COMA, 10, skill_lv, 0, src->id, 0, 0, SCSTART_NONE);
}
```

### Madness Canceller (`GS_MADNESSCANCEL`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：3000 ms；技能后摇：4000 ms；持续时间1：15000 ms；伤害标记：NoDamage；消耗/限制：SP 30；气弹 4；关联状态：MadnessCancel。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Adjustment (`GS_ADJUSTMENT`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP 15；气弹 2；关联状态：Adjustment。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Increasing Accuracy (`GS_INCREASING`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；技能后摇：1000 ms；持续时间1：60000 ms；伤害标记：NoDamage；消耗/限制：SP 30；气弹 4；关联状态：Increasing。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Magical Bullet (`GS_MAGICALBULLET`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Single；段数：1；属性：Ghost；消耗/限制：SP 7；气弹 1。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:4503
bonus += static_cast<decltype(bonus)>(pow(skill_lv + sd->inventory.u.items_inventory[index].refine, 2));
// src/map/battle.cpp:4505
atk = max(100, rnd_value(100, bonus));
// src/map/battle.cpp:4511
if (sstatus->matk_max > sstatus->matk_min)
// src/map/battle.cpp:4512
atk = sstatus->matk_min + rnd()%(sstatus->matk_max - sstatus->matk_min);
// src/map/battle.cpp:4514
atk = sstatus->matk_min;
// src/map/battle.cpp:4520
atk = 40 * pc_checkskill(sd, RA_RESEARCHTRAP);
```

### Cracker (`GS_CRACKER`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Single；段数：1；属性：Weapon；技能后摇：1000 ms；持续时间2：5000 ms；伤害标记：NoDamage；消耗/限制：SP 10；弹药数 1；气弹 1；弹药 Arrow, Dagger, Bullet, Shell, Grenade, Shuriken, Kunai, Cannonball, Throwweapon；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCracker`
- 实现文件：`src/map/skills/gunslinger/cracker.cpp`

#### `SkillCracker::SkillCracker`

来源：`src/map/skills/gunslinger/cracker.cpp:9-10`

```cpp
SkillCracker::SkillCracker() : SkillImpl(GS_CRACKER) {
}
```

#### `SkillCracker::castendNoDamageId`

来源：`src/map/skills/gunslinger/cracker.cpp:12-25`

```cpp
void SkillCracker::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	map_session_data *dstsd = BL_CAST(BL_PC, target);
	mob_data *dstmd = BL_CAST(BL_MOB, target);

	/* per official standards, this skill works on players and mobs. */
	if (sd && (dstsd || dstmd)) {
		int32 i = 65 - 5 * distance_bl(src, target); // Base rate
		if (i < 30)
			i = 30;
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
		sc_start(src, target, SC_STUN, i, skill_lv, skill_get_time2(getSkillId(), skill_lv));
	}
}
```

### Single Action (`GS_SINGLEACTION`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
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
// src/map/status.cpp:2398
aspd = ((int32)(temp_aspd + ((float)(status_calc_aspd(sd, &sd->sc, true) + val) * status->agi / 200)) - min(aspd, 200));
// src/map/status.cpp:2399
return aspd;
// src/map/status.cpp:2402
return AMOTION_ZERO_ASPD;
// src/map/status.cpp:4483
base_status->hit += skill*2;
// src/map/status.cpp:4487
base_status->hit += skill;
// src/map/status.cpp:4494
base_status->hit += 2*skill;
// src/map/status.cpp:4496
base_status->hit += skill;
```

### Snake Eye (`GS_SNAKEEYE`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:4483
base_status->hit += skill*2;
// src/map/status.cpp:4487
base_status->hit += skill;
// src/map/status.cpp:4494
base_status->hit += 2*skill;
// src/map/status.cpp:4496
base_status->hit += skill;
// src/map/status.cpp:4501
base_status->hit += skill * 3;
// src/map/status.cpp:4503
base_status->hit += skill * 2;
// src/map/status.cpp:4505
base_status->hit += 20;
// src/map/status.cpp:4507
base_status->hit += skill * 3;
```

### Chain Action (`GS_CHAINACTION`)

武器/物理技能；目标：被动；最高等级 10；射程：-9；命中类型：Multi_Hit；段数：2；属性：Weapon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillChainAction`
- 实现文件：`src/map/skills/gunslinger/chainaction.cpp`

#### `SkillChainAction::SkillChainAction`

来源：`src/map/skills/gunslinger/chainaction.cpp:8-9`

```cpp
SkillChainAction::SkillChainAction() : WeaponSkillImpl(GS_CHAINACTION) {
}
```

#### `SkillChainAction::modifyDamageData`

来源：`src/map/skills/gunslinger/chainaction.cpp:11-14`

```cpp
void SkillChainAction::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	// For NPC used skill.
	dmg.type = DMG_MULTI_HIT;
}
```

### Tracking (`GS_TRACKING`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-9；命中类型：Single；段数：1；属性：Weapon；吟唱：Lv1=1200; Lv2=1400; Lv3=1600; Lv4=1800; Lv5=2000; Lv6=2200; Lv7=2400; Lv8=2600; Lv9=2800; Lv10=3000 ms；消耗/限制：SP Lv1=15; Lv2=20; Lv3=25; Lv4=30; Lv5=35; Lv6=40; Lv7=45; Lv8=50; Lv9=55; Lv10=60；弹药数 1；武器 Revolver, Rifle；弹药 Bullet。

- 覆盖：`exact-class-methods`
- 实现类：`SkillTracking`
- 实现文件：`src/map/skills/gunslinger/tracking.cpp`

#### `SkillTracking::SkillTracking`

来源：`src/map/skills/gunslinger/tracking.cpp:6-7`

```cpp
SkillTracking::SkillTracking() : WeaponSkillImpl(GS_TRACKING) {
}
```

#### `SkillTracking::calculateSkillRatio`

来源：`src/map/skills/gunslinger/tracking.cpp:9-11`

```cpp
void SkillTracking::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 100 * (skill_lv + 1);
}
```

### Disarm (`GS_DISARM`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：-9；命中类型：Single；段数：1；属性：Weapon；持续时间1：30000 ms；消耗/限制：SP Lv1=15; Lv2=20; Lv3=25; Lv4=30; Lv5=35；弹药数 1；武器 Revolver, Rifle；弹药 Bullet；关联状态：StripWeapon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDisarm`
- 实现文件：`src/map/skills/gunslinger/disarm.cpp`

#### `SkillDisarm::SkillDisarm`

来源：`src/map/skills/gunslinger/disarm.cpp:8-9`

```cpp
SkillDisarm::SkillDisarm() : WeaponSkillImpl(GS_DISARM) {
}
```

#### `SkillDisarm::applyAdditionalEffects`

来源：`src/map/skills/gunslinger/disarm.cpp:11-14`

```cpp
void SkillDisarm::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	skill_strip_equip(src, target, getSkillId(), skill_lv);
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
}
```

### Piercing Shot (`GS_PIERCINGSHOT`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：-9；命中类型：Single；段数：1；属性：Weapon；吟唱：1500 ms；持续时间2：120000 ms；伤害标记：IgnoreDefense；消耗/限制：SP Lv1=11; Lv2=12; Lv3=13; Lv4=14; Lv5=15；弹药数 1；武器 Revolver, Rifle；弹药 Bullet；关联状态：Bleeding。

- 覆盖：`exact-class-methods`
- 实现类：`SkillPiercingShot`
- 实现文件：`src/map/skills/gunslinger/piercingshot.cpp`

#### `SkillPiercingShot::SkillPiercingShot`

来源：`src/map/skills/gunslinger/piercingshot.cpp:9-10`

```cpp
SkillPiercingShot::SkillPiercingShot() : WeaponSkillImpl(GS_PIERCINGSHOT) {
}
```

#### `SkillPiercingShot::calculateSkillRatio`

来源：`src/map/skills/gunslinger/piercingshot.cpp:12-23`

```cpp
void SkillPiercingShot::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd && sd->weapontype1 == W_RIFLE)
		base_skillratio += 150 + 30 * skill_lv;
	else
		base_skillratio += 100 + 20 * skill_lv;
#else
	base_skillratio += 20 * skill_lv;
#endif
}
```

#### `SkillPiercingShot::applyAdditionalEffects`

来源：`src/map/skills/gunslinger/piercingshot.cpp:25-27`

```cpp
void SkillPiercingShot::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start2(src, target, SC_BLEEDING, (skill_lv * 3), skill_lv, src->id, skill_get_time2(getSkillId(), skill_lv));
}
```

### Rapid Shower (`GS_RAPIDSHOWER`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-9；命中类型：Multi_Hit；段数：-5；属性：Weapon；技能后摇：1000 ms；消耗/限制：SP Lv1=22; Lv2=24; Lv3=26; Lv4=28; Lv5=30; Lv6=32; Lv7=34; Lv8=36; Lv9=38; Lv10=40；弹药数 5；武器 Revolver；弹药 Bullet。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRapidShower`
- 实现文件：`src/map/skills/gunslinger/rapidshower.cpp`

#### `SkillRapidShower::SkillRapidShower`

来源：`src/map/skills/gunslinger/rapidshower.cpp:6-7`

```cpp
SkillRapidShower::SkillRapidShower() : WeaponSkillImpl(GS_RAPIDSHOWER) {
}
```

#### `SkillRapidShower::calculateSkillRatio`

来源：`src/map/skills/gunslinger/rapidshower.cpp:9-11`

```cpp
void SkillRapidShower::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 400 + 50 * skill_lv;
}
```

### Desperado (`GS_DESPERADO`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Multi_Hit；段数：1；属性：Weapon；范围：3；技能后摇：1000 ms；移动后摇：1000 ms；持续时间1：1000 ms；伤害标记：Splash；消耗/限制：SP Lv1=32; Lv2=34; Lv3=36; Lv4=38; Lv5=40; Lv6=42; Lv7=44; Lv8=46; Lv9=48; Lv10=50；弹药数 10；武器 Revolver；弹药 Bullet。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDesperado`
- 实现文件：`src/map/skills/gunslinger/desperado.cpp`

#### `SkillDesperado::SkillDesperado`

来源：`src/map/skills/gunslinger/desperado.cpp:8-9`

```cpp
SkillDesperado::SkillDesperado() : SkillImpl(GS_DESPERADO) {
}
```

#### `SkillDesperado::calculateSkillRatio`

来源：`src/map/skills/gunslinger/desperado.cpp:11-17`

```cpp
void SkillDesperado::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_change *sc = status_get_sc(src);

	base_skillratio += 50 * (skill_lv - 1);
	if (sc && sc->getSCE(SC_FALLEN_ANGEL))
		base_skillratio *= 2;
}
```

#### `SkillDesperado::castendPos2`

来源：`src/map/skills/gunslinger/desperado.cpp:19-23`

```cpp
void SkillDesperado::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;
	skill_unitsetting(src, getSkillId(), skill_lv, x, y, 0);
}
```

### Gatling Fever (`GS_GATLINGFEVER`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；属性：Weapon；持续时间1：Lv1=30000; Lv2=45000; Lv3=60000; Lv4=75000; Lv5=90000; Lv6=105000; Lv7=120000; Lv8=135000; Lv9=150000; Lv10=165000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=30; Lv2=32; Lv3=34; Lv4=36; Lv5=38; Lv6=40; Lv7=42; Lv8=44; Lv9=46; Lv10=48；武器 Gatling；关联状态：GatlingFever。

- 覆盖：`exact-class-methods`
- 实现类：`SkillGatlingfever`
- 实现文件：`src/map/skills/gunslinger/gatlingfever.cpp`

#### `SkillGatlingfever::SkillGatlingfever`

来源：`src/map/skills/gunslinger/gatlingfever.cpp:9-10`

```cpp
SkillGatlingfever::SkillGatlingfever() : SkillImpl(GS_GATLINGFEVER) {
}
```

#### `SkillGatlingfever::castendNoDamageId`

来源：`src/map/skills/gunslinger/gatlingfever.cpp:12-23`

```cpp
void SkillGatlingfever::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	status_change *tsc = status_get_sc(target);
	sc_type type = skill_get_sc(getSkillId());
	status_change_entry *tsce = (tsc) ? tsc->getSCE(type) : nullptr;

	if (tsce) {
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv, status_change_end(target, type));
		return;
	}

	clif_skill_nodamage(src, *target, getSkillId(), skill_lv, sc_start(src, target, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
}
```

### Dust (`GS_DUST`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：2；命中类型：Single；段数：1；属性：Weapon；击退：5；吟唱：1000 ms；技能后摇：1000 ms；消耗/限制：SP Lv1=3; Lv2=6; Lv3=9; Lv4=12; Lv5=15; Lv6=18; Lv7=21; Lv8=24; Lv9=27; Lv10=30；弹药数 1；武器 Shotgun；弹药 Bullet。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDust`
- 实现文件：`src/map/skills/gunslinger/dust.cpp`

#### `SkillDust::SkillDust`

来源：`src/map/skills/gunslinger/dust.cpp:6-7`

```cpp
SkillDust::SkillDust() : WeaponSkillImpl(GS_DUST) {
}
```

#### `SkillDust::calculateSkillRatio`

来源：`src/map/skills/gunslinger/dust.cpp:9-11`

```cpp
void SkillDust::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 50 * skill_lv;
}
```

### Full Buster (`GS_FULLBUSTER`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-9；命中类型：Single；段数：1；属性：Weapon；技能后摇：Lv1=1200; Lv2=1400; Lv3=1600; Lv4=1800; Lv5=2000; Lv6=2200; Lv7=2400; Lv8=2600; Lv9=2800; Lv10=3000 ms；持续时间2：10000 ms；消耗/限制：SP Lv1=20; Lv2=25; Lv3=30; Lv4=35; Lv5=40; Lv6=45; Lv7=50; Lv8=55; Lv9=60; Lv10=65；弹药数 Lv1-2=2; Lv3-4=4; Lv5-6=6; Lv7-8=8; Lv9-10=10；武器 Shotgun；弹药 Bullet。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFullBuster`
- 实现文件：`src/map/skills/gunslinger/fullbuster.cpp`

#### `SkillFullBuster::SkillFullBuster`

来源：`src/map/skills/gunslinger/fullbuster.cpp:8-9`

```cpp
SkillFullBuster::SkillFullBuster() : WeaponSkillImpl(GS_FULLBUSTER) {
}
```

#### `SkillFullBuster::applyCounterAdditionalEffects`

来源：`src/map/skills/gunslinger/fullbuster.cpp:11-13`

```cpp
void SkillFullBuster::applyCounterAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& attack_type) const {
	sc_start(src, src, SC_BLIND, 2 * skill_lv, skill_lv, skill_get_time2(getSkillId(), skill_lv));
}
```

#### `SkillFullBuster::calculateSkillRatio`

来源：`src/map/skills/gunslinger/fullbuster.cpp:15-17`

```cpp
void SkillFullBuster::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 100 * (skill_lv + 2);
}
```

### Spread Attack (`GS_SPREADATTACK`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-9；命中类型：Single；段数：1；属性：Weapon；范围：Lv1-3=1; Lv4-6=2; Lv7-9=3; Lv10=4；伤害标记：Splash；消耗/限制：SP Lv1=15; Lv2=20; Lv3=25; Lv4=30; Lv5=35; Lv6=40; Lv7=45; Lv8=50; Lv9=55; Lv10=60；弹药数 5；武器 Shotgun；弹药 Bullet。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpreadAttack`
- 实现文件：`src/map/skills/gunslinger/spreadattack.cpp`

#### `SkillSpreadAttack::SkillSpreadAttack`

来源：`src/map/skills/gunslinger/spreadattack.cpp:6-7`

```cpp
SkillSpreadAttack::SkillSpreadAttack() : SkillImplRecursiveDamageSplash(GS_SPREADATTACK) {
}
```

#### `SkillSpreadAttack::calculateSkillRatio`

来源：`src/map/skills/gunslinger/spreadattack.cpp:9-15`

```cpp
void SkillSpreadAttack::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 30 * skill_lv;
#else
	base_skillratio += 20 * (skill_lv - 1);
#endif
}
```

### Ground Drift (`GS_GROUNDDRIFT`)

武器/物理技能；目标：地面区域；最高等级 10；射程：-9；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：3；吟唱：2000 ms；持续时间1：Lv1=3000; Lv2=6000; Lv3=9000; Lv4=12000; Lv5=15000; Lv6=18000; Lv7=21000; Lv8=24000; Lv9=27000; Lv10=30000 ms；持续时间2：Lv1=5000; Lv2=30000; Lv3=60000; Lv4=12000 ms；伤害标记：Splash, IgnoreAtkCard, IgnoreFlee；消耗/限制：SP Lv1=4; Lv2=8; Lv3=12; Lv4=16; Lv5=20; Lv6=24; Lv7=28; Lv8=32; Lv9=36; Lv10=40；弹药数 1；武器 Grenade；弹药 Grenade。

- 覆盖：`exact-class-methods`
- 实现类：`SkillGroundDrift`
- 实现文件：`src/map/skills/gunslinger/grounddrift.cpp`

#### `SkillGroundDrift::SkillGroundDrift`

来源：`src/map/skills/gunslinger/grounddrift.cpp:10-11`

```cpp
SkillGroundDrift::SkillGroundDrift() : SkillImpl(GS_GROUNDDRIFT) {
}
```

#### `SkillGroundDrift::modifyDamageData`

来源：`src/map/skills/gunslinger/grounddrift.cpp:13-18`

```cpp
void SkillGroundDrift::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const status_data* sstatus = status_get_status_data(src);

	dmg.amotion = sstatus->amotion;
	dmg.blewcount = 0;
}
```

#### `SkillGroundDrift::calculateSkillRatio`

来源：`src/map/skills/gunslinger/grounddrift.cpp:20-24`

```cpp
void SkillGroundDrift::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 100 + 20 * skill_lv;
#endif
}
```

#### `SkillGroundDrift::castendPos2`

来源：`src/map/skills/gunslinger/grounddrift.cpp:26-29`

```cpp
void SkillGroundDrift::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	// Ammo should be deleted right away.
	skill_unitsetting(src, getSkillId(), skill_lv, x, y, 0);
}
```

#### `SkillGroundDrift::modifyElement`

来源：`src/map/skills/gunslinger/grounddrift.cpp:31-33`

```cpp
void SkillGroundDrift::modifyElement(const Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv, int32& element, int32 flag) const {
	element = dmg.miscflag; // element comes in flag.
}
```
