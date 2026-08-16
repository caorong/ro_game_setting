# Paladin 技能

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
| 63 | `KN_RIDING` | Peco Peco Riding | 1 | Crusader | 否 | SM_ENDURE Lv1 | Weapon / Passive |
| 64 | `KN_CAVALIERMASTERY` | Cavalier Mastery | 5 | Crusader | 否 | KN_RIDING Lv1 | Weapon / Passive |
| 55 | `KN_SPEARMASTERY` | Spear Mastery | 10 | Crusader | 否 | — | Weapon / Passive |
| 35 | `AL_CURE` | Cure | 1 | Crusader | 否 | CR_TRUST Lv5 | Magic / Support |
| 22 | `AL_DP` | Divine Protection | 10 | Crusader | 否 | AL_CURE Lv1 | Weapon / Passive |
| 23 | `AL_DEMONBANE` | Demon Bane | 10 | Crusader | 否 | AL_DP Lv3 | Weapon / Passive |
| 28 | `AL_HEAL` | Heal | 10 | Crusader | 否 | AL_DEMONBANE Lv5, CR_TRUST Lv10 | Magic / Support |
| 248 | `CR_TRUST` | Faith | 10 | Crusader | 否 | — | None / Passive |
| 249 | `CR_AUTOGUARD` | Guard | 10 | Crusader | 否 | — | Weapon / Self |
| 250 | `CR_SHIELDCHARGE` | Smite | 5 | Crusader | 否 | CR_AUTOGUARD Lv5 | Weapon / Attack |
| 251 | `CR_SHIELDBOOMERANG` | Shield Boomerang | 5 | Crusader | 否 | CR_SHIELDCHARGE Lv3 | Weapon / Attack |
| 252 | `CR_REFLECTSHIELD` | Shield Reflect | 10 | Crusader | 否 | CR_SHIELDBOOMERANG Lv3 | Weapon / Self |
| 253 | `CR_HOLYCROSS` | Holy Cross | 10 | Crusader | 否 | CR_TRUST Lv7 | Weapon / Attack |
| 254 | `CR_GRANDCROSS` | Grand Cross | 10 | Crusader | 否 | CR_HOLYCROSS Lv6, CR_TRUST Lv10 | Magic / Self |
| 255 | `CR_DEVOTION` | Sacrifice | 5 | Crusader | 否 | CR_REFLECTSHIELD Lv5, CR_GRANDCROSS Lv4 | None / Support |
| 256 | `CR_PROVIDENCE` | Resistant Souls | 5 | Crusader | 否 | AL_DP Lv5, AL_HEAL Lv5 | None / Support |
| 257 | `CR_DEFENDER` | Defending Aura | 5 | Crusader | 否 | CR_SHIELDBOOMERANG Lv1 | Weapon / Self |
| 258 | `CR_SPEARQUICKEN` | Spear Quicken | 10 | Crusader | 否 | KN_SPEARMASTERY Lv10 | Weapon / Self |
| 1002 | `CR_SHRINK` | Shrink | 1 | Crusader | 否 | — | Weapon / Self |
| 367 | `PA_PRESSURE` | Gloria Domini | 5 | Paladin | 是 | SM_ENDURE Lv5, CR_TRUST Lv5, CR_SHIELDCHARGE Lv2 | Misc / Attack |
| 368 | `PA_SACRIFICE` | Martyr's Reckoning | 5 | Paladin | 是 | SM_ENDURE Lv1, CR_TRUST Lv5, CR_DEVOTION Lv3 | Weapon / Self |
| 369 | `PA_GOSPEL` | Battle Chant | 10 | Paladin | 是 | CR_TRUST Lv8, AL_DP Lv3, AL_DEMONBANE Lv5 | Misc / Self |
| 480 | `PA_SHIELDCHAIN` | Shield Chain | 5 | Paladin | 是 | CR_SHIELDBOOMERANG Lv5 | Weapon / Attack |

## 技能详情

### Gloria Domini (`PA_PRESSURE`)

特殊技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：1；吟唱：Lv1=2000; Lv2=2500; Lv3=3000; Lv4=3500; Lv5=4000 ms；技能后摇：Lv1=2000; Lv2=2500; Lv3=3000; Lv4=3500; Lv5=4000 ms；持续时间2：Lv1=2000; Lv2=3000; Lv3=4000; Lv4=5000; Lv5=6000 ms；伤害标记：IgnoreElement, IgnoreFlee, IgnoreDefCard；消耗/限制：SP Lv1=30; Lv2=35; Lv3=40; Lv4=45; Lv5=50。

