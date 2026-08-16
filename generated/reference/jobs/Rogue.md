# Rogue 技能

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
| 2 | `SM_SWORD` | Sword Mastery | 10 | Rogue | 是 | — | Weapon / Passive |
| 44 | `AC_VULTURE` | Vulture's Eye | 10 | Rogue | 是 | — | None / Passive |
| 46 | `AC_DOUBLE` | Double Strafe | 10 | Rogue | 是 | AC_VULTURE Lv10 | Weapon / Attack |
| 124 | `HT_REMOVETRAP` | Remove Trap | 1 | Rogue | 是 | AC_DOUBLE Lv5 | Misc / Trap |
| 210 | `RG_SNATCHER` | Gank | 10 | Rogue | 是 | TF_STEAL Lv1 | Weapon / Passive |
| 211 | `RG_STEALCOIN` | Mug | 10 | Rogue | 是 | RG_SNATCHER Lv4 | Weapon / Attack |
| 212 | `RG_BACKSTAP` | Back Stab | 10 | Rogue | 是 | RG_STEALCOIN Lv4 | Weapon / Attack |
| 213 | `RG_TUNNELDRIVE` | Stalk | 5 | Rogue | 是 | TF_HIDING Lv1 | None / Passive |
| 214 | `RG_RAID` | Sightless Mind | 5 | Rogue | 是 | RG_BACKSTAP Lv2, RG_TUNNELDRIVE Lv2 | Weapon / Self |
| 215 | `RG_STRIPWEAPON` | Divest Weapon | 5 | Rogue | 是 | RG_STRIPARMOR Lv5 | Weapon / Attack |
| 216 | `RG_STRIPSHIELD` | Divest Shield | 5 | Rogue | 是 | RG_STRIPHELM Lv5 | Weapon / Attack |
| 217 | `RG_STRIPARMOR` | Divest Armor | 5 | Rogue | 是 | RG_STRIPSHIELD Lv5 | Weapon / Attack |
| 218 | `RG_STRIPHELM` | Divest Helm | 5 | Rogue | 是 | RG_STEALCOIN Lv2 | Weapon / Attack |
| 219 | `RG_INTIMIDATE` | Snatch | 5 | Rogue | 是 | RG_BACKSTAP Lv4, RG_RAID Lv5 | Weapon / Attack |
| 220 | `RG_GRAFFITI` | Scribble | 1 | Rogue | 是 | RG_FLAGGRAFFITI Lv5 | None / Ground |
| 221 | `RG_FLAGGRAFFITI` | Piece | 5 | Rogue | 是 | RG_CLEANER Lv1 | None / Ground |
| 222 | `RG_CLEANER` | Remover | 1 | Rogue | 是 | RG_GANGSTER Lv1 | None / Ground |
| 223 | `RG_GANGSTER` | Slyness | 1 | Rogue | 是 | RG_STRIPSHIELD Lv3 | None / Passive |
| 224 | `RG_COMPULSION` | Haggle | 5 | Rogue | 是 | RG_GANGSTER Lv1 | None / Passive |
| 225 | `RG_PLAGIARISM` | Intimidate | 10 | Rogue | 是 | RG_INTIMIDATE Lv5 | None / Passive |
| 1005 | `RG_CLOSECONFINE` | Close Confine | 1 | Rogue | 是 | — | Weapon / Attack |

## 技能详情

### Sword Mastery (`SM_SWORD`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2335
damage += (skill * 3);
// src/map/battle.cpp:2339
damage += (skill * 4);
// src/map/battle.cpp:2341
damage += skill * 10;
// src/map/battle.cpp:2345
damage += (skill * 4);
```

### Vulture's Eye (`AC_VULTURE`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
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

### Double Strafe (`AC_DOUBLE`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-9；命中类型：Multi_Hit；段数：2；属性：Weapon；持续时间1：100 ms；消耗/限制：SP 12；弹药数 1；武器 Bow；弹药 Arrow。

- 技能树最高等级：`10`
- 前置技能：AC_VULTURE Lv10
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

### Remove Trap (`HT_REMOVETRAP`)

特殊技能；目标：陷阱；最高等级 1；射程：2；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 5。

- 技能树最高等级：`1`
- 前置技能：AC_DOUBLE Lv5
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

### Gank (`RG_SNATCHER`)

武器/物理技能；目标：被动；最高等级 10；属性：Weapon。

- 技能树最高等级：`10`
- 前置技能：TF_STEAL Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:1373
int32 rate = sstatus->con * 10 / 3 + 1;
// src/map/skill.cpp:1375
rate += rate * (20 * pc_checkskill(sd, WH_NATUREFRIENDLY)) / 100;
// src/map/skill.cpp:1377
if (rnd() % 1000 <= rate)
// src/map/skill.cpp:1378
skill_castend_damage_id(src, bl, WH_HAWKRUSH, skill, tick, 0);
// src/map/skill.cpp:1385
clif_skill_nodamage(src,*bl,TF_STEAL,skill);
// src/map/skill.cpp:1392
struct status_change_entry *sce;
// src/map/skill.cpp:1394
if((sce=sc->getSCE(SC_ENCPOISON))) //Don't use sc_start since chance comes in 1/10000 rate.
// src/map/skill.cpp:1395
status_change_start(src,bl,SC_POISON,sce->val2, sce->val1,src->id,0,0,
// src/map/skill.cpp:1396
skill_get_time2(AS_ENCHANTPOISON,sce->val1),SCSTART_NONE);
// src/map/skill.cpp:1399
sc_start4(src,bl,SC_DPOISON,sce->val2, sce->val1,src->id,0,0,
```

