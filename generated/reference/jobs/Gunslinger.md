# Gunslinger 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 500 | `GS_GLITTERING` | Flip the Coin | 5 | Gunslinger | 是 | — | Misc / Self |
| 501 | `GS_FLING` | Fling | 1 | Gunslinger | 是 | GS_GLITTERING Lv1 | Misc / Attack |
| 502 | `GS_TRIPLEACTION` | Triple Action | 1 | Gunslinger | 是 | GS_GLITTERING Lv1, GS_CHAINACTION Lv10 | Weapon / Attack |
| 503 | `GS_BULLSEYE` | Bulls Eye | 1 | Gunslinger | 是 | GS_GLITTERING Lv5, GS_TRACKING Lv10 | Weapon / Attack |
| 504 | `GS_MADNESSCANCEL` | Madness Canceller | 1 | Gunslinger | 是 | GS_GLITTERING Lv4, GS_GATLINGFEVER Lv10 | Weapon / Self |
| 505 | `GS_ADJUSTMENT` | Adjustment | 1 | Gunslinger | 是 | GS_GLITTERING Lv4, GS_DISARM Lv5 | Weapon / Self |
| 506 | `GS_INCREASING` | Increasing Accuracy | 1 | Gunslinger | 是 | GS_GLITTERING Lv2, GS_SNAKEEYE Lv10 | Weapon / Self |
| 507 | `GS_MAGICALBULLET` | Magical Bullet | 1 | Gunslinger | 是 | GS_GLITTERING Lv1 | Weapon / Attack |
| 508 | `GS_CRACKER` | Cracker | 1 | Gunslinger | 是 | GS_GLITTERING Lv1 | Weapon / Attack |
| 509 | `GS_SINGLEACTION` | Single Action | 10 | Gunslinger | 是 | — | None / Passive |
| 510 | `GS_SNAKEEYE` | Snake Eye | 10 | Gunslinger | 是 | — | None / Passive |
| 511 | `GS_CHAINACTION` | Chain Action | 10 | Gunslinger | 是 | GS_SINGLEACTION Lv1 | Weapon / Passive |
| 512 | `GS_TRACKING` | Tracking | 10 | Gunslinger | 是 | GS_SINGLEACTION Lv5 | Weapon / Attack |
| 513 | `GS_DISARM` | Disarm | 5 | Gunslinger | 是 | GS_TRACKING Lv7 | Weapon / Attack |
| 514 | `GS_PIERCINGSHOT` | Piercing Shot | 5 | Gunslinger | 是 | GS_TRACKING Lv5 | Weapon / Attack |
| 515 | `GS_RAPIDSHOWER` | Rapid Shower | 10 | Gunslinger | 是 | GS_CHAINACTION Lv3 | Weapon / Attack |
| 516 | `GS_DESPERADO` | Desperado | 10 | Gunslinger | 是 | GS_RAPIDSHOWER Lv5 | Weapon / Self |
| 517 | `GS_GATLINGFEVER` | Gatling Fever | 10 | Gunslinger | 是 | GS_RAPIDSHOWER Lv7, GS_DESPERADO Lv5 | Weapon / Self |
| 518 | `GS_DUST` | Dust | 10 | Gunslinger | 是 | GS_SINGLEACTION Lv5 | Weapon / Attack |
| 519 | `GS_FULLBUSTER` | Full Buster | 10 | Gunslinger | 是 | GS_DUST Lv3 | Weapon / Attack |
| 520 | `GS_SPREADATTACK` | Spread Attack | 10 | Gunslinger | 是 | GS_FULLBUSTER Lv5 | Weapon / Attack |
| 521 | `GS_GROUNDDRIFT` | Ground Drift | 10 | Gunslinger | 是 | GS_SPREADATTACK Lv7 | Weapon / Ground |

## 技能详情

### Flip the Coin (`GS_GLITTERING`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：600000 ms；伤害标记：NoDamage, IgnoreFlee；消耗/限制：SP 2；Zeny 1。

