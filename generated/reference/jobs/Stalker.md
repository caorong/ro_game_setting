# Stalker 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 48 | `TF_DOUBLE` | Double Attack | 10 | Thief | 否 | — | Weapon / Passive |
| 49 | `TF_MISS` | Improve Dodge | 10 | Thief | 否 | — | Weapon / Passive |
| 50 | `TF_STEAL` | Steal | 10 | Thief | 否 | — | Weapon / Attack |
| 51 | `TF_HIDING` | Hiding | 10 | Thief | 否 | TF_STEAL Lv5 | None / Self |
| 52 | `TF_POISON` | Envenom | 10 | Thief | 否 | — | Weapon / Attack |
| 53 | `TF_DETOXIFY` | Detoxify | 1 | Thief | 否 | TF_POISON Lv3 | Weapon / Support |
| 149 | `TF_SPRINKLESAND` | Sand Attack | 1 | Thief | 否 | — | Weapon / Attack |
| 150 | `TF_BACKSLIDING` | Back Slide | 1 | Thief | 否 | — | Weapon / Self |
| 151 | `TF_PICKSTONE` | Find Stone | 1 | Thief | 否 | — | None / Self |
| 152 | `TF_THROWSTONE` | Stone Fling | 1 | Thief | 否 | — | Misc / Attack |
| 2 | `SM_SWORD` | Sword Mastery | 10 | Rogue | 否 | — | Weapon / Passive |
| 44 | `AC_VULTURE` | Vulture's Eye | 10 | Rogue | 否 | — | None / Passive |
| 46 | `AC_DOUBLE` | Double Strafe | 10 | Rogue | 否 | AC_VULTURE Lv10 | Weapon / Attack |
| 124 | `HT_REMOVETRAP` | Remove Trap | 1 | Rogue | 否 | AC_DOUBLE Lv5 | Misc / Trap |
| 210 | `RG_SNATCHER` | Gank | 10 | Rogue | 否 | TF_STEAL Lv1 | Weapon / Passive |
| 211 | `RG_STEALCOIN` | Mug | 10 | Rogue | 否 | RG_SNATCHER Lv4 | Weapon / Attack |
| 212 | `RG_BACKSTAP` | Back Stab | 10 | Rogue | 否 | RG_STEALCOIN Lv4 | Weapon / Attack |
| 213 | `RG_TUNNELDRIVE` | Stalk | 5 | Rogue | 否 | TF_HIDING Lv1 | None / Passive |
| 214 | `RG_RAID` | Sightless Mind | 5 | Rogue | 否 | RG_BACKSTAP Lv2, RG_TUNNELDRIVE Lv2 | Weapon / Self |
| 215 | `RG_STRIPWEAPON` | Divest Weapon | 5 | Rogue | 否 | RG_STRIPARMOR Lv5 | Weapon / Attack |
| 216 | `RG_STRIPSHIELD` | Divest Shield | 5 | Rogue | 否 | RG_STRIPHELM Lv5 | Weapon / Attack |
| 217 | `RG_STRIPARMOR` | Divest Armor | 5 | Rogue | 否 | RG_STRIPSHIELD Lv5 | Weapon / Attack |
| 218 | `RG_STRIPHELM` | Divest Helm | 5 | Rogue | 否 | RG_STEALCOIN Lv2 | Weapon / Attack |
| 219 | `RG_INTIMIDATE` | Snatch | 5 | Rogue | 否 | RG_BACKSTAP Lv4, RG_RAID Lv5 | Weapon / Attack |
| 220 | `RG_GRAFFITI` | Scribble | 1 | Rogue | 否 | RG_FLAGGRAFFITI Lv5 | None / Ground |
| 221 | `RG_FLAGGRAFFITI` | Piece | 5 | Rogue | 否 | RG_CLEANER Lv1 | None / Ground |
| 222 | `RG_CLEANER` | Remover | 1 | Rogue | 否 | RG_GANGSTER Lv1 | None / Ground |
| 223 | `RG_GANGSTER` | Slyness | 1 | Rogue | 否 | RG_STRIPSHIELD Lv3 | None / Passive |
| 224 | `RG_COMPULSION` | Haggle | 5 | Rogue | 否 | RG_GANGSTER Lv1 | None / Passive |
| 225 | `RG_PLAGIARISM` | Intimidate | 10 | Rogue | 否 | RG_INTIMIDATE Lv5 | None / Passive |
| 1005 | `RG_CLOSECONFINE` | Close Confine | 1 | Rogue | 否 | — | Weapon / Attack |
| 389 | `ST_CHASEWALK` | Stealth | 5 | Stalker | 是 | TF_HIDING Lv5, RG_TUNNELDRIVE Lv3 | None / Self |
| 390 | `ST_REJECTSWORD` | Counter Instinct | 5 | Stalker | 是 | RG_STRIPWEAPON Lv1 | Weapon / Self |
| 475 | `ST_PRESERVE` | Preserve | 1 | Stalker | 是 | RG_PLAGIARISM Lv10 | None / Self |
| 476 | `ST_FULLSTRIP` | Divest All | 5 | Stalker | 是 | RG_STRIPWEAPON Lv5, RG_STRIPSHIELD Lv5, RG_STRIPARMOR Lv5, RG_STRIPHELM Lv5 | Weapon / Attack |

