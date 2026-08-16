# Thief 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 48 | `TF_DOUBLE` | Double Attack | 10 | Thief | 是 | — | Weapon / Passive |
| 49 | `TF_MISS` | Improve Dodge | 10 | Thief | 是 | — | Weapon / Passive |
| 50 | `TF_STEAL` | Steal | 10 | Thief | 是 | — | Weapon / Attack |
| 51 | `TF_HIDING` | Hiding | 10 | Thief | 是 | TF_STEAL Lv5 | None / Self |
| 52 | `TF_POISON` | Envenom | 10 | Thief | 是 | — | Weapon / Attack |
| 53 | `TF_DETOXIFY` | Detoxify | 1 | Thief | 是 | TF_POISON Lv3 | Weapon / Support |
| 149 | `TF_SPRINKLESAND` | Sand Attack | 1 | Thief | 是 | — | Weapon / Attack |
| 150 | `TF_BACKSLIDING` | Back Slide | 1 | Thief | 是 | — | Weapon / Self |
| 151 | `TF_PICKSTONE` | Find Stone | 1 | Thief | 是 | — | None / Self |
| 152 | `TF_THROWSTONE` | Stone Fling | 1 | Thief | 是 | — | Misc / Attack |

## 技能详情

### Double Attack (`TF_DOUBLE`)

武器/物理技能；目标：被动；最高等级 10；射程：-1；命中类型：Multi_Hit；段数：2；属性：Weapon。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/mob.cpp`, `src/map/skill.cpp`, `src/map/skills/thief/doubleattack.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

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
// src/map/battle.cpp:3049
cri += sd->indexed_bonus.critaddrace[tstatus->race] + sd->indexed_bonus.critaddrace[RC_ALL];
// src/map/battle.cpp:3288
if (sd) //in Renewal hit bonus from Vultures Eye is not anymore shown in status window
// src/map/battle.cpp:3289
hitrate += pc_checkskill(sd,AC_VULTURE);
// src/map/battle.cpp:3295
skill->impl->modifyHitRate(hitrate, src, target, skill_lv);
// src/map/battle.cpp:3297
} else if (sd && wd->type&DMG_MULTI_HIT && wd->div_ == 2) // +1 hit per level of Double Attack on a successful double attack (making sure other multi attack skills do not trigger this) [helvetica]
```

### Improve Dodge (`TF_MISS`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:4505
base_status->hit += 20;
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
// src/map/status.cpp:8143
if( sc->getSCE(SC_MARSHOFABYSS) && speed_rate > 150 )
// src/map/status.cpp:8144
speed_rate = 150;
```

### Steal (`TF_STEAL`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`, `src/map/skills/thief/steal.cpp`

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
// src/map/skills/thief/steal.cpp:13
void SkillSteal::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/thief/steal.cpp:14
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/thief/steal.cpp:17
if (pc_steal_item(sd, bl, skill_lv))
```

### Hiding (`TF_HIDING`)

非伤害技能；目标：自身；最高等级 10；射程：1；命中类型：Single；段数：1；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000; Lv6=180000; Lv7=210000; Lv8=240000; Lv9=270000; Lv10=300000 ms；伤害标记：NoDamage；消耗/限制：SP 10；关联状态：Hiding。

- 技能树最高等级：`10`
- 前置技能：TF_STEAL Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/thief/hiding.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/thief/hiding.cpp:12
void SkillHiding::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/thief/hiding.cpp:14
status_change *tsc = status_get_sc(bl);
// src/map/skills/thief/hiding.cpp:15
status_change_entry *tsce = tsc ? tsc->getSCE(SC_HIDING) : nullptr;
// src/map/skills/thief/hiding.cpp:18
clif_skill_nodamage(src, *bl, getSkillId(), -1, status_change_end(bl, type)); // Hide skill-scream animation.
```

### Envenom (`TF_POISON`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-2；命中类型：Single；段数：1；属性：Poison；持续时间2：60000 ms；消耗/限制：SP 12；关联状态：Poison。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/thief/envenom.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3711
ATK_ADD2(wd->damage, wd->damage2, sd->right_weapon.star, sd->left_weapon.star);
// src/map/battle.cpp:3716
ATK_ADD(wd->damage, wd->damage2, battle_get_spiritball_damage(*wd, *src, skill_id));
// src/map/battle.cpp:3721
ATK_ADD(wd->damage, wd->damage2, 15 * skill_lv);
// src/map/battle.cpp:3723
wd->damage = battle_attr_fix(src, target, wd->damage, right_element, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3726
ATK_ADD(wd->damage, wd->damage2, 4 * skill_lv);
// src/map/battle.cpp:3728
ATK_ADD(wd->damage, wd->damage2, 3 * pc_checkskill(sd, NJ_TOBIDOUGU));
// src/map/battle.cpp:3729
ATK_ADD(wd->damage, wd->damage2, sd->bonus.arrow_atk);
// src/map/battle.cpp:3732
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3804
wd->damage2 = battle_addmastery(sd,target,wd->damage2,1);
// src/map/battle.cpp:3812
if(skill_id == TF_POISON) //Additional ATK from Envenom is treated as mastery type damage [helvetica]
// src/map/battle.cpp:3813
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, 15 * skill_lv);
// src/map/battle.cpp:3819
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, battle_get_spiritball_damage(*wd, *src, skill_id));
```

### Detoxify (`TF_DETOXIFY`)

武器/物理技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Poison；伤害标记：NoDamage；消耗/限制：SP 10。

- 技能树最高等级：`1`
- 前置技能：TF_POISON Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/thief/detoxify.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/thief/detoxify.cpp:12
void SkillDetoxify::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/thief/detoxify.cpp:13
clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);
// src/map/skills/thief/detoxify.cpp:14
status_change_end(bl, SC_POISON);
// src/map/skills/thief/detoxify.cpp:15
status_change_end(bl, SC_DPOISON);
```

