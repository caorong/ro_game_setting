# High_Priest 技能

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
| 9 | `MG_SRECOVERY` | Increase SP Recovery | 10 | Priest | 否 | — | None / Passive |
| 12 | `MG_SAFETYWALL` | Safety Wall | 10 | Priest | 否 | PR_ASPERSIO Lv4, PR_SANCTUARY Lv3 | Magic / Ground |
| 54 | `ALL_RESURRECTION` | Resurrection | 4 | Priest | 否 | PR_STRECOVERY Lv1, MG_SRECOVERY Lv4 | Magic / Support |
| 65 | `PR_MACEMASTERY` | Mace Mastery | 10 | Priest | 否 | — | Weapon / Passive |
| 66 | `PR_IMPOSITIO` | Impositio Manus | 5 | Priest | 否 | — | Magic / Support |
| 67 | `PR_SUFFRAGIUM` | Suffragium | 3 | Priest | 否 | PR_IMPOSITIO Lv2 | Magic / Support |
| 68 | `PR_ASPERSIO` | Aspersio | 5 | Priest | 否 | AL_HOLYWATER Lv1, PR_IMPOSITIO Lv3 | Magic / Support |
| 69 | `PR_BENEDICTIO` | B.S. Sacramenti | 5 | Priest | 否 | PR_GLORIA Lv3, PR_ASPERSIO Lv5 | Magic / Ground |
| 70 | `PR_SANCTUARY` | Sanctuary | 10 | Priest | 否 | AL_HEAL Lv1 | Magic / Ground |
| 71 | `PR_SLOWPOISON` | Slow Poison | 4 | High_Priest | 是 | PR_STRECOVERY Lv1 | Magic / Support |
| 72 | `PR_STRECOVERY` | Status Recovery | 1 | Priest | 否 | — | Magic / Support |
| 73 | `PR_KYRIE` | Kyrie Eleison | 10 | Priest | 否 | AL_ANGELUS Lv2 | Magic / Support |
| 74 | `PR_MAGNIFICAT` | Magnificat | 5 | Priest | 否 | — | Magic / Self |
| 75 | `PR_GLORIA` | Gloria | 5 | Priest | 否 | PR_KYRIE Lv4, PR_MAGNIFICAT Lv3 | Magic / Self |
| 76 | `PR_LEXDIVINA` | Lex Divina | 10 | Priest | 否 | AL_RUWACH Lv1 | Magic / Attack |
| 77 | `PR_TURNUNDEAD` | Turn Undead | 10 | Priest | 否 | ALL_RESURRECTION Lv1, PR_LEXDIVINA Lv3 | Magic / Attack |
| 78 | `PR_LEXAETERNA` | Lex Aeterna | 1 | Priest | 否 | PR_LEXDIVINA Lv5 | Magic / Attack |
| 79 | `PR_MAGNUS` | Magnus Exorcismus | 10 | Priest | 否 | MG_SAFETYWALL Lv1, PR_LEXAETERNA Lv1, PR_TURNUNDEAD Lv3 | Magic / Ground |
| 1014 | `PR_REDEMPTIO` | Redemptio | 1 | Priest | 否 | — | Magic / Self |
| 361 | `HP_ASSUMPTIO` | Assumptio | 5 | High_Priest | 是 | AL_ANGELUS Lv1, MG_SRECOVERY Lv3, PR_IMPOSITIO Lv3 | Magic / Support |
| 362 | `HP_BASILICA` | Basilica | 5 | High_Priest | 是 | PR_GLORIA Lv2, MG_SRECOVERY Lv1, PR_KYRIE Lv3 | Magic / Self |
| 363 | `HP_MEDITATIO` | Meditatio | 10 | High_Priest | 是 | PR_ASPERSIO Lv3, MG_SRECOVERY Lv5, PR_LEXDIVINA Lv5 | Magic / Passive |
| 481 | `HP_MANARECHARGE` | Mana Recharge | 5 | High_Priest | 是 | PR_MACEMASTERY Lv10, AL_DEMONBANE Lv10 | None / Passive |

## 技能详情

### Slow Poison (`PR_SLOWPOISON`)

魔法技能；目标：友方目标；最高等级 4；射程：9；命中类型：Single；段数：1；持续时间1：Lv1=10000; Lv2=20000; Lv3=30000; Lv4=40000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=6; Lv2=8; Lv3=10; Lv4=12；关联状态：SlowPoison。

