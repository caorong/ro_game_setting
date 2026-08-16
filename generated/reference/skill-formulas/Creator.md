# Creator 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 478 | `CR_SLIMPITCHER` / Aid Condensed Potion | `exact-class-methods` | `SkillAidCondensedPotion` | src/map/skills/merchant/aidcondensedpotion.cpp |
| 479 | `CR_FULLPROTECTION` / Full Protection | `exact-class-methods` | `SkillFullProtection` | src/map/skills/merchant/fullprotection.cpp |
| 490 | `CR_ACIDDEMONSTRATION` / Acid Demonstration | `exact-class-methods` | `SkillAcidDemonstration` | src/map/skills/merchant/aciddemonstration.cpp |
| 491 | `CR_CULTIVATION` / Plant Cultivation | `exact-class-methods` | `SkillPlantCultivation` | src/map/skills/merchant/plantcultivation.cpp |

## 详细公式与效果实现

### Aid Condensed Potion (`CR_SLIMPITCHER`)

非伤害技能；目标：地面区域；最高等级 10；射程：3；命中类型：Single；段数：1；范围：3；吟唱：1000 ms；技能后摇：1000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 30；道具 Red_Slim_Potion×1, Red_Slim_Potion×1, Red_Slim_Potion×1, Red_Slim_Potion×1, Red_Slim_Potion×1, Yellow_Slim_Potion×1, Yellow_Slim_Potion×1, Yellow_Slim_Potion×1, Yellow_Slim_Potion×1, White_Slim_Potion×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAidCondensedPotion`
- 实现文件：`src/map/skills/merchant/aidcondensedpotion.cpp`

#### `SkillAidCondensedPotion::SkillAidCondensedPotion`

来源：`src/map/skills/merchant/aidcondensedpotion.cpp:13-14`

```cpp
SkillAidCondensedPotion::SkillAidCondensedPotion() : SkillImpl(CR_SLIMPITCHER) {
}
```

#### `SkillAidCondensedPotion::castendNoDamageId`

来源：`src/map/skills/merchant/aidcondensedpotion.cpp:16-59`

```cpp
void SkillAidCondensedPotion::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	mob_data* dstmd = BL_CAST(BL_MOB, target);
	map_session_data* dstsd = BL_CAST( BL_PC, target );
	status_data* tstatus = status_get_status_data(*target);
	status_change *tsc = status_get_sc(target);

	// Updated to block Slim Pitcher from working on barricades and guardian stones.
	if (dstmd && (dstmd->mob_id == MOBID_EMPERIUM || status_get_class_(target) == CLASS_BATTLEFIELD))
		return;
	if (potion_hp || potion_sp) {
		int32 hp = potion_hp, sp = potion_sp;
		hp = hp * (100 + (tstatus->vit * 2))/100;
		sp = sp * (100 + (tstatus->int_ * 2))/100;
		if (dstsd) {
			if (hp)
				hp = hp * (100 + pc_checkskill(dstsd,SM_RECOVERY)*10 + pc_skillheal2_bonus(dstsd, getSkillId()))/100;
			if (sp)
				sp = sp * (100 + pc_checkskill(dstsd,MG_SRECOVERY)*10 + pc_skillheal2_bonus(dstsd, getSkillId()))/100;
		}
		if (tsc != nullptr && !tsc->empty()) {
			uint8 penalty = 0;

			if (tsc->getSCE(SC_WATER_INSIGNIA) && tsc->getSCE(SC_WATER_INSIGNIA)->val1 == 2) {
				hp += hp / 10;
				sp += sp / 10;
			}
			if (tsc->getSCE(SC_CRITICALWOUND))
				penalty += tsc->getSCE(SC_CRITICALWOUND)->val2;
			if (tsc->getSCE(SC_DEATHHURT) && tsc->getSCE(SC_DEATHHURT)->val3 == 1)
				penalty += 20;
			if (tsc->getSCE(SC_NORECOVER_STATE))
				penalty = 100;
			if (penalty > 0) {
				hp -= hp * penalty / 100;
				sp -= sp * penalty / 100;
			}
		}
		if(hp > 0)
			clif_skill_nodamage(nullptr,*target,AL_HEAL,hp);
		if(sp > 0)
			clif_skill_nodamage(nullptr,*target,MG_SRECOVERY,sp);
		status_heal(target,hp,sp,0);
	}
}
```

#### `SkillAidCondensedPotion::castendPos2`

来源：`src/map/skills/merchant/aidcondensedpotion.cpp:61-126`

```cpp
void SkillAidCondensedPotion::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	if (sd) {
		int32 i_lv = 0, j = 0;
		struct s_skill_condition require = skill_get_requirement(sd, getSkillId(), skill_lv);
		i_lv = skill_lv%11 - 1;
		j = pc_search_inventory(sd, require.itemid[i_lv]);
		if (j < 0 || require.itemid[i_lv] <= 0 || sd->inventory_data[j] == nullptr || sd->inventory.u.items_inventory[j].amount < require.amount[i_lv])
		{
			clif_skill_fail( *sd, getSkillId() );
			flag |= SKILL_NOCONSUME_REQ;
			return;
		}
		potion_flag = 1;
		potion_hp = 0;
		potion_sp = 0;
		run_script(sd->inventory_data[j]->script,0,sd->id,0);
		potion_flag = 0;
		//Apply skill bonuses
		i_lv = pc_checkskill(sd,CR_SLIMPITCHER)*10
			+ pc_checkskill(sd,AM_POTIONPITCHER)*10
			+ pc_checkskill(sd,AM_LEARNINGPOTION)*5
			+ pc_skillheal_bonus(sd, getSkillId());

		potion_hp = potion_hp * (100+i_lv)/100;
		potion_sp = potion_sp * (100+i_lv)/100;

		// Final heal increased by HPlus.
		// Is this the right place for this??? [Rytech]
		// Can HPlus also affect SP recovery???
		status_data* sstatus = status_get_status_data(*src);

		if (sstatus && sstatus->hplus > 0) {
			potion_hp += potion_hp * sstatus->hplus / 100;
			potion_sp += potion_sp * sstatus->hplus / 100;
		}

		if(potion_hp > 0 || potion_sp > 0) {
			i_lv = skill_get_splash(getSkillId(), skill_lv);
			map_foreachinallarea(skill_area_sub,
				src->m,x-i_lv,y-i_lv,x+i_lv,y+i_lv,BL_CHAR,
				src,getSkillId(),skill_lv,tick,flag|BCT_PARTY|BCT_GUILD|1,
				skill_castend_nodamage_id);
		}
	} else {
		struct item_data *item = itemdb_search(skill_db.find(getSkillId())->require.itemid[skill_lv - 1]);
		int32 id = skill_get_max(CR_SLIMPITCHER) * 10;

		potion_flag = 1;
		potion_hp = 0;
		potion_sp = 0;
		run_script(item->script,0,src->id,0);
		potion_flag = 0;
		potion_hp = potion_hp * (100+id)/100;
		potion_sp = potion_sp * (100+id)/100;

		if(potion_hp > 0 || potion_sp > 0) {
			id = skill_get_splash(getSkillId(), skill_lv);
			map_foreachinallarea(skill_area_sub,
				src->m,x-id,y-id,x+id,y+id,BL_CHAR,
				src,getSkillId(),skill_lv,tick,flag|BCT_PARTY|BCT_GUILD|1,
					skill_castend_nodamage_id);
		}
	}
}
```

### Full Protection (`CR_FULLPROTECTION`)

武器/物理技能；目标：友方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：Lv1=120000; Lv2=240000; Lv3=360000; Lv4=480000; Lv5=600000 ms；伤害标记：NoDamage；消耗/限制：SP 40；道具 Coating_Bottle×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFullProtection`
- 实现文件：`src/map/skills/merchant/fullprotection.cpp`

