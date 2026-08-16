# Alchemist 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 226 | `AM_AXEMASTERY` / Axe Mastery | `core-source-references` | `` | src/map/battle.cpp |
| 227 | `AM_LEARNINGPOTION` / Potion Research | `core-source-references` | `` | src/map/pc.cpp, src/map/skill.cpp, src/map/skills/merchant/acidterror.cpp, src/map/skills/merchant/aidberserkpotion.cpp, src/map/skills/merchant/aidcondensedpotion.cpp, src/map/skills/merchant/aidpotion.cpp |
| 228 | `AM_PHARMACY` / Prepare Potion | `exact-class-methods` | `SkillPreparePotion` | src/map/skills/merchant/preparepotion.cpp |
| 229 | `AM_DEMONSTRATION` / Bomb | `exact-class-methods` | `SkillBomb` | src/map/skills/merchant/bomb.cpp |
| 230 | `AM_ACIDTERROR` / Acid Terror | `exact-class-methods` | `SkillAcidTerror` | src/map/skills/merchant/acidterror.cpp |
| 231 | `AM_POTIONPITCHER` / Aid Potion | `exact-class-methods` | `SkillAidPotion` | src/map/skills/merchant/aidpotion.cpp |
| 232 | `AM_CANNIBALIZE` / Summon Flora | `exact-class-methods` | `SkillSummonFlora` | src/map/skills/merchant/summonflora.cpp |
| 233 | `AM_SPHEREMINE` / Summon Marine Sphere | `exact-class-methods` | `SkillSummonMarineSphere` | src/map/skills/merchant/summonmarinesphere.cpp |
| 234 | `AM_CP_WEAPON` / Alchemical Weapon | `exact-class-methods` | `SkillAlchemicalWeapon` | src/map/skills/merchant/alchemicalweapon.cpp |
| 235 | `AM_CP_SHIELD` / Synthesized Shield | `exact-class-methods` | `SkillSynthesizedShield` | src/map/skills/merchant/synthesizedshield.cpp |
| 236 | `AM_CP_ARMOR` / Synthetic Armor | `exact-class-methods` | `SkillSyntheticArmor` | src/map/skills/merchant/syntheticarmor.cpp |
| 237 | `AM_CP_HELM` / Biochemical Helm | `exact-class-methods` | `SkillBiochemicalHelm` | src/map/skills/merchant/biochemicalhelm.cpp |
| 238 | `AM_BIOETHICS` / Bioethics | `core-source-references` | `` | src/map/skill.cpp |
| 243 | `AM_CALLHOMUN` / Call Homunculus | `exact-class-methods` | `SkillCallHomunculus` | src/map/skills/merchant/callhomunculus.cpp |
| 244 | `AM_REST` / Vaporize | `exact-class-methods` | `SkillVaporize` | src/map/skills/merchant/vaporize.cpp |
| 247 | `AM_RESURRECTHOMUN` / Homunculus Resurrection | `exact-class-methods` | `SkillHomunculusResurrection` | src/map/skills/merchant/homunculusresurrection.cpp |
| 446 | `AM_BERSERKPITCHER` / Aid Berserk Potion | `exact-class-methods` | `SkillAidBerserkPotion` | src/map/skills/merchant/aidberserkpotion.cpp |
| 496 | `AM_TWILIGHT1` / Twilight Alchemy 1 | `exact-class-methods` | `SkillTwilightAlchemy1` | src/map/skills/merchant/twilightalchemy1.cpp |
| 497 | `AM_TWILIGHT2` / Twilight Alchemy 2 | `exact-class-methods` | `SkillTwilightAlchemy2` | src/map/skills/merchant/twilightalchemy2.cpp |
| 498 | `AM_TWILIGHT3` / Twilight Alchemy 3 | `exact-class-methods` | `SkillTwilightAlchemy3` | src/map/skills/merchant/twilightalchemy3.cpp |

## 详细公式与效果实现

### Axe Mastery (`AM_AXEMASTERY`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2323
damage += damage * 30 / 100;
// src/map/battle.cpp:2335
damage += (skill * 3);
// src/map/battle.cpp:2339
damage += (skill * 4);
// src/map/battle.cpp:2341
damage += skill * 10;
// src/map/battle.cpp:2345
damage += (skill * 4);
// src/map/battle.cpp:2351
damage += (skill * 4);
// src/map/battle.cpp:2353
damage += (skill * 5);
// src/map/battle.cpp:2356
damage += (skill * 10);
// src/map/battle.cpp:2362
damage += (skill * 3);
// src/map/battle.cpp:2364
damage += (skill * 5);
// src/map/battle.cpp:2369
damage += (skill * 3);
// src/map/battle.cpp:2371
damage += (skill * 4);
```

### Potion Research (`AM_LEARNINGPOTION`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/merchant/acidterror.cpp`, `src/map/skills/merchant/aidberserkpotion.cpp`, `src/map/skills/merchant/aidcondensedpotion.cpp`, `src/map/skills/merchant/aidpotion.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:10688
* Heal player HP and/or SP linearly. Calculate any bonus based on active statuses.
// src/map/pc.cpp:10691
* @param hp: HP to heal
// src/map/pc.cpp:10692
* @param sp: SP to heal
// src/map/pc.cpp:10693
* @return Amount healed to an object
// src/map/pc.cpp:10695
int32 pc_itemheal(map_session_data *sd, t_itemid itemid, int32 hp, int32 sp)
// src/map/pc.cpp:10699
if (hp) {
// src/map/pc.cpp:10705
bonus += bonus; // Receive an additional +100% effect from ranked potions to HP only
// src/map/pc.cpp:10708
bonus += sd->bonus.itemhealrate2;
// src/map/pc.cpp:10710
bonus += bonus * pc_get_itemgroup_bonus(sd, itemid, sd->itemgrouphealrate) / 100;
// src/map/pc.cpp:10712
for(const auto &it : sd->itemhealrate) {
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
```

