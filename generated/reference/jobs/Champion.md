# Champion 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Champion` 公式页](../skill-formulas/Champion.md)

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 22 | `AL_DP` | Divine Protection | 10 | Acolyte | 否 | — | Weapon / Passive |
| 23 | `AL_DEMONBANE` | Demon Bane | 10 | Acolyte | 否 | AL_DP Lv3 | Weapon / Passive |
| 24 | `AL_RUWACH` | Ruwach | 1 | Acolyte | 否 | — | Magic / Self |
| 25 | `AL_PNEUMA` | Pneuma | 1 | Acolyte | 否 | AL_WARP Lv4 | Magic / Ground |
| 26 | `AL_TELEPORT` | Teleport | 2 | Acolyte | 否 | AL_RUWACH Lv1 | Magic / Self |
| 27 | `AL_WARP` | Warp Portal | 4 | Acolyte | 否 | AL_TELEPORT Lv2 | Magic / Ground |
| 28 | `AL_HEAL` | Heal | 10 | Acolyte | 否 | — | Magic / Support |
| 29 | `AL_INCAGI` | Increase AGI | 10 | Acolyte | 否 | AL_HEAL Lv3 | Magic / Support |
| 30 | `AL_DECAGI` | Decrease AGI | 10 | Acolyte | 否 | AL_INCAGI Lv1 | Magic / Attack |
| 31 | `AL_HOLYWATER` | Aqua Benedicta | 1 | Acolyte | 否 | — | Magic / Self |
| 32 | `AL_CRUCIS` | Signum Crucis | 10 | Acolyte | 否 | AL_DEMONBANE Lv3 | Magic / Self |
| 33 | `AL_ANGELUS` | Angelus | 10 | Acolyte | 否 | AL_DP Lv3 | Magic / Self |
| 34 | `AL_BLESSING` | Blessing | 10 | Acolyte | 否 | AL_DP Lv5 | Magic / Support |
| 35 | `AL_CURE` | Cure | 1 | Acolyte | 否 | AL_HEAL Lv2 | Magic / Support |
| 156 | `AL_HOLYLIGHT` | Holy Light | 1 | Acolyte | 否 | — | Magic / Attack |
| 259 | `MO_IRONHAND` | Iron Fists | 10 | Monk | 否 | AL_DEMONBANE Lv10, AL_DP Lv10 | Weapon / Passive |
| 260 | `MO_SPIRITSRECOVERY` | Spiritual Cadence | 5 | Monk | 否 | MO_BLADESTOP Lv2 | Weapon / Passive |
| 261 | `MO_CALLSPIRITS` | Summon Spirit Sphere | 5 | Monk | 否 | MO_IRONHAND Lv2 | None / Self |
| 262 | `MO_ABSORBSPIRITS` | Absorb Spirit Sphere | 1 | Monk | 否 | MO_CALLSPIRITS Lv5 | Weapon / Support |
| 263 | `MO_TRIPLEATTACK` | Raging Trifecta Blow | 10 | Monk | 否 | MO_DODGE Lv5 | Weapon / Passive |
| 264 | `MO_BODYRELOCATION` | Snap | 1 | Monk | 否 | MO_EXTREMITYFIST Lv3, MO_SPIRITSRECOVERY Lv2, MO_STEELBODY Lv3 | None / Ground |
| 265 | `MO_DODGE` | Dodge | 10 | Monk | 否 | MO_IRONHAND Lv5, MO_CALLSPIRITS Lv5 | Weapon / Passive |
| 266 | `MO_INVESTIGATE` | Occult Impaction | 5 | Monk | 否 | MO_CALLSPIRITS Lv5 | Weapon / Attack |
| 267 | `MO_FINGEROFFENSIVE` | Throw Spirit Sphere | 5 | Monk | 否 | MO_INVESTIGATE Lv3 | Weapon / Attack |
| 268 | `MO_STEELBODY` | Mental Strength | 5 | Monk | 否 | MO_COMBOFINISH Lv3 | Weapon / Self |
| 269 | `MO_BLADESTOP` | Root | 5 | Monk | 否 | MO_DODGE Lv5 | Weapon / Self |
| 270 | `MO_EXPLOSIONSPIRITS` | Fury | 5 | Monk | 否 | MO_ABSORBSPIRITS Lv1 | Weapon / Self |
| 271 | `MO_EXTREMITYFIST` | Asura Strike | 5 | Monk | 否 | MO_EXPLOSIONSPIRITS Lv3, MO_FINGEROFFENSIVE Lv3 | Weapon / Attack |
| 272 | `MO_CHAINCOMBO` | Raging Quadruple Blow | 5 | Monk | 否 | MO_TRIPLEATTACK Lv5 | Weapon / Self |
| 273 | `MO_COMBOFINISH` | Raging Thrust | 5 | Monk | 否 | MO_CHAINCOMBO Lv3 | Weapon / Self |
| 1015 | `MO_KITRANSLATION` | Ki Translation | 1 | Monk | 否 | — | Weapon / Support |
| 1016 | `MO_BALKYOUNG` | Ki Explosion | 1 | Monk | 否 | — | Weapon / Attack |
| 370 | `CH_PALMSTRIKE` | Raging Palm Strike | 5 | Champion | 是 | MO_IRONHAND Lv7, MO_CALLSPIRITS Lv5 | Weapon / Attack |
| 371 | `CH_TIGERFIST` | Glacier Fist | 5 | Champion | 是 | MO_IRONHAND Lv5, MO_TRIPLEATTACK Lv5, MO_CALLSPIRITS Lv5, MO_COMBOFINISH Lv3 | Weapon / Self |
| 372 | `CH_CHAINCRUSH` | Chain Crush Combo | 10 | Champion | 是 | MO_IRONHAND Lv5, MO_CALLSPIRITS Lv5, CH_TIGERFIST Lv2 | Weapon / Self |
| 401 | `CH_SOULCOLLECT` | Zen | 1 | Champion | 是 | MO_CALLSPIRITS Lv5, MO_ABSORBSPIRITS Lv1, MO_EXPLOSIONSPIRITS Lv5 | None / Self |

