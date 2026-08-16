# Crusader 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 2 | `SM_SWORD` | Sword Mastery | 10 | Swordman | 否 | — | Weapon / Passive |
| 3 | `SM_TWOHAND` | Two-Handed Sword Mastery | 10 | Swordman | 否 | SM_SWORD Lv1 | Weapon / Passive |
| 4 | `SM_RECOVERY` | Increase HP Recovery | 10 | Swordman | 否 | — | None / Passive |
| 5 | `SM_BASH` | Bash | 10 | Swordman | 否 | — | Weapon / Attack |
| 6 | `SM_PROVOKE` | Provoke | 10 | Swordman | 否 | — | None / Attack |
| 7 | `SM_MAGNUM` | Magnum Break | 10 | Swordman | 否 | SM_BASH Lv5 | Weapon / Self |
| 8 | `SM_ENDURE` | Endure | 10 | Swordman | 否 | SM_PROVOKE Lv5 | Weapon / Self |
| 144 | `SM_MOVINGRECOVERY` | Moving HP-Recovery | 1 | Swordman | 否 | — | None / Passive |
| 145 | `SM_FATALBLOW` | Fatal Blow | 1 | Swordman | 否 | — | Weapon / Passive |
| 146 | `SM_AUTOBERSERK` | Auto Berserk | 1 | Swordman | 否 | — | Weapon / Self |
| 63 | `KN_RIDING` | Peco Peco Riding | 1 | Crusader | 是 | SM_ENDURE Lv1 | Weapon / Passive |
| 64 | `KN_CAVALIERMASTERY` | Cavalier Mastery | 5 | Crusader | 是 | KN_RIDING Lv1 | Weapon / Passive |
| 55 | `KN_SPEARMASTERY` | Spear Mastery | 10 | Crusader | 是 | — | Weapon / Passive |
| 35 | `AL_CURE` | Cure | 1 | Crusader | 是 | CR_TRUST Lv5 | Magic / Support |
| 22 | `AL_DP` | Divine Protection | 10 | Crusader | 是 | AL_CURE Lv1 | Weapon / Passive |
| 23 | `AL_DEMONBANE` | Demon Bane | 10 | Crusader | 是 | AL_DP Lv3 | Weapon / Passive |
| 28 | `AL_HEAL` | Heal | 10 | Crusader | 是 | AL_DEMONBANE Lv5, CR_TRUST Lv10 | Magic / Support |
| 248 | `CR_TRUST` | Faith | 10 | Crusader | 是 | — | None / Passive |
| 249 | `CR_AUTOGUARD` | Guard | 10 | Crusader | 是 | — | Weapon / Self |
| 250 | `CR_SHIELDCHARGE` | Smite | 5 | Crusader | 是 | CR_AUTOGUARD Lv5 | Weapon / Attack |
| 251 | `CR_SHIELDBOOMERANG` | Shield Boomerang | 5 | Crusader | 是 | CR_SHIELDCHARGE Lv3 | Weapon / Attack |
| 252 | `CR_REFLECTSHIELD` | Shield Reflect | 10 | Crusader | 是 | CR_SHIELDBOOMERANG Lv3 | Weapon / Self |
| 253 | `CR_HOLYCROSS` | Holy Cross | 10 | Crusader | 是 | CR_TRUST Lv7 | Weapon / Attack |
| 254 | `CR_GRANDCROSS` | Grand Cross | 10 | Crusader | 是 | CR_HOLYCROSS Lv6, CR_TRUST Lv10 | Magic / Self |
| 255 | `CR_DEVOTION` | Sacrifice | 5 | Crusader | 是 | CR_REFLECTSHIELD Lv5, CR_GRANDCROSS Lv4 | None / Support |
| 256 | `CR_PROVIDENCE` | Resistant Souls | 5 | Crusader | 是 | AL_DP Lv5, AL_HEAL Lv5 | None / Support |
| 257 | `CR_DEFENDER` | Defending Aura | 5 | Crusader | 是 | CR_SHIELDBOOMERANG Lv1 | Weapon / Self |
| 258 | `CR_SPEARQUICKEN` | Spear Quicken | 10 | Crusader | 是 | KN_SPEARMASTERY Lv10 | Weapon / Self |
| 1002 | `CR_SHRINK` | Shrink | 1 | Crusader | 是 | — | Weapon / Self |