#### `SkillFullProtection::SkillFullProtection`

来源：`src/map/skills/merchant/fullprotection.cpp:10-11`

```cpp
SkillFullProtection::SkillFullProtection() : SkillImpl(CR_FULLPROTECTION) {
}
```

#### `SkillFullProtection::castendNoDamageId`

来源：`src/map/skills/merchant/fullprotection.cpp:13-33`

```cpp
void SkillFullProtection::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );
	map_session_data* dstsd = BL_CAST( BL_PC, target );

	uint32 equip[] = {EQP_WEAPON, EQP_SHIELD, EQP_ARMOR, EQP_HEAD_TOP};
	int32 i_eqp, s = 0, skilltime = skill_get_time(getSkillId(),skill_lv);

	for (i_eqp = 0; i_eqp < 4; i_eqp++) {
		if( target->type != BL_PC || ( dstsd && pc_checkequip(dstsd,equip[i_eqp]) < 0 ) )
			continue;
		sc_start(src,target,(sc_type)(SC_CP_WEAPON + i_eqp),100,skill_lv,skilltime);
		s++;
	}
	if( sd && !s ){
		clif_skill_fail( *sd, getSkillId() );
		// Don't consume item requirements
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
}
```

### Acid Demonstration (`CR_ACIDDEMONSTRATION`)

