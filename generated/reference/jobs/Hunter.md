# Hunter 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 43 | `AC_OWL` | Owl's Eye | 10 | Archer | 否 | — | None / Passive |
| 44 | `AC_VULTURE` | Vulture's Eye | 10 | Archer | 否 | AC_OWL Lv3 | None / Passive |
| 45 | `AC_CONCENTRATION` | Improve Concentration | 10 | Archer | 否 | AC_VULTURE Lv1 | Weapon / Self |
| 46 | `AC_DOUBLE` | Double Strafe | 10 | Archer | 否 | — | Weapon / Attack |
| 47 | `AC_SHOWER` | Arrow Shower | 10 | Archer | 否 | AC_DOUBLE Lv5 | Weapon / Ground |
| 147 | `AC_MAKINGARROW` | Arrow Crafting | 1 | Archer | 否 | — | Weapon / Self |
| 148 | `AC_CHARGEARROW` | Arrow Repel | 1 | Archer | 否 | — | Weapon / Attack |
| 115 | `HT_SKIDTRAP` | Skid Trap | 5 | Hunter | 是 | — | Misc / Ground |
| 116 | `HT_LANDMINE` | Land Mine | 5 | Hunter | 是 | — | Misc / Ground |
| 117 | `HT_ANKLESNARE` | Ankle Snare | 5 | Hunter | 是 | HT_SKIDTRAP Lv1 | Misc / Ground |
| 118 | `HT_SHOCKWAVE` | Shockwave Trap | 5 | Hunter | 是 | HT_ANKLESNARE Lv1 | Misc / Ground |
| 119 | `HT_SANDMAN` | Sandman | 5 | Hunter | 是 | HT_FLASHER Lv1 | Misc / Ground |
| 120 | `HT_FLASHER` | Flasher | 5 | Hunter | 是 | HT_SKIDTRAP Lv1 | Misc / Ground |
| 121 | `HT_FREEZINGTRAP` | Freezing Trap | 5 | Hunter | 是 | HT_FLASHER Lv1 | Weapon / Ground |
| 122 | `HT_BLASTMINE` | Blast Mine | 5 | Hunter | 是 | HT_LANDMINE Lv1, HT_SANDMAN Lv1, HT_FREEZINGTRAP Lv1 | Misc / Ground |
| 123 | `HT_CLAYMORETRAP` | Claymore Trap | 5 | Hunter | 是 | HT_SHOCKWAVE Lv1, HT_BLASTMINE Lv1 | Misc / Ground |
| 124 | `HT_REMOVETRAP` | Remove Trap | 1 | Hunter | 是 | HT_LANDMINE Lv1 | Misc / Trap |
| 125 | `HT_TALKIEBOX` | Talkie Box | 1 | Hunter | 是 | HT_SHOCKWAVE Lv1, HT_REMOVETRAP Lv1 | Misc / Ground |
| 126 | `HT_BEASTBANE` | Beast Bane | 10 | Hunter | 是 | — | Weapon / Passive |
| 127 | `HT_FALCON` | Falconry Mastery | 1 | Hunter | 是 | HT_BEASTBANE Lv1 | Misc / Passive |
| 128 | `HT_STEELCROW` | Steel Crow | 10 | Hunter | 是 | HT_BLITZBEAT Lv5 | Misc / Passive |
| 129 | `HT_BLITZBEAT` | Blitz Beat | 5 | Hunter | 是 | HT_FALCON Lv1 | Misc / Attack |
| 130 | `HT_DETECTING` | Detect | 4 | Hunter | 是 | AC_CONCENTRATION Lv1, HT_FALCON Lv1 | Misc / Ground |
| 131 | `HT_SPRINGTRAP` | Spring Trap | 5 | Hunter | 是 | HT_REMOVETRAP Lv1, HT_FALCON Lv1 | Misc / Trap |
| 1009 | `HT_PHANTASMIC` | Phantasmic Arrow | 1 | Hunter | 是 | — | Weapon / Attack |
| 499 | `HT_POWER` | Beast Strafing | 1 | Hunter | 是 | AC_DOUBLE Lv10 | Weapon / Attack |

## 技能详情