## 技能详情

### Raging Palm Strike (`CH_PALMSTRIKE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：-2；命中类型：Single；段数：1；属性：Weapon；击退：3；技能后摇：300 ms；消耗/限制：SP Lv1=2; Lv2=4; Lv3=6; Lv4=8; Lv5=10；前置状态 Explosionspirits。

- 技能树最高等级：`5`
- 前置技能：MO_IRONHAND Lv7, MO_CALLSPIRITS Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/ragingpalmstrike.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2911
if( rnd()%100 > (1 + skill_lv) )
// src/map/skill.cpp:2915
if (damage < dmg.div_ && skill_id != CH_PALMSTRIKE)
// src/map/skill.cpp:2916
dmg.blewcount = 0; //only pushback when it hit for other
// src/map/skill.cpp:3874
skill_attack(BF_WEAPON, src, src, target, skl->skill_id, skl->skill_lv, tick, skl->flag|SD_LEVEL);
// src/map/skill.cpp:3878
status_change* tsc = status_get_sc(target);
// src/map/skill.cpp:3879
status_change* sc = status_get_sc(src);
// src/map/skill.cpp:3882
skill_blown(src,target,skill_get_blewcount(skl->skill_id, skl->skill_lv), -1, BLOWN_NONE);
// src/map/skill.cpp:3885
skill_attack(skl->type,src,src,target,skl->skill_id,skl->skill_lv,tick,skl->flag);
// src/map/skills/acolyte/ragingpalmstrike.cpp:14
void SkillRagingPalmStrike::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/ragingpalmstrike.cpp:17
clif_damage(*src, *target, tick, status_get_amotion(src), 0, -1, 1, DMG_ENDURE, 0, false); //Display an absorbed damage attack.
// src/map/skills/acolyte/ragingpalmstrike.cpp:18
skill_addtimerskill(src, tick + (1000 + status_get_amotion(src)), target->id, 0, 0, getSkillId(), skill_lv, BF_WEAPON, flag);
// src/map/skills/acolyte/ragingpalmstrike.cpp:21
void SkillRagingPalmStrike::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& skillratio, int32 mflag) const {
```

### Glacier Fist (`CH_TIGERFIST`)

武器/物理技能；目标：自身；最高等级 5；射程：-2；命中类型：Multi_Hit；段数：1；属性：Weapon；持续时间1：Lv1=2000; Lv2=4000; Lv3=6000; Lv4=8000; Lv5=10000 ms；消耗/限制：SP Lv1=4; Lv2=6; Lv3=8; Lv4=10; Lv5=12；气弹 1；关联状态：Ankle。

- 技能树最高等级：`5`
- 前置技能：MO_IRONHAND Lv5, MO_TRIPLEATTACK Lv5, MO_CALLSPIRITS Lv5, MO_COMBOFINISH Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/glacierfist.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2444
duration = 1;
// src/map/skill.cpp:2450
party_skill_check(sd, sd->status.party_id, skill_id, skill_lv);
// src/map/skill.cpp:2452
duration = 1;
// src/map/skill.cpp:2456
duration = 1;
// src/map/skill.cpp:2460
duration = 1;
// src/map/skill.cpp:2466
duration = 1;
// src/map/skill.cpp:2472
duration = 1;
// src/map/skill.cpp:2477
duration = 1;
// src/map/skill.cpp:2484
duration = 2000;
// src/map/skill.cpp:2485
nodelay = 1; //Neither gives walk nor attack delay
// src/map/skill.cpp:9986
req.sp -= req.sp*7*kaina_lv/100;
// src/map/skill.cpp:9988
req.sp -= req.sp*5*kaina_lv/100;
```

### Chain Crush Combo (`CH_CHAINCRUSH`)

武器/物理技能；目标：自身；最高等级 10；射程：-2；命中类型：Multi_Hit；段数：Lv1-2=-1; Lv3-4=-2; Lv5-6=-3; Lv7-8=-4; Lv9-10=-5；属性：Weapon；消耗/限制：SP Lv1=4; Lv2=6; Lv3=8; Lv4=10; Lv5=12; Lv6=14; Lv7=16; Lv8=18; Lv9=20; Lv10=22；气弹 2。

- 技能树最高等级：`10`
- 前置技能：MO_IRONHAND Lv5, MO_CALLSPIRITS Lv5, CH_TIGERFIST Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/chaincrushcombo.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2367
TBL_HOM *hd = BL_CAST(BL_HOM, bl);
// src/map/skill.cpp:2444
duration = 1;
// src/map/skill.cpp:2450
party_skill_check(sd, sd->status.party_id, skill_id, skill_lv);
// src/map/skill.cpp:2452
duration = 1;
// src/map/skill.cpp:2456
duration = 1;
// src/map/skill.cpp:2460
duration = 1;
// src/map/skill.cpp:2466
duration = 1;
// src/map/skill.cpp:2472
duration = 1;
// src/map/skill.cpp:2477
duration = 1;
// src/map/skill.cpp:9986
req.sp -= req.sp*7*kaina_lv/100;
// src/map/skill.cpp:9988
req.sp -= req.sp*5*kaina_lv/100;
// src/map/skill.cpp:9990
req.sp -= req.sp*3*kaina_lv/100;
```

### Zen (`CH_SOULCOLLECT`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 20。

- 技能树最高等级：`1`
- 前置技能：MO_CALLSPIRITS Lv5, MO_ABSORBSPIRITS Lv1, MO_EXPLOSIONSPIRITS Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/acolyte/zen.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/skill_factory_acolyte.cpp:220
case CD_REPARATIO:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:221
return std::make_unique<SkillReparatio>();
// src/map/skills/acolyte/zen.cpp:13
void SkillZen::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/zen.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/zen.cpp:20
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/acolyte/zen.cpp:22
pc_addspiritball(sd,skill_get_time(getSkillId(),skill_lv),limit);
```