## 技能详情

### Peco Peco Riding (`KN_RIDING`)

武器/物理技能；目标：被动；最高等级 1。

- 技能树最高等级：`1`
- 前置技能：SM_ENDURE Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/status.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Cavalier Mastery (`KN_CAVALIERMASTERY`)

武器/物理技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：KN_RIDING Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
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
// src/map/status.cpp:2406
? (job->aspd_base[sd->status.weapon]) // Single weapon
```

### Spear Mastery (`KN_SPEARMASTERY`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/swordman/phantomthrust.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
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
// src/map/skills/swordman/phantomthrust.cpp:18
void SkillPhantomThrust::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
// src/map/skills/swordman/phantomthrust.cpp:19
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/swordman/phantomthrust.cpp:22
skillratio += -100 + 50 * skill_lv + 10 * (sd ? pc_checkskill(sd,KN_SPEARMASTERY) : 5);
// src/map/skills/swordman/phantomthrust.cpp:26
void SkillPhantomThrust::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Cure (`AL_CURE`)

魔法技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；技能后摇：1000 ms；持续时间2：6000 ms；伤害标记：NoDamage；消耗/限制：SP 15。

- 技能树最高等级：`1`
- 前置技能：CR_TRUST Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/cure.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/cure.cpp:13
void SkillCure::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
// src/map/skills/acolyte/cure.cpp:17
clif_skill_nodamage(src, *bl, getSkillId(), skill_lv, false);
// src/map/skills/acolyte/cure.cpp:20
status_change_end(bl, SC_SILENCE);
// src/map/skills/acolyte/cure.cpp:21
status_change_end(bl, SC_BLIND);
// src/map/skills/acolyte/skill_factory_acolyte.cpp:174
case AL_HEAL:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:175
return std::make_unique<SkillHeal>();
```

### Divine Protection (`AL_DP`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：AL_CURE Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Demon Bane (`AL_DEMONBANE`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：AL_DP Lv3
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2279
int64 damage;
// src/map/battle.cpp:2284
damage = 0;
// src/map/battle.cpp:2286
damage = dmg;
// src/map/battle.cpp:2294
damage += static_cast<decltype(damage)>(skill * (sd->status.base_level / 20.0 + 3.0));
// src/map/battle.cpp:2296
damage += (skill * 5);
// src/map/battle.cpp:2298
damage += (skill * 10);
// src/map/battle.cpp:2300
damage += (15 * pc_checkskill(sd, NC_MADOLICENCE)); // Attack bonus is granted even without the Madogear
// src/map/battle.cpp:2303
damage += (skill * 4);
```

### Heal (`AL_HEAL`)

魔法技能；目标：友方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Holy；技能后摇：1000 ms；伤害标记：NoDamage, IgnoreDefense；消耗/限制：SP Lv1=13; Lv2=16; Lv3=19; Lv4=22; Lv5=25; Lv6=28; Lv7=31; Lv8=34; Lv9=37; Lv10=40。

- 技能树最高等级：`10`
- 前置技能：AL_DEMONBANE Lv5, CR_TRUST Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/mob.cpp`, `src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/coluceoheal.cpp`, `src/map/skills/acolyte/competentia.cpp`, `src/map/skills/acolyte/dilectioheal.cpp`, `src/map/skills/acolyte/heal.cpp`, `src/map/skills/acolyte/medialevotum.cpp`, `src/map/skills/acolyte/reparatio.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/homunculus/homunculus_benedictionofchaos.cpp`, `src/map/skills/mage/drainlife.cpp`, `src/map/skills/merchant/aidberserkpotion.cpp`, `src/map/skills/merchant/aidcondensedpotion.cpp`, `src/map/skills/merchant/aidpotion.cpp`, `src/map/skills/npc/energydrain.cpp`, `src/map/skills/npc/fullheal.cpp`, `src/map/skills/npc/npccoluceoheal.cpp`, `src/map/skills/npc/suckingblood.cpp`, `src/map/skills/npc/vampiregift.cpp`, `src/map/skills/other/netrepair.cpp`, `src/map/skills/summoner/kisulwaterspraying.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5881
ad.damage = 0;
// src/map/battle.cpp:5883
#define MATK_RATE(a) { ad.damage = ad.damage * (a) / 100; }
// src/map/battle.cpp:5885
#define MATK_ADDRATE(a) { ad.damage += ad.damage * (a) / 100; }
// src/map/battle.cpp:5887
#define MATK_ADD(a) { ad.damage += a; }
// src/map/battle.cpp:5891
case AL_HEAL:
// src/map/battle.cpp:5894
case AB_HIGHNESSHEAL:
// src/map/battle.cpp:5895
ad.damage = skill_calc_heal(src, target, skill_id, skill_lv, false);
// src/map/battle.cpp:5898
ad.damage = 40;
// src/map/mob.cpp:4715
ms->cond1 = MSC_MYHPLTMAXRATE;
// src/map/mob.cpp:4719
ms->delay += -5000 +(skill_get_time(skill_id, ms->skill_lv) + skill_get_time2(skill_id, ms->skill_lv))/2;
// src/map/mob.cpp:4720
if (ms->delay < 5000)
// src/map/mob.cpp:4721
ms->delay = 5000; //With a minimum of 5 secs.
```

