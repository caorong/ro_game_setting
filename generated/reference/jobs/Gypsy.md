# Gypsy 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Gypsy` 公式页](../skill-formulas/Gypsy.md)

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 43 | `AC_OWL` | Owl's Eye | 10 | Archer | 否 | — | None / Passive |
| 44 | `AC_VULTURE` | Vulture's Eye | 10 | Archer | 否 | AC_OWL Lv3 | None / Passive |
| 45 | `AC_CONCENTRATION` | Improve Concentration | 10 | Archer | 否 | AC_VULTURE Lv1 | Weapon / Self |
| 46 | `AC_DOUBLE` | Double Strafe | 10 | Archer | 否 | — | Weapon / Attack |
| 47 | `AC_SHOWER` | Arrow Shower | 10 | Archer | 否 | AC_DOUBLE Lv5 | Weapon / Ground |
| 147 | `AC_MAKINGARROW` | Arrow Crafting | 1 | Archer | 否 | — | Weapon / Self |
| 148 | `AC_CHARGEARROW` | Arrow Repel | 1 | Archer | 否 | — | Weapon / Attack |
| 323 | `DC_DANCINGLESSON` | Dance Lessons | 10 | Dancer | 否 | — | Weapon / Passive |
| 324 | `DC_THROWARROW` | Slinging Arrow | 5 | Dancer | 否 | DC_DANCINGLESSON Lv3 | Weapon / Attack |
| 325 | `DC_UGLYDANCE` | Hip Shaker | 5 | Dancer | 否 | DC_DANCINGLESSON Lv1, BD_ADAPTATION Lv1 | Misc / Self |
| 326 | `DC_SCREAM` | Dazzler | 5 | Dancer | 否 | BD_ENCORE Lv1 | Misc / Self |
| 327 | `DC_HUMMING` | Focus Ballet | 10 | Dancer | 否 | DC_UGLYDANCE Lv3 | Misc / Self |
| 328 | `DC_DONTFORGETME` | Slow Grace | 10 | Dancer | 否 | DC_UGLYDANCE Lv3 | Misc / Self |
| 329 | `DC_FORTUNEKISS` | Lady Luck | 10 | Dancer | 否 | DC_UGLYDANCE Lv3 | Misc / Self |
| 330 | `DC_SERVICEFORYOU` | Gypsy's Kiss | 10 | Dancer | 否 | DC_UGLYDANCE Lv3 | Misc / Self |
| 304 | `BD_ADAPTATION` | Amp | 1 | Dancer | 否 | — | None / Self |
| 305 | `BD_ENCORE` | Encore | 1 | Dancer | 否 | BD_ADAPTATION Lv1 | None / Self |
| 306 | `BD_LULLABY` | Lullaby | 1 | Dancer | 否 | DC_HUMMING Lv10 | Misc / Self |
| 307 | `BD_RICHMANKIM` | Mental Sensing | 5 | Dancer | 否 | BD_SIEGFRIED Lv3 | Misc / Self |
| 308 | `BD_ETERNALCHAOS` | Down Tempo | 1 | Dancer | 否 | BD_ROKISWEIL Lv1 | Misc / Self |
| 309 | `BD_DRUMBATTLEFIELD` | Battle Theme | 5 | Dancer | 否 | DC_SERVICEFORYOU Lv10 | Misc / Self |
| 310 | `BD_RINGNIBELUNGEN` | Harmonic Lick | 5 | Dancer | 否 | BD_DRUMBATTLEFIELD Lv3 | Misc / Self |
| 311 | `BD_ROKISWEIL` | Classical Pluck | 1 | Dancer | 否 | DC_DONTFORGETME Lv10 | Misc / Self |
| 312 | `BD_INTOABYSS` | Power Chord | 1 | Dancer | 否 | BD_LULLABY Lv1 | Misc / Self |
| 313 | `BD_SIEGFRIED` | Acoustic Rhythm | 5 | Dancer | 否 | DC_FORTUNEKISS Lv10 | Misc / Self |
| 1011 | `DC_WINKCHARM` | Wink of Charm | 1 | Dancer | 否 | — | Misc / Attack |
| 394 | `CG_ARROWVULCAN` | Vulcan Arrow | 10 | Gypsy | 是 | AC_SHOWER Lv5, DC_THROWARROW Lv1 | Weapon / Attack |
| 395 | `CG_MOONLIT` | Sheltering Bliss | 5 | Gypsy | 是 | AC_CONCENTRATION Lv5, DC_DANCINGLESSON Lv7 | Misc / Self |
| 396 | `CG_MARIONETTE` | Marionette Control | 1 | Gypsy | 是 | AC_CONCENTRATION Lv5, DC_DANCINGLESSON Lv5 | None / Support |
| 487 | `CG_LONGINGFREEDOM` | Longing for Freedom | 5 | Gypsy | 是 | DC_DANCINGLESSON Lv10, CG_MARIONETTE Lv1 | None / Self |
| 488 | `CG_HERMODE` | Wand of Hermode | 5 | Gypsy | 是 | AC_CONCENTRATION Lv10, DC_DANCINGLESSON Lv10 | Misc / Self |
| 489 | `CG_TAROTCARD` | Tarot Card of Fate | 5 | Gypsy | 是 | AC_CONCENTRATION Lv10, DC_UGLYDANCE Lv3 | Misc / Attack |

