# Assassin 技能

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
| 132 | `AS_RIGHT` | Righthand Mastery | 5 | Assassin | 是 | — | Weapon / Passive |
| 133 | `AS_LEFT` | Lefthand Mastery | 5 | Assassin | 是 | AS_RIGHT Lv2 | Weapon / Passive |
| 134 | `AS_KATAR` | Katar Mastery | 10 | Assassin | 是 | — | Weapon / Passive |
| 135 | `AS_CLOAKING` | Cloaking | 10 | Assassin | 是 | TF_HIDING Lv2 | Weapon / Self |
| 136 | `AS_SONICBLOW` | Sonic Blow | 10 | Assassin | 是 | AS_KATAR Lv4 | Weapon / Attack |
| 137 | `AS_GRIMTOOTH` | Grimtooth | 5 | Assassin | 是 | AS_CLOAKING Lv2, AS_SONICBLOW Lv5 | Weapon / Attack |
| 138 | `AS_ENCHANTPOISON` | Enchant Poison | 10 | Assassin | 是 | TF_POISON Lv1 | Weapon / Support |
| 139 | `AS_POISONREACT` | Poison React | 10 | Assassin | 是 | AS_ENCHANTPOISON Lv3 | Weapon / Self |
| 140 | `AS_VENOMDUST` | Venom Dust | 10 | Assassin | 是 | AS_ENCHANTPOISON Lv5 | Weapon / Ground |
| 141 | `AS_SPLASHER` | Venom Splasher | 10 | Assassin | 是 | AS_POISONREACT Lv5, AS_VENOMDUST Lv5 | Weapon / Attack |
| 1003 | `AS_SONICACCEL` | Sonic Acceleration | 1 | Assassin | 是 | — | Weapon / Passive |
| 1004 | `AS_VENOMKNIFE` | Throw Venom Knife | 1 | Assassin | 是 | — | Weapon / Attack |

## 技能详情

### Righthand Mastery (`AS_RIGHT`)

