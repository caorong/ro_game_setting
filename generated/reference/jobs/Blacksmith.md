# Blacksmith 技能

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
| 94 | `BS_IRON` | Iron Tempering | 5 | Blacksmith | 是 | — | Weapon / Passive |
| 95 | `BS_STEEL` | Steel Tempering | 5 | Blacksmith | 是 | BS_IRON Lv1 | Weapon / Passive |
| 96 | `BS_ENCHANTEDSTONE` | Enchanted Stone Craft | 5 | Blacksmith | 是 | BS_IRON Lv1 | Weapon / Passive |
| 97 | `BS_ORIDEOCON` | Oridecon Research | 5 | Blacksmith | 是 | BS_ENCHANTEDSTONE Lv1 | Weapon / Passive |
| 98 | `BS_DAGGER` | Smith Dagger | 3 | Blacksmith | 是 | — | Weapon / Passive |
| 99 | `BS_SWORD` | Smith Sword | 3 | Blacksmith | 是 | BS_DAGGER Lv1 | Weapon / Passive |
| 100 | `BS_TWOHANDSWORD` | Smith Two-handed Sword | 3 | Blacksmith | 是 | BS_SWORD Lv1 | Weapon / Passive |
| 101 | `BS_AXE` | Smith Axe | 3 | Blacksmith | 是 | BS_SWORD Lv2 | Weapon / Passive |
| 102 | `BS_MACE` | Smith Mace | 3 | Blacksmith | 是 | BS_KNUCKLE Lv1 | Weapon / Passive |
| 103 | `BS_KNUCKLE` | Smith Knucklebrace | 3 | Blacksmith | 是 | BS_DAGGER Lv1 | Weapon / Passive |
| 104 | `BS_SPEAR` | Smith Spear | 3 | Blacksmith | 是 | BS_DAGGER Lv2 | Weapon / Passive |
| 105 | `BS_HILTBINDING` | Hilt Binding | 1 | Blacksmith | 是 | — | Weapon / Passive |
| 106 | `BS_FINDINGORE` | Ore Discovery | 1 | Blacksmith | 是 | BS_STEEL Lv1, BS_HILTBINDING Lv1 | Weapon / Passive |
| 107 | `BS_WEAPONRESEARCH` | Weaponry Research | 10 | Blacksmith | 是 | BS_HILTBINDING Lv1 | Weapon / Passive |
| 108 | `BS_REPAIRWEAPON` | Weapon Repair | 1 | Blacksmith | 是 | BS_WEAPONRESEARCH Lv1 | Weapon / Support |
| 109 | `BS_SKINTEMPER` | Skin Tempering | 5 | Blacksmith | 是 | — | Weapon / Passive |
| 110 | `BS_HAMMERFALL` | Hammer Fall | 5 | Blacksmith | 是 | — | Weapon / Ground |
| 111 | `BS_ADRENALINE` | Adrenaline Rush | 5 | Blacksmith | 是 | BS_HAMMERFALL Lv2 | Weapon / Self |
| 112 | `BS_WEAPONPERFECT` | Weapon Perfection | 5 | Blacksmith | 是 | BS_WEAPONRESEARCH Lv2, BS_ADRENALINE Lv2 | Weapon / Self |
| 113 | `BS_OVERTHRUST` | Power-Thrust | 5 | Blacksmith | 是 | BS_ADRENALINE Lv3 | Weapon / Self |
| 114 | `BS_MAXIMIZE` | Maximize Power | 5 | Blacksmith | 是 | BS_WEAPONPERFECT Lv3, BS_OVERTHRUST Lv2 | Weapon / Self |
| 1012 | `BS_UNFAIRLYTRICK` | Unfair Trick | 1 | Blacksmith | 是 | — | Weapon / Passive |
| 1013 | `BS_GREED` | Greed | 1 | Blacksmith | 是 | — | Weapon / Self |
| 459 | `BS_ADRENALINE2` | Advanced Adrenaline Rush | 1 | Blacksmith | 是 | BS_ADRENALINE Lv5 | Weapon / Self |

## 技能详情

### Iron Tempering (`BS_IRON`)

武器/物理技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:13436
case ASC_CDP: //25% Damage yourself, and display same effect as failed potion.
// src/map/skill.cpp:13437
status_percent_damage(nullptr, sd, -25, 0, true);
```

### Steel Tempering (`BS_STEEL`)

武器/物理技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：BS_IRON Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:13437
status_percent_damage(nullptr, sd, -25, 0, true);
```

### Enchanted Stone Craft (`BS_ENCHANTEDSTONE`)

