# High_Wizard 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 364 | `HW_SOULDRAIN` / Soul Drain | `core-source-references` | `` | src/map/skill.cpp, src/map/status.cpp |
| 365 | `HW_MAGICCRASHER` / Stave Crasher | `generic-or-class-mapped` | `WeaponSkillImpl` |  |
| 366 | `HW_MAGICPOWER` / Mystical Amplification | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 400 | `HW_NAPALMVULCAN` / Napalm Vulcan | `exact-class-methods` | `SkillNapalmVulcan` | src/map/skills/mage/napalmvulcan.cpp |
| 483 | `HW_GANBANTEIN` / Ganbantein | `exact-class-methods` | `SkillGanbantein` | src/map/skills/mage/ganbantein.cpp |
| 484 | `HW_GRAVITATION` / Gravitation Field | `exact-class-methods` | `SkillGravitationField` | src/map/skills/mage/gravitationfield.cpp |

## 详细公式与效果实现

### Soul Drain (`HW_SOULDRAIN`)

魔法技能；目标：被动；最高等级 10；段数：1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:1746
if (rnd_chance(battle_config.sg_miracle_skill_ratio, 20000) && rnd_chance(46, (int32)sd->battle_status.agi))
// src/map/skill.cpp:1747
sc_start(src, src, SC_MIRACLE, 100, 1, battle_config.sg_miracle_skill_duration);
// src/map/skill.cpp:1752
(rate=pc_checkskill(sd,HW_SOULDRAIN))>0
// src/map/skill.cpp:1755
clif_skill_nodamage(src,*bl,HW_SOULDRAIN,rate);
// src/map/skill.cpp:1756
status_heal(src, 0, status_get_lv(bl)*(95+15*rate)/100, 2);
// src/map/skill.cpp:1760
int32 sp = 0, hp = 0;
// src/map/skill.cpp:1762
sp += sd->bonus.sp_gain_value;
// src/map/skill.cpp:1763
sp += sd->indexed_bonus.sp_gain_race[status_get_race(bl)] + sd->indexed_bonus.sp_gain_race[RC_ALL];
// src/map/skill.cpp:1764
hp += sd->bonus.hp_gain_value;
// src/map/skill.cpp:1767
sp += sd->bonus.long_sp_gain_value;
// src/map/status.cpp:3345
} else if (type == STATUS_BONUS_RATE) {
// src/map/status.cpp:3346
status_change *sc = status_get_sc(bl);
// src/map/status.cpp:3360
if (sc->getSCE(SC_NIBELUNGEN) && sc->getSCE(SC_NIBELUNGEN)->val2 == RINGNBL_SPRATE)
```

### Stave Crasher (`HW_MAGICCRASHER`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Multi_Hit；段数：1；属性：Weapon；吟唱：300 ms；技能后摇：300 ms；消耗/限制：SP 8。

- 覆盖：`generic-or-class-mapped`
- 实现类：`WeaponSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:3698
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3700
wd->damage2 = battle_attr_fix(src, target, wd->damage2, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:4138
if (is_attack_critical(wd, src, target, skill_id, skill_lv, false)) bflag |= BDMG_CRIT;
// src/map/battle.cpp:4142
battle_calc_damage_parts(wd, src, target, skill_id, skill_lv);
// src/map/battle.cpp:4144
wd->damage = battle_calc_base_damage(src, sstatus, &sstatus->rhw, sc, tstatus->size, bflag);
// src/map/battle.cpp:4146
wd->damage2 = battle_calc_base_damage(src, sstatus, &sstatus->lhw, sc, tstatus->size, bflag);
// src/map/battle.cpp:5461
battle_calc_skill_base_damage(&wd, src, target, skill_id, skill_lv); // base skill damage
// src/map/battle.cpp:5465
ATK_RATE(wd.damage, wd.damage2, battle_calc_attack_skill_ratio(&wd, src, target, skill_id, skill_lv));
// src/map/battle.cpp:5468
ATK_ADD(wd.damage, wd.damage2, battle_calc_skill_constant_addition(&wd, src, target, skill_id, skill_lv));
// src/map/battle.cpp:5472
if(skill_id == HW_MAGICCRASHER) { // Add weapon attack for MATK onto Magic Crasher
// src/map/battle.cpp:5475
if (sstatus->matk_max > sstatus->matk_min) {
// src/map/battle.cpp:5476
ATK_ADD(wd.weaponAtk, wd.weaponAtk2, sstatus->matk_min+rnd()%(sstatus->matk_max-sstatus->matk_min));
// src/map/battle.cpp:5478
ATK_ADD(wd.weaponAtk, wd.weaponAtk2, sstatus->matk_min);
```

### Mystical Amplification (`HW_MAGICPOWER`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；吟唱：700 ms；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=14; Lv2=18; Lv3=22; Lv4=26; Lv5=30; Lv6=34; Lv7=38; Lv8=42; Lv9=46; Lv10=50；关联状态：MagicPower。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:10357
fixcast_r = max(fixcast_r, skill_lv * 6);
// src/map/skill.cpp:10366
fixed += skill_lv * 500;
// src/map/skill.cpp:10368
if (sc && sc->getSCE(SC_SECRAMENT) && skill_id == HW_MAGICPOWER && (flag&2)) // Sacrament lowers Mystical Amplification cast time
// src/map/skill.cpp:10369
fixcast_r = max(fixcast_r, sc->getSCE(SC_SECRAMENT)->val2);
// src/map/skill.cpp:10371
if (varcast_r < 0)
// src/map/skill.cpp:10372
time = time * (1 - (float)min(varcast_r, 100) / 100);
// src/map/skill.cpp:10376
time = time * (1 - sqrt(((float)(status_get_dex(bl) * 2 + status_get_int(bl)) / battle_config.vcast_stat_scale)));
// src/map/skill.cpp:10378
time = time * (1 - (float)min(reduce_cast_rate, 100) / 100);
// src/map/skill.cpp:10379
time = max((int32)time, 0) + (1 - (float)min(fixcast_r, 100) / 100) * max(fixed, 0); //Underflow checking/capping
```

### Napalm Vulcan (`HW_NAPALMVULCAN`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；属性：Ghost；范围：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间2：30000 ms；伤害标记：Splash, SplashSplit；消耗/限制：SP Lv1=10; Lv2=25; Lv3=40; Lv4=55; Lv5=70；关联状态：Curse。

- 覆盖：`exact-class-methods`
- 实现类：`SkillNapalmVulcan`
- 实现文件：`src/map/skills/mage/napalmvulcan.cpp`

#### `SkillNapalmVulcan::SkillNapalmVulcan`

来源：`src/map/skills/mage/napalmvulcan.cpp:10-11`

```cpp
SkillNapalmVulcan::SkillNapalmVulcan() : SkillImplRecursiveDamageSplash(HW_NAPALMVULCAN) {
}
```

#### `SkillNapalmVulcan::calculateSkillRatio`

来源：`src/map/skills/mage/napalmvulcan.cpp:13-20`

```cpp
void SkillNapalmVulcan::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
#ifdef RENEWAL
	skillratio += -100 + 70 * skill_lv;
	RE_LVL_DMOD(100);
#else
	skillratio += 25;
#endif
}
```

#### `SkillNapalmVulcan::applyAdditionalEffects`

来源：`src/map/skills/mage/napalmvulcan.cpp:22-24`

```cpp
void SkillNapalmVulcan::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src,target,SC_CURSE,5*skill_lv,skill_lv,skill_get_time2(getSkillId(),skill_lv));
}
```

### Ganbantein (`HW_GANBANTEIN`)

非伤害技能；目标：地面区域；最高等级 1；射程：18；命中类型：Single；段数：1；范围：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；吟唱：3000 ms；技能后摇：5000 ms；伤害标记：NoDamage；消耗/限制：SP 40；道具 Yellow_Gemstone×1, Blue_Gemstone×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillGanbantein`
- 实现文件：`src/map/skills/mage/ganbantein.cpp`

#### `SkillGanbantein::SkillGanbantein`

来源：`src/map/skills/mage/ganbantein.cpp:9-10`

```cpp
SkillGanbantein::SkillGanbantein() : SkillImpl(HW_GANBANTEIN) {
}
```

#### `SkillGanbantein::castendPos2`

来源：`src/map/skills/mage/ganbantein.cpp:12-26`

```cpp
void SkillGanbantein::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	if (rnd()%100 < 80) {
		int32 dummy = 1;
		clif_skill_poseffect( *src, getSkillId(), skill_lv, x, y, tick );
		bool i = skill_get_splash(getSkillId(), skill_lv);
		map_foreachinallarea(skill_cell_overlap, src->m, x-i, y-i, x+i, y+i, BL_SKILL, getSkillId(), &dummy, src);
	} else {
		if (sd) clif_skill_fail( *sd, getSkillId() );
	
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}
}
```

### Gravitation Field (`HW_GRAVITATION`)

特殊技能；目标：地面区域；最高等级 5；射程：18；命中类型：Single；段数：1；属性：Earth；吟唱：5000 ms；技能后摇：Lv1=5000; Lv2=6000; Lv3=7000; Lv4=8000; Lv5=9000 ms；持续时间1：Lv1=5000; Lv2=6000; Lv3=7000; Lv4=8000; Lv5=9000 ms；伤害标记：NoDamage, IgnoreElement, IgnoreFlee, IgnoreDefCard；消耗/限制：SP Lv1=20; Lv2=40; Lv3=60; Lv4=80; Lv5=100；道具 Blue_Gemstone×1；关联状态：Gravitation。

- 覆盖：`exact-class-methods`
- 实现类：`SkillGravitationField`
- 实现文件：`src/map/skills/mage/gravitationfield.cpp`

#### `SkillGravitationField::SkillGravitationField`

来源：`src/map/skills/mage/gravitationfield.cpp:10-11`

```cpp
SkillGravitationField::SkillGravitationField() : SkillImpl(HW_GRAVITATION) {
}
```

#### `SkillGravitationField::calculateSkillRatio`

来源：`src/map/skills/mage/gravitationfield.cpp:13-18`

```cpp
void SkillGravitationField::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
#ifdef RENEWAL
	skillratio += -100 + 100 * skill_lv;
	RE_LVL_DMOD(100);
#endif
}
```

#### `SkillGravitationField::castendPos2`

来源：`src/map/skills/mage/gravitationfield.cpp:20-32`

```cpp
void SkillGravitationField::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#else
	std::shared_ptr<s_skill_unit_group> sg;
	sc_type type = skill_get_sc(getSkillId());

	if ((sg = skill_unitsetting(src,getSkillId(),skill_lv,x,y,0)))
		sc_start4(src,src,type,100,skill_lv,0,BCT_SELF,sg->group_id,skill_get_time(getSkillId(),skill_lv));
	flag|=1;
#endif
}
```

#### `SkillGravitationField::applyAdditionalEffects`

来源：`src/map/skills/mage/gravitationfield.cpp:34-40`

```cpp
void SkillGravitationField::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
#ifndef RENEWAL
	// Gravitation can trigger physical autospells
	attack_type |= BF_NORMAL;
	attack_type |= BF_WEAPON;
#endif
}
```
