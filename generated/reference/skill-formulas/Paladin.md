# Paladin 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 367 | `PA_PRESSURE` / Gloria Domini | `exact-class-methods` | `SkillGloriaDomini` | src/map/skills/swordman/gloriadomini.cpp |
| 368 | `PA_SACRIFICE` / Martyr's Reckoning | `exact-class-methods` | `SkillMartyrsReckoning` | src/map/skills/swordman/martyrsreckoning.cpp |
| 369 | `PA_GOSPEL` / Battle Chant | `exact-class-methods` | `SkillBattleChant` | src/map/skills/swordman/battlechant.cpp |
| 480 | `PA_SHIELDCHAIN` / Shield Chain | `exact-class-methods` | `SkillShieldChain` | src/map/skills/swordman/shieldchain.cpp |

## 详细公式与效果实现

### Gloria Domini (`PA_PRESSURE`)

特殊技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：1；吟唱：Lv1=2000; Lv2=2500; Lv3=3000; Lv4=3500; Lv5=4000 ms；技能后摇：Lv1=2000; Lv2=2500; Lv3=3000; Lv4=3500; Lv5=4000 ms；持续时间2：Lv1=2000; Lv2=3000; Lv3=4000; Lv4=5000; Lv5=6000 ms；伤害标记：IgnoreElement, IgnoreFlee, IgnoreDefCard；消耗/限制：SP Lv1=30; Lv2=35; Lv3=40; Lv4=45; Lv5=50。

- 覆盖：`exact-class-methods`
- 实现类：`SkillGloriaDomini`
- 实现文件：`src/map/skills/swordman/gloriadomini.cpp`

#### `SkillGloriaDomini::SkillGloriaDomini`

来源：`src/map/skills/swordman/gloriadomini.cpp:10-11`

```cpp
SkillGloriaDomini::SkillGloriaDomini() : SkillImpl(PA_PRESSURE) {
}
```

#### `SkillGloriaDomini::calculateSkillRatio`

来源：`src/map/skills/swordman/gloriadomini.cpp:13-18`

```cpp
void SkillGloriaDomini::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
#ifdef RENEWAL
	skillratio += -100 + 500 + 150 * skill_lv;
	RE_LVL_DMOD(100);
#endif
}
```

#### `SkillGloriaDomini::castendDamageId`

来源：`src/map/skills/swordman/gloriadomini.cpp:20-26`

```cpp
void SkillGloriaDomini::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_attack(BF_MAGIC,src,src,target,getSkillId(),skill_lv,tick,flag);
#else
	skill_attack(skill_get_type(getSkillId()),src,src,target,getSkillId(),skill_lv,tick,flag);
#endif
}
```

#### `SkillGloriaDomini::applyAdditionalEffects`

来源：`src/map/skills/swordman/gloriadomini.cpp:28-35`

```cpp
void SkillGloriaDomini::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
#ifndef RENEWAL
	status_percent_damage(src, target, 0, 15+5*skill_lv, false);
	//Pressure can trigger physical autospells
	attack_type |= BF_NORMAL;
	attack_type |= BF_WEAPON;
#endif
}
```

### Martyr's Reckoning (`PA_SACRIFICE`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；技能后摇：2000 ms；伤害标记：NoDamage, IgnoreDefense, IgnoreFlee；消耗/限制：SP 100；关联状态：Sacrifice。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMartyrsReckoning`
- 实现文件：`src/map/skills/swordman/martyrsreckoning.cpp`

#### `SkillMartyrsReckoning::SkillMartyrsReckoning`

来源：`src/map/skills/swordman/martyrsreckoning.cpp:9-10`

```cpp
SkillMartyrsReckoning::SkillMartyrsReckoning() : WeaponSkillImpl(PA_SACRIFICE) {
}
```

#### `SkillMartyrsReckoning::calculateSkillRatio`

来源：`src/map/skills/swordman/martyrsreckoning.cpp:12-14`