武器/物理技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：BS_IRON Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:13462
int32 rate = rnd() % 1000 + 1;
```

### Oridecon Research (`BS_ORIDEOCON`)

武器/物理技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：BS_ENCHANTEDSTONE Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Smith Dagger (`BS_DAGGER`)

武器/物理技能；目标：被动；最高等级 3。

- 技能树最高等级：`3`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Smith Sword (`BS_SWORD`)

武器/物理技能；目标：被动；最高等级 3。

- 技能树最高等级：`3`
- 前置技能：BS_DAGGER Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Smith Two-handed Sword (`BS_TWOHANDSWORD`)

武器/物理技能；目标：被动；最高等级 3。

- 技能树最高等级：`3`
- 前置技能：BS_SWORD Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Smith Axe (`BS_AXE`)

武器/物理技能；目标：被动；最高等级 3。

- 技能树最高等级：`3`
- 前置技能：BS_SWORD Lv2
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Smith Mace (`BS_MACE`)

武器/物理技能；目标：被动；最高等级 3。

- 技能树最高等级：`3`
- 前置技能：BS_KNUCKLE Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Smith Knucklebrace (`BS_KNUCKLE`)

武器/物理技能；目标：被动；最高等级 3。

- 技能树最高等级：`3`
- 前置技能：BS_DAGGER Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Smith Spear (`BS_SPEAR`)

武器/物理技能；目标：被动；最高等级 3。

- 技能树最高等级：`3`
- 前置技能：BS_DAGGER Lv2
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Hilt Binding (`BS_HILTBINDING`)

武器/物理技能；目标：被动；最高等级 1。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3804
wd->damage2 = battle_addmastery(sd,target,wd->damage2,1);
// src/map/battle.cpp:3812
if(skill_id == TF_POISON) //Additional ATK from Envenom is treated as mastery type damage [helvetica]
// src/map/battle.cpp:3813
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, 15 * skill_lv);
// src/map/battle.cpp:3819
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, battle_get_spiritball_damage(*wd, *src, skill_id));
// src/map/battle.cpp:3822
ATK_ADD(wd->damage, wd->damage2, 3 * skill);
// src/map/battle.cpp:5715
wd.damage = 0;
// src/map/battle.cpp:5724
ATK_ADD(wd.damage, wd.damage2, skill * 2);
// src/map/battle.cpp:5726
ATK_ADD(wd.damage, wd.damage2, 50 * skill_lv);
// src/map/battle.cpp:5728
ATK_ADD(wd.damage, wd.damage2, 4);
// src/map/battle.cpp:5735
wd.damage = wd.damage * (100 + sd->bonus.long_attack_atk_rate) / 100;
// src/map/battle.cpp:5737
wd.damage2 = wd.damage2 * (100 + sd->bonus.long_attack_atk_rate) / 100;
// src/map/status.cpp:4355
if(battle_config.hp_rate != 100)
```

### Ore Discovery (`BS_FINDINGORE`)

武器/物理技能；目标：被动；最高等级 1。

