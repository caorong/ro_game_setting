# Rogue 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 2 | `SM_SWORD` / Sword Mastery | `core-source-references` | `` | src/map/battle.cpp |
| 44 | `AC_VULTURE` / Vulture's Eye | `core-source-references` | `` | src/map/battle.cpp, src/map/skill.cpp, src/map/status.cpp |
| 46 | `AC_DOUBLE` / Double Strafe | `exact-class-methods` | `SkillDoubleStrafe` | src/map/skills/archer/doublestrafe.cpp |
| 124 | `HT_REMOVETRAP` / Remove Trap | `exact-class-methods` | `SkillRemoveTrap` | src/map/skills/archer/removetrap.cpp |
| 210 | `RG_SNATCHER` / Gank | `core-source-references` | `` | src/map/pc.cpp, src/map/skill.cpp |
| 211 | `RG_STEALCOIN` / Mug | `exact-class-methods` | `SkillMug` | src/map/skills/thief/mug.cpp |
| 212 | `RG_BACKSTAP` / Back Stab | `exact-class-methods` | `SkillBackStab` | src/map/skills/thief/backstab.cpp |
| 213 | `RG_TUNNELDRIVE` / Stalk | `core-source-references` | `` | src/map/status.cpp |
| 214 | `RG_RAID` / Sightless Mind | `exact-class-methods` | `SkillSightlessMind` | src/map/skills/thief/sightlessmind.cpp |
| 215 | `RG_STRIPWEAPON` / Divest Weapon | `exact-class-methods` | `SkillDivestWeapon` | src/map/skills/thief/divestweapon.cpp |
| 216 | `RG_STRIPSHIELD` / Divest Shield | `exact-class-methods` | `SkillDivestShield` | src/map/skills/thief/divestshield.cpp |
| 217 | `RG_STRIPARMOR` / Divest Armor | `exact-class-methods` | `SkillDivestArmor` | src/map/skills/thief/divestarmor.cpp |
| 218 | `RG_STRIPHELM` / Divest Helm | `exact-class-methods` | `SkillDivestHelm` | src/map/skills/thief/divesthelm.cpp |
| 219 | `RG_INTIMIDATE` / Snatch | `exact-class-methods` | `SkillSnatch` | src/map/skills/thief/snatch.cpp |
| 220 | `RG_GRAFFITI` / Scribble | `exact-class-methods` | `SkillScribble` | src/map/skills/thief/scribble.cpp |
| 221 | `RG_FLAGGRAFFITI` / Piece | `metadata-only` | `` |  |
| 222 | `RG_CLEANER` / Remover | `exact-class-methods` | `SkillRemover` | src/map/skills/thief/remover.cpp |
| 223 | `RG_GANGSTER` / Slyness | `core-source-references` | `` | src/map/skill.cpp |
| 224 | `RG_COMPULSION` / Haggle | `core-source-references` | `` | src/map/pc.cpp |
| 225 | `RG_PLAGIARISM` / Intimidate | `core-source-references` | `` | src/map/pc.cpp, src/map/skill.cpp, src/map/status.cpp |
| 1005 | `RG_CLOSECONFINE` / Close Confine | `exact-class-methods` | `SkillCloseConfine` | src/map/skills/thief/closeconfine.cpp |

## 详细公式与效果实现

