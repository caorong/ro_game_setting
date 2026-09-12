# Assassin_Cross 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 376 | `ASC_KATAR` / Advanced Katar Mastery | `core-source-references` | `` | src/map/battle.cpp |
| 378 | `ASC_EDP` / Enchant Deadly Poison | `exact-class-methods` | `SkillEnchantDeadlyPoison` | src/map/skills/thief/enchantdeadlypoison.cpp |
| 379 | `ASC_BREAKER` / Soul Destroyer | `exact-class-methods` | `SkillSoulDestroyer` | src/map/skills/thief/souldestroyer.cpp |
| 406 | `ASC_METEORASSAULT` / Meteor Assault | `exact-class-methods` | `SkillMeteorAssault` | src/map/skills/thief/meteorassault.cpp |
| 407 | `ASC_CDP` / Create Deadly Poison | `exact-class-methods` | `SkillCreateDeadlyPoison` | src/map/skills/thief/createdeadlypoison.cpp |

## 详细公式与效果实现

### Advanced Katar Mastery (`ASC_KATAR`)

武器/物理技能；目标：被动；最高等级 5；段数：1；伤害标记：NoDamage。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:1056
if( sd->status.weapon == W_KATAR && (skill = pc_checkskill(sd,ASC_KATAR)) > 0 ) // Adv. Katar Mastery functions similar to a +%ATK card on official [helvetica]
// src/map/battle.cpp:5567
ATK_RATE(wd.damage, wd.damage2, battle_calc_attack_skill_ratio(&wd, src, target, skill_id, skill_lv));
// src/map/battle.cpp:5570
ATK_ADD(wd.damage, wd.damage2, battle_calc_skill_constant_addition(&wd, src, target, skill_id, skill_lv));
// src/map/battle.cpp:5576
if (sd->status.weapon == W_KATAR && (katar_skill = pc_checkskill(sd, ASC_KATAR)) > 0) // Adv. Katar Mastery applied after calculate with skillratio.
// src/map/battle.cpp:5577
ATK_ADDRATE(wd.damage, wd.damage2, (10 + 2 * katar_skill));
// src/map/battle.cpp:5582
if ((wd.damage + wd.damage2) && tstatus->res > 0 && !nk[NK_SIMPLEDEFENSE]) {
```

### Enchant Deadly Poison (`ASC_EDP`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；属性：Poison；技能后摇：2000 ms；持续时间1：Lv1=40000; Lv2=45000; Lv3=50000; Lv4=55000; Lv5=60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=60; Lv2=70; Lv3=80; Lv4=90; Lv5=100；道具 Poison_Bottle×1；关联状态：Edp。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEnchantDeadlyPoison`
- 实现文件：`src/map/skills/thief/enchantdeadlypoison.cpp`

#### `SkillEnchantDeadlyPoison::SkillEnchantDeadlyPoison`

来源：`src/map/skills/thief/enchantdeadlypoison.cpp:10-11`

```cpp
SkillEnchantDeadlyPoison::SkillEnchantDeadlyPoison() : StatusSkillImpl(ASC_EDP) {
}
```

#### `SkillEnchantDeadlyPoison::castendNoDamageId`

来源：`src/map/skills/thief/enchantdeadlypoison.cpp:13-22`

```cpp
void SkillEnchantDeadlyPoison::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	// EDP also give +25% WATK poison pseudo element to user.
	StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);

#ifdef RENEWAL
	sc_start4(src, src, SC_SUB_WEAPONPROPERTY, 100, ELE_POISON, 25, getSkillId(), 0, skill_get_time(getSkillId(), skill_lv));
#else
	sc_start4(src, src, SC_WATK_ELEMENT, 100, ELE_POISON, 25, 0, 0, skill_get_time(getSkillId(), skill_lv));
#endif
}
```

### Soul Destroyer (`ASC_BREAKER`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Weapon；吟唱：700 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800; Lv6=2000; Lv7=2200; Lv8=2400; Lv9=2600; Lv10=2800 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP Lv1-5=20; Lv6-10=30。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSoulDestroyer`
- 实现文件：`src/map/skills/thief/souldestroyer.cpp`

#### `SkillSoulDestroyer::SkillSoulDestroyer`

来源：`src/map/skills/thief/souldestroyer.cpp:10-11`

```cpp
SkillSoulDestroyer::SkillSoulDestroyer() : WeaponSkillImpl(ASC_BREAKER) {
}
```

#### `SkillSoulDestroyer::calculateSkillRatio`

来源：`src/map/skills/thief/souldestroyer.cpp:13-23`

```cpp
void SkillSoulDestroyer::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
#ifdef RENEWAL
	const status_data* sstatus = status_get_status_data(*src);

	skillratio += -100 + 150 * skill_lv + sstatus->str + sstatus->int_; // !TODO: Confirm stat modifier
	RE_LVL_DMOD(100);
#else
	// Pre-Renewal: skill ratio for weapon part of damage [helvetica]
	skillratio += -100 + 100 * skill_lv;
#endif
}
```

### Meteor Assault (`ASC_METEORASSAULT`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；属性：Weapon；范围：2；吟唱：500 ms；技能后摇：500 ms；持续时间2：Lv1=30000; Lv2=5000; Lv3=120000 ms；伤害标记：Splash, IgnoreAtkCard；消耗/限制：SP Lv1=10; Lv2=12; Lv3=14; Lv4=16; Lv5=18; Lv6=20; Lv7=22; Lv8=24; Lv9=26; Lv10=28。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMeteorAssault`
- 实现文件：`src/map/skills/thief/meteorassault.cpp`

#### `SkillMeteorAssault::SkillMeteorAssault`

来源：`src/map/skills/thief/meteorassault.cpp:11-12`

```cpp
SkillMeteorAssault::SkillMeteorAssault() : SkillImplRecursiveDamageSplash(ASC_METEORASSAULT) {
}
```

#### `SkillMeteorAssault::calculateSkillRatio`

来源：`src/map/skills/thief/meteorassault.cpp:14-21`

```cpp
void SkillMeteorAssault::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
#ifdef RENEWAL
	skillratio += 100 + 120 * skill_lv;
	RE_LVL_DMOD(100);
#else
	skillratio += -60 + 40 * skill_lv;
#endif
}
```

#### `SkillMeteorAssault::castendNoDamageId`

来源：`src/map/skills/thief/meteorassault.cpp:23-26`

```cpp
void SkillMeteorAssault::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
	skill_castend_damage_id(src, target, getSkillId(), skill_lv, tick, flag);
}
```

#### `SkillMeteorAssault::applyAdditionalEffects`

来源：`src/map/skills/thief/meteorassault.cpp:28-40`

```cpp
void SkillMeteorAssault::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	//Any enemies hit by this skill will receive Stun, Darkness, or external bleeding status ailment with a 5%+5*skill_lv% chance.
	switch(rnd()%3) {
		case 0:
			sc_start(src,target,SC_BLIND,(5+skill_lv*5),skill_lv,skill_get_time2(getSkillId(),1));
			break;
		case 1:
			sc_start(src,target,SC_STUN,(5+skill_lv*5),skill_lv,skill_get_time2(getSkillId(),2));
			break;
		default:
			sc_start2(src,target,SC_BLEEDING,(5+skill_lv*5),skill_lv,src->id,skill_get_time2(getSkillId(),3));
	}
}
```

### Create Deadly Poison (`ASC_CDP`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；技能后摇：500 ms；伤害标记：NoDamage；消耗/限制：SP 50。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCreateDeadlyPoison`
- 实现文件：`src/map/skills/thief/createdeadlypoison.cpp`

#### `SkillCreateDeadlyPoison::SkillCreateDeadlyPoison`

来源：`src/map/skills/thief/createdeadlypoison.cpp:9-10`

```cpp
SkillCreateDeadlyPoison::SkillCreateDeadlyPoison() : SkillImpl(ASC_CDP) {
}
```

#### `SkillCreateDeadlyPoison::castendNoDamageId`

来源：`src/map/skills/thief/createdeadlypoison.cpp:12-21`

```cpp
void SkillCreateDeadlyPoison::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	if(sd) {
		if(skill_produce_mix(sd, getSkillId(), ITEMID_POISON_BOTTLE, 0, 0, 0, 1, -1)) //Produce a Poison Bottle.
			clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
		else
			clif_skill_fail( *sd, getSkillId(), USESKILL_FAIL_STUFF_INSUFFICIENT );
	}
}
```
