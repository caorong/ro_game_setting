# Bard 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

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
| 315 | `BA_MUSICALLESSON` | Music Lessons | 10 | Bard | 是 | — | Weapon / Passive |
| 316 | `BA_MUSICALSTRIKE` | Melody Strike | 5 | Bard | 是 | BA_MUSICALLESSON Lv3 | Weapon / Attack |
| 317 | `BA_DISSONANCE` | Unchained Serenade | 5 | Bard | 是 | BA_MUSICALLESSON Lv1, BD_ADAPTATION Lv1 | Misc / Self |
| 318 | `BA_FROSTJOKER` | Unbarring Octave | 5 | Bard | 是 | BD_ENCORE Lv1 | Misc / Self |
| 319 | `BA_WHISTLE` | Perfect Tablature | 10 | Bard | 是 | BA_DISSONANCE Lv3 | Misc / Self |
| 320 | `BA_ASSASSINCROSS` | Impressive Riff | 10 | Bard | 是 | BA_DISSONANCE Lv3 | Misc / Self |
| 321 | `BA_POEMBRAGI` | Magic Strings | 10 | Bard | 是 | BA_DISSONANCE Lv3 | Misc / Self |
| 322 | `BA_APPLEIDUN` | Song of Lutie | 10 | Bard | 是 | BA_DISSONANCE Lv3 | Misc / Self |
| 304 | `BD_ADAPTATION` | Amp | 1 | Bard | 是 | — | None / Self |
| 305 | `BD_ENCORE` | Encore | 1 | Bard | 是 | BD_ADAPTATION Lv1 | None / Self |
| 306 | `BD_LULLABY` | Lullaby | 1 | Bard | 是 | BA_WHISTLE Lv10 | Misc / Self |
| 307 | `BD_RICHMANKIM` | Mental Sensing | 5 | Bard | 是 | BD_SIEGFRIED Lv3 | Misc / Self |
| 308 | `BD_ETERNALCHAOS` | Down Tempo | 1 | Bard | 是 | BD_ROKISWEIL Lv1 | Misc / Self |
| 309 | `BD_DRUMBATTLEFIELD` | Battle Theme | 5 | Bard | 是 | BA_APPLEIDUN Lv10 | Misc / Self |
| 310 | `BD_RINGNIBELUNGEN` | Harmonic Lick | 5 | Bard | 是 | BD_DRUMBATTLEFIELD Lv3 | Misc / Self |
| 311 | `BD_ROKISWEIL` | Classical Pluck | 1 | Bard | 是 | BA_ASSASSINCROSS Lv10 | Misc / Self |
| 312 | `BD_INTOABYSS` | Power Chord | 1 | Bard | 是 | BD_LULLABY Lv1 | Misc / Self |
| 313 | `BD_SIEGFRIED` | Acoustic Rhythm | 5 | Bard | 是 | BA_POEMBRAGI Lv10 | Misc / Self |
| 1010 | `BA_PANGVOICE` | Pang Voice | 1 | Bard | 是 | — | Misc / Attack |

## 技能详情

### Music Lessons (`BA_MUSICALLESSON`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
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
// src/map/battle.cpp:2391
damage += (skill * 3);
// src/map/battle.cpp:6391
DAMAGE_DIV_FIX2(md.damage, skill_get_num(HT_BLITZBEAT, 5));
// src/map/battle.cpp:6393
md.damage = md.damage * (150 + 70 * skill_lv) / 100;
// src/map/battle.cpp:6399
md.damage = 30 + 10 * skill_lv;
// src/map/battle.cpp:6400
md.damage += skill_lv * pc_checkskill(sd, BA_MUSICALLESSON);
// src/map/battle.cpp:6404
md.damage = sstatus->hp;
// src/map/battle.cpp:6407
md.damage = 3;
```

### Melody Strike (`BA_MUSICALSTRIKE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Weapon；吟唱：1500 ms；消耗/限制：SP Lv1=1; Lv2=3; Lv3=5; Lv4=7; Lv5=9；弹药数 1；武器 Musical；弹药 Arrow。

