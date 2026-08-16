# Archer 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 43 | `AC_OWL` | Owl's Eye | 10 | Archer | 是 | — | None / Passive |
| 44 | `AC_VULTURE` | Vulture's Eye | 10 | Archer | 是 | AC_OWL Lv3 | None / Passive |
| 45 | `AC_CONCENTRATION` | Improve Concentration | 10 | Archer | 是 | AC_VULTURE Lv1 | Weapon / Self |
| 46 | `AC_DOUBLE` | Double Strafe | 10 | Archer | 是 | — | Weapon / Attack |
| 47 | `AC_SHOWER` | Arrow Shower | 10 | Archer | 是 | AC_DOUBLE Lv5 | Weapon / Ground |
| 147 | `AC_MAKINGARROW` | Arrow Crafting | 1 | Archer | 是 | — | Weapon / Self |
| 148 | `AC_CHARGEARROW` | Arrow Repel | 1 | Archer | 是 | — | Weapon / Attack |

## 技能详情

### Owl's Eye (`AC_OWL`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:311
return CAST_NODAMAGE;
// src/map/skill.cpp:315
return CAST_DAMAGE; //Combo skill.
// src/map/skill.cpp:316
return CAST_NODAMAGE;
// src/map/skill.cpp:318
if (skill->nk[NK_NODAMAGE])
// src/map/skill.cpp:319
return CAST_NODAMAGE;
// src/map/skill.cpp:320
return CAST_DAMAGE;
// src/map/skill.cpp:324
int32 skill_get_range2(const block_list* bl, uint16 skill_id, uint16 skill_lv, bool isServer) {
// src/map/skill.cpp:328
int32 range = skill_get_range(skill_id, skill_lv);
```

### Vulture's Eye (`AC_VULTURE`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：AC_OWL Lv3
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3278
hitrate += sstatus->hit - flee;
// src/map/battle.cpp:3282
hitrate -= 50;
// src/map/battle.cpp:3285
hitrate += sd->bonus.arrow_hit;
// src/map/battle.cpp:3288
if (sd) //in Renewal hit bonus from Vultures Eye is not anymore shown in status window
// src/map/battle.cpp:3289
hitrate += pc_checkskill(sd,AC_VULTURE);
// src/map/battle.cpp:3295
skill->impl->modifyHitRate(hitrate, src, target, skill_lv);
// src/map/battle.cpp:3297
} else if (sd && wd->type&DMG_MULTI_HIT && wd->div_ == 2) // +1 hit per level of Double Attack on a successful double attack (making sure other multi attack skills do not trigger this) [helvetica]
// src/map/battle.cpp:3298
hitrate += pc_checkskill(sd,TF_DOUBLE);
// src/map/battle.cpp:6618
flee = (flee * (100 - (attacker_count - (battle_config.agi_penalty_count - 1))*battle_config.agi_penalty_num))/100;
// src/map/battle.cpp:6620
flee -= (attacker_count - (battle_config.agi_penalty_count - 1))*battle_config.agi_penalty_num;
// src/map/battle.cpp:6621
if(flee < 1)
// src/map/battle.cpp:6622
flee = 1;
```

### Improve Concentration (`AC_CONCENTRATION`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；范围：3；持续时间1：Lv1=60000; Lv2=80000; Lv3=100000; Lv4=120000; Lv5=140000; Lv6=160000; Lv7=180000; Lv8=200000; Lv9=220000; Lv10=240000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=25; Lv2=30; Lv3=35; Lv4=40; Lv5=45; Lv6=50; Lv7=55; Lv8=60; Lv9=65; Lv10=70；关联状态：Concentrate。

- 技能树最高等级：`10`
- 前置技能：AC_VULTURE Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/concentration.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/concentration.cpp:4
#include "concentration.hpp"
// src/map/skills/archer/concentration.cpp:9
SkillConcentration::SkillConcentration() : SkillImpl(AC_CONCENTRATION)
// src/map/skills/archer/concentration.cpp:13
void SkillConcentration::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const
// src/map/skills/archer/concentration.cpp:17
int32 splash = skill_get_splash(getSkillId(), skill_lv);
// src/map/skills/archer/concentration.cpp:18
clif_skill_nodamage(src, *target, getSkillId(), skill_lv, sc_start(src, target, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
// src/map/skills/archer/concentration.cpp:20
map_foreachinallrange(status_change_timer_sub, src, splash, BL_CHAR, src, nullptr, type, tick);
// src/map/skills/archer/skill_factory_archer.cpp:141
case AC_CONCENTRATION:
// src/map/skills/archer/skill_factory_archer.cpp:142
return std::make_unique<SkillConcentration>();
```

### Double Strafe (`AC_DOUBLE`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-9；命中类型：Multi_Hit；段数：2；属性：Weapon；持续时间1：100 ms；消耗/限制：SP 12；弹药数 1；武器 Bow；弹药 Arrow。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/doublestrafe.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:835
if (!sd.state.autocast && sd.skillitem != skill_id && sd.canskill_tick &&
// src/map/skill.cpp:837
{// attempted to cast a skill before the attack motion has finished
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
// src/map/skill.cpp:8553
if (skill_check_pc_partner(&sd, skill_id, &skill_lv, 1, 0) < 2) {
// src/map/skill.cpp:8568
if(!npc_check_areanpc(1,sd.m,sd.x,sd.y,skill_get_splash(skill_id, skill_lv))) {
// src/map/skill.cpp:8574
case CG_MOONLIT: //Check there's no wall in the range+1 area around the caster. [Skotlex]
// src/map/skills/archer/doublestrafe.cpp:9
void SkillDoubleStrafe::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/archer/doublestrafe.cpp:10
base_skillratio += 10 * (skill_lv - 1);
```

### Arrow Shower (`AC_SHOWER`)

武器/物理技能；目标：地面区域；最高等级 10；射程：-9；命中类型：Single；段数：1；属性：Weapon；范围：2；击退：2；持续时间1：100 ms；伤害标记：Splash；消耗/限制：SP 15；弹药数 1；武器 Bow；弹药 Arrow。

- 技能树最高等级：`10`
- 前置技能：AC_DOUBLE Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/arrowshower.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2671
static int32 battle_range_type(const block_list* src, const block_list* target, uint16 skill_id, uint16 skill_lv)
// src/map/battle.cpp:2679
case AM_DEMONSTRATION:
// src/map/skill.cpp:2635
if(!battle_config.stormgust_knockback)
// src/map/skill.cpp:2639
if (battle_config.cart_revo_knockback)
// src/map/skill.cpp:2644
if (!battle_config.arrow_shower_knockback && skill_id == AC_SHOWER)
// src/map/skill.cpp:2650
if (status_get_hp(target) - damage <= 0) return;
// src/map/skills/archer/arrowshower.cpp:8
SkillArrowShower::SkillArrowShower() : SkillImplRecursiveDamageSplash(AC_SHOWER) {
// src/map/skills/archer/arrowshower.cpp:11
void SkillArrowShower::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/archer/arrowshower.cpp:13
base_skillratio += 50 + 10 * skill_lv;
// src/map/skills/archer/arrowshower.cpp:15
base_skillratio += -25 + 5 * skill_lv;
// src/map/skills/archer/arrowshower.cpp:19
void SkillArrowShower::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/arrowshower.cpp:20
status_change_end(src, SC_CAMOUFLAGE);
```

### Arrow Crafting (`AC_MAKINGARROW`)

武器/物理技能；目标：自身；最高等级 1；伤害标记：NoDamage；消耗/限制：SP 10；状态 Recover_Weight_Rate。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/makingarrow.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:9351
switch( sd.menuskill_id ) { // Cast start or cast end??
// src/map/skills/archer/makingarrow.cpp:13
void SkillMakingArrow::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const
// src/map/skills/archer/makingarrow.cpp:15
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/archer/makingarrow.cpp:20
clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
// src/map/skills/archer/skill_factory_archer.cpp:141
case AC_CONCENTRATION:
// src/map/skills/archer/skill_factory_archer.cpp:142
return std::make_unique<SkillConcentration>();
```

### Arrow Repel (`AC_CHARGEARROW`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Single；段数：1；属性：Weapon；击退：6；吟唱：1500 ms；伤害标记：Splash；消耗/限制：SP 15；弹药数 1；武器 Bow；弹药 Arrow。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/chargearrow.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/chargearrow.cpp:10
void SkillChargeArrow::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const
// src/map/skills/archer/chargearrow.cpp:12
base_skillratio += 50;
// src/map/skills/archer/skill_factory_archer.cpp:141
case AC_CONCENTRATION:
// src/map/skills/archer/skill_factory_archer.cpp:142
return std::make_unique<SkillConcentration>();
```