### Mug (`RG_STEALCOIN`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：1；命中类型：Single；段数：1；技能后摇：500 ms；伤害标记：NoDamage；消耗/限制：SP 15。

- 技能树最高等级：`10`
- 前置技能：RG_SNATCHER Lv4
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/mug.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/thief/mug.cpp:17
void SkillMug::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/thief/mug.cpp:18
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/thief/mug.cpp:19
mob_data *dstmd = BL_CAST(BL_MOB, target);
// src/map/skills/thief/mug.cpp:25
int32 rate = 10 * pc_checkskill(sd, RG_STEALCOIN);
// src/map/skills/thief/mug.cpp:26
rate += sd->battle_status.dex / 2;
// src/map/skills/thief/mug.cpp:27
rate += sd->battle_status.luk / 2;
// src/map/skills/thief/mug.cpp:28
rate += 2 * (sd->status.base_level - target_lv);
// src/map/skills/thief/mug.cpp:30
if (!rnd_chance_official(rate, 1000))
```

### Back Stab (`RG_BACKSTAP`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-1；命中类型：Single；段数：1；属性：Weapon；技能后摇：500 ms；伤害标记：IgnoreFlee；消耗/限制：SP 16；关联状态：Stun。

- 技能树最高等级：`10`
- 前置技能：RG_STEALCOIN Lv4
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/backstab.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:4643
return USESKILL_FAIL_MAX; // Don't show a skill fail message (NoDamage type doesn't consume requirements)
// src/map/skill.cpp:4646
case AL_HEAL:
// src/map/skill.cpp:4651
case AB_HIGHNESSHEAL:
// src/map/skills/thief/backstab.cpp:14
void SkillBackStab::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
// src/map/skills/thief/backstab.cpp:16
const map_session_data* sd = BL_CAST(BL_PC, &src);
// src/map/skills/thief/backstab.cpp:23
void SkillBackStab::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
```

### Stalk (`RG_TUNNELDRIVE`)

非伤害技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：TF_HIDING Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:8059
speed_rate -= val;
```

### Sightless Mind (`RG_RAID`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；属性：Weapon；范围：1；持续时间1：5000 ms；持续时间2：30000 ms；伤害标记：Splash；消耗/限制：SP 20；前置状态 Hiding；关联状态：Stun。

- 技能树最高等级：`5`
- 前置技能：RG_BACKSTAP Lv2, RG_TUNNELDRIVE Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/thief/sightlessmind.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/thief/sightlessmind.cpp:11
SkillSightlessMind::SkillSightlessMind() : SkillImplRecursiveDamageSplash(RG_RAID) {
// src/map/skills/thief/sightlessmind.cpp:14
void SkillSightlessMind::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/thief/sightlessmind.cpp:16
base_skillratio += -100 + 50 + skill_lv * 150;
// src/map/skills/thief/sightlessmind.cpp:18
base_skillratio += 40 * skill_lv;
// src/map/skills/thief/sightlessmind.cpp:22
void SkillSightlessMind::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Divest Weapon (`RG_STRIPWEAPON`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：Lv1=75000; Lv2=90000; Lv3=105000; Lv4=120000; Lv5=135000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=17; Lv2=19; Lv3=21; Lv4=23; Lv5=25；关联状态：StripWeapon。

- 技能树最高等级：`5`
- 前置技能：RG_STRIPARMOR Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/divestweapon.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

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
// src/map/skill.cpp:2134
if (rnd()%mod >= rate)
// src/map/skill.cpp:2137
switch (skill_id) { // Duration
// src/map/skill.cpp:2140
time = skill_get_time(skill_id, skill_lv);
// src/map/skill.cpp:2151
time = skill_get_time2(skill_id, skill_lv);
// src/map/skill.cpp:2153
time = skill_get_time(skill_id, skill_lv);
// src/map/skill.cpp:2156
time += max(1, skill_lv + 500 * (sstatus->dex - tstatus->dex));
```