### Sword Mastery (`SM_SWORD`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2335
damage += (skill * 3);
// src/map/battle.cpp:2339
damage += (skill * 4);
// src/map/battle.cpp:2341
damage += skill * 10;
// src/map/battle.cpp:2345
damage += (skill * 4);
```

### Vulture's Eye (`AC_VULTURE`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:3278
hitrate += sstatus->hit - flee;
// src/map/battle.cpp:3282
hitrate -= 50;
// src/map/battle.cpp:3285
hitrate += sd->bonus.arrow_hit;
// src/map/battle.cpp:3288
if (sd) //in Renewal hit bonus from Vultures Eye is not anymore shown in status window
// src/map/battle.cpp:3289
hitrate += pc_checkskill(sd,AC_VULTURE);
// src/map/battle.cpp:3295
skill->impl->modifyHitRate(hitrate, src, target, skill_lv);
// src/map/battle.cpp:3297
} else if (sd && wd->type&DMG_MULTI_HIT && wd->div_ == 2) // +1 hit per level of Double Attack on a successful double attack (making sure other multi attack skills do not trigger this) [helvetica]
// src/map/battle.cpp:3298
hitrate += pc_checkskill(sd,TF_DOUBLE);
// src/map/battle.cpp:6618
flee = (flee * (100 - (attacker_count - (battle_config.agi_penalty_count - 1))*battle_config.agi_penalty_num))/100;
// src/map/battle.cpp:6620
flee -= (attacker_count - (battle_config.agi_penalty_count - 1))*battle_config.agi_penalty_num;
// src/map/battle.cpp:6621
if(flee < 1)
// src/map/battle.cpp:6622
flee = 1;
// src/map/battle.cpp:6626
hitrate += sstatus->hit - flee;
// src/map/battle.cpp:6628
if( sd ) //in Renewal hit bonus from Vultures Eye is not shown anymore in status window
// src/map/battle.cpp:6629
hitrate += pc_checkskill(sd,AC_VULTURE);
// src/map/battle.cpp:6631
hitrate = cap_value(hitrate, battle_config.min_hitrate, battle_config.max_hitrate);
```

### Double Strafe (`AC_DOUBLE`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-9；命中类型：Multi_Hit；段数：2；属性：Weapon；持续时间1：100 ms；消耗/限制：SP 12；弹药数 1；武器 Bow；弹药 Arrow。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDoubleStrafe`
- 实现文件：`src/map/skills/archer/doublestrafe.cpp`

#### `SkillDoubleStrafe::SkillDoubleStrafe`

来源：`src/map/skills/archer/doublestrafe.cpp:6-7`

```cpp
SkillDoubleStrafe::SkillDoubleStrafe() : WeaponSkillImpl(AC_DOUBLE) {
}
```

#### `SkillDoubleStrafe::calculateSkillRatio`

来源：`src/map/skills/archer/doublestrafe.cpp:9-11`

```cpp
void SkillDoubleStrafe::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += 10 * (skill_lv - 1);
}
```

### Remove Trap (`HT_REMOVETRAP`)

