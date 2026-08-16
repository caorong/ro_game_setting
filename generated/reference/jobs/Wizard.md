# Wizard 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 9 | `MG_SRECOVERY` | Increase SP Recovery | 10 | Mage | 否 | — | None / Passive |
| 10 | `MG_SIGHT` | Sight | 1 | Mage | 否 | — | Magic / Self |
| 11 | `MG_NAPALMBEAT` | Napalm Beat | 10 | Mage | 否 | — | Magic / Attack |
| 12 | `MG_SAFETYWALL` | Safety Wall | 10 | Mage | 否 | MG_NAPALMBEAT Lv7, MG_SOULSTRIKE Lv5 | Magic / Ground |
| 13 | `MG_SOULSTRIKE` | Soul Strike | 10 | Mage | 否 | MG_NAPALMBEAT Lv4 | Magic / Attack |
| 14 | `MG_COLDBOLT` | Cold Bolt | 10 | Mage | 否 | — | Magic / Attack |
| 15 | `MG_FROSTDIVER` | Frost Diver | 10 | Mage | 否 | MG_COLDBOLT Lv5 | Magic / Attack |
| 16 | `MG_STONECURSE` | Stone Curse | 10 | Mage | 否 | — | Magic / Attack |
| 17 | `MG_FIREBALL` | Fire Ball | 10 | Mage | 否 | MG_FIREBOLT Lv4 | Magic / Attack |
| 18 | `MG_FIREWALL` | Fire Wall | 10 | Mage | 否 | MG_FIREBALL Lv5, MG_SIGHT Lv1 | Magic / Ground |
| 19 | `MG_FIREBOLT` | Fire Bolt | 10 | Mage | 否 | — | Magic / Attack |
| 20 | `MG_LIGHTNINGBOLT` | Lightning Bolt | 10 | Mage | 否 | — | Magic / Attack |
| 21 | `MG_THUNDERSTORM` | Thunderstorm | 10 | Mage | 否 | MG_LIGHTNINGBOLT Lv4 | Magic / Ground |
| 157 | `MG_ENERGYCOAT` | Energy Coat | 1 | Mage | 否 | — | Magic / Self |
| 80 | `WZ_FIREPILLAR` | Fire Pillar | 10 | Wizard | 是 | MG_FIREWALL Lv1 | Magic / Ground |
| 81 | `WZ_SIGHTRASHER` | Sightrasher | 10 | Wizard | 是 | MG_LIGHTNINGBOLT Lv1, MG_SIGHT Lv1 | Magic / Self |
| 83 | `WZ_METEOR` | Meteor Storm | 10 | Wizard | 是 | WZ_SIGHTRASHER Lv2, MG_THUNDERSTORM Lv1 | Magic / Ground |
| 84 | `WZ_JUPITEL` | Jupitel Thunder | 10 | Wizard | 是 | MG_NAPALMBEAT Lv1, MG_LIGHTNINGBOLT Lv1 | Magic / Attack |
| 85 | `WZ_VERMILION` | Lord of Vermilion | 10 | Wizard | 是 | MG_THUNDERSTORM Lv1, WZ_JUPITEL Lv5 | Magic / Ground |
| 86 | `WZ_WATERBALL` | Water Ball | 5 | Wizard | 是 | MG_COLDBOLT Lv1, MG_LIGHTNINGBOLT Lv1 | Magic / Attack |
| 87 | `WZ_ICEWALL` | Ice Wall | 10 | Wizard | 是 | MG_STONECURSE Lv1, MG_FROSTDIVER Lv1 | Magic / Ground |
| 88 | `WZ_FROSTNOVA` | Frost Nova | 10 | Wizard | 是 | WZ_ICEWALL Lv1 | Magic / Self |
| 89 | `WZ_STORMGUST` | Storm Gust | 10 | Wizard | 是 | MG_FROSTDIVER Lv1, WZ_JUPITEL Lv3 | Magic / Ground |
| 90 | `WZ_EARTHSPIKE` | Earth Spike | 5 | Wizard | 是 | MG_STONECURSE Lv1 | Magic / Attack |
| 91 | `WZ_HEAVENDRIVE` | Heaven's Drive | 5 | Wizard | 是 | WZ_EARTHSPIKE Lv3 | Magic / Ground |
| 92 | `WZ_QUAGMIRE` | Quagmire | 5 | Wizard | 是 | WZ_HEAVENDRIVE Lv1 | Magic / Ground |
| 93 | `WZ_ESTIMATION` | Sense | 1 | Wizard | 是 | — | Magic / Attack |
| 1006 | `WZ_SIGHTBLASTER` | Sight Blaster | 1 | Wizard | 是 | — | Magic / Self |