### Prepare Potion (`AM_PHARMACY`)

非伤害技能；目标：自身；最高等级 10；命中类型：Single；伤害标记：NoDamage；消耗/限制：SP 5；道具 Medicine_Bowl×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillPreparePotion`
- 实现文件：`src/map/skills/merchant/preparepotion.cpp`

#### `SkillPreparePotion::SkillPreparePotion`

来源：`src/map/skills/merchant/preparepotion.cpp:9-10`

```cpp
SkillPreparePotion::SkillPreparePotion() : SkillImpl(AM_PHARMACY) {
}
```

#### `SkillPreparePotion::castendNoDamageId`

来源：`src/map/skills/merchant/preparepotion.cpp:12-19`

```cpp
void SkillPreparePotion::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if(sd) {
		clif_skill_produce_mix_list( *sd, getSkillId(), 22);
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
	}
}
```

### Bomb (`AM_DEMONSTRATION`)

武器/物理技能；目标：地面区域；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Fire；吟唱：1000 ms；持续时间1：Lv1=40000; Lv2=45000; Lv3=50000; Lv4=55000; Lv5=60000 ms；伤害标记：NoDamage, IgnoreAtkCard；消耗/限制：SP 10；道具 Fire_Bottle×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBomb`
- 实现文件：`src/map/skills/merchant/bomb.cpp`

#### `SkillBomb::SkillBomb`

来源：`src/map/skills/merchant/bomb.cpp:10-11`

```cpp
SkillBomb::SkillBomb() : SkillImpl(AM_DEMONSTRATION) {
}
```

#### `SkillBomb::castendPos2`

来源：`src/map/skills/merchant/bomb.cpp:13-18`

```cpp
void SkillBomb::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag|=1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillBomb::calculateSkillRatio`

来源：`src/map/skills/merchant/bomb.cpp:20-22`

```cpp
void SkillBomb::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += 20 * skill_lv;
}
```

#### `SkillBomb::applyAdditionalEffects`

来源：`src/map/skills/merchant/bomb.cpp:24-30`

```cpp
void SkillBomb::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
#ifdef RENEWAL
	skill_break_equip(src,target, EQP_WEAPON, 300 * skill_lv, BCT_ENEMY);
#else
	skill_break_equip(src,target, EQP_WEAPON, 100*skill_lv, BCT_ENEMY);
#endif
}
```

### Acid Terror (`AM_ACIDTERROR`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；持续时间1：Lv1=3; Lv2=7; Lv3=10; Lv4=12; Lv5=13 ms；持续时间2：120000 ms；伤害标记：IgnoreAtkCard, IgnoreDefense, IgnoreFlee；消耗/限制：SP 15；道具 Acid_Bottle×1；关联状态：Bleeding。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAcidTerror`
- 实现文件：`src/map/skills/merchant/acidterror.cpp`

#### `SkillAcidTerror::SkillAcidTerror`

来源：`src/map/skills/merchant/acidterror.cpp:12-13`

```cpp
SkillAcidTerror::SkillAcidTerror() : WeaponSkillImpl(AM_ACIDTERROR) {
}
```

#### `SkillAcidTerror::calculateSkillRatio`

来源：`src/map/skills/merchant/acidterror.cpp:15-25`

```cpp
void SkillAcidTerror::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const map_session_data* sd = BL_CAST(BL_PC, src);

	base_skillratio += -100 + 200 * skill_lv;
	if (sd && pc_checkskill(sd, AM_LEARNINGPOTION))
		base_skillratio += 100; // !TODO: What's this bonus increase?
#else
	base_skillratio += -50 + 50 * skill_lv;
#endif
}
```

#### `SkillAcidTerror::applyAdditionalEffects`

来源：`src/map/skills/merchant/acidterror.cpp:27-35`

```cpp
void SkillAcidTerror::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start2(src,target,SC_BLEEDING,(skill_lv*3),skill_lv,src->id,skill_get_time2(getSkillId(),skill_lv));
#ifdef RENEWAL
	if (skill_break_equip(src,target, EQP_ARMOR, (1000 * skill_lv + 500) - 1000, BCT_ENEMY))
#else
	if (skill_break_equip(src,target, EQP_ARMOR, 100*skill_get_time(getSkillId(),skill_lv), BCT_ENEMY))
#endif
		clif_emotion( *target, ET_HUK );
}
```