特殊技能；目标：陷阱；最高等级 1；射程：2；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 5。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRemoveTrap`
- 实现文件：`src/map/skills/archer/removetrap.cpp`

#### `SkillRemoveTrap::SkillRemoveTrap`

来源：`src/map/skills/archer/removetrap.cpp:10-11`

```cpp
SkillRemoveTrap::SkillRemoveTrap() : SkillImpl(HT_REMOVETRAP) {
}
```

#### `SkillRemoveTrap::castendNoDamageId`

来源：`src/map/skills/archer/removetrap.cpp:13-67`

```cpp
void SkillRemoveTrap::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if( sd == nullptr ){
		return;
	}

	skill_unit* su = BL_CAST(BL_SKILL, target);
	std::shared_ptr<s_skill_unit_group> sg;
	std::shared_ptr<s_skill_db> skill_group;

	// Players can only remove their own traps or traps on Vs maps.
	if( su && (sg = su->group) && (sg->src_id == src->id || map_flag_vs(target->m)) && ( skill_group = skill_db.find(sg->skill_id) ) && skill_group->inf2[INF2_ISTRAP] )
	{
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
		if( !(sg->unit_id == UNT_USED_TRAPS || (sg->unit_id == UNT_ANKLESNARE && sg->val2 != 0 )) )
		{ // prevent picking up expired traps
			if( battle_config.skill_removetrap_type )
			{ // get back all items used to deploy the trap
				for( int32 i = 0; i < MAX_SKILL_ITEM_REQUIRE; i++ )
				{
					if( skill_group->require.itemid[i] > 0 )
					{
						int32 flag2;
						struct item item_tmp;
						memset(&item_tmp,0,sizeof(item_tmp));
						item_tmp.nameid = skill_group->require.itemid[i];
						item_tmp.identify = 1;
						item_tmp.amount = skill_group->require.amount[i];
						if( item_tmp.nameid && (flag2=pc_additem(sd,&item_tmp,item_tmp.amount,LOG_TYPE_OTHER)) ){
							clif_additem(sd,0,0,flag2);
							if (battle_config.skill_drop_items_full)
								map_addflooritem(&item_tmp,item_tmp.amount,sd->m,sd->x,sd->y,0,0,0,4,0);
						}
					}
				}
			}
			else
			{ // get back 1 trap
				struct item item_tmp;
				memset(&item_tmp,0,sizeof(item_tmp));
				item_tmp.nameid = su->group->item_id?su->group->item_id:ITEMID_TRAP;
				item_tmp.identify = 1;
				if( item_tmp.nameid && (flag=pc_additem(sd,&item_tmp,1,LOG_TYPE_OTHER)) )
				{
					clif_additem(sd,0,0,flag);
					if (battle_config.skill_drop_items_full)
						map_addflooritem(&item_tmp,1,sd->m,sd->x,sd->y,0,0,0,4,0);
				}
			}
		}
		skill_delunit(su);
	}else
		clif_skill_fail( *sd, getSkillId() );
}
```

### Gank (`RG_SNATCHER`)

武器/物理技能；目标：被动；最高等级 10；属性：Weapon。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:1373
int32 rate = sstatus->con * 10 / 3 + 1;
// src/map/skill.cpp:1375
rate += rate * (20 * pc_checkskill(sd, WH_NATUREFRIENDLY)) / 100;
// src/map/skill.cpp:1377
if (rnd() % 1000 <= rate)
// src/map/skill.cpp:1378
skill_castend_damage_id(src, bl, WH_HAWKRUSH, skill, tick, 0);
// src/map/skill.cpp:1385
clif_skill_nodamage(src,*bl,TF_STEAL,skill);
// src/map/skill.cpp:1392
struct status_change_entry *sce;
// src/map/skill.cpp:1394
if((sce=sc->getSCE(SC_ENCPOISON))) //Don't use sc_start since chance comes in 1/10000 rate.
// src/map/skill.cpp:1395
status_change_start(src,bl,SC_POISON,sce->val2, sce->val1,src->id,0,0,
// src/map/skill.cpp:1396
skill_get_time2(AS_ENCHANTPOISON,sce->val1),SCSTART_NONE);
// src/map/skill.cpp:1399
sc_start4(src,bl,SC_DPOISON,sce->val2, sce->val1,src->id,0,0,
```

### Mug (`RG_STEALCOIN`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：1；命中类型：Single；段数：1；技能后摇：500 ms；伤害标记：NoDamage；消耗/限制：SP 15。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMug`
- 实现文件：`src/map/skills/thief/mug.cpp`

#### `SkillMug::SkillMug`

来源：`src/map/skills/thief/mug.cpp:14-15`

```cpp
SkillMug::SkillMug() : SkillImpl(RG_STEALCOIN) {
}
```

#### `SkillMug::castendNoDamageId`

来源：`src/map/skills/thief/mug.cpp:17-49`

```cpp
void SkillMug::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );
	mob_data *dstmd = BL_CAST(BL_MOB, target);

	if (sd == nullptr || dstmd == nullptr)
		return;

	int32 target_lv = status_get_lv(target);
	int32 rate = 10 * pc_checkskill(sd, RG_STEALCOIN);
	rate += sd->battle_status.dex / 2;
	rate += sd->battle_status.luk / 2;
	rate += 2 * (sd->status.base_level - target_lv);

	if (!rnd_chance_official(rate, 1000))
	{
		clif_skill_fail(*sd, getSkillId());
		return;
	}

	dstmd->state.steal_coin_flag = 1;

	// Zeny Steal Amount
	int32 amount = rnd_value(8 * target_lv, 10 * target_lv);
	amount += (skill_lv * target_lv) / 10;

	pc_getzeny(sd, amount, LOG_TYPE_STEAL);

	// This triggers a 0 damage event and might make the monster switch target to caster
	battle_damage(src, target, 0, 1, skill_lv, 0, ATK_DEF, BF_WEAPON|BF_LONG|BF_NORMAL, true, tick, false);

	// Client uses skill_lv to show how many Zeny were stolen
	clif_skill_nodamage(src, *target, getSkillId(), amount);		
}
```