### Divest Shield (`RG_STRIPSHIELD`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：Lv1=75000; Lv2=90000; Lv3=105000; Lv4=120000; Lv5=135000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20；关联状态：StripShield。

- 技能树最高等级：`5`
- 前置技能：RG_STRIPHELM Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/divestshield.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

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
// src/map/skill.cpp:2134
if (rnd()%mod >= rate)
// src/map/skill.cpp:2137
switch (skill_id) { // Duration
// src/map/skill.cpp:2140
time = skill_get_time(skill_id, skill_lv);
// src/map/skill.cpp:2151
time = skill_get_time2(skill_id, skill_lv);
// src/map/skill.cpp:2153
time = skill_get_time(skill_id, skill_lv);
// src/map/skill.cpp:2156
time += max(1, skill_lv + 500 * (sstatus->dex - tstatus->dex));
```

### Divest Armor (`RG_STRIPARMOR`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：Lv1=75000; Lv2=90000; Lv3=105000; Lv4=120000; Lv5=135000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=17; Lv2=19; Lv3=21; Lv4=23; Lv5=25；关联状态：StripArmor。

- 技能树最高等级：`5`
- 前置技能：RG_STRIPSHIELD Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/divestarmor.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

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
// src/map/skill.cpp:2134
if (rnd()%mod >= rate)
// src/map/skill.cpp:2137
switch (skill_id) { // Duration
// src/map/skill.cpp:2140
time = skill_get_time(skill_id, skill_lv);
// src/map/skill.cpp:2151
time = skill_get_time2(skill_id, skill_lv);
// src/map/skill.cpp:2153
time = skill_get_time(skill_id, skill_lv);
// src/map/skill.cpp:2156
time += max(1, skill_lv + 500 * (sstatus->dex - tstatus->dex));
```

### Divest Helm (`RG_STRIPHELM`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：Lv1=75000; Lv2=90000; Lv3=105000; Lv4=120000; Lv5=135000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20；关联状态：StripHelm。

- 技能树最高等级：`5`
- 前置技能：RG_STEALCOIN Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/divesthelm.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

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
// src/map/skill.cpp:2134
if (rnd()%mod >= rate)
// src/map/skill.cpp:2137
switch (skill_id) { // Duration
// src/map/skill.cpp:2140
time = skill_get_time(skill_id, skill_lv);
// src/map/skill.cpp:2151
time = skill_get_time2(skill_id, skill_lv);
// src/map/skill.cpp:2153
time = skill_get_time(skill_id, skill_lv);
// src/map/skill.cpp:2156
time += max(1, skill_lv + 500 * (sstatus->dex - tstatus->dex));
```

### Snatch (`RG_INTIMIDATE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：1；命中类型：Single；段数：1；属性：Weapon；消耗/限制：SP Lv1=13; Lv2=16; Lv3=19; Lv4=22; Lv5=25。

- 技能树最高等级：`5`
- 前置技能：RG_BACKSTAP Lv4, RG_RAID Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`, `src/map/skills/thief/snatch.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:3238
if (!rmdamage) {
// src/map/skill.cpp:3239
clif_skill_damage( *e_bl, *e_bl, gettick(), 0, 0, damage, dmg.div_, skill_id, -1, skill_get_hit(skill_id) );
// src/map/skill.cpp:3240
battle_fix_damage(src, e_bl, damage, 0, 0);
// src/map/skill.cpp:3242
clif_skill_damage( *bl, *bl, gettick(), 0, 0, damage, dmg.div_, skill_id, -1, skill_get_hit(skill_id) );
// src/map/skill.cpp:3243
battle_fix_damage(bl, bl, damage, 0, 0);
// src/map/skill.cpp:3249
if(damage > 0 && !status_has_mode(tstatus,MD_STATUSIMMUNE)) {
// src/map/skill.cpp:3251
int32 rate = 50 + skill_lv * 5;
// src/map/skill.cpp:3252
rate = rate + (status_get_lv(src) - status_get_lv(bl));
// src/map/skill.cpp:3253
if(rnd()%100 < rate)
// src/map/skill.cpp:3254
skill_addtimerskill(src,tick + 800,bl->id,0,0,skill_id,skill_lv,0,flag);
// src/map/skill.cpp:3259
skill_addtimerskill(bl,tick + 800,bl->id,x,y,skill_id,skill_lv,0,flag);
// src/map/skill.cpp:3692
clif_skill_damage( *src, *src, tick, status_get_amotion(src), 0, DMGVAL_IGNORE, 1, skl->skill_id, skl->skill_lv, DMG_SINGLE );
```

### Scribble (`RG_GRAFFITI`)

非伤害技能；目标：地面区域；最高等级 1；射程：1；命中类型：Single；段数：1；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 15；道具 Red_Gemstone×1。

- 技能树最高等级：`1`
- 前置技能：RG_FLAGGRAFFITI Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/scribble.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:6198
sd->skill_lv_dance = skill_lv;
// src/map/skill.cpp:8362
if (skill_check_pc_partner(&sd, skill_id, &skill_lv, 1, 0) < 1 && !(sc && sc->getSCE(SC_KVASIR_SONATA))) {
// src/map/skill.cpp:8370
if (map_foreachinmap(skill_graffitiremover,sd.m,BL_SKILL,0)) { // If a previous Graffiti exists skill fails to cast.
// src/map/skill.cpp:8381
case SA_CASTCANCEL:
// src/map/skills/thief/scribble.cpp:9
void SkillScribble::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/thief/scribble.cpp:10
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Piece (`RG_FLAGGRAFFITI`)

非伤害技能；目标：地面区域；最高等级 5；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 10。

- 技能树最高等级：`5`
- 前置技能：RG_CLEANER Lv1
- 公式覆盖：`metadata-only` / `metadata-only`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Remover (`RG_CLEANER`)

非伤害技能；目标：地面区域；最高等级 1；射程：1；命中类型：Single；段数：1；范围：5；伤害标记：NoDamage, Splash；消耗/限制：SP 5。

- 技能树最高等级：`1`
- 前置技能：RG_GANGSTER Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/thief/remover.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/thief/remover.cpp:11
void SkillRemover::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/thief/remover.cpp:12
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/thief/remover.cpp:15
void SkillRemover::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/thief/remover.cpp:16
int32 i = skill_get_splash(getSkillId(), skill_lv);
```

### Slyness (`RG_GANGSTER`)

非伤害技能；目标：被动；最高等级 1；范围：1。

- 技能树最高等级：`1`
- 前置技能：RG_STRIPSHIELD Lv3
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:10799
status_calc_regen_rate(bl, &sd->regen, &sd->sc);
```

### Haggle (`RG_COMPULSION`)

非伤害技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：RG_GANGSTER Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:5691
int32 skill,val = orig_value,rate1 = 0,rate2 = 0;
// src/map/pc.cpp:5693
rate1 = 5+skill*2-((skill==10)? 1:0);
// src/map/pc.cpp:5695
rate2 = 5+skill*4;
// src/map/pc.cpp:5696
if(rate1 < rate2) rate1 = rate2;
// src/map/pc.cpp:5697
if(rate1)
// src/map/pc.cpp:5698
val = (int32)((double)orig_value*(double)(100-rate1)/100.);
```

### Intimidate (`RG_PLAGIARISM`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：RG_INTIMIDATE Lv5
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:2396
if ((j = static_cast<uint16>(pc_readglobalreg(sd, add_str(sg_info[i].feel_var)))) != 0) {
// src/map/pc.cpp:2403
sd->hate_mob[i] = static_cast<int16>(pc_readglobalreg(sd, add_str(sg_info[i].hate_var)))-1;
// src/map/pc.cpp:2407
uint16 skid = static_cast<uint16>(pc_readglobalreg(sd, add_str(SKILL_VAR_PLAGIARISM)));
// src/map/pc.cpp:2411
sd->status.skill[sd->cloneskill_idx].lv = static_cast<uint8>(pc_readglobalreg(sd, add_str(SKILL_VAR_PLAGIARISM_LV)));
// src/map/pc.cpp:2418
uint16 skid = static_cast<uint16>(pc_readglobalreg(sd, add_str(SKILL_VAR_REPRODUCE)));
// src/map/skill.cpp:812
* Check if the skill is ok to cast and when.
// src/map/skill.cpp:813
* Done before skill_check_condition_castbegin, requirement
// src/map/skill.cpp:814
* @param skill_id: Skill ID that casted
// src/map/skill.cpp:815
* @param sd: Player who casted
// src/map/skill.cpp:2530
* @param src: The caster
// src/map/skill.cpp:2532
* @param skill_id: Skill that casted
// src/map/skill.cpp:2533
* @param skill_lv: Skill level of the casted skill
```

### Close Confine (`RG_CLOSECONFINE`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：1；命中类型：Single；段数：1；持续时间1：10000 ms；伤害标记：NoDamage；消耗/限制：SP 25；关联状态：CloseConfine2。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/thief/closeconfine.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/thief/closeconfine.cpp:12
void SkillCloseConfine::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/thief/closeconfine.cpp:15
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
// src/map/skills/thief/closeconfine.cpp:16
sc_start4(src,target,type,100,skill_lv,src->id,0,0,skill_get_time(getSkillId(),skill_lv)));
```
