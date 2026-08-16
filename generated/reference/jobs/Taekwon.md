# Taekwon 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 411 | `TK_RUN` | Running | 10 | Taekwon | 是 | — | Misc / Self |
| 412 | `TK_READYSTORM` | Tornado Stance | 1 | Taekwon | 是 | TK_STORMKICK Lv1 | Weapon / Self |
| 413 | `TK_STORMKICK` | Tornado Kick | 7 | Taekwon | 是 | — | Weapon / Self |
| 414 | `TK_READYDOWN` | Heel Drop Stance | 1 | Taekwon | 是 | TK_DOWNKICK Lv1 | Weapon / Self |
| 415 | `TK_DOWNKICK` | Heel Drop | 7 | Taekwon | 是 | — | Weapon / Self |
| 416 | `TK_READYTURN` | Roundhouse Stance | 1 | Taekwon | 是 | TK_TURNKICK Lv1 | Weapon / Self |
| 417 | `TK_TURNKICK` | Roundhouse Kick | 7 | Taekwon | 是 | — | Weapon / Self |
| 418 | `TK_READYCOUNTER` | Counter Kick Stance | 1 | Taekwon | 是 | TK_COUNTER Lv1 | Weapon / Self |
| 419 | `TK_COUNTER` | Counter Kick | 7 | Taekwon | 是 | — | Weapon / Self |
| 420 | `TK_DODGE` | Tumbling | 1 | Taekwon | 是 | TK_JUMPKICK Lv7 | Weapon / Self |
| 421 | `TK_JUMPKICK` | Flying Kick | 7 | Taekwon | 是 | — | Weapon / Attack |
| 422 | `TK_HPTIME` | Peaceful Break | 10 | Taekwon | 是 | — | None / Passive |
| 423 | `TK_SPTIME` | Happy Break | 10 | Taekwon | 是 | — | None / Passive |
| 424 | `TK_POWER` | Kihop | 5 | Taekwon | 是 | — | Weapon / Passive |
| 425 | `TK_SEVENWIND` | Mild Wind | 7 | Taekwon | 是 | TK_HPTIME Lv5, TK_SPTIME Lv5, TK_POWER Lv5 | Weapon / Self |
| 426 | `TK_HIGHJUMP` | Taekwon Jump | 5 | Taekwon | 是 | — | Weapon / Self |
| 493 | `TK_MISSION` | Taekwon Mission | 1 | Taekwon | 是 | TK_POWER Lv5 | None / Self |

## 技能详情

### Running (`TK_RUN`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；击退：4；吟唱：Lv1=6000; Lv2=5000; Lv3=4000; Lv4=3000; Lv5=2000; Lv6=1000 ms；持续时间1：1000 ms；持续时间2：150000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=100; Lv2=90; Lv3=80; Lv4=70; Lv5=60; Lv6=50; Lv7=40; Lv8=30; Lv9=20; Lv10=10；状态 Move_Enable；关联状态：Run。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/run.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2362
damage += (skill * 3);
// src/map/battle.cpp:2364
damage += (skill * 5);
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
// src/map/battle.cpp:5654
if (tsd && tsd->bonus.crit_def_rate != 0)
// src/map/battle.cpp:5655
ATK_ADDRATE(wd.damage, wd.damage2, -tsd->bonus.crit_def_rate);
// src/map/battle.cpp:5665
ATK_ADD(wd.damage, wd.damage2, 10 * pc_checkskill(sd, TK_RUN));
// src/map/battle.cpp:5669
int32 damagevalue = 0;
// src/map/battle.cpp:5673
damagevalue = sstatus->vit * sd->inventory.u.items_inventory[index].refine;
```

### Tornado Stance (`TK_READYSTORM`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：ReadyStorm。

- 技能树最高等级：`1`
- 前置技能：TK_STORMKICK Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:13310
clif_skill_nodamage(bl,*bl,TK_READYSTORM,1);
// src/map/status.cpp:13314
clif_skill_nodamage(bl,*bl,TK_READYDOWN,1);
// src/map/status.cpp:13318
clif_skill_nodamage(bl,*bl,TK_READYTURN,1);
// src/map/status.cpp:13322
clif_skill_nodamage(bl,*bl,TK_READYCOUNTER,1);
```

### Tornado Kick (`TK_STORMKICK`)

