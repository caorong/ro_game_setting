# Monk 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

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
| 259 | `MO_IRONHAND` | Iron Fists | 10 | Monk | 是 | AL_DEMONBANE Lv10, AL_DP Lv10 | Weapon / Passive |
| 260 | `MO_SPIRITSRECOVERY` | Spiritual Cadence | 5 | Monk | 是 | MO_BLADESTOP Lv2 | Weapon / Passive |
| 261 | `MO_CALLSPIRITS` | Summon Spirit Sphere | 5 | Monk | 是 | MO_IRONHAND Lv2 | None / Self |
| 262 | `MO_ABSORBSPIRITS` | Absorb Spirit Sphere | 1 | Monk | 是 | MO_CALLSPIRITS Lv5 | Weapon / Support |
| 263 | `MO_TRIPLEATTACK` | Raging Trifecta Blow | 10 | Monk | 是 | MO_DODGE Lv5 | Weapon / Passive |
| 264 | `MO_BODYRELOCATION` | Snap | 1 | Monk | 是 | MO_EXTREMITYFIST Lv3, MO_SPIRITSRECOVERY Lv2, MO_STEELBODY Lv3 | None / Ground |
| 265 | `MO_DODGE` | Dodge | 10 | Monk | 是 | MO_IRONHAND Lv5, MO_CALLSPIRITS Lv5 | Weapon / Passive |
| 266 | `MO_INVESTIGATE` | Occult Impaction | 5 | Monk | 是 | MO_CALLSPIRITS Lv5 | Weapon / Attack |
| 267 | `MO_FINGEROFFENSIVE` | Throw Spirit Sphere | 5 | Monk | 是 | MO_INVESTIGATE Lv3 | Weapon / Attack |
| 268 | `MO_STEELBODY` | Mental Strength | 5 | Monk | 是 | MO_COMBOFINISH Lv3 | Weapon / Self |
| 269 | `MO_BLADESTOP` | Root | 5 | Monk | 是 | MO_DODGE Lv5 | Weapon / Self |
| 270 | `MO_EXPLOSIONSPIRITS` | Fury | 5 | Monk | 是 | MO_ABSORBSPIRITS Lv1 | Weapon / Self |
| 271 | `MO_EXTREMITYFIST` | Asura Strike | 5 | Monk | 是 | MO_EXPLOSIONSPIRITS Lv3, MO_FINGEROFFENSIVE Lv3 | Weapon / Attack |
| 272 | `MO_CHAINCOMBO` | Raging Quadruple Blow | 5 | Monk | 是 | MO_TRIPLEATTACK Lv5 | Weapon / Self |
| 273 | `MO_COMBOFINISH` | Raging Thrust | 5 | Monk | 是 | MO_CHAINCOMBO Lv3 | Weapon / Self |
| 1015 | `MO_KITRANSLATION` | Ki Translation | 1 | Monk | 是 | — | Weapon / Support |
| 1016 | `MO_BALKYOUNG` | Ki Explosion | 1 | Monk | 是 | — | Weapon / Attack |

## 技能详情

### Iron Fists (`MO_IRONHAND`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：AL_DEMONBANE Lv10, AL_DP Lv10
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2369
damage += (skill * 3);
// src/map/battle.cpp:2371
damage += (skill * 4);
// src/map/battle.cpp:2375
damage += (skill * 10);
// src/map/battle.cpp:2379
damage += (skill * 3);
// src/map/battle.cpp:2383
damage += (skill * 3);
// src/map/battle.cpp:2387
damage += (skill * 3);
```

### Spiritual Cadence (`MO_SPIRITSRECOVERY`)

武器/物理技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：MO_BLADESTOP Lv2
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:5322
sregen->sp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5333
sregen->hp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5343
sregen->sp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5349
val = regen->hp*(100+5*skill)/100;
// src/map/status.cpp:5350
regen->hp = cap_value(val, 1, SHRT_MAX);
// src/map/status.cpp:5353
val = regen->sp*(100+3*skill)/100;
```

### Summon Spirit Sphere (`MO_CALLSPIRITS`)

非伤害技能；目标：自身；最高等级 5；命中类型：Single；段数：1；吟唱：1000 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 8。

