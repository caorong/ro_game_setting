# Creator 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 36 | `MC_INCCARRY` | Enlarge Weight Limit | 10 | Merchant | 否 | — | None / Passive |
| 37 | `MC_DISCOUNT` | Discount | 10 | Merchant | 否 | MC_INCCARRY Lv3 | None / Passive |
| 38 | `MC_OVERCHARGE` | Overcharge | 10 | Merchant | 否 | MC_DISCOUNT Lv3 | None / Passive |
| 39 | `MC_PUSHCART` | Pushcart | 10 | Merchant | 否 | MC_INCCARRY Lv5 | None / Passive |
| 40 | `MC_IDENTIFY` | Item Appraisal | 1 | Merchant | 否 | — | None / Self |
| 41 | `MC_VENDING` | Vending | 10 | Merchant | 否 | MC_PUSHCART Lv3 | None / Self |
| 42 | `MC_MAMMONITE` | Mammonite | 10 | Merchant | 否 | — | Weapon / Attack |
| 153 | `MC_CARTREVOLUTION` | Cart Revolution | 1 | Merchant | 否 | — | Weapon / Attack |
| 154 | `MC_CHANGECART` | Change Cart | 1 | Merchant | 否 | — | None / Self |
| 155 | `MC_LOUD` | Crazy Uproar | 1 | Merchant | 否 | — | Weapon / Self |
| 2535 | `ALL_BUYING_STORE` | Open Buying Store | 1 | Merchant | 否 | MC_VENDING Lv1 | None / Self |
| 2544 | `MC_CARTDECORATE` | Decorate Cart | 1 | Merchant | 否 | — | None / Self |
| 226 | `AM_AXEMASTERY` | Axe Mastery | 10 | Alchemist | 否 | — | Weapon / Passive |
| 227 | `AM_LEARNINGPOTION` | Potion Research | 10 | Alchemist | 否 | — | None / Passive |
| 228 | `AM_PHARMACY` | Prepare Potion | 10 | Alchemist | 否 | AM_LEARNINGPOTION Lv5 | None / Self |
| 229 | `AM_DEMONSTRATION` | Bomb | 5 | Alchemist | 否 | AM_PHARMACY Lv4 | Weapon / Ground |
| 230 | `AM_ACIDTERROR` | Acid Terror | 5 | Alchemist | 否 | AM_PHARMACY Lv5 | Weapon / Attack |
| 231 | `AM_POTIONPITCHER` | Aid Potion | 5 | Alchemist | 否 | AM_PHARMACY Lv3 | None / Support |
| 232 | `AM_CANNIBALIZE` | Summon Flora | 5 | Alchemist | 否 | AM_PHARMACY Lv6 | None / Ground |
| 233 | `AM_SPHEREMINE` | Summon Marine Sphere | 5 | Alchemist | 否 | AM_PHARMACY Lv2 | None / Ground |
| 234 | `AM_CP_WEAPON` | Alchemical Weapon | 5 | Alchemist | 否 | AM_CP_ARMOR Lv3 | Weapon / Support |
| 235 | `AM_CP_SHIELD` | Synthesized Shield | 5 | Alchemist | 否 | AM_CP_HELM Lv3 | Weapon / Support |
| 236 | `AM_CP_ARMOR` | Synthetic Armor | 5 | Alchemist | 否 | AM_CP_SHIELD Lv3 | Weapon / Support |
| 237 | `AM_CP_HELM` | Biochemical Helm | 5 | Alchemist | 否 | AM_PHARMACY Lv2 | Weapon / Support |
| 238 | `AM_BIOETHICS` | Bioethics | 1 | Alchemist | 否 | — | None / Passive |
| 243 | `AM_CALLHOMUN` | Call Homunculus | 1 | Alchemist | 否 | AM_REST Lv1 | None / Self |
| 244 | `AM_REST` | Vaporize | 1 | Alchemist | 否 | AM_BIOETHICS Lv1 | None / Self |
| 247 | `AM_RESURRECTHOMUN` | Homunculus Resurrection | 5 | Alchemist | 否 | AM_CALLHOMUN Lv1 | None / Self |
| 446 | `AM_BERSERKPITCHER` | Aid Berserk Potion | 1 | Alchemist | 否 | — | None / Support |
| 496 | `AM_TWILIGHT1` | Twilight Alchemy 1 | 1 | Alchemist | 否 | AM_PHARMACY Lv10 | None / Self |
| 497 | `AM_TWILIGHT2` | Twilight Alchemy 2 | 1 | Alchemist | 否 | AM_PHARMACY Lv10 | None / Self |
| 498 | `AM_TWILIGHT3` | Twilight Alchemy 3 | 1 | Alchemist | 否 | AM_PHARMACY Lv10 | None / Self |
| 478 | `CR_SLIMPITCHER` | Aid Condensed Potion | 10 | Creator | 是 | AM_POTIONPITCHER Lv5 | None / Ground |
| 479 | `CR_FULLPROTECTION` | Full Protection | 5 | Creator | 是 | AM_CP_WEAPON Lv5, AM_CP_SHIELD Lv5, AM_CP_ARMOR Lv5, AM_CP_HELM Lv5 | Weapon / Support |
| 490 | `CR_ACIDDEMONSTRATION` | Acid Demonstration | 10 | Creator | 是 | AM_DEMONSTRATION Lv5, AM_ACIDTERROR Lv5 | Misc / Attack |
| 491 | `CR_CULTIVATION` | Plant Cultivation | 2 | Creator | 是 | — | None / Ground |