### Skid Trap (`HT_SKIDTRAP`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；击退：Lv1=6; Lv2=7; Lv3=8; Lv4=9; Lv5=10；持续时间1：Lv1=300000; Lv2=240000; Lv3=180000; Lv4=120000; Lv5=60000 ms；伤害标记：NoDamage；消耗/限制：SP 10；道具 Booby_Trap×1。

- 技能树最高等级：`5`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/skidtrap.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5838
val1=skill_lv+2;
// src/map/skill.cpp:5841
case AM_DEMONSTRATION:
// src/map/skill.cpp:9914
if( itemdb_group.item_exists(IG_GEMSTONE, skill->require.itemid[i]) && (sd->special_state.no_gemstone == 2 || skill_check_pc_partner(sd,skill_id,&skill_lv, 1, 2)) )
// src/map/skills/archer/skidtrap.cpp:9
void SkillSkidTrap::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/skidtrap.cpp:13
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Land Mine (`HT_LANDMINE`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；属性：Earth；持续时间1：Lv1=200000; Lv2=160000; Lv3=120000; Lv4=80000; Lv5=40000 ms；持续时间2：5000 ms；伤害标记：IgnoreFlee, IgnoreDefCard；消耗/限制：SP 10；道具 Booby_Trap×1；关联状态：Stun。

- 技能树最高等级：`5`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/landmine.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6345
md.damage = 50;
// src/map/battle.cpp:6347
md.damage = 30;
// src/map/battle.cpp:6351
md.damage = 10000;
// src/map/battle.cpp:6358
md.damage = (int64)(skill_lv * sstatus->dex * (3.0 + (float)status_get_lv(src) / 100.0) * (1.0 + (float)sstatus->int_ / 35.0));
// src/map/battle.cpp:6359
md.damage += md.damage * (rnd()%20 - 10) / 100;
// src/map/battle.cpp:6360
md.damage += (sd ? pc_checkskill(sd,RA_RESEARCHTRAP) * 40 : 0);
// src/map/battle.cpp:6365
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex + 75.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6368
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex / 2.0 + 50.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6371
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex / 2.0 + 75.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/skill.cpp:3075
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, (flag&SD_LEVEL) ? -1 : skill_lv, DMG_SPLASH );
// src/map/skill.cpp:3076
if( dsrc != src ) // avoid damage display redundancy
// src/map/skill.cpp:3080
clif_skill_damage( *dsrc, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, -1, dmg_type );
```

### Ankle Snare (`HT_ANKLESNARE`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；持续时间1：Lv1=250000; Lv2=200000; Lv3=150000; Lv4=100000; Lv5=50000 ms；持续时间2：Lv1=4000; Lv2=8000; Lv3=12000; Lv4=16000; Lv5=20000 ms；伤害标记：NoDamage；消耗/限制：SP 12；道具 Booby_Trap×1；关联状态：Ankle。

- 技能树最高等级：`5`
- 前置技能：HT_SKIDTRAP Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/anklesnare.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5838
val1=skill_lv+2;
// src/map/skill.cpp:5841
case AM_DEMONSTRATION:
// src/map/skill.cpp:6225
continue; // no path between cell and caster
// src/map/skill.cpp:11795
status_change_end(target, SC_ANKLE);
// src/map/skills/archer/anklesnare.cpp:9
void SkillAnkleSnare::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/anklesnare.cpp:13
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Shockwave Trap (`HT_SHOCKWAVE`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；持续时间1：Lv1=200000; Lv2=160000; Lv3=120000; Lv4=80000; Lv5=40000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 45；道具 Booby_Trap×2。

- 技能树最高等级：`5`
- 前置技能：HT_ANKLESNARE Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/shockwavetrap.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5841
case AM_DEMONSTRATION:
// src/map/skill.cpp:6225
continue; // no path between cell and caster
// src/map/skills/archer/shockwavetrap.cpp:11
void SkillShockwaveTrap::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/shockwavetrap.cpp:15
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/archer/shockwavetrap.cpp:18
void SkillShockwaveTrap::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/archer/shockwavetrap.cpp:19
status_percent_damage(src, target, 0, -(15*skill_lv+5), false);
```