- 技能树最高等级：`5`
- 前置技能：MO_IRONHAND Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/powervelocity.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/acolyte/summonspiritsphere.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:8416
skill_lv += sc->getSCE(SC_RAISINGDRAGON)->val1;
// src/map/skill.cpp:8417
if(sd.spiritball >= skill_lv) {
// src/map/skills/acolyte/powervelocity.cpp:12
void SkillPowerVelocity::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/powervelocity.cpp:13
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/powervelocity.cpp:14
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/acolyte/powervelocity.cpp:21
pc_addspiritball(dstsd, skill_get_time(MO_CALLSPIRITS, pc_checkskill(sd, MO_CALLSPIRITS)), i);
// src/map/skills/acolyte/powervelocity.cpp:25
clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
// src/map/skills/acolyte/summonspiritsphere.cpp:13
void SkillSummoningSpiritSphere::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/summonspiritsphere.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/summonspiritsphere.cpp:17
int32 limit = skill_lv;
// src/map/skills/acolyte/summonspiritsphere.cpp:20
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/acolyte/summonspiritsphere.cpp:21
pc_addspiritball(sd,skill_get_time(getSkillId(),skill_lv),limit);
```

### Absorb Spirit Sphere (`MO_ABSORBSPIRITS`)

武器/物理技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；吟唱：2000 ms；伤害标记：NoDamage；消耗/限制：SP 5。

- 技能树最高等级：`1`
- 前置技能：MO_CALLSPIRITS Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/absorbspiritsphere.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/absorbspiritsphere.cpp:14
void SkillAbsorbSpiritSphere::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/absorbspiritsphere.cpp:15
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/absorbspiritsphere.cpp:16
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/acolyte/absorbspiritsphere.cpp:17
mob_data* dstmd = BL_CAST(BL_MOB, target);
// src/map/skills/acolyte/skill_factory_acolyte.cpp:260
case IQ_THIRD_CONSECRATION:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:261
return std::make_unique<SkillThirdConsecration>();
```

### Raging Trifecta Blow (`MO_TRIPLEATTACK`)

武器/物理技能；目标：被动；最高等级 10；射程：-1；命中类型：Multi_Hit；段数：-3；属性：Weapon。

- 技能树最高等级：`10`
- 前置技能：MO_DODGE Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/mob.cpp`, `src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/ragingtrifectablow.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4990
if (wd->damage > 0) {
// src/map/battle.cpp:4991
wd->damage = battle_attr_fix(src, target, wd->damage, right_element, tstatus->def_ele, tstatus->ele_lv);
// src/map/battle.cpp:4992
wd->damage = battle_calc_gvg_damage(src, target, wd->damage, skill_id, wd->flag);
// src/map/battle.cpp:4993
} else if (wd->damage2 > 0) {
// src/map/battle.cpp:4994
wd->damage2 = battle_attr_fix(src, target, wd->damage2, left_element, tstatus->def_ele, tstatus->ele_lv);
// src/map/battle.cpp:4995
wd->damage2 = battle_calc_gvg_damage(src, target, wd->damage2, skill_id, wd->flag);
// src/map/battle.cpp:5004
&& tstatus->def == 100
// src/map/battle.cpp:5013
if(wd->damage > 1 && wd->damage2 > 0) {
// src/map/battle.cpp:5014
wd->damage = 1;
// src/map/battle.cpp:7255
duration = 2000; // Only lasts 2 seconds for Boss monsters
// src/map/battle.cpp:7257
status_change_end(target, SC_BLADESTOP_WAIT);
// src/map/battle.cpp:7258
if(sc_start4(src,src, SC_BLADESTOP, 100, sd?pc_checkskill(sd, MO_BLADESTOP):5, 0, 0, target->id, duration))
```

### Snap (`MO_BODYRELOCATION`)

非伤害技能；目标：地面区域；最高等级 1；射程：18；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 14；气弹 1。

- 技能树最高等级：`1`
- 前置技能：MO_EXTREMITYFIST Lv3, MO_SPIRITSRECOVERY Lv2, MO_STEELBODY Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/acolyte/snap.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5420
sd = BL_CAST(BL_PC, src);
// src/map/skill.cpp:5440
clif_skill_nodamage(src,*src,skill_id,skill_lv);
// src/map/skill.cpp:9988
req.sp -= req.sp*5*kaina_lv/100;
// src/map/skill.cpp:9990
req.sp -= req.sp*3*kaina_lv/100;
// src/map/skill.cpp:9998
req.sp = 2; //Monk Spirit makes monk/champion combo skills cost 2 SP regardless of original cost
// src/map/skills/acolyte/snap.cpp:15
void SkillSnap::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/snap.cpp:16
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/snap.cpp:22
clif_skill_poseffect( *src, getSkillId(), skill_lv, src->x, src->y, tick );
```

### Dodge (`MO_DODGE`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：MO_IRONHAND Lv5, MO_CALLSPIRITS Lv5
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:4507
base_status->hit += skill * 3;
// src/map/status.cpp:4509
base_status->hit += skill * 3;
// src/map/status.cpp:4518
base_status->flee += skill*(sd->class_&JOBL_2 && (sd->class_&MAPID_FIRSTMASK) == MAPID_THIEF? 4 : 3);
// src/map/status.cpp:4520
base_status->flee += (skill*3) / 2;
// src/map/status.cpp:4522
base_status->flee += 20;
// src/map/status.cpp:4524
base_status->flee += skill * 10;
// src/map/status.cpp:4530
base_status->cri += skill * 10;
```

### Occult Impaction (`MO_INVESTIGATE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：2；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；伤害标记：IgnoreFlee；消耗/限制：SP Lv1=10; Lv2=14; Lv3=17; Lv4=19; Lv5=20；气弹 1。

- 技能树最高等级：`5`
- 前置技能：MO_CALLSPIRITS Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/acolyte/occultimpaction.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3165
static int32 is_attack_piercing(struct Damage* wd, block_list* src, const block_list* target, int32 skill_id, int32 skill_lv, int16 weapon_position)
// src/map/battle.cpp:3171
const map_session_data* sd = BL_CAST(BL_PC,src);
// src/map/battle.cpp:3176
&& !is_attack_critical(wd, src, target, skill_id, skill_lv, false)
// src/map/battle.cpp:3600
static int32 battle_get_spiritball_damage(struct Damage& wd, block_list& src, uint16 skill_id) {
// src/map/battle.cpp:3602
map_session_data* sd = BL_CAST(BL_PC, &src);
// src/map/battle.cpp:3608
int32 damage = 0;
// src/map/battle.cpp:3616
damage = (wd.div_ + sd->spiritball) * 3;
// src/map/battle.cpp:3621
damage = (sd->spiritball_old + sd->spiritball) * 3;
// src/map/battle.cpp:3676
wd->damage2 = battle_attr_fix(src, target, wd->damage2, left_element, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3698
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/skills/acolyte/occultimpaction.cpp:11
void SkillOccultImpaction::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/occultimpaction.cpp:12
WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, flag);
```

### Throw Spirit Sphere (`MO_FINGEROFFENSIVE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；属性：Weapon；吟唱：1000 ms；技能后摇：500 ms；移动后摇：Lv2=200; Lv3=400; Lv4=600; Lv5=800 ms；消耗/限制：SP 10；气弹 Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5。

- 技能树最高等级：`5`
- 前置技能：MO_INVESTIGATE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/acolyte/throwspiritsphere.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3602
map_session_data* sd = BL_CAST(BL_PC, &src);
// src/map/battle.cpp:3608
int32 damage = 0;
// src/map/battle.cpp:3616
damage = (wd.div_ + sd->spiritball) * 3;
// src/map/battle.cpp:3621
damage = (sd->spiritball_old + sd->spiritball) * 3;
// src/map/battle.cpp:3626
damage = sd->spiritball_old * 3;
// src/map/battle.cpp:3630
damage = sd->spiritball * 3;
// src/map/battle.cpp:4990
if (wd->damage > 0) {
// src/map/battle.cpp:4991
wd->damage = battle_attr_fix(src, target, wd->damage, right_element, tstatus->def_ele, tstatus->ele_lv);
// src/map/battle.cpp:4992
wd->damage = battle_calc_gvg_damage(src, target, wd->damage, skill_id, wd->flag);
// src/map/battle.cpp:4993
} else if (wd->damage2 > 0) {
// src/map/battle.cpp:4994
wd->damage2 = battle_attr_fix(src, target, wd->damage2, left_element, tstatus->def_ele, tstatus->ele_lv);
// src/map/battle.cpp:4995
wd->damage2 = battle_calc_gvg_damage(src, target, wd->damage2, skill_id, wd->flag);
```

### Mental Strength (`MO_STEELBODY`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；吟唱：5000 ms；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000 ms；伤害标记：NoDamage；消耗/限制：SP 200；气弹 5；关联状态：SteelBody。

- 技能树最高等级：`5`
- 前置技能：MO_COMBOFINISH Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:9785
status_percent_heal(sd, 100, 100);
// src/map/pc.cpp:9788
sc_start(sd,sd,SC_STEELBODY,100,5,skill_get_time(MO_STEELBODY,5));
// src/map/pc.cpp:9799
status_change_end(devsd, SC_DEVOTION);
```

### Root (`MO_BLADESTOP`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：Lv1=500; Lv2=700; Lv3=900; Lv4=1100; Lv5=1300 ms；持续时间2：Lv1=20000; Lv2=30000; Lv3=40000; Lv4=50000; Lv5=60000 ms；伤害标记：NoDamage；消耗/限制：SP 10；气弹 1；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；关联状态：BladeStop_Wait。

- 技能树最高等级：`5`
- 前置技能：MO_DODGE Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:7250
uint16 skill_lv = tsc->getSCE(SC_BLADESTOP_WAIT)->val1;
// src/map/battle.cpp:7251
int32 duration = skill_get_time2(MO_BLADESTOP,skill_lv);
// src/map/battle.cpp:7255
duration = 2000; // Only lasts 2 seconds for Boss monsters
// src/map/battle.cpp:7257
status_change_end(target, SC_BLADESTOP_WAIT);
// src/map/battle.cpp:7258
if(sc_start4(src,src, SC_BLADESTOP, 100, sd?pc_checkskill(sd, MO_BLADESTOP):5, 0, 0, target->id, duration))
// src/map/battle.cpp:7260
clif_damage(*src, *target, tick, sstatus->amotion, 1, 0, 1, DMG_NORMAL, 0, false); //Display MISS.
// src/map/battle.cpp:7262
sc_start4(src,target, SC_BLADESTOP, 100, skill_lv, 0, 0, src->id, duration);
// src/map/battle.cpp:7269
int32 triple_rate = 30; //Base Rate
// src/map/skills/acolyte/skill_factory_acolyte.cpp:260
case IQ_THIRD_CONSECRATION:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:261
return std::make_unique<SkillThirdConsecration>();
```

### Fury (`MO_EXPLOSIONSPIRITS`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 15；气弹 5；关联状态：ExplosionSpirits。

- 技能树最高等级：`5`
- 前置技能：MO_ABSORBSPIRITS Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/skill_factory_acolyte.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Asura Strike (`MO_EXTREMITYFIST`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：-2；命中类型：Single；段数：1；吟唱：Lv1=4000; Lv2=3500; Lv3=3000; Lv4=2500; Lv5=2000 ms；技能后摇：Lv1=3000; Lv2=2500; Lv3=2000; Lv4=1500; Lv5=1000 ms；持续时间1：300000 ms；伤害标记：IgnoreDefense, IgnoreFlee；消耗/限制：SP 1；气弹 5；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；前置状态 Explosionspirits；关联状态：ExtremityFist。

- 技能树最高等级：`5`
- 前置技能：MO_EXPLOSIONSPIRITS Lv3, MO_FINGEROFFENSIVE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/asurastrike.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/acolyte/snap.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3616
damage = (wd.div_ + sd->spiritball) * 3;
// src/map/battle.cpp:3621
damage = (sd->spiritball_old + sd->spiritball) * 3;
// src/map/battle.cpp:3626
damage = sd->spiritball_old * 3;
// src/map/battle.cpp:3630
damage = sd->spiritball * 3;
// src/map/battle.cpp:3634
return damage;
// src/map/battle.cpp:3676
wd->damage2 = battle_attr_fix(src, target, wd->damage2, left_element, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3698
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3700
wd->damage2 = battle_attr_fix(src, target, wd->damage2, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:4483
static int64 battle_calc_skill_constant_addition(struct Damage* wd, block_list *src,block_list *target,uint16 skill_id,uint16 skill_lv)
// src/map/battle.cpp:4485
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/battle.cpp:4486
map_session_data *tsd = BL_CAST(BL_PC, target);
// src/map/battle.cpp:4489
int64 atk = 0;
```

### Raging Quadruple Blow (`MO_CHAINCOMBO`)

武器/物理技能；目标：自身；最高等级 5；射程：-2；命中类型：Multi_Hit；段数：-4；属性：Weapon；消耗/限制：SP Lv1=11; Lv2=12; Lv3=13; Lv4=14; Lv5=15；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma。

- 技能树最高等级：`5`
- 前置技能：MO_TRIPLEATTACK Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/ragingquadrupleblow.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2429
status_change_end(src, SC_COMBO);
// src/map/skill.cpp:2438
duration = 1;
// src/map/skill.cpp:2444
duration = 1;
// src/map/skill.cpp:2450
party_skill_check(sd, sd->status.party_id, skill_id, skill_lv);
// src/map/skill.cpp:2452
duration = 1;
// src/map/skill.cpp:9986
req.sp -= req.sp*7*kaina_lv/100;
// src/map/skill.cpp:9988
req.sp -= req.sp*5*kaina_lv/100;
// src/map/skill.cpp:9990
req.sp -= req.sp*3*kaina_lv/100;
// src/map/skill.cpp:9998
req.sp = 2; //Monk Spirit makes monk/champion combo skills cost 2 SP regardless of original cost
// src/map/skill.cpp:10398
int32 delaynodex = skill_get_delaynodex(skill_id);
// src/map/skill.cpp:10399
double time = skill_get_delay(skill_id, skill_lv);
// src/map/skill.cpp:10404
status_change* sc = status_get_sc(bl);
```

### Raging Thrust (`MO_COMBOFINISH`)

武器/物理技能；目标：自身；最高等级 5；射程：-2；命中类型：Single；段数：1；属性：Weapon；范围：2；伤害标记：Splash；消耗/限制：SP Lv1=11; Lv2=12; Lv3=13; Lv4=14; Lv5=15；气弹 1；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma。

- 技能树最高等级：`5`
- 前置技能：MO_CHAINCOMBO Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/ragingthrust.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2367
TBL_HOM *hd = BL_CAST(BL_HOM, bl);
// src/map/skill.cpp:2438
duration = 1;
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
// src/map/skill.cpp:9986
req.sp -= req.sp*7*kaina_lv/100;
// src/map/skill.cpp:9988
req.sp -= req.sp*5*kaina_lv/100;
// src/map/skill.cpp:9990
req.sp -= req.sp*3*kaina_lv/100;
// src/map/skill.cpp:9998
req.sp = 2; //Monk Spirit makes monk/champion combo skills cost 2 SP regardless of original cost
// src/map/skill.cpp:10398
int32 delaynodex = skill_get_delaynodex(skill_id);
```

### Ki Translation (`MO_KITRANSLATION`)

武器/物理技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；吟唱：2000 ms；技能后摇：1000 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 40；气弹 1。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/kitranslation.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:9610
case CG_TAROTCARD: // TarotCard will consume sp in skill_cast_nodamage_id [Inkfish]
// src/map/skill.cpp:9615
require.sp = 0;
// src/map/skill.cpp:9619
require.sp *= 5;
// src/map/skill.cpp:9626
if(sd->state.autocast)
// src/map/skill.cpp:9627
require.sp = 0;
// src/map/skill.cpp:9633
if(require.hp || require.sp || require.ap)
// src/map/skills/acolyte/kitranslation.cpp:12
void SkillKiTranslation::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/kitranslation.cpp:13
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/kitranslation.cpp:14
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/acolyte/kitranslation.cpp:19
require = skill_get_requirement(sd,getSkillId(),skill_lv);
```

### Ki Explosion (`MO_BALKYOUNG`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-1；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：5；技能后摇：2000 ms；持续时间2：5000 ms；伤害标记：Splash, IgnoreAtkCard；消耗/限制：HP 10；SP 20；关联状态：Stun。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/kiexplosion.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/kiexplosion.cpp:13
void SkillKiExplosion::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
// src/map/skills/acolyte/kiexplosion.cpp:17
void SkillKiExplosion::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/kiexplosion.cpp:20
skill_blown(src,target,skill_get_blewcount(getSkillId(),skill_lv),-1,BLOWN_NONE);
// src/map/skills/acolyte/kiexplosion.cpp:21
skill_additional_effect(src,target,getSkillId(),skill_lv,BF_MISC,ATK_DEF,tick); //Use Misc rather than weapon to signal passive pushback
// src/map/skills/acolyte/skill_factory_acolyte.cpp:260
case IQ_THIRD_CONSECRATION:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:261
return std::make_unique<SkillThirdConsecration>();
```