## 技能详情

### Aid Condensed Potion (`CR_SLIMPITCHER`)

非伤害技能；目标：地面区域；最高等级 10；射程：3；命中类型：Single；段数：1；范围：3；吟唱：1000 ms；技能后摇：1000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 30；道具 Red_Slim_Potion×1, Red_Slim_Potion×1, Red_Slim_Potion×1, Red_Slim_Potion×1, Red_Slim_Potion×1, Yellow_Slim_Potion×1, Yellow_Slim_Potion×1, Yellow_Slim_Potion×1, Yellow_Slim_Potion×1, White_Slim_Potion×1。

- 技能树最高等级：`10`
- 前置技能：AM_POTIONPITCHER Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/merchant/aidcondensedpotion.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:9607
int32 pc_skillheal_bonus(map_session_data *sd, uint16 skill_id) {
// src/map/pc.cpp:9608
int32 bonus = sd->bonus.add_heal_rate;
// src/map/pc.cpp:9616
case AL_HEAL:           if( !(battle_config.skill_add_heal_rate&1) ) bonus = 0; break;
// src/map/pc.cpp:9617
case PR_SANCTUARY:      if( !(battle_config.skill_add_heal_rate&2) ) bonus = 0; break;
// src/map/pc.cpp:9618
case AM_POTIONPITCHER:  if( !(battle_config.skill_add_heal_rate&4) ) bonus = 0; break;
// src/map/pc.cpp:9619
case CR_SLIMPITCHER:    if( !(battle_config.skill_add_heal_rate&8) ) bonus = 0; break;
// src/map/pc.cpp:9620
case BA_APPLEIDUN:      if( !(battle_config.skill_add_heal_rate&16)) bonus = 0; break;
// src/map/pc.cpp:9621
case AB_CHEAL:          if (!(battle_config.skill_add_heal_rate & 32)) bonus = 0; break;
// src/map/pc.cpp:9622
case AB_HIGHNESSHEAL:   if (!(battle_config.skill_add_heal_rate & 64)) bonus = 0; break;
// src/map/pc.cpp:9623
case CD_MEDIALE_VOTUM:  if (!(battle_config.skill_add_heal_rate & 128)) bonus = 0; break;
// src/map/pc.cpp:9624
case CD_DILECTIO_HEAL:  if (!(battle_config.skill_add_heal_rate & 256)) bonus = 0; break;
// src/map/pc.cpp:9628
for (auto &it : sd->skillheal) {
```

### Full Protection (`CR_FULLPROTECTION`)

武器/物理技能；目标：友方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：Lv1=120000; Lv2=240000; Lv3=360000; Lv4=480000; Lv5=600000 ms；伤害标记：NoDamage；消耗/限制：SP 40；道具 Coating_Bottle×1。

- 技能树最高等级：`5`
- 前置技能：AM_CP_WEAPON Lv5, AM_CP_SHIELD Lv5, AM_CP_ARMOR Lv5, AM_CP_HELM Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/fullprotection.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:13092
case ITEMID_CONCENTRATED_CEROMAIN_SOUP:
// src/map/skill.cpp:13101
make_per = status->int_ + status->dex / 2 + status->luk + sd->status.job_level + (30 + rnd() % 120 + 1) + // Caster's INT + (Caster's DEX / 2) + Caster's LUK + Caster's Job Level + Random number between (30 ~ 150) +
// src/map/skill.cpp:13102
sd->status.base_level + 5 * (pc_checkskill(sd, AM_LEARNINGPOTION) - 20) + pc_checkskill(sd, CR_FULLPROTECTION) * (6 + rnd() % 4 + 1); // Caster's Base Level + (5 x (Potion Research Skill Level - 20)) + (Full Chemical Protection Skill Level x Random number between (6 ~ 10))
// src/map/skill.cpp:13104
qty = production_count[skill_lv - 1];
// src/map/skills/merchant/fullprotection.cpp:13
void SkillFullProtection::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/fullprotection.cpp:14
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/merchant/fullprotection.cpp:15
map_session_data* dstsd = BL_CAST( BL_PC, target );
// src/map/skills/merchant/fullprotection.cpp:18
int32 i_eqp, s = 0, skilltime = skill_get_time(getSkillId(),skill_lv);
// src/map/skills/merchant/skill_factory_merchant.cpp:214
case CR_ACIDDEMONSTRATION:
// src/map/skills/merchant/skill_factory_merchant.cpp:215
return std::make_unique<SkillAcidDemonstration>();
```

### Acid Demonstration (`CR_ACIDDEMONSTRATION`)

特殊技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；吟唱：1000 ms；技能后摇：1000 ms；伤害标记：IgnoreFlee；消耗/限制：SP 30；道具 Fire_Bottle×1, Acid_Bottle×1。

- 技能树最高等级：`10`
- 前置技能：AM_DEMONSTRATION Lv5, AM_ACIDTERROR Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/merchant/aciddemonstration.cpp`, `src/map/skills/merchant/fireexpansion.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1552
sc_start(target, src, SC_STUN, 50, skill_lv, skill_get_time2(skill_id, skill_lv));
// src/map/battle.cpp:1564
|| skill_id == CR_ACIDDEMONSTRATION
// src/map/battle.cpp:6454
struct Damage atk = battle_calc_weapon_attack(src, target, skill_id, skill_lv, 0);
// src/map/battle.cpp:6455
struct Damage matk = battle_calc_magic_attack(src, target, skill_id, skill_lv, 0);
// src/map/battle.cpp:6456
md.damage = 7 * ((atk.damage/skill_lv + matk.damage/skill_lv) * tstatus->vit / 100 );
// src/map/battle.cpp:6459
md.damage = battle_attr_fix(src, target, md.damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv);
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
```

### Plant Cultivation (`CR_CULTIVATION`)

非伤害技能；目标：地面区域；最高等级 2；射程：1；命中类型：Single；段数：1；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP 10；道具 Mushroom_Spore×1, Stem×1。

- 技能树最高等级：`2`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/plantcultivation.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5420
sd = BL_CAST(BL_PC, src);
// src/map/skill.cpp:5440
clif_skill_nodamage(src,*src,skill_id,skill_lv);
// src/map/skill.cpp:5442
clif_skill_poseffect( *src, skill_id, skill_lv, x, y, tick );
// src/map/skill.cpp:9886
if (i != skill_lv%11 - 1)
// src/map/skills/merchant/plantcultivation.cpp:13
void SkillPlantCultivation::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/plantcultivation.cpp:14
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/merchant/skill_factory_merchant.cpp:214
case CR_ACIDDEMONSTRATION:
// src/map/skills/merchant/skill_factory_merchant.cpp:215
return std::make_unique<SkillAcidDemonstration>();
```