### Back Stab (`RG_BACKSTAP`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-1；命中类型：Single；段数：1；属性：Weapon；技能后摇：500 ms；伤害标记：IgnoreFlee；消耗/限制：SP 16；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBackStab`
- 实现文件：`src/map/skills/thief/backstab.cpp`

#### `SkillBackStab::SkillBackStab`

来源：`src/map/skills/thief/backstab.cpp:11-12`

```cpp
SkillBackStab::SkillBackStab() : SkillImpl(RG_BACKSTAP) {
}
```

#### `SkillBackStab::modifyDamageData`

来源：`src/map/skills/thief/backstab.cpp:14-21`

```cpp
void SkillBackStab::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
#ifdef RENEWAL
	const map_session_data* sd = BL_CAST(BL_PC, &src);

	if (sd != nullptr && sd->status.weapon == W_DAGGER)
		dmg.div_ = 2;
#endif
}
```

#### `SkillBackStab::calculateSkillRatio`

来源：`src/map/skills/thief/backstab.cpp:23-30`

```cpp
void SkillBackStab::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const map_session_data* sd = BL_CAST( BL_PC, src );

	if(sd && sd->status.weapon == W_BOW && battle_config.backstab_bow_penalty)
		base_skillratio += (200 + 40 * skill_lv) / 2;
	else
		base_skillratio += 200 + 40 * skill_lv;
}
```

#### `SkillBackStab::castendDamageId`

来源：`src/map/skills/thief/backstab.cpp:32-84`

```cpp
void SkillBackStab::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

#ifdef RENEWAL
	uint8 dir = map_calc_dir(src, target->x, target->y);
	int16 x, y;

	if (dir > 0 && dir < 4)
		x = -1;
	else if (dir > 4)
		x = 1;
	else
		x = 0;

	if (dir > 2 && dir < 6)
		y = -1;
	else if (dir == 7 || dir < 2)
		y = 1;
	else
		y = 0;

	if (battle_check_target(src, target, BCT_ENEMY) > 0 && unit_movepos(src, target->x + x, target->y + y, 2, true)) { // Display movement + animation.
#else
	if (check_distance_bl(src, target, 0))
		return;

	uint8 dir = map_calc_dir(src, target->x, target->y), t_dir = unit_getdir(target);

	if (!map_check_dir(dir, t_dir) || target->type == BL_SKILL) {
#endif
		status_change_end(src, SC_HIDING);
		dir = dir < 4 ? dir+4 : dir-4; // change direction [Celest]
		unit_setdir(target,dir);
#ifdef RENEWAL
		clif_blown(src);
#endif
		skill_attack(BF_WEAPON, src, src, target, getSkillId(), skill_lv, tick, flag);
	}
	else if (sd)
		clif_skill_fail( *sd, getSkillId() );
}

void SkillBackStab::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
#ifdef RENEWAL
	sc_start(src,target,SC_STUN,(5+2*skill_lv),skill_lv,skill_get_time(getSkillId(),skill_lv));
#endif
}

void SkillBackStab::modifyHitRate(int16& hit_rate, const block_list* src, const block_list* target, uint16 skill_lv) const {
#ifdef RENEWAL
	hit_rate += skill_lv; // !TODO: What's the rate increase?
#endif
}
```

### Stalk (`RG_TUNNELDRIVE`)

非伤害技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:8059
speed_rate -= val;
```

### Sightless Mind (`RG_RAID`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；属性：Weapon；范围：1；持续时间1：5000 ms；持续时间2：30000 ms；伤害标记：Splash；消耗/限制：SP 20；前置状态 Hiding；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSightlessMind`
- 实现文件：`src/map/skills/thief/sightlessmind.cpp`