### Sand Attack (`TF_SPRINKLESAND`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：1；命中类型：Single；段数：1；属性：Earth；持续时间2：30000 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP 9；关联状态：Blind。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/thief/sandattack.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4579
RE_ALLATK_ADDRATE(wd, map_flag_gvg2(src->m) ? 25 : 100); //+25% dmg on woe/+100% dmg on nonwoe
// src/map/battle.cpp:4581
ATK_ADDRATE(wd->damage, wd->damage2, 100);
// src/map/battle.cpp:4582
RE_ALLATK_ADDRATE(wd, 100);
// src/map/battle.cpp:4586
ATK_ADDRATE(wd->damage, wd->damage2, sc->getSCE(SC_GT_CHANGE)->val1);
// src/map/battle.cpp:4602
ATK_RATE(wd->weaponAtk, wd->weaponAtk2, 250 + (sc->getSCE(SC_EDP)->val1 * 30));
// src/map/battle.cpp:4603
ATK_RATE(wd->equipAtk, wd->equipAtk2, 250 + (sc->getSCE(SC_EDP)->val1 * 30));
// src/map/skills/thief/sandattack.cpp:12
void SkillSandAttack::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/thief/sandattack.cpp:13
base_skillratio += 30;
// src/map/skills/thief/sandattack.cpp:16
void SkillSandAttack::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/thief/sandattack.cpp:17
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/thief/sandattack.cpp:18
sc_start(src, target, SC_BLIND, (sd != nullptr) ? 20 : 15, skill_lv, skill_get_time2(getSkillId(), skill_lv));
```

### Back Slide (`TF_BACKSLIDING`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；击退：5；伤害标记：NoDamage；消耗/限制：SP 7。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/thief/backslide.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/thief/backslide.cpp:13
void SkillBackSlide::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/thief/backslide.cpp:21
int16 blew_count = skill_blown(src, bl, skill_get_blewcount(getSkillId(), skill_lv), unit_getdir(bl),
// src/map/skills/thief/backslide.cpp:22
static_cast<enum e_skill_blown>(BLOWN_IGNORE_NO_KNOCKBACK | BLOWN_DONT_SEND_PACKET));
// src/map/status.cpp:13687
status_change_end(src, SC_CLOSECONFINE);
// src/map/status.cpp:13697
map_foreachinallarea(status_change_timer_sub,
```

### Find Stone (`TF_PICKSTONE`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：500 ms；伤害标记：NoDamage；消耗/限制：SP 3；状态 Recover_Weight_Rate；关联状态：Stun。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/thief/findstone.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/thief/findstone.cpp:15
void SkillFindStone::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/thief/findstone.cpp:16
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/thief/findstone.cpp:22
clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);
```

### Stone Fling (`TF_THROWSTONE`)

特殊技能；目标：敌方目标；最高等级 1；射程：7；命中类型：Single；段数：1；持续时间1：5000 ms；持续时间2：30000 ms；伤害标记：IgnoreFlee；消耗/限制：SP 2；道具 Stone×1；关联状态：Stun。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`, `src/map/skills/thief/stonefling.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1281
* @return True: Damage inflicted, False: Missed
// src/map/battle.cpp:1283
bool battle_status_block_damage(block_list *src, block_list *target, status_change *sc, struct Damage *d, int64 &damage, uint16 skill_id, uint16 skill_lv) {
// src/map/battle.cpp:1287
status_change_entry *sce;
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
// src/map/battle.cpp:6332
s_ele = battle_get_misc_element(md, *src, *target, skill_id, skill_lv);
// src/map/battle.cpp:6335
md.flag |= battle_range_type(src, target, skill_id, skill_lv);
// src/map/battle.cpp:6339
skill->impl->modifyDamageData(md, *src, *target, skill_lv);
// src/map/battle.cpp:6345
md.damage = 50;
```