### Aid Potion (`AM_POTIONPITCHER`)

非伤害技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；技能后摇：500 ms；伤害标记：NoDamage；消耗/限制：SP 1；道具 Red_Potion×1, Orange_Potion×1, Yellow_Potion×1, White_Potion×1, Blue_Potion×1, Fruit_Of_Mastela×1, Royal_Jelly×1, Seed_Of_Yggdrasil×1, Yggdrasilberry×1, Berserk_Potion×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAidPotion`
- 实现文件：`src/map/skills/merchant/aidpotion.cpp`

#### `SkillAidPotion::SkillAidPotion`

来源：`src/map/skills/merchant/aidpotion.cpp:13-14`

```cpp
SkillAidPotion::SkillAidPotion() : SkillImpl(AM_POTIONPITCHER) {
}
```

#### `SkillAidPotion::castendNoDamageId`

来源：`src/map/skills/merchant/aidpotion.cpp:16-149`

```cpp
void SkillAidPotion::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	status_data* sstatus = status_get_status_data(*src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);
	mob_data* dstmd = BL_CAST(BL_MOB, target);
	status_data* tstatus = status_get_status_data(*target);
	status_change* tsc = status_get_sc(target);

	int32 j,hp = 0,sp = 0;
	if( dstmd && dstmd->mob_id == MOBID_EMPERIUM ) {
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}
	if( sd ) {
		int32 x,bonus=100;
		struct s_skill_condition require = skill_get_requirement(sd, getSkillId(), skill_lv);
		x = skill_lv%11 - 1;
		j = pc_search_inventory(sd, require.itemid[x]);
		if (j < 0 || require.itemid[x] <= 0) {
			clif_skill_fail( *sd, getSkillId() );
			flag |= SKILL_NOCONSUME_REQ;
			return;
		}
		if (sd->inventory_data[j] == nullptr || sd->inventory.u.items_inventory[j].amount < require.amount[x]) {
			clif_skill_fail( *sd, getSkillId() );
			flag |= SKILL_NOCONSUME_REQ;
			return;
		}
		potion_flag = 1;
		potion_hp = potion_sp = potion_per_hp = potion_per_sp = 0;
		potion_target = target->id;
		run_script(sd->inventory_data[j]->script,0,sd->id,0);
		potion_flag = potion_target = 0;
		if( sd->sc.getSCE(SC_SPIRIT) && sd->sc.getSCE(SC_SPIRIT)->val2 == SL_ALCHEMIST )
			bonus += sd->status.base_level;
		if( potion_per_hp > 0 || potion_per_sp > 0 ) {
			hp = tstatus->max_hp * potion_per_hp / 100;
			hp = hp * (100 + pc_checkskill(sd,AM_POTIONPITCHER)*10 + pc_checkskill(sd,AM_LEARNINGPOTION)*5)*bonus/10000;
			if( dstsd ) {
				sp = dstsd->status.max_sp * potion_per_sp / 100;
				sp = sp * (100 + pc_checkskill(sd,AM_POTIONPITCHER)*10 + pc_checkskill(sd,AM_LEARNINGPOTION)*5)*bonus/10000;
			}
		} else {
			if( potion_hp > 0 ) {
				hp = potion_hp * (100 + pc_checkskill(sd,AM_POTIONPITCHER)*10 + pc_checkskill(sd,AM_LEARNINGPOTION)*5)*bonus/10000;
				hp = hp * (100 + (tstatus->vit * 2)) / 100;
				if( dstsd )
					hp = hp * (100 + pc_checkskill(dstsd,SM_RECOVERY)*10) / 100;
			}
			if( potion_sp > 0 ) {
				sp = potion_sp * (100 + pc_checkskill(sd,AM_POTIONPITCHER)*10 + pc_checkskill(sd,AM_LEARNINGPOTION)*5)*bonus/10000;
				sp = sp * (100 + (tstatus->int_ * 2)) / 100;
				if( dstsd )
					sp = sp * (100 + pc_checkskill(dstsd,MG_SRECOVERY)*10) / 100;
			}
		}

		if ((bonus = pc_get_itemgroup_bonus_group(sd, IG_POTION, sd->itemgrouphealrate))) {
			hp += hp * bonus / 100;
		}

		if( ( bonus = pc_get_itemgroup_bonus_group( sd, IG_POTION, sd->itemgroupsphealrate ) ) ){
			sp += sp * bonus / 100;
		}

		if( (j = pc_skillheal_bonus(sd, getSkillId())) ) {
			hp += hp * j / 100;
			sp += sp * j / 100;
		}
	} else {
		//Maybe replace with potion_hp, but I'm unsure how that works [Playtester]
		switch (skill_lv) {
			case 1: hp = 45; break;
			case 2: hp = 105; break;
			case 3: hp = 175; break;
			default: hp = 325; break;
		}
		hp = (hp + rnd()%(skill_lv*20+1)) * (150 + skill_lv*10) / 100;
		hp = hp * (100 + (tstatus->vit * 2)) / 100;
		if( dstsd )
			hp = hp * (100 + pc_checkskill(dstsd,SM_RECOVERY)*10) / 100;
	}
	if( dstsd && (j = pc_skillheal2_bonus(dstsd, getSkillId())) ) {
		hp += hp * j / 100;
		sp += sp * j / 100;
	}
	// Final heal increased by HPlus.
	// Is this the right place for this??? [Rytech]
	// Can HPlus also affect SP recovery???
	if (sd && sstatus->hplus > 0) {
		hp += hp * sstatus->hplus / 100;
		sp += sp * sstatus->hplus / 100;
	}
	if (tsc != nullptr && !tsc->empty()) {
		uint8 penalty = 0;

		if (tsc->getSCE(SC_WATER_INSIGNIA) && tsc->getSCE(SC_WATER_INSIGNIA)->val1 == 2) {
			hp += hp / 10;
			sp += sp / 10;
		}
		if (tsc->getSCE(SC_CRITICALWOUND))
			penalty += tsc->getSCE(SC_CRITICALWOUND)->val2;
		if (tsc->getSCE(SC_DEATHHURT) && tsc->getSCE(SC_DEATHHURT)->val3)
			penalty += 20;
		if (tsc->getSCE(SC_NORECOVER_STATE))
			penalty = 100;
		if (penalty > 0) {
			hp -= hp * penalty / 100;
			sp -= sp * penalty / 100;
		}
	}