- 技能树最高等级：`4`
- 前置技能：PR_STRECOVERY Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/skill_factory_acolyte.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Assumptio (`HP_ASSUMPTIO`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；范围：1；吟唱：Lv1=1000; Lv2=1500; Lv3=2000; Lv4=2500; Lv5=3000 ms；技能后摇：Lv1=1100; Lv2=1200; Lv3=1300; Lv4=1400; Lv5=1500 ms；持续时间1：Lv1=20000; Lv2=40000; Lv3=60000; Lv4=80000; Lv5=100000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=20; Lv2=30; Lv3=40; Lv4=50; Lv5=60；关联状态：Assumptio。

- 技能树最高等级：`5`
- 前置技能：AL_ANGELUS Lv1, MG_SRECOVERY Lv3, PR_IMPOSITIO Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/acolyte/assumptio.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/acolyte/assumptio.cpp:13
void SkillAssumptio::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/acolyte/assumptio.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/acolyte/assumptio.cpp:15
mob_data* dstmd = BL_CAST(BL_MOB, target);
// src/map/skills/acolyte/assumptio.cpp:20
StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
// src/map/skills/acolyte/skill_factory_acolyte.cpp:220
case CD_REPARATIO:
// src/map/skills/acolyte/skill_factory_acolyte.cpp:221
return std::make_unique<SkillReparatio>();
```

### Basilica (`HP_BASILICA`)

魔法技能；目标：自身；最高等级 5；射程：4；命中类型：Single；段数：1；击退：2；吟唱：Lv1=5000; Lv2=6000; Lv3=7000; Lv4=8000; Lv5=9000 ms；技能后摇：Lv1=2000; Lv2=3000; Lv3=4000; Lv4=5000; Lv5=6000 ms；持续时间1：Lv1=20000; Lv2=25000; Lv3=30000; Lv4=35000; Lv5=40000 ms；持续时间2：Lv1=20000; Lv2=25000; Lv3=30000; Lv4=35000; Lv5=40000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=80; Lv2=90; Lv3=100; Lv4=110; Lv5=120；道具 Yellow_Gemstone×1, Red_Gemstone×1, Blue_Gemstone×1, Holy_Water×1；关联状态：Basilica。

- 技能树最高等级：`5`
- 前置技能：PR_GLORIA Lv2, MG_SRECOVERY Lv1, PR_KYRIE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/acolyte/basilica.cpp`, `src/map/skills/acolyte/skill_factory_acolyte.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:3408
case NPC_REVERBERATION:
// src/map/skill.cpp:3456
if( skill_id == AM_DEMONSTRATION && bl->type == BL_MOB && ((TBL_MOB*)bl)->mob_id == MOBID_EMPERIUM )
// src/map/skill.cpp:3457
return 0; //Allow casting Bomb/Demonstration Right under emperium [Skotlex]
// src/map/skill.cpp:3462
* Used to check range condition of the casted skill. Used if the skill has UF_NOFOOTSET or INF2_DISABLENEARNPC
// src/map/skill.cpp:3463
* @param bl Object that casted skill
// src/map/skill.cpp:5817
val1 = src->id; // Store caster id.
// src/map/skill.cpp:5823
val1=skill_lv+3;
// src/map/skill.cpp:8603
int32 s,range = skill_get_unit_layout_type(skill_id,skill_lv)+1;
// src/map/skill.cpp:10424
time = 0; // There is no Delay on Basilica creation, only on cancel
// src/map/skill.cpp:10428
if (battle_config.delay_dependon_dex && !(delaynodex&1)) { // if skill delay is allowed to be reduced by dex
// src/map/skill.cpp:10429
int32 scale = battle_config.castrate_dex_scale - status_get_dex(bl);
// src/map/skill.cpp:10432
time = time * scale / battle_config.castrate_dex_scale;
```

### Meditatio (`HP_MEDITATIO`)

魔法技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：PR_ASPERSIO Lv3, MG_SRECOVERY Lv5, PR_LEXDIVINA Lv5
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:540
hp = (skill_lv > 6) ? 777 : skill_lv * 100;
// src/map/skill.cpp:543
hp = (skill_lv > 6) ? 666 : skill_lv * 100;
// src/map/skill.cpp:545
case AB_HIGHNESSHEAL:
// src/map/skill.cpp:547
hp = ((status_get_int(src) + status_get_lv(src)) / 5) * 30;
// src/map/skill.cpp:552
hp = ((status_get_lv(src) + status_get_int(src)) / 8) * (4 + ((sd ? pc_checkskill(sd, AL_HEAL) : 1) * 8));
// src/map/skill.cpp:553
hp = (hp * (17 + 3 * skill_lv)) / 10;
// src/map/skill.cpp:557
hp = (status_get_lv(src) + status_get_int(src)) / 5 * 6;
// src/map/skill.cpp:560
hp = (status_get_lv(src) + status_get_int(src)) / 5 * 15;
// src/map/skill.cpp:562
case CD_MEDIALE_VOTUM:// Does the learned level of heal affect this skill?
// src/map/skill.cpp:563
case CD_DILECTIO_HEAL:// Same question for this one too. [Rytech]
// src/map/skill.cpp:565
hp = (status_get_lv(src) + status_get_int(src)) / 5 * 30;
// src/map/skill.cpp:573
hp = (500 + pc_checkskill(sd,SOA_TALISMAN_MASTERY) * 50) * skill_lv * status_get_lv(src) / 100;
```

### Mana Recharge (`HP_MANARECHARGE`)

非伤害技能；目标：被动；最高等级 5。

- 技能树最高等级：`5`
- 前置技能：PR_MACEMASTERY Lv10, AL_DEMONBANE Lv10
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:4660
sd->dsprate -= 4*skill;
// src/map/status.cpp:4663
sd->dsprate -= sc->getSCE(SC_SERVICE4U)->val3;
// src/map/status.cpp:4666
if(sd->dsprate < 0)
// src/map/status.cpp:4667
sd->dsprate = 0;
// src/map/status.cpp:4668
if(sd->castrate < 0)
// src/map/status.cpp:4669
sd->castrate = 0;
// src/map/status.cpp:4670
if(sd->hprecov_rate < 0)
// src/map/status.cpp:4671
sd->hprecov_rate = 0;
```
