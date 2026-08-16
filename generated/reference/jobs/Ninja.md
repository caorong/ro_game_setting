# Ninja 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 522 | `NJ_TOBIDOUGU` | Shuriken Training | 10 | Ninja | 是 | — | Weapon / Passive |
| 523 | `NJ_SYURIKEN` | Throw Shuriken | 10 | Ninja | 是 | NJ_TOBIDOUGU Lv1 | Weapon / Attack |
| 524 | `NJ_KUNAI` | Throw Kunai | 5 | Ninja | 是 | NJ_SYURIKEN Lv5 | Weapon / Attack |
| 525 | `NJ_HUUMA` | Throw Huuma Shuriken | 5 | Ninja | 是 | NJ_TOBIDOUGU Lv5, NJ_KUNAI Lv5 | Weapon / Attack |
| 526 | `NJ_ZENYNAGE` | Throw Zeny | 10 | Ninja | 是 | NJ_TOBIDOUGU Lv10, NJ_HUUMA Lv5 | Misc / Attack |
| 527 | `NJ_TATAMIGAESHI` | Improvised Defense | 5 | Ninja | 是 | — | Weapon / Self |
| 528 | `NJ_KASUMIKIRI` | Vanishing Slash | 10 | Ninja | 是 | NJ_SHADOWJUMP Lv1 | Weapon / Attack |
| 529 | `NJ_SHADOWJUMP` | Shadow Leap | 5 | Ninja | 是 | NJ_TATAMIGAESHI Lv1 | None / Ground |
| 530 | `NJ_KIRIKAGE` | Shadow Slash | 5 | Ninja | 是 | NJ_KASUMIKIRI Lv5 | Weapon / Attack |
| 531 | `NJ_UTSUSEMI` | Cicada Skin Sheeding | 5 | Ninja | 是 | NJ_SHADOWJUMP Lv5 | None / Self |
| 532 | `NJ_BUNSINJYUTSU` | Mirror Image | 10 | Ninja | 是 | NJ_UTSUSEMI Lv4, NJ_KIRIKAGE Lv3, NJ_NEN Lv1 | Magic / Self |
| 533 | `NJ_NINPOU` | Spirit of the Blade | 10 | Ninja | 是 | — | None / Passive |
| 534 | `NJ_KOUENKA` | Crimson Fire Petal | 10 | Ninja | 是 | NJ_NINPOU Lv1 | Magic / Attack |
| 535 | `NJ_KAENSIN` | Crimson Fire Formation | 10 | Ninja | 是 | NJ_KOUENKA Lv5 | Magic / Self |
| 536 | `NJ_BAKUENRYU` | Raging Fire Dragon | 5 | Ninja | 是 | NJ_NINPOU Lv10, NJ_KAENSIN Lv7 | Magic / Attack |
| 537 | `NJ_HYOUSENSOU` | Spear of Ice | 10 | Ninja | 是 | NJ_NINPOU Lv1 | Magic / Attack |
| 538 | `NJ_SUITON` | Hidden Water | 10 | Ninja | 是 | NJ_HYOUSENSOU Lv5 | Magic / Ground |
| 539 | `NJ_HYOUSYOURAKU` | Ice Meteor | 5 | Ninja | 是 | NJ_NINPOU Lv10, NJ_SUITON Lv7 | Magic / Self |
| 540 | `NJ_HUUJIN` | Wind Blade | 10 | Ninja | 是 | NJ_NINPOU Lv1 | Magic / Attack |
| 541 | `NJ_RAIGEKISAI` | Lightning Strike of Destruction | 5 | Ninja | 是 | NJ_HUUJIN Lv5 | Magic / Self |
| 542 | `NJ_KAMAITACHI` | Kamaitachi | 5 | Ninja | 是 | NJ_NINPOU Lv10, NJ_RAIGEKISAI Lv5 | Magic / Attack |
| 543 | `NJ_NEN` | Soul | 5 | Ninja | 是 | NJ_NINPOU Lv5 | None / Self |
| 544 | `NJ_ISSEN` | Final Strike | 10 | Ninja | 是 | NJ_TOBIDOUGU Lv7, NJ_KIRIKAGE Lv5, NJ_NEN Lv1 | Weapon / Attack |

## 技能详情

### Shuriken Training (`NJ_TOBIDOUGU`)