#ifdef RENEWAL
	if (target->type == BL_HOM)
		hp *= 3; // Heal effectiveness is 3x for Homunculus
#endif

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
	if( hp > 0 || sp <= 0 )
		clif_skill_nodamage(nullptr,*target,AL_HEAL,hp,1);
	if( sp > 0 )
		clif_skill_nodamage(nullptr,*target,MG_SRECOVERY,sp);
	if (tsc) {
#ifdef RENEWAL
		if (tsc->getSCE(SC_EXTREMITYFIST))
			sp = 0;
#endif
		if (tsc->getSCE(SC_NORECOVER_STATE)) {
			hp = 0;
			sp = 0;
		}
	}
	status_heal(target,hp,sp,0);
}
```

### Summon Flora (`AM_CANNIBALIZE`)

非伤害技能；目标：地面区域；最高等级 5；射程：4；命中类型：Single；段数：1；吟唱：2000 ms；技能后摇：500 ms；持续时间1：Lv1=300000; Lv2=240000; Lv3=180000; Lv4=120000; Lv5=60000 ms；伤害标记：NoDamage；消耗/限制：SP 20；道具 MenEater_Plant_Bottle×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSummonFlora`
- 实现文件：`src/map/skills/merchant/summonflora.cpp`

#### `SkillSummonFlora::SkillSummonFlora`

来源：`src/map/skills/merchant/summonflora.cpp:8-9`

```cpp
SkillSummonFlora::SkillSummonFlora() : SkillImpl(AM_CANNIBALIZE) {
}
```

#### `SkillSummonFlora::castendPos2`

来源：`src/map/skills/merchant/summonflora.cpp:11-27`

```cpp
void SkillSummonFlora::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	int32 summons[5] = { MOBID_G_MANDRAGORA, MOBID_G_HYDRA, MOBID_G_FLORA, MOBID_G_PARASITE, MOBID_G_GEOGRAPHER };
	int32 class_ = summons[skill_lv-1];
	enum mob_ai ai = AI_FLORA;
	mob_data *md;

	// Correct info, don't change any of this! [celest]
	md = mob_once_spawn_sub(src, src->m, x, y, status_get_name(*src), class_, "", SZ_SMALL, ai);
	if (md) {
		md->master_id = src->id;
		md->special_state.ai = ai;
		if( md->deletetimer != INVALID_TIMER )
			delete_timer(md->deletetimer, mob_timer_delete);
		md->deletetimer = add_timer (gettick() + skill_get_time(getSkillId(),skill_lv), mob_timer_delete, md->id, 0);
		mob_spawn (md); //Now it is ready for spawning.
	}
}
```

### Summon Marine Sphere (`AM_SPHEREMINE`)

非伤害技能；目标：地面区域；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：2000 ms；技能后摇：500 ms；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP 10；道具 Mini_Bottle×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSummonMarineSphere`
- 实现文件：`src/map/skills/merchant/summonmarinesphere.cpp`

#### `SkillSummonMarineSphere::SkillSummonMarineSphere`

来源：`src/map/skills/merchant/summonmarinesphere.cpp:8-9`

```cpp
SkillSummonMarineSphere::SkillSummonMarineSphere() : SkillImpl(AM_SPHEREMINE) {
}
```

#### `SkillSummonMarineSphere::castendPos2`

来源：`src/map/skills/merchant/summonmarinesphere.cpp:11-26`

```cpp
void SkillSummonMarineSphere::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	int32 class_ = MOBID_MARINE_SPHERE;
	enum mob_ai ai = AI_SPHERE;
	mob_data *md;

	// Correct info, don't change any of this! [celest]
	md = mob_once_spawn_sub(src, src->m, x, y, status_get_name(*src), class_, "", SZ_SMALL, ai);
	if (md) {
		md->master_id = src->id;
		md->special_state.ai = ai;
		if( md->deletetimer != INVALID_TIMER )
			delete_timer(md->deletetimer, mob_timer_delete);
		md->deletetimer = add_timer (gettick() + skill_get_time(getSkillId(),skill_lv), mob_timer_delete, md->id, 0);
		mob_spawn (md); //Now it is ready for spawning.
	}
}
```

### Alchemical Weapon (`AM_CP_WEAPON`)

武器/物理技能；目标：友方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：Lv1=120000; Lv2=240000; Lv3=360000; Lv4=480000; Lv5=600000 ms；伤害标记：NoDamage；消耗/限制：SP 30；道具 Coating_Bottle×1；关联状态：Cp_Weapon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAlchemicalWeapon`
- 实现文件：`src/map/skills/merchant/alchemicalweapon.cpp`