### Faith (`CR_TRUST`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:3142
status_change *sc = status_get_sc(bl);
// src/map/status.cpp:3147
uint16 skill_lv;
// src/map/status.cpp:3149
bonus += sd->bonus.hp;
// src/map/status.cpp:3150
if ((skill_lv = pc_checkskill(sd,CR_TRUST)) > 0)
// src/map/status.cpp:3151
bonus += skill_lv * 200;
// src/map/status.cpp:3159
if ((skill_lv = pc_checkskill(sd, NV_BREAKTHROUGH)) > 0)
// src/map/status.cpp:3160
bonus += 350 * skill_lv + (skill_lv > 4 ? 250 : 0);
// src/map/status.cpp:3161
if ((skill_lv = pc_checkskill(sd, NV_TRANSCENDENCE)) > 0)
// src/map/status.cpp:3162
bonus += 350 * skill_lv + (skill_lv > 4 ? 250 : 0);
// src/map/status.cpp:4666
if(sd->dsprate < 0)
// src/map/status.cpp:4667
sd->dsprate = 0;
// src/map/status.cpp:4668
if(sd->castrate < 0)
```

### Guard (`CR_AUTOGUARD`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30；状态 Shield；关联状态：AutoGuard。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1532
delay = 100;
// src/map/battle.cpp:1542
{ //If player is target of devotion, show guard effect on the devotion caster rather than the target
// src/map/battle.cpp:1543
clif_skill_nodamage(d_bl, *d_bl, CR_AUTOGUARD, sce->val1);
// src/map/battle.cpp:1544
unit_set_walkdelay(d_bl, gettick(), delay, 1);
// src/map/battle.cpp:1548
clif_skill_nodamage(target, *target, CR_AUTOGUARD, sce->val1);
// src/map/battle.cpp:1549
unit_set_walkdelay(target, gettick(), delay, 1);
// src/map/battle.cpp:1552
sc_start(target, src, SC_STUN, 50, skill_lv, skill_get_time2(skill_id, skill_lv));
```

### Smite (`CR_SHIELDCHARGE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：3；命中类型：Single；段数：1；击退：Lv1=5; Lv2=6; Lv3=7; Lv4=8; Lv5=9；持续时间2：5000 ms；消耗/限制：SP 10；状态 Shield；关联状态：Stun。