#### `SkillSightlessMind::SkillSightlessMind`

来源：`src/map/skills/thief/sightlessmind.cpp:11-12`

```cpp
SkillSightlessMind::SkillSightlessMind() : SkillImplRecursiveDamageSplash(RG_RAID) {
}
```

#### `SkillSightlessMind::calculateSkillRatio`

来源：`src/map/skills/thief/sightlessmind.cpp:14-20`

```cpp
void SkillSightlessMind::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += -100 + 50 + skill_lv * 150;
#else
	base_skillratio += 40 * skill_lv;
#endif
}
```

#### `SkillSightlessMind::castendNoDamageId`

来源：`src/map/skills/thief/sightlessmind.cpp:22-30`

```cpp
void SkillSightlessMind::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_area_temp[1] = 0;
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
	map_foreachinrange(skill_area_sub, target,
		skill_get_splash(getSkillId(), skill_lv), BL_CHAR|BL_SKILL,
		src,getSkillId(),skill_lv,tick, flag|BCT_ENEMY|1,
		skill_castend_damage_id);
	status_change_end(src, SC_HIDING);
}
```

#### `SkillSightlessMind::applyAdditionalEffects`

来源：`src/map/skills/thief/sightlessmind.cpp:32-38`

```cpp
void SkillSightlessMind::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src,target,SC_STUN,(10+3*skill_lv),skill_lv,skill_get_time(getSkillId(),skill_lv));
	sc_start(src,target,SC_BLIND,(10+3*skill_lv),skill_lv,skill_get_time2(getSkillId(),skill_lv));
#ifdef RENEWAL
	sc_start(src, target, SC_RAID, 100, skill_lv, 10000); // Hardcoded to 10 seconds since Duration1 and Duration2 are used
#endif
}
```

### Divest Weapon (`RG_STRIPWEAPON`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：Lv1=75000; Lv2=90000; Lv3=105000; Lv4=120000; Lv5=135000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=17; Lv2=19; Lv3=21; Lv4=23; Lv5=25；关联状态：StripWeapon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDivestWeapon`
- 实现文件：`src/map/skills/thief/divestweapon.cpp`

#### `SkillDivestWeapon::SkillDivestWeapon`

来源：`src/map/skills/thief/divestweapon.cpp:9-10`

```cpp
SkillDivestWeapon::SkillDivestWeapon() : SkillImpl(RG_STRIPWEAPON) {
}
```

#### `SkillDivestWeapon::castendNoDamageId`

来源：`src/map/skills/thief/divestweapon.cpp:12-22`

```cpp
void SkillDivestWeapon::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	bool i = skill_strip_equip(src, target, getSkillId(), skill_lv);

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,i);

	//Nothing stripped.
	if( sd && !i )
		clif_skill_fail( *sd, getSkillId() );
}
```

### Divest Shield (`RG_STRIPSHIELD`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：Lv1=75000; Lv2=90000; Lv3=105000; Lv4=120000; Lv5=135000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20；关联状态：StripShield。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDivestShield`
- 实现文件：`src/map/skills/thief/divestshield.cpp`

#### `SkillDivestShield::SkillDivestShield`

来源：`src/map/skills/thief/divestshield.cpp:9-10`

```cpp
SkillDivestShield::SkillDivestShield() : SkillImpl(RG_STRIPSHIELD) {
}
```

#### `SkillDivestShield::castendNoDamageId`

来源：`src/map/skills/thief/divestshield.cpp:12-22`

```cpp
void SkillDivestShield::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	bool i = skill_strip_equip(src, target, getSkillId(), skill_lv);

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,i);

	//Nothing stripped.
	if( sd && !i )
		clif_skill_fail( *sd, getSkillId() );
}
```

### Divest Armor (`RG_STRIPARMOR`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：Lv1=75000; Lv2=90000; Lv3=105000; Lv4=120000; Lv5=135000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=17; Lv2=19; Lv3=21; Lv4=23; Lv5=25；关联状态：StripArmor。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDivestArmor`
- 实现文件：`src/map/skills/thief/divestarmor.cpp`

