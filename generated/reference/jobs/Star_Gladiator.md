# Star_Gladiator 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 411 | `TK_RUN` | Running | 10 | Taekwon | 否 | — | Misc / Self |
| 412 | `TK_READYSTORM` | Tornado Stance | 1 | Taekwon | 否 | TK_STORMKICK Lv1 | Weapon / Self |
| 413 | `TK_STORMKICK` | Tornado Kick | 7 | Taekwon | 否 | — | Weapon / Self |
| 414 | `TK_READYDOWN` | Heel Drop Stance | 1 | Taekwon | 否 | TK_DOWNKICK Lv1 | Weapon / Self |
| 415 | `TK_DOWNKICK` | Heel Drop | 7 | Taekwon | 否 | — | Weapon / Self |
| 416 | `TK_READYTURN` | Roundhouse Stance | 1 | Taekwon | 否 | TK_TURNKICK Lv1 | Weapon / Self |
| 417 | `TK_TURNKICK` | Roundhouse Kick | 7 | Taekwon | 否 | — | Weapon / Self |
| 418 | `TK_READYCOUNTER` | Counter Kick Stance | 1 | Taekwon | 否 | TK_COUNTER Lv1 | Weapon / Self |
| 419 | `TK_COUNTER` | Counter Kick | 7 | Taekwon | 否 | — | Weapon / Self |
| 420 | `TK_DODGE` | Tumbling | 1 | Taekwon | 否 | TK_JUMPKICK Lv7 | Weapon / Self |
| 421 | `TK_JUMPKICK` | Flying Kick | 7 | Taekwon | 否 | — | Weapon / Attack |
| 422 | `TK_HPTIME` | Peaceful Break | 10 | Taekwon | 否 | — | None / Passive |
| 423 | `TK_SPTIME` | Happy Break | 10 | Taekwon | 否 | — | None / Passive |
| 424 | `TK_POWER` | Kihop | 5 | Taekwon | 否 | — | Weapon / Passive |
| 425 | `TK_SEVENWIND` | Mild Wind | 7 | Taekwon | 否 | TK_HPTIME Lv5, TK_SPTIME Lv5, TK_POWER Lv5 | Weapon / Self |
| 426 | `TK_HIGHJUMP` | Taekwon Jump | 5 | Taekwon | 否 | — | Weapon / Self |
| 493 | `TK_MISSION` | Taekwon Mission | 1 | Taekwon | 否 | TK_POWER Lv5 | None / Self |
| 427 | `SG_FEEL` | Feeling the Sun Moon and Stars | 3 | Star_Gladiator | 是 | — | Magic / Self |
| 428 | `SG_SUN_WARM` | Warmth of the Sun | 3 | Star_Gladiator | 是 | SG_FEEL Lv1 | Weapon / Self |
| 429 | `SG_MOON_WARM` | Warmth of the Moon | 3 | Star_Gladiator | 是 | SG_FEEL Lv2 | Weapon / Self |
| 430 | `SG_STAR_WARM` | Warmth of the Stars | 3 | Star_Gladiator | 是 | SG_FEEL Lv3 | Weapon / Self |
| 431 | `SG_SUN_COMFORT` | Comfort of the Sun | 4 | Star_Gladiator | 是 | SG_FEEL Lv1 | Magic / Self |
| 432 | `SG_MOON_COMFORT` | Comfort of the Moon | 4 | Star_Gladiator | 是 | SG_FEEL Lv2 | Magic / Self |
| 433 | `SG_STAR_COMFORT` | Comfort of the Stars | 4 | Star_Gladiator | 是 | SG_FEEL Lv3 | Magic / Self |
| 434 | `SG_HATE` | Hatred of the Sun Moon and Stars | 3 | Star_Gladiator | 是 | — | Magic / Attack |
| 435 | `SG_SUN_ANGER` | Anger of the Sun | 3 | Star_Gladiator | 是 | SG_HATE Lv1 | None / Passive |
| 436 | `SG_MOON_ANGER` | Anger of the Moon | 3 | Star_Gladiator | 是 | SG_HATE Lv2 | None / Passive |
| 437 | `SG_STAR_ANGER` | Anger of the Stars | 3 | Star_Gladiator | 是 | SG_HATE Lv3 | None / Passive |
| 438 | `SG_SUN_BLESS` | Blessing of the Sun | 5 | Star_Gladiator | 是 | SG_FEEL Lv1, SG_HATE Lv1 | None / Passive |
| 439 | `SG_MOON_BLESS` | Blessing of the Moon | 5 | Star_Gladiator | 是 | SG_FEEL Lv2, SG_HATE Lv2 | None / Passive |
| 440 | `SG_STAR_BLESS` | Blessing of the Stars | 5 | Star_Gladiator | 是 | SG_FEEL Lv3, SG_HATE Lv3 | None / Passive |
| 441 | `SG_DEVIL` | Demon of the Sun Moon and Stars | 10 | Star_Gladiator | 是 | — | None / Passive |
| 442 | `SG_FRIEND` | Friend of the Sun Moon and Stars | 3 | Star_Gladiator | 是 | — | None / Passive |
| 443 | `SG_KNOWLEDGE` | Knowledge of the Sun Moon and Stars | 10 | Star_Gladiator | 是 | — | None / Passive |
| 444 | `SG_FUSION` | Union of the Sun Moon and Stars | 1 | Star_Gladiator | 是 | SG_KNOWLEDGE Lv9 | Misc / Self |