## 技能详情

### Vulcan Arrow (`CG_ARROWVULCAN`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：-9；属性：Weapon；吟唱：Lv1=2000; Lv2=2200; Lv3=2400; Lv4=2600; Lv5=2800; Lv6=3000; Lv7=3200; Lv8=3400; Lv9=3600; Lv10=3800 ms；技能后摇：Lv1-5=2800; Lv6-10=3000 ms；移动后摇：2000 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30；弹药数 1；武器 Musical, Whip；弹药 Arrow。

- 技能树最高等级：`10`
- 前置技能：AC_SHOWER Lv5, DC_THROWARROW Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/skill_factory_archer.cpp`, `src/map/skills/archer/vulcanarrow.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/vulcanarrow.cpp:13
void SkillVulcanArrow::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
// src/map/skills/archer/vulcanarrow.cpp:15
skillratio += 400 + 100 * skill_lv;
// src/map/skills/archer/vulcanarrow.cpp:18
skillratio += 100 + 100 * skill_lv;
```

### Sheltering Bliss (`CG_MOONLIT`)

特殊技能；目标：自身；最高等级 5；段数：1；范围：3；击退：2；持续时间1：Lv1=20000; Lv2=25000; Lv3=30000; Lv4=35000; Lv5=40000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=30; Lv2=40; Lv3=50; Lv4=60; Lv5=70；武器 Musical, Whip。

- 技能树最高等级：`5`
- 前置技能：AC_CONCENTRATION Lv5, DC_DANCINGLESSON Lv7
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/longingforfreedom.cpp`, `src/map/skills/archer/shelteringbliss.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:6611
skill_blown(ss, bl, skill_get_blewcount(skill_id, sg->skill_lv), unit_getdir(bl), BLOWN_NONE);
// src/map/skill.cpp:6615
sc_start4(ss, bl, type, 100, 0, 0, sg->group_id, ss->id, sg->limit);
// src/map/skill.cpp:6626
skill_blown(ss,bl,skill_get_blewcount(sg->skill_id,sg->skill_lv),unit_getdir(bl),BLOWN_NONE);
// src/map/skill.cpp:6629
case UNT_REVERBERATION:
// src/map/skill.cpp:6631
break; //Does not affect the caster.
// src/map/skill.cpp:6633
map_foreachinrange(skill_trap_splash,unit, skill_get_splash(sg->skill_id, sg->skill_lv), sg->bl_flag, unit,tick);
// src/map/skill.cpp:8037
i = 2 * (*skill_lv);
// src/map/skill.cpp:8052
sc_start4(sd, tsd, SC_DANCING, 100, skill_id, sd->sc.getSCE(SC_DANCING)->val2, *skill_lv, sd->id, skill_get_time(skill_id, *skill_lv) + 1000);
// src/map/skill.cpp:8053
clif_skill_nodamage(tsd, *sd, skill_id, *skill_lv);
// src/map/skill.cpp:8055
tsd->skill_lv_dance = *skill_lv;
// src/map/skill.cpp:8059
sc_start(sd, sd, SC_ENSEMBLEFATIGUE, 100, 1, skill_get_time(CG_SPECIALSINGER, *skill_lv));
// src/map/skill.cpp:8568
if(!npc_check_areanpc(1,sd.m,sd.x,sd.y,skill_get_splash(skill_id, skill_lv))) {
```

### Marionette Control (`CG_MARIONETTE`)

非伤害技能；目标：友方目标；最高等级 1；射程：7；命中类型：Single；段数：1；持续时间1：1000 ms；伤害标记：NoDamage；消耗/限制：SP 100；关联状态：Marionette。

