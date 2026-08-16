# Lord_Knight 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Lord_Knight` 公式页](../skill-formulas/Lord_Knight.md)

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
| 55 | `KN_SPEARMASTERY` | Spear Mastery | 10 | Knight | 否 | — | Weapon / Passive |
| 56 | `KN_PIERCE` | Pierce | 10 | Knight | 否 | KN_SPEARMASTERY Lv1 | Weapon / Attack |
| 57 | `KN_BRANDISHSPEAR` | Brandish Spear | 10 | Knight | 否 | KN_RIDING Lv1, KN_SPEARSTAB Lv3 | Weapon / Attack |
| 58 | `KN_SPEARSTAB` | Spear Stab | 10 | Knight | 否 | KN_PIERCE Lv5 | Weapon / Attack |
| 59 | `KN_SPEARBOOMERANG` | Spear Boomerang | 5 | Knight | 否 | KN_PIERCE Lv3 | Weapon / Attack |
| 60 | `KN_TWOHANDQUICKEN` | Twohand Quicken | 10 | Knight | 否 | SM_TWOHAND Lv1 | Weapon / Self |
| 61 | `KN_AUTOCOUNTER` | Counter Attack | 5 | Knight | 否 | SM_TWOHAND Lv1 | Weapon / Self |
| 62 | `KN_BOWLINGBASH` | Bowling Bash | 10 | Knight | 否 | SM_BASH Lv10, SM_MAGNUM Lv3, SM_TWOHAND Lv5, KN_TWOHANDQUICKEN Lv10, KN_AUTOCOUNTER Lv5 | Weapon / Attack |
| 63 | `KN_RIDING` | Peco Peco Riding | 1 | Knight | 否 | SM_ENDURE Lv1 | Weapon / Passive |
| 64 | `KN_CAVALIERMASTERY` | Cavalier Mastery | 5 | Knight | 否 | KN_RIDING Lv1 | Weapon / Passive |
| 1001 | `KN_CHARGEATK` | Charge Attack | 1 | Knight | 否 | — | Weapon / Attack |
| 495 | `KN_ONEHAND` | Onehand Quicken | 1 | Knight | 否 | KN_TWOHANDQUICKEN Lv10 | Weapon / Self |
| 355 | `LK_AURABLADE` | Aura Blade | 5 | Lord_Knight | 是 | SM_BASH Lv5, SM_MAGNUM Lv5, SM_TWOHAND Lv5 | Weapon / Self |
| 356 | `LK_PARRYING` | Parrying | 10 | Lord_Knight | 是 | SM_TWOHAND Lv10, SM_PROVOKE Lv5, KN_TWOHANDQUICKEN Lv3 | Weapon / Self |
| 357 | `LK_CONCENTRATION` | Concentration | 5 | Lord_Knight | 是 | SM_RECOVERY Lv5, KN_SPEARMASTERY Lv5, KN_RIDING Lv1 | Weapon / Self |
| 358 | `LK_TENSIONRELAX` | Relax | 1 | Lord_Knight | 是 | SM_RECOVERY Lv10, SM_PROVOKE Lv5, SM_ENDURE Lv3 | Weapon / Self |
| 359 | `LK_BERSERK` | Frenzy | 1 | Lord_Knight | 是 | — | Weapon / Self |
| 397 | `LK_SPIRALPIERCE` | Spiral Pierce | 5 | Lord_Knight | 是 | KN_SPEARMASTERY Lv10, KN_PIERCE Lv5, KN_SPEARSTAB Lv5, KN_RIDING Lv1 | Weapon / Attack |
| 398 | `LK_HEADCRUSH` | Traumatic Blow | 5 | Lord_Knight | 是 | KN_SPEARMASTERY Lv9, KN_RIDING Lv1 | Weapon / Attack |
| 399 | `LK_JOINTBEAT` | Vital Strike | 10 | Lord_Knight | 是 | KN_SPEARMASTERY Lv9, KN_CAVALIERMASTERY Lv3, LK_HEADCRUSH Lv3 | Weapon / Attack |

## 技能详情