武器/物理技能；目标：被动；最高等级 10；段数：1。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/ninja/kunaiexplosion.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3716
ATK_ADD(wd->damage, wd->damage2, battle_get_spiritball_damage(*wd, *src, skill_id));
// src/map/battle.cpp:3721
ATK_ADD(wd->damage, wd->damage2, 15 * skill_lv);
// src/map/battle.cpp:3723
wd->damage = battle_attr_fix(src, target, wd->damage, right_element, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3726
ATK_ADD(wd->damage, wd->damage2, 4 * skill_lv);
// src/map/battle.cpp:3728
ATK_ADD(wd->damage, wd->damage2, 3 * pc_checkskill(sd, NJ_TOBIDOUGU));
// src/map/battle.cpp:3729
ATK_ADD(wd->damage, wd->damage2, sd->bonus.arrow_atk);
// src/map/battle.cpp:3732
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3736
ATK_ADD(wd->damage, wd->damage2, 3 * sd->bonus.arrow_atk);
// src/map/battle.cpp:3739
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3812
if(skill_id == TF_POISON) //Additional ATK from Envenom is treated as mastery type damage [helvetica]
// src/map/battle.cpp:3813
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, 15 * skill_lv);
// src/map/battle.cpp:3819
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, battle_get_spiritball_damage(*wd, *src, skill_id));
```

### Throw Shuriken (`NJ_SYURIKEN`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Weapon；伤害标记：IgnoreAtkCard；消耗/限制：SP 2；弹药数 1；弹药 Shuriken。

- 技能树最高等级：`10`
- 前置技能：NJ_TOBIDOUGU Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`, `src/map/skills/ninja/throwshuriken.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3716
ATK_ADD(wd->damage, wd->damage2, battle_get_spiritball_damage(*wd, *src, skill_id));
// src/map/battle.cpp:3721
ATK_ADD(wd->damage, wd->damage2, 15 * skill_lv);
// src/map/battle.cpp:3723
wd->damage = battle_attr_fix(src, target, wd->damage, right_element, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3726
ATK_ADD(wd->damage, wd->damage2, 4 * skill_lv);
// src/map/battle.cpp:3728
ATK_ADD(wd->damage, wd->damage2, 3 * pc_checkskill(sd, NJ_TOBIDOUGU));
// src/map/battle.cpp:3729
ATK_ADD(wd->damage, wd->damage2, sd->bonus.arrow_atk);
// src/map/battle.cpp:3732
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3736
ATK_ADD(wd->damage, wd->damage2, 3 * sd->bonus.arrow_atk);
// src/map/battle.cpp:3812
if(skill_id == TF_POISON) //Additional ATK from Envenom is treated as mastery type damage [helvetica]
// src/map/battle.cpp:3813
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, 15 * skill_lv);
// src/map/battle.cpp:3819
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, battle_get_spiritball_damage(*wd, *src, skill_id));
// src/map/battle.cpp:3822
ATK_ADD(wd->damage, wd->damage2, 3 * skill);
```

### Throw Kunai (`NJ_KUNAI`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：3；属性：Weapon；技能后摇：1000 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP Lv1=30; Lv2=25; Lv3=20; Lv4=15; Lv5=10；弹药数 1；弹药 Kunai。