武器/物理技能；目标：自身；最高等级 7；射程：-2；命中类型：Multi_Hit；段数：-3；属性：Weapon；范围：2；伤害标记：Splash；消耗/限制：SP Lv1=14; Lv2=12; Lv3=10; Lv4=8; Lv5=6; Lv6=4; Lv7=2。

- 技能树最高等级：`7`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`, `src/map/skills/taekwon/stormkick.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5650
wd.damage2 = (int64)floor((float)((wd.damage2 * (1.4f + (0.01f * sstatus->crate)))));
// src/map/battle.cpp:5652
wd.damage = (int64)floor((float)(wd.damage * 1.4f));
// src/map/battle.cpp:5654
if (tsd && tsd->bonus.crit_def_rate != 0)
// src/map/battle.cpp:5655
ATK_ADDRATE(wd.damage, wd.damage2, -tsd->bonus.crit_def_rate);
// src/map/battle.cpp:5665
ATK_ADD(wd.damage, wd.damage2, 10 * pc_checkskill(sd, TK_RUN));
// src/map/battle.cpp:5669
int32 damagevalue = 0;
// src/map/battle.cpp:5673
damagevalue = sstatus->vit * sd->inventory.u.items_inventory[index].refine;
// src/map/skill.cpp:1218
map_session_data* dstsd = BL_CAST( BL_PC, bl );
// src/map/skill.cpp:1219
mob_data* dstmd = BL_CAST( BL_MOB, bl );
// src/map/skill.cpp:1221
status_change* sc = status_get_sc( src );
// src/map/skill.cpp:1222
status_change* tsc = status_get_sc( bl );
// src/map/skill.cpp:1230
sc_start4(src, src, SC_COMBO, 15, TK_STORMKICK,
```

### Heel Drop Stance (`TK_READYDOWN`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：ReadyDown。

- 技能树最高等级：`1`
- 前置技能：TK_DOWNKICK Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:13310
clif_skill_nodamage(bl,*bl,TK_READYSTORM,1);
// src/map/status.cpp:13314
clif_skill_nodamage(bl,*bl,TK_READYDOWN,1);
// src/map/status.cpp:13318
clif_skill_nodamage(bl,*bl,TK_READYTURN,1);
// src/map/status.cpp:13322
clif_skill_nodamage(bl,*bl,TK_READYCOUNTER,1);
```

### Heel Drop (`TK_DOWNKICK`)

武器/物理技能；目标：自身；最高等级 7；射程：-2；命中类型：Multi_Hit；段数：-3；属性：Weapon；持续时间2：3000 ms；消耗/限制：SP Lv1=14; Lv2=12; Lv3=10; Lv4=8; Lv5=6; Lv6=4; Lv7=2；关联状态：Stun。

- 技能树最高等级：`7`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/downkick.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5648
wd.damage = (int64)floor((float)((wd.damage * (1.4f + (0.01f * sstatus->crate)))));
// src/map/battle.cpp:5650
wd.damage2 = (int64)floor((float)((wd.damage2 * (1.4f + (0.01f * sstatus->crate)))));
// src/map/battle.cpp:5652
wd.damage = (int64)floor((float)(wd.damage * 1.4f));
// src/map/battle.cpp:5654
if (tsd && tsd->bonus.crit_def_rate != 0)
// src/map/battle.cpp:5655
ATK_ADDRATE(wd.damage, wd.damage2, -tsd->bonus.crit_def_rate);
// src/map/battle.cpp:5665
ATK_ADD(wd.damage, wd.damage2, 10 * pc_checkskill(sd, TK_RUN));
// src/map/battle.cpp:5669
int32 damagevalue = 0;
// src/map/skill.cpp:1230
sc_start4(src, src, SC_COMBO, 15, TK_STORMKICK,
// src/map/skill.cpp:1235
sc_start4(src, src, SC_COMBO, 15, TK_DOWNKICK,
// src/map/skill.cpp:1240
sc_start4(src, src, SC_COMBO, 15, TK_TURNKICK,
// src/map/skill.cpp:1244
else if (sc->getSCE(SC_READYCOUNTER)) { //additional chance from SG_FRIEND [Komurka]
// src/map/skill.cpp:1245
int32 rate = 20;
```

### Roundhouse Stance (`TK_READYTURN`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：ReadyTurn。

- 技能树最高等级：`1`
- 前置技能：TK_TURNKICK Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:13310
clif_skill_nodamage(bl,*bl,TK_READYSTORM,1);
// src/map/status.cpp:13314
clif_skill_nodamage(bl,*bl,TK_READYDOWN,1);
// src/map/status.cpp:13318
clif_skill_nodamage(bl,*bl,TK_READYTURN,1);
// src/map/status.cpp:13322
clif_skill_nodamage(bl,*bl,TK_READYCOUNTER,1);
```

### Roundhouse Kick (`TK_TURNKICK`)

武器/物理技能；目标：自身；最高等级 7；射程：-2；命中类型：Multi_Hit；段数：-3；属性：Weapon；范围：1；击退：2；持续时间1：5000 ms；持续时间2：2000 ms；伤害标记：Splash；消耗/限制：SP Lv1=14; Lv2=12; Lv3=10; Lv4=8; Lv5=6; Lv6=4; Lv7=2。

- 技能树最高等级：`7`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`, `src/map/skills/taekwon/turnkick.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5650
wd.damage2 = (int64)floor((float)((wd.damage2 * (1.4f + (0.01f * sstatus->crate)))));
// src/map/battle.cpp:5652
wd.damage = (int64)floor((float)(wd.damage * 1.4f));
// src/map/battle.cpp:5654
if (tsd && tsd->bonus.crit_def_rate != 0)
// src/map/battle.cpp:5655
ATK_ADDRATE(wd.damage, wd.damage2, -tsd->bonus.crit_def_rate);
// src/map/battle.cpp:5665
ATK_ADD(wd.damage, wd.damage2, 10 * pc_checkskill(sd, TK_RUN));
// src/map/battle.cpp:5669
int32 damagevalue = 0;
// src/map/battle.cpp:5673
damagevalue = sstatus->vit * sd->inventory.u.items_inventory[index].refine;
// src/map/battle.cpp:5674
ATK_ADD(wd.damage, wd.damage2, damagevalue);
// src/map/skill.cpp:1230
sc_start4(src, src, SC_COMBO, 15, TK_STORMKICK,
// src/map/skill.cpp:1235
sc_start4(src, src, SC_COMBO, 15, TK_DOWNKICK,
// src/map/skill.cpp:1240
sc_start4(src, src, SC_COMBO, 15, TK_TURNKICK,
// src/map/skill.cpp:1244
else if (sc->getSCE(SC_READYCOUNTER)) { //additional chance from SG_FRIEND [Komurka]
```

### Counter Kick Stance (`TK_READYCOUNTER`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：ReadyCounter。

- 技能树最高等级：`1`
- 前置技能：TK_COUNTER Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:13310
clif_skill_nodamage(bl,*bl,TK_READYSTORM,1);
// src/map/status.cpp:13314
clif_skill_nodamage(bl,*bl,TK_READYDOWN,1);
// src/map/status.cpp:13318
clif_skill_nodamage(bl,*bl,TK_READYTURN,1);
// src/map/status.cpp:13322
clif_skill_nodamage(bl,*bl,TK_READYCOUNTER,1);
```

### Counter Kick (`TK_COUNTER`)

武器/物理技能；目标：自身；最高等级 7；射程：-2；命中类型：Multi_Hit；段数：-3；属性：Weapon；伤害标记：IgnoreFlee；消耗/限制：SP Lv1=14; Lv2=12; Lv3=10; Lv4=8; Lv5=6; Lv6=4; Lv7=2。

- 技能树最高等级：`7`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/counter.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5652
wd.damage = (int64)floor((float)(wd.damage * 1.4f));
// src/map/battle.cpp:5654
if (tsd && tsd->bonus.crit_def_rate != 0)
// src/map/battle.cpp:5655
ATK_ADDRATE(wd.damage, wd.damage2, -tsd->bonus.crit_def_rate);
// src/map/battle.cpp:5665
ATK_ADD(wd.damage, wd.damage2, 10 * pc_checkskill(sd, TK_RUN));
// src/map/battle.cpp:5669
int32 damagevalue = 0;
// src/map/battle.cpp:5673
damagevalue = sstatus->vit * sd->inventory.u.items_inventory[index].refine;
// src/map/battle.cpp:5674
ATK_ADD(wd.damage, wd.damage2, damagevalue);
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
```

### Tumbling (`TK_DODGE`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：Dodge。

- 技能树最高等级：`1`
- 前置技能：TK_JUMPKICK Lv7
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1591
clif_skill_nodamage(target, *target, LK_PARRYING, sce->val1);
// src/map/battle.cpp:1592
unit_set_attackdelay(*target, gettick(), DELAY_EVENT_PARRY);
// src/map/battle.cpp:1601
clif_skill_nodamage(target, *target, TK_DODGE, 1);
// src/map/battle.cpp:1602
sc_start4(src, target, SC_COMBO, 100, TK_JUMPKICK, src->id, 1, 0, 2000);
// src/map/battle.cpp:1606
if ((sce = sc->getSCE(SC_KAUPE)) && (skill_id != NPC_EARTHQUAKE || (skill_id == NPC_EARTHQUAKE && flag & NPC_EARTHQUAKE_FLAG)) && rnd() % 100 < sce->val2) { //Kaupe blocks damage (skill or otherwise) from players, mobs, homuns, mercenaries.
// src/map/battle.cpp:1613
status_change_end(target, SC_KAUPE);
```

### Flying Kick (`TK_JUMPKICK`)

武器/物理技能；目标：敌方目标；最高等级 7；射程：9；命中类型：Multi_Hit；段数：-3；属性：Weapon；伤害标记：NoDamage；消耗/限制：SP Lv1=70; Lv2=60; Lv3=50; Lv4=40; Lv5=30; Lv6=20; Lv7=10。

- 技能树最高等级：`7`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/jumpkick.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1591
clif_skill_nodamage(target, *target, LK_PARRYING, sce->val1);
// src/map/battle.cpp:1592
unit_set_attackdelay(*target, gettick(), DELAY_EVENT_PARRY);
// src/map/battle.cpp:1601
clif_skill_nodamage(target, *target, TK_DODGE, 1);
// src/map/battle.cpp:1602
sc_start4(src, target, SC_COMBO, 100, TK_JUMPKICK, src->id, 1, 0, 2000);
// src/map/battle.cpp:1606
if ((sce = sc->getSCE(SC_KAUPE)) && (skill_id != NPC_EARTHQUAKE || (skill_id == NPC_EARTHQUAKE && flag & NPC_EARTHQUAKE_FLAG)) && rnd() % 100 < sce->val2) { //Kaupe blocks damage (skill or otherwise) from players, mobs, homuns, mercenaries.
// src/map/battle.cpp:1613
status_change_end(target, SC_KAUPE);
// src/map/skill.cpp:5060
if (src != target && (status_bl_has_mode(target,MD_SKILLIMMUNE) || (status_get_class(target) == MOBID_EMPERIUM && !skill_get_inf2(ud->skill_id, INF2_TARGETEMPERIUM))) && skill_get_casttype(ud->skill_id) == CAST_DAMAGE) {
// src/map/skill.cpp:5062
break; // Show a skill fail message (Damage type consumes requirements)
// src/map/skill.cpp:5067
if( (src->type == BL_MER || src->type == BL_HOM) && !skill_check_condition_mercenary(src, ud->skill_id, ud->skill_lv, 1) )
// src/map/skill.cpp:5072
status_change_end(src, SC_RUN);
// src/map/skill.cpp:5079
if (!sd || sd->skillitem != ud->skill_id || skill_get_delay(ud->skill_id, ud->skill_lv))
// src/map/skill.cpp:5080
ud->canact_tick = i64max(tick + skill_delayfix(src, ud->skill_id, ud->skill_lv), ud->canact_tick - SECURITY_CASTTIME);
```

### Peaceful Break (`TK_HPTIME`)

非伤害技能；目标：被动；最高等级 10；范围：1。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:10799
status_calc_regen_rate(bl, &sd->regen, &sd->sc);
// src/map/status.cpp:5322
sregen->sp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5333
sregen->hp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5343
sregen->sp = cap_value(val, 0, SHRT_MAX);
```

### Happy Break (`TK_SPTIME`)

非伤害技能；目标：被动；最高等级 10；范围：1；持续时间1：1800000 ms；关联状态：EarthScroll。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:10799
status_calc_regen_rate(bl, &sd->regen, &sd->sc);
// src/map/status.cpp:5333
sregen->hp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5343
sregen->sp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:15626
sregen->tick.hp -= battle_config.natural_heal_skill_interval;
// src/map/status.cpp:15627
if(status_heal(bl, sregen->hp, 0, 3) < sregen->hp)
// src/map/status.cpp:15631
if(flag&RGN_SSP) { // Skill SP regen
// src/map/status.cpp:15632
sregen->tick.sp += (int32)(natural_heal_diff_tick * (sregen->rate.sp /100.));
// src/map/status.cpp:15633
while(sregen->tick.sp >= (uint32)battle_config.natural_heal_skill_interval) {
// src/map/status.cpp:15634
int32 val = sregen->sp;
// src/map/status.cpp:15638
if ((rate = pc_checkskill(sd,TK_SPTIME)))
// src/map/status.cpp:15639
sc_start(bl,bl,skill_get_sc(TK_SPTIME),
// src/map/status.cpp:15640
100,rate,skill_get_time(TK_SPTIME, rate));
```

### Kihop (`TK_POWER`)

武器/物理技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4197
if (bflag & BDMG_CRIT) { // add +crit damage bonuses here in pre-renewal mode [helvetica]
// src/map/battle.cpp:4198
if (sd->bonus.crit_atk_rate > 0) {
// src/map/battle.cpp:4199
ATK_ADDRATE(wd->damage, wd->damage2, sd->bonus.crit_atk_rate);
// src/map/battle.cpp:4204
if (sd->bonus.non_crit_atk_rate > 0) {
// src/map/battle.cpp:4205
ATK_ADDRATE(wd->damage, wd->damage2, sd->bonus.non_crit_atk_rate);
// src/map/battle.cpp:4213
ATK_ADDRATE(wd->damage, wd->damage2, 2*skill*i);
// src/map/battle.cpp:4220
ATK_ADDRATE(wd->damage, wd->damage2, dmg_bonus);
// src/map/battle.cpp:4221
RE_ALLATK_ADDRATE(wd, dmg_bonus);
// src/map/battle.cpp:4226
if (tsd != nullptr && tsd->bonus.crit_def_rate != 0 && !skill_id && (bflag & BDMG_CRIT)) {
// src/map/battle.cpp:4227
ATK_ADDRATE(wd->damage, wd->damage2, -tsd->bonus.crit_def_rate);
```

### Mild Wind (`TK_SEVENWIND`)

武器/物理技能；目标：自身；最高等级 7；命中类型：Single；段数：1；属性：Lv1=Earth; Lv2=Wind; Lv3=Water; Lv4=Fire; Lv5=Ghost; Lv6=Dark; Lv7=Holy；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-4=20; Lv5-7=50；关联状态：SevenWind。

- 技能树最高等级：`7`
- 前置技能：TK_HPTIME Lv5, TK_SPTIME Lv5, TK_POWER Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/taekwon/sevenwind.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/taekwon/sevenwind.cpp:12
void SkillSevenWind::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/taekwon/sevenwind.cpp:15
switch (skill_get_ele(getSkillId(), skill_lv)) {
```

### Taekwon Jump (`TK_HIGHJUMP`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；吟唱：Lv1=5000; Lv2=4000; Lv3=3000; Lv4=2000; Lv5=1000 ms；伤害标记：NoDamage；消耗/限制：SP 50。

- 技能树最高等级：`5`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/taekwon/highjump.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/taekwon/highjump.cpp:12
void SkillHighJump::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/taekwon/highjump.cpp:18
clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
```

### Taekwon Mission (`TK_MISSION`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：1000 ms；伤害标记：NoDamage；消耗/限制：SP 10。

- 技能树最高等级：`1`
- 前置技能：TK_POWER Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/mob.cpp`, `src/map/skill.cpp`, `src/map/skills/taekwon/mission.cpp`, `src/map/skills/taekwon/skill_factory_taekwon.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/mob.cpp:3553
sd = BL_CAST(BL_PC,battle_get_master(src));
// src/map/mob.cpp:3564
if (++(sd->mission_count) >= 100 && (temp = mob_get_random_id(MOBG_BRANCH_OF_DEAD_TREE, static_cast<e_random_monster_flags>(RMF_CHECK_MOB_LV|RMF_MOB_NOT_BOSS|RMF_MOB_NOT_SPAWN), sd->status.base_level)))
// src/map/skills/taekwon/mission.cpp:13
void SkillMission::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/taekwon/mission.cpp:14
map_session_data *sd = BL_CAST(BL_PC, src);
```
