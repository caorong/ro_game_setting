# Assassin_Cross 技能

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
| 132 | `AS_RIGHT` | Righthand Mastery | 5 | Assassin | 否 | — | Weapon / Passive |
| 133 | `AS_LEFT` | Lefthand Mastery | 5 | Assassin | 否 | AS_RIGHT Lv2 | Weapon / Passive |
| 134 | `AS_KATAR` | Katar Mastery | 10 | Assassin | 否 | — | Weapon / Passive |
| 135 | `AS_CLOAKING` | Cloaking | 10 | Assassin | 否 | TF_HIDING Lv2 | Weapon / Self |
| 136 | `AS_SONICBLOW` | Sonic Blow | 10 | Assassin | 否 | AS_KATAR Lv4 | Weapon / Attack |
| 137 | `AS_GRIMTOOTH` | Grimtooth | 5 | Assassin | 否 | AS_CLOAKING Lv2, AS_SONICBLOW Lv5 | Weapon / Attack |
| 138 | `AS_ENCHANTPOISON` | Enchant Poison | 10 | Assassin | 否 | TF_POISON Lv1 | Weapon / Support |
| 139 | `AS_POISONREACT` | Poison React | 10 | Assassin | 否 | AS_ENCHANTPOISON Lv3 | Weapon / Self |
| 140 | `AS_VENOMDUST` | Venom Dust | 10 | Assassin | 否 | AS_ENCHANTPOISON Lv5 | Weapon / Ground |
| 141 | `AS_SPLASHER` | Venom Splasher | 10 | Assassin | 否 | AS_POISONREACT Lv5, AS_VENOMDUST Lv5 | Weapon / Attack |
| 1003 | `AS_SONICACCEL` | Sonic Acceleration | 1 | Assassin | 否 | — | Weapon / Passive |
| 1004 | `AS_VENOMKNIFE` | Throw Venom Knife | 1 | Assassin | 否 | — | Weapon / Attack |
| 376 | `ASC_KATAR` | Advanced Katar Mastery | 5 | Assassin_Cross | 是 | TF_DOUBLE Lv5, AS_KATAR Lv7 | Weapon / Passive |
| 378 | `ASC_EDP` | Enchant Deadly Poison | 5 | Assassin_Cross | 是 | ASC_CDP Lv1 | Weapon / Self |
| 379 | `ASC_BREAKER` | Soul Destroyer | 10 | Assassin_Cross | 是 | TF_DOUBLE Lv5, AS_CLOAKING Lv3, AS_ENCHANTPOISON Lv6, TF_POISON Lv5 | Weapon / Attack |
| 406 | `ASC_METEORASSAULT` | Meteor Assault | 10 | Assassin_Cross | 是 | AS_RIGHT Lv3, AS_KATAR Lv5, AS_SONICBLOW Lv5, ASC_BREAKER Lv1 | Weapon / Self |
| 407 | `ASC_CDP` | Create Deadly Poison | 1 | Assassin_Cross | 是 | TF_POISON Lv10, TF_DETOXIFY Lv1, AS_ENCHANTPOISON Lv5 | None / Self |

## 技能详情

### Advanced Katar Mastery (`ASC_KATAR`)

武器/物理技能；目标：被动；最高等级 5；段数：1；伤害标记：NoDamage。

