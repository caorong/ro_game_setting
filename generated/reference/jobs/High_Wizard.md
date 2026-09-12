# High_Wizard 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `High_Wizard` 公式页](../skill-formulas/High_Wizard.md)

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 9 | `MG_SRECOVERY` | Increase SP Recovery | 10 | Mage | 否 | — | None / Passive |
| 10 | `MG_SIGHT` | Sight | 1 | Mage | 否 | — | Magic / Self |
| 11 | `MG_NAPALMBEAT` | Napalm Beat | 10 | Mage | 否 | — | Magic / Attack |
| 12 | `MG_SAFETYWALL` | Safety Wall | 10 | Mage | 否 | MG_NAPALMBEAT Lv7, MG_SOULSTRIKE Lv5 | Magic / Ground |
| 13 | `MG_SOULSTRIKE` | Soul Strike | 10 | Mage | 否 | MG_NAPALMBEAT Lv4 | Magic / Attack |
| 14 | `MG_COLDBOLT` | Cold Bolt | 10 | Mage | 否 | — | Magic / Attack |
| 15 | `MG_FROSTDIVER` | Frost Diver | 10 | Mage | 否 | MG_COLDBOLT Lv5 | Magic / Attack |
| 16 | `MG_STONECURSE` | Stone Curse | 10 | Mage | 否 | — | Magic / Attack |
| 17 | `MG_FIREBALL` | Fire Ball | 10 | Mage | 否 | MG_FIREBOLT Lv4 | Magic / Attack |
| 18 | `MG_FIREWALL` | Fire Wall | 10 | Mage | 否 | MG_FIREBALL Lv5, MG_SIGHT Lv1 | Magic / Ground |
| 19 | `MG_FIREBOLT` | Fire Bolt | 10 | Mage | 否 | — | Magic / Attack |
| 20 | `MG_LIGHTNINGBOLT` | Lightning Bolt | 10 | Mage | 否 | — | Magic / Attack |
| 21 | `MG_THUNDERSTORM` | Thunderstorm | 10 | Mage | 否 | MG_LIGHTNINGBOLT Lv4 | Magic / Ground |
| 157 | `MG_ENERGYCOAT` | Energy Coat | 1 | Mage | 否 | — | Magic / Self |
| 80 | `WZ_FIREPILLAR` | Fire Pillar | 10 | Wizard | 否 | MG_FIREWALL Lv1 | Magic / Ground |
| 81 | `WZ_SIGHTRASHER` | Sightrasher | 10 | Wizard | 否 | MG_LIGHTNINGBOLT Lv1, MG_SIGHT Lv1 | Magic / Self |
| 83 | `WZ_METEOR` | Meteor Storm | 10 | Wizard | 否 | WZ_SIGHTRASHER Lv2, MG_THUNDERSTORM Lv1 | Magic / Ground |
| 84 | `WZ_JUPITEL` | Jupitel Thunder | 10 | Wizard | 否 | MG_NAPALMBEAT Lv1, MG_LIGHTNINGBOLT Lv1 | Magic / Attack |
| 85 | `WZ_VERMILION` | Lord of Vermilion | 10 | Wizard | 否 | MG_THUNDERSTORM Lv1, WZ_JUPITEL Lv5 | Magic / Ground |
| 86 | `WZ_WATERBALL` | Water Ball | 5 | Wizard | 否 | MG_COLDBOLT Lv1, MG_LIGHTNINGBOLT Lv1 | Magic / Attack |
| 87 | `WZ_ICEWALL` | Ice Wall | 10 | Wizard | 否 | MG_STONECURSE Lv1, MG_FROSTDIVER Lv1 | Magic / Ground |
| 88 | `WZ_FROSTNOVA` | Frost Nova | 10 | Wizard | 否 | WZ_ICEWALL Lv1 | Magic / Self |
| 89 | `WZ_STORMGUST` | Storm Gust | 10 | Wizard | 否 | MG_FROSTDIVER Lv1, WZ_JUPITEL Lv3 | Magic / Ground |
| 90 | `WZ_EARTHSPIKE` | Earth Spike | 5 | Wizard | 否 | MG_STONECURSE Lv1 | Magic / Attack |
| 91 | `WZ_HEAVENDRIVE` | Heaven's Drive | 5 | Wizard | 否 | WZ_EARTHSPIKE Lv3 | Magic / Ground |
| 92 | `WZ_QUAGMIRE` | Quagmire | 5 | Wizard | 否 | WZ_HEAVENDRIVE Lv1 | Magic / Ground |
| 93 | `WZ_ESTIMATION` | Sense | 1 | Wizard | 否 | — | Magic / Attack |
| 1006 | `WZ_SIGHTBLASTER` | Sight Blaster | 1 | Wizard | 否 | — | Magic / Self |
| 364 | `HW_SOULDRAIN` | Soul Drain | 10 | High_Wizard | 是 | MG_SRECOVERY Lv5, MG_SOULSTRIKE Lv7 | Magic / Passive |
| 365 | `HW_MAGICCRASHER` | Stave Crasher | 1 | High_Wizard | 是 | MG_SRECOVERY Lv1 | Weapon / Attack |
| 366 | `HW_MAGICPOWER` | Mystical Amplification | 10 | High_Wizard | 是 | — | Magic / Self |
| 400 | `HW_NAPALMVULCAN` | Napalm Vulcan | 5 | High_Wizard | 是 | MG_NAPALMBEAT Lv5 | Magic / Attack |
| 483 | `HW_GANBANTEIN` | Ganbantein | 1 | High_Wizard | 是 | WZ_ESTIMATION Lv1, WZ_ICEWALL Lv1 | None / Ground |
| 484 | `HW_GRAVITATION` | Gravitation Field | 5 | High_Wizard | 是 | HW_MAGICCRASHER Lv1, HW_MAGICPOWER Lv10, WZ_QUAGMIRE Lv1 | Misc / Ground |