### Aura Blade (`LK_AURABLADE`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：Lv1=40000; Lv2=60000; Lv3=80000; Lv4=100000; Lv5=120000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=18; Lv2=26; Lv3=34; Lv4=42; Lv5=50；武器 Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Bow, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；关联状态：AuraBlade。

- 技能树最高等级：`5`
- 前置技能：SM_BASH Lv5, SM_MAGNUM Lv5, SM_TWOHAND Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/skill_factory_swordman.cpp:222
case LG_REFLECTDAMAGE:
// src/map/skills/swordman/skill_factory_swordman.cpp:234
case LK_CONCENTRATION:
```

### Parrying (`LK_PARRYING`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：Lv1=15000; Lv2=20000; Lv3=25000; Lv4=30000; Lv5=35000; Lv6=40000; Lv7=45000; Lv8=50000; Lv9=55000; Lv10=60000 ms；伤害标记：NoDamage；消耗/限制：SP 50；武器 2hSword；关联状态：Parrying。

- 技能树最高等级：`10`
- 前置技能：SM_TWOHAND Lv10, SM_PROVOKE Lv5, KN_TWOHANDQUICKEN Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

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
// src/map/skills/swordman/skill_factory_swordman.cpp:234
case LK_CONCENTRATION:
```

### Concentration (`LK_CONCENTRATION`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：Lv1=25000; Lv2=30000; Lv3=35000; Lv4=40000; Lv5=45000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=14; Lv2=18; Lv3=22; Lv4=26; Lv5=30；关联状态：Concentration。

- 技能树最高等级：`5`
- 前置技能：SM_RECOVERY Lv5, KN_SPEARMASTERY Lv5, KN_RIDING Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/skill_factory_swordman.cpp:222
case LG_REFLECTDAMAGE:
// src/map/skills/swordman/skill_factory_swordman.cpp:234
case LK_CONCENTRATION:
```

### Relax (`LK_TENSIONRELAX`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 15；关联状态：TensionRelax。

- 技能树最高等级：`1`
- 前置技能：SM_RECOVERY Lv10, SM_PROVOKE Lv5, SM_ENDURE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/relax.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/relax.cpp:12
void SkillRelax::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/swordman/relax.cpp:15
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
// src/map/skills/swordman/relax.cpp:16
sc_start4(src,target,type,100,skill_lv,0,0,skill_get_time2(getSkillId(),skill_lv),
// src/map/skills/swordman/relax.cpp:17
skill_get_time(getSkillId(),skill_lv)));
// src/map/skills/swordman/skill_factory_swordman.cpp:234
case LK_CONCENTRATION:
```

### Frenzy (`LK_BERSERK`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：300000 ms；持续时间2：10000 ms；伤害标记：NoDamage；消耗/限制：SP 200；关联状态：Berserk。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/skill_factory_swordman.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/skill_factory_swordman.cpp:222
case LG_REFLECTDAMAGE:
// src/map/skills/swordman/skill_factory_swordman.cpp:234
case LK_CONCENTRATION:
// src/map/status.cpp:13720
status_change_end(bl, SC_ENDURE);
// src/map/status.cpp:13723
if(status->hp > 200 && sc && sc->getSCE(SC__BLOODYLUST)) {
// src/map/status.cpp:13724
status_percent_heal(bl, 100, 0);
// src/map/status.cpp:13725
status_change_end(bl, SC__BLOODYLUST);
// src/map/status.cpp:13726
} else if (status->hp > 100 && val2) // If val2 is removed, no HP penalty (dispelled?) [Skotlex]
// src/map/status.cpp:13730
status_change_end(bl, SC_ENDURE);
// src/map/status.cpp:13732
sc_start4(bl, bl, SC_REGENERATION, 100, 10,0,0,(RGN_HP|RGN_SP), skill_get_time(LK_BERSERK, val1));
```

### Spiral Pierce (`LK_SPIRALPIERCE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：4；命中类型：Multi_Hit；段数：5；属性：Weapon；吟唱：Lv1=300; Lv2=500; Lv3=700; Lv4=900; Lv5=1000 ms；技能后摇：Lv1=1200; Lv2=1400; Lv3=1600; Lv4=1800; Lv5=2000 ms；持续时间2：1000 ms；伤害标记：IgnoreDefense；消耗/限制：SP Lv1=18; Lv2=21; Lv3=24; Lv4=27; Lv5=30；武器 1hSpear, 2hSpear；关联状态：Ankle。

