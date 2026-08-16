# Whitesmith 技能

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
| 94 | `BS_IRON` | Iron Tempering | 5 | Blacksmith | 否 | — | Weapon / Passive |
| 95 | `BS_STEEL` | Steel Tempering | 5 | Blacksmith | 否 | BS_IRON Lv1 | Weapon / Passive |
| 96 | `BS_ENCHANTEDSTONE` | Enchanted Stone Craft | 5 | Blacksmith | 否 | BS_IRON Lv1 | Weapon / Passive |
| 97 | `BS_ORIDEOCON` | Oridecon Research | 5 | Blacksmith | 否 | BS_ENCHANTEDSTONE Lv1 | Weapon / Passive |
| 98 | `BS_DAGGER` | Smith Dagger | 3 | Blacksmith | 否 | — | Weapon / Passive |
| 99 | `BS_SWORD` | Smith Sword | 3 | Blacksmith | 否 | BS_DAGGER Lv1 | Weapon / Passive |
| 100 | `BS_TWOHANDSWORD` | Smith Two-handed Sword | 3 | Blacksmith | 否 | BS_SWORD Lv1 | Weapon / Passive |
| 101 | `BS_AXE` | Smith Axe | 3 | Blacksmith | 否 | BS_SWORD Lv2 | Weapon / Passive |
| 102 | `BS_MACE` | Smith Mace | 3 | Blacksmith | 否 | BS_KNUCKLE Lv1 | Weapon / Passive |
| 103 | `BS_KNUCKLE` | Smith Knucklebrace | 3 | Blacksmith | 否 | BS_DAGGER Lv1 | Weapon / Passive |
| 104 | `BS_SPEAR` | Smith Spear | 3 | Blacksmith | 否 | BS_DAGGER Lv2 | Weapon / Passive |
| 105 | `BS_HILTBINDING` | Hilt Binding | 1 | Blacksmith | 否 | — | Weapon / Passive |
| 106 | `BS_FINDINGORE` | Ore Discovery | 1 | Blacksmith | 否 | BS_STEEL Lv1, BS_HILTBINDING Lv1 | Weapon / Passive |
| 107 | `BS_WEAPONRESEARCH` | Weaponry Research | 10 | Blacksmith | 否 | BS_HILTBINDING Lv1 | Weapon / Passive |
| 108 | `BS_REPAIRWEAPON` | Weapon Repair | 1 | Blacksmith | 否 | BS_WEAPONRESEARCH Lv1 | Weapon / Support |
| 109 | `BS_SKINTEMPER` | Skin Tempering | 5 | Blacksmith | 否 | — | Weapon / Passive |
| 110 | `BS_HAMMERFALL` | Hammer Fall | 5 | Blacksmith | 否 | — | Weapon / Ground |
| 111 | `BS_ADRENALINE` | Adrenaline Rush | 5 | Blacksmith | 否 | BS_HAMMERFALL Lv2 | Weapon / Self |
| 112 | `BS_WEAPONPERFECT` | Weapon Perfection | 5 | Blacksmith | 否 | BS_WEAPONRESEARCH Lv2, BS_ADRENALINE Lv2 | Weapon / Self |
| 113 | `BS_OVERTHRUST` | Power-Thrust | 5 | Blacksmith | 否 | BS_ADRENALINE Lv3 | Weapon / Self |
| 114 | `BS_MAXIMIZE` | Maximize Power | 5 | Blacksmith | 否 | BS_WEAPONPERFECT Lv3, BS_OVERTHRUST Lv2 | Weapon / Self |
| 1012 | `BS_UNFAIRLYTRICK` | Unfair Trick | 1 | Blacksmith | 否 | — | Weapon / Passive |
| 1013 | `BS_GREED` | Greed | 1 | Blacksmith | 否 | — | Weapon / Self |
| 459 | `BS_ADRENALINE2` | Advanced Adrenaline Rush | 1 | Blacksmith | 否 | BS_ADRENALINE Lv5 | Weapon / Self |
| 384 | `WS_MELTDOWN` | Shattering Strike | 10 | Whitesmith | 是 | BS_SKINTEMPER Lv3, BS_HILTBINDING Lv1, BS_WEAPONRESEARCH Lv5, BS_OVERTHRUST Lv3 | Weapon / Self |
| 387 | `WS_CARTBOOST` | Cart Boost | 1 | Whitesmith | 是 | MC_PUSHCART Lv5, MC_CARTREVOLUTION Lv1, MC_CHANGECART Lv1, BS_HILTBINDING Lv1 | Weapon / Self |
| 477 | `WS_WEAPONREFINE` | Upgrade Weapon | 10 | Whitesmith | 是 | BS_WEAPONRESEARCH Lv10 | Weapon / Self |
| 485 | `WS_CARTTERMINATION` | Cart Termination | 10 | Whitesmith | 是 | MC_MAMMONITE Lv10, BS_HAMMERFALL Lv5, WS_CARTBOOST Lv1 | Weapon / Attack |
| 486 | `WS_OVERTHRUSTMAX` | Maximum Power Thrust | 5 | Whitesmith | 是 | BS_OVERTHRUST Lv5 | Weapon / Self |

