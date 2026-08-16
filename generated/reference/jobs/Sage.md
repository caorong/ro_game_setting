# Sage 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Sage` 公式页](../skill-formulas/Sage.md)

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
| 93 | `WZ_ESTIMATION` | Sense | 1 | Sage | 是 | — | Magic / Attack |
| 90 | `WZ_EARTHSPIKE` | Earth Spike | 5 | Sage | 是 | SA_SEISMICWEAPON Lv1 | Magic / Attack |
| 91 | `WZ_HEAVENDRIVE` | Heaven's Drive | 5 | Sage | 是 | WZ_EARTHSPIKE Lv1 | Magic / Ground |
| 274 | `SA_ADVANCEDBOOK` | Study | 10 | Sage | 是 | — | Weapon / Passive |
| 275 | `SA_CASTCANCEL` | Cast Cancel | 5 | Sage | 是 | SA_ADVANCEDBOOK Lv2 | Magic / Self |
| 276 | `SA_MAGICROD` | Magic Rod | 5 | Sage | 是 | SA_ADVANCEDBOOK Lv4 | Magic / Self |
| 277 | `SA_SPELLBREAKER` | Spell Breaker | 5 | Sage | 是 | SA_MAGICROD Lv1 | Magic / Attack |
| 278 | `SA_FREECAST` | Free Cast | 10 | Sage | 是 | SA_CASTCANCEL Lv1 | Magic / Passive |
| 279 | `SA_AUTOSPELL` | Hindsight | 10 | Sage | 是 | SA_FREECAST Lv4 | Magic / Self |
| 280 | `SA_FLAMELAUNCHER` | Endow Blaze | 5 | Sage | 是 | MG_FIREBOLT Lv1, SA_ADVANCEDBOOK Lv5 | Magic / Support |
| 281 | `SA_FROSTWEAPON` | Endow Tsunami | 5 | Sage | 是 | MG_COLDBOLT Lv1, SA_ADVANCEDBOOK Lv5 | Magic / Support |
| 282 | `SA_LIGHTNINGLOADER` | Endow Tornado | 5 | Sage | 是 | MG_LIGHTNINGBOLT Lv1, SA_ADVANCEDBOOK Lv5 | Magic / Support |
| 283 | `SA_SEISMICWEAPON` | Endow Quake | 5 | Sage | 是 | MG_STONECURSE Lv1, SA_ADVANCEDBOOK Lv5 | Magic / Support |
| 284 | `SA_DRAGONOLOGY` | Dragonology | 5 | Sage | 是 | SA_ADVANCEDBOOK Lv9 | Weapon / Passive |
| 285 | `SA_VOLCANO` | Volcano | 5 | Sage | 是 | SA_FLAMELAUNCHER Lv2 | Magic / Ground |
| 286 | `SA_DELUGE` | Deluge | 5 | Sage | 是 | SA_FROSTWEAPON Lv2 | Magic / Ground |
| 287 | `SA_VIOLENTGALE` | Whirlwind | 5 | Sage | 是 | SA_LIGHTNINGLOADER Lv2 | Magic / Ground |
| 288 | `SA_LANDPROTECTOR` | Magnetic Earth | 5 | Sage | 是 | SA_VOLCANO Lv3, SA_DELUGE Lv3, SA_VIOLENTGALE Lv3 | Magic / Ground |
| 289 | `SA_DISPELL` | Dispell | 5 | Sage | 是 | SA_SPELLBREAKER Lv3 | Magic / Attack |
| 290 | `SA_ABRACADABRA` | Hocus-pocus | 10 | Sage | 是 | SA_AUTOSPELL Lv5, SA_DISPELL Lv1, SA_LANDPROTECTOR Lv1 | Magic / Self |
| 1007 | `SA_CREATECON` | Create Elemental Converter | 1 | Sage | 是 | — | None / Self |
| 1008 | `SA_ELEMENTWATER` | Elemental Change Water | 1 | Sage | 是 | — | Magic / Attack |
| 1017 | `SA_ELEMENTGROUND` | Elemental Change Earth | 1 | Sage | 是 | — | Magic / Attack |
| 1018 | `SA_ELEMENTFIRE` | Elemental Change Fire | 1 | Sage | 是 | — | Magic / Attack |
| 1019 | `SA_ELEMENTWIND` | Elemental Change Wind | 1 | Sage | 是 | — | Magic / Attack |