## 技能详情

### Stealth (`ST_CHASEWALK`)

非伤害技能；目标：自身；最高等级 5；命中类型：Single；段数：1；吟唱：1200 ms；持续时间1：10000 ms；持续时间2：30000 ms；伤害标记：NoDamage；消耗/限制：SP 10；关联状态：ChaseWalk。

- 技能树最高等级：`5`
- 前置技能：TF_HIDING Lv5, RG_TUNNELDRIVE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/thief/skill_factory_thief.cpp`, `src/map/skills/thief/stealth.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/thief/skill_factory_thief.cpp:271
case SHC_IMPACT_CRATER:
// src/map/skills/thief/skill_factory_thief.cpp:272
return std::make_unique<SkillImpactCrater>();
// src/map/skills/thief/stealth.cpp:12
void SkillStealth::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/thief/stealth.cpp:14
status_change *tsc = status_get_sc(target);
// src/map/skills/thief/stealth.cpp:15
status_change_entry *tsce = (tsc && type != SC_NONE)?tsc->getSCE(type):nullptr;
// src/map/skills/thief/stealth.cpp:19
clif_skill_nodamage(src,*target,getSkillId(),-1,status_change_end(target, type)); //Hide skill-scream animation.
```

### Counter Instinct (`ST_REJECTSWORD`)

武器/物理技能；目标：自身；最高等级 5；段数：1；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=10; Lv2=15; Lv3=20; Lv4=25; Lv5=30；关联状态：RejectSword。

- 技能树最高等级：`5`
- 前置技能：RG_STRIPWEAPON Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/thief/counterinstinct.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5177
if(wd->damage && tsc && tsc->getSCE(SC_REJECTSWORD) &&
// src/map/battle.cpp:5186
ATK_RATER(wd->damage, 50)
// src/map/battle.cpp:5187
clif_skill_nodamage(target, *target,ST_REJECTSWORD, tsc->getSCE(SC_REJECTSWORD)->val1);
// src/map/battle.cpp:5188
clif_damage(*target, *src, gettick(), 0, 0, wd->damage, 0, DMG_NORMAL, 0, false);
// src/map/battle.cpp:5189
battle_fix_damage(target, src, wd->damage, wd->div_, ST_REJECTSWORD);
// src/map/battle.cpp:5193
status_change_end(target, SC_REJECTSWORD);
// src/map/battle.cpp:5197
if (tsc != nullptr && wd->damage > 0) {
// src/map/battle.cpp:5198
if (status_change_entry* sce = tsc->getSCE(SC_POISONREACT); sce != nullptr && rnd_chance_official(sce->val3, 100)) {
// src/map/skills/thief/counterinstinct.cpp:11
void SkillCounterInstinct::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/thief/counterinstinct.cpp:12
sc_start(src,target,SC_AUTOCOUNTER,(skill_lv*15),skill_lv,skill_get_time(getSkillId(),skill_lv));
```

### Preserve (`ST_PRESERVE`)

非伤害技能；目标：自身；最高等级 1；段数：1；吟唱：1000 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 30；关联状态：Preserve。

- 技能树最高等级：`1`
- 前置技能：RG_PLAGIARISM Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/thief/skill_factory_thief.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Divest All (`ST_FULLSTRIP`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：1；命中类型：Single；段数：1；技能后摇：1000 ms；持续时间1：Lv1=75000; Lv2=90000; Lv3=105000; Lv4=120000; Lv5=135000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=22; Lv2=24; Lv3=26; Lv4=28; Lv5=30。

- 技能树最高等级：`5`
- 前置技能：RG_STRIPWEAPON Lv5, RG_STRIPSHIELD Lv5, RG_STRIPARMOR Lv5, RG_STRIPHELM Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/divestall.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2092
int32 rate, time, location, mod = 100;
// src/map/skill.cpp:2094
switch (skill_id) { // Rate
// src/map/skill.cpp:2100
rate = 50 * (skill_lv + 1) + 2 * (sstatus->dex - tstatus->dex);
// src/map/skill.cpp:2104
int32 min_rate = 50 + 20 * skill_lv;
// src/map/skill.cpp:2106
rate = min_rate + 2 * (sstatus->dex - tstatus->dex);
// src/map/skill.cpp:2107
rate = max(min_rate, rate);
// src/map/skill.cpp:2112
rate = sstatus->dex / (4 * (7 - skill_lv)) + sstatus->luk / (4 * (6 - skill_lv));
// src/map/skill.cpp:2113
rate = rate + status_get_lv(src) - (tstatus->agi * rate / 100) - tstatus->luk - status_get_lv(target);
// src/map/skill.cpp:2137
switch (skill_id) { // Duration
// src/map/skill.cpp:2140
time = skill_get_time(skill_id, skill_lv);
// src/map/skill.cpp:2151
time = skill_get_time2(skill_id, skill_lv);
// src/map/skill.cpp:2153
time = skill_get_time(skill_id, skill_lv);
```
