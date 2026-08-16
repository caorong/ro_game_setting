# Sniper 技能

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
| 115 | `HT_SKIDTRAP` | Skid Trap | 5 | Hunter | 否 | — | Misc / Ground |
| 116 | `HT_LANDMINE` | Land Mine | 5 | Hunter | 否 | — | Misc / Ground |
| 117 | `HT_ANKLESNARE` | Ankle Snare | 5 | Hunter | 否 | HT_SKIDTRAP Lv1 | Misc / Ground |
| 118 | `HT_SHOCKWAVE` | Shockwave Trap | 5 | Hunter | 否 | HT_ANKLESNARE Lv1 | Misc / Ground |
| 119 | `HT_SANDMAN` | Sandman | 5 | Hunter | 否 | HT_FLASHER Lv1 | Misc / Ground |
| 120 | `HT_FLASHER` | Flasher | 5 | Hunter | 否 | HT_SKIDTRAP Lv1 | Misc / Ground |
| 121 | `HT_FREEZINGTRAP` | Freezing Trap | 5 | Hunter | 否 | HT_FLASHER Lv1 | Weapon / Ground |
| 122 | `HT_BLASTMINE` | Blast Mine | 5 | Hunter | 否 | HT_LANDMINE Lv1, HT_SANDMAN Lv1, HT_FREEZINGTRAP Lv1 | Misc / Ground |
| 123 | `HT_CLAYMORETRAP` | Claymore Trap | 5 | Hunter | 否 | HT_SHOCKWAVE Lv1, HT_BLASTMINE Lv1 | Misc / Ground |
| 124 | `HT_REMOVETRAP` | Remove Trap | 1 | Hunter | 否 | HT_LANDMINE Lv1 | Misc / Trap |
| 125 | `HT_TALKIEBOX` | Talkie Box | 1 | Hunter | 否 | HT_SHOCKWAVE Lv1, HT_REMOVETRAP Lv1 | Misc / Ground |
| 126 | `HT_BEASTBANE` | Beast Bane | 10 | Hunter | 否 | — | Weapon / Passive |
| 127 | `HT_FALCON` | Falconry Mastery | 1 | Hunter | 否 | HT_BEASTBANE Lv1 | Misc / Passive |
| 128 | `HT_STEELCROW` | Steel Crow | 10 | Hunter | 否 | HT_BLITZBEAT Lv5 | Misc / Passive |
| 129 | `HT_BLITZBEAT` | Blitz Beat | 5 | Hunter | 否 | HT_FALCON Lv1 | Misc / Attack |
| 130 | `HT_DETECTING` | Detect | 4 | Hunter | 否 | AC_CONCENTRATION Lv1, HT_FALCON Lv1 | Misc / Ground |
| 131 | `HT_SPRINGTRAP` | Spring Trap | 5 | Hunter | 否 | HT_REMOVETRAP Lv1, HT_FALCON Lv1 | Misc / Trap |
| 1009 | `HT_PHANTASMIC` | Phantasmic Arrow | 1 | Hunter | 否 | — | Weapon / Attack |
| 499 | `HT_POWER` | Beast Strafing | 1 | Hunter | 否 | AC_DOUBLE Lv10 | Weapon / Attack |
| 380 | `SN_SIGHT` | Falcon Eyes | 10 | Sniper | 是 | AC_OWL Lv10, AC_VULTURE Lv10, AC_CONCENTRATION Lv10, HT_FALCON Lv1 | Weapon / Self |
| 381 | `SN_FALCONASSAULT` | Falcon Assault | 5 | Sniper | 是 | HT_STEELCROW Lv3, AC_VULTURE Lv5, HT_BLITZBEAT Lv5, HT_FALCON Lv1 | Misc / Attack |
| 382 | `SN_SHARPSHOOTING` | Focused Arrow Strike | 5 | Sniper | 是 | AC_CONCENTRATION Lv10, AC_DOUBLE Lv5 | Weapon / Attack |
| 383 | `SN_WINDWALK` | Wind Walker | 10 | Sniper | 是 | AC_CONCENTRATION Lv9 | Weapon / Self |

## 技能详情

### Falcon Eyes (`SN_SIGHT`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-2=20; Lv3-4=25; Lv5-6=30; Lv7-8=35; Lv9-10=40；关联状态：TrueSight。