## 技能详情

### Sense (`WZ_ESTIMATION`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 10。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/sense.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/sense.cpp:13
void SkillSense::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/sense.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/mage/sense.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/mage/sense.cpp:16
mob_data* dstmd = BL_CAST(BL_MOB, target);
```

### Earth Spike (`WZ_EARTHSPIKE`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；属性：Earth；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20。

- 技能树最高等级：`5`
- 前置技能：SA_SEISMICWEAPON Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/homunculus/homunculus_caprice.cpp`, `src/map/skills/mage/earthspike.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6217
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6222
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6227
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6232
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6238
ad.damage = battle_attr_fix(src, target, ad.damage, s_ele, tstatus->def_ele, tstatus->ele_lv);
// src/map/battle.cpp:6241
ad.damage += battle_calc_cardfix(BF_MAGIC, src, target, nk, s_ele, 0, ad.damage, 0, ad.flag);
// src/map/battle.cpp:7747
battle_autocast_elembuff_skill(sd, target, MG_FIREBOLT, tick, flag);
// src/map/battle.cpp:7749
battle_autocast_elembuff_skill(sd, target, MG_COLDBOLT, tick, flag);
// src/map/battle.cpp:7751
battle_autocast_elembuff_skill(sd, target, MG_LIGHTNINGBOLT, tick, flag);
// src/map/battle.cpp:7753
battle_autocast_elembuff_skill(sd, target, WZ_EARTHSPIKE, tick, flag);
// src/map/battle.cpp:7755
battle_autocast_elembuff_skill(sd, target, SO_POISON_BUSTER, tick, flag);
// src/map/battle.cpp:7757
if (wd.flag & BF_WEAPON && src != target && damage > 0) {
```

### Heaven's Drive (`WZ_HEAVENDRIVE`)

魔法技能；目标：地面区域；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；属性：Earth；吟唱：Lv1=1000; Lv2=2000; Lv3=3000; Lv4=4000; Lv5=5000 ms；技能后摇：1000 ms；持续时间1：100 ms；消耗/限制：SP Lv1=28; Lv2=32; Lv3=36; Lv4=40; Lv5=44。

- 技能树最高等级：`5`
- 前置技能：WZ_EARTHSPIKE Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/mage/heavensdrive.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6222
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6227
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6232
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6238
ad.damage = battle_attr_fix(src, target, ad.damage, s_ele, tstatus->def_ele, tstatus->ele_lv);
// src/map/battle.cpp:6241
ad.damage += battle_calc_cardfix(BF_MAGIC, src, target, nk, s_ele, 0, ad.damage, 0, ad.flag);
// src/map/skills/mage/heavensdrive.cpp:13
void SkillHeavensDrive::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/heavensdrive.cpp:17
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/heavensdrive.cpp:20
void SkillHeavensDrive::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/mage/heavensdrive.cpp:22
base_skillratio += 25;
```

### Study (`SA_ADVANCEDBOOK`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

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
```

### Cast Cancel (`SA_CASTCANCEL`)

魔法技能；目标：自身；最高等级 5；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 2。