## 技能详情

### Fire Pillar (`WZ_FIREPILLAR`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=3; Lv2=4; Lv3=5; Lv4=6; Lv5=7; Lv6=8; Lv7=9; Lv8=10; Lv9=11; Lv10=12；属性：Fire；范围：Lv1-5=1; Lv6-11=2；吟唱：Lv1=3000; Lv2=2700; Lv3=2400; Lv4=2100; Lv5=1800; Lv6=1500; Lv7=1200; Lv8=900; Lv9=600; Lv10=300 ms；技能后摇：1000 ms；持续时间1：30000 ms；持续时间2：Lv1=600; Lv2=800; Lv3=1000; Lv4=1200; Lv5=1400; Lv6=1600; Lv7=1800; Lv8=2000; Lv9=2200; Lv10=2400 ms；伤害标记：IgnoreDefense；消耗/限制：SP 75；道具 Blue_Gemstone×1@Lv6, Blue_Gemstone×1@Lv7, Blue_Gemstone×1@Lv8, Blue_Gemstone×1@Lv9, Blue_Gemstone×1@Lv10。

- 技能树最高等级：`10`
- 前置技能：MG_FIREWALL Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/mage/firepillar.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5991
skillratio += 25;
// src/map/battle.cpp:5994
has_skillratio = true;
// src/map/battle.cpp:5996
MATK_RATE(skillratio);
// src/map/battle.cpp:6000
MATK_ADD(100 + 50 * skill_lv);
// src/map/battle.cpp:6006
ad.damage += battle_calc_cardfix(BF_MAGIC, src, target, nk, s_ele, 0, ad.damage, 0, ad.flag);
// src/map/battle.cpp:6011
ad.damage += ad.damage * i / 100;
// src/map/skill.cpp:5823
val1=skill_lv+3;
// src/map/skill.cpp:5838
val1=skill_lv+2;
// src/map/skill.cpp:5841
case AM_DEMONSTRATION:
// src/map/skills/mage/firepillar.cpp:12
void SkillFirePillar::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/firepillar.cpp:16
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/firepillar.cpp:19
void SkillFirePillar::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
```

### Sightrasher (`WZ_SIGHTRASHER`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；属性：Fire；范围：7；击退：5；吟唱：500 ms；技能后摇：2000 ms；持续时间1：500 ms；伤害标记：Splash；消耗/限制：SP Lv1=35; Lv2=37; Lv3=39; Lv4=41; Lv5=43; Lv6=45; Lv7=47; Lv8=49; Lv9=51; Lv10=53；前置状态 Sight。

- 技能树最高等级：`10`
- 前置技能：MG_LIGHTNINGBOLT Lv1, MG_SIGHT Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/sightrasher.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/sightrasher.cpp:12
void SkillSightRasher::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/sightrasher.cpp:14
status_change_end(src, SC_SIGHT);
// src/map/skills/mage/sightrasher.cpp:15
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/mage/sightrasher.cpp:17
skill_get_splash(getSkillId(), skill_lv),BL_CHAR|BL_SKILL,
// src/map/skills/mage/sightrasher.cpp:18
src,getSkillId(),skill_lv,tick, flag|BCT_ENEMY|SD_ANIMATION|1,
// src/map/skills/mage/sightrasher.cpp:19
skill_castend_damage_id);
```

### Meteor Storm (`WZ_METEOR`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1-2=1; Lv3-4=2; Lv5-6=3; Lv7-8=4; Lv9-10=5; Lv11=15；属性：Fire；范围：Lv1-10=3; Lv11=16；吟唱：15000 ms；技能后摇：Lv1=2000; Lv2-3=3000; Lv4-5=4000; Lv6-7=5000; Lv8-9=6000; Lv10=7000 ms；持续时间1：Lv1=2000; Lv2-3=3000; Lv4-5=4000; Lv6-7=5000; Lv8-9=6000; Lv10=7000; Lv11=10000 ms；持续时间2：5000 ms；消耗/限制：SP Lv1=20; Lv2=24; Lv3=30; Lv4=34; Lv5=40; Lv6=44; Lv7=50; Lv8=54; Lv9=60; Lv10=64；关联状态：Stun。

