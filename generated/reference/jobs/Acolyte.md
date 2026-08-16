# Acolyte 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 22 | `AL_DP` | Divine Protection | 10 | Acolyte | 是 | — | Weapon / Passive |
| 23 | `AL_DEMONBANE` | Demon Bane | 10 | Acolyte | 是 | AL_DP Lv3 | Weapon / Passive |
| 24 | `AL_RUWACH` | Ruwach | 1 | Acolyte | 是 | — | Magic / Self |
| 25 | `AL_PNEUMA` | Pneuma | 1 | Acolyte | 是 | AL_WARP Lv4 | Magic / Ground |
| 26 | `AL_TELEPORT` | Teleport | 2 | Acolyte | 是 | AL_RUWACH Lv1 | Magic / Self |
| 27 | `AL_WARP` | Warp Portal | 4 | Acolyte | 是 | AL_TELEPORT Lv2 | Magic / Ground |
| 28 | `AL_HEAL` | Heal | 10 | Acolyte | 是 | — | Magic / Support |
| 29 | `AL_INCAGI` | Increase AGI | 10 | Acolyte | 是 | AL_HEAL Lv3 | Magic / Support |
| 30 | `AL_DECAGI` | Decrease AGI | 10 | Acolyte | 是 | AL_INCAGI Lv1 | Magic / Attack |
| 31 | `AL_HOLYWATER` | Aqua Benedicta | 1 | Acolyte | 是 | — | Magic / Self |
| 32 | `AL_CRUCIS` | Signum Crucis | 10 | Acolyte | 是 | AL_DEMONBANE Lv3 | Magic / Self |
| 33 | `AL_ANGELUS` | Angelus | 10 | Acolyte | 是 | AL_DP Lv3 | Magic / Self |
| 34 | `AL_BLESSING` | Blessing | 10 | Acolyte | 是 | AL_DP Lv5 | Magic / Support |
| 35 | `AL_CURE` | Cure | 1 | Acolyte | 是 | AL_HEAL Lv2 | Magic / Support |
| 156 | `AL_HOLYLIGHT` | Holy Light | 1 | Acolyte | 是 | — | Magic / Attack |

## 技能详情

### Divine Protection (`AL_DP`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Demon Bane (`AL_DEMONBANE`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：AL_DP Lv3
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2279
int64 damage;
// src/map/battle.cpp:2284
damage = 0;
// src/map/battle.cpp:2286
damage = dmg;
// src/map/battle.cpp:2294
damage += static_cast<decltype(damage)>(skill * (sd->status.base_level / 20.0 + 3.0));
// src/map/battle.cpp:2296
damage += (skill * 5);
// src/map/battle.cpp:2298
damage += (skill * 10);
// src/map/battle.cpp:2300
damage += (15 * pc_checkskill(sd, NC_MADOLICENCE)); // Attack bonus is granted even without the Madogear
// src/map/battle.cpp:2303
damage += (skill * 4);
```

### Ruwach (`AL_RUWACH`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；段数：1；属性：Holy；范围：2；持续时间1：10000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 10；关联状态：Ruwach。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/ruwach.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/ruwach.cpp:13
void SkillRuwach::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
// src/map/skills/acolyte/ruwach.cpp:17
clif_skill_nodamage(src, *bl, getSkillId(), skill_lv, sc_start2(src, bl, type, 100, skill_lv, getSkillId(), skill_get_time(getSkillId(), skill_lv)));
// src/map/skills/acolyte/ruwach.cpp:20
void SkillRuwach::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/acolyte/ruwach.cpp:21
base_skillratio += 45;
// src/map/skills/acolyte/skill_factory_acolyte.cpp:174
case AL_HEAL:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:175
return std::make_unique<SkillHeal>();
// src/map/status.cpp:15269
status_change_end(bl, SC__SHADOWFORM);
// src/map/status.cpp:15274
status_change_end(bl, SC_HIDING);
// src/map/status.cpp:15275
status_change_end(bl, SC_CLOAKING);
// src/map/status.cpp:15276
status_change_end(bl, SC_CAMOUFLAGE);
// src/map/status.cpp:15277
status_change_end(bl, SC_CLOAKINGEXCEED);
// src/map/status.cpp:15278
status_change_end(bl, SC_NEWMOON);
```