#### `SkillDivestArmor::SkillDivestArmor`

来源：`src/map/skills/thief/divestarmor.cpp:9-10`

```cpp
SkillDivestArmor::SkillDivestArmor() : SkillImpl(RG_STRIPARMOR) {
}
```

#### `SkillDivestArmor::castendNoDamageId`

来源：`src/map/skills/thief/divestarmor.cpp:12-22`

```cpp
void SkillDivestArmor::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	bool i = skill_strip_equip(src, target, getSkillId(), skill_lv);

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,i);

	//Nothing stripped.
	if( sd && !i )
		clif_skill_fail( *sd, getSkillId() );
}
```

### Divest Helm (`RG_STRIPHELM`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：Lv1=75000; Lv2=90000; Lv3=105000; Lv4=120000; Lv5=135000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20；关联状态：StripHelm。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDivestHelm`
- 实现文件：`src/map/skills/thief/divesthelm.cpp`

#### `SkillDivestHelm::SkillDivestHelm`

来源：`src/map/skills/thief/divesthelm.cpp:9-10`

```cpp
SkillDivestHelm::SkillDivestHelm() : SkillImpl(RG_STRIPHELM) {
}
```

#### `SkillDivestHelm::castendNoDamageId`

来源：`src/map/skills/thief/divesthelm.cpp:12-22`

```cpp
void SkillDivestHelm::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	bool i = skill_strip_equip(src, target, getSkillId(), skill_lv);

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,i);

	//Nothing stripped.
	if( sd && !i )
		clif_skill_fail( *sd, getSkillId() );
}
```

### Snatch (`RG_INTIMIDATE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：1；命中类型：Single；段数：1；属性：Weapon；消耗/限制：SP Lv1=13; Lv2=16; Lv3=19; Lv4=22; Lv5=25。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSnatch`
- 实现文件：`src/map/skills/thief/snatch.cpp`

#### `SkillSnatch::SkillSnatch`

来源：`src/map/skills/thief/snatch.cpp:6-7`

```cpp
SkillSnatch::SkillSnatch() : WeaponSkillImpl(RG_INTIMIDATE) {
}
```

#### `SkillSnatch::calculateSkillRatio`

来源：`src/map/skills/thief/snatch.cpp:9-11`

```cpp
void SkillSnatch::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 30 * skill_lv;
}
```

### Scribble (`RG_GRAFFITI`)

非伤害技能；目标：地面区域；最高等级 1；射程：1；命中类型：Single；段数：1；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 15；道具 Red_Gemstone×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillScribble`
- 实现文件：`src/map/skills/thief/scribble.cpp`

#### `SkillScribble::SkillScribble`

来源：`src/map/skills/thief/scribble.cpp:6-7`

```cpp
SkillScribble::SkillScribble() : SkillImpl(RG_GRAFFITI) {
}
```

#### `SkillScribble::castendPos2`

来源：`src/map/skills/thief/scribble.cpp:9-12`

```cpp
void SkillScribble::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
	flag|=1;
}
```

### Piece (`RG_FLAGGRAFFITI`)

非伤害技能；目标：地面区域；最高等级 5；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 10。

- 覆盖：`metadata-only`
- 实现类：`N/A`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Remover (`RG_CLEANER`)

非伤害技能；目标：地面区域；最高等级 1；射程：1；命中类型：Single；段数：1；范围：5；伤害标记：NoDamage, Splash；消耗/限制：SP 5。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRemover`
- 实现文件：`src/map/skills/thief/remover.cpp`

#### `SkillRemover::SkillRemover`

来源：`src/map/skills/thief/remover.cpp:8-9`

```cpp
SkillRemover::SkillRemover() : SkillImpl(RG_CLEANER) {
}
```

#### `SkillRemover::castendNoDamageId`

来源：`src/map/skills/thief/remover.cpp:11-13`

```cpp
void SkillRemover::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
}
```

#### `SkillRemover::castendPos2`