- 技能树最高等级：`5`
- 前置技能：SM_ENDURE Lv5, CR_TRUST Lv5, CR_SHIELDCHARGE Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/swordman/gloriadomini.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:434
damage > 0 && skill_id != CR_REFLECTSHIELD
// src/map/battle.cpp:439
map_session_data* tsd = BL_CAST( BL_PC, target );
// src/map/battle.cpp:446
damage = 0;
// src/map/battle.cpp:1291
if ((sce = sc->getSCE(SC_KYRIE)) && damage > 0) {
// src/map/battle.cpp:1292
sce->val2 -= static_cast<int32>(cap_value(damage, INT_MIN, INT_MAX));
// src/map/battle.cpp:1295
damage = 0;
// src/map/battle.cpp:1297
damage = -sce->val2;
// src/map/battle.cpp:1302
status_change_end(target, SC_KYRIE);
// src/map/battle.cpp:1309
element = battle_get_weapon_element(*d, *src, *target, skill_id, skill_lv, EQI_HAND_L, false);
// src/map/battle.cpp:1311
element = battle_get_weapon_element(*d, *src, *target, skill_id, skill_lv, EQI_HAND_R, false);
// src/map/battle.cpp:1313
element = battle_get_magic_element(*d, *src, *target, skill_id, skill_lv);
// src/map/battle.cpp:1691
if(flag&BF_MAGIC && sd->special_state.no_magic_damage)
```

### Martyr's Reckoning (`PA_SACRIFICE`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；技能后摇：2000 ms；伤害标记：NoDamage, IgnoreDefense, IgnoreFlee；消耗/限制：SP 100；关联状态：Sacrifice。

- 技能树最高等级：`5`
- 前置技能：SM_ENDURE Lv1, CR_TRUST Lv5, CR_DEVOTION Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/swordman/martyrsreckoning.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

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
// src/map/battle.cpp:3647
std::bitset<NK_MAX> nk = battle_skill_get_damage_properties(skill_id, wd->miscflag);
// src/map/battle.cpp:3648
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/battle.cpp:3649
status_change* sc = status_get_sc(src);
// src/map/battle.cpp:3652
int32 right_element = battle_get_weapon_element(*wd, *src, *target, skill_id, skill_lv, EQI_HAND_R, true);
// src/map/battle.cpp:3655
if(!nk[NK_IGNOREELEMENT] && (wd->damage > 0 || wd->damage2 > 0)) {
// src/map/battle.cpp:3656
int32 left_element = battle_get_weapon_element(*wd, *src, *target, skill_id, skill_lv, EQI_HAND_L, true);
```

### Battle Chant (`PA_GOSPEL`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage, IgnoreFlee；消耗/限制：SP Lv1-5=80; Lv6-10=100；关联状态：Gospel。

- 技能树最高等级：`10`
- 前置技能：CR_TRUST Lv8, AL_DP Lv3, AL_DEMONBANE Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/swordman/battlechant.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6422
mob_data& mob = *reinterpret_cast<mob_data*>(target);
// src/map/battle.cpp:6425
md.damage = 400;
// src/map/battle.cpp:6429
md.damage = 500 + 300 * skill_lv;
// src/map/battle.cpp:6434
md.damage = (rnd() % 4000) + 1500;
// src/map/battle.cpp:6436
md.damage = (rnd() % 5000) + 3000;
// src/map/battle.cpp:6438
md.damage -= (int64)status_get_def(target);
// src/map/battle.cpp:6440
md.damage -= (md.damage * (int64)status_get_def(target)) / 100;
// src/map/battle.cpp:6442
md.damage -= tstatus->def2;
// src/map/battle.cpp:6443
if (md.damage < 0)
// src/map/battle.cpp:6444
md.damage = 0;
// src/map/skill.cpp:2975
if (homun_data *hd = BL_CAST(BL_HOM, src); hd != nullptr) {
// src/map/skill.cpp:2983
skill_combo(src,dsrc,bl,skill_id,skill_lv,tick);
```

### Shield Chain (`PA_SHIELDCHAIN`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：4；命中类型：Multi_Hit；段数：5；吟唱：1000 ms；技能后摇：1000 ms；消耗/限制：SP Lv1=28; Lv2=31; Lv3=34; Lv4=37; Lv5=40；状态 Shield。

- 技能树最高等级：`5`
- 前置技能：CR_SHIELDBOOMERANG Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/archer/gloomyday.cpp`, `src/map/skills/swordman/shieldchain.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

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
// src/map/battle.cpp:3305
hitrate += hitrate * ( 2 * skill ) / 100;
// src/map/battle.cpp:3309
hitrate += 3 * skill;
// src/map/battle.cpp:3312
hitrate = cap_value(hitrate, battle_config.min_hitrate, battle_config.max_hitrate);
// src/map/battle.cpp:3315
hitrate += 20; //Rapid Smiting gives a flat +20 hit after the hitrate was capped
// src/map/battle.cpp:3317
return (rnd()%100 < hitrate);
// src/map/battle.cpp:3321
* If attack ignores def.
```