- 技能树最高等级：`5`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/gunslinger/glittering.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:8677
if (status->hp < (status->hp/100)) {
// src/map/skill.cpp:8679
if (status->hp < 2) {
// src/map/skills/gunslinger/glittering.cpp:12
void SkillGlittering::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/gunslinger/glittering.cpp:13
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/gunslinger/glittering.cpp:16
clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
// src/map/skills/gunslinger/glittering.cpp:17
if (rnd() % 100 < (20 + 10 * skill_lv))
// src/map/skills/gunslinger/glittering.cpp:18
pc_addspiritball(sd, skill_get_time(getSkillId(), skill_lv), 10);
```

### Fling (`GS_FLING`)

特殊技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Weapon；持续时间1：30000 ms；伤害标记：IgnoreElement, IgnoreFlee；消耗/限制：SP 10；气弹 5；关联状态：Fling。

- 技能树最高等级：`1`
- 前置技能：GS_GLITTERING Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/gunslinger/fling.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6523
md.damage += (md.damage * (((i + 1) * 10) / 5)) / 10;
// src/map/battle.cpp:6527
md.damage -= totaldef;
// src/map/battle.cpp:6533
md.damage = (sd ? sd->status.job_level : status_get_lv(src));
// src/map/battle.cpp:6536
md.damage = (int64)sstatus->max_hp * (50 + 50 * skill_lv) / 100;
// src/map/battle.cpp:6541
md.damage = skill_lv * status_get_dex(src) + status_get_int(src) * 5 ;
// src/map/battle.cpp:6544
int32 researchskill_lv = pc_checkskill(sd,RA_RESEARCHTRAP);
// src/map/skill.cpp:8416
skill_lv += sc->getSCE(SC_RAISINGDRAGON)->val1;
// src/map/skill.cpp:8417
if(sd.spiritball >= skill_lv) {
// src/map/skills/gunslinger/fling.cpp:12
void SkillFling::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/gunslinger/fling.cpp:13
skill_attack(skill_get_type(getSkillId()), src, src, target, getSkillId(), skill_lv, tick, flag);
// src/map/skills/gunslinger/fling.cpp:16
void SkillFling::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/gunslinger/fling.cpp:17
map_session_data *sd = BL_CAST(BL_PC, src);
```

### Triple Action (`GS_TRIPLEACTION`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Multi_Hit；段数：3；属性：Weapon；消耗/限制：SP 20；弹药数 1；气弹 1；弹药 Arrow, Dagger, Bullet, Shell, Grenade, Shuriken, Kunai, Cannonball, Throwweapon。

- 技能树最高等级：`1`
- 前置技能：GS_GLITTERING Lv1, GS_CHAINACTION Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/skill_factory_gunslinger.cpp`, `src/map/skills/gunslinger/tripleaction.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/gunslinger/tripleaction.cpp:9
void SkillTripleAction::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/gunslinger/tripleaction.cpp:10
base_skillratio += 50 * skill_lv;
```

### Bulls Eye (`GS_BULLSEYE`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Single；段数：1；属性：Weapon；吟唱：500 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP 30；弹药数 1；气弹 1；弹药 Arrow, Dagger, Bullet, Shell, Grenade, Shuriken, Kunai, Cannonball, Throwweapon。

- 技能树最高等级：`1`
- 前置技能：GS_GLITTERING Lv5, GS_TRACKING Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/bullseye.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/gunslinger/bullseye.cpp:11
void SkillBullseye::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/gunslinger/bullseye.cpp:17
base_skillratio += 400;
// src/map/skills/gunslinger/bullseye.cpp:20
void SkillBullseye::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
```

### Madness Canceller (`GS_MADNESSCANCEL`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：3000 ms；技能后摇：4000 ms；持续时间1：15000 ms；伤害标记：NoDamage；消耗/限制：SP 30；气弹 4；关联状态：MadnessCancel。

- 技能树最高等级：`1`
- 前置技能：GS_GLITTERING Lv4, GS_GATLINGFEVER Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Adjustment (`GS_ADJUSTMENT`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP 15；气弹 2；关联状态：Adjustment。

- 技能树最高等级：`1`
- 前置技能：GS_GLITTERING Lv4, GS_DISARM Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Increasing Accuracy (`GS_INCREASING`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；技能后摇：1000 ms；持续时间1：60000 ms；伤害标记：NoDamage；消耗/限制：SP 30；气弹 4；关联状态：Increasing。

- 技能树最高等级：`1`
- 前置技能：GS_GLITTERING Lv2, GS_SNAKEEYE Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Magical Bullet (`GS_MAGICALBULLET`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Single；段数：1；属性：Ghost；消耗/限制：SP 7；气弹 1。

- 技能树最高等级：`1`
- 前置技能：GS_GLITTERING Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4503
bonus += static_cast<decltype(bonus)>(pow(skill_lv + sd->inventory.u.items_inventory[index].refine, 2));
// src/map/battle.cpp:4505
atk = max(100, rnd_value(100, bonus));
// src/map/battle.cpp:4511
if (sstatus->matk_max > sstatus->matk_min)
// src/map/battle.cpp:4512
atk = sstatus->matk_min + rnd()%(sstatus->matk_max - sstatus->matk_min);
// src/map/battle.cpp:4514
atk = sstatus->matk_min;
// src/map/battle.cpp:4520
atk = 40 * pc_checkskill(sd, RA_RESEARCHTRAP);
```

### Cracker (`GS_CRACKER`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Single；段数：1；属性：Weapon；技能后摇：1000 ms；持续时间2：5000 ms；伤害标记：NoDamage；消耗/限制：SP 10；弹药数 1；气弹 1；弹药 Arrow, Dagger, Bullet, Shell, Grenade, Shuriken, Kunai, Cannonball, Throwweapon；关联状态：Stun。

- 技能树最高等级：`1`
- 前置技能：GS_GLITTERING Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/cracker.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/gunslinger/cracker.cpp:12
void SkillCracker::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/gunslinger/cracker.cpp:13
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/gunslinger/cracker.cpp:14
map_session_data *dstsd = BL_CAST(BL_PC, target);
// src/map/skills/gunslinger/cracker.cpp:15
mob_data *dstmd = BL_CAST(BL_MOB, target);
// src/map/skills/gunslinger/cracker.cpp:19
int32 i = 65 - 5 * distance_bl(src, target); // Base rate
```

### Single Action (`GS_SINGLEACTION`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:2381
temp_aspd = status->dex * status->dex / 7.0f + status->agi * status->agi * 0.5f;
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
```

### Snake Eye (`GS_SNAKEEYE`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:4483
base_status->hit += skill*2;
// src/map/status.cpp:4487
base_status->hit += skill;
// src/map/status.cpp:4494
base_status->hit += 2*skill;
// src/map/status.cpp:4496
base_status->hit += skill;
// src/map/status.cpp:4501
base_status->hit += skill * 3;
// src/map/status.cpp:4503
base_status->hit += skill * 2;
// src/map/status.cpp:4505
base_status->hit += 20;
// src/map/status.cpp:4507
base_status->hit += skill * 3;
```

### Chain Action (`GS_CHAINACTION`)

武器/物理技能；目标：被动；最高等级 10；射程：-9；命中类型：Multi_Hit；段数：2；属性：Weapon。

- 技能树最高等级：`10`
- 前置技能：GS_SINGLEACTION Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/mob.cpp`, `src/map/skill.cpp`, `src/map/skills/gunslinger/chainaction.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3030
if( sstatus->cri )
// src/map/battle.cpp:3032
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/battle.cpp:3034
if(wd->type == DMG_MULTI_HIT){	//Multiple Hit Attack Skills.
// src/map/battle.cpp:3043
status_change *sc = status_get_sc(src);
// src/map/battle.cpp:3044
const status_change *tsc = status_get_sc(target);
// src/map/battle.cpp:3045
const map_session_data *tsd = BL_CAST(BL_PC, target);
// src/map/battle.cpp:3046
int16 cri = sstatus->cri;
// src/map/battle.cpp:4322
max_rate = max(7 * skill_lv, sd->bonus.double_rate);
// src/map/battle.cpp:4324
max_rate = max(5 * skill_lv, sd->bonus.double_rate);
// src/map/battle.cpp:4327
if( rnd()%100 < max_rate ) {
// src/map/battle.cpp:4328
wd->div_ = skill_get_num(TF_DOUBLE,skill_lv?skill_lv:1);
// src/map/battle.cpp:4332
if( wd->div_ == 1 && ((sd->weapontype1 == W_REVOLVER && (skill_lv = pc_checkskill(sd,GS_CHAINACTION)) > 0) //Normal Chain Action effect
```

### Tracking (`GS_TRACKING`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-9；命中类型：Single；段数：1；属性：Weapon；吟唱：Lv1=1200; Lv2=1400; Lv3=1600; Lv4=1800; Lv5=2000; Lv6=2200; Lv7=2400; Lv8=2600; Lv9=2800; Lv10=3000 ms；消耗/限制：SP Lv1=15; Lv2=20; Lv3=25; Lv4=30; Lv5=35; Lv6=40; Lv7=45; Lv8=50; Lv9=55; Lv10=60；弹药数 1；武器 Revolver, Rifle；弹药 Bullet。

- 技能树最高等级：`10`
- 前置技能：GS_SINGLEACTION Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/skill_factory_gunslinger.cpp`, `src/map/skills/gunslinger/tracking.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/gunslinger/tracking.cpp:9
void SkillTracking::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/gunslinger/tracking.cpp:10
base_skillratio += 100 * (skill_lv + 1);
```

### Disarm (`GS_DISARM`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：-9；命中类型：Single；段数：1；属性：Weapon；持续时间1：30000 ms；消耗/限制：SP Lv1=15; Lv2=20; Lv3=25; Lv4=30; Lv5=35；弹药数 1；武器 Revolver, Rifle；弹药 Bullet；关联状态：StripWeapon。

- 技能树最高等级：`5`
- 前置技能：GS_TRACKING Lv7
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/gunslinger/disarm.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
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
// src/map/skill.cpp:2120
rate = 6 * skill_lv + job_lv / 4 + sstatus->dex / 10;
// src/map/skill.cpp:2127
rate = 50 * (skill_lv + 3) + 2 * (sstatus->dex - tstatus->dex);
// src/map/skill.cpp:2134
if (rnd()%mod >= rate)
// src/map/skill.cpp:2137
switch (skill_id) { // Duration
// src/map/skill.cpp:2140
time = skill_get_time(skill_id, skill_lv);
// src/map/skill.cpp:2151
time = skill_get_time2(skill_id, skill_lv);
```

### Piercing Shot (`GS_PIERCINGSHOT`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：-9；命中类型：Single；段数：1；属性：Weapon；吟唱：1500 ms；持续时间2：120000 ms；伤害标记：IgnoreDefense；消耗/限制：SP Lv1=11; Lv2=12; Lv3=13; Lv4=14; Lv5=15；弹药数 1；武器 Revolver, Rifle；弹药 Bullet；关联状态：Bleeding。

- 技能树最高等级：`5`
- 前置技能：GS_TRACKING Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/piercingshot.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/gunslinger/piercingshot.cpp:12
void SkillPiercingShot::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/gunslinger/piercingshot.cpp:14
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/gunslinger/piercingshot.cpp:17
base_skillratio += 150 + 30 * skill_lv;
// src/map/skills/gunslinger/piercingshot.cpp:19
base_skillratio += 100 + 20 * skill_lv;
// src/map/skills/gunslinger/piercingshot.cpp:21
base_skillratio += 20 * skill_lv;
```

### Rapid Shower (`GS_RAPIDSHOWER`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-9；命中类型：Multi_Hit；段数：-5；属性：Weapon；技能后摇：1000 ms；消耗/限制：SP Lv1=22; Lv2=24; Lv3=26; Lv4=28; Lv5=30; Lv6=32; Lv7=34; Lv8=36; Lv9=38; Lv10=40；弹药数 5；武器 Revolver；弹药 Bullet。

- 技能树最高等级：`10`
- 前置技能：GS_CHAINACTION Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/rapidshower.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/gunslinger/rapidshower.cpp:9
void SkillRapidShower::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/gunslinger/rapidshower.cpp:10
base_skillratio += 400 + 50 * skill_lv;
```

### Desperado (`GS_DESPERADO`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Multi_Hit；段数：1；属性：Weapon；范围：3；技能后摇：1000 ms；移动后摇：1000 ms；持续时间1：1000 ms；伤害标记：Splash；消耗/限制：SP Lv1=32; Lv2=34; Lv3=36; Lv4=38; Lv5=40; Lv6=42; Lv7=44; Lv8=46; Lv9=48; Lv10=50；弹药数 10；武器 Revolver；弹药 Bullet。

- 技能树最高等级：`10`
- 前置技能：GS_RAPIDSHOWER Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/gunslinger/desperado.cpp`, `src/map/skills/gunslinger/firedance.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5106
skill_blockmerc_start(mc, ud->skill_id, skill_get_cooldown(ud->skill_id, ud->skill_lv));
// src/map/skill.cpp:5112
clif_status_change(src, EFST_POSTDELAY, 1, skill_delayfix(src, ud->skill_id, ud->skill_lv), 0, 0, 0);
// src/map/skill.cpp:5119
sd->canequip_tick = tick + skill_get_time(ud->skill_id, ud->skill_lv);
// src/map/skill.cpp:6252
unit_val1 = (skill_get_time(skill_id, skill_lv) / interval); //Default: 950/300 = 3 hits
// src/map/skill.cpp:6255
unit_val1 = 200 + 200*skill_lv;
// src/map/skill.cpp:6276
case NPC_REVERBERATION:
// src/map/skill.cpp:6864
case WZ_STORMGUST: //SG counter does not reset per stormgust. IE: One hit from a SG and two hits from another will freeze you.
// src/map/skill.cpp:6866
tsc->sg_counter++; //SG hit counter.
// src/map/skill.cpp:6867
if (skill_attack(skill_get_type(sg->skill_id),ss,unit,bl,sg->skill_id,sg->skill_lv,tick,0) <= 0 && tsc)
// src/map/skill.cpp:6873
skill_attack(BF_WEAPON,ss,unit,bl,sg->skill_id,sg->skill_lv,tick,0);
// src/map/skill.cpp:6878
skill_attack(skill_get_type(sg->skill_id),ss,unit,bl,sg->skill_id,sg->skill_lv,tick,0);
// src/map/skill.cpp:6881
int32 heal = (int32)skill_attack(skill_get_type(sg->skill_id),ss,unit,bl,sg->skill_id,sg->skill_lv,tick,0);
```

### Gatling Fever (`GS_GATLINGFEVER`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；属性：Weapon；持续时间1：Lv1=30000; Lv2=45000; Lv3=60000; Lv4=75000; Lv5=90000; Lv6=105000; Lv7=120000; Lv8=135000; Lv9=150000; Lv10=165000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=30; Lv2=32; Lv3=34; Lv4=36; Lv5=38; Lv6=40; Lv7=42; Lv8=44; Lv9=46; Lv10=48；武器 Gatling；关联状态：GatlingFever。

- 技能树最高等级：`10`
- 前置技能：GS_RAPIDSHOWER Lv7, GS_DESPERADO Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/gatlingfever.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/gunslinger/gatlingfever.cpp:12
void SkillGatlingfever::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/gunslinger/gatlingfever.cpp:13
status_change *tsc = status_get_sc(target);
// src/map/skills/gunslinger/gatlingfever.cpp:15
status_change_entry *tsce = (tsc) ? tsc->getSCE(type) : nullptr;
// src/map/skills/gunslinger/gatlingfever.cpp:18
clif_skill_nodamage(src, *target, getSkillId(), skill_lv, status_change_end(target, type));
```

### Dust (`GS_DUST`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：2；命中类型：Single；段数：1；属性：Weapon；击退：5；吟唱：1000 ms；技能后摇：1000 ms；消耗/限制：SP Lv1=3; Lv2=6; Lv3=9; Lv4=12; Lv5=15; Lv6=18; Lv7=21; Lv8=24; Lv9=27; Lv10=30；弹药数 1；武器 Shotgun；弹药 Bullet。

- 技能树最高等级：`10`
- 前置技能：GS_SINGLEACTION Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/dust.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/gunslinger/dust.cpp:9
void SkillDust::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/gunslinger/dust.cpp:10
base_skillratio += 50 * skill_lv;
```

### Full Buster (`GS_FULLBUSTER`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-9；命中类型：Single；段数：1；属性：Weapon；技能后摇：Lv1=1200; Lv2=1400; Lv3=1600; Lv4=1800; Lv5=2000; Lv6=2200; Lv7=2400; Lv8=2600; Lv9=2800; Lv10=3000 ms；持续时间2：10000 ms；消耗/限制：SP Lv1=20; Lv2=25; Lv3=30; Lv4=35; Lv5=40; Lv6=45; Lv7=50; Lv8=55; Lv9=60; Lv10=65；弹药数 Lv1-2=2; Lv3-4=4; Lv5-6=6; Lv7-8=8; Lv9-10=10；武器 Shotgun；弹药 Bullet。

- 技能树最高等级：`10`
- 前置技能：GS_DUST Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/fullbuster.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/gunslinger/fullbuster.cpp:11
void SkillFullBuster::applyCounterAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& attack_type) const {
// src/map/skills/gunslinger/fullbuster.cpp:12
sc_start(src, src, SC_BLIND, 2 * skill_lv, skill_lv, skill_get_time2(getSkillId(), skill_lv));
// src/map/skills/gunslinger/fullbuster.cpp:15
void SkillFullBuster::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/gunslinger/fullbuster.cpp:16
base_skillratio += 100 * (skill_lv + 2);
```

### Spread Attack (`GS_SPREADATTACK`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-9；命中类型：Single；段数：1；属性：Weapon；范围：Lv1-3=1; Lv4-6=2; Lv7-9=3; Lv10=4；伤害标记：Splash；消耗/限制：SP Lv1=15; Lv2=20; Lv3=25; Lv4=30; Lv5=35; Lv6=40; Lv7=45; Lv8=50; Lv9=55; Lv10=60；弹药数 5；武器 Shotgun；弹药 Bullet。

- 技能树最高等级：`10`
- 前置技能：GS_FULLBUSTER Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/gunslinger/skill_factory_gunslinger.cpp`, `src/map/skills/gunslinger/spreadattack.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/gunslinger/spreadattack.cpp:6
SkillSpreadAttack::SkillSpreadAttack() : SkillImplRecursiveDamageSplash(GS_SPREADATTACK) {
// src/map/skills/gunslinger/spreadattack.cpp:9
void SkillSpreadAttack::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/gunslinger/spreadattack.cpp:11
base_skillratio += 30 * skill_lv;
// src/map/skills/gunslinger/spreadattack.cpp:13
base_skillratio += 20 * (skill_lv - 1);
```

### Ground Drift (`GS_GROUNDDRIFT`)

武器/物理技能；目标：地面区域；最高等级 10；射程：-9；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：3；吟唱：2000 ms；持续时间1：Lv1=3000; Lv2=6000; Lv3=9000; Lv4=12000; Lv5=15000; Lv6=18000; Lv7=21000; Lv8=24000; Lv9=27000; Lv10=30000 ms；持续时间2：Lv1=5000; Lv2=30000; Lv3=60000; Lv4=12000 ms；伤害标记：Splash, IgnoreAtkCard, IgnoreFlee；消耗/限制：SP Lv1=4; Lv2=8; Lv3=12; Lv4=16; Lv5=20; Lv6=24; Lv7=28; Lv8=32; Lv9=36; Lv10=40；弹药数 1；武器 Grenade；弹药 Grenade。

- 技能树最高等级：`10`
- 前置技能：GS_SPREADATTACK Lv7
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/gunslinger/grounddrift.cpp`, `src/map/skills/gunslinger/skill_factory_gunslinger.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
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
// src/map/skill.cpp:5998
val2 = (skill_lv+1)/2 + 4;
// src/map/skill.cpp:6007
int32 ele = skill_get_ele(skill_id, skill_lv);
// src/map/skill.cpp:6164
group = skill_initunitgroup(src, layout->count, skill_id, skill_lv, (flag & 1 ? skill->unit_id2 : skill->unit_id) + subunt, limit, interval);
// src/map/skills/gunslinger/grounddrift.cpp:13
void SkillGroundDrift::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
// src/map/skills/gunslinger/grounddrift.cpp:20
void SkillGroundDrift::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/gunslinger/grounddrift.cpp:22
base_skillratio += 100 + 20 * skill_lv;
```
