# Priest 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Priest` 公式页](../skill-formulas/Priest.md)

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
| 9 | `MG_SRECOVERY` | Increase SP Recovery | 10 | Priest | 是 | — | None / Passive |
| 12 | `MG_SAFETYWALL` | Safety Wall | 10 | Priest | 是 | PR_ASPERSIO Lv4, PR_SANCTUARY Lv3 | Magic / Ground |
| 54 | `ALL_RESURRECTION` | Resurrection | 4 | Priest | 是 | PR_STRECOVERY Lv1, MG_SRECOVERY Lv4 | Magic / Support |
| 65 | `PR_MACEMASTERY` | Mace Mastery | 10 | Priest | 是 | — | Weapon / Passive |
| 66 | `PR_IMPOSITIO` | Impositio Manus | 5 | Priest | 是 | — | Magic / Support |
| 67 | `PR_SUFFRAGIUM` | Suffragium | 3 | Priest | 是 | PR_IMPOSITIO Lv2 | Magic / Support |
| 68 | `PR_ASPERSIO` | Aspersio | 5 | Priest | 是 | AL_HOLYWATER Lv1, PR_IMPOSITIO Lv3 | Magic / Support |
| 69 | `PR_BENEDICTIO` | B.S. Sacramenti | 5 | Priest | 是 | PR_GLORIA Lv3, PR_ASPERSIO Lv5 | Magic / Ground |
| 70 | `PR_SANCTUARY` | Sanctuary | 10 | Priest | 是 | AL_HEAL Lv1 | Magic / Ground |
| 71 | `PR_SLOWPOISON` | Slow Poison | 4 | Priest | 是 | — | Magic / Support |
| 72 | `PR_STRECOVERY` | Status Recovery | 1 | Priest | 是 | — | Magic / Support |
| 73 | `PR_KYRIE` | Kyrie Eleison | 10 | Priest | 是 | AL_ANGELUS Lv2 | Magic / Support |
| 74 | `PR_MAGNIFICAT` | Magnificat | 5 | Priest | 是 | — | Magic / Self |
| 75 | `PR_GLORIA` | Gloria | 5 | Priest | 是 | PR_KYRIE Lv4, PR_MAGNIFICAT Lv3 | Magic / Self |
| 76 | `PR_LEXDIVINA` | Lex Divina | 10 | Priest | 是 | AL_RUWACH Lv1 | Magic / Attack |
| 77 | `PR_TURNUNDEAD` | Turn Undead | 10 | Priest | 是 | ALL_RESURRECTION Lv1, PR_LEXDIVINA Lv3 | Magic / Attack |
| 78 | `PR_LEXAETERNA` | Lex Aeterna | 1 | Priest | 是 | PR_LEXDIVINA Lv5 | Magic / Attack |
| 79 | `PR_MAGNUS` | Magnus Exorcismus | 10 | Priest | 是 | MG_SAFETYWALL Lv1, PR_LEXAETERNA Lv1, PR_TURNUNDEAD Lv3 | Magic / Ground |
| 1014 | `PR_REDEMPTIO` | Redemptio | 1 | Priest | 是 | — | Magic / Self |

## 技能详情