## 技能详情

### Feeling the Sun Moon and Stars (`SG_FEEL`)

魔法技能；目标：自身；最高等级 3；命中类型：Single；段数：1；吟唱：1000 ms；伤害标记：NoDamage；消耗/限制：SP 100。

- 技能树最高等级：`3`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/taekwon/feelingthesunmoonandstars.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/taekwon/feelingthesunmoonandstars.cpp:12
void SkillFeelingtheSunMoonandStars::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/taekwon/feelingthesunmoonandstars.cpp:13
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/taekwon/feelingthesunmoonandstars.cpp:17
if(!sd->feel_map[skill_lv-1].index)
// src/map/skills/taekwon/feelingthesunmoonandstars.cpp:18
clif_feel_req(sd->fd,sd, skill_lv);
// src/map/skills/taekwon/feelingthesunmoonandstars.cpp:20
clif_feel_info(sd, skill_lv-1, 1);
```

### Warmth of the Sun (`SG_SUN_WARM`)

武器/物理技能；目标：自身；最高等级 3；射程：1；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：2；持续时间1：Lv1=10000; Lv2=20000; Lv3=60000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 20；关联状态：Warm。

- 技能树最高等级：`3`
- 前置技能：SG_FEEL Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`, `src/map/skills/taekwon/warmthofthesun.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5102
static void battle_calc_attack_gvg_bg(struct Damage* wd, block_list *src,block_list *target,uint16 skill_id,uint16 skill_lv)
// src/map/battle.cpp:5104
if( wd->damage + wd->damage2 ) { //There is a total damage value
// src/map/battle.cpp:5105
if( src != target && //Don't reflect your own damage (Grand Cross)
// src/map/battle.cpp:5108
int64 damage = wd->damage + wd->damage2, rdamage = 0;
// src/map/battle.cpp:5109
map_session_data *tsd = BL_CAST(BL_PC, target);
// src/map/battle.cpp:5113
rdamage = battle_calc_return_damage(target, src, &damage, wd->flag, skill_id, false);
// src/map/battle.cpp:5114
if( rdamage > 0 ) { //Item reflect gets calculated before any mapflag reducing is applicated
// src/map/battle.cpp:5117
clif_damage(*src, (d_bl == nullptr) ? *src : *d_bl, tick, wd->amotion, sstatus->dmotion, rdamage, 1, DMG_ENDURE, 0, false);
// src/map/battle.cpp:5119
battle_drain(tsd, src, rdamage, rdamage, sstatus->race, sstatus->class_);
// src/map/battle.cpp:5326
* Check if we should reflect the damage and calculate it if so
// src/map/battle.cpp:5328
* @param wd : weapon damage
// src/map/battle.cpp:5331
* @param skill_id : id of casted skill, 0 = basic atk
```

### Warmth of the Moon (`SG_MOON_WARM`)

武器/物理技能；目标：自身；最高等级 3；射程：1；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：2；持续时间1：Lv1=10000; Lv2=20000; Lv3=60000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 20；关联状态：Warm。