#### `SkillAlchemicalWeapon::SkillAlchemicalWeapon`

来源：`src/map/skills/merchant/alchemicalweapon.cpp:10-11`

```cpp
SkillAlchemicalWeapon::SkillAlchemicalWeapon() : SkillImpl(AM_CP_WEAPON) {
}
```

#### `SkillAlchemicalWeapon::castendNoDamageId`

来源：`src/map/skills/merchant/alchemicalweapon.cpp:13-24`

```cpp
void SkillAlchemicalWeapon::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if( sd && ( target->type != BL_PC || ( dstsd && pc_checkequip(dstsd,EQP_WEAPON) < 0 ) ) ){
		clif_skill_fail( *sd, getSkillId() );
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start(src,target,skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
}
```

### Synthesized Shield (`AM_CP_SHIELD`)

武器/物理技能；目标：友方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：Lv1=120000; Lv2=240000; Lv3=360000; Lv4=480000; Lv5=600000 ms；伤害标记：NoDamage；消耗/限制：SP 25；道具 Coating_Bottle×1；关联状态：Cp_Shield。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSynthesizedShield`
- 实现文件：`src/map/skills/merchant/synthesizedshield.cpp`

#### `SkillSynthesizedShield::SkillSynthesizedShield`

来源：`src/map/skills/merchant/synthesizedshield.cpp:10-11`

```cpp
SkillSynthesizedShield::SkillSynthesizedShield() : SkillImpl(AM_CP_SHIELD) {
}
```

#### `SkillSynthesizedShield::castendNoDamageId`

来源：`src/map/skills/merchant/synthesizedshield.cpp:13-24`

```cpp
void SkillSynthesizedShield::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if( sd && ( target->type != BL_PC || ( dstsd && pc_checkequip(dstsd,EQP_SHIELD) < 0 ) ) ){
		clif_skill_fail( *sd, getSkillId() );
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start(src,target,skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
}
```

### Synthetic Armor (`AM_CP_ARMOR`)

武器/物理技能；目标：友方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：Lv1=120000; Lv2=240000; Lv3=360000; Lv4=480000; Lv5=600000 ms；伤害标记：NoDamage；消耗/限制：SP 25；道具 Coating_Bottle×1；关联状态：Cp_Armor。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSyntheticArmor`
- 实现文件：`src/map/skills/merchant/syntheticarmor.cpp`

#### `SkillSyntheticArmor::SkillSyntheticArmor`

来源：`src/map/skills/merchant/syntheticarmor.cpp:10-11`

```cpp
SkillSyntheticArmor::SkillSyntheticArmor() : SkillImpl(AM_CP_ARMOR) {
}
```

#### `SkillSyntheticArmor::castendNoDamageId`

来源：`src/map/skills/merchant/syntheticarmor.cpp:13-24`

```cpp
void SkillSyntheticArmor::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if( sd && ( target->type != BL_PC || ( dstsd && pc_checkequip(dstsd,EQP_ARMOR) < 0 ) ) ){
		clif_skill_fail( *sd, getSkillId() );
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start(src,target,skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
}
```

### Biochemical Helm (`AM_CP_HELM`)

武器/物理技能；目标：友方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：Lv1=120000; Lv2=240000; Lv3=360000; Lv4=480000; Lv5=600000 ms；伤害标记：NoDamage；消耗/限制：SP 25；道具 Coating_Bottle×1；关联状态：Cp_Helm。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBiochemicalHelm`
- 实现文件：`src/map/skills/merchant/biochemicalhelm.cpp`

#### `SkillBiochemicalHelm::SkillBiochemicalHelm`

来源：`src/map/skills/merchant/biochemicalhelm.cpp:10-11`

```cpp
SkillBiochemicalHelm::SkillBiochemicalHelm() : SkillImpl(AM_CP_HELM) {
}
```

#### `SkillBiochemicalHelm::castendNoDamageId`

来源：`src/map/skills/merchant/biochemicalhelm.cpp:13-24`

```cpp
void SkillBiochemicalHelm::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if( sd && ( target->type != BL_PC || ( dstsd && pc_checkequip(dstsd,EQP_HEAD_TOP) < 0 ) ) ){
		clif_skill_fail( *sd, getSkillId() );
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start(src,target,skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
}
```

### Bioethics (`AM_BIOETHICS`)

非伤害技能；目标：被动；最高等级 1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:12779
pc_checkskill(sd,j) < skill_produce_db[i].req_skill_lv)
// src/map/skill.cpp:12780
continue; // must iterate again to check other skills that produce it. [malufett]
```

### Call Homunculus (`AM_CALLHOMUN`)

非伤害技能；目标：自身；最高等级 1；范围：1；伤害标记：NoDamage；消耗/限制：SP 10；道具 Germination_Breed×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCallHomunculus`
- 实现文件：`src/map/skills/merchant/callhomunculus.cpp`

#### `SkillCallHomunculus::SkillCallHomunculus`

来源：`src/map/skills/merchant/callhomunculus.cpp:12-13`

```cpp
SkillCallHomunculus::SkillCallHomunculus() : SkillImpl(AM_CALLHOMUN) {
}
```

#### `SkillCallHomunculus::castendNoDamageId`

来源：`src/map/skills/merchant/callhomunculus.cpp:15-24`

```cpp
void SkillCallHomunculus::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd && !hom_call(sd))
		clif_skill_fail( *sd, getSkillId() );
#ifdef RENEWAL
	else if (sd && hom_is_active(sd->hd))
		skill_area_temp[0] = 1; // Already passed pre-cast checks
#endif
}
```

### Vaporize (`AM_REST`)

非伤害技能；目标：自身；最高等级 1；伤害标记：NoDamage；消耗/限制：SP 50。

- 覆盖：`exact-class-methods`
- 实现类：`SkillVaporize`
- 实现文件：`src/map/skills/merchant/vaporize.cpp`

#### `SkillVaporize::SkillVaporize`

来源：`src/map/skills/merchant/vaporize.cpp:10-11`

```cpp
SkillVaporize::SkillVaporize() : SkillImpl(AM_REST) {
}
```

#### `SkillVaporize::castendNoDamageId`

来源：`src/map/skills/merchant/vaporize.cpp:13-22`

```cpp
void SkillVaporize::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd) {
		if (hom_vaporize(sd,HOM_ST_REST))
			clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
		else
			clif_skill_fail( *sd, getSkillId() );
	}
}
```

### Homunculus Resurrection (`AM_RESURRECTHOMUN`)

非伤害技能；目标：自身；最高等级 5；命中类型：Single；范围：1；吟唱：2000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=74; Lv2=68; Lv3=62; Lv4=56; Lv5=50。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHomunculusResurrection`
- 实现文件：`src/map/skills/merchant/homunculusresurrection.cpp`