来源：`src/map/skills/thief/remover.cpp:15-18`

```cpp
void SkillRemover::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	int32 i = skill_get_splash(getSkillId(), skill_lv);
	map_foreachinallarea(skill_graffitiremover,src->m,x-i,y-i,x+i,y+i,BL_SKILL,1);
}
```

### Slyness (`RG_GANGSTER`)

非伤害技能；目标：被动；最高等级 1；范围：1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:10799
status_calc_regen_rate(bl, &sd->regen, &sd->sc);
```

### Haggle (`RG_COMPULSION`)

非伤害技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:5691
int32 skill,val = orig_value,rate1 = 0,rate2 = 0;
// src/map/pc.cpp:5693
rate1 = 5+skill*2-((skill==10)? 1:0);
// src/map/pc.cpp:5695
rate2 = 5+skill*4;
// src/map/pc.cpp:5696
if(rate1 < rate2) rate1 = rate2;
// src/map/pc.cpp:5697
if(rate1)
// src/map/pc.cpp:5698
val = (int32)((double)orig_value*(double)(100-rate1)/100.);
```

### Intimidate (`RG_PLAGIARISM`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:2396
if ((j = static_cast<uint16>(pc_readglobalreg(sd, add_str(sg_info[i].feel_var)))) != 0) {
// src/map/pc.cpp:2403
sd->hate_mob[i] = static_cast<int16>(pc_readglobalreg(sd, add_str(sg_info[i].hate_var)))-1;
// src/map/pc.cpp:2407
uint16 skid = static_cast<uint16>(pc_readglobalreg(sd, add_str(SKILL_VAR_PLAGIARISM)));
// src/map/pc.cpp:2411
sd->status.skill[sd->cloneskill_idx].lv = static_cast<uint8>(pc_readglobalreg(sd, add_str(SKILL_VAR_PLAGIARISM_LV)));
// src/map/pc.cpp:2418
uint16 skid = static_cast<uint16>(pc_readglobalreg(sd, add_str(SKILL_VAR_REPRODUCE)));
// src/map/skill.cpp:812
* Check if the skill is ok to cast and when.
// src/map/skill.cpp:813
* Done before skill_check_condition_castbegin, requirement
// src/map/skill.cpp:814
* @param skill_id: Skill ID that casted
// src/map/skill.cpp:815
* @param sd: Player who casted
// src/map/skill.cpp:2530
* @param src: The caster
// src/map/skill.cpp:2532
* @param skill_id: Skill that casted
// src/map/skill.cpp:2533
* @param skill_lv: Skill level of the casted skill
// src/map/skill.cpp:2535
static void skill_do_copy(block_list* src,block_list *bl, uint16 skill_id, uint16 skill_lv)
// src/map/skill.cpp:2537
TBL_PC *tsd = BL_CAST(BL_PC, bl);
// src/map/skill.cpp:2564
lv = min(skill_lv, pc_checkskill(tsd, RG_PLAGIARISM));
// src/map/status.cpp:8347
if (sc->getSCE(SC_NIBELUNGEN) && sc->getSCE(SC_NIBELUNGEN)->val2 == RINGNBL_ASPDRATE)
```

### Close Confine (`RG_CLOSECONFINE`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：1；命中类型：Single；段数：1；持续时间1：10000 ms；伤害标记：NoDamage；消耗/限制：SP 25；关联状态：CloseConfine2。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCloseConfine`
- 实现文件：`src/map/skills/thief/closeconfine.cpp`

#### `SkillCloseConfine::SkillCloseConfine`

来源：`src/map/skills/thief/closeconfine.cpp:9-10`

```cpp
SkillCloseConfine::SkillCloseConfine() : SkillImpl(RG_CLOSECONFINE) {
}
```

#### `SkillCloseConfine::castendNoDamageId`

来源：`src/map/skills/thief/closeconfine.cpp:12-17`

```cpp
void SkillCloseConfine::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start4(src,target,type,100,skill_lv,src->id,0,0,skill_get_time(getSkillId(),skill_lv)));
}
```