- 技能树最高等级：`5`
- 前置技能：BA_MUSICALLESSON Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/melodystrike.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/melodystrike.cpp:11
void SkillMelodyStrike::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/archer/melodystrike.cpp:13
base_skillratio += 10 + 40 * skill_lv;
// src/map/skills/archer/melodystrike.cpp:15
base_skillratio += -40 + 40 * skill_lv;
```

### Unchained Serenade (`BA_DISSONANCE`)

特殊技能；目标：自身；最高等级 5；命中类型：Multi_Hit；段数：1；持续时间1：30000 ms；持续时间2：3000 ms；伤害标记：NoDamage, IgnoreFlee；消耗/限制：SP Lv1=18; Lv2=21; Lv3=24; Lv4=27; Lv5=30；武器 Musical。

- 技能树最高等级：`5`
- 前置技能：BA_MUSICALLESSON Lv1, BD_ADAPTATION Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/skills/archer/unchainedserenade.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6386
if(mflag > 1) //Autocasted Blitz
// src/map/battle.cpp:6391
DAMAGE_DIV_FIX2(md.damage, skill_get_num(HT_BLITZBEAT, 5));
// src/map/battle.cpp:6393
md.damage = md.damage * (150 + 70 * skill_lv) / 100;
// src/map/battle.cpp:6399
md.damage = 30 + 10 * skill_lv;
// src/map/battle.cpp:6400
md.damage += skill_lv * pc_checkskill(sd, BA_MUSICALLESSON);
// src/map/battle.cpp:6404
md.damage = sstatus->hp;
// src/map/battle.cpp:6407
md.damage = 3;
// src/map/battle.cpp:6410
md.damage = skill_calc_heal(src,target,skill_id,skill_lv,false);
// src/map/skill.cpp:4283
uint16 skill_id = static_cast<uint16>(va_arg(ap, int32));
// src/map/skill.cpp:4284
uint16 skill_lv = static_cast<uint16>(va_arg(ap, int32));
// src/map/skill.cpp:4291
skill_attack(BF_MAGIC, src, src, target, skill_id, skill_lv, tick, 0);
// src/map/skill.cpp:4295
return skill_additional_effect(src, target, skill_id, skill_lv, BF_LONG | BF_SKILL | BF_MISC, ATK_DEF, tick);
```

### Unbarring Octave (`BA_FROSTJOKER`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；技能后摇：4000 ms；持续时间1：15000 ms；持续时间2：12000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20；关联状态：Freeze。