- 技能树最高等级：`10`
- 前置技能：WZ_SIGHTRASHER Lv2, MG_THUNDERSTORM Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/meteorstorm.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5420
sd = BL_CAST(BL_PC, src);
// src/map/skill.cpp:5817
val1 = src->id; // Store caster id.
// src/map/skill.cpp:5823
val1=skill_lv+3;
// src/map/skill.cpp:12414
if (unit->val1 <= 0 || unit->val2 <= 0) // Remove the unit only if no HP or hit limit is reached
// src/map/skill.cpp:12434
clif_skill_poseffect( *src, group->skill_id, group->skill_lv, bl->x, bl->y, tick );
// src/map/skills/mage/meteorstorm.cpp:13
void SkillMeteorStorm::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/meteorstorm.cpp:14
int32 area = skill_get_splash(getSkillId(), skill_lv);
// src/map/skills/mage/meteorstorm.cpp:17
for (int32 i = 1; i <= skill_get_time(getSkillId(), skill_lv) / skill_get_unit_interval(getSkillId()); i++) {
// src/map/skills/mage/meteorstorm.cpp:21
skill_unitsetting(src, getSkillId(), skill_lv, tmpx, tmpy, flag + i * skill_get_unit_interval(getSkillId()));
```

### Jupitel Thunder (`WZ_JUPITEL`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=3; Lv2=4; Lv3=5; Lv4=6; Lv5=7; Lv6=8; Lv7=9; Lv8=10; Lv9=11; Lv10=12；属性：Wind；击退：Lv1=2; Lv2-3=3; Lv4-5=4; Lv6-7=5; Lv8-9=6; Lv10=7；吟唱：Lv1=2500; Lv2=3000; Lv3=3500; Lv4=4000; Lv5=4500; Lv6=5000; Lv7=5500; Lv8=6000; Lv9=6500; Lv10=7000 ms；消耗/限制：SP Lv1=20; Lv2=23; Lv3=26; Lv4=29; Lv5=32; Lv6=35; Lv7=38; Lv8=41; Lv9=44; Lv10=47。

- 技能树最高等级：`10`
- 前置技能：MG_NAPALMBEAT Lv1, MG_LIGHTNINGBOLT Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/jupitelthunder.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:3767
layout = skill_get_unit_layout(skl->skill_id, skl->skill_lv, src, skl->x, skl->y);
// src/map/skill.cpp:3782
skill_attack(BF_MAGIC, src, src, target, skl->skill_id, skl->skill_lv, tick, skl->flag);
// src/map/skill.cpp:3787
unit_set_walkdelay(src, tick, TIMERSKILL_INTERVAL, 1);
// src/map/skill.cpp:3788
skill_addtimerskill(src,tick+TIMERSKILL_INTERVAL,target->id,skl->x,skl->y,skl->skill_id,skl->skill_lv,skl->type+1,skl->flag);
// src/map/skills/mage/jupitelthunder.cpp:9
void SkillJupitelThunder::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/jupitelthunder.cpp:11
skill_addtimerskill(src, tick + TIMERSKILL_INTERVAL, target->id, 0, 0, getSkillId(), skill_lv, 1, flag);
```

### Lord of Vermilion (`WZ_VERMILION`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：-10；属性：Wind；吟唱：Lv1=15000; Lv2=14500; Lv3=14000; Lv4=13500; Lv5=13000; Lv6=12500; Lv7=12000; Lv8=11500; Lv9=11000; Lv10=10500 ms；技能后摇：5000 ms；持续时间1：4000 ms；持续时间2：30000 ms；消耗/限制：SP Lv1=60; Lv2=64; Lv3=68; Lv4=72; Lv5=76; Lv6=80; Lv7=84; Lv8=88; Lv9=92; Lv10=96；关联状态：Blind。

- 技能树最高等级：`10`
- 前置技能：MG_THUNDERSTORM Lv1, WZ_JUPITEL Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/mage/lordofvermilion.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/lordofvermilion.cpp:14
void SkillLordOfVermilion::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/lordofvermilion.cpp:18
skill_unitsetting(src, getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/lordofvermilion.cpp:21
void SkillLordOfVermilion::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/mage/lordofvermilion.cpp:23
const map_session_data* sd = BL_CAST(BL_PC, src);
```

### Water Ball (`WZ_WATERBALL`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：1；属性：Water；吟唱：Lv1=1000; Lv2=2000; Lv3=3000; Lv4=4000; Lv5=5000; Lv6=6000; Lv7=7000; Lv8=8000; Lv9=9000; Lv10=10000 ms；持续时间1：10000 ms；消耗/限制：SP Lv1=15; Lv2-3=20; Lv4-10=25；状态 Water。

- 技能树最高等级：`5`
- 前置技能：MG_COLDBOLT Lv1, MG_LIGHTNINGBOLT Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/skills/mage/waterball.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:1160
int32 pos = skill_get_unit_layout_type(skill_id,skill_lv);
// src/map/skill.cpp:1164
ShowError("skill_get_unit_layout: unsupported layout type %d for skill %d (level %d)\n", pos, skill_id, skill_lv);
// src/map/skill.cpp:1171
if (src->type == BL_MOB && skill_lv >= 10) {
// src/map/skill.cpp:1762
sp += sd->bonus.sp_gain_value;
// src/map/skill.cpp:1763
sp += sd->indexed_bonus.sp_gain_race[status_get_race(bl)] + sd->indexed_bonus.sp_gain_race[RC_ALL];
// src/map/skill.cpp:1764
hp += sd->bonus.hp_gain_value;
// src/map/skill.cpp:1767
sp += sd->bonus.long_sp_gain_value;
// src/map/skill.cpp:1768
hp += sd->bonus.long_hp_gain_value;
// src/map/skill.cpp:1771
sp += sd->bonus.magic_sp_gain_value;
// src/map/skill.cpp:1772
hp += sd->bonus.magic_hp_gain_value;
// src/map/skill.cpp:1774
status_change *sc = nullptr;
// src/map/skill.cpp:1783
if( hp || sp ) { // updated to force healing to allow healing through berserk
```

### Ice Wall (`WZ_ICEWALL`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Water；伤害标记：NoDamage；消耗/限制：SP 20。

- 技能树最高等级：`10`
- 前置技能：MG_STONECURSE Lv1, MG_FROSTDIVER Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/mage/icewall.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:1171
if (src->type == BL_MOB && skill_lv >= 10) {
// src/map/skill.cpp:1192
ShowError("skill_get_unit_layout: unknown unit layout for skill %d (level %d)\n", skill_id, skill_lv);
// src/map/skill.cpp:3471
static int32 skill_check_unit_range2 (block_list *bl, int32 x, int32 y, uint16 skill_id, uint16 skill_lv, bool isNearNPC)
// src/map/skill.cpp:3477
range = skill_get_splash(skill_id,skill_lv);
// src/map/skill.cpp:3489
int32 layout_type = skill_get_unit_layout_type(skill_id,skill_lv);
// src/map/skill.cpp:5420
sd = BL_CAST(BL_PC, src);
// src/map/skill.cpp:5440
clif_skill_nodamage(src,*src,skill_id,skill_lv);
// src/map/skill.cpp:6252
unit_val1 = (skill_get_time(skill_id, skill_lv) / interval); //Default: 950/300 = 3 hits
// src/map/skill.cpp:6255
unit_val1 = 200 + 200*skill_lv;
// src/map/skill.cpp:11739
skill_unitsetmapcell(unit,WZ_ICEWALL,group->skill_lv,CELL_ICEWALL,true);
// src/map/skill.cpp:11742
skill_unitsetmapcell(unit,SA_LANDPROTECTOR,group->skill_lv,CELL_LANDPROTECTOR,true);
// src/map/skill.cpp:11746
skill_unitsetmapcell(unit,HP_BASILICA,group->skill_lv,CELL_BASILICA,true);
```

### Frost Nova (`WZ_FROSTNOVA`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；属性：Water；范围：2；吟唱：Lv1-2=6000; Lv3-4=5500; Lv5-6=5000; Lv7-8=4500; Lv9-10=4000 ms；技能后摇：1000 ms；持续时间2：Lv1=1500; Lv2=3000; Lv3=4500; Lv4=6000; Lv5=7500; Lv6=9000; Lv7=10500; Lv8=12000; Lv9=13500; Lv10=15000 ms；伤害标记：Splash；消耗/限制：SP Lv1=45; Lv2=43; Lv3=41; Lv4=39; Lv5=37; Lv6=35; Lv7=33; Lv8=31; Lv9=29; Lv10=27；关联状态：Freeze。

- 技能树最高等级：`10`
- 前置技能：WZ_ICEWALL Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/frostnova.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:10959
map_foreachinallrange(skill_area_sub, bl, skill_get_splash(SS_FUUMAKOUCHIKU,skill_lv), BL_CHAR,
// src/map/skill.cpp:10960
src, SS_FUUMAKOUCHIKU, skill_lv, tick, flag | BCT_ENEMY | SD_SPLASH | SKILL_ALTDMG_FLAG | 1, skill_castend_damage_id);
// src/map/skill.cpp:10973
return 0; //Does not hit current cell
// src/map/skill.cpp:10983
return (int32)skill_attack(atk_type,src,dsrc,bl,skill_id,skill_lv,tick,flag);
// src/map/skills/mage/frostnova.cpp:15
void SkillFrostNova::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/frostnova.cpp:16
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/mage/frostnova.cpp:19
skill_get_splash(getSkillId(), skill_lv), splash_target(src),
// src/map/skills/mage/frostnova.cpp:20
BF_MAGIC, src, src, getSkillId(), skill_lv, tick, flag, BCT_ENEMY);
// src/map/skills/mage/frostnova.cpp:23
void SkillFrostNova::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
```

### Storm Gust (`WZ_STORMGUST`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Water；击退：2；吟唱：Lv1=6000; Lv2=7000; Lv3=8000; Lv4=9000; Lv5=10000; Lv6=11000; Lv7=12000; Lv8=13000; Lv9=14000; Lv10=15000 ms；技能后摇：5000 ms；持续时间1：4600 ms；持续时间2：12000 ms；消耗/限制：SP 78；关联状态：Freeze。

- 技能树最高等级：`10`
- 前置技能：MG_FROSTDIVER Lv1, WZ_JUPITEL Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/skills/mage/stormgust.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2635
if(!battle_config.stormgust_knockback)
// src/map/skill.cpp:2639
if (battle_config.cart_revo_knockback)
// src/map/skill.cpp:2644
if (!battle_config.arrow_shower_knockback && skill_id == AC_SHOWER)
// src/map/skill.cpp:6857
skill_attack(BF_WEAPON, ss, unit, bl, sg->skill_id, sg->skill_lv, tick + (t_tick)count * sg->interval, 0);
// src/map/skill.cpp:6864
case WZ_STORMGUST: //SG counter does not reset per stormgust. IE: One hit from a SG and two hits from another will freeze you.
// src/map/skill.cpp:6866
tsc->sg_counter++; //SG hit counter.
// src/map/skill.cpp:6867
if (skill_attack(skill_get_type(sg->skill_id),ss,unit,bl,sg->skill_id,sg->skill_lv,tick,0) <= 0 && tsc)
// src/map/skill.cpp:6873
skill_attack(BF_WEAPON,ss,unit,bl,sg->skill_id,sg->skill_lv,tick,0);
// src/map/skills/mage/stormgust.cpp:13
void SkillStormGust::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/stormgust.cpp:17
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/stormgust.cpp:20
void SkillStormGust::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/mage/stormgust.cpp:22
base_skillratio -= 30; // Offset only once
```

### Earth Spike (`WZ_EARTHSPIKE`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；属性：Earth；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20。

- 技能树最高等级：`5`
- 前置技能：MG_STONECURSE Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/homunculus/homunculus_caprice.cpp`, `src/map/skills/mage/earthspike.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6217
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6222
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6227
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6232
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6238
ad.damage = battle_attr_fix(src, target, ad.damage, s_ele, tstatus->def_ele, tstatus->ele_lv);
// src/map/battle.cpp:6241
ad.damage += battle_calc_cardfix(BF_MAGIC, src, target, nk, s_ele, 0, ad.damage, 0, ad.flag);
// src/map/battle.cpp:7747
battle_autocast_elembuff_skill(sd, target, MG_FIREBOLT, tick, flag);
// src/map/battle.cpp:7749
battle_autocast_elembuff_skill(sd, target, MG_COLDBOLT, tick, flag);
// src/map/battle.cpp:7751
battle_autocast_elembuff_skill(sd, target, MG_LIGHTNINGBOLT, tick, flag);
// src/map/battle.cpp:7753
battle_autocast_elembuff_skill(sd, target, WZ_EARTHSPIKE, tick, flag);
// src/map/battle.cpp:7755
battle_autocast_elembuff_skill(sd, target, SO_POISON_BUSTER, tick, flag);
// src/map/battle.cpp:7757
if (wd.flag & BF_WEAPON && src != target && damage > 0) {
```

### Heaven's Drive (`WZ_HEAVENDRIVE`)

魔法技能；目标：地面区域；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；属性：Earth；吟唱：Lv1=1000; Lv2=2000; Lv3=3000; Lv4=4000; Lv5=5000 ms；技能后摇：1000 ms；持续时间1：100 ms；消耗/限制：SP Lv1=28; Lv2=32; Lv3=36; Lv4=40; Lv5=44。

- 技能树最高等级：`5`
- 前置技能：WZ_EARTHSPIKE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/mage/heavensdrive.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6222
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6227
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6232
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6238
ad.damage = battle_attr_fix(src, target, ad.damage, s_ele, tstatus->def_ele, tstatus->ele_lv);
// src/map/battle.cpp:6241
ad.damage += battle_calc_cardfix(BF_MAGIC, src, target, nk, s_ele, 0, ad.damage, 0, ad.flag);
// src/map/skills/mage/heavensdrive.cpp:13
void SkillHeavensDrive::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/heavensdrive.cpp:17
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/heavensdrive.cpp:20
void SkillHeavensDrive::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/mage/heavensdrive.cpp:22
base_skillratio += 25;
```

### Quagmire (`WZ_QUAGMIRE`)

魔法技能；目标：地面区域；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Earth；技能后摇：1000 ms；持续时间1：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000 ms；持续时间2：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=5; Lv2=10; Lv3=15; Lv4=20; Lv5=25；关联状态：Quagmire。

- 技能树最高等级：`5`
- 前置技能：WZ_HEAVENDRIVE Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/quagmire.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5838
val1=skill_lv+2;
// src/map/skill.cpp:5841
case AM_DEMONSTRATION:
// src/map/skill.cpp:7684
struct status_change_entry *sce;
// src/map/skill.cpp:7700
status_change_end(bl, type);
// src/map/skills/mage/quagmire.cpp:9
void SkillQuagmire::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/quagmire.cpp:13
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Sense (`WZ_ESTIMATION`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 10。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/sense.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/sense.cpp:13
void SkillSense::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/sense.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/mage/sense.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/mage/sense.cpp:16
mob_data* dstmd = BL_CAST(BL_MOB, target);
```

### Sight Blaster (`WZ_SIGHTBLASTER`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；段数：1；属性：Fire；范围：1；击退：3；吟唱：2000 ms；持续时间1：120000 ms；消耗/限制：SP 40；关联状态：SightBlaster。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/sightblaster.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:3075
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, (flag&SD_LEVEL) ? -1 : skill_lv, DMG_SPLASH );
// src/map/skill.cpp:3076
if( dsrc != src ) // avoid damage display redundancy
// src/map/skill.cpp:3080
clif_skill_damage( *dsrc, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, -1, dmg_type );
// src/map/skill.cpp:3084
clif_skill_damage( *src, *bl, tick, dmg.amotion, dmg.dmotion, damage, dmg.div_, skill_id, (flag&SD_LEVEL) ? -1 : skill_lv, DMG_SPLASH );
// src/map/skill.cpp:3088
clif_skill_damage( *dsrc, *bl, tick, status_get_amotion(src), dmg.dmotion, damage, dmg.div_, skill_id, -1, DMG_SPLASH );
// src/map/skills/mage/sightblaster.cpp:14
void SkillSightBlaster::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/sightblaster.cpp:15
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
// src/map/skills/mage/sightblaster.cpp:16
sc_start2(src,target,skill_get_sc(getSkillId()),100,skill_lv,getSkillId(),skill_get_time(getSkillId(),skill_lv)));
// src/map/skills/mage/sightblaster.cpp:19
void SkillSightBlaster::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/sightblaster.cpp:20
skill_attack(BF_MAGIC,src,src,target,getSkillId(),skill_lv,tick,flag);
// src/map/skills/mage/sightblaster.cpp:23
void SkillSightBlaster::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/status.cpp:15284
status_change_end(bl, SC__SHADOWFORM);
```
