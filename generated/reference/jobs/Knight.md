# Knight 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

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
| 55 | `KN_SPEARMASTERY` | Spear Mastery | 10 | Knight | 是 | — | Weapon / Passive |
| 56 | `KN_PIERCE` | Pierce | 10 | Knight | 是 | KN_SPEARMASTERY Lv1 | Weapon / Attack |
| 57 | `KN_BRANDISHSPEAR` | Brandish Spear | 10 | Knight | 是 | KN_RIDING Lv1, KN_SPEARSTAB Lv3 | Weapon / Attack |
| 58 | `KN_SPEARSTAB` | Spear Stab | 10 | Knight | 是 | KN_PIERCE Lv5 | Weapon / Attack |
| 59 | `KN_SPEARBOOMERANG` | Spear Boomerang | 5 | Knight | 是 | KN_PIERCE Lv3 | Weapon / Attack |
| 60 | `KN_TWOHANDQUICKEN` | Twohand Quicken | 10 | Knight | 是 | SM_TWOHAND Lv1 | Weapon / Self |
| 61 | `KN_AUTOCOUNTER` | Counter Attack | 5 | Knight | 是 | SM_TWOHAND Lv1 | Weapon / Self |
| 62 | `KN_BOWLINGBASH` | Bowling Bash | 10 | Knight | 是 | SM_BASH Lv10, SM_MAGNUM Lv3, SM_TWOHAND Lv5, KN_TWOHANDQUICKEN Lv10, KN_AUTOCOUNTER Lv5 | Weapon / Attack |
| 63 | `KN_RIDING` | Peco Peco Riding | 1 | Knight | 是 | SM_ENDURE Lv1 | Weapon / Passive |
| 64 | `KN_CAVALIERMASTERY` | Cavalier Mastery | 5 | Knight | 是 | KN_RIDING Lv1 | Weapon / Passive |
| 1001 | `KN_CHARGEATK` | Charge Attack | 1 | Knight | 是 | — | Weapon / Attack |
| 495 | `KN_ONEHAND` | Onehand Quicken | 1 | Knight | 是 | KN_TWOHANDQUICKEN Lv10 | Weapon / Self |

## 技能详情