- 技能树最高等级：`5`
- 前置技能：BD_ENCORE Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/dazzler.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/skills/archer/unbarringoctave.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:3729
clif_skill_nodamage(src,*target,skl->skill_id,skl->skill_lv);
// src/map/skill.cpp:3741
range= skill_get_splash(skl->skill_id, skl->skill_lv);
// src/map/skill.cpp:3743
skl->x+range,skl->y+range,BL_CHAR,src,skl->skill_id,skl->skill_lv,tick);
// src/map/skill.cpp:3748
sc_start(src, target, SC_SILENCE, skl->type, skl->skill_lv, skill_get_time2(status_db.getSkill(SC_SILENCE), 1));
// src/map/skill.cpp:3751
sc_start(src, target, SC_SILENCE, skl->type, skl->skill_lv, skill_get_time2(skl->skill_id, skl->skill_lv));
// src/map/skills/archer/dazzler.cpp:14
void SkillDazzler::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/archer/dazzler.cpp:15
int32 rate = 150 + 50 * skill_lv + 100; // Aegis accuracy (1000 = 100%). DC_SCREAM has a 10% higher base chance than BA_FROSTJOKER
// src/map/skills/archer/dazzler.cpp:16
int32 duration = skill_get_time2(getSkillId(), skill_lv);
// src/map/skills/archer/dazzler.cpp:21
rate /= 4;
// src/map/skills/archer/dazzler.cpp:22
duration = skill_get_time(getSkillId(), skill_lv);
// src/map/skills/archer/dazzler.cpp:24
status_change_start(src, target, skill_get_sc(getSkillId()), rate*10, skill_lv, 0, 0, 0, duration, SCSTART_NONE);
// src/map/skills/archer/dazzler.cpp:27
void SkillDazzler::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Perfect Tablature (`BA_WHISTLE`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=24; Lv2=28; Lv3=32; Lv4=36; Lv5=40; Lv6=44; Lv7=48; Lv8=52; Lv9=56; Lv10=60；武器 Musical, Whip；关联状态：Whistle。

- 技能树最高等级：`10`
- 前置技能：BA_DISSONANCE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/perfecttablature.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5903
limit = skill_get_time(skill_id,skill_lv);
// src/map/skill.cpp:5911
val1 = skill_lv + status->agi / 10; // Flee increase
// src/map/skill.cpp:5912
val2 = (skill_lv + 1) / 2 + status->luk / 30; // Perfect dodge increase
// src/map/skill.cpp:5919
val1 = 1 + 2 * skill_lv + status->dex / 10; // Hit increase
// src/map/skill.cpp:7754
status_change_end(bl, type);
// src/map/skill.cpp:7766
delete_timer(sce->timer, status_change_timer);
// src/map/skill.cpp:7769
t_tick duration = skill_get_time2(skill_id, 1);
// src/map/skill.cpp:11969
skill_usave_add(((TBL_PC*)src), group->skill_id, group->skill_lv);
// src/map/skills/archer/perfecttablature.cpp:11
void SkillPerfectTablature::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/perfecttablature.cpp:13
skill_castend_song(src, getSkillId(), skill_lv, tick);
// src/map/skills/archer/perfecttablature.cpp:17
void SkillPerfectTablature::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/perfecttablature.cpp:20
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Impressive Riff (`BA_ASSASSINCROSS`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：120000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=38; Lv2=41; Lv3=44; Lv4=47; Lv5=50; Lv6=53; Lv7=56; Lv8=59; Lv9=62; Lv10=65；武器 Musical, Whip；关联状态：AssnCros。

- 技能树最高等级：`10`
- 前置技能：BA_DISSONANCE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/impressiveriff.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5948
val1 *= 10; //Because 10 is actually 1% aspd
// src/map/skill.cpp:5951
val1 = 15 + skill_lv + (status->int_ / 10); // MaxSP percent increase
// src/map/skill.cpp:5952
val2 = 20 + 3 * skill_lv + (status->int_ / 10); // SP cost reduction
// src/map/skill.cpp:5961
val1 += 5 + skill_lv + (status->agi / 20);
// src/map/skill.cpp:5962
val1 *= 10; // ASPD works with 1000 as 100%
// src/map/skill.cpp:5965
val1 = 10 + skill_lv + (status->luk / 10); // Critical increase
// src/map/skill.cpp:5966
val1 *= 10; //Because every 10 crit is an actual cri point.
// src/map/skill.cpp:7754
status_change_end(bl, type);
// src/map/skill.cpp:7766
delete_timer(sce->timer, status_change_timer);
// src/map/skill.cpp:7769
t_tick duration = skill_get_time2(skill_id, 1);
// src/map/skill.cpp:7770
sce->val4 = 1; //Store the fact that this is a "reduced" duration effect.
// src/map/skill.cpp:11969
skill_usave_add(((TBL_PC*)src), group->skill_id, group->skill_lv);
```

### Magic Strings (`BA_POEMBRAGI`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：180000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=40; Lv2=45; Lv3=50; Lv4=55; Lv5=60; Lv6=65; Lv7=70; Lv8=75; Lv9=80; Lv10=85；武器 Musical, Whip；关联状态：PoemBragi。

- 技能树最高等级：`10`
- 前置技能：BA_DISSONANCE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/magicstrings.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5911
val1 = skill_lv + status->agi / 10; // Flee increase
// src/map/skill.cpp:5912
val2 = (skill_lv + 1) / 2 + status->luk / 30; // Perfect dodge increase
// src/map/skill.cpp:5919
val1 = 1 + 2 * skill_lv + status->dex / 10; // Hit increase
// src/map/skill.cpp:5924
val1 = 3 * skill_lv + status->dex / 10; // Casting time reduction
// src/map/skill.cpp:5926
val2 = (skill_lv < 10 ? 3 * skill_lv : 50) + status->int_ / 5; // After-cast delay reduction
// src/map/skill.cpp:5934
val1 = 3 * skill_lv + status->dex / 15; // ASPD decrease
// src/map/skill.cpp:5935
val2 = 2 * skill_lv + status->agi / 20; // Movement speed adjustment.
// src/map/skill.cpp:7754
status_change_end(bl, type);
// src/map/skill.cpp:7766
delete_timer(sce->timer, status_change_timer);
// src/map/skill.cpp:11969
skill_usave_add(((TBL_PC*)src), group->skill_id, group->skill_lv);
// src/map/skills/archer/magicstrings.cpp:11
void SkillMagicStrings::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/magicstrings.cpp:13
skill_castend_song(src, getSkillId(), skill_lv, tick);
```

### Song of Lutie (`BA_APPLEIDUN`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：180000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=40; Lv2=45; Lv3=50; Lv4=55; Lv5=60; Lv6=65; Lv7=70; Lv8=75; Lv9=80; Lv10=85；武器 Musical, Whip；关联状态：AppleIdun。

- 技能树最高等级：`10`
- 前置技能：BA_DISSONANCE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/skills/archer/songoflutie.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:9608
int32 bonus = sd->bonus.add_heal_rate;
// src/map/pc.cpp:9616
case AL_HEAL:           if( !(battle_config.skill_add_heal_rate&1) ) bonus = 0; break;
// src/map/pc.cpp:9617
case PR_SANCTUARY:      if( !(battle_config.skill_add_heal_rate&2) ) bonus = 0; break;
// src/map/pc.cpp:9618
case AM_POTIONPITCHER:  if( !(battle_config.skill_add_heal_rate&4) ) bonus = 0; break;
// src/map/pc.cpp:9619
case CR_SLIMPITCHER:    if( !(battle_config.skill_add_heal_rate&8) ) bonus = 0; break;
// src/map/pc.cpp:9620
case BA_APPLEIDUN:      if( !(battle_config.skill_add_heal_rate&16)) bonus = 0; break;
// src/map/pc.cpp:9621
case AB_CHEAL:          if (!(battle_config.skill_add_heal_rate & 32)) bonus = 0; break;
// src/map/pc.cpp:9622
case AB_HIGHNESSHEAL:   if (!(battle_config.skill_add_heal_rate & 64)) bonus = 0; break;
// src/map/pc.cpp:9623
case CD_MEDIALE_VOTUM:  if (!(battle_config.skill_add_heal_rate & 128)) bonus = 0; break;
// src/map/pc.cpp:9624
case CD_DILECTIO_HEAL:  if (!(battle_config.skill_add_heal_rate & 256)) bonus = 0; break;
// src/map/pc.cpp:9628
for (auto &it : sd->skillheal) {
// src/map/skill.cpp:524
map_session_data *sd = BL_CAST(BL_PC, src);
```

### Amp (`BD_ADAPTATION`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间2：5000 ms；伤害标记：NoDamage；消耗/限制：SP 1。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/amp.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5169
status_change_end(src, SC_CAMOUFLAGE); // Applies to the first skill if active
// src/map/skill.cpp:5188
ud->skill_lv = ud->skilltarget = 0;
// src/map/skill.cpp:8524
status_change_end(&sd, SC_COMBO);
// src/map/skill.cpp:8541
if (skill_get_time(
// src/map/skill.cpp:8544
- time < skill_get_time2(skill_id,skill_lv))
// src/map/skill.cpp:9606
require = skill_get_requirement(sd,skill_id,skill_lv);
// src/map/skill.cpp:9610
case CG_TAROTCARD: // TarotCard will consume sp in skill_cast_nodamage_id [Inkfish]
// src/map/skill.cpp:9615
require.sp = 0;
// src/map/skill.cpp:9619
require.sp *= 5;
// src/map/skills/archer/amp.cpp:14
void SkillAmp::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/amp.cpp:16
StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
// src/map/skills/archer/amp.cpp:18
status_change *tsc = status_get_sc(target);
```

### Encore (`BD_ENCORE`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；武器 Musical, Whip；关联状态：Dancing。

- 技能树最高等级：`1`
- 前置技能：BD_ADAPTATION Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/encore.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:9606
require = skill_get_requirement(sd,skill_id,skill_lv);
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
// src/map/skill.cpp:9634
skill_consume_hpspap(sd, skill_id, require.hp, require.sp, require.ap);
// src/map/skill.cpp:9770
req.hp = skill->require.hp[skill_lv - 1];
// src/map/skill.cpp:9771
hp_rate = skill->require.hp_rate[skill_lv - 1];
// src/map/skill.cpp:9772
if(hp_rate > 0)
// src/map/skill.cpp:9773
req.hp += (status->hp * hp_rate)/100;
```

### Lullaby (`BD_LULLABY`)

特殊技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：30000 ms；伤害标记：NoDamage；消耗/限制：SP 20；武器 Musical, Whip；关联状态：Sleep。

- 技能树最高等级：`1`
- 前置技能：BA_WHISTLE Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/lullaby.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:4283
uint16 skill_id = static_cast<uint16>(va_arg(ap, int32));
// src/map/skill.cpp:4284
uint16 skill_lv = static_cast<uint16>(va_arg(ap, int32));
// src/map/skill.cpp:4291
skill_attack(BF_MAGIC, src, src, target, skill_id, skill_lv, tick, 0);
// src/map/skill.cpp:4295
return skill_additional_effect(src, target, skill_id, skill_lv, BF_LONG | BF_SKILL | BF_MISC, ATK_DEF, tick);
// src/map/skill.cpp:4298
status_change_clear_buffs(target, SCCB_HERMODE); // Should dispell only allies.
// src/map/skill.cpp:4299
return sc_start(src, target, skill_get_sc(skill_id), 100, skill_lv, skill_get_time(skill_id, skill_lv));
// src/map/skill.cpp:4324
ShowWarning("skill_castend_song: Unknown song skill ID: %u\n", skill_id);
// src/map/skill.cpp:4328
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skill.cpp:4347
clif_skill_nodamage(src, *src, skill_id, skill_lv);
// src/map/skill.cpp:7700
status_change_end(bl, type);
// src/map/skill.cpp:7718
status_change_end(bl, SC_DANCING);
// src/map/skills/archer/lullaby.cpp:13
void SkillLullaby::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
```

### Mental Sensing (`BD_RICHMANKIM`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP 20；武器 Musical, Whip；关联状态：RichManKim。

- 技能树最高等级：`5`
- 前置技能：BD_SIEGFRIED Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/mentalsensing.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5965
val1 = 10 + skill_lv + (status->luk / 10); // Critical increase
// src/map/skill.cpp:5966
val1 *= 10; //Because every 10 crit is an actual cri point.
// src/map/skill.cpp:5971
val1 = (skill_lv+1)*25;	//Atk increase
// src/map/skill.cpp:5972
val2 = (skill_lv+1)*2;	//Def increase
// src/map/skill.cpp:5975
val1 = (skill_lv+2)*25;	//Atk increase
// src/map/skill.cpp:5978
val1 = 25 + 11*skill_lv; //Exp increase bonus.
// src/map/skill.cpp:5981
val1 = 55 + skill_lv*5;	//Elemental Resistance
// src/map/skill.cpp:5982
val2 = skill_lv*10;	//Status ailment resistance
// src/map/skill.cpp:7700
status_change_end(bl, type);
// src/map/skills/archer/mentalsensing.cpp:11
void SkillMentalSensing::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/mentalsensing.cpp:13
skill_castend_song(src, getSkillId(), skill_lv, tick);
// src/map/skills/archer/mentalsensing.cpp:17
void SkillMentalSensing::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Down Tempo (`BD_ETERNALCHAOS`)

特殊技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP 30；武器 Musical, Whip；关联状态：EternalChaos。

- 技能树最高等级：`1`
- 前置技能：BD_ROKISWEIL Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/downtempo.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:4324
ShowWarning("skill_castend_song: Unknown song skill ID: %u\n", skill_id);
// src/map/skill.cpp:4328
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skill.cpp:4347
clif_skill_nodamage(src, *src, skill_id, skill_lv);
// src/map/skill.cpp:7700
status_change_end(bl, type);
// src/map/skills/archer/downtempo.cpp:11
void SkillDownTempo::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/downtempo.cpp:13
skill_castend_song(src, getSkillId(), skill_lv, tick);
// src/map/skills/archer/downtempo.cpp:17
void SkillDownTempo::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/downtempo.cpp:20
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Battle Theme (`BD_DRUMBATTLEFIELD`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=40; Lv2=45; Lv3=50; Lv4=55; Lv5=60；武器 Musical, Whip；关联状态：DrumBattle。

- 技能树最高等级：`5`
- 前置技能：BA_APPLEIDUN Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/battletheme.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5961
val1 += 5 + skill_lv + (status->agi / 20);
// src/map/skill.cpp:5962
val1 *= 10; // ASPD works with 1000 as 100%
// src/map/skill.cpp:5965
val1 = 10 + skill_lv + (status->luk / 10); // Critical increase
// src/map/skill.cpp:5966
val1 *= 10; //Because every 10 crit is an actual cri point.
// src/map/skill.cpp:5971
val1 = (skill_lv+1)*25;	//Atk increase
// src/map/skill.cpp:5972
val2 = (skill_lv+1)*2;	//Def increase
// src/map/skill.cpp:5975
val1 = (skill_lv+2)*25;	//Atk increase
// src/map/skill.cpp:5978
val1 = 25 + 11*skill_lv; //Exp increase bonus.
// src/map/skill.cpp:5981
val1 = 55 + skill_lv*5;	//Elemental Resistance
// src/map/skill.cpp:5982
val2 = skill_lv*10;	//Status ailment resistance
// src/map/skill.cpp:7700
status_change_end(bl, type);
// src/map/skill.cpp:7718
status_change_end(bl, SC_DANCING);
```

### Harmonic Lick (`BD_RINGNIBELUNGEN`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=38; Lv2=41; Lv3=44; Lv4=47; Lv5=50；武器 Musical, Whip；关联状态：Nibelungen。

- 技能树最高等级：`5`
- 前置技能：BD_DRUMBATTLEFIELD Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/harmoniclick.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5962
val1 *= 10; // ASPD works with 1000 as 100%
// src/map/skill.cpp:5965
val1 = 10 + skill_lv + (status->luk / 10); // Critical increase
// src/map/skill.cpp:5966
val1 *= 10; //Because every 10 crit is an actual cri point.
// src/map/skill.cpp:5971
val1 = (skill_lv+1)*25;	//Atk increase
// src/map/skill.cpp:5972
val2 = (skill_lv+1)*2;	//Def increase
// src/map/skill.cpp:5975
val1 = (skill_lv+2)*25;	//Atk increase
// src/map/skill.cpp:5978
val1 = 25 + 11*skill_lv; //Exp increase bonus.
// src/map/skill.cpp:5981
val1 = 55 + skill_lv*5;	//Elemental Resistance
// src/map/skill.cpp:5982
val2 = skill_lv*10;	//Status ailment resistance
// src/map/skill.cpp:7700
status_change_end(bl, type);
// src/map/skill.cpp:7718
status_change_end(bl, SC_DANCING);
// src/map/skills/archer/harmoniclick.cpp:11
void SkillHarmonicLick::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Classical Pluck (`BD_ROKISWEIL`)

特殊技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP 15；武器 Musical, Whip；关联状态：RokisWeil。

- 技能树最高等级：`1`
- 前置技能：BA_ASSASSINCROSS Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/classicalpluck.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:4324
ShowWarning("skill_castend_song: Unknown song skill ID: %u\n", skill_id);
// src/map/skill.cpp:4328
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skill.cpp:7700
status_change_end(bl, type);
// src/map/skill.cpp:7718
status_change_end(bl, SC_DANCING);
// src/map/skills/archer/classicalpluck.cpp:11
void SkillClassicalPluck::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/classicalpluck.cpp:13
skill_castend_song(src, getSkillId(), skill_lv, tick);
// src/map/skills/archer/classicalpluck.cpp:17
void SkillClassicalPluck::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/classicalpluck.cpp:20
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Power Chord (`BD_INTOABYSS`)

特殊技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP 10；武器 Musical, Whip；关联状态：IntoAbyss。

- 技能树最高等级：`1`
- 前置技能：BD_LULLABY Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/powerchord.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:7700
status_change_end(bl, type);
// src/map/skill.cpp:7718
status_change_end(bl, SC_DANCING);
// src/map/skills/archer/powerchord.cpp:11
void SkillPowerChord::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/powerchord.cpp:13
skill_castend_song(src, getSkillId(), skill_lv, tick);
// src/map/skills/archer/powerchord.cpp:17
void SkillPowerChord::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/powerchord.cpp:20
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Acoustic Rhythm (`BD_SIEGFRIED`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP 20；武器 Musical, Whip；关联状态：Siegfried。

- 技能树最高等级：`5`
- 前置技能：BA_POEMBRAGI Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/acousticrhythm.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5971
val1 = (skill_lv+1)*25;	//Atk increase
// src/map/skill.cpp:5972
val2 = (skill_lv+1)*2;	//Def increase
// src/map/skill.cpp:5975
val1 = (skill_lv+2)*25;	//Atk increase
// src/map/skill.cpp:5978
val1 = 25 + 11*skill_lv; //Exp increase bonus.
// src/map/skill.cpp:5981
val1 = 55 + skill_lv*5;	//Elemental Resistance
// src/map/skill.cpp:5982
val2 = skill_lv*10;	//Status ailment resistance
// src/map/skill.cpp:7700
status_change_end(bl, type);
// src/map/skill.cpp:7718
status_change_end(bl, SC_DANCING);
// src/map/skills/archer/acousticrhythm.cpp:11
void SkillAcousticRhythm::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/acousticrhythm.cpp:13
skill_castend_song(src, getSkillId(), skill_lv, tick);
// src/map/skills/archer/acousticrhythm.cpp:17
void SkillAcousticRhythm::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/acousticrhythm.cpp:20
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
```

### Pang Voice (`BA_PANGVOICE`)

特殊技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；吟唱：1000 ms；技能后摇：2000 ms；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP 20。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/pangvoice.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/pangvoice.cpp:14
void SkillPangVoice::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/pangvoice.cpp:17
sc_start(src, target, SC_CONFUSION, 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
// src/map/skills/archer/pangvoice.cpp:18
sc_start(src, target, SC_BLEEDING, 100, skill_lv, skill_get_time2(getSkillId(), skill_lv));
// src/map/skills/archer/pangvoice.cpp:21
sc_start(src, target, SC_CONFUSION, 70, skill_lv, skill_get_time(getSkillId(), skill_lv));
// src/map/skills/archer/pangvoice.cpp:23
clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
```