## 技能详情

### Soul Drain (`HW_SOULDRAIN`)

魔法技能；目标：被动；最高等级 10；段数：1。

- 技能树最高等级：`10`
- 前置技能：MG_SRECOVERY Lv5, MG_SOULSTRIKE Lv7
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

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
```

### Stave Crasher (`HW_MAGICCRASHER`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Multi_Hit；段数：1；属性：Weapon；吟唱：300 ms；技能后摇：300 ms；消耗/限制：SP 8。

- 技能树最高等级：`1`
- 前置技能：MG_SRECOVERY Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

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
```

### Mystical Amplification (`HW_MAGICPOWER`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；吟唱：700 ms；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=14; Lv2=18; Lv3=22; Lv4=26; Lv5=30; Lv6=34; Lv7=38; Lv8=42; Lv9=46; Lv10=50；关联状态：MagicPower。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

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

- 技能树最高等级：`5`
- 前置技能：MG_NAPALMBEAT Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/mage/napalmvulcan.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/napalmvulcan.cpp:10
SkillNapalmVulcan::SkillNapalmVulcan() : SkillImplRecursiveDamageSplash(HW_NAPALMVULCAN) {
// src/map/skills/mage/napalmvulcan.cpp:13
void SkillNapalmVulcan::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
// src/map/skills/mage/napalmvulcan.cpp:15
skillratio += -100 + 70 * skill_lv;
// src/map/skills/mage/napalmvulcan.cpp:18
skillratio += 25;
// src/map/skills/mage/napalmvulcan.cpp:22
void SkillNapalmVulcan::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
```

### Ganbantein (`HW_GANBANTEIN`)

非伤害技能；目标：地面区域；最高等级 1；射程：18；命中类型：Single；段数：1；范围：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；吟唱：3000 ms；技能后摇：5000 ms；伤害标记：NoDamage；消耗/限制：SP 40；道具 Yellow_Gemstone×1, Blue_Gemstone×1。

- 技能树最高等级：`1`
- 前置技能：WZ_ESTIMATION Lv1, WZ_ICEWALL Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/ganbantein.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5420
sd = BL_CAST(BL_PC, src);
// src/map/skill.cpp:5440
clif_skill_nodamage(src,*src,skill_id,skill_lv);
// src/map/skill.cpp:5442
clif_skill_poseffect( *src, skill_id, skill_lv, x, y, tick );
// src/map/skill.cpp:9692
status_change *sc = &sd->sc;
// src/map/skill.cpp:9938
req.itemid[0] = skill->require.itemid[skill_lv - 1];
// src/map/skill.cpp:9939
req.amount[0] = skill->require.amount[skill_lv - 1];
// src/map/skill.cpp:9949
{	// All gem skills except Hocus Pocus and Ganbantein can cast for free with Mistress card -helvetica
// src/map/skills/mage/ganbantein.cpp:12
void SkillGanbantein::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/ganbantein.cpp:13
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/ganbantein.cpp:17
clif_skill_poseffect( *src, getSkillId(), skill_lv, x, y, tick );
// src/map/skills/mage/ganbantein.cpp:18
bool i = skill_get_splash(getSkillId(), skill_lv);
```

### Gravitation Field (`HW_GRAVITATION`)

特殊技能；目标：地面区域；最高等级 5；射程：18；命中类型：Single；段数：1；属性：Earth；吟唱：5000 ms；技能后摇：Lv1=5000; Lv2=6000; Lv3=7000; Lv4=8000; Lv5=9000 ms；持续时间1：Lv1=5000; Lv2=6000; Lv3=7000; Lv4=8000; Lv5=9000 ms；伤害标记：NoDamage, IgnoreElement, IgnoreFlee, IgnoreDefCard；消耗/限制：SP Lv1=20; Lv2=40; Lv3=60; Lv4=80; Lv5=100；道具 Blue_Gemstone×1；关联状态：Gravitation。

- 技能树最高等级：`5`
- 前置技能：HW_MAGICCRASHER Lv1, HW_MAGICPOWER Lv10, WZ_QUAGMIRE Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/mage/gravitationfield.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1692
damage -= damage * sd->special_state.no_magic_damage / 100;
// src/map/battle.cpp:1694
if(flag&BF_MISC && sd->special_state.no_misc_damage)
// src/map/battle.cpp:1695
damage -= damage * sd->special_state.no_misc_damage / 100;
// src/map/battle.cpp:1697
if(!damage)
// src/map/battle.cpp:1709
damage = battle_calc_pk_damage(*src, *bl, damage, skill_id, flag);
// src/map/battle.cpp:1711
return damage; //These skills bypass everything else.
// src/map/battle.cpp:1714
status_change* tsc = status_get_sc(bl); //check target status
// src/map/battle.cpp:6407
md.damage = 3;
// src/map/battle.cpp:6410
md.damage = skill_calc_heal(src,target,skill_id,skill_lv,false);
// src/map/battle.cpp:6414
md.damage = 500 + rnd()%500 + 5 * skill_lv * sstatus->int_;
// src/map/battle.cpp:6415
nk.set(NK_IGNOREFLEE);
// src/map/battle.cpp:6419
md.damage = 200 + 200 * skill_lv;
```