#### `SkillHomunculusResurrection::SkillHomunculusResurrection`

来源：`src/map/skills/merchant/homunculusresurrection.cpp:10-11`

```cpp
SkillHomunculusResurrection::SkillHomunculusResurrection() : SkillImpl(AM_RESURRECTHOMUN) {
}
```

#### `SkillHomunculusResurrection::castendPos2`

来源：`src/map/skills/merchant/homunculusresurrection.cpp:13-24`

```cpp
void SkillHomunculusResurrection::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd)
	{
		if (!hom_ressurect(sd, 20*skill_lv, x, y))
		{
			clif_skill_fail( *sd, getSkillId() );
			return;
		}
	}
}
```

### Aid Berserk Potion (`AM_BERSERKPITCHER`)

非伤害技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；技能后摇：500 ms；伤害标记：NoDamage；消耗/限制：SP 10；SP% 8；道具 Berserk_Potion×2。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAidBerserkPotion`
- 实现文件：`src/map/skills/merchant/aidberserkpotion.cpp`

#### `SkillAidBerserkPotion::SkillAidBerserkPotion`

来源：`src/map/skills/merchant/aidberserkpotion.cpp:13-14`

```cpp
SkillAidBerserkPotion::SkillAidBerserkPotion() : SkillImpl(AM_BERSERKPITCHER) {
}
```

#### `SkillAidBerserkPotion::castendNoDamageId`

来源：`src/map/skills/merchant/aidberserkpotion.cpp:16-154`

```cpp
void SkillAidBerserkPotion::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	status_data* sstatus = status_get_status_data(*src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);
	mob_data* dstmd = BL_CAST(BL_MOB, target);
	status_data* tstatus = status_get_status_data(*target);
	status_change* tsc = status_get_sc(target);

	int32 j,hp = 0,sp = 0;
	if( dstmd && dstmd->mob_id == MOBID_EMPERIUM ) {
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}
	if( sd ) {
		int32 x,bonus=100;
		struct s_skill_condition require = skill_get_requirement(sd, getSkillId(), skill_lv);
		x = skill_lv%11 - 1;
		j = pc_search_inventory(sd, require.itemid[x]);
		if (j < 0 || require.itemid[x] <= 0) {
			clif_skill_fail( *sd, getSkillId() );
			flag |= SKILL_NOCONSUME_REQ;
			return;
		}
		if (sd->inventory_data[j] == nullptr || sd->inventory.u.items_inventory[j].amount < require.amount[x]) {
			clif_skill_fail( *sd, getSkillId() );
			flag |= SKILL_NOCONSUME_REQ;
			return;
		}
		if( dstsd && dstsd->status.base_level < (uint32)sd->inventory_data[j]->elv ) {
			clif_skill_fail( *sd, getSkillId() );
			flag |= SKILL_NOCONSUME_REQ;
			return;
		}
		potion_flag = 1;
		potion_hp = potion_sp = potion_per_hp = potion_per_sp = 0;
		potion_target = target->id;
		run_script(sd->inventory_data[j]->script,0,sd->id,0);
		potion_flag = potion_target = 0;
		if( sd->sc.getSCE(SC_SPIRIT) && sd->sc.getSCE(SC_SPIRIT)->val2 == SL_ALCHEMIST )
			bonus += sd->status.base_level;
		if( potion_per_hp > 0 || potion_per_sp > 0 ) {
			hp = tstatus->max_hp * potion_per_hp / 100;
			hp = hp * (100 + pc_checkskill(sd,AM_POTIONPITCHER)*10 + pc_checkskill(sd,AM_LEARNINGPOTION)*5)*bonus/10000;
			if( dstsd ) {
				sp = dstsd->status.max_sp * potion_per_sp / 100;
				sp = sp * (100 + pc_checkskill(sd,AM_POTIONPITCHER)*10 + pc_checkskill(sd,AM_LEARNINGPOTION)*5)*bonus/10000;
			}
		} else {
			if( potion_hp > 0 ) {
				hp = potion_hp * (100 + pc_checkskill(sd,AM_POTIONPITCHER)*10 + pc_checkskill(sd,AM_LEARNINGPOTION)*5)*bonus/10000;
				hp = hp * (100 + (tstatus->vit * 2)) / 100;
				if( dstsd )
					hp = hp * (100 + pc_checkskill(dstsd,SM_RECOVERY)*10) / 100;
			}
			if( potion_sp > 0 ) {
				sp = potion_sp * (100 + pc_checkskill(sd,AM_POTIONPITCHER)*10 + pc_checkskill(sd,AM_LEARNINGPOTION)*5)*bonus/10000;
				sp = sp * (100 + (tstatus->int_ * 2)) / 100;
				if( dstsd )
					sp = sp * (100 + pc_checkskill(dstsd,MG_SRECOVERY)*10) / 100;
			}
		}

		if ((bonus = pc_get_itemgroup_bonus_group(sd, IG_POTION, sd->itemgrouphealrate))) {
			hp += hp * bonus / 100;
		}

		if( ( bonus = pc_get_itemgroup_bonus_group( sd, IG_POTION, sd->itemgroupsphealrate ) ) ){
			sp += sp * bonus / 100;
		}

		if( (j = pc_skillheal_bonus(sd, getSkillId())) ) {
			hp += hp * j / 100;
			sp += sp * j / 100;
		}
	} else {
		//Maybe replace with potion_hp, but I'm unsure how that works [Playtester]
		switch (skill_lv) {
			case 1: hp = 45; break;
			case 2: hp = 105; break;
			case 3: hp = 175; break;
			default: hp = 325; break;
		}
		hp = (hp + rnd()%(skill_lv*20+1)) * (150 + skill_lv*10) / 100;
		hp = hp * (100 + (tstatus->vit * 2)) / 100;
		if( dstsd )
			hp = hp * (100 + pc_checkskill(dstsd,SM_RECOVERY)*10) / 100;
	}
	if( dstsd && (j = pc_skillheal2_bonus(dstsd, getSkillId())) ) {
		hp += hp * j / 100;
		sp += sp * j / 100;
	}
	// Final heal increased by HPlus.
	// Is this the right place for this??? [Rytech]
	// Can HPlus also affect SP recovery???
	if (sd && sstatus->hplus > 0) {
		hp += hp * sstatus->hplus / 100;
		sp += sp * sstatus->hplus / 100;
	}
	if (tsc != nullptr && !tsc->empty()) {
		uint8 penalty = 0;

		if (tsc->getSCE(SC_WATER_INSIGNIA) && tsc->getSCE(SC_WATER_INSIGNIA)->val1 == 2) {
			hp += hp / 10;
			sp += sp / 10;
		}
		if (tsc->getSCE(SC_CRITICALWOUND))
			penalty += tsc->getSCE(SC_CRITICALWOUND)->val2;
		if (tsc->getSCE(SC_DEATHHURT) && tsc->getSCE(SC_DEATHHURT)->val3)
			penalty += 20;
		if (tsc->getSCE(SC_NORECOVER_STATE))
			penalty = 100;
		if (penalty > 0) {
			hp -= hp * penalty / 100;
			sp -= sp * penalty / 100;
		}
	}