- 技能树最高等级：`3`
- 前置技能：SG_FEEL Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`, `src/map/skills/taekwon/warmthofthemoon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5102
static void battle_calc_attack_gvg_bg(struct Damage* wd, block_list *src,block_list *target,uint16 skill_id,uint16 skill_lv)
// src/map/battle.cpp:5104
if( wd->damage + wd->damage2 ) { //There is a total damage value
// src/map/battle.cpp:5105
if( src != target && //Don't reflect your own damage (Grand Cross)
// src/map/battle.cpp:5108
int64 damage = wd->damage + wd->damage2, rdamage = 0;
// src/map/battle.cpp:5109
map_session_data *tsd = BL_CAST(BL_PC, target);
// src/map/battle.cpp:5113
rdamage = battle_calc_return_damage(target, src, &damage, wd->flag, skill_id, false);
// src/map/battle.cpp:5114
if( rdamage > 0 ) { //Item reflect gets calculated before any mapflag reducing is applicated
// src/map/battle.cpp:5117
clif_damage(*src, (d_bl == nullptr) ? *src : *d_bl, tick, wd->amotion, sstatus->dmotion, rdamage, 1, DMG_ENDURE, 0, false);
// src/map/battle.cpp:5119
battle_drain(tsd, src, rdamage, rdamage, sstatus->race, sstatus->class_);
// src/map/battle.cpp:5326
* Check if we should reflect the damage and calculate it if so
// src/map/battle.cpp:5328
* @param wd : weapon damage
// src/map/battle.cpp:5331
* @param skill_id : id of casted skill, 0 = basic atk
```

### Warmth of the Stars (`SG_STAR_WARM`)

武器/物理技能；目标：自身；最高等级 3；射程：1；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：2；持续时间1：Lv1=10000; Lv2=20000; Lv3=60000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 10；关联状态：Warm。

- 技能树最高等级：`3`
- 前置技能：SG_FEEL Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`, `src/map/skills/taekwon/warmthofthestars.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5102
static void battle_calc_attack_gvg_bg(struct Damage* wd, block_list *src,block_list *target,uint16 skill_id,uint16 skill_lv)
// src/map/battle.cpp:5104
if( wd->damage + wd->damage2 ) { //There is a total damage value
// src/map/battle.cpp:5105
if( src != target && //Don't reflect your own damage (Grand Cross)
// src/map/battle.cpp:5108
int64 damage = wd->damage + wd->damage2, rdamage = 0;
// src/map/battle.cpp:5109
map_session_data *tsd = BL_CAST(BL_PC, target);
// src/map/battle.cpp:5113
rdamage = battle_calc_return_damage(target, src, &damage, wd->flag, skill_id, false);
// src/map/battle.cpp:5114
if( rdamage > 0 ) { //Item reflect gets calculated before any mapflag reducing is applicated
// src/map/battle.cpp:5117
clif_damage(*src, (d_bl == nullptr) ? *src : *d_bl, tick, wd->amotion, sstatus->dmotion, rdamage, 1, DMG_ENDURE, 0, false);
// src/map/battle.cpp:5119
battle_drain(tsd, src, rdamage, rdamage, sstatus->race, sstatus->class_);
// src/map/battle.cpp:5326
* Check if we should reflect the damage and calculate it if so
// src/map/battle.cpp:5328
* @param wd : weapon damage
// src/map/battle.cpp:5331
* @param skill_id : id of casted skill, 0 = basic atk
```

### Comfort of the Sun (`SG_SUN_COMFORT`)

魔法技能；目标：自身；最高等级 4；段数：1；技能后摇：1000 ms；持续时间1：Lv1=80000; Lv2=160000; Lv3=240000; Lv4=320000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=70; Lv2=60; Lv3=50; Lv4=40；关联状态：Sun_Comfort。

- 技能树最高等级：`4`
- 前置技能：SG_FEEL Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
// src/map/skill.cpp:8622
if (!party_skill_check(&sd, sd.status.party_id, skill_id, skill_lv)) {
// src/map/skill.cpp:8643
if( require.sp > 0 ) {
// src/map/skill.cpp:8644
if (status->sp < (uint32)require.sp)
```

### Comfort of the Moon (`SG_MOON_COMFORT`)

魔法技能；目标：自身；最高等级 4；段数：1；技能后摇：1000 ms；持续时间1：Lv1=80000; Lv2=160000; Lv3=240000; Lv4=320000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=70; Lv2=60; Lv3=50; Lv4=40；关联状态：Moon_Comfort。

- 技能树最高等级：`4`
- 前置技能：SG_FEEL Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
// src/map/skill.cpp:8622
if (!party_skill_check(&sd, sd.status.party_id, skill_id, skill_lv)) {
```

### Comfort of the Stars (`SG_STAR_COMFORT`)

魔法技能；目标：自身；最高等级 4；段数：1；技能后摇：1000 ms；持续时间1：Lv1=80000; Lv2=160000; Lv3=240000; Lv4=320000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=70; Lv2=60; Lv3=50; Lv4=40；关联状态：Star_Comfort。

- 技能树最高等级：`4`
- 前置技能：SG_FEEL Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
// src/map/skill.cpp:8622
if (!party_skill_check(&sd, sd.status.party_id, skill_id, skill_lv)) {
```

### Hatred of the Sun Moon and Stars (`SG_HATE`)

魔法技能；目标：敌方目标；最高等级 3；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；伤害标记：NoDamage；消耗/限制：SP 100。

- 技能树最高等级：`3`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/taekwon/hatredofthesunmoonandstars.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/taekwon/hatredofthesunmoonandstars.cpp:12
void SkillHatredoftheSunMoonandStars::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/taekwon/hatredofthesunmoonandstars.cpp:13
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/taekwon/hatredofthesunmoonandstars.cpp:16
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/taekwon/hatredofthesunmoonandstars.cpp:17
if (!pc_set_hate_mob(sd, skill_lv-1, target))
```

### Anger of the Sun (`SG_SUN_ANGER`)

非伤害技能；目标：被动；最高等级 3。

- 技能树最高等级：`3`
- 前置技能：SG_HATE Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
```

### Anger of the Moon (`SG_MOON_ANGER`)

非伤害技能；目标：被动；最高等级 3。

- 技能树最高等级：`3`
- 前置技能：SG_HATE Lv2
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
```

### Anger of the Stars (`SG_STAR_ANGER`)

非伤害技能；目标：被动；最高等级 3。

- 技能树最高等级：`3`
- 前置技能：SG_HATE Lv3
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/pc.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4684
RE_ALLATK_ADDRATE(wd, 20);
// src/map/battle.cpp:4693
int32 skillratio = sd->status.base_level + sstatus->dex + sstatus->luk;
// src/map/battle.cpp:4696
skillratio += sstatus->str; // SG_STAR_ANGER additionally has STR added in its formula.
// src/map/battle.cpp:4698
skillratio /= 12 - 3 * anger_level;
// src/map/battle.cpp:4702
skillratio = min( skillratio, 25 * anger_level );
// src/map/battle.cpp:4705
ATK_ADDRATE(wd->damage, wd->damage2, skillratio);
// src/map/battle.cpp:4707
RE_ALLATK_ADDRATE(wd, skillratio);
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
```

### Blessing of the Sun (`SG_SUN_BLESS`)

非伤害技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：SG_FEEL Lv1, SG_HATE Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
```

### Blessing of the Moon (`SG_MOON_BLESS`)

非伤害技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：SG_FEEL Lv2, SG_HATE Lv2
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
```

### Blessing of the Stars (`SG_STAR_BLESS`)

非伤害技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：SG_FEEL Lv3, SG_HATE Lv3
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
```

### Demon of the Sun Moon and Stars (`SG_DEVIL`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:8349
clif_status_change(sd, EFST_DEVIL1, 1, 0, 0, 0, 1); //Permanent blind effect from SG_DEVIL.
// src/map/pc.cpp:9174
clif_status_change(sd, EFST_DEVIL1, 1, 0, 0, 0, 1); //Permanent blind effect from SG_DEVIL.
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
```

### Friend of the Sun Moon and Stars (`SG_FRIEND`)

非伤害技能；目标：被动；最高等级 3；持续时间1：10000 ms；关联状态：SkillRate_Up。

- 技能树最高等级：`3`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:1235
sc_start4(src, src, SC_COMBO, 15, TK_DOWNKICK,
// src/map/skill.cpp:1240
sc_start4(src, src, SC_COMBO, 15, TK_TURNKICK,
// src/map/skill.cpp:1244
else if (sc->getSCE(SC_READYCOUNTER)) { //additional chance from SG_FRIEND [Komurka]
// src/map/skill.cpp:1245
int32 rate = 20;
// src/map/skill.cpp:1246
if (sc->getSCE(SC_SKILLRATE_UP) && sc->getSCE(SC_SKILLRATE_UP)->val1 == TK_COUNTER) {
// src/map/skill.cpp:1247
rate += rate*sc->getSCE(SC_SKILLRATE_UP)->val2 / 100;
// src/map/skill.cpp:1248
status_change_end(src, SC_SKILLRATE_UP);
// src/map/skill.cpp:1250
sc_start4(src, src, SC_COMBO, rate, TK_COUNTER,
// src/map/skill.cpp:2438
duration = 1;
// src/map/skill.cpp:2444
duration = 1;
// src/map/skill.cpp:2450
party_skill_check(sd, sd->status.party_id, skill_id, skill_lv);
// src/map/skill.cpp:2452
duration = 1;
```

### Knowledge of the Sun Moon and Stars (`SG_KNOWLEDGE`)

非伤害技能；目标：被动；最高等级 10；持续时间1：600000 ms；关联状态：Knowledge。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`metadata-only` / `metadata-only`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Union of the Sun Moon and Stars (`SG_FUSION`)

特殊技能；目标：自身；最高等级 1；命中类型：Single；段数：1；技能后摇：1000 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 100；关联状态：Fusion。

- 技能树最高等级：`1`
- 前置技能：SG_KNOWLEDGE Lv9
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:8643
if( require.sp > 0 ) {
// src/map/skill.cpp:8644
if (status->sp < (uint32)require.sp)
// src/map/skill.cpp:8647
status_zap(&sd, 0, require.sp);
```