- 技能树最高等级：`1`
- 前置技能：AC_CONCENTRATION Lv5, DC_DANCINGLESSON Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/marionettecontrol.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/marionettecontrol.cpp:13
void SkillMarionetteControl::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/marionettecontrol.cpp:14
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/archer/marionettecontrol.cpp:15
map_session_data *dstsd = BL_CAST(BL_PC, target);
// src/map/skills/archer/marionettecontrol.cpp:16
status_change *sc = status_get_sc(src);
// src/map/skills/archer/marionettecontrol.cpp:17
status_change *tsc = status_get_sc(target);
// src/map/status.cpp:2170
if (skill_id && // Do not block item-casted skills.
// src/map/status.cpp:2174
( sc->cant.cast && skill_id != RK_REFRESH && skill_id != SU_GROOMING && skill_id != SR_GENTLETOUCH_CURE ) ||
// src/map/status.cpp:2176
(sc->getSCE(SC_BASILICA) && (sc->getSCE(SC_BASILICA)->val4 != src->id || skill_id != HP_BASILICA)) || // Only Basilica caster that can cast, and only Basilica to cancel it
```

### Longing for Freedom (`CG_LONGINGFREEDOM`)

非伤害技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 15；关联状态：Longing。

- 技能树最高等级：`5`
- 前置技能：DC_DANCINGLESSON Lv10, CG_MARIONETTE Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/longingforfreedom.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/longingforfreedom.cpp:14
void SkillLongingForFreedom::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/longingforfreedom.cpp:17
status_change *tsc = status_get_sc(target);
// src/map/skills/archer/longingforfreedom.cpp:18
status_change_entry *tsce = (tsc != nullptr && type != SC_NONE) ? tsc->getSCE(type) : nullptr;
// src/map/skills/archer/longingforfreedom.cpp:23
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
```

### Wand of Hermode (`CG_HERMODE`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：1；持续时间1：Lv1=10000; Lv2=15000; Lv3=20000; Lv4=25000; Lv5=30000 ms；持续时间2：Lv1=10000; Lv2=15000; Lv3=20000; Lv4=25000; Lv5=30000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=20; Lv2=30; Lv3=40; Lv4=50; Lv5=60；武器 Musical, Whip；关联状态：Hermode。

- 技能树最高等级：`5`
- 前置技能：AC_CONCENTRATION Lv10, DC_DANCINGLESSON Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/skills/archer/wandofhermode.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:4291
skill_attack(BF_MAGIC, src, src, target, skill_id, skill_lv, tick, 0);
// src/map/skill.cpp:4295
return skill_additional_effect(src, target, skill_id, skill_lv, BF_LONG | BF_SKILL | BF_MISC, ATK_DEF, tick);
// src/map/skill.cpp:4298
status_change_clear_buffs(target, SCCB_HERMODE); // Should dispell only allies.
// src/map/skill.cpp:4299
return sc_start(src, target, skill_get_sc(skill_id), 100, skill_lv, skill_get_time(skill_id, skill_lv));
// src/map/skill.cpp:4308
* @param src: Caster
// src/map/skill.cpp:4347
clif_skill_nodamage(src, *src, skill_id, skill_lv);
// src/map/skill.cpp:4349
sd->skill_lv_dance = skill_lv;
// src/map/skill.cpp:4352
skill_check_pc_partner(sd, skill_id, &skill_lv, 3, 1);
// src/map/skill.cpp:4354
return map_foreachinrange(skill_apply_songs, src, skill_get_splash(skill_id, skill_lv), splash_target(src), flag, src, skill_id, skill_lv, tick);
// src/map/skill.cpp:6198
sd->skill_lv_dance = skill_lv;
// src/map/skill.cpp:6201
sc_start4(src, src, SC_DANCING, 100, skill_id, group->group_id, skill_lv, (group->state.song_dance&2?BCT_SELF:0), limit+1000) &&
// src/map/skill.cpp:6204
skill_check_pc_partner(sd, skill_id, &skill_lv, 1, 1);
```

### Tarot Card of Fate (`CG_TAROTCARD`)

特殊技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：3000 ms；持续时间2：30000 ms；伤害标记：NoDamage, IgnoreFlee；消耗/限制：SP 40；关联状态：TarotCard。

- 技能树最高等级：`5`
- 前置技能：AC_CONCENTRATION Lv10, DC_UGLYDANCE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/skills/archer/tarotcardoffate.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:9600
void skill_consume_requirement(map_session_data *sd, uint16 skill_id, uint16 skill_lv, int16 type)
// src/map/skill.cpp:9606
require = skill_get_requirement(sd,skill_id,skill_lv);
// src/map/skill.cpp:9610
case CG_TAROTCARD: // TarotCard will consume sp in skill_cast_nodamage_id [Inkfish]
// src/map/skill.cpp:9615
require.sp = 0;
// src/map/skill.cpp:9619
require.sp *= 5;
// src/map/skills/archer/tarotcardoffate.cpp:17
int32 skill_tarotcard(block_list* src, block_list* target, uint16 skill_id, uint16 skill_lv, t_tick tick);
// src/map/skills/archer/tarotcardoffate.cpp:23
void SkillTarotCardOfFate::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/tarotcardoffate.cpp:24
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/archer/tarotcardoffate.cpp:25
mob_data *dstmd = BL_CAST(BL_MOB, target);
// src/map/skills/archer/tarotcardoffate.cpp:26
status_change *tsc = status_get_sc(target);
```