武器/物理技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5034
if(sd->status.weapon == W_KATAR && !skill_id) { //Katars (offhand damage only applies to normal attacks, tested on Aegis 10.2)
// src/map/battle.cpp:5036
wd->damage2 = (int64)wd->damage * (1 + (skill * 2))/100;
// src/map/battle.cpp:5043
if (is_attack_right_handed(src, skill_id) && wd->damage) {
// src/map/battle.cpp:5046
ATK_RATER(wd->damage, 50 + (skill * 10))
// src/map/battle.cpp:5050
ATK_RATER(wd->damage, 70 + (skill * 10))
// src/map/battle.cpp:5052
if(wd->damage < 1)
// src/map/battle.cpp:5053
wd->damage = 1;
// src/map/battle.cpp:5056
if (wd->damage2) {
```

### Lefthand Mastery (`AS_LEFT`)

武器/物理技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：AS_RIGHT Lv2
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/pc.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5046
ATK_RATER(wd->damage, 50 + (skill * 10))
// src/map/battle.cpp:5050
ATK_RATER(wd->damage, 70 + (skill * 10))
// src/map/battle.cpp:5052
if(wd->damage < 1)
// src/map/battle.cpp:5053
wd->damage = 1;
// src/map/battle.cpp:5056
if (wd->damage2) {
// src/map/battle.cpp:5059
ATK_RATEL(wd->damage2, 30 + (skill * 10))
// src/map/battle.cpp:5063
ATK_RATEL(wd->damage2, 50 + (skill * 10))
// src/map/battle.cpp:5065
if(wd->damage2 < 1)
// src/map/battle.cpp:5066
wd->damage2 = 1;
```

### Katar Mastery (`AS_KATAR`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2383
damage += (skill * 3);
// src/map/battle.cpp:2387
damage += (skill * 3);
// src/map/battle.cpp:2391
damage += (skill * 3);
// src/map/battle.cpp:2395
damage += (skill * 3);
// src/map/battle.cpp:2399
return damage;
// src/map/battle.cpp:2402
/** Calculates overrefine damage bonus and weapon related bonuses (unofficial)
// src/map/battle.cpp:2404
* @param damage Current damage
```

### Cloaking (`AS_CLOAKING`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：Lv1=500; Lv2=1000; Lv3=2000; Lv4=3000; Lv5=4000; Lv6=5000; Lv7=6000; Lv8=7000; Lv9=8000; Lv10=9000 ms；伤害标记：NoDamage；消耗/限制：SP 15；关联状态：Cloaking。

- 技能树最高等级：`10`
- 前置技能：TF_HIDING Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/cloaking.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:8381
case SA_CASTCANCEL:
// src/map/skill.cpp:8389
if( skill_lv < 3 && ((sd.type == BL_PC && battle_config.pc_cloak_check_type&1)
// src/map/skills/thief/cloaking.cpp:13
void SkillCloaking::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/thief/cloaking.cpp:14
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/thief/cloaking.cpp:16
status_change *tsc = status_get_sc(target);
// src/map/skills/thief/cloaking.cpp:17
status_change_entry *tsce = (tsc && type != SC_NONE)?tsc->getSCE(type):nullptr;
// src/map/skills/thief/cloaking.cpp:21
i = status_change_end(target, type);
```

### Sonic Blow (`AS_SONICBLOW`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：1；命中类型：Multi_Hit；段数：-8；属性：Weapon；技能后摇：2000 ms；移动后摇：2000 ms；持续时间2：5000 ms；消耗/限制：SP Lv1=16; Lv2=18; Lv3=20; Lv4=22; Lv5=24; Lv6=26; Lv7=28; Lv8=30; Lv9=32; Lv10=34；武器 Katar；关联状态：Stun。

- 技能树最高等级：`10`
- 前置技能：AS_KATAR Lv4
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`, `src/map/skills/thief/sonicblow.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4566
ATK_ADD(wd->weaponAtk, wd->weaponAtk2, i64max(sstatus->matk_min - tmdef, 0));
// src/map/battle.cpp:4573
ATK_RATE(wd->damage, wd->damage2, battle_get_atkpercent(*src, skill_id, *sc));
// src/map/battle.cpp:4574
ATK_RATER(wd->basedamage, battle_get_atkpercent(*src, 0, *sc));
// src/map/battle.cpp:4578
ATK_ADDRATE(wd->damage, wd->damage2, map_flag_gvg2(src->m) ? 25 : 100); //+25% dmg on woe/+100% dmg on nonwoe
// src/map/battle.cpp:4579
RE_ALLATK_ADDRATE(wd, map_flag_gvg2(src->m) ? 25 : 100); //+25% dmg on woe/+100% dmg on nonwoe
// src/map/battle.cpp:4581
ATK_ADDRATE(wd->damage, wd->damage2, 100);
// src/map/battle.cpp:4582
RE_ALLATK_ADDRATE(wd, 100);
// src/map/battle.cpp:4586
ATK_ADDRATE(wd->damage, wd->damage2, sc->getSCE(SC_GT_CHANGE)->val1);
// src/map/battle.cpp:4923
ATK_ADD(wd->damage, wd->damage2, (3 + sc->getSCE(SC_AURABLADE)->val1) * status_get_lv(src)); // !TODO: Confirm formula
// src/map/battle.cpp:4925
ATK_ADD(wd->damage, wd->damage2, 20 * sc->getSCE(SC_AURABLADE)->val1);
// src/map/battle.cpp:4931
battle_min_damage(*wd, *src, skill_id, 1);
// src/map/battle.cpp:4937
ATK_ADDRATE(wd->damage, wd->damage2, 90);
```

### Grimtooth (`AS_GRIMTOOTH`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：Lv1=3; Lv2=4; Lv3=5; Lv4=6; Lv5=7；命中类型：Single；段数：1；属性：Weapon；范围：1；持续时间2：1000 ms；伤害标记：Splash；消耗/限制：SP 3；武器 Katar；前置状态 Hiding。

- 技能树最高等级：`5`
- 前置技能：AS_CLOAKING Lv2, AS_SONICBLOW Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/thief/grimtooth.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4582
RE_ALLATK_ADDRATE(wd, 100);
// src/map/battle.cpp:4586
ATK_ADDRATE(wd->damage, wd->damage2, sc->getSCE(SC_GT_CHANGE)->val1);
// src/map/battle.cpp:4602
ATK_RATE(wd->weaponAtk, wd->weaponAtk2, 250 + (sc->getSCE(SC_EDP)->val1 * 30));
// src/map/battle.cpp:4603
ATK_RATE(wd->equipAtk, wd->equipAtk2, 250 + (sc->getSCE(SC_EDP)->val1 * 30));
// src/map/skills/thief/grimtooth.cpp:9
SkillGrimtooth::SkillGrimtooth() : SkillImplRecursiveDamageSplash(AS_GRIMTOOTH) {
// src/map/skills/thief/grimtooth.cpp:12
void SkillGrimtooth::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/thief/grimtooth.cpp:13
base_skillratio += 20 * skill_lv;
// src/map/skills/thief/grimtooth.cpp:16
void SkillGrimtooth::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/thief/grimtooth.cpp:17
flag |= SD_PREAMBLE; // a fake packet will be sent for the first target to be hit
// src/map/skills/thief/grimtooth.cpp:19
SkillImplRecursiveDamageSplash::castendDamageId(src, target, skill_lv, tick, flag);
```

### Enchant Poison (`AS_ENCHANTPOISON`)

武器/物理技能；目标：友方目标；最高等级 10；射程：1；命中类型：Single；段数：1；属性：Poison；持续时间1：Lv1=30000; Lv2=45000; Lv3=60000; Lv4=75000; Lv5=90000; Lv6=105000; Lv7=120000; Lv8=135000; Lv9=150000; Lv10=165000 ms；持续时间2：Lv1=10000; Lv2=20000; Lv3=30000; Lv4=40000; Lv5=50000; Lv6=60000; Lv7=70000; Lv8=80000; Lv9=90000; Lv10=100000 ms；伤害标记：NoDamage；消耗/限制：SP 20；关联状态：EncPoison。

- 技能树最高等级：`10`
- 前置技能：TF_POISON Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/enchantpoison.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
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
// src/map/skill.cpp:1400
skill_get_time2(ASC_EDP,sce->val1));
// src/map/skill.cpp:1402
skill_castend_nodamage_id(src, bl, RK_STORMBLAST, 1, tick, 0);
// src/map/skills/thief/enchantpoison.cpp:13
void SkillEnchantPoison::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/thief/enchantpoison.cpp:15
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/thief/enchantpoison.cpp:17
if( sc_start( src, target, type, 100, skill_lv, skill_get_time( getSkillId(), skill_lv ) ) ){
// src/map/skills/thief/enchantpoison.cpp:18
clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
```

### Poison React (`AS_POISONREACT`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：Lv1=20000; Lv2=25000; Lv3=30000; Lv4=35000; Lv5=40000; Lv6=45000; Lv7=50000; Lv8=55000; Lv9-10=60000 ms；持续时间2：60000 ms；消耗/限制：SP Lv1=25; Lv2=30; Lv3=35; Lv4=40; Lv5=45; Lv6=50; Lv7=55; Lv8=60; Lv9-10=45；关联状态：PoisonReact。

- 技能树最高等级：`10`
- 前置技能：AS_ENCHANTPOISON Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`, `src/map/skills/thief/venomsplasher.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4428
skillratio += sc->getSCE(SC_MAXOVERTHRUST)->val2;
// src/map/battle.cpp:4431
skillratio += 100;
// src/map/battle.cpp:4433
skillratio += 200;
// src/map/battle.cpp:4436
if (const status_change_entry* sce = sc->getSCE(SC_POISONREACT); sce != nullptr && sce->val4 == 1) {
// src/map/battle.cpp:4439
skillratio += 30 * pc_checkskill(sd, AS_POISONREACT);
// src/map/battle.cpp:4441
skillratio += 30 * sce->val1;
// src/map/battle.cpp:4443
sc_start2(src, target, SC_POISON, sce->val3, sce->val1, src->id, skill_get_time2(AS_POISONREACT, sce->val1), sstatus->amotion);
// src/map/battle.cpp:4444
status_change_end(src, SC_POISONREACT);
// src/map/battle.cpp:4447
if (sd) { //ATK [{Weapon Level * (Weapon Upgrade Level + 6) * 100} + (Weapon ATK) + (Weapon Weight)]%
// src/map/battle.cpp:4451
skillratio += -100 + sd->inventory_data[index]->weight / 10 + sd->inventory_data[index]->atk +
// src/map/battle.cpp:4454
status_change_end(src,SC_CRUSHSTRIKE);
// src/map/skills/thief/venomsplasher.cpp:12
SkillVenomSplasher::SkillVenomSplasher() : SkillImplRecursiveDamageSplash(AS_SPLASHER) {
```

### Venom Dust (`AS_VENOMDUST`)

武器/物理技能；目标：地面区域；最高等级 10；射程：2；命中类型：Single；段数：1；属性：Poison；持续时间1：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000; Lv6=30000; Lv7=35000; Lv8=40000; Lv9=45000; Lv10=50000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP 20；道具 Red_Gemstone×1；关联状态：Poison。

- 技能树最高等级：`10`
- 前置技能：AS_ENCHANTPOISON Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`, `src/map/skills/thief/venomdust.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:3408
case NPC_REVERBERATION:
// src/map/skill.cpp:3425
static int32 skill_check_unit_range (block_list *bl, int32 x, int32 y, uint16 skill_id, uint16 skill_lv)
// src/map/skills/thief/venomdust.cpp:10
void SkillVenomDust::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/thief/venomdust.cpp:12
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Venom Splasher (`AS_SPLASHER`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：1；命中类型：Single；段数：1；属性：Weapon；范围：2；吟唱：1000 ms；冷却：Lv1=7500; Lv2=8000; Lv3=8500; Lv4=9000; Lv5=9500; Lv6=10000; Lv7=10500; Lv8=11000; Lv9=11500; Lv10=12000 ms；持续时间1：Lv1=11000; Lv2=10000; Lv3=9000; Lv4=8000; Lv5=7000; Lv6=6000; Lv7=5000; Lv8=4000; Lv9=3000; Lv10=2000 ms；持续时间2：60000 ms；伤害标记：NoDamage, IgnoreAtkCard, IgnoreFlee；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30；道具 Red_Gemstone×1；关联状态：Splasher。

- 技能树最高等级：`10`
- 前置技能：AS_POISONREACT Lv5, AS_VENOMDUST Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`, `src/map/skills/thief/venomsplasher.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3234
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/battle.cpp:3235
std::bitset<NK_MAX> nk = battle_skill_get_damage_properties(skill_id, wd->miscflag);
// src/map/battle.cpp:3236
int16 flee, hitrate;
// src/map/battle.cpp:3239
return (wd->dmg_lv != ATK_FLEE);
// src/map/battle.cpp:3240
if (is_attack_critical(wd, src, target, skill_id, skill_lv, false))
// src/map/battle.cpp:3252
else if (nk[NK_IGNOREFLEE])
// src/map/battle.cpp:3258
flee = tstatus->flee;
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
```

### Sonic Acceleration (`AS_SONICACCEL`)

武器/物理技能；目标：被动；最高等级 1。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/thief/sonicblow.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4925
ATK_ADD(wd->damage, wd->damage2, 20 * sc->getSCE(SC_AURABLADE)->val1);
// src/map/battle.cpp:4931
battle_min_damage(*wd, *src, skill_id, 1);
// src/map/battle.cpp:4937
ATK_ADDRATE(wd->damage, wd->damage2, 90);
// src/map/battle.cpp:4944
* "Plant"-type (mobs that only take 1 damage from all sources) damage calculation
// src/map/skills/thief/sonicblow.cpp:14
void SkillSonicBlow::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/thief/sonicblow.cpp:18
base_skillratio += 100 + 100 * skill_lv;
// src/map/skills/thief/sonicblow.cpp:19
if (tstatus->hp < (tstatus->max_hp / 2))
// src/map/skills/thief/sonicblow.cpp:20
base_skillratio += base_skillratio / 2;
// src/map/skills/thief/sonicblow.cpp:22
const map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/thief/sonicblow.cpp:24
base_skillratio += 200 + 50 * skill_lv;
// src/map/skills/thief/sonicblow.cpp:26
base_skillratio += base_skillratio / 10;
// src/map/skills/thief/sonicblow.cpp:30
void SkillSonicBlow::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
```

### Throw Venom Knife (`AS_VENOMKNIFE`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Multi_Hit；段数：1；持续时间2：60000 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP 15；弹药数 1；弹药 Dagger；关联状态：Poison。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/pc.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`, `src/map/skills/thief/throwvenomknife.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4586
ATK_ADDRATE(wd->damage, wd->damage2, sc->getSCE(SC_GT_CHANGE)->val1);
// src/map/battle.cpp:4602
ATK_RATE(wd->weaponAtk, wd->weaponAtk2, 250 + (sc->getSCE(SC_EDP)->val1 * 30));
// src/map/battle.cpp:4603
ATK_RATE(wd->equipAtk, wd->equipAtk2, 250 + (sc->getSCE(SC_EDP)->val1 * 30));
// src/map/skills/thief/throwvenomknife.cpp:13
void SkillThrowVenomKnife::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/thief/throwvenomknife.cpp:15
base_skillratio += 400;
// src/map/skills/thief/throwvenomknife.cpp:19
void SkillThrowVenomKnife::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/thief/throwvenomknife.cpp:20
sc_start2(src, target, SC_POISON, 100, skill_lv, src->id, skill_get_time2(getSkillId(), skill_lv));
```
