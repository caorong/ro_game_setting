# Dancer 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Dancer` 公式页](../skill-formulas/Dancer.md)

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
| 323 | `DC_DANCINGLESSON` | Dance Lessons | 10 | Dancer | 是 | — | Weapon / Passive |
| 324 | `DC_THROWARROW` | Slinging Arrow | 5 | Dancer | 是 | DC_DANCINGLESSON Lv3 | Weapon / Attack |
| 325 | `DC_UGLYDANCE` | Hip Shaker | 5 | Dancer | 是 | DC_DANCINGLESSON Lv1, BD_ADAPTATION Lv1 | Misc / Self |
| 326 | `DC_SCREAM` | Dazzler | 5 | Dancer | 是 | BD_ENCORE Lv1 | Misc / Self |
| 327 | `DC_HUMMING` | Focus Ballet | 10 | Dancer | 是 | DC_UGLYDANCE Lv3 | Misc / Self |
| 328 | `DC_DONTFORGETME` | Slow Grace | 10 | Dancer | 是 | DC_UGLYDANCE Lv3 | Misc / Self |
| 329 | `DC_FORTUNEKISS` | Lady Luck | 10 | Dancer | 是 | DC_UGLYDANCE Lv3 | Misc / Self |
| 330 | `DC_SERVICEFORYOU` | Gypsy's Kiss | 10 | Dancer | 是 | DC_UGLYDANCE Lv3 | Misc / Self |
| 304 | `BD_ADAPTATION` | Amp | 1 | Dancer | 是 | — | None / Self |
| 305 | `BD_ENCORE` | Encore | 1 | Dancer | 是 | BD_ADAPTATION Lv1 | None / Self |
| 306 | `BD_LULLABY` | Lullaby | 1 | Dancer | 是 | DC_HUMMING Lv10 | Misc / Self |
| 307 | `BD_RICHMANKIM` | Mental Sensing | 5 | Dancer | 是 | BD_SIEGFRIED Lv3 | Misc / Self |
| 308 | `BD_ETERNALCHAOS` | Down Tempo | 1 | Dancer | 是 | BD_ROKISWEIL Lv1 | Misc / Self |
| 309 | `BD_DRUMBATTLEFIELD` | Battle Theme | 5 | Dancer | 是 | DC_SERVICEFORYOU Lv10 | Misc / Self |
| 310 | `BD_RINGNIBELUNGEN` | Harmonic Lick | 5 | Dancer | 是 | BD_DRUMBATTLEFIELD Lv3 | Misc / Self |
| 311 | `BD_ROKISWEIL` | Classical Pluck | 1 | Dancer | 是 | DC_DONTFORGETME Lv10 | Misc / Self |
| 312 | `BD_INTOABYSS` | Power Chord | 1 | Dancer | 是 | BD_LULLABY Lv1 | Misc / Self |
| 313 | `BD_SIEGFRIED` | Acoustic Rhythm | 5 | Dancer | 是 | DC_FORTUNEKISS Lv10 | Misc / Self |
| 1011 | `DC_WINKCHARM` | Wink of Charm | 1 | Dancer | 是 | — | Misc / Attack |

## 技能详情

### Dance Lessons (`DC_DANCINGLESSON`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/hipshaker.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
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
// src/map/battle.cpp:2395
damage += (skill * 3);
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
```

### Slinging Arrow (`DC_THROWARROW`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Weapon；吟唱：1500 ms；消耗/限制：SP Lv1=1; Lv2=3; Lv3=5; Lv4=7; Lv5=9；弹药数 1；武器 Whip；弹药 Arrow。

- 技能树最高等级：`5`
- 前置技能：DC_DANCINGLESSON Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/archer/skill_factory_archer.cpp`, `src/map/skills/archer/slingingarrow.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/slingingarrow.cpp:11
void SkillSlingingArrow::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/archer/slingingarrow.cpp:13
base_skillratio += 10 + 40 * skill_lv;
// src/map/skills/archer/slingingarrow.cpp:15
base_skillratio += -40 + 40 * skill_lv;
```

### Hip Shaker (`DC_UGLYDANCE`)

特殊技能；目标：自身；最高等级 5；命中类型：Multi_Hit；段数：1；持续时间1：30000 ms；持续时间2：3000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=23; Lv2=26; Lv3=29; Lv4=32; Lv5=35；武器 Whip。

- 技能树最高等级：`5`
- 前置技能：DC_DANCINGLESSON Lv1, BD_ADAPTATION Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/hipshaker.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

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
// src/map/skill.cpp:4328
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skill.cpp:4347
clif_skill_nodamage(src, *src, skill_id, skill_lv);
// src/map/skill.cpp:4349
sd->skill_lv_dance = skill_lv;
// src/map/skill.cpp:11969
skill_usave_add(((TBL_PC*)src), group->skill_id, group->skill_lv);
// src/map/skills/archer/hipshaker.cpp:13
void SkillHipShaker::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/archer/hipshaker.cpp:16
status_zap( target, 0, 2 * skill_lv + 10 );
```

### Dazzler (`DC_SCREAM`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；技能后摇：4000 ms；持续时间1：5000 ms；持续时间2：5000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20；关联状态：Stun。

- 技能树最高等级：`5`
- 前置技能：BD_ENCORE Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/dazzler.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`

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

### Focus Ballet (`DC_HUMMING`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=22; Lv2=24; Lv3=26; Lv4=28; Lv5=30; Lv6=32; Lv7=34; Lv8=36; Lv9=38; Lv10=40；武器 Musical, Whip；关联状态：Humming。