- 技能树最高等级：`5`
- 前置技能：TF_DOUBLE Lv5, AS_KATAR Lv7
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1056
if( sd->status.weapon == W_KATAR && (skill = pc_checkskill(sd,ASC_KATAR)) > 0 ) // Adv. Katar Mastery functions similar to a +%ATK card on official [helvetica]
// src/map/battle.cpp:5567
ATK_RATE(wd.damage, wd.damage2, battle_calc_attack_skill_ratio(&wd, src, target, skill_id, skill_lv));
// src/map/battle.cpp:5570
ATK_ADD(wd.damage, wd.damage2, battle_calc_skill_constant_addition(&wd, src, target, skill_id, skill_lv));
// src/map/battle.cpp:5576
if (sd->status.weapon == W_KATAR && (katar_skill = pc_checkskill(sd, ASC_KATAR)) > 0) // Adv. Katar Mastery applied after calculate with skillratio.
// src/map/battle.cpp:5577
ATK_ADDRATE(wd.damage, wd.damage2, (10 + 2 * katar_skill));
// src/map/battle.cpp:5582
if ((wd.damage + wd.damage2) && tstatus->res > 0 && !nk[NK_SIMPLEDEFENSE]) {
```

### Enchant Deadly Poison (`ASC_EDP`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；属性：Poison；技能后摇：2000 ms；持续时间1：Lv1=40000; Lv2=45000; Lv3=50000; Lv4=55000; Lv5=60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=60; Lv2=70; Lv3=80; Lv4=90; Lv5=100；道具 Poison_Bottle×1；关联状态：Edp。

- 技能树最高等级：`5`
- 前置技能：ASC_CDP Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/enchantdeadlypoison.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
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
// src/map/skill.cpp:9476
int32 maxcount = skill_get_maxcount(skill_id, skill_lv), c = 0;
// src/map/skills/thief/enchantdeadlypoison.cpp:13
void SkillEnchantDeadlyPoison::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/thief/enchantdeadlypoison.cpp:15
StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
// src/map/skills/thief/enchantdeadlypoison.cpp:18
sc_start4(src, src, SC_SUB_WEAPONPROPERTY, 100, ELE_POISON, 25, getSkillId(), 0, skill_get_time(getSkillId(), skill_lv));
// src/map/skills/thief/enchantdeadlypoison.cpp:20
sc_start4(src, src, SC_WATK_ELEMENT, 100, ELE_POISON, 25, 0, 0, skill_get_time(getSkillId(), skill_lv));
```

### Soul Destroyer (`ASC_BREAKER`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Weapon；吟唱：700 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800; Lv6=2000; Lv7=2200; Lv8=2400; Lv9=2600; Lv10=2800 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP Lv1-5=20; Lv6-10=30。

- 技能树最高等级：`10`
- 前置技能：TF_DOUBLE Lv5, AS_CLOAKING Lv3, AS_ENCHANTPOISON Lv6, TF_POISON Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`, `src/map/skills/thief/souldestroyer.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1601
clif_skill_nodamage(target, *target, TK_DODGE, 1);
// src/map/battle.cpp:1602
sc_start4(src, target, SC_COMBO, 100, TK_JUMPKICK, src->id, 1, 0, 2000);
// src/map/battle.cpp:1606
if ((sce = sc->getSCE(SC_KAUPE)) && (skill_id != NPC_EARTHQUAKE || (skill_id == NPC_EARTHQUAKE && flag & NPC_EARTHQUAKE_FLAG)) && rnd() % 100 < sce->val2) { //Kaupe blocks damage (skill or otherwise) from players, mobs, homuns, mercenaries.
// src/map/battle.cpp:1613
status_change_end(target, SC_KAUPE);
// src/map/battle.cpp:1739
damage += damage * 10 / 100;
// src/map/battle.cpp:1741
damage += damage / 10;
// src/map/battle.cpp:1745
damage *= 2; // Lex Aeterna only doubles damage of regular attacks from mercenaries
// src/map/battle.cpp:1750
status_change_end(bl, SC_AETERNA); //Shouldn't end until Breaker's non-weapon part connects.
// src/map/battle.cpp:1756
damage += damage * 15 / 100;
// src/map/battle.cpp:1758
damage += damage * 30 / 100;
// src/map/battle.cpp:3083
cri += 300; // !TODO: Confirm new bonus
// src/map/battle.cpp:3085
cri += 200;
```

### Meteor Assault (`ASC_METEORASSAULT`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；属性：Weapon；范围：2；吟唱：500 ms；技能后摇：500 ms；持续时间2：Lv1=30000; Lv2=5000; Lv3=120000 ms；伤害标记：Splash, IgnoreAtkCard；消耗/限制：SP Lv1=10; Lv2=12; Lv3=14; Lv4=16; Lv5=18; Lv6=20; Lv7=22; Lv8=24; Lv9=26; Lv10=28。

- 技能树最高等级：`10`
- 前置技能：AS_RIGHT Lv3, AS_KATAR Lv5, AS_SONICBLOW Lv5, ASC_BREAKER Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/thief/meteorassault.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4545
ATK_ADDRATE(wd->damage, wd->damage2, 15 * sd->spiritcharm);
// src/map/battle.cpp:4547
ATK_ADDRATE(wd->weaponAtk, wd->weaponAtk2, 15 * sd->spiritcharm);
// src/map/battle.cpp:4555
ATK_ADDRATE(wd->weaponAtk, wd->weaponAtk2, sc->getSCE(SC_WATK_ELEMENT)->val2);
// src/map/battle.cpp:4561
int16 tmdef = tstatus->mdef + tstatus->mdef2;
// src/map/battle.cpp:4563
if (sstatus->matk_min > tmdef && sstatus->matk_max > sstatus->matk_min) {
// src/map/battle.cpp:4564
ATK_ADD(wd->weaponAtk, wd->weaponAtk2, i64max((sstatus->matk_min + rnd() % (sstatus->matk_max - sstatus->matk_min)) - tmdef, 0));
// src/map/battle.cpp:4566
ATK_ADD(wd->weaponAtk, wd->weaponAtk2, i64max(sstatus->matk_min - tmdef, 0));
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

### Create Deadly Poison (`ASC_CDP`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；技能后摇：500 ms；伤害标记：NoDamage；消耗/限制：SP 50。

- 技能树最高等级：`1`
- 前置技能：TF_POISON Lv10, TF_DETOXIFY Lv1, AS_ENCHANTPOISON Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/thief/createdeadlypoison.cpp`, `src/map/skills/thief/skill_factory_thief.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:12951
make_per = 100000; // Star Crumbs are 100% success crafting rate? (made 1000% so it succeeds even after penalties) [Skotlex]
// src/map/skill.cpp:12965
case AM_PHARMACY: // Potion Preparation - reviewed with the help of various Ragnainfo sources [DracoRPG]
// src/map/skill.cpp:13436
case ASC_CDP: //25% Damage yourself, and display same effect as failed potion.
// src/map/skill.cpp:13437
status_percent_damage(nullptr, sd, -25, 0, true);
// src/map/skills/thief/createdeadlypoison.cpp:12
void SkillCreateDeadlyPoison::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/thief/createdeadlypoison.cpp:13
map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/thief/createdeadlypoison.cpp:17
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
```