- 技能树最高等级：`5`
- 前置技能：CR_AUTOGUARD Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/gloomyday.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`, `src/map/skills/swordman/smite.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/gloomyday.cpp:13
void SkillGloomyDay::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/gloomyday.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/archer/gloomyday.cpp:17
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/archer/gloomyday.cpp:22
sc_start(src,target,SC_GLOOMYDAY_SK,100,skill_lv,skill_get_time(getSkillId(),skill_lv));
// src/map/skills/archer/gloomyday.cpp:26
sc_start(src,target,type,100,skill_lv,skill_get_time(getSkillId(),skill_lv));
// src/map/skills/swordman/smite.cpp:11
void SkillSmite::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/swordman/smite.cpp:12
base_skillratio += 20 * skill_lv;
// src/map/skills/swordman/smite.cpp:15
void SkillSmite::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/swordman/smite.cpp:16
sc_start(src,target,SC_STUN,(15+skill_lv*5),skill_lv,skill_get_time2(getSkillId(),skill_lv));
```

### Shield Boomerang (`CR_SHIELDBOOMERANG`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：Lv1=3; Lv2=5; Lv3=7; Lv4=9; Lv5=11；命中类型：Single；段数：1；技能后摇：700 ms；消耗/限制：SP 12；状态 Shield。

- 技能树最高等级：`5`
- 前置技能：CR_SHIELDCHARGE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/gloomyday.cpp`, `src/map/skills/swordman/shieldboomerang.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3236
int16 flee, hitrate;
// src/map/battle.cpp:3239
return (wd->dmg_lv != ATK_FLEE);
// src/map/battle.cpp:3240
if (is_attack_critical(wd, src, target, skill_id, skill_lv, false))
// src/map/battle.cpp:3252
else if (nk[NK_IGNOREFLEE])
// src/map/battle.cpp:3258
flee = tstatus->flee;
// src/map/battle.cpp:3260
hitrate = 0; //Default hitrate
// src/map/battle.cpp:3698
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3700
wd->damage2 = battle_attr_fix(src, target, wd->damage2, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:4044
ATK_ADD(wd->damage, wd->damage2, i); //Add str bonus.
// src/map/battle.cpp:4047
ATK_RATE(wd->damage, wd->damage2, 125);
// src/map/battle.cpp:4051
ATK_RATE(wd->damage, wd->damage2, 75);
// src/map/battle.cpp:4058
wd->damage = sstatus->batk;
```

### Shield Reflect (`CR_REFLECTSHIELD`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=35; Lv2=40; Lv3=45; Lv4=50; Lv5=55; Lv6=60; Lv7=65; Lv8=70; Lv9=75; Lv10=80；状态 Shield；关联状态：ReflectShield。