- 技能树最高等级：`10`
- 前置技能：DC_UGLYDANCE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/focusballet.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

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
// src/map/skill.cpp:7754
status_change_end(bl, type);
// src/map/skill.cpp:7766
delete_timer(sce->timer, status_change_timer);
// src/map/skill.cpp:7769
t_tick duration = skill_get_time2(skill_id, 1);
// src/map/skill.cpp:7770
sce->val4 = 1; //Store the fact that this is a "reduced" duration effect.
// src/map/skill.cpp:7771
sce->timer = add_timer(tick + duration, status_change_timer, bl->id, type);
// src/map/skill.cpp:11969
skill_usave_add(((TBL_PC*)src), group->skill_id, group->skill_lv);
// src/map/skill.cpp:11975
status_change* sc = status_get_sc(src);
```

### Slow Grace (`DC_DONTFORGETME`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：180000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=28; Lv2=31; Lv3=34; Lv4=37; Lv5=40; Lv6=43; Lv7=46; Lv8=49; Lv9=52; Lv10=55；武器 Musical, Whip；关联状态：DontForgetMe。

- 技能树最高等级：`10`
- 前置技能：DC_UGLYDANCE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/skills/archer/slowgrace.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:4328
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skill.cpp:4347
clif_skill_nodamage(src, *src, skill_id, skill_lv);
// src/map/skill.cpp:4349
sd->skill_lv_dance = skill_lv;
// src/map/skill.cpp:5924
val1 = 3 * skill_lv + status->dex / 10; // Casting time reduction
// src/map/skill.cpp:5926
val2 = (skill_lv < 10 ? 3 * skill_lv : 50) + status->int_ / 5; // After-cast delay reduction
// src/map/skill.cpp:5934
val1 = 3 * skill_lv + status->dex / 15; // ASPD decrease
// src/map/skill.cpp:5935
val2 = 2 * skill_lv + status->agi / 20; // Movement speed adjustment.
// src/map/skill.cpp:5937
val1 = 5 + 3 * skill_lv + status->dex / 10; // ASPD decrease
// src/map/skill.cpp:5938
val2 = 5 + 3 * skill_lv + status->agi / 10; // Movement speed adjustment.
// src/map/skill.cpp:7754
status_change_end(bl, type);
// src/map/skill.cpp:7766
delete_timer(sce->timer, status_change_timer);
// src/map/skill.cpp:7769
t_tick duration = skill_get_time2(skill_id, 1);
```

### Lady Luck (`DC_FORTUNEKISS`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：120000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=43; Lv2=46; Lv3=49; Lv4=52; Lv5=55; Lv6=58; Lv7=61; Lv8=64; Lv9=67; Lv10=70；武器 Musical, Whip；关联状态：Fortune。

- 技能树最高等级：`10`
- 前置技能：DC_UGLYDANCE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/ladyluck.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
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
// src/map/skill.cpp:5971
val1 = (skill_lv+1)*25;	//Atk increase
// src/map/skill.cpp:5972
val2 = (skill_lv+1)*2;	//Def increase
// src/map/skill.cpp:5975
val1 = (skill_lv+2)*25;	//Atk increase
// src/map/skill.cpp:7754
status_change_end(bl, type);
// src/map/skill.cpp:7766
delete_timer(sce->timer, status_change_timer);
// src/map/skill.cpp:7769
t_tick duration = skill_get_time2(skill_id, 1);
// src/map/skill.cpp:7770
sce->val4 = 1; //Store the fact that this is a "reduced" duration effect.
```

### Gypsy's Kiss (`DC_SERVICEFORYOU`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：180000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=40; Lv2=45; Lv3=50; Lv4=55; Lv5=60; Lv6=65; Lv7=70; Lv8=75; Lv9=80; Lv10=85；武器 Musical, Whip；关联状态：Service4U。

- 技能树最高等级：`10`
- 前置技能：DC_UGLYDANCE Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/gypsyskiss.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:5938
val2 = 5 + 3 * skill_lv + status->agi / 10; // Movement speed adjustment.
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
// src/map/skill.cpp:7754
status_change_end(bl, type);
// src/map/skill.cpp:7766
delete_timer(sce->timer, status_change_timer);
// src/map/skill.cpp:7769
t_tick duration = skill_get_time2(skill_id, 1);
// src/map/skill.cpp:7770
sce->val4 = 1; //Store the fact that this is a "reduced" duration effect.
// src/map/skill.cpp:7771
sce->timer = add_timer(tick + duration, status_change_timer, bl->id, type);
// src/map/skill.cpp:7775
clif_status_change(bl, static_cast<int32>(scdb->icon), 1, duration, 1, 0, 0);
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
- 前置技能：DC_HUMMING Lv10
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
- 前置技能：DC_SERVICEFORYOU Lv10
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
- 前置技能：DC_DONTFORGETME Lv10
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
- 前置技能：DC_FORTUNEKISS Lv10
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

### Wink of Charm (`DC_WINKCHARM`)

特殊技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；吟唱：1000 ms；技能后摇：2000 ms；持续时间1：30000 ms；持续时间2：10000 ms；伤害标记：NoDamage；消耗/限制：SP 40；关联状态：WinkCharm。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/archer/skill_factory_archer.cpp`, `src/map/skills/archer/winkofcharm.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/archer/winkofcharm.cpp:17
void SkillWinkofCharm::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/winkofcharm.cpp:19
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/archer/winkofcharm.cpp:20
mob_data* dstmd = BL_CAST(BL_MOB, target);
// src/map/skills/archer/winkofcharm.cpp:25
sc_start(src, target, SC_CONFUSION, 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
// src/map/skills/archer/winkofcharm.cpp:26
sc_start(src, target, SC_HALLUCINATION, 100, skill_lv, skill_get_time2(getSkillId(), skill_lv));
```