### Sandman (`HT_SANDMAN`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；范围：2；持续时间1：Lv1=150000; Lv2=120000; Lv3=90000; Lv4=60000; Lv5=30000 ms；持续时间2：30000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 12；道具 Booby_Trap×1；关联状态：Sleep。

- 技能树最高等级：`5`
- 前置技能：HT_FLASHER Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/sandman.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5841
case AM_DEMONSTRATION:
// src/map/skill.cpp:6225
continue; // no path between cell and caster
// src/map/skills/archer/sandman.cpp:11
void SkillSandman::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/sandman.cpp:15
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/archer/sandman.cpp:18
void SkillSandman::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/archer/sandman.cpp:19
sc_start(src, target, SC_SLEEP, (10 * skill_lv + 40), skill_lv, skill_get_time2(getSkillId(), skill_lv), 1000);
```

### Flasher (`HT_FLASHER`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；持续时间1：Lv1=150000; Lv2=120000; Lv3=90000; Lv4=60000; Lv5=30000 ms；持续时间2：30000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 12；道具 Booby_Trap×1；关联状态：Blind。

- 技能树最高等级：`5`
- 前置技能：HT_SKIDTRAP Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/flasher.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:3060
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, GN_SLINGITEM, -2, DMG_SINGLE );
// src/map/skill.cpp:3063
clif_skill_damage( *dsrc, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, -1, (flag&1) ? DMG_MULTI_HIT : DMG_SPLASH );
// src/map/skill.cpp:3066
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, WM_SEVERE_RAINSTORM, -2, DMG_SPLASH );
// src/map/skill.cpp:3075
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, (flag&SD_LEVEL) ? -1 : skill_lv, DMG_SPLASH );
// src/map/skill.cpp:3076
if( dsrc != src ) // avoid damage display redundancy
// src/map/skill.cpp:3080
clif_skill_damage( *dsrc, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, -1, dmg_type );
// src/map/skill.cpp:6225
continue; // no path between cell and caster
// src/map/skills/archer/flasher.cpp:11
void SkillFlasher::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/flasher.cpp:15
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/archer/flasher.cpp:18
void SkillFlasher::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/archer/flasher.cpp:19
sc_start(src, target, SC_BLIND, 100, skill_lv, skill_get_time2(getSkillId(), skill_lv), 1000);
```

### Freezing Trap (`HT_FREEZINGTRAP`)

武器/物理技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；属性：Water；范围：1；持续时间1：Lv1=150000; Lv2=120000; Lv3=90000; Lv4=60000; Lv5=30000 ms；持续时间2：Lv1=3000; Lv2=6000; Lv3=9000; Lv4=12000; Lv5=15000 ms；伤害标记：Splash, IgnoreAtkCard；消耗/限制：SP 10；道具 Booby_Trap×1；关联状态：Freeze。

