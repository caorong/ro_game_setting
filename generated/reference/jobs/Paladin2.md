# Paladin2 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Paladin2` 公式页](../skill-formulas/Paladin2.md)

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
| 367 | `PA_PRESSURE` | Gloria Domini | 5 | Paladin | 否 | SM_ENDURE Lv5, CR_TRUST Lv5, CR_SHIELDCHARGE Lv2 | Misc / Attack |
| 368 | `PA_SACRIFICE` | Martyr's Reckoning | 5 | Paladin2 | 是 | SM_ENDURE Lv5, CR_TRUST Lv5, CR_DEVOTION Lv3 | Weapon / Self |
| 369 | `PA_GOSPEL` | Battle Chant | 10 | Paladin | 否 | CR_TRUST Lv8, AL_DP Lv3, AL_DEMONBANE Lv5 | Misc / Self |
| 480 | `PA_SHIELDCHAIN` | Shield Chain | 5 | Paladin | 否 | CR_SHIELDBOOMERANG Lv5 | Weapon / Attack |

## 技能详情

### Martyr's Reckoning (`PA_SACRIFICE`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；技能后摇：2000 ms；伤害标记：NoDamage, IgnoreDefense, IgnoreFlee；消耗/限制：SP 100；关联状态：Sacrifice。

- 技能树最高等级：`5`
- 前置技能：SM_ENDURE Lv5, CR_TRUST Lv5, CR_DEVOTION Lv3
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