- 技能树最高等级：`10`
- 前置技能：AC_OWL Lv10, AC_VULTURE Lv10, AC_CONCENTRATION Lv10, HT_FALCON Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/skill_factory_archer.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Falcon Assault (`SN_FALCONASSAULT`)

特殊技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：1；吟唱：1000 ms；技能后摇：3000 ms；伤害标记：IgnoreFlee；消耗/限制：SP Lv1=30; Lv2=34; Lv3=38; Lv4=42; Lv5=46；状态 Falcon。

- 技能树最高等级：`5`
- 前置技能：HT_STEELCROW Lv3, AC_VULTURE Lv5, HT_BLITZBEAT Lv5, HT_FALCON Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/archer/falconassault.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

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
// src/map/skills/archer/falconassault.cpp:9
void SkillFalconAssault::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/falconassault.cpp:10
skill_attack(skill_get_type(getSkillId()),src,src,target,getSkillId(),skill_lv,tick,flag);
```

### Focused Arrow Strike (`SN_SHARPSHOOTING`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：1；属性：Weapon；范围：1；吟唱：2000 ms；技能后摇：1500 ms；伤害标记：Critical；消耗/限制：SP Lv1=18; Lv2=21; Lv3=24; Lv4=27; Lv5=30；弹药数 1；武器 Bow；弹药 Arrow。

- 技能树最高等级：`5`
- 前置技能：AC_CONCENTRATION Lv10, AC_DOUBLE Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/archer/focusedarrowstrike.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3071
status_change_end(src, SC_AUTOCOUNTER);
// src/map/battle.cpp:3078
cri *= 2;
// src/map/battle.cpp:3083
cri += 300; // !TODO: Confirm new bonus
// src/map/battle.cpp:3085
cri += 200;
// src/map/battle.cpp:3089
cri += 250 + 50*skill_lv;
// src/map/battle.cpp:4174
bflag &= ~(BDMG_CRIT); // Sharpshooting just ignores DEF/FLEE but damage is like a normal attack
// src/map/battle.cpp:4175
wd->damage = battle_calc_base_damage(src, sstatus, &sstatus->rhw, sc, tstatus->size, bflag);
// src/map/battle.cpp:4177
wd->damage2 = battle_calc_base_damage(src, sstatus, &sstatus->lhw, sc, tstatus->size, bflag);
// src/map/battle.cpp:4179
if (nk[NK_SPLASHSPLIT]){ // Divide ATK among targets
// src/map/battle.cpp:4181
wd->damage /= wd->miscflag;
// src/map/battle.cpp:4944
* "Plant"-type (mobs that only take 1 damage from all sources) damage calculation
// src/map/battle.cpp:4951
static void battle_calc_attack_plant(struct Damage* wd, block_list *src,block_list *target, uint16 skill_id, uint16 skill_lv)
```

### Wind Walker (`SN_WINDWALK`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；范围：-1；吟唱：Lv1=2000; Lv2=2400; Lv3=2800; Lv4=3200; Lv5=3600; Lv6=4000; Lv7=4400; Lv8=4800; Lv9=5200; Lv10=5600 ms；技能后摇：2000 ms；持续时间1：Lv1=130000; Lv2=160000; Lv3=190000; Lv4=220000; Lv5=250000; Lv6=280000; Lv7=310000; Lv8=340000; Lv9=370000; Lv10=400000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=46; Lv2=52; Lv3=58; Lv4=64; Lv5=70; Lv6=76; Lv7=82; Lv8=88; Lv9=94; Lv10=100；关联状态：WindWalk。

- 技能树最高等级：`10`
- 前置技能：AC_CONCENTRATION Lv9
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/skill_factory_archer.cpp`, `src/map/skills/archer/windwalker.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/windwalker.cpp:14
void SkillWindWalker::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/windwalker.cpp:16
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/archer/windwalker.cpp:19
clif_skill_nodamage(target, *target, getSkillId(), skill_lv, sc_start(src,target,type,100,skill_lv,skill_get_time(getSkillId(),skill_lv)));
// src/map/skills/archer/windwalker.cpp:22
party_foreachsamemap(skill_area_sub, sd, skill_get_splash(getSkillId(), skill_lv), src, getSkillId(), skill_lv, tick, flag|BCT_PARTY|1, skill_castend_nodamage_id);
```