### Spear Mastery (`KN_SPEARMASTERY`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/swordman/phantomthrust.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2339
damage += (skill * 4);
// src/map/battle.cpp:2341
damage += skill * 10;
// src/map/battle.cpp:2345
damage += (skill * 4);
// src/map/battle.cpp:2351
damage += (skill * 4);
// src/map/battle.cpp:2353
damage += (skill * 5);
// src/map/battle.cpp:2356
damage += (skill * 10);
// src/map/battle.cpp:2362
damage += (skill * 3);
// src/map/battle.cpp:2364
damage += (skill * 5);
// src/map/skills/swordman/phantomthrust.cpp:18
void SkillPhantomThrust::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
// src/map/skills/swordman/phantomthrust.cpp:19
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/swordman/phantomthrust.cpp:22
skillratio += -100 + 50 * skill_lv + 10 * (sd ? pc_checkskill(sd,KN_SPEARMASTERY) : 5);
// src/map/skills/swordman/phantomthrust.cpp:26
void SkillPhantomThrust::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Pierce (`KN_PIERCE`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-2；命中类型：Multi_Hit；段数：3；属性：Weapon；消耗/限制：SP 7；武器 1hSpear, 2hSpear。

- 技能树最高等级：`10`
- 前置技能：KN_SPEARMASTERY Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/swordman/pierce.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2942
if (skill_lv >= 7) {
// src/map/skill.cpp:2943
status_change *sc_cur = status_get_sc(src);
// src/map/skill.cpp:2945
sc_start(src,src,SC_SMA,100,skill_lv,skill_get_time(SL_SMA, skill_lv));
// src/map/skill.cpp:2948
case DK_SERVANT_W_DEMOL:// Only give servant's per target after damage calculation.
// src/map/skill.cpp:2958
sc_start(src, src, SC_CHARGINGPIERCE_COUNT, 100, sc->getSCE(SC_CHARGINGPIERCE_COUNT)->val1 + 1, skill_get_time2(DK_CHARGINGPIERCE, 1));
// src/map/skill.cpp:2959
else { // If charge count is 10, bonus damage is applied for 1 attack and then the count status ends.
// src/map/skill.cpp:2961
status_change_end(src, SC_CHARGINGPIERCE_COUNT);
// src/map/skills/swordman/pierce.cpp:11
void SkillPierce::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
// src/map/skills/swordman/pierce.cpp:17
void SkillPierce::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/swordman/pierce.cpp:18
const status_change* sc = status_get_sc(src);
// src/map/skills/swordman/pierce.cpp:20
base_skillratio += 10 * skill_lv;
```

### Brandish Spear (`KN_BRANDISHSPEAR`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-2；命中类型：Single；段数：1；属性：Weapon；范围：2；击退：2；吟唱：700 ms；持续时间1：1000 ms；伤害标记：NoDamage；消耗/限制：SP 12；武器 1hSpear, 2hSpear；状态 Riding。

- 技能树最高等级：`10`
- 前置技能：KN_RIDING Lv1, KN_SPEARSTAB Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/gloomyday.cpp`, `src/map/skills/swordman/brandishspear.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2679
case AM_DEMONSTRATION:
// src/map/skill.cpp:5112
clif_status_change(src, EFST_POSTDELAY, 1, skill_delayfix(src, ud->skill_id, ud->skill_lv), 0, 0, 0);
// src/map/skill.cpp:5119
sd->canequip_tick = tick + skill_get_time(ud->skill_id, ud->skill_lv);
// src/map/skill.cpp:5133
if (timer && timer->func == status_change_timer && DIFF_TICK(timer->tick, gettick() + skill_get_time(ud->skill_id, ud->skill_lv)) > 0)
// src/map/skill.cpp:5136
sc_start2(src, src, type, 100, 0, 1, skill_get_time(ud->skill_id, ud->skill_lv));
// src/map/skills/archer/gloomyday.cpp:13
void SkillGloomyDay::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/gloomyday.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/archer/gloomyday.cpp:17
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/archer/gloomyday.cpp:22
sc_start(src,target,SC_GLOOMYDAY_SK,100,skill_lv,skill_get_time(getSkillId(),skill_lv));
// src/map/skills/archer/gloomyday.cpp:26
sc_start(src,target,type,100,skill_lv,skill_get_time(getSkillId(),skill_lv));
// src/map/skills/swordman/brandishspear.cpp:14
void SkillBrandishSpear::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/swordman/brandishspear.cpp:17
skill_get_splash(getSkillId(), skill_lv), skill_get_maxcount(getSkillId(), skill_lv), 0, splash_target(src),
```

### Spear Stab (`KN_SPEARSTAB`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-4；命中类型：Single；段数：1；属性：Weapon；击退：6；伤害标记：Splash；消耗/限制：SP 9；武器 1hSpear, 2hSpear。

- 技能树最高等级：`10`
- 前置技能：KN_PIERCE Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/skill_factory_swordman.cpp`, `src/map/skills/swordman/spearstab.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/spearstab.cpp:11
void SkillSpearStab::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
// src/map/skills/swordman/spearstab.cpp:15
void SkillSpearStab::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/swordman/spearstab.cpp:19
if (skill_attack(BF_WEAPON,src,src,target,getSkillId(), skill_lv, tick, SD_ANIMATION))
```

### Spear Boomerang (`KN_SPEARBOOMERANG`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：Lv1=3; Lv2=5; Lv3=7; Lv4=9; Lv5=11；命中类型：Single；段数：1；属性：Weapon；技能后摇：1000 ms；消耗/限制：SP 10；武器 1hSpear, 2hSpear。

- 技能树最高等级：`5`
- 前置技能：KN_PIERCE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/skill_factory_swordman.cpp`, `src/map/skills/swordman/spearboomerang.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/spearboomerang.cpp:9
void SkillSpearBoomerang::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/swordman/spearboomerang.cpp:10
base_skillratio += 50 * skill_lv;
```

### Twohand Quicken (`KN_TWOHANDQUICKEN`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000; Lv6=180000; Lv7=210000; Lv8=240000; Lv9=270000; Lv10-11=300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=14; Lv2=18; Lv3=22; Lv4=26; Lv5=30; Lv6=34; Lv7=38; Lv8=42; Lv9=46; Lv10=50；武器 2hSword；关联状态：TwoHandQuicken。

- 技能树最高等级：`10`
- 前置技能：SM_TWOHAND Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/skill_factory_swordman.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Counter Attack (`KN_AUTOCOUNTER`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；属性：Weapon；持续时间1：Lv1=400; Lv2=800; Lv3=1200; Lv4=1600; Lv5=2000 ms；伤害标记：IgnoreDefense, Critical；消耗/限制：SP 3；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；关联状态：AutoCounter。

- 技能树最高等级：`5`
- 前置技能：SM_TWOHAND Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/swordman/counterattack.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3061
cri -= tstatus->luk * ((!sd && tsd) ? 3 : 2);
// src/map/battle.cpp:3064
cri *= 2;
// src/map/battle.cpp:3071
status_change_end(src, SC_AUTOCOUNTER);
// src/map/battle.cpp:3078
cri *= 2;
// src/map/battle.cpp:3083
cri += 300; // !TODO: Confirm new bonus
// src/map/battle.cpp:3085
cri += 200;
// src/map/battle.cpp:4424
skillratio += sd->bonus.skill_ratio;
// src/map/battle.cpp:4426
skillratio += sc->getSCE(SC_OVERTHRUST)->val3;
// src/map/battle.cpp:4428
skillratio += sc->getSCE(SC_MAXOVERTHRUST)->val2;
// src/map/battle.cpp:4431
skillratio += 100;
// src/map/battle.cpp:4433
skillratio += 200;
// src/map/battle.cpp:4436
if (const status_change_entry* sce = sc->getSCE(SC_POISONREACT); sce != nullptr && sce->val4 == 1) {
```

### Bowling Bash (`KN_BOWLINGBASH`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-2；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：1；吟唱：700 ms；伤害标记：Splash；消耗/限制：SP Lv1=13; Lv2=14; Lv3=15; Lv4=16; Lv5=17; Lv6=18; Lv7=19; Lv8=20; Lv9=21; Lv10=22。

- 技能树最高等级：`10`
- 前置技能：SM_BASH Lv10, SM_MAGNUM Lv3, SM_TWOHAND Lv5, KN_TWOHANDQUICKEN Lv10, KN_AUTOCOUNTER Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/bowlingbash.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/bowlingbash.cpp:16
void SkillBowlingBash::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
// src/map/skills/swordman/bowlingbash.cpp:18
const map_session_data* sd = BL_CAST(BL_PC, &src);
```

### Peco Peco Riding (`KN_RIDING`)

武器/物理技能；目标：被动；最高等级 1。

- 技能树最高等级：`1`
- 前置技能：SM_ENDURE Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/status.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Cavalier Mastery (`KN_CAVALIERMASTERY`)

武器/物理技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：KN_RIDING Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:2384
temp_aspd = status->dex * status->dex / 5.0f + status->agi * status->agi * 0.5f;
// src/map/status.cpp:2387
temp_aspd = (float)(sqrt(temp_aspd) * 0.25f) + 196;
// src/map/status.cpp:2388
if ((skill_lv = pc_checkskill(sd,SA_ADVANCEDBOOK)) > 0 && sd->status.weapon == W_BOOK)
// src/map/status.cpp:2389
val += (skill_lv - 1) / 2 + 1;
// src/map/status.cpp:2390
if ((skill_lv = pc_checkskill(sd, SG_DEVIL)) > 0 && ((sd->class_&MAPID_THIRDMASK) == MAPID_STAR_EMPEROR || pc_is_maxjoblv(sd)))
// src/map/status.cpp:2391
val += 1 + skill_lv;
// src/map/status.cpp:2392
if ((skill_lv = pc_checkskill(sd,GS_SINGLEACTION)) > 0 && (sd->status.weapon >= W_REVOLVER && sd->status.weapon <= W_GRENADE))
// src/map/status.cpp:2393
val += ((skill_lv + 1) / 2);
// src/map/status.cpp:2398
aspd = ((int32)(temp_aspd + ((float)(status_calc_aspd(sd, &sd->sc, true) + val) * status->agi / 200)) - min(aspd, 200));
// src/map/status.cpp:2399
return aspd;
// src/map/status.cpp:2402
return AMOTION_ZERO_ASPD;
// src/map/status.cpp:2406
? (job->aspd_base[sd->status.weapon]) // Single weapon
```

### Charge Attack (`KN_CHARGEATK`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：14；命中类型：Single；段数：1；属性：Weapon；吟唱：500 ms；消耗/限制：SP 40。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/chargeattack.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/chargeattack.cpp:16
void SkillChargeAttack::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/swordman/chargeattack.cpp:19
int32 dist = skill_get_blewcount(getSkillId(), skill_lv);
// src/map/skills/swordman/chargeattack.cpp:22
int32 dist = static_cast<int32>(distance_math_bl(src, target));
```

### Onehand Quicken (`KN_ONEHAND`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP 100；武器 1hSword；关联状态：OneHand。

- 技能树最高等级：`1`
- 前置技能：KN_TWOHANDQUICKEN Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/skill_factory_swordman.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。