```cpp
void SkillMartyrsReckoning::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += -10 + 10 * skill_lv;
}
```

#### `SkillMartyrsReckoning::castendNoDamageId`

来源：`src/map/skills/swordman/martyrsreckoning.cpp:16-21`

```cpp
void SkillMartyrsReckoning::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start(src,target,type,100,skill_lv,skill_get_time(getSkillId(),skill_lv)));
}
```

### Battle Chant (`PA_GOSPEL`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage, IgnoreFlee；消耗/限制：SP Lv1-5=80; Lv6-10=100；关联状态：Gospel。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBattleChant`
- 实现文件：`src/map/skills/swordman/battlechant.cpp`

#### `SkillBattleChant::SkillBattleChant`

来源：`src/map/skills/swordman/battlechant.cpp:9-10`

```cpp
SkillBattleChant::SkillBattleChant() : SkillImpl(PA_GOSPEL) {
}
```

#### `SkillBattleChant::castendPos2`

来源：`src/map/skills/swordman/battlechant.cpp:12-32`

```cpp
void SkillBattleChant::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	status_change* sc = status_get_sc(src);
	status_change_entry *sce = (sc && type != SC_NONE)?sc->getSCE(type):nullptr;

	if (sce && sce->val4 == BCT_SELF)
	{
		status_change_end(src, SC_GOSPEL);
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}
	else
	{
		std::shared_ptr<s_skill_unit_group> sg = skill_unitsetting(src,getSkillId(),skill_lv,src->x,src->y,0);
		if (!sg) return;
		if (sce)
			status_change_end(src, type); //Was under someone else's Gospel. [Skotlex]
		sc_start4(src,src,type,100,skill_lv,0,sg->group_id,BCT_SELF,skill_get_time(getSkillId(),skill_lv));
		clif_skill_poseffect( *src, getSkillId(), skill_lv, 0, 0, tick ); // PA_GOSPEL music packet
	}
}
```

### Shield Chain (`PA_SHIELDCHAIN`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：4；命中类型：Multi_Hit；段数：5；吟唱：1000 ms；技能后摇：1000 ms；消耗/限制：SP Lv1=28; Lv2=31; Lv3=34; Lv4=37; Lv5=40；状态 Shield。

- 覆盖：`exact-class-methods`
- 实现类：`SkillShieldChain`
- 实现文件：`src/map/skills/swordman/shieldchain.cpp`

#### `SkillShieldChain::SkillShieldChain`

来源：`src/map/skills/swordman/shieldchain.cpp:11-12`

```cpp
SkillShieldChain::SkillShieldChain() : WeaponSkillImpl(PA_SHIELDCHAIN) {
}
```

#### `SkillShieldChain::calculateSkillRatio`

来源：`src/map/skills/swordman/shieldchain.cpp:14-42`

```cpp
void SkillShieldChain::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
	const status_change *sc = status_get_sc(src);

#ifdef RENEWAL
	const map_session_data* sd = BL_CAST( BL_PC, src );

	skillratio = -100 + 300 + 200 * skill_lv;

	if( sd != nullptr ){
		int16 index = sd->equip_index[EQI_HAND_L];

		// Damage affected by the shield's weight and refine.
		if( index >= 0 && sd->inventory_data[index] != nullptr && sd->inventory_data[index]->type == IT_ARMOR ){
			skillratio += sd->inventory_data[index]->weight / 10 + 4 * sd->inventory.u.items_inventory[index].refine;
		}

		// Damage affected by shield mastery
		if( sc != nullptr && sc->getSCE( SC_SHIELD_POWER ) ){
			skillratio += skill_lv * 14 * pc_checkskill( sd, IG_SHIELD_MASTERY );
		}
	}

	RE_LVL_DMOD(100);
#else
	skillratio += 30 * skill_lv;
#endif
	if (sc && sc->getSCE(SC_SHIELD_POWER))// Whats the official increase? [Rytech]
		skillratio += skillratio * 50 / 100;
}
```