- 技能树最高等级：`5`
- 前置技能：KN_SPEARMASTERY Lv10, KN_PIERCE Lv5, KN_SPEARSTAB Lv5, KN_RIDING Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/gloomyday.cpp`, `src/map/skills/swordman/hundredspear.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`, `src/map/skills/swordman/spiralpierce.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3975
std::bitset<NK_MAX> nk = battle_skill_get_damage_properties(skill_id, wd->miscflag);
// src/map/battle.cpp:3977
switch (skill_id) {	//Calc base damage according to skill
// src/map/battle.cpp:3979
wd->damage = sstatus->max_hp* 9/100;
// src/map/battle.cpp:3980
wd->damage2 = 0;
// src/map/battle.cpp:3982
wd->weaponAtk = wd->damage;
// src/map/battle.cpp:3983
wd->weaponAtk2 = wd->damage2;
// src/map/battle.cpp:3990
battle_calc_damage_parts(wd, src, target, skill_id, skill_lv);
// src/map/battle.cpp:3996
ATK_RATE(wd->statusAtk, wd->statusAtk2, 0);
// src/map/battle.cpp:3997
ATK_RATE(wd->weaponAtk, wd->weaponAtk2, 0);
// src/map/battle.cpp:4015
ATK_RATE(wd->equipAtk, wd->equipAtk2, 115);
// src/map/battle.cpp:4020
wd->damage = battle_calc_base_damage(src, sstatus, &sstatus->rhw, sc, tstatus->size, 0); //Monsters have no weight and use ATK instead
// src/map/battle.cpp:4024
wd->damage = 40 * sstatus->str + sstatus->hp * 8 * skill_lv / 100;
```

### Traumatic Blow (`LK_HEADCRUSH`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：4；命中类型：Single；段数：1；属性：Weapon；技能后摇：500 ms；持续时间2：120000 ms；消耗/限制：SP 23；关联状态：Bleeding。

- 技能树最高等级：`5`
- 前置技能：KN_SPEARMASTERY Lv9, KN_RIDING Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/skill_factory_swordman.cpp`, `src/map/skills/swordman/traumaticblow.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/skill_factory_swordman.cpp:234
case LK_CONCENTRATION:
// src/map/skills/swordman/traumaticblow.cpp:13
void SkillTraumaticBlow::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/swordman/traumaticblow.cpp:14
base_skillratio += 40 * skill_lv;
// src/map/skills/swordman/traumaticblow.cpp:17
void SkillTraumaticBlow::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/swordman/traumaticblow.cpp:18
map_session_data* sd = BL_CAST( BL_PC, src );
```

### Vital Strike (`LK_JOINTBEAT`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：4；命中类型：Single；段数：1；属性：Weapon；技能后摇：Lv1-5=800; Lv6-10=1000 ms；持续时间2：30000 ms；消耗/限制：SP Lv1-2=12; Lv3-4=14; Lv5-6=16; Lv7-8=18; Lv9-10=20；武器 1hSpear, 2hSpear；关联状态：JointBeat。

- 技能树最高等级：`10`
- 前置技能：KN_SPEARMASTERY Lv9, KN_CAVALIERMASTERY Lv3, LK_HEADCRUSH Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/skill_factory_swordman.cpp`, `src/map/skills/swordman/vitalstrike.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/skill_factory_swordman.cpp:234
case LK_CONCENTRATION:
// src/map/skills/swordman/vitalstrike.cpp:11
void SkillVitalStrike::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/swordman/vitalstrike.cpp:12
const status_change *tsc = status_get_sc(target);
// src/map/skills/swordman/vitalstrike.cpp:14
base_skillratio += 10 * skill_lv - 50;
// src/map/skills/swordman/vitalstrike.cpp:18
base_skillratio *= 2;
```