### Increase SP Recovery (`MG_SRECOVERY`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/competentia.cpp`, `src/map/skills/merchant/aidberserkpotion.cpp`, `src/map/skills/merchant/aidcondensedpotion.cpp`, `src/map/skills/merchant/aidpotion.cpp`, `src/map/skills/other/netsupport.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:10719
if (sd->sc.getSCE(SC_INCHEALRATE))
// src/map/pc.cpp:10720
bonus += bonus * sd->sc.getSCE(SC_INCHEALRATE)->val1 / 100;
// src/map/pc.cpp:10722
tmp = hp * bonus / 100; // Overflow check
// src/map/pc.cpp:10723
if (bonus != 100 && tmp > hp)
// src/map/pc.cpp:10724
hp = tmp;
// src/map/pc.cpp:10726
if (sp) {
// src/map/pc.cpp:10733
bonus += sd->bonus.itemsphealrate2;
// src/map/pc.cpp:10735
bonus += bonus * pc_get_itemgroup_bonus( sd, itemid, sd->itemgroupsphealrate ) / 100;
// src/map/pc.cpp:10737
for( const auto &it : sd->itemsphealrate ){
// src/map/skill.cpp:7337
int32 hp, sp;
// src/map/skill.cpp:7339
switch( sg->skill_lv ) {
// src/map/skill.cpp:7340
case 1: case 2: hp = 3; sp = 2; break;
```

### Safety Wall (`MG_SAFETYWALL`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：1；属性：Ghost；吟唱：Lv1=4000; Lv2-3=3500; Lv4=2500; Lv5=2000; Lv6=1500; Lv7-10=1000 ms；持续时间1：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000; Lv6=30000; Lv7=35000; Lv8=40000; Lv9=45000; Lv10=50000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-3=30; Lv4-6=35; Lv7-10=40；道具 Blue_Gemstone×1；关联状态：Safetywall。

- 技能树最高等级：`10`
- 前置技能：PR_ASPERSIO Lv4, PR_SANCTUARY Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/mage/elementalshield.cpp`, `src/map/skills/mage/safetywall.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1436
if (damage == 0)
// src/map/battle.cpp:1453
if (group->val3 - damage > 0)
// src/map/battle.cpp:1454
group->val3 -= static_cast<int32>(cap_value(damage, INT_MIN, INT_MAX));
// src/map/skill.cpp:5777
layout = skill_get_unit_layout(skill_id,skill_lv,src,x,y);
// src/map/skill.cpp:5779
sd = BL_CAST(BL_PC, src);
// src/map/skill.cpp:5786
val2 = 4 + skill_lv;
// src/map/skill.cpp:5787
val3 = 300 * skill_lv + 65 * ( status->int_ +  status_get_lv(src) ) + status->max_sp; //nb hp
// src/map/skill.cpp:5790
val2 = skill_lv + 1;
// src/map/skill.cpp:5792
val3 = 300 * skill_lv + 65 * (status->int_ + status_get_lv(src)) + status->max_sp;
// src/map/skill.cpp:5798
val2 = 4+skill_lv;
// src/map/skill.cpp:7718
status_change_end(bl, SC_DANCING);
// src/map/skills/mage/elementalshield.cpp:14
void SkillElementalShield::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Resurrection (`ALL_RESURRECTION`)

魔法技能；目标：友方目标；最高等级 4；射程：9；命中类型：Single；段数：1；属性：Holy；吟唱：Lv1=6000; Lv2=4000; Lv3=2000 ms；技能后摇：Lv2=1000; Lv3=2000; Lv4=3000 ms；伤害标记：NoDamage；消耗/限制：SP 60；道具 Blue_Gemstone×1。

- 技能树最高等级：`4`
- 前置技能：PR_STRECOVERY Lv1, MG_SRECOVERY Lv4
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/mob.cpp`, `src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/epiclesis.cpp`, `src/map/skills/acolyte/redemptio.cpp`, `src/map/skills/acolyte/resurrection.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5891
case AL_HEAL:
// src/map/battle.cpp:5894
case AB_HIGHNESSHEAL:
// src/map/battle.cpp:5895
ad.damage = skill_calc_heal(src, target, skill_id, skill_lv, false);
// src/map/battle.cpp:5898
ad.damage = 40;
// src/map/battle.cpp:5904
i = 10 * skill_lv + sstatus->luk + sstatus->int_ + status_get_lv(src)
// src/map/battle.cpp:5905
+ 300 - 300 * tstatus->hp / tstatus->max_hp;
// src/map/battle.cpp:5907
i = 20 * skill_lv + sstatus->luk + sstatus->int_ + status_get_lv(src)
// src/map/battle.cpp:5908
+ 200 - 200 * tstatus->hp / tstatus->max_hp;
// src/map/mob.cpp:4719
ms->delay += -5000 +(skill_get_time(skill_id, ms->skill_lv) + skill_get_time2(skill_id, ms->skill_lv))/2;
// src/map/mob.cpp:4720
if (ms->delay < 5000)
// src/map/mob.cpp:4721
ms->delay = 5000; //With a minimum of 5 secs.
// src/map/mob.cpp:4725
ms->cond1 = MSC_FRIENDHPLTMAXRATE;
```

### Mace Mastery (`PR_MACEMASTERY`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2356
damage += (skill * 10);
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
// src/map/status.cpp:4520
base_status->flee += (skill*3) / 2;
// src/map/status.cpp:4522
base_status->flee += 20;
// src/map/status.cpp:4524
base_status->flee += skill * 10;
// src/map/status.cpp:4530
base_status->cri += skill * 10;
// src/map/status.cpp:4532
base_status->cri += skill * 10;
```

### Impositio Manus (`PR_IMPOSITIO`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；技能后摇：3000 ms；持续时间1：60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=13; Lv2=16; Lv3=19; Lv4=22; Lv5=25；关联状态：Impositio。

- 技能树最高等级：`5`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/impositiomanus.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/impositiomanus.cpp:15
void SkillImpositioManus::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/impositiomanus.cpp:16
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/impositiomanus.cpp:22
clif_skill_nodamage(target, *target, getSkillId(), skill_lv);
// src/map/skills/acolyte/impositiomanus.cpp:24
sc_start(src, target, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
// src/map/skills/acolyte/impositiomanus.cpp:27
party_foreachsamemap(skill_area_sub, sd, skill_get_splash(getSkillId(), skill_lv), src, getSkillId(), skill_lv, tick, flag | BCT_PARTY | 1, skill_castend_nodamage_id);
```

### Suffragium (`PR_SUFFRAGIUM`)

魔法技能；目标：友方目标；最高等级 3；射程：9；命中类型：Single；段数：1；技能后摇：2000 ms；持续时间1：Lv1=30000; Lv2=20000; Lv3=10000 ms；伤害标记：NoDamage；消耗/限制：SP 8；关联状态：Suffragium。

- 技能树最高等级：`3`
- 前置技能：PR_IMPOSITIO Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/acolyte/suffragium.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/suffragium.cpp:15
void SkillSuffragium::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/suffragium.cpp:16
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/suffragium.cpp:22
clif_skill_nodamage(target, *target, getSkillId(), skill_lv);
// src/map/skills/acolyte/suffragium.cpp:24
sc_start(src, target, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
// src/map/skills/acolyte/suffragium.cpp:27
party_foreachsamemap(skill_area_sub, sd, skill_get_splash(getSkillId(), skill_lv), src, getSkillId(), skill_lv, tick, flag | BCT_PARTY | 1, skill_castend_nodamage_id);
```

### Aspersio (`PR_ASPERSIO`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Holy；技能后摇：2000 ms；持续时间1：Lv1=60000; Lv2=90000; Lv3=120000; Lv4=150000; Lv5=180000 ms；伤害标记：NoDamage, IgnoreElement, IgnoreDefense；消耗/限制：SP Lv1=14; Lv2=18; Lv3=22; Lv4=26; Lv5=30；道具 Holy_Water×1；关联状态：Aspersio。

- 技能树最高等级：`5`
- 前置技能：AL_HOLYWATER Lv1, PR_IMPOSITIO Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/aspersio.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
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
// src/map/battle.cpp:5904
i = 10 * skill_lv + sstatus->luk + sstatus->int_ + status_get_lv(src)
// src/map/battle.cpp:5905
+ 300 - 300 * tstatus->hp / tstatus->max_hp;
// src/map/battle.cpp:5907
i = 20 * skill_lv + sstatus->luk + sstatus->int_ + status_get_lv(src)
// src/map/battle.cpp:5908
+ 200 - 200 * tstatus->hp / tstatus->max_hp;
// src/map/skill.cpp:4417
case AL_HEAL:
// src/map/skill.cpp:4420
case AB_HIGHNESSHEAL:
```

### B.S. Sacramenti (`PR_BENEDICTIO`)

魔法技能；目标：地面区域；最高等级 5；射程：9；命中类型：Single；段数：1；范围：1；持续时间1：Lv1=40000; Lv2=80000; Lv3=120000; Lv4=160000; Lv5=200000 ms；伤害标记：NoDamage, Splash, IgnoreDefense；消耗/限制：SP 20；关联状态：Benedictio。

- 技能树最高等级：`5`
- 前置技能：PR_GLORIA Lv3, PR_ASPERSIO Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/bssacramenti.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

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
// src/map/battle.cpp:5904
i = 10 * skill_lv + sstatus->luk + sstatus->int_ + status_get_lv(src)
// src/map/skill.cpp:7943
if (tsd->sc.cant.cast)
// src/map/skill.cpp:7959
&& sd->status.sp >= 10)
// src/map/skill.cpp:8025
if (cast_flag) {	//Execute the skill on the partners.
```

### Sanctuary (`PR_SANCTUARY`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Holy；击退：2；吟唱：5000 ms；持续时间1：Lv1=3900; Lv2=6900; Lv3=9900; Lv4=12900; Lv5=15900; Lv6=18900; Lv7=21900; Lv8=24900; Lv9=27900; Lv10=30900 ms；伤害标记：NoDamage, IgnoreDefense；消耗/限制：SP Lv1=15; Lv2=18; Lv3=21; Lv4=24; Lv5=27; Lv6=30; Lv7=33; Lv8=36; Lv9=39; Lv10=42；道具 Blue_Gemstone×1。

- 技能树最高等级：`10`
- 前置技能：AL_HEAL Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/sanctuary.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

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
// src/map/battle.cpp:5904
i = 10 * skill_lv + sstatus->luk + sstatus->int_ + status_get_lv(src)
// src/map/battle.cpp:5905
+ 300 - 300 * tstatus->hp / tstatus->max_hp;
// src/map/pc.cpp:9607
int32 pc_skillheal_bonus(map_session_data *sd, uint16 skill_id) {
// src/map/pc.cpp:9608
int32 bonus = sd->bonus.add_heal_rate;
```

### Slow Poison (`PR_SLOWPOISON`)

魔法技能；目标：友方目标；最高等级 4；射程：9；命中类型：Single；段数：1；持续时间1：Lv1=10000; Lv2=20000; Lv3=30000; Lv4=40000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=6; Lv2=8; Lv3=10; Lv4=12；关联状态：SlowPoison。

- 技能树最高等级：`4`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/skill_factory_acolyte.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Status Recovery (`PR_STRECOVERY`)

魔法技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；技能后摇：2000 ms；持续时间2：30000 ms；伤害标记：NoDamage；消耗/限制：SP 5；关联状态：Blind。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/acolyte/statusrecovery.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:3741
range= skill_get_splash(skl->skill_id, skl->skill_lv);
// src/map/skill.cpp:3743
skl->x+range,skl->y+range,BL_CHAR,src,skl->skill_id,skl->skill_lv,tick);
// src/map/skill.cpp:3748
sc_start(src, target, SC_SILENCE, skl->type, skl->skill_lv, skill_get_time2(status_db.getSkill(SC_SILENCE), 1));
// src/map/skill.cpp:3751
sc_start(src, target, SC_SILENCE, skl->type, skl->skill_lv, skill_get_time2(skl->skill_id, skl->skill_lv));
// src/map/skill.cpp:3754
sc_start(src, target, SC_BLIND, skl->type, skl->skill_lv, skill_get_time2(skl->skill_id, skl->skill_lv));
// src/map/skill.cpp:3757
sc_start(src, target, SC_STUN, skl->type, skl->skill_lv, skill_get_time2(skl->skill_id, skl->skill_lv));
// src/map/skill.cpp:3760
sc_start(src, target, SC_SILENCE, skl->type, skl->skill_lv, skill_get_time2(skl->skill_id, skl->skill_lv));
// src/map/skills/acolyte/statusrecovery.cpp:13
void SkillStatusRecovery::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/statusrecovery.cpp:15
status_change* tsc = status_get_sc(target);
// src/map/skills/acolyte/statusrecovery.cpp:16
mob_data* dstmd = BL_CAST(BL_MOB, target);
// src/map/skills/acolyte/statusrecovery.cpp:19
clif_skill_nodamage(src,*target,getSkillId(), skill_lv, false);
```

### Kyrie Eleison (`PR_KYRIE`)

魔法技能；目标：友方目标；最高等级 10；射程：9；命中类型：Single；段数：1；吟唱：2000 ms；技能后摇：2000 ms；持续时间1：120000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-3=20; Lv4-6=25; Lv7-9=30; Lv10=35；关联状态：Kyrie。

- 技能树最高等级：`10`
- 前置技能：AL_ANGELUS Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/kyrieeleison.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/kyrieeleison.cpp:12
void SkillKyrieEleison::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/kyrieeleison.cpp:13
clif_skill_nodamage(target,*target,getSkillId(), skill_lv,
// src/map/skills/acolyte/kyrieeleison.cpp:14
sc_start(src,target,skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
```

### Magnificat (`PR_MAGNIFICAT`)

魔法技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；吟唱：4000 ms；技能后摇：2000 ms；持续时间1：Lv1=30000; Lv2=45000; Lv3=60000; Lv4=75000; Lv5=90000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 40；关联状态：Magnificat。

- 技能树最高等级：`5`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/magnificat.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/magnificat.cpp:14
void SkillMagnificat::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/magnificat.cpp:15
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/magnificat.cpp:21
clif_skill_nodamage(target, *target, getSkillId(), skill_lv);
// src/map/skills/acolyte/magnificat.cpp:23
sc_start(src, target, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
```

### Gloria (`PR_GLORIA`)

魔法技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；技能后摇：2000 ms；持续时间1：Lv1=10000; Lv2=15000; Lv3=20000; Lv4=25000; Lv5=30000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 20；关联状态：Gloria。

- 技能树最高等级：`5`
- 前置技能：PR_KYRIE Lv4, PR_MAGNIFICAT Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/gloria.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/gloria.cpp:14
void SkillGloria::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/gloria.cpp:15
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/gloria.cpp:21
clif_skill_nodamage(target, *target, getSkillId(), skill_lv);
// src/map/skills/acolyte/gloria.cpp:23
sc_start(src, target, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
```

### Lex Divina (`PR_LEXDIVINA`)

魔法技能；目标：敌方目标；最高等级 10；射程：5；命中类型：Single；技能后摇：3000 ms；持续时间2：Lv1=30000; Lv2=35000; Lv3=40000; Lv4=45000; Lv5=50000; Lv6-10=60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-5=20; Lv6=18; Lv7=16; Lv8=14; Lv9=12; Lv10=10；关联状态：Silence。

- 技能树最高等级：`10`
- 前置技能：AL_RUWACH Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/lexdivina.cpp`, `src/map/skills/acolyte/silentium.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:3741
range= skill_get_splash(skl->skill_id, skl->skill_lv);
// src/map/skill.cpp:3743
skl->x+range,skl->y+range,BL_CHAR,src,skl->skill_id,skl->skill_lv,tick);
// src/map/skill.cpp:3748
sc_start(src, target, SC_SILENCE, skl->type, skl->skill_lv, skill_get_time2(status_db.getSkill(SC_SILENCE), 1));
// src/map/skill.cpp:3751
sc_start(src, target, SC_SILENCE, skl->type, skl->skill_lv, skill_get_time2(skl->skill_id, skl->skill_lv));
// src/map/skill.cpp:3754
sc_start(src, target, SC_BLIND, skl->type, skl->skill_lv, skill_get_time2(skl->skill_id, skl->skill_lv));
// src/map/skill.cpp:3757
sc_start(src, target, SC_STUN, skl->type, skl->skill_lv, skill_get_time2(skl->skill_id, skl->skill_lv));
// src/map/skills/acolyte/lexdivina.cpp:12
void SkillLexDivina::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/lexdivina.cpp:14
status_change* tsc = status_get_sc(target);
// src/map/skills/acolyte/lexdivina.cpp:15
status_change_entry* tsce = (tsc && type != SC_NONE) ? tsc->getSCE(type) : nullptr;
// src/map/skills/acolyte/lexdivina.cpp:18
status_change_end(target, type);
// src/map/skills/acolyte/lexdivina.cpp:20
skill_addtimerskill(src, tick+1000, target->id, 0, 0, getSkillId(), skill_lv, 100, flag);
// src/map/skills/acolyte/lexdivina.cpp:21
clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
```

### Turn Undead (`PR_TURNUNDEAD`)

魔法技能；目标：敌方目标；最高等级 10；射程：5；命中类型：Single；段数：1；属性：Holy；吟唱：1000 ms；技能后摇：3000 ms；伤害标记：IgnoreAtkCard, IgnoreDefense；消耗/限制：SP 20。

- 技能树最高等级：`10`
- 前置技能：ALL_RESURRECTION Lv1, PR_LEXDIVINA Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/mob.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/acolyte/turnundead.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:5891
case AL_HEAL:
// src/map/battle.cpp:5894
case AB_HIGHNESSHEAL:
// src/map/battle.cpp:5895
ad.damage = skill_calc_heal(src, target, skill_id, skill_lv, false);
// src/map/battle.cpp:5898
ad.damage = 40;
// src/map/battle.cpp:5904
i = 10 * skill_lv + sstatus->luk + sstatus->int_ + status_get_lv(src)
// src/map/battle.cpp:5905
+ 300 - 300 * tstatus->hp / tstatus->max_hp;
// src/map/battle.cpp:5907
i = 20 * skill_lv + sstatus->luk + sstatus->int_ + status_get_lv(src)
// src/map/battle.cpp:5908
+ 200 - 200 * tstatus->hp / tstatus->max_hp;
// src/map/battle.cpp:5913
ad.damage = tstatus->hp;
// src/map/mob.cpp:4566
* Previously, using skill_nocast with flag 16
// src/map/mob.cpp:4585
int32 mob_clone_spawn(map_session_data *sd, int16 m, int16 x, int16 y, const char *event, int32 master_id, enum e_mode mode, int32 flag, uint32 duration)
// src/map/skills/acolyte/turnundead.cpp:11
void SkillTurnUndead::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Lex Aeterna (`PR_LEXAETERNA`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；技能后摇：3000 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 10；关联状态：Aeterna。

- 技能树最高等级：`1`
- 前置技能：PR_LEXDIVINA Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/skills/npc/lexaeterna2.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/npc/lexaeterna2.cpp:11
void SkillLexAeterna2::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/npc/lexaeterna2.cpp:12
int32 i = skill_get_splash(getSkillId(), skill_lv);
// src/map/skills/npc/lexaeterna2.cpp:13
map_foreachinallarea(skill_area_sub, src->m, x-i, y-i, x+i, y+i, BL_CHAR, src, PR_LEXAETERNA, 1, tick, flag|BCT_ENEMY|1, skill_castend_nodamage_id);
```

### Magnus Exorcismus (`PR_MAGNUS`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Holy；吟唱：15000 ms；技能后摇：4000 ms；持续时间1：Lv1=5000; Lv2=6000; Lv3=7000; Lv4=8000; Lv5=9000; Lv6=10000; Lv7=11000; Lv8=12000; Lv9=13000; Lv10=14000 ms；消耗/限制：SP Lv1=40; Lv2=42; Lv3=44; Lv4=46; Lv5=48; Lv6=50; Lv7=52; Lv8=54; Lv9=56; Lv10=58；道具 Blue_Gemstone×1。

- 技能树最高等级：`10`
- 前置技能：MG_SAFETYWALL Lv1, PR_LEXAETERNA Lv1, PR_TURNUNDEAD Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/mob.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/magnusexorcismus.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:7523
clif_status_change(src, EFST_POSTDELAY, 1, autospell_tick, 0, 0, 0);
// src/map/battle.cpp:7537
if( (type = skill_get_casttype(r_skill)) == CAST_GROUND ) {
// src/map/battle.cpp:7541
if( !(BL_PC&battle_config.skill_reiteration) && skill->unit_flag[UF_NOREITERATION] )
// src/map/mob.cpp:4566
* Previously, using skill_nocast with flag 16
// src/map/mob.cpp:4585
int32 mob_clone_spawn(map_session_data *sd, int16 m, int16 x, int16 y, const char *event, int32 master_id, enum e_mode mode, int32 flag, uint32 duration)
// src/map/skills/acolyte/magnusexorcismus.cpp:11
void SkillMagnusExorcismus::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/magnusexorcismus.cpp:15
skill_unitsetting(src, getSkillId(), skill_lv, x, y, 0);
// src/map/skills/acolyte/magnusexorcismus.cpp:18
void SkillMagnusExorcismus::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
```

### Redemptio (`PR_REDEMPTIO`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；属性：Holy；范围：14；吟唱：4000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 400。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/redemptio.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:4391
dstsd = BL_CAST(BL_PC, bl);
// src/map/skill.cpp:4392
dstmd = BL_CAST(BL_MOB, bl);
// src/map/skill.cpp:4400
switch( skill_id ) { // Skills that may be cast on dead targets
// src/map/skills/acolyte/redemptio.cpp:18
void SkillRedemptio::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/redemptio.cpp:19
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/redemptio.cpp:20
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/acolyte/redemptio.cpp:21
status_change* tsc = status_get_sc(target);
```