- 技能树最高等级：`5`
- 前置技能：HT_FLASHER Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/freezingtrap.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4511
if (sstatus->matk_max > sstatus->matk_min)
// src/map/battle.cpp:4512
atk = sstatus->matk_min + rnd()%(sstatus->matk_max - sstatus->matk_min);
// src/map/battle.cpp:4514
atk = sstatus->matk_min;
// src/map/battle.cpp:4520
atk = 40 * pc_checkskill(sd, RA_RESEARCHTRAP);
// src/map/battle.cpp:4524
return atk;
// src/map/battle.cpp:4528
* Stackable SC bonuses added on top of calculated skill damage
// src/map/skill.cpp:3060
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, GN_SLINGITEM, -2, DMG_SINGLE );
// src/map/skill.cpp:3063
clif_skill_damage( *dsrc, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, -1, (flag&1) ? DMG_MULTI_HIT : DMG_SPLASH );
// src/map/skill.cpp:3066
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, WM_SEVERE_RAINSTORM, -2, DMG_SPLASH );
// src/map/skill.cpp:3075
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, (flag&SD_LEVEL) ? -1 : skill_lv, DMG_SPLASH );
// src/map/skill.cpp:3076
if( dsrc != src ) // avoid damage display redundancy
// src/map/skill.cpp:3080
clif_skill_damage( *dsrc, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, -1, dmg_type );
```

### Blast Mine (`HT_BLASTMINE`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；属性：Wind；范围：1；持续时间1：Lv1=25000; Lv2=20000; Lv3=15000; Lv4=10000; Lv5=5000 ms；伤害标记：Splash, IgnoreFlee, IgnoreDefCard；消耗/限制：SP 10；道具 Booby_Trap×1。

- 技能树最高等级：`5`
- 前置技能：HT_LANDMINE Lv1, HT_SANDMAN Lv1, HT_FREEZINGTRAP Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/blastmine.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6345
md.damage = 50;
// src/map/battle.cpp:6347
md.damage = 30;
// src/map/battle.cpp:6351
md.damage = 10000;
// src/map/battle.cpp:6358
md.damage = (int64)(skill_lv * sstatus->dex * (3.0 + (float)status_get_lv(src) / 100.0) * (1.0 + (float)sstatus->int_ / 35.0));
// src/map/battle.cpp:6359
md.damage += md.damage * (rnd()%20 - 10) / 100;
// src/map/battle.cpp:6360
md.damage += (sd ? pc_checkskill(sd,RA_RESEARCHTRAP) * 40 : 0);
// src/map/battle.cpp:6365
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex + 75.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6368
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex / 2.0 + 50.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6371
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex / 2.0 + 75.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:7399
clif_damage(*src, *target, tick, wd.amotion, wd.dmotion, wd.damage, wd.div_, wd.type, wd.damage2, wd.isspdamage);
// src/map/battle.cpp:7401
if (sd && sd->bonus.splash_range > 0 && damage > 0)
// src/map/battle.cpp:7402
skill_castend_damage_id(src, target, 0, 1, tick, 0);
```

### Claymore Trap (`HT_CLAYMORETRAP`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；属性：Fire；范围：2；持续时间1：Lv1=20000; Lv2=40000; Lv3=60000; Lv4=80000; Lv5=100000 ms；伤害标记：Splash, IgnoreFlee, IgnoreDefCard；消耗/限制：SP 15；道具 Booby_Trap×2。

- 技能树最高等级：`5`
- 前置技能：HT_SHOCKWAVE Lv1, HT_BLASTMINE Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/claymoretrap.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6345
md.damage = 50;
// src/map/battle.cpp:6347
md.damage = 30;
// src/map/battle.cpp:6351
md.damage = 10000;
// src/map/battle.cpp:6358
md.damage = (int64)(skill_lv * sstatus->dex * (3.0 + (float)status_get_lv(src) / 100.0) * (1.0 + (float)sstatus->int_ / 35.0));
// src/map/battle.cpp:6359
md.damage += md.damage * (rnd()%20 - 10) / 100;
// src/map/battle.cpp:6360
md.damage += (sd ? pc_checkskill(sd,RA_RESEARCHTRAP) * 40 : 0);
// src/map/battle.cpp:6365
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex + 75.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6368
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex / 2.0 + 50.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6371
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex / 2.0 + 75.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/skill.cpp:3057
clif_skill_damage( *dsrc, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, CR_ACIDDEMONSTRATION, skill_lv, DMG_MULTI_HIT );
// src/map/skill.cpp:3060
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, GN_SLINGITEM, -2, DMG_SINGLE );
// src/map/skill.cpp:3063
clif_skill_damage( *dsrc, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, -1, (flag&1) ? DMG_MULTI_HIT : DMG_SPLASH );
```

### Remove Trap (`HT_REMOVETRAP`)

特殊技能；目标：陷阱；最高等级 1；射程：2；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 5。

- 技能树最高等级：`1`
- 前置技能：HT_LANDMINE Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/removetrap.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/removetrap.cpp:13
void SkillRemoveTrap::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/removetrap.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/archer/removetrap.cpp:20
skill_unit* su = BL_CAST(BL_SKILL, target);
```

### Talkie Box (`HT_TALKIEBOX`)

特殊技能；目标：地面区域；最高等级 1；射程：3；命中类型：Single；段数：1；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 1；道具 Booby_Trap×1。