#ifdef RENEWAL
	if (target->type == BL_HOM)
		hp *= 3; // Heal effectiveness is 3x for Homunculus
#endif

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
	if( hp > 0 )
		clif_skill_nodamage(nullptr,*target,AL_HEAL,hp,1);
	if( sp > 0 )
		clif_skill_nodamage(nullptr,*target,MG_SRECOVERY,sp);
	if (tsc) {
#ifdef RENEWAL
		if (tsc->getSCE(SC_EXTREMITYFIST))
			sp = 0;
#endif
		if (tsc->getSCE(SC_NORECOVER_STATE)) {
			hp = 0;
			sp = 0;
		}
	}
	status_heal(target,hp,sp,0);
}
```

### Twilight Alchemy 1 (`AM_TWILIGHT1`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；吟唱：3000 ms；技能后摇：10000 ms；伤害标记：NoDamage；消耗/限制：SP 200；道具 Medicine_Bowl×200。

- 覆盖：`exact-class-methods`
- 实现类：`SkillTwilightAlchemy1`
- 实现文件：`src/map/skills/merchant/twilightalchemy1.cpp`

#### `SkillTwilightAlchemy1::SkillTwilightAlchemy1`

来源：`src/map/skills/merchant/twilightalchemy1.cpp:10-11`

```cpp
SkillTwilightAlchemy1::SkillTwilightAlchemy1() : SkillImpl(AM_TWILIGHT1) {
}
```

#### `SkillTwilightAlchemy1::castendNoDamageId`

来源：`src/map/skills/merchant/twilightalchemy1.cpp:13-22`

```cpp
void SkillTwilightAlchemy1::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd) {
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
		//Prepare 200 White Potions.
		if (!skill_produce_mix(sd, getSkillId(), ITEMID_WHITE_POTION, 0, 0, 0, 200, -1))
			clif_skill_fail( *sd, getSkillId() );
	}
}
```

### Twilight Alchemy 2 (`AM_TWILIGHT2`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；吟唱：3000 ms；技能后摇：10000 ms；伤害标记：NoDamage；消耗/限制：SP 200；道具 Medicine_Bowl×200。

- 覆盖：`exact-class-methods`
- 实现类：`SkillTwilightAlchemy2`
- 实现文件：`src/map/skills/merchant/twilightalchemy2.cpp`

#### `SkillTwilightAlchemy2::SkillTwilightAlchemy2`

来源：`src/map/skills/merchant/twilightalchemy2.cpp:10-11`

```cpp
SkillTwilightAlchemy2::SkillTwilightAlchemy2() : SkillImpl(AM_TWILIGHT2) {
}
```

#### `SkillTwilightAlchemy2::castendNoDamageId`

来源：`src/map/skills/merchant/twilightalchemy2.cpp:13-22`

```cpp
void SkillTwilightAlchemy2::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd) {
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
		//Prepare 200 Slim White Potions.
		if (!skill_produce_mix(sd, getSkillId(), ITEMID_WHITE_SLIM_POTION, 0, 0, 0, 200, -1))
			clif_skill_fail( *sd, getSkillId() );
	}
}
```

### Twilight Alchemy 3 (`AM_TWILIGHT3`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；吟唱：3000 ms；技能后摇：10000 ms；伤害标记：NoDamage；消耗/限制：SP 200；道具 Medicine_Bowl×200。

- 覆盖：`exact-class-methods`
- 实现类：`SkillTwilightAlchemy3`
- 实现文件：`src/map/skills/merchant/twilightalchemy3.cpp`

#### `SkillTwilightAlchemy3::SkillTwilightAlchemy3`

来源：`src/map/skills/merchant/twilightalchemy3.cpp:10-11`

```cpp
SkillTwilightAlchemy3::SkillTwilightAlchemy3() : SkillImpl(AM_TWILIGHT3) {
}
```

#### `SkillTwilightAlchemy3::castendNoDamageId`

来源：`src/map/skills/merchant/twilightalchemy3.cpp:13-35`

```cpp
void SkillTwilightAlchemy3::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd) {
		int32 ebottle = pc_search_inventory(sd,ITEMID_EMPTY_BOTTLE);
		int16 alcohol_idx = -1, acid_idx = -1, fire_idx = -1;
		if( ebottle >= 0 )
			ebottle = sd->inventory.u.items_inventory[ebottle].amount;
		//check if you can produce all three, if not, then fail:
		if (!(alcohol_idx = skill_can_produce_mix(sd,ITEMID_ALCOHOL,-1, 100)) //100 Alcohol
			|| !(acid_idx = skill_can_produce_mix(sd,ITEMID_ACID_BOTTLE,-1, 50)) //50 Acid Bottle
			|| !(fire_idx = skill_can_produce_mix(sd,ITEMID_FIRE_BOTTLE,-1, 50)) //50 Flame Bottle
			|| ebottle < 200 //200 empty bottle are required at total.
		) {
			clif_skill_fail( *sd, getSkillId() );
			return;
		}
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
		skill_produce_mix(sd, getSkillId(), ITEMID_ALCOHOL, 0, 0, 0, 100, alcohol_idx-1);
		skill_produce_mix(sd, getSkillId(), ITEMID_ACID_BOTTLE, 0, 0, 0, 50, acid_idx-1);
		skill_produce_mix(sd, getSkillId(), ITEMID_FIRE_BOTTLE, 0, 0, 0, 50, fire_idx-1);
	}
}
```