### Pneuma (`AL_PNEUMA`)

魔法技能；目标：地面区域；最高等级 1；射程：9；命中类型：Single；段数：1；持续时间1：10000 ms；伤害标记：NoDamage；消耗/限制：SP 10；关联状态：Pneuma。

- 技能树最高等级：`1`
- 前置技能：AL_WARP Lv4
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/pneuma.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/mage/elementalshield.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:7718
status_change_end(bl, SC_DANCING);
// src/map/skills/acolyte/pneuma.cpp:9
void SkillPneuma::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/pneuma.cpp:13
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/acolyte/skill_factory_acolyte.cpp:174
case AL_HEAL:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:175
return std::make_unique<SkillHeal>();
// src/map/skills/mage/elementalshield.cpp:14
void SkillElementalShield::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/elementalshield.cpp:15
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/mage/elementalshield.cpp:19
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/mage/elementalshield.cpp:23
skill_unitsetting(target, MG_SAFETYWALL, skill_lv + 5, target->x, target->y, 0);
// src/map/skills/mage/elementalshield.cpp:27
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/mage/elementalshield.cpp:30
party_foreachsamemap(skill_area_sub, sd, skill_get_splash(getSkillId(),skill_lv), src, getSkillId(), skill_lv, tick, flag|BCT_PARTY|1, skill_castend_nodamage_id);
```

### Teleport (`AL_TELEPORT`)

魔法技能；目标：自身；最高等级 2；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP Lv1=10; Lv2=9。

- 技能树最高等级：`2`
- 前置技能：AL_RUWACH Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/acolyte/teleport.cpp`, `src/map/skills/other/odinsrecall.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:812
* Check if the skill is ok to cast and when.
// src/map/skill.cpp:813
* Done before skill_check_condition_castbegin, requirement
// src/map/skill.cpp:814
* @param skill_id: Skill ID that casted
// src/map/skill.cpp:815
* @param sd: Player who casted
// src/map/skill.cpp:835
if (!sd.state.autocast && sd.skillitem != skill_id && sd.canskill_tick &&
// src/map/skill.cpp:892
return false; // gonna be checked in 'skill_castend_nodamage_id'
// src/map/skill.cpp:5497
ShowInfo("PC %d skill castend skill =%d map=%s\n",sd->id,skill_id,mapname);
// src/map/skill.cpp:14593
const status_change *sc = status_get_sc(bl);
// src/map/skills/acolyte/skill_factory_acolyte.cpp:174
case AL_HEAL:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:175
return std::make_unique<SkillHeal>();
// src/map/skills/acolyte/teleport.cpp:15
void SkillTeleport::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/teleport.cpp:16
map_session_data* sd = BL_CAST(BL_PC, src);
```

### Warp Portal (`AL_WARP`)

魔法技能；目标：地面区域；最高等级 4；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；持续时间1：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000; Lv6=30000; Lv7=35000; Lv8=40000; Lv9=45000; Lv10=50000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=35; Lv2=32; Lv3=29; Lv4=26；道具 Blue_Gemstone×1。