- 技能树最高等级：`1`
- 前置技能：HT_SHOCKWAVE Lv1, HT_REMOVETRAP Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/skills/archer/talkiebox.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:6198
sd->skill_lv_dance = skill_lv;
// src/map/skill.cpp:9914
if( itemdb_group.item_exists(IG_GEMSTONE, skill->require.itemid[i]) && (sd->special_state.no_gemstone == 2 || skill_check_pc_partner(sd,skill_id,&skill_lv, 1, 2)) )
// src/map/skills/archer/talkiebox.cpp:9
void SkillTalkieBox::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/talkiebox.cpp:13
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Beast Bane (`HT_BEASTBANE`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
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
// src/map/battle.cpp:2305
damage += sd->status.str;
// src/map/battle.cpp:2311
damage += (skill * 2);
```

### Falconry Mastery (`HT_FALCON`)

特殊技能；目标：被动；最高等级 1。

- 技能树最高等级：`1`
- 前置技能：HT_BEASTBANE Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Steel Crow (`HT_STEELCROW`)

特殊技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：HT_BLITZBEAT Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/archer/wildwalk.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6368
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex / 2.0 + 50.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6371
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex / 2.0 + 75.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6383
md.damage = skill_lv * 20 + skill * 6 + ((sstatus->agi / 2) *2) + ((sstatus->dex / 10) *2);
// src/map/battle.cpp:6385
md.damage = (sstatus->dex / 10 + sstatus->int_ / 2 + skill * 3 + 40) * 2;
// src/map/battle.cpp:6386
if(mflag > 1) //Autocasted Blitz
// src/map/battle.cpp:6391
DAMAGE_DIV_FIX2(md.damage, skill_get_num(HT_BLITZBEAT, 5));
// src/map/skills/archer/wildwalk.cpp:15
void SkillWildWalk::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
// src/map/skills/archer/wildwalk.cpp:17
const map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/archer/wildwalk.cpp:19
skillratio += -100 + 1800 + 2800 * skill_lv;
// src/map/skills/archer/wildwalk.cpp:21
skillratio += 5 * sstatus->con;
// src/map/skills/archer/wildwalk.cpp:22
skillratio += skillratio * pc_checkskill(sd, WH_NATUREFRIENDLY) / 10;
// src/map/skills/archer/wildwalk.cpp:23
skillratio += skillratio * pc_checkskill(sd, HT_STEELCROW) / 10;
```

### Blitz Beat (`HT_BLITZBEAT`)

特殊技能；目标：敌方目标；最高等级 5；射程：5；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；范围：1；吟唱：1500 ms；技能后摇：1000 ms；伤害标记：Splash, IgnoreFlee；消耗/限制：SP Lv1=10; Lv2=13; Lv3=16; Lv4=19; Lv5=22；状态 Falcon。

- 技能树最高等级：`5`
- 前置技能：HT_FALCON Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/blitzbeat.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6365
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex + 75.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6368
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex / 2.0 + 50.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6371
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex / 2.0 + 75.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6383
md.damage = skill_lv * 20 + skill * 6 + ((sstatus->agi / 2) *2) + ((sstatus->dex / 10) *2);
// src/map/battle.cpp:6385
md.damage = (sstatus->dex / 10 + sstatus->int_ / 2 + skill * 3 + 40) * 2;
// src/map/battle.cpp:6386
if(mflag > 1) //Autocasted Blitz
// src/map/battle.cpp:6391
DAMAGE_DIV_FIX2(md.damage, skill_get_num(HT_BLITZBEAT, 5));
// src/map/battle.cpp:6393
md.damage = md.damage * (150 + 70 * skill_lv) / 100;
// src/map/battle.cpp:6399
md.damage = 30 + 10 * skill_lv;
// src/map/battle.cpp:6400
md.damage += skill_lv * pc_checkskill(sd, BA_MUSICALLESSON);
// src/map/skill.cpp:1339
skill->impl->applyAdditionalEffects(src, bl, skill_lv, tick, attack_type, dmg_lv);
// src/map/skill.cpp:1346
break; // If a normal attack is a skill, it's splash damage. [Inkfish]
```

### Detect (`HT_DETECTING`)

特殊技能；目标：地面区域；最高等级 4；射程：Lv1=3; Lv2=5; Lv3=7; Lv4=9；命中类型：Single；段数：1；范围：3；伤害标记：NoDamage, Splash；消耗/限制：SP 8；状态 Falcon。

- 技能树最高等级：`4`
- 前置技能：AC_CONCENTRATION Lv1, HT_FALCON Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/detect.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/detect.cpp:11
void SkillDetect::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/detect.cpp:12
int32 i = skill_get_splash(getSkillId(), skill_lv);
// src/map/skills/archer/detect.cpp:13
map_foreachinallarea( status_change_timer_sub,
```

### Spring Trap (`HT_SPRINGTRAP`)

特殊技能；目标：陷阱；最高等级 5；射程：Lv1=4; Lv2=5; Lv3=6; Lv4=7; Lv5=8；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 10；状态 Falcon。

- 技能树最高等级：`5`
- 前置技能：HT_REMOVETRAP Lv1, HT_FALCON Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/skill_factory_archer.cpp`, `src/map/skills/archer/springtrap.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/springtrap.cpp:11
void SkillSpringTrap::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/springtrap.cpp:12
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
```

### Phantasmic Arrow (`HT_PHANTASMIC`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Single；段数：1；属性：Weapon；击退：3；消耗/限制：SP 10；武器 Bow。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/phantasmicarrow.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2639
if (battle_config.cart_revo_knockback)
// src/map/skill.cpp:2644
if (!battle_config.arrow_shower_knockback && skill_id == AC_SHOWER)
// src/map/skill.cpp:2650
if (status_get_hp(target) - damage <= 0) return;
// src/map/skill.cpp:2660
if (skill_blown(dsrc, target, blewcount, dir_ka, (enum e_skill_blown)(BLOWN_IGNORE_NO_KNOCKBACK|BLOWN_NO_KNOCKBACK_MAP|BLOWN_MD_KNOCKBACK_IMMUNE|BLOWN_TARGET_NO_KNOCKBACK|BLOWN_TARGET_BASILICA)) < blewcount)
// src/map/skill.cpp:2661
skill_addtimerskill(src, tick + 300 * ((flag&2) ? 1 : 2), target->id, 0, 0, skill_id, skill_lv, BF_WEAPON, flag|4);
// src/map/skill.cpp:8159
!skill->nk[NK_NODAMAGE] &&
// src/map/skill.cpp:8165
* Check SC required to cast a skill
// src/map/skills/archer/phantasmicarrow.cpp:11
void SkillPhantasmicArrow::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/archer/phantasmicarrow.cpp:13
base_skillratio += 400;
// src/map/skills/archer/phantasmicarrow.cpp:15
base_skillratio += 50;
```

### Beast Strafing (`HT_POWER`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Multi_Hit；段数：2；属性：Weapon；持续时间1：100 ms；消耗/限制：SP 12；弹药数 1；武器 Bow；弹药 Arrow。

- 技能树最高等级：`1`
- 前置技能：AC_DOUBLE Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/beaststrafing.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2472
duration = 1;
// src/map/skill.cpp:2477
duration = 1;
// src/map/skill.cpp:2484
duration = 2000;
// src/map/skill.cpp:2485
nodelay = 1; //Neither gives walk nor attack delay
// src/map/skill.cpp:2491
duration = 1;
// src/map/skill.cpp:2495
duration = 1;
// src/map/skill.cpp:8553
if (skill_check_pc_partner(&sd, skill_id, &skill_lv, 1, 0) < 2) {
// src/map/skill.cpp:8568
if(!npc_check_areanpc(1,sd.m,sd.x,sd.y,skill_get_splash(skill_id, skill_lv))) {
// src/map/skill.cpp:8574
case CG_MOONLIT: //Check there's no wall in the range+1 area around the caster. [Skotlex]
// src/map/skills/archer/beaststrafing.cpp:11
void SkillBeastStrafing::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/beaststrafing.cpp:15
skill_attack(BF_WEAPON,src,src,target,getSkillId(),skill_lv,tick,flag);
// src/map/skills/archer/beaststrafing.cpp:18
void SkillBeastStrafing::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
```