- 技能树最高等级：`10`
- 前置技能：CR_SHIELDBOOMERANG Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/swordman/shieldreflect.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:397
battle_damage(src, target, dat->damage, dat->div_, dat->skill_lv, dat->skill_id, dat->dmg_lv, dat->attack_type, dat->additional_effects, tick, dat->isspdamage, dat->is_norm_attacked);
// src/map/battle.cpp:398
} else if( !src && dat->skill_id == CR_REFLECTSHIELD ) { // it was monster reflected damage, and the monster died, we pass the damage to the character as expected
// src/map/battle.cpp:399
battle_fix_damage(target, target, dat->damage, dat->div_, dat->skill_id);
// src/map/battle.cpp:403
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/battle.cpp:405
if (sd && --sd->delayed_damage == 0 && sd->state.hold_recalc) {
// src/map/battle.cpp:410
ers_free(delay_damage_ers, dat);
// src/map/battle.cpp:434
damage > 0 && skill_id != CR_REFLECTSHIELD
// src/map/battle.cpp:439
map_session_data* tsd = BL_CAST( BL_PC, target );
// src/map/battle.cpp:446
damage = 0;
// src/map/battle.cpp:5109
map_session_data *tsd = BL_CAST(BL_PC, target);
// src/map/battle.cpp:5113
rdamage = battle_calc_return_damage(target, src, &damage, wd->flag, skill_id, false);
// src/map/battle.cpp:5114
if( rdamage > 0 ) { //Item reflect gets calculated before any mapflag reducing is applicated
```

### Holy Cross (`CR_HOLYCROSS`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-2；命中类型：Multi_Hit；段数：-2；属性：Holy；持续时间2：30000 ms；消耗/限制：SP Lv1=11; Lv2=12; Lv3=13; Lv4=14; Lv5=15; Lv6=16; Lv7=17; Lv8=18; Lv9=19; Lv10=20；关联状态：Blind。

- 技能树最高等级：`10`
- 前置技能：CR_TRUST Lv7
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/swordman/holycross.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2983
skill_combo(src,dsrc,bl,skill_id,skill_lv,tick);
// src/map/skill.cpp:2988
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, CR_HOLYCROSS, -1, DMG_SPLASH );
// src/map/skill.cpp:2994
dmg.amotion = 0; //Disable delay or attack will do no damage since source is dead by the time it takes effect. [Skotlex]
// src/map/skills/swordman/holycross.cpp:14
void SkillHolyCross::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/swordman/holycross.cpp:16
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/swordman/holycross.cpp:19
base_skillratio += 70 * skill_lv;
// src/map/skills/swordman/holycross.cpp:22
base_skillratio += 35 * skill_lv;
```

### Grand Cross (`CR_GRANDCROSS`)

魔法技能；目标：自身；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Holy；吟唱：3000 ms；技能后摇：1500 ms；移动后摇：1000 ms；持续时间1：950 ms；持续时间2：30000 ms；消耗/限制：SP Lv1=37; Lv2=44; Lv3=51; Lv4=58; Lv5=65; Lv6=72; Lv7=79; Lv8=86; Lv9=93; Lv10=100；HP% 20；关联状态：Blind。

- 技能树最高等级：`10`
- 前置技能：CR_HOLYCROSS Lv6, CR_TRUST Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/swordman/grandcross.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3165
static int32 is_attack_piercing(struct Damage* wd, block_list* src, const block_list* target, int32 skill_id, int32 skill_lv, int16 weapon_position)
// src/map/battle.cpp:3171
const map_session_data* sd = BL_CAST(BL_PC,src);
// src/map/battle.cpp:3176
&& !is_attack_critical(wd, src, target, skill_id, skill_lv, false)
// src/map/battle.cpp:3180
if( sd && (sd->right_weapon.def_ratio_atk_ele & (1<<tstatus->def_ele) || sd->right_weapon.def_ratio_atk_ele & (1<<ELE_ALL) ||
// src/map/battle.cpp:3181
sd->right_weapon.def_ratio_atk_race & (1<<tstatus->race) || sd->right_weapon.def_ratio_atk_race & (1<<RC_ALL) ||
// src/map/battle.cpp:3182
sd->right_weapon.def_ratio_atk_class & (1<<tstatus->class_) || sd->right_weapon.def_ratio_atk_class & (1<<CLASS_ALL))
// src/map/battle.cpp:6168
ad.damage = (int64)( (double)( ad.damage + ad.damage * i / 100. ) );
// src/map/battle.cpp:6179
struct Damage wd = initialize_weapon_data(src, target, skill_id, skill_lv, mflag);
// src/map/battle.cpp:6180
battle_calc_skill_base_damage(&wd, src, target, skill_id, skill_lv);
// src/map/battle.cpp:6184
wd.damage = wd.statusAtk + wd.weaponAtk + wd.equipAtk + wd.percentAtk;
// src/map/battle.cpp:6238
ad.damage = battle_attr_fix(src, target, ad.damage, s_ele, tstatus->def_ele, tstatus->ele_lv);
// src/map/battle.cpp:6241
ad.damage += battle_calc_cardfix(BF_MAGIC, src, target, nk, s_ele, 0, ad.damage, 0, ad.flag);
```

### Sacrifice (`CR_DEVOTION`)

非伤害技能；目标：友方目标；最高等级 5；射程：Lv1=7; Lv2=8; Lv3=9; Lv4=10; Lv5=11；命中类型：Single；段数：1；吟唱：3000 ms；持续时间2：Lv1=30000; Lv2=45000; Lv3=60000; Lv4=75000; Lv5=90000 ms；伤害标记：NoDamage；消耗/限制：SP 25；关联状态：Devotion。

- 技能树最高等级：`5`
- 前置技能：CR_REFLECTSHIELD Lv5, CR_GRANDCROSS Lv4
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/swordman/sacrifice.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:7454
status_change *d_sc = status_get_sc(d_bl);
// src/map/battle.cpp:7463
devotion_damage -= devotion_damage * d_sc->getSCE(SC_REBOUND_S)->val2 / 100;
// src/map/battle.cpp:7465
clif_damage(*d_bl, *d_bl, gettick(), wd.amotion, wd.dmotion, devotion_damage, 1, DMG_NORMAL, 0, false);
// src/map/battle.cpp:7466
battle_fix_damage(src, d_bl, devotion_damage, 0, CR_DEVOTION);
// src/map/battle.cpp:7470
status_change_end(target, SC_DEVOTION);
// src/map/battle.cpp:7476
clif_skill_damage(*ed, *target, tick, status_get_amotion(src), 0, DMGVAL_IGNORE, 1, EL_CIRCLE_OF_FIRE, tsc->getSCE(SC_CIRCLE_OF_FIRE_OPTION)->val1, DMG_SINGLE );
// src/map/skills/swordman/sacrifice.cpp:13
void SkillSacrifice::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/swordman/sacrifice.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/swordman/sacrifice.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
```

### Resistant Souls (`CR_PROVIDENCE`)

非伤害技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：3000 ms；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 30；关联状态：Providence。

- 技能树最高等级：`5`
- 前置技能：AL_DP Lv5, AL_HEAL Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/resistantsouls.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/resistantsouls.cpp:13
void SkillResistantSouls::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/swordman/resistantsouls.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/swordman/resistantsouls.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
```

### Defending Aura (`CR_DEFENDER`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；技能后摇：800 ms；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 30；状态 Shield；关联状态：Defender。

- 技能树最高等级：`5`
- 前置技能：CR_SHIELDBOOMERANG Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/skill_factory_swordman.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:12146
val2 = (status->int_ + status->luk) * val1 / 20 * status_get_lv(bl) / 200 + val1;	// Chance to evade magic damage.
// src/map/status.cpp:12150
val2 = 5; // 5% HP every 3 seconds
// src/map/status.cpp:12155
val2 = 3; // 3% SP every 5 seconds
```

### Spear Quicken (`CR_SPEARQUICKEN`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000; Lv6=180000; Lv7=210000; Lv8=240000; Lv9=270000; Lv10=300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=24; Lv2=28; Lv3=32; Lv4=36; Lv5=40; Lv6=44; Lv7=48; Lv8=52; Lv9=56; Lv10=60；武器 2hSpear；关联状态：SpearQuicken。

- 技能树最高等级：`10`
- 前置技能：KN_SPEARMASTERY Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/overbrand.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/overbrand.cpp:16
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/swordman/overbrand.cpp:17
skill_castend_damage_id(src, target, getSkillId(), skill_lv, tick, flag);
// src/map/skills/swordman/overbrand.cpp:20
void SkillOverBrand::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& skillratio, int32 mflag) const {
// src/map/skills/swordman/overbrand.cpp:21
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/swordman/overbrand.cpp:22
const status_change* sc = status_get_sc(src);
// src/map/skills/swordman/overbrand.cpp:25
skillratio += -100 + 500 * skill_lv;
// src/map/skills/swordman/overbrand.cpp:27
skillratio += -100 + 350 * skill_lv;
// src/map/skills/swordman/overbrand.cpp:28
skillratio += ((sd) ? pc_checkskill(sd, CR_SPEARQUICKEN) * 50 : 0);
```

### Shrink (`CR_SHRINK`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；击退：2；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP 15；状态 Shield；关联状态：Shrink。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1543
clif_skill_nodamage(d_bl, *d_bl, CR_AUTOGUARD, sce->val1);
// src/map/battle.cpp:1544
unit_set_walkdelay(d_bl, gettick(), delay, 1);
// src/map/battle.cpp:1548
clif_skill_nodamage(target, *target, CR_AUTOGUARD, sce->val1);
// src/map/battle.cpp:1549
unit_set_walkdelay(target, gettick(), delay, 1);
// src/map/battle.cpp:1552
sc_start(target, src, SC_STUN, 50, skill_lv, skill_get_time2(skill_id, skill_lv));
// src/map/battle.cpp:1564
|| skill_id == CR_ACIDDEMONSTRATION
```