- 技能树最高等级：`4`
- 前置技能：AL_TELEPORT Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/acolyte/warpportal.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:857
(skill_nocast&4 && mapdata_flag_gvg2_no_te(mapdata)) ||
// src/map/skill.cpp:858
(skill_nocast&8 && mapdata->getMapFlag(MF_BATTLEGROUND)) ||
// src/map/skill.cpp:859
(skill_nocast&16 && mapdata_flag_gvg2_te(mapdata)) || // WOE:TE
// src/map/skill.cpp:860
(mapdata->zone && skill_nocast&(mapdata->zone) && mapdata->getMapFlag(MF_RESTRICTED)) ){
// src/map/skill.cpp:870
case RETURN_TO_ELDICASTES:
// src/map/skill.cpp:3456
if( skill_id == AM_DEMONSTRATION && bl->type == BL_MOB && ((TBL_MOB*)bl)->mob_id == MOBID_EMPERIUM )
// src/map/skill.cpp:3457
return 0; //Allow casting Bomb/Demonstration Right under emperium [Skotlex]
// src/map/skill.cpp:5299
!check_distance_blxy(src, ud->skillx, ud->skilly, skill_get_range2(src, ud->skill_id, ud->skill_lv, true) + battle_config.skill_add_range)) {
// src/map/skill.cpp:5301
skill_consume_requirement(sd, ud->skill_id, ud->skill_lv, 3);
// src/map/skill.cpp:5308
if( ud->skill_id != AL_WARP && !skill_check_condition_castend(*sd, ud->skill_id, ud->skill_lv) )
// src/map/skill.cpp:5311
skill_consume_requirement(sd, ud->skill_id, ud->skill_lv, 1);
// src/map/skill.cpp:5313
int32 add_ap = skill_get_giveap(ud->skill_id, ud->skill_lv);
```

### Heal (`AL_HEAL`)

魔法技能；目标：友方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Holy；技能后摇：1000 ms；伤害标记：NoDamage, IgnoreDefense；消耗/限制：SP Lv1=13; Lv2=16; Lv3=19; Lv4=22; Lv5=25; Lv6=28; Lv7=31; Lv8=34; Lv9=37; Lv10=40。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/mob.cpp`, `src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/coluceoheal.cpp`, `src/map/skills/acolyte/competentia.cpp`, `src/map/skills/acolyte/dilectioheal.cpp`, `src/map/skills/acolyte/heal.cpp`, `src/map/skills/acolyte/medialevotum.cpp`, `src/map/skills/acolyte/reparatio.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/homunculus/homunculus_benedictionofchaos.cpp`, `src/map/skills/mage/drainlife.cpp`, `src/map/skills/merchant/aidberserkpotion.cpp`, `src/map/skills/merchant/aidcondensedpotion.cpp`, `src/map/skills/merchant/aidpotion.cpp`, `src/map/skills/npc/energydrain.cpp`, `src/map/skills/npc/fullheal.cpp`, `src/map/skills/npc/npccoluceoheal.cpp`, `src/map/skills/npc/suckingblood.cpp`, `src/map/skills/npc/vampiregift.cpp`, `src/map/skills/other/netrepair.cpp`, `src/map/skills/summoner/kisulwaterspraying.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5881
ad.damage = 0;
// src/map/battle.cpp:5883
#define MATK_RATE(a) { ad.damage = ad.damage * (a) / 100; }
// src/map/battle.cpp:5885
#define MATK_ADDRATE(a) { ad.damage += ad.damage * (a) / 100; }
// src/map/battle.cpp:5887
#define MATK_ADD(a) { ad.damage += a; }
// src/map/battle.cpp:5891
case AL_HEAL:
// src/map/battle.cpp:5894
case AB_HIGHNESSHEAL:
// src/map/battle.cpp:5895
ad.damage = skill_calc_heal(src, target, skill_id, skill_lv, false);
// src/map/battle.cpp:5898
ad.damage = 40;
// src/map/mob.cpp:4715
ms->cond1 = MSC_MYHPLTMAXRATE;
// src/map/mob.cpp:4719
ms->delay += -5000 +(skill_get_time(skill_id, ms->skill_lv) + skill_get_time2(skill_id, ms->skill_lv))/2;
// src/map/mob.cpp:4720
if (ms->delay < 5000)
// src/map/mob.cpp:4721
ms->delay = 5000; //With a minimum of 5 secs.
```

### Increase AGI (`AL_INCAGI`)

魔法技能；目标：友方目标；最高等级 10；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：Lv1=60000; Lv2=80000; Lv3=100000; Lv4=120000; Lv5=140000; Lv6=160000; Lv7=180000; Lv8=200000; Lv9=220000; Lv10=240000 ms；伤害标记：NoDamage；消耗/限制：HP 15；SP Lv1=18; Lv2=21; Lv3=24; Lv4=27; Lv5=30; Lv6=33; Lv7=36; Lv8=39; Lv9=42; Lv10=45；关联状态：IncreaseAgi。

- 技能树最高等级：`10`
- 前置技能：AL_HEAL Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/cantocandidus.cpp`, `src/map/skills/acolyte/incagi.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2882
damage = dmg.damage + dmg.damage2;
// src/map/skill.cpp:2886
sce->val3 = (int32)damage;
// src/map/skill.cpp:2889
skill_castend_damage_id(bl, src, NPC_MAXPAIN_ATK, sce->val1, tick, flag);
// src/map/skill.cpp:2895
damage = 1;
// src/map/skill.cpp:2897
if( damage && tsc && tsc->getSCE(SC_GENSOU) && dmg.flag&BF_MAGIC ){
// src/map/skill.cpp:2901
damage = damage / 2; // Deflect half of the damage to a target nearby
// src/map/skill.cpp:2902
clif_skill_damage( *bl, *nbl, tick, status_get_amotion(src), 0, battle_fix_damage(bl,nbl,damage,0,0), dmg.div_, OB_OBOROGENSOU_TRANSITION_ATK, -1, DMG_SINGLE );
// src/map/skill.cpp:4637
static int8 skill_castend_id_check(block_list *src, block_list *target, uint16 skill_id, uint16 skill_lv) {
// src/map/skill.cpp:4640
status_change *tsc = status_get_sc(target);
// src/map/skill.cpp:4642
if (src != target && (status_bl_has_mode(target,MD_SKILLIMMUNE) || (status_get_class(target) == MOBID_EMPERIUM && !skill->inf2[INF2_TARGETEMPERIUM])) && skill_get_casttype(skill_id) == CAST_NODAMAGE)
// src/map/skill.cpp:4643
return USESKILL_FAIL_MAX; // Don't show a skill fail message (NoDamage type doesn't consume requirements)
// src/map/skill.cpp:4646
case AL_HEAL:
```

### Decrease AGI (`AL_DECAGI`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：Lv1=40000; Lv2=50000; Lv3=60000; Lv4=70000; Lv5=80000; Lv6=90000; Lv7=100000; Lv8=110000; Lv9=120000; Lv10-11=130000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=15; Lv2=17; Lv3=19; Lv4=21; Lv5=23; Lv6=25; Lv7=27; Lv8=29; Lv9=31; Lv10=33；关联状态：DecreaseAgi。

- 技能树最高等级：`10`
- 前置技能：AL_INCAGI Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/decagi.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:4637
static int8 skill_castend_id_check(block_list *src, block_list *target, uint16 skill_id, uint16 skill_lv) {
// src/map/skill.cpp:4640
status_change *tsc = status_get_sc(target);
// src/map/skill.cpp:4642
if (src != target && (status_bl_has_mode(target,MD_SKILLIMMUNE) || (status_get_class(target) == MOBID_EMPERIUM && !skill->inf2[INF2_TARGETEMPERIUM])) && skill_get_casttype(skill_id) == CAST_NODAMAGE)
// src/map/skill.cpp:4643
return USESKILL_FAIL_MAX; // Don't show a skill fail message (NoDamage type doesn't consume requirements)
// src/map/skill.cpp:4646
case AL_HEAL:
// src/map/skill.cpp:4651
case AB_HIGHNESSHEAL:
// src/map/skills/acolyte/decagi.cpp:13
void SkillDecreaseAgi::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
// src/map/skills/acolyte/decagi.cpp:18
clif_skill_nodamage(src, *bl, getSkillId(), skill_lv, sc_start(src, bl, type, (50 + skill_lv * 3 + (status_get_lv(src) + sstatus->int_) / 5), skill_lv, skill_get_time(getSkillId(), skill_lv)));
// src/map/skills/acolyte/skill_factory_acolyte.cpp:174
case AL_HEAL:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:175
return std::make_unique<SkillHeal>();
```

### Aqua Benedicta (`AL_HOLYWATER`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；伤害标记：NoDamage；消耗/限制：SP 10；状态 Water。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/holywater.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:8416
skill_lv += sc->getSCE(SC_RAISINGDRAGON)->val1;
// src/map/skill.cpp:8417
if(sd.spiritball >= skill_lv) {
// src/map/skill.cpp:12951
make_per = 100000; // Star Crumbs are 100% success crafting rate? (made 1000% so it succeeds even after penalties) [Skotlex]
// src/map/skill.cpp:12965
case AM_PHARMACY: // Potion Preparation - reviewed with the help of various Ragnainfo sources [DracoRPG]
// src/map/skills/acolyte/holywater.cpp:12
void SkillHolyWater::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
// src/map/skills/acolyte/holywater.cpp:14
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/skill_factory_acolyte.cpp:174
case AL_HEAL:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:175
return std::make_unique<SkillHeal>();
```

### Signum Crucis (`AL_CRUCIS`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；范围：15；吟唱：500 ms；技能后摇：2000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 35；关联状态：SignumCrucis。

- 技能树最高等级：`10`
- 前置技能：AL_DEMONBANE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/crucis.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/crucis.cpp:14
void SkillCrucis::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
// src/map/skills/acolyte/crucis.cpp:19
sc_start(src, bl, type, 25 + skill_lv * 4 + status_get_lv(src) - status_get_lv(bl), skill_lv, skill_get_time(getSkillId(), skill_lv));
// src/map/skills/acolyte/crucis.cpp:22
map_foreachinallrange(skill_area_sub, src, skill_get_splash(getSkillId(), skill_lv), BL_CHAR, src, getSkillId(), skill_lv, tick, flag | BCT_ENEMY | 1, skill_castend_nodamage_id);
// src/map/skills/acolyte/skill_factory_acolyte.cpp:174
case AL_HEAL:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:175
return std::make_unique<SkillHeal>();
```

### Angelus (`AL_ANGELUS`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；范围：-1；吟唱：500 ms；技能后摇：3500 ms；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000; Lv6=180000; Lv7=210000; Lv8=240000; Lv9=270000; Lv10=300000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=23; Lv2=26; Lv3=29; Lv4=32; Lv5=35; Lv6=38; Lv7=41; Lv8=44; Lv9=47; Lv10=50；关联状态：Angelus。

- 技能树最高等级：`10`
- 前置技能：AL_DP Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/angelus.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/angelus.cpp:14
void SkillAngelus::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
// src/map/skills/acolyte/angelus.cpp:16
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/skill_factory_acolyte.cpp:174
case AL_HEAL:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:175
return std::make_unique<SkillHeal>();
```

### Blessing (`AL_BLESSING`)

魔法技能；目标：友方目标；最高等级 10；射程：9；命中类型：Single；段数：1；持续时间1：Lv1=60000; Lv2=80000; Lv3=100000; Lv4=120000; Lv5=140000; Lv6=160000; Lv7=180000; Lv8=200000; Lv9=220000; Lv10=240000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=28; Lv2=32; Lv3=36; Lv4=40; Lv5=44; Lv6=48; Lv7=52; Lv8=56; Lv9=60; Lv10=64；关联状态：Blessing。

- 技能树最高等级：`10`
- 前置技能：AL_DP Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/blessing.cpp`, `src/map/skills/acolyte/crementia.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:2882
damage = dmg.damage + dmg.damage2;
// src/map/skill.cpp:2886
sce->val3 = (int32)damage;
// src/map/skill.cpp:2889
skill_castend_damage_id(bl, src, NPC_MAXPAIN_ATK, sce->val1, tick, flag);
// src/map/skill.cpp:2895
damage = 1;
// src/map/skill.cpp:2897
if( damage && tsc && tsc->getSCE(SC_GENSOU) && dmg.flag&BF_MAGIC ){
// src/map/skill.cpp:2901
damage = damage / 2; // Deflect half of the damage to a target nearby
// src/map/skill.cpp:2902
clif_skill_damage( *bl, *nbl, tick, status_get_amotion(src), 0, battle_fix_damage(bl,nbl,damage,0,0), dmg.div_, OB_OBOROGENSOU_TRANSITION_ATK, -1, DMG_SINGLE );
// src/map/skill.cpp:7213
sc_start(ss, bl, SC_INCMSPRATE, 100, 100, time);
// src/map/skill.cpp:7219
sc_start(ss, bl, SC_INCALLSTATUS, 100, 20, time);
// src/map/skill.cpp:7225
sc_start(ss, bl, SC_BLESSING, 100, 10, skill_get_time(AL_BLESSING, 10));
// src/map/skill.cpp:7228
sc_start(ss, bl, SC_INCREASEAGI, 100, 10, skill_get_time(AL_INCAGI, 10));
// src/map/skill.cpp:7231
sc_start(ss, bl, SC_ASPERSIO, 100, 1, time);
```

### Cure (`AL_CURE`)

魔法技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；技能后摇：1000 ms；持续时间2：6000 ms；伤害标记：NoDamage；消耗/限制：SP 15。

- 技能树最高等级：`1`
- 前置技能：AL_HEAL Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/cure.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/cure.cpp:13
void SkillCure::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
// src/map/skills/acolyte/cure.cpp:17
clif_skill_nodamage(src, *bl, getSkillId(), skill_lv, false);
// src/map/skills/acolyte/cure.cpp:20
status_change_end(bl, SC_SILENCE);
// src/map/skills/acolyte/cure.cpp:21
status_change_end(bl, SC_BLIND);
// src/map/skills/acolyte/skill_factory_acolyte.cpp:174
case AL_HEAL:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:175
return std::make_unique<SkillHeal>();
```

### Holy Light (`AL_HOLYLIGHT`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Holy；吟唱：2000 ms；消耗/限制：SP 15。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/holylight.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1291
if ((sce = sc->getSCE(SC_KYRIE)) && damage > 0) {
// src/map/battle.cpp:1292
sce->val2 -= static_cast<int32>(cap_value(damage, INT_MIN, INT_MAX));
// src/map/battle.cpp:1295
damage = 0;
// src/map/battle.cpp:1297
damage = -sce->val2;
// src/map/battle.cpp:1302
status_change_end(target, SC_KYRIE);
// src/map/battle.cpp:1309
element = battle_get_weapon_element(*d, *src, *target, skill_id, skill_lv, EQI_HAND_L, false);
// src/map/battle.cpp:1311
element = battle_get_weapon_element(*d, *src, *target, skill_id, skill_lv, EQI_HAND_R, false);
// src/map/battle.cpp:1313
element = battle_get_magic_element(*d, *src, *target, skill_id, skill_lv);
// src/map/battle.cpp:7523
clif_status_change(src, EFST_POSTDELAY, 1, autospell_tick, 0, 0, 0);
// src/map/battle.cpp:7537
if( (type = skill_get_casttype(r_skill)) == CAST_GROUND ) {
// src/map/battle.cpp:7541
if( !(BL_PC&battle_config.skill_reiteration) && skill->unit_flag[UF_NOREITERATION] )
// src/map/skill.cpp:9606
require = skill_get_requirement(sd,skill_id,skill_lv);
```