特殊技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；吟唱：1000 ms；技能后摇：1000 ms；伤害标记：IgnoreFlee；消耗/限制：SP 30；道具 Fire_Bottle×1, Acid_Bottle×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAcidDemonstration`
- 实现文件：`src/map/skills/merchant/aciddemonstration.cpp`

#### `SkillAcidDemonstration::SkillAcidDemonstration`

来源：`src/map/skills/merchant/aciddemonstration.cpp:11-12`

```cpp
SkillAcidDemonstration::SkillAcidDemonstration() : WeaponSkillImpl(CR_ACIDDEMONSTRATION) {
}
```

#### `SkillAcidDemonstration::calculateSkillRatio`

来源：`src/map/skills/merchant/aciddemonstration.cpp:14-23`

```cpp
void SkillAcidDemonstration::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const status_data* sstatus = status_get_status_data(*src);
	const status_data* tstatus = status_get_status_data(*target);

	base_skillratio += -100 + 200 * skill_lv + sstatus->int_ + tstatus->vit; // !TODO: Confirm status bonus
	if (target->type == BL_PC)
		base_skillratio /= 2;
#endif
}
```

#### `SkillAcidDemonstration::castendDamageId`

来源：`src/map/skills/merchant/aciddemonstration.cpp:25-31`

```cpp
void SkillAcidDemonstration::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, flag);
#else
	skill_attack(skill_get_type(getSkillId()),src,src,target,getSkillId(),skill_lv,tick,flag);
#endif
}
```

#### `SkillAcidDemonstration::applyAdditionalEffects`

来源：`src/map/skills/merchant/aciddemonstration.cpp:33-35`

```cpp
void SkillAcidDemonstration::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	skill_break_equip(src,target, EQP_WEAPON|EQP_ARMOR, 100*skill_lv, BCT_ENEMY);
}
```

### Plant Cultivation (`CR_CULTIVATION`)

非伤害技能；目标：地面区域；最高等级 2；射程：1；命中类型：Single；段数：1；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP 10；道具 Mushroom_Spore×1, Stem×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillPlantCultivation`
- 实现文件：`src/map/skills/merchant/plantcultivation.cpp`

#### `SkillPlantCultivation::SkillPlantCultivation`

来源：`src/map/skills/merchant/plantcultivation.cpp:10-11`

```cpp
SkillPlantCultivation::SkillPlantCultivation() : SkillImpl(CR_CULTIVATION) {
}
```

#### `SkillPlantCultivation::castendPos2`

来源：`src/map/skills/merchant/plantcultivation.cpp:13-61`

```cpp
void SkillPlantCultivation::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	if (sd) {
		if( map_count_oncell(src->m,x,y,BL_CHAR,0) > 0 )
		{
			clif_skill_fail( *sd, getSkillId() );
			flag |= SKILL_NOCONSUME_REQ;
			return;
		}
		clif_skill_poseffect( *src, getSkillId(), skill_lv, x, y, tick );
		if (rnd()%100 < 50) {
			clif_skill_fail( *sd, getSkillId() );
		} else {
			TBL_MOB* md = nullptr;
			int32 t, mob_id;

			if (skill_lv == 1)
				mob_id = MOBID_BLACK_MUSHROOM + rnd() % 2;
			else {
				int32 rand_val = rnd() % 100;

				if (rand_val < 30)
					mob_id = MOBID_GREEN_PLANT;
				else if (rand_val < 55)
					mob_id = MOBID_RED_PLANT;
				else if (rand_val < 80)
					mob_id = MOBID_YELLOW_PLANT;
				else if (rand_val < 90)
					mob_id = MOBID_WHITE_PLANT;
				else if (rand_val < 98)
					mob_id = MOBID_BLUE_PLANT;
				else
					mob_id = MOBID_SHINING_PLANT;
			}

			md = mob_once_spawn_sub(src, src->m, x, y, "--ja--", mob_id, "", SZ_SMALL, AI_NONE);
			if (!md)
				return;
			if ((t = skill_get_time(getSkillId(), skill_lv)) > 0)
			{
				if( md->deletetimer != INVALID_TIMER )
					delete_timer(md->deletetimer, mob_timer_delete);
				md->deletetimer = add_timer (tick + t, mob_timer_delete, md->id, 0);
			}
			mob_spawn(md);
		}
	}
}
```