- 技能树最高等级：`5`
- 前置技能：SA_ADVANCEDBOOK Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/castcancel.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:4876
sd = BL_CAST(BL_PC,  src);
// src/map/skill.cpp:4877
md = BL_CAST(BL_MOB, src);
// src/map/skill.cpp:4878
status_change *sc = status_get_sc(src);
// src/map/skill.cpp:4885
if(ud->skill_id != SA_CASTCANCEL && ud->skill_id != SO_SPELLFIST) {// otherwise handled in unit_skillcastcancel()
// src/map/skill.cpp:4887
ShowError("skill_castend_id: Timer mismatch %d!=%d!\n", ud->skilltimer, tid);
// src/map/skill.cpp:4892
if( sd && ud->skilltimer != INVALID_TIMER && (pc_checkskill(sd,SA_FREECAST) > 0 || ud->skill_id == LG_EXEEDBREAK) )
// src/map/skill.cpp:4895
status_calc_bl(sd, { SCB_SPEED, SCB_ASPD });
// src/map/skill.cpp:8370
if (map_foreachinmap(skill_graffitiremover,sd.m,BL_SKILL,0)) { // If a previous Graffiti exists skill fails to cast.
// src/map/skill.cpp:8381
case SA_CASTCANCEL:
// src/map/skill.cpp:8389
if( skill_lv < 3 && ((sd.type == BL_PC && battle_config.pc_cloak_check_type&1)
// src/map/skills/mage/castcancel.cpp:4
#include "castcancel.hpp"
// src/map/skills/mage/castcancel.cpp:11
SkillCastCancel::SkillCastCancel() : SkillImpl(SA_CASTCANCEL) {
```

### Magic Rod (`SA_MAGICROD`)

魔法技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：Lv1=400; Lv2=600; Lv3=800; Lv4=1000; Lv5=1200 ms；伤害标记：NoDamage；消耗/限制：SP 2；关联状态：MagicRod。

- 技能树最高等级：`5`
- 前置技能：SA_ADVANCEDBOOK Lv4
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/magicrod.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2856
if (dmg.damage > 0) {
// src/map/skill.cpp:2857
dmg.damage -= dmg.damage * i64min(100, reduce) / 100;
// src/map/skill.cpp:2858
dmg.damage = i64max(dmg.damage, dmg.div_);
// src/map/skill.cpp:2865
int32 sp = skill_get_sp(skill_id,skill_lv);
// src/map/skill.cpp:2867
clif_skill_nodamage(bl,*bl,SA_MAGICROD,skill_lv);
// src/map/skill.cpp:2869
dmg.damage = dmg.damage2 = 0;
// src/map/skill.cpp:2871
sp = sp * tsc->getSCE(SC_MAGICROD)->val2 / 100;
// src/map/skill.cpp:2872
if(skill_id == WZ_WATERBALL && skill_lv > 1)
// src/map/skill.cpp:2873
sp = sp/((skill_lv|1)*(skill_lv|1)); //Estimate SP cost of a single water-ball
// src/map/skill.cpp:2874
status_heal(bl, 0, sp, 2);
// src/map/skill.cpp:2876
if( (dmg.damage || dmg.damage2) && tsc && (tsc->getSCE(SC_HALLUCINATIONWALK) && rnd()%100 < tsc->getSCE(SC_HALLUCINATIONWALK)->val3 || tsc->getSCE(SC_NPC_HALLUCINATIONWALK) && rnd()%100 < tsc->getSCE(SC_NPC_HALLUCINATIONWALK)->val3) ) {
// src/map/skill.cpp:2877
dmg.damage = dmg.damage2 = 0;
```

### Spell Breaker (`SA_SPELLBREAKER`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：700 ms；伤害标记：NoDamage；消耗/限制：SP 10。

- 技能树最高等级：`5`
- 前置技能：SA_MAGICROD Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/mage/skill_factory_mage.cpp`, `src/map/skills/mage/spellbreaker.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/spellbreaker.cpp:15
void SkillSpellBreaker::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/spellbreaker.cpp:17
status_change *tsc = status_get_sc(target);
// src/map/skills/mage/spellbreaker.cpp:18
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/spellbreaker.cpp:19
map_session_data* dstsd = BL_CAST( BL_PC, target );
// src/map/skills/mage/spellbreaker.cpp:21
int32 sp;
// src/map/skills/mage/spellbreaker.cpp:24
sp = status_percent_damage(target, src, 0, -20, false);
```

### Free Cast (`SA_FREECAST`)

魔法技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：SA_CASTCANCEL Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

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
```

### Hindsight (`SA_AUTOSPELL`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；吟唱：3000 ms；持续时间1：Lv1=120000; Lv2=150000; Lv3=180000; Lv4=210000; Lv5=240000; Lv6=270000; Lv7=300000; Lv8=330000; Lv9=360000; Lv10=390000 ms；伤害标记：NoDamage；消耗/限制：SP 35；关联状态：AutoSpell。

- 技能树最高等级：`10`
- 前置技能：SA_FREECAST Lv4
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/hindsight.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:10742
if(skill_lv==8) maxlv=1;
// src/map/skill.cpp:10743
else if(skill_lv>=9) maxlv=2;
// src/map/skill.cpp:10751
sc_start4(sd,sd,SC_AUTOSPELL,100,skill_lv,skill_id,maxlv,0,
// src/map/skill.cpp:10752
skill_get_time(SA_AUTOSPELL,skill_lv));
// src/map/skills/mage/hindsight.cpp:13
void SkillHindsight::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/hindsight.cpp:15
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/hindsight.cpp:17
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/mage/hindsight.cpp:20
clif_autospell( *sd, skill_lv );
// src/map/skills/mage/hindsight.cpp:40
else if(skill_lv >=2) {
// src/map/skills/mage/hindsight.cpp:43
maxlv = skill_lv - 1;
// src/map/skills/mage/hindsight.cpp:45
else if(skill_lv > 0) {
// src/map/skills/mage/hindsight.cpp:51
sc_start4(src,src,SC_AUTOSPELL,100,skill_lv,spellid,maxlv,0,
```

### Endow Blaze (`SA_FLAMELAUNCHER`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Fire；吟唱：3000 ms；持续时间1：Lv1-4=1200000; Lv5=1800000 ms；伤害标记：NoDamage；消耗/限制：SP 40；道具 Boody_Red×1；关联状态：FireWeapon。

- 技能树最高等级：`5`
- 前置技能：MG_FIREBOLT Lv1, SA_ADVANCEDBOOK Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/endowblaze.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/endowblaze.cpp:15
void SkillEndowBlaze::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/endowblaze.cpp:17
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/endowblaze.cpp:18
map_session_data* dstsd = BL_CAST( BL_PC, target );
// src/map/skills/mage/endowblaze.cpp:23
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,false);
```

### Endow Tsunami (`SA_FROSTWEAPON`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Water；吟唱：3000 ms；持续时间1：Lv1-4=1200000; Lv5=1800000 ms；伤害标记：NoDamage；消耗/限制：SP 40；道具 Crystal_Blue×1；关联状态：WaterWeapon。

- 技能树最高等级：`5`
- 前置技能：MG_COLDBOLT Lv1, SA_ADVANCEDBOOK Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/diamonddust.cpp`, `src/map/skills/mage/endowtsunami.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/diamonddust.cpp:20
rate += (sd ? sd->status.job_level / 5 : 0);
// src/map/skills/mage/diamonddust.cpp:22
sc_start(src, target, SC_CRYSTALIZE, rate, skill_lv, skill_get_time2(getSkillId(), skill_lv));
// src/map/skills/mage/diamonddust.cpp:25
void SkillDiamondDust::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
// src/map/skills/mage/diamonddust.cpp:26
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/mage/diamonddust.cpp:27
const status_change* sc = status_get_sc(src);
// src/map/skills/mage/diamonddust.cpp:30
skillratio += -100 + 2 * sstatus->int_ + 300 * pc_checkskill(sd, SA_FROSTWEAPON) + sstatus->int_ * skill_lv;
// src/map/skills/mage/diamonddust.cpp:33
skillratio += (sd ? sd->status.job_level * 5 : 0);
// src/map/skills/mage/diamonddust.cpp:36
void SkillDiamondDust::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/diamonddust.cpp:38
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/endowtsunami.cpp:15
void SkillEndowTsunami::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/endowtsunami.cpp:17
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/endowtsunami.cpp:18
map_session_data* dstsd = BL_CAST( BL_PC, target );
```

### Endow Tornado (`SA_LIGHTNINGLOADER`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Wind；吟唱：3000 ms；持续时间1：Lv1-4=1200000; Lv5=1800000 ms；伤害标记：NoDamage；消耗/限制：SP 40；道具 Wind_Of_Verdure×1；关联状态：WindWeapon。

- 技能树最高等级：`5`
- 前置技能：MG_LIGHTNINGBOLT Lv1, SA_ADVANCEDBOOK Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/endowtornado.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/skills/mage/varetyrspear.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/endowtornado.cpp:15
void SkillEndowTornado::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/endowtornado.cpp:17
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/endowtornado.cpp:18
map_session_data* dstsd = BL_CAST( BL_PC, target );
// src/map/skills/mage/endowtornado.cpp:23
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,false);
// src/map/skills/mage/varetyrspear.cpp:11
SkillVaretyrSpear::SkillVaretyrSpear() : SkillImplRecursiveDamageSplash(SO_VARETYR_SPEAR) {
// src/map/skills/mage/varetyrspear.cpp:14
void SkillVaretyrSpear::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/mage/varetyrspear.cpp:15
sc_start(src,target, SC_STUN, 5 * skill_lv, skill_lv, skill_get_time(getSkillId(), skill_lv));
// src/map/skills/mage/varetyrspear.cpp:18
void SkillVaretyrSpear::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
// src/map/skills/mage/varetyrspear.cpp:20
const status_change *sc = status_get_sc(src);
// src/map/skills/mage/varetyrspear.cpp:21
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/mage/varetyrspear.cpp:23
skillratio += -100 + (2 * sstatus->int_ + 150 * (pc_checkskill(sd, SO_STRIKING) + pc_checkskill(sd, SA_LIGHTNINGLOADER)) + sstatus->int_ * skill_lv / 2) / 3;
// src/map/skills/mage/varetyrspear.cpp:26
skillratio += (sd ? sd->status.job_level * 5 : 0);
```

### Endow Quake (`SA_SEISMICWEAPON`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Earth；吟唱：3000 ms；持续时间1：Lv1-4=1200000; Lv5=1800000 ms；伤害标记：NoDamage；消耗/限制：SP 40；道具 Yellow_Live×1；关联状态：EarthWeapon。

- 技能树最高等级：`5`
- 前置技能：MG_STONECURSE Lv1, SA_ADVANCEDBOOK Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/earthgrave.cpp`, `src/map/skills/mage/endowquake.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/earthgrave.cpp:14
void SkillEarthGrave::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/mage/earthgrave.cpp:15
sc_start2(src, target, SC_BLEEDING, 5 * skill_lv, skill_lv, src->id, skill_get_time2(getSkillId(), skill_lv)); // Need official rate. [LimitLine]
// src/map/skills/mage/earthgrave.cpp:18
void SkillEarthGrave::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
// src/map/skills/mage/earthgrave.cpp:19
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/mage/earthgrave.cpp:20
const status_change* sc = status_get_sc(src);
// src/map/skills/mage/earthgrave.cpp:23
skillratio += -100 + 2 * sstatus->int_ + 300 * pc_checkskill(sd, SA_SEISMICWEAPON) + sstatus->int_ * skill_lv;
// src/map/skills/mage/earthgrave.cpp:26
skillratio += (sd ? sd->status.job_level * 5 : 0);
// src/map/skills/mage/earthgrave.cpp:29
void SkillEarthGrave::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/earthgrave.cpp:31
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/endowquake.cpp:15
void SkillEndowQuake::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/endowquake.cpp:17
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/endowquake.cpp:18
map_session_data* dstsd = BL_CAST( BL_PC, target );
```

### Dragonology (`SA_DRAGONOLOGY`)

武器/物理技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：SA_ADVANCEDBOOK Lv9
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

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

- 技能树最高等级：`5`
- 前置技能：SA_FLAMELAUNCHER Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/deluge.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/skills/mage/volcano.cpp`, `src/map/skills/mage/whirlwind.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5872
struct s_skill_condition req = skill_get_requirement(sd,skill_id,skill_lv);
// src/map/skill.cpp:5903
limit = skill_get_time(skill_id,skill_lv);
// src/map/skill.cpp:7718
status_change_end(bl, SC_DANCING);
// src/map/skills/mage/deluge.cpp:9
void SkillDeluge::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/deluge.cpp:16
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/deluge.cpp:23
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/volcano.cpp:9
void SkillVolcano::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/volcano.cpp:16
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/volcano.cpp:23
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/whirlwind.cpp:9
void SkillWhirlwind::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/whirlwind.cpp:16
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/whirlwind.cpp:23
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Deluge (`SA_DELUGE`)

魔法技能；目标：地面区域；最高等级 5；射程：2；命中类型：Single；段数：1；属性：Water；吟唱：5000 ms；持续时间1：Lv1=60000; Lv2=120000; Lv3=180000; Lv4=240000; Lv5=300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=48; Lv2=46; Lv3=44; Lv4=42; Lv5=40；道具 Yellow_Gemstone×1；关联状态：Deluge。

- 技能树最高等级：`5`
- 前置技能：SA_FROSTWEAPON Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/deluge.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/skills/mage/volcano.cpp`, `src/map/skills/mage/whirlwind.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5903
limit = skill_get_time(skill_id,skill_lv);
// src/map/skill.cpp:6252
unit_val1 = (skill_get_time(skill_id, skill_lv) / interval); //Default: 950/300 = 3 hits
// src/map/skill.cpp:6255
unit_val1 = 200 + 200*skill_lv;
// src/map/skill.cpp:7718
status_change_end(bl, SC_DANCING);
// src/map/skills/mage/deluge.cpp:9
void SkillDeluge::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/deluge.cpp:16
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/deluge.cpp:23
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/skill_factory_mage.cpp:305
case SA_CASTCANCEL:
// src/map/skills/mage/skill_factory_mage.cpp:306
return std::make_unique<SkillCastCancel>();
// src/map/skills/mage/volcano.cpp:9
void SkillVolcano::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/volcano.cpp:16
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/volcano.cpp:23
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Whirlwind (`SA_VIOLENTGALE`)

魔法技能；目标：地面区域；最高等级 5；射程：2；命中类型：Single；段数：1；属性：Wind；吟唱：5000 ms；持续时间1：Lv1=60000; Lv2=120000; Lv3=180000; Lv4=240000; Lv5=300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=48; Lv2=46; Lv3=44; Lv4=42; Lv5=40；道具 Yellow_Gemstone×1；关联状态：ViolentGale。

- 技能树最高等级：`5`
- 前置技能：SA_LIGHTNINGLOADER Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/deluge.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/skills/mage/volcano.cpp`, `src/map/skills/mage/whirlwind.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5903
limit = skill_get_time(skill_id,skill_lv);
// src/map/skill.cpp:7718
status_change_end(bl, SC_DANCING);
// src/map/skills/mage/deluge.cpp:9
void SkillDeluge::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/deluge.cpp:16
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/deluge.cpp:23
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/volcano.cpp:9
void SkillVolcano::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/volcano.cpp:16
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/volcano.cpp:23
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/whirlwind.cpp:9
void SkillWhirlwind::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/whirlwind.cpp:16
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/whirlwind.cpp:23
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Magnetic Earth (`SA_LANDPROTECTOR`)

魔法技能；目标：地面区域；最高等级 5；射程：2；命中类型：Single；段数：1；吟唱：5000 ms；持续时间1：Lv1=165000; Lv2=210000; Lv3=255000; Lv4=300000; Lv5=345000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=66; Lv2=62; Lv3=58; Lv4=54; Lv5=50；道具 Blue_Gemstone×1, Yellow_Gemstone×1。

- 技能树最高等级：`5`
- 前置技能：SA_VOLCANO Lv3, SA_DELUGE Lv3, SA_VIOLENTGALE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/magneticearth.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5872
struct s_skill_condition req = skill_get_requirement(sd,skill_id,skill_lv);
// src/map/skill.cpp:11342
* Chance triggered when damaged, timeout, or char step on it.
// src/map/skill.cpp:11739
skill_unitsetmapcell(unit,WZ_ICEWALL,group->skill_lv,CELL_ICEWALL,true);
// src/map/skill.cpp:11742
skill_unitsetmapcell(unit,SA_LANDPROTECTOR,group->skill_lv,CELL_LANDPROTECTOR,true);
// src/map/skill.cpp:11746
skill_unitsetmapcell(unit,HP_BASILICA,group->skill_lv,CELL_BASILICA,true);
// src/map/skill.cpp:11750
skill_unitsetmapcell(unit,SC_MAELSTROM,group->skill_lv,CELL_MAELSTROM,true);
// src/map/skill.cpp:11795
status_change_end(target, SC_ANKLE);
// src/map/skill.cpp:11802
skill_unitsetmapcell(unit,WZ_ICEWALL,group->skill_lv,CELL_ICEWALL,false);
// src/map/skill.cpp:11805
skill_unitsetmapcell(unit,SA_LANDPROTECTOR,group->skill_lv,CELL_LANDPROTECTOR,false);
// src/map/skill.cpp:11809
skill_unitsetmapcell(unit,HP_BASILICA,group->skill_lv,CELL_BASILICA,false);
// src/map/skill.cpp:11816
status_change_end(target, SC_ELECTRICSHOCKER);
// src/map/skills/mage/magneticearth.cpp:9
void SkillMagneticEarth::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Dispell (`SA_DISPELL`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：2000 ms；伤害标记：NoDamage；消耗/限制：SP 1；道具 Yellow_Gemstone×1。

- 技能树最高等级：`5`
- 前置技能：SA_SPELLBREAKER Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/dispell.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:4637
static int8 skill_castend_id_check(block_list *src, block_list *target, uint16 skill_id, uint16 skill_lv) {
// src/map/skill.cpp:4640
status_change *tsc = status_get_sc(target);
// src/map/skill.cpp:4642
if (src != target && (status_bl_has_mode(target,MD_SKILLIMMUNE) || (status_get_class(target) == MOBID_EMPERIUM && !skill->inf2[INF2_TARGETEMPERIUM])) && skill_get_casttype(skill_id) == CAST_NODAMAGE)
// src/map/skill.cpp:4643
return USESKILL_FAIL_MAX; // Don't show a skill fail message (NoDamage type doesn't consume requirements)
// src/map/skill.cpp:4646
case AL_HEAL:
// src/map/skill.cpp:4651
case AB_HIGHNESSHEAL:
// src/map/skills/mage/dispell.cpp:14
void SkillDispell::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/dispell.cpp:15
mob_data* dstmd = BL_CAST(BL_MOB, target);
// src/map/skills/mage/dispell.cpp:16
status_change *tsc = status_get_sc(target);
// src/map/skills/mage/dispell.cpp:17
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/dispell.cpp:18
map_session_data* dstsd = BL_CAST( BL_PC, target );
// src/map/skills/mage/dispell.cpp:21
if (flag&1 || (i = skill_get_splash(getSkillId(), skill_lv)) < 1) {
```

### Hocus-pocus (`SA_ABRACADABRA`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 50；道具 Yellow_Gemstone×2。

- 技能树最高等级：`10`
- 前置技能：SA_AUTOSPELL Lv5, SA_DISPELL Lv1, SA_LANDPROTECTOR Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/hocuspocus.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5188
ud->skill_lv = ud->skilltarget = 0;
// src/map/skill.cpp:9938
req.itemid[0] = skill->require.itemid[skill_lv - 1];
// src/map/skill.cpp:9939
req.amount[0] = skill->require.amount[skill_lv - 1];
// src/map/skill.cpp:9949
{	// All gem skills except Hocus Pocus and Ganbantein can cast for free with Mistress card -helvetica
// src/map/skill.cpp:10386
* Does delay reductions based on dex/agi, sc data, item bonuses, ...
// src/map/skill.cpp:10388
int32 skill_delayfix(block_list *bl, uint16 skill_id, uint16 skill_lv)
// src/map/skill.cpp:10393
return 0; //Will use picked skill's delay.
// src/map/skill.cpp:10395
if (bl->type&battle_config.no_skill_delay)
// src/map/skill.cpp:10396
return battle_config.min_skill_delay_limit;
// src/map/skill.cpp:10398
int32 delaynodex = skill_get_delaynodex(skill_id);
// src/map/skill.cpp:10399
double time = skill_get_delay(skill_id, skill_lv);
// src/map/skill.cpp:10404
status_change* sc = status_get_sc(bl);
```

### Create Elemental Converter (`SA_CREATECON`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；伤害标记：NoDamage；消耗/限制：SP 30。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/createelementalconverter.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:13007
if (battle_config.pp_rate != 100)
// src/map/skill.cpp:13008
make_per = make_per * battle_config.pp_rate / 100;
// src/map/skill.cpp:13014
make_per = 100000; // should be 100% success rate
// src/map/skills/mage/createelementalconverter.cpp:12
void SkillCreateElementalConverter::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/createelementalconverter.cpp:13
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/createelementalconverter.cpp:17
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/mage/skill_factory_mage.cpp:305
case SA_CASTCANCEL:
// src/map/skills/mage/skill_factory_mage.cpp:306
return std::make_unique<SkillCastCancel>();
```

### Elemental Change Water (`SA_ELEMENTWATER`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Water；吟唱：2000 ms；技能后摇：1000 ms；持续时间1：1800000 ms；伤害标记：NoDamage；消耗/限制：SP 30；道具 Elemental_Water×1；关联状态：ElementalChange。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/mage/elementalchangewater.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/elementalchangewater.cpp:14
void SkillElementalChangeWater::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/elementalchangewater.cpp:17
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/elementalchangewater.cpp:18
mob_data* dstmd = BL_CAST( BL_MOB, target );
// src/map/skills/mage/elementalchangewater.cpp:22
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
// src/map/skills/mage/elementalchangewater.cpp:23
sc_start2(src,target, type, 100, skill_lv, skill_get_ele(getSkillId(),skill_lv),
```

### Elemental Change Earth (`SA_ELEMENTGROUND`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Earth；吟唱：2000 ms；技能后摇：1000 ms；持续时间1：1800000 ms；伤害标记：NoDamage；消耗/限制：SP 30；道具 Elemental_Earth×1；关联状态：ElementalChange。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/mage/elementalchangeearth.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/elementalchangeearth.cpp:14
void SkillElementalChangeEarth::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/elementalchangeearth.cpp:17
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/elementalchangeearth.cpp:18
mob_data* dstmd = BL_CAST( BL_MOB, target );
// src/map/skills/mage/elementalchangeearth.cpp:22
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
// src/map/skills/mage/elementalchangeearth.cpp:23
sc_start2(src,target, type, 100, skill_lv, skill_get_ele(getSkillId(),skill_lv),
```

### Elemental Change Fire (`SA_ELEMENTFIRE`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Fire；吟唱：2000 ms；技能后摇：1000 ms；持续时间1：1800000 ms；伤害标记：NoDamage；消耗/限制：SP 30；道具 Elemental_Fire×1；关联状态：ElementalChange。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/mage/elementalchangefire.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/elementalchangefire.cpp:14
void SkillElementalChangeFire::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/elementalchangefire.cpp:17
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/elementalchangefire.cpp:18
mob_data* dstmd = BL_CAST( BL_MOB, target );
// src/map/skills/mage/elementalchangefire.cpp:22
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
// src/map/skills/mage/elementalchangefire.cpp:23
sc_start2(src,target, type, 100, skill_lv, skill_get_ele(getSkillId(),skill_lv),
```

### Elemental Change Wind (`SA_ELEMENTWIND`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Wind；吟唱：2000 ms；技能后摇：1000 ms；持续时间1：1800000 ms；伤害标记：NoDamage；消耗/限制：SP 30；道具 Elemental_Wind×1；关联状态：ElementalChange。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/mage/elementalchangewind.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/elementalchangewind.cpp:14
void SkillElementalChangeWind::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/elementalchangewind.cpp:17
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/mage/elementalchangewind.cpp:18
mob_data* dstmd = BL_CAST( BL_MOB, target );
// src/map/skills/mage/elementalchangewind.cpp:22
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
// src/map/skills/mage/elementalchangewind.cpp:23
sc_start2(src,target, type, 100, skill_lv, skill_get_ele(getSkillId(),skill_lv),
```