## 技能详情

### Shattering Strike (`WS_MELTDOWN`)

武器/物理技能；目标：自身；最高等级 10；段数：1；吟唱：Lv1-2=500; Lv3-4=600; Lv5-6=700; Lv7-8=800; Lv9=900; Lv10=1000 ms；持续时间1：Lv1=15000; Lv2=20000; Lv3=25000; Lv4=30000; Lv5=35000; Lv6=40000; Lv7=45000; Lv8=50000; Lv9=55000; Lv10=60000 ms；持续时间2：5000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-2=50; Lv3-4=60; Lv5-6=70; Lv7-8=80; Lv9-10=90；关联状态：Meltdown。

- 技能树最高等级：`10`
- 前置技能：BS_SKINTEMPER Lv3, BS_HILTBINDING Lv1, BS_WEAPONRESEARCH Lv5, BS_OVERTHRUST Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:1940
- rate goes from 0 to 10000 (100.00%)
// src/map/skill.cpp:1944
int32 skill_break_equip(block_list *src, block_list *bl, uint16 where, int32 rate, int32 flag)
// src/map/skill.cpp:1946
status_change *src_sc = status_get_sc(src);
// src/map/skill.cpp:1956
status_change *sc = status_get_sc(bl);
// src/map/skill.cpp:1959
sd = BL_CAST(BL_PC, bl);
```

### Cart Boost (`WS_CARTBOOST`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：60000 ms；伤害标记：NoDamage；消耗/限制：SP 20；状态 Cart；关联状态：CartBoost。

- 技能树最高等级：`1`
- 前置技能：MC_PUSHCART Lv5, MC_CARTREVOLUTION Lv1, MC_CHANGECART Lv1, BS_HILTBINDING Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/skill_factory_merchant.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Upgrade Weapon (`WS_WEAPONREFINE`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 5。

- 技能树最高等级：`10`
- 前置技能：BS_WEAPONRESEARCH Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/skills/merchant/upgradeweapon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/upgradeweapon.cpp:12
void SkillUpgradeWeapon::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/upgradeweapon.cpp:13
map_session_data* sd = BL_CAST( BL_PC, src );
```

### Cart Termination (`WS_CARTTERMINATION`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-2；命中类型：Single；段数：1；属性：Weapon；持续时间2：5000 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP 15；Zeny Lv1=600; Lv2=700; Lv3=800; Lv4=900; Lv5=1000; Lv6=1100; Lv7=1200; Lv8=1300; Lv9=1400; Lv10=1500；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；前置状态 Cartboost；关联状态：Stun。

- 技能树最高等级：`10`
- 前置技能：MC_MAMMONITE Lv10, BS_HAMMERFALL Lv5, WS_CARTBOOST Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/merchant/carttermination.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1580
status_change_end(target, SC_LIGHTNINGWALK);
// src/map/battle.cpp:1591
clif_skill_nodamage(target, *target, LK_PARRYING, sce->val1);
// src/map/battle.cpp:1592
unit_set_attackdelay(*target, gettick(), DELAY_EVENT_PARRY);
// src/map/battle.cpp:1601
clif_skill_nodamage(target, *target, TK_DODGE, 1);
// src/map/battle.cpp:1602
sc_start4(src, target, SC_COMBO, 100, TK_JUMPKICK, src->id, 1, 0, 2000);
// src/map/battle.cpp:1870
damage = damage * 80 / 100; // 20% reduction to all type attacks
// src/map/battle.cpp:1873
damage -= damage * 90 / 100;
// src/map/battle.cpp:1877
damage /= tsc->getSCE(SC_ARMOR)->val2;
// src/map/battle.cpp:1888
int32 per = 100*status->sp / status->max_sp -1; //100% should be counted as the 80~99% interval
// src/map/battle.cpp:1889
per /=20; //Uses 20% SP intervals.
// src/map/battle.cpp:1892
status_change_end(bl, SC_ENERGYCOAT);
// src/map/battle.cpp:1893
damage -= damage * 6 * (1 + per) / 100; //Reduction: 6% + 6% every 20%
```

### Maximum Power Thrust (`WS_OVERTHRUSTMAX`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 15；Zeny Lv1=3000; Lv2=3500; Lv3=4000; Lv4=4500; Lv5=5000；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；关联状态：MaxOverThrust。

- 技能树最高等级：`5`
- 前置技能：BS_OVERTHRUST Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/skill_factory_merchant.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。