- 技能树最高等级：`1`
- 前置技能：BS_STEEL Lv1, BS_HILTBINDING Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/mob.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/mob.cpp:3346
if (first_sd != nullptr && entry->rate <= battle_config.rare_drop_announce) {
// src/map/mob.cpp:3348
sprintf(message, msg_txt(nullptr, 541), first_sd->status.name, md->name, it->ename.c_str(), (float)drop_rate / 100);
// src/map/mob.cpp:3350
intif_broadcast(message, strlen(message) + 1, BC_DEFAULT);
// src/map/mob.cpp:3354
mob_item_drop(md, dlist, ditem, 0, battle_config.autoloot_adjust ? drop_rate : entry->rate, homkillonly || merckillonly);
// src/map/mob.cpp:3364
mobdrop->rate = entry->adj_rate;
// src/map/mob.cpp:3368
mob_item_drop(md, dlist, ditem, 0, mobdrop->rate, homkillonly || merckillonly);
```

### Weaponry Research (`BS_WEAPONRESEARCH`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：BS_HILTBINDING Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2298
damage += (skill * 10);
// src/map/battle.cpp:2300
damage += (15 * pc_checkskill(sd, NC_MADOLICENCE)); // Attack bonus is granted even without the Madogear
// src/map/battle.cpp:2303
damage += (skill * 4);
// src/map/battle.cpp:2305
damage += sd->status.str;
// src/map/battle.cpp:2311
damage += (skill * 2);
// src/map/battle.cpp:2315
damage += 15 * skill + (skill > 4 ? 25 : 0);
// src/map/battle.cpp:3295
skill->impl->modifyHitRate(hitrate, src, target, skill_lv);
// src/map/battle.cpp:3297
} else if (sd && wd->type&DMG_MULTI_HIT && wd->div_ == 2) // +1 hit per level of Double Attack on a successful double attack (making sure other multi attack skills do not trigger this) [helvetica]
// src/map/battle.cpp:3298
hitrate += pc_checkskill(sd,TF_DOUBLE);
// src/map/battle.cpp:3305
hitrate += hitrate * ( 2 * skill ) / 100;
// src/map/battle.cpp:3309
hitrate += 3 * skill;
// src/map/battle.cpp:3312
hitrate = cap_value(hitrate, battle_config.min_hitrate, battle_config.max_hitrate);
```

### Weapon Repair (`BS_REPAIRWEAPON`)

武器/物理技能；目标：友方目标；最高等级 1；射程：2；命中类型：Single；段数：1；吟唱：7500 ms；伤害标记：NoDamage；消耗/限制：SP 30。

- 技能树最高等级：`1`
- 前置技能：BS_WEAPONRESEARCH Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/skills/merchant/weaponrepair.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:9351
switch( sd.menuskill_id ) { // Cast start or cast end??
// src/map/skills/merchant/skill_factory_merchant.cpp:214
case CR_ACIDDEMONSTRATION:
// src/map/skills/merchant/skill_factory_merchant.cpp:215
return std::make_unique<SkillAcidDemonstration>();
// src/map/skills/merchant/weaponrepair.cpp:12
void SkillWeaponRepair::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/weaponrepair.cpp:13
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/weaponrepair.cpp:14
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/merchant/weaponrepair.cpp:17
clif_item_repair_list( *sd, *dstsd, skill_lv );
```

### Skin Tempering (`BS_SKINTEMPER`)

武器/物理技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:4666
if(sd->dsprate < 0)
// src/map/status.cpp:4667
sd->dsprate = 0;
// src/map/status.cpp:4668
if(sd->castrate < 0)
// src/map/status.cpp:4669
sd->castrate = 0;
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
```

### Hammer Fall (`BS_HAMMERFALL`)

武器/物理技能；目标：地面区域；最高等级 5；射程：1；命中类型：Single；段数：1；范围：Lv1-5=2; Lv6=12；持续时间2：5000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 10；武器 Dagger, 1hSword, 1hAxe, 2hAxe, Mace；关联状态：Stun。

- 技能树最高等级：`5`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/hammerfall.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:3748
sc_start(src, target, SC_SILENCE, skl->type, skl->skill_lv, skill_get_time2(status_db.getSkill(SC_SILENCE), 1));
// src/map/skill.cpp:3751
sc_start(src, target, SC_SILENCE, skl->type, skl->skill_lv, skill_get_time2(skl->skill_id, skl->skill_lv));
// src/map/skill.cpp:3754
sc_start(src, target, SC_BLIND, skl->type, skl->skill_lv, skill_get_time2(skl->skill_id, skl->skill_lv));
// src/map/skill.cpp:3757
sc_start(src, target, SC_STUN, skl->type, skl->skill_lv, skill_get_time2(skl->skill_id, skl->skill_lv));
// src/map/skill.cpp:3760
sc_start(src, target, SC_SILENCE, skl->type, skl->skill_lv, skill_get_time2(skl->skill_id, skl->skill_lv));
// src/map/skill.cpp:3767
layout = skill_get_unit_layout(skl->skill_id, skl->skill_lv, src, skl->x, skl->y);
// src/map/skills/merchant/hammerfall.cpp:9
void SkillHammerFall::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/hammerfall.cpp:10
skill_addtimerskill(src, tick+1000, target->id, 0, 0, getSkillId(), skill_lv, min(20+10*skill_lv, 50+5*skill_lv), flag);
// src/map/skills/merchant/hammerfall.cpp:13
void SkillHammerFall::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/hammerfall.cpp:14
int32 i = skill_get_splash(getSkillId(), skill_lv);
// src/map/skills/merchant/hammerfall.cpp:17
src, getSkillId(), skill_lv, tick, flag|BCT_ENEMY|2,
// src/map/skills/merchant/hammerfall.cpp:18
skill_castend_nodamage_id);
```

### Adrenaline Rush (`BS_ADRENALINE`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=20; Lv2=23; Lv3=26; Lv4=29; Lv5=32；武器 1hAxe, 2hAxe, Mace；关联状态：Adrenaline。

- 技能树最高等级：`5`
- 前置技能：BS_HAMMERFALL Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/adrenalinerush.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/adrenalinerush.cpp:13
void SkillAdrenalineRush::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/adrenalinerush.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/adrenalinerush.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/merchant/adrenalinerush.cpp:20
clif_skill_nodamage(target, *target, getSkillId(), skill_lv,
// src/map/skills/merchant/adrenalinerush.cpp:21
sc_start2(src, target, skill_get_sc(getSkillId()), 100, skill_lv, (src == target) ? 1 : 0, skill_get_time(getSkillId(), skill_lv)));
```

### Weapon Perfection (`BS_WEAPONPERFECT`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；持续时间1：Lv1=10000; Lv2=20000; Lv3=30000; Lv4=40000; Lv5=50000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=18; Lv2=16; Lv3=14; Lv4=12; Lv5=10；关联状态：WeaponPerfection。

- 技能树最高等级：`5`
- 前置技能：BS_WEAPONRESEARCH Lv2, BS_ADRENALINE Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/skills/merchant/weaponperfection.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/skill_factory_merchant.cpp:214
case CR_ACIDDEMONSTRATION:
// src/map/skills/merchant/skill_factory_merchant.cpp:215
return std::make_unique<SkillAcidDemonstration>();
// src/map/skills/merchant/weaponperfection.cpp:13
void SkillWeaponPerfection::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/weaponperfection.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/weaponperfection.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/merchant/weaponperfection.cpp:20
clif_skill_nodamage(target, *target, getSkillId(), skill_lv,
// src/map/skills/merchant/weaponperfection.cpp:21
sc_start2(src, target, skill_get_sc(getSkillId()), 100, skill_lv, (src == target) ? 1 : 0, skill_get_time(getSkillId(), skill_lv)));
```

### Power-Thrust (`BS_OVERTHRUST`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；持续时间1：Lv1=20000; Lv2=40000; Lv3=60000; Lv4=80000; Lv5=100000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=18; Lv2=16; Lv3=14; Lv4=12; Lv5=10；武器 Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Bow, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma, 2hStaff；关联状态：Overthrust。

- 技能树最高等级：`5`
- 前置技能：BS_ADRENALINE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/powerthrust.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/powerthrust.cpp:13
void SkillPowerThrust::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/powerthrust.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/powerthrust.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/merchant/powerthrust.cpp:20
clif_skill_nodamage(target, *target, getSkillId(), skill_lv,
// src/map/skills/merchant/powerthrust.cpp:21
sc_start2(src, target, skill_get_sc(getSkillId()), 100, skill_lv, (src == target) ? 1 : 0, skill_get_time(getSkillId(), skill_lv)));
// src/map/skills/merchant/skill_factory_merchant.cpp:214
case CR_ACIDDEMONSTRATION:
// src/map/skills/merchant/skill_factory_merchant.cpp:215
return std::make_unique<SkillAcidDemonstration>();
```

### Maximize Power (`BS_MAXIMIZE`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：Lv1=1000; Lv2=2000; Lv3=3000; Lv4=4000; Lv5=5000 ms；伤害标记：NoDamage；消耗/限制：SP 10；关联状态：MaximizePower。

- 技能树最高等级：`5`
- 前置技能：BS_WEAPONPERFECT Lv3, BS_OVERTHRUST Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/skill_factory_merchant.cpp:214
case CR_ACIDDEMONSTRATION:
// src/map/skills/merchant/skill_factory_merchant.cpp:215
return std::make_unique<SkillAcidDemonstration>();
```

### Unfair Trick (`BS_UNFAIRLYTRICK`)

武器/物理技能；目标：被动；最高等级 1。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Greed (`BS_GREED`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；范围：2；技能后摇：1000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 10。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skills/merchant/greed.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/greed.cpp:12
void SkillGreed::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/greed.cpp:13
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/greed.cpp:16
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/merchant/greed.cpp:18
skill_get_splash(getSkillId(), skill_lv),BL_ITEM,target);
// src/map/skills/merchant/skill_factory_merchant.cpp:214
case CR_ACIDDEMONSTRATION:
```

### Advanced Adrenaline Rush (`BS_ADRENALINE2`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；范围：-1；持续时间1：150000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 64；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar；关联状态：Adrenaline2。

- 技能树最高等级：`1`
- 前置技能：BS_ADRENALINE Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/advancedadrenalinerush.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/advancedadrenalinerush.cpp:13
void SkillAdvancedAdrenalineRush::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/advancedadrenalinerush.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/advancedadrenalinerush.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/merchant/advancedadrenalinerush.cpp:20
clif_skill_nodamage(target, *target, getSkillId(), skill_lv,
// src/map/skills/merchant/advancedadrenalinerush.cpp:21
sc_start2(src, target, skill_get_sc(getSkillId()), 100, skill_lv, (src == target) ? 1 : 0, skill_get_time(getSkillId(), skill_lv)));
```