- 技能树最高等级：`5`
- 前置技能：NJ_SYURIKEN Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`, `src/map/skills/ninja/throwkunai.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3723
wd->damage = battle_attr_fix(src, target, wd->damage, right_element, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3726
ATK_ADD(wd->damage, wd->damage2, 4 * skill_lv);
// src/map/battle.cpp:3728
ATK_ADD(wd->damage, wd->damage2, 3 * pc_checkskill(sd, NJ_TOBIDOUGU));
// src/map/battle.cpp:3729
ATK_ADD(wd->damage, wd->damage2, sd->bonus.arrow_atk);
// src/map/battle.cpp:3732
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3736
ATK_ADD(wd->damage, wd->damage2, 3 * sd->bonus.arrow_atk);
// src/map/battle.cpp:3739
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/skills/ninja/throwkunai.cpp:11
void SkillThrowKunai::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/ninja/throwkunai.cpp:13
base_skillratio += -100 + 100 * skill_lv;
```

### Throw Huuma Shuriken (`NJ_HUUMA`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1-2=-3; Lv3-4=-4; Lv5=-5；属性：Weapon；范围：1；吟唱：3000 ms；技能后摇：2000 ms；伤害标记：Splash, SplashSplit；消耗/限制：SP Lv1=20; Lv2=25; Lv3=30; Lv4=35; Lv5=40；武器 Huuma。

- 技能树最高等级：`5`
- 前置技能：NJ_TOBIDOUGU Lv5, NJ_KUNAI Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`, `src/map/skills/ninja/swirlingpetal.cpp`, `src/map/skills/ninja/throwhuumashuriken.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:3006
clif_skill_damage( *dsrc, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, -1, DMG_SPLASH ); // needs -1 as skill level
// src/map/skill.cpp:3008
clif_skill_damage( *dsrc, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, -2, DMG_SPLASH ); // needs -2(!) as skill level
// src/map/skill.cpp:3011
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, 1, skill_id, -2, DMG_SINGLE );
// src/map/skill.cpp:3020
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, skill_lv, DMG_MULTI_HIT );
// src/map/skill.cpp:3023
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, 1, WL_CHAINLIGHTNING_ATK, -2, DMG_SINGLE );
// src/map/skill.cpp:3026
clif_skill_damage( *dsrc, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, WL_TETRAVORTEX_WIND, -1, DMG_SPLASH );
// src/map/skill.cpp:3029
clif_skill_damage( *dsrc, *bl, tick, status_get_amotion(src), dmg.dmotion, damage, dmg.div_, skill_id, -1, DMG_SINGLE );
// src/map/skills/ninja/skill_factory_ninja.cpp:123
return std::make_unique<SkillCastNinjaSpell>();
// src/map/skills/ninja/swirlingpetal.cpp:11
SkillSwirlingPetal::SkillSwirlingPetal() : SkillImplRecursiveDamageSplash(KO_HUUMARANKA) {
// src/map/skills/ninja/swirlingpetal.cpp:14
void SkillSwirlingPetal::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
// src/map/skills/ninja/swirlingpetal.cpp:16
const status_change *sc = status_get_sc(src);
// src/map/skills/ninja/swirlingpetal.cpp:17
const map_session_data* sd = BL_CAST(BL_PC, src);
```

### Throw Zeny (`NJ_ZENYNAGE`)

特殊技能；目标：敌方目标；最高等级 10；射程：7；命中类型：Single；段数：1；技能后摇：5000 ms；伤害标记：IgnoreElement, IgnoreFlee；消耗/限制：SP 50；Zeny Lv1=500; Lv2=1000; Lv3=1500; Lv4=2000; Lv5=2500; Lv6=3000; Lv7=3500; Lv8=4000; Lv9=4500; Lv10=5000。

- 技能树最高等级：`10`
- 前置技能：NJ_TOBIDOUGU Lv10, NJ_HUUMA Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`, `src/map/skills/ninja/throwzeny.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1822
damage = (int64)damage*2/3; //Receive 66% damage
// src/map/battle.cpp:1824
damage /= 2; //Receive 50% damage
// src/map/battle.cpp:1829
damage = damage * 85 / 100;
// src/map/battle.cpp:1839
damage -= damage * tsc->getSCE(SC_DEFENDER)->val2 / 100;
// src/map/battle.cpp:1842
damage -= damage * 20 / 100;
// src/map/battle.cpp:6463
case CR_ACIDDEMONSTRATION:
// src/map/battle.cpp:6465
md.damage = (int32)((int64)7*tstatus->vit*sstatus->int_*sstatus->int_ / (10*(tstatus->vit+sstatus->int_)));
// src/map/battle.cpp:6467
md.damage = 0;
// src/map/battle.cpp:6469
md.damage /= 2;
// src/map/battle.cpp:6473
md.damage = skill_get_zeny( skill_id, skill_lv );
// src/map/battle.cpp:6475
if( md.damage == 0 ){
// src/map/battle.cpp:6476
md.damage = 2;
```

### Improvised Defense (`NJ_TATAMIGAESHI`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；属性：Weapon；击退：3；技能后摇：3000 ms；持续时间1：3000 ms；持续时间2：3000 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP 15；关联状态：Tatamigaeshi。

- 技能树最高等级：`5`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/ninja/improviseddefense.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2930
case NJ_TATAMIGAESHI: //For correct knockback.
// src/map/skill.cpp:2942
if (skill_lv >= 7) {
// src/map/skills/ninja/improviseddefense.cpp:13
void SkillImprovisedDefense::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/ninja/improviseddefense.cpp:14
base_skillratio += 10 * skill_lv;
// src/map/skills/ninja/improviseddefense.cpp:16
base_skillratio *= 2;
// src/map/skills/ninja/improviseddefense.cpp:20
void SkillImprovisedDefense::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/ninja/improviseddefense.cpp:21
if (skill_unitsetting(src,getSkillId(),skill_lv,src->x,src->y,0))
// src/map/skills/ninja/improviseddefense.cpp:22
sc_start(src,src,skill_get_sc(getSkillId()),100,skill_lv,skill_get_time2(getSkillId(),skill_lv));
```

### Vanishing Slash (`NJ_KASUMIKIRI`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-1；命中类型：Single；段数：1；属性：Weapon；技能后摇：1000 ms；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000; Lv6=180000; Lv7=210000; Lv8=240000; Lv9=270000; Lv10=300000 ms；消耗/限制：SP Lv1=10; Lv2=12; Lv3=14; Lv4=16; Lv5=18; Lv6=20; Lv7=22; Lv8=24; Lv9=26; Lv10=28；关联状态：Hiding。

- 技能树最高等级：`10`
- 前置技能：NJ_SHADOWJUMP Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/ninja/skill_factory_ninja.cpp`, `src/map/skills/ninja/vanishingslash.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/ninja/vanishingslash.cpp:13
void SkillVanishingSlash::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/ninja/vanishingslash.cpp:14
sc_start(src, src, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
// src/map/skills/ninja/vanishingslash.cpp:17
void SkillVanishingSlash::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/ninja/vanishingslash.cpp:19
base_skillratio += 20 * skill_lv;
// src/map/skills/ninja/vanishingslash.cpp:21
base_skillratio += 10 * skill_lv;
```

### Shadow Leap (`NJ_SHADOWJUMP`)

非伤害技能；目标：地面区域；最高等级 5；射程：Lv1=5; Lv2=6; Lv3=7; Lv4=8; Lv5=9；命中类型：Single；段数：1；技能后摇：1000 ms；伤害标记：NoDamage；消耗/限制：SP 10；前置状态 Hiding。

- 技能树最高等级：`5`
- 前置技能：NJ_TATAMIGAESHI Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/ninja/shadowleap.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2698
case NJ_KIRIKAGE: // Cast range mimics NJ_SHADOWJUMP but damage is considered melee
// src/map/battle.cpp:2699
case GC_CROSSIMPACT: // Cast range is 7 cells and player jumps to target but skill is considered melee
// src/map/battle.cpp:2700
case DK_SERVANT_W_PHANTOM: // 9 cell cast range.
// src/map/battle.cpp:2701
case SHC_SAVAGE_IMPACT: // 7 cell cast range.
// src/map/battle.cpp:2702
case SHC_FATAL_SHADOW_CROW: // 9 cell cast range.
// src/map/battle.cpp:2703
case MT_RUSH_QUAKE: // 9 cell cast range.
// src/map/battle.cpp:2704
case MT_RUSH_STRIKE: // 7 cell cast range.
// src/map/battle.cpp:2705
case ABC_UNLUCKY_RUSH: // 7 cell cast range.
// src/map/battle.cpp:2706
case ABC_CHASING_BREAK: // 7 cell cast range.
// src/map/battle.cpp:2707
case MH_THE_ONE_FIGHTER_RISES: // 7 cell cast range.
// src/map/battle.cpp:2710
case SS_SHIMIRU: // 11 cell cast range.
// src/map/skills/ninja/shadowleap.cpp:13
void SkillShadowLeap::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Shadow Slash (`NJ_KIRIKAGE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：Lv1=5; Lv2=6; Lv3=7; Lv4=8; Lv5=9；命中类型：Single；段数：1；属性：Weapon；伤害标记：Critical；消耗/限制：SP Lv1=14; Lv2=16; Lv3=18; Lv4=20; Lv5=22；前置状态 Hiding。

- 技能树最高等级：`5`
- 前置技能：NJ_KASUMIKIRI Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/ninja/shadowslash.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2698
case NJ_KIRIKAGE: // Cast range mimics NJ_SHADOWJUMP but damage is considered melee
// src/map/battle.cpp:2699
case GC_CROSSIMPACT: // Cast range is 7 cells and player jumps to target but skill is considered melee
// src/map/battle.cpp:2700
case DK_SERVANT_W_PHANTOM: // 9 cell cast range.
// src/map/battle.cpp:2701
case SHC_SAVAGE_IMPACT: // 7 cell cast range.
// src/map/battle.cpp:2702
case SHC_FATAL_SHADOW_CROW: // 9 cell cast range.
// src/map/battle.cpp:2703
case MT_RUSH_QUAKE: // 9 cell cast range.
// src/map/battle.cpp:2704
case MT_RUSH_STRIKE: // 7 cell cast range.
// src/map/battle.cpp:2705
case ABC_UNLUCKY_RUSH: // 7 cell cast range.
// src/map/battle.cpp:2706
case ABC_CHASING_BREAK: // 7 cell cast range.
// src/map/battle.cpp:2707
case MH_THE_ONE_FIGHTER_RISES: // 7 cell cast range.
// src/map/battle.cpp:2710
case SS_SHIMIRU: // 11 cell cast range.
// src/map/battle.cpp:3078
cri *= 2;
```

### Cicada Skin Sheeding (`NJ_UTSUSEMI`)

非伤害技能；目标：自身；最高等级 5；命中类型：Single；段数：1；击退：7；技能后摇：1000 ms；持续时间1：Lv1=20000; Lv2=30000; Lv3=40000; Lv4=50000; Lv5=60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=12; Lv2=15; Lv3=18; Lv4=21; Lv5=24；关联状态：Utsusemi。

- 技能树最高等级：`5`
- 前置技能：NJ_SHADOWJUMP Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/ninja/skill_factory_ninja.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:11724
val3=skill_get_blewcount(NJ_UTSUSEMI, val1); // knockback value.
// src/map/status.cpp:11735
tick /= 5; // !TODO: Reduce skill's duration. But for how long?
```

### Mirror Image (`NJ_BUNSINJYUTSU`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；吟唱：Lv1=4000; Lv2=3500; Lv3=3000; Lv4=2500; Lv5=2000; Lv6=1500; Lv7-10=1000 ms；技能后摇：1000 ms；持续时间1：Lv1=60000; Lv2=80000; Lv3=100000; Lv4=120000; Lv5=140000; Lv6=160000; Lv7=180000; Lv8=200000; Lv9=220000; Lv10=240000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=30; Lv2=32; Lv3=34; Lv4=36; Lv5=38; Lv6=40; Lv7=42; Lv8=44; Lv9=46; Lv10=48；道具 Shadow_Orb×1；关联状态：Bunsinjyutsu。

- 技能树最高等级：`10`
- 前置技能：NJ_UTSUSEMI Lv4, NJ_KIRIKAGE Lv3, NJ_NEN Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/ninja/mirrorimage.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:8677
if (status->hp < (status->hp/100)) {
// src/map/skill.cpp:8679
if (status->hp < 2) {
// src/map/skills/ninja/mirrorimage.cpp:11
void SkillMirrorImage::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/ninja/mirrorimage.cpp:13
status_change_end(target, SC_BUNSINJYUTSU); // on official recasting cancels existing mirror image [helvetica]
// src/map/skills/ninja/mirrorimage.cpp:14
StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
// src/map/skills/ninja/mirrorimage.cpp:15
status_change_end(target, SC_NEN);
// src/map/skills/ninja/skill_factory_ninja.cpp:123
return std::make_unique<SkillCastNinjaSpell>();
```

### Spirit of the Blade (`NJ_NINPOU`)

非伤害技能；目标：被动；最高等级 10；消耗/限制：SP 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:5307
sregen->hp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5322
sregen->sp = cap_value(val, 0, SHRT_MAX);
```

### Crimson Fire Petal (`NJ_KOUENKA`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Fire；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；消耗/限制：SP Lv1=18; Lv2=20; Lv3=22; Lv4=24; Lv5=26; Lv6=28; Lv7=30; Lv8=32; Lv9=34; Lv10=36。

- 技能树最高等级：`10`
- 前置技能：NJ_NINPOU Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/ninja/crimsonfirepetal.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/ninja/crimsonfirepetal.cpp:11
void SkillCrimsonFirePetal::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/ninja/crimsonfirepetal.cpp:12
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/ninja/crimsonfirepetal.cpp:14
base_skillratio -= 10;
// src/map/skills/ninja/crimsonfirepetal.cpp:16
base_skillratio += 10 * sd->spiritcharm;
// src/map/skills/ninja/crimsonfirepetal.cpp:19
void SkillCrimsonFirePetal::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/ninja/crimsonfirepetal.cpp:20
skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
```

### Crimson Fire Formation (`NJ_KAENSIN`)

魔法技能；目标：自身；最高等级 10；命中类型：Multi_Hit；段数：1；属性：Fire；吟唱：Lv1=6000; Lv2=5500; Lv3=5000; Lv4=4500; Lv5=4000; Lv6=3500; Lv7=3000; Lv8=2500; Lv9=2000; Lv10=1500 ms；技能后摇：1000 ms；持续时间1：20000 ms；消耗/限制：SP 25；道具 Flame_Stone×1。

- 技能树最高等级：`10`
- 前置技能：NJ_KOUENKA Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/ninja/crimsonfireformation.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5998
val2 = (skill_lv+1)/2 + 4;
// src/map/skill.cpp:6007
int32 ele = skill_get_ele(skill_id, skill_lv);
// src/map/skill.cpp:6252
unit_val1 = (skill_get_time(skill_id, skill_lv) / interval); //Default: 950/300 = 3 hits
// src/map/skill.cpp:6255
unit_val1 = 200 + 200*skill_lv;
// src/map/skills/ninja/crimsonfireformation.cpp:11
void SkillCrimsonFireFormation::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/ninja/crimsonfireformation.cpp:12
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/ninja/crimsonfireformation.cpp:14
base_skillratio -= 50;
// src/map/skills/ninja/crimsonfireformation.cpp:16
base_skillratio += 20 * sd->spiritcharm;
// src/map/skills/ninja/crimsonfireformation.cpp:19
void SkillCrimsonFireFormation::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Raging Fire Dragon (`NJ_BAKUENRYU`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：-3；属性：Fire；吟唱：3000 ms；技能后摇：2000 ms；持续时间1：100 ms；消耗/限制：SP Lv1=20; Lv2=25; Lv3=30; Lv4=35; Lv5=40；道具 Flame_Stone×1。

- 技能树最高等级：`5`
- 前置技能：NJ_NINPOU Lv10, NJ_KAENSIN Lv7
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/ninja/ragingfiredragon.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/ninja/ragingfiredragon.cpp:12
void SkillRagingFireDragon::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/ninja/ragingfiredragon.cpp:13
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/ninja/ragingfiredragon.cpp:15
base_skillratio += 50 + 150 * skill_lv;
// src/map/skills/ninja/ragingfiredragon.cpp:17
base_skillratio += 100 * sd->spiritcharm;
// src/map/skills/ninja/ragingfiredragon.cpp:20
void SkillRagingFireDragon::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/ninja/skill_factory_ninja.cpp:123
return std::make_unique<SkillCastNinjaSpell>();
```

### Spear of Ice (`NJ_HYOUSENSOU`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=3; Lv2=4; Lv3=5; Lv4=6; Lv5=7; Lv6=8; Lv7=9; Lv8=10; Lv9=11; Lv10=12；属性：Water；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；消耗/限制：SP Lv1=15; Lv2=18; Lv3=21; Lv4=24; Lv5=27; Lv6=30; Lv7=33; Lv8=36; Lv9=39; Lv10=42。

- 技能树最高等级：`10`
- 前置技能：NJ_NINPOU Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/ninja/skill_factory_ninja.cpp`, `src/map/skills/ninja/spearofice.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/ninja/skill_factory_ninja.cpp:123
return std::make_unique<SkillCastNinjaSpell>();
// src/map/skills/ninja/spearofice.cpp:14
void SkillSpearOfIce::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/ninja/spearofice.cpp:15
const map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/ninja/spearofice.cpp:18
const status_change *sc = status_get_sc(src);
// src/map/skills/ninja/spearofice.cpp:20
base_skillratio -= 30;
// src/map/skills/ninja/spearofice.cpp:22
base_skillratio += 2 * skill_lv;
```

### Hidden Water (`NJ_SUITON`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Water；吟唱：3000 ms；持续时间1：Lv1=15000; Lv2=20000; Lv3=25000; Lv4=30000; Lv5=35000; Lv6=40000; Lv7=45000; Lv8=50000; Lv9=55000; Lv10=60000 ms；持续时间2：Lv1=15000; Lv2=20000; Lv3=25000; Lv4=30000; Lv5=35000; Lv6=40000; Lv7=45000; Lv8=50000; Lv9=55000; Lv10=60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=15; Lv2=18; Lv3=21; Lv4=24; Lv5=27; Lv6=30; Lv7=33; Lv8=36; Lv9=39; Lv10=42；道具 Ice_Stone×1；关联状态：Suiton。

- 技能树最高等级：`10`
- 前置技能：NJ_HYOUSENSOU Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/holywater.cpp`, `src/map/skills/ninja/hiddenwater.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5998
val2 = (skill_lv+1)/2 + 4;
// src/map/skill.cpp:6007
int32 ele = skill_get_ele(skill_id, skill_lv);
// src/map/skill.cpp:6252
unit_val1 = (skill_get_time(skill_id, skill_lv) / interval); //Default: 950/300 = 3 hits
// src/map/skill.cpp:6255
unit_val1 = 200 + 200*skill_lv;
// src/map/skills/acolyte/holywater.cpp:12
void SkillHolyWater::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
// src/map/skills/acolyte/holywater.cpp:14
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/holywater.cpp:22
clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);
// src/map/skills/ninja/hiddenwater.cpp:9
void SkillHiddenWater::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/ninja/hiddenwater.cpp:13
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Ice Meteor (`NJ_HYOUSYOURAKU`)

魔法技能；目标：自身；最高等级 5；命中类型：Single；段数：1；属性：Water；吟唱：Lv1=2000; Lv2=2500; Lv3=3000; Lv4=3500; Lv5=4000 ms；技能后摇：2000 ms；持续时间1：100 ms；持续时间2：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000 ms；消耗/限制：SP Lv1=40; Lv2=45; Lv3=50; Lv4=55; Lv5=60；道具 Ice_Stone×1；关联状态：Freeze。

- 技能树最高等级：`5`
- 前置技能：NJ_NINPOU Lv10, NJ_SUITON Lv7
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/ninja/icemeteor.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/ninja/icemeteor.cpp:12
void SkillIceMeteor::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/ninja/icemeteor.cpp:13
sc_start(src,target,SC_FREEZE,(10+10*skill_lv),skill_lv,skill_get_time2(getSkillId(),skill_lv));
// src/map/skills/ninja/icemeteor.cpp:16
void SkillIceMeteor::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/ninja/icemeteor.cpp:17
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/ninja/icemeteor.cpp:19
base_skillratio += 50 * skill_lv;
// src/map/skills/ninja/icemeteor.cpp:21
base_skillratio += 100 * sd->spiritcharm;
// src/map/skills/ninja/skill_factory_ninja.cpp:123
return std::make_unique<SkillCastNinjaSpell>();
```

### Wind Blade (`NJ_HUUJIN`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2-3=2; Lv4-5=3; Lv6-7=4; Lv8-9=5; Lv10=6；属性：Wind；吟唱：Lv1=1000; Lv2=1500; Lv3=2000; Lv4=2500; Lv5=3000; Lv6=3500; Lv7=4000; Lv8=4500; Lv9=5000; Lv10=5500 ms；技能后摇：1000 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30。

- 技能树最高等级：`10`
- 前置技能：NJ_NINPOU Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/ninja/skill_factory_ninja.cpp`, `src/map/skills/ninja/windblade.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/ninja/skill_factory_ninja.cpp:123
return std::make_unique<SkillCastNinjaSpell>();
// src/map/skills/ninja/windblade.cpp:13
void SkillWindBlade::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/ninja/windblade.cpp:14
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/ninja/windblade.cpp:17
base_skillratio += 50;
// src/map/skills/ninja/windblade.cpp:20
base_skillratio += 10 * sd->spiritcharm;
```

### Lightning Strike of Destruction (`NJ_RAIGEKISAI`)

魔法技能；目标：自身；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Wind；吟唱：4000 ms；持续时间1：100 ms；消耗/限制：SP Lv1=16; Lv2=20; Lv3=24; Lv4=28; Lv5=32；道具 Wind_Stone×1。

- 技能树最高等级：`5`
- 前置技能：NJ_HUUJIN Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/ninja/lightningstrikeofdestruction.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/ninja/lightningstrikeofdestruction.cpp:13
void SkillLightningStrikeOfDestruction::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/ninja/lightningstrikeofdestruction.cpp:14
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/ninja/lightningstrikeofdestruction.cpp:17
base_skillratio += 100 * skill_lv;
// src/map/skills/ninja/lightningstrikeofdestruction.cpp:19
base_skillratio += 60 + 40 * skill_lv;
// src/map/skills/ninja/lightningstrikeofdestruction.cpp:22
base_skillratio += 20 * sd->spiritcharm;
```

### Kamaitachi (`NJ_KAMAITACHI`)

魔法技能；目标：敌方目标；最高等级 5；射程：Lv1=5; Lv2=6; Lv3=7; Lv4=8; Lv5=9；命中类型：Multi_Hit；段数：1；属性：Wind；范围：1；吟唱：4000 ms；消耗/限制：SP Lv1=24; Lv2=28; Lv3=32; Lv4=36; Lv5=40；道具 Wind_Stone×1。

- 技能树最高等级：`5`
- 前置技能：NJ_NINPOU Lv10, NJ_RAIGEKISAI Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/ninja/kamaitachi.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/ninja/kamaitachi.cpp:13
void SkillKamaitachi::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/ninja/kamaitachi.cpp:14
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/ninja/kamaitachi.cpp:16
base_skillratio += 100 * skill_lv;
// src/map/skills/ninja/kamaitachi.cpp:18
base_skillratio += 100 * sd->spiritcharm;
// src/map/skills/ninja/kamaitachi.cpp:21
void SkillKamaitachi::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Soul (`NJ_NEN`)

非伤害技能；目标：自身；最高等级 5；命中类型：Single；段数：1；吟唱：Lv1=5000; Lv2=4000; Lv3=3000; Lv4=2000; Lv5=1000 ms；持续时间1：Lv1=30000; Lv2=45000; Lv3=60000; Lv4=75000; Lv5=90000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=20; Lv2=30; Lv3=40; Lv4=50; Lv5=60；HP% -5；关联状态：Nen。

- 技能树最高等级：`5`
- 前置技能：NJ_NINPOU Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/ninja/skill_factory_ninja.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Final Strike (`NJ_ISSEN`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-5；命中类型：Single；段数：1；伤害标记：IgnoreFlee；消耗/限制：SP Lv1=55; Lv2=60; Lv3=65; Lv4=70; Lv5=75; Lv6=80; Lv7=85; Lv8=90; Lv9=95; Lv10=100。

- 技能树最高等级：`10`
- 前置技能：NJ_TOBIDOUGU Lv7, NJ_KIRIKAGE Lv5, NJ_NEN Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/ninja/finalstrike.cpp`, `src/map/skills/ninja/skill_factory_ninja.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4012
ATK_RATE(wd->equipAtk, wd->equipAtk2, 130);
// src/map/battle.cpp:4015
ATK_RATE(wd->equipAtk, wd->equipAtk2, 115);
// src/map/battle.cpp:4020
wd->damage = battle_calc_base_damage(src, sstatus, &sstatus->rhw, sc, tstatus->size, 0); //Monsters have no weight and use ATK instead
// src/map/battle.cpp:4024
wd->damage = 40 * sstatus->str + sstatus->hp * 8 * skill_lv / 100;
// src/map/battle.cpp:4025
wd->damage2 = 0;
// src/map/battle.cpp:4035
wd->damage = sd->inventory_data[index]->weight*8/100; //80% of weight
// src/map/battle.cpp:5763
battle_calc_attack_plant(&wd, src, target, skill_id, skill_lv);
// src/map/battle.cpp:5770
battle_calc_attack_left_right_hands(&wd, src, target, skill_id, skill_lv);
// src/map/battle.cpp:5779
battle_calc_attack_gvg_bg(&wd, src, target, skill_id, skill_lv);
// src/map/battle.cpp:5785
battle_calc_weapon_final_atk_modifiers(&wd, src, target, skill_id, skill_lv);
// src/map/battle.cpp:6497
md.damage = rnd_value( md.damage / 2, md.damage );
// src/map/battle.cpp:6500
md.damage /= 2;
```
