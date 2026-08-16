# Swordman 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Swordman` 公式页](../skill-formulas/Swordman.md)

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 2 | `SM_SWORD` | Sword Mastery | 10 | Swordman | 是 | — | Weapon / Passive |
| 3 | `SM_TWOHAND` | Two-Handed Sword Mastery | 10 | Swordman | 是 | SM_SWORD Lv1 | Weapon / Passive |
| 4 | `SM_RECOVERY` | Increase HP Recovery | 10 | Swordman | 是 | — | None / Passive |
| 5 | `SM_BASH` | Bash | 10 | Swordman | 是 | — | Weapon / Attack |
| 6 | `SM_PROVOKE` | Provoke | 10 | Swordman | 是 | — | None / Attack |
| 7 | `SM_MAGNUM` | Magnum Break | 10 | Swordman | 是 | SM_BASH Lv5 | Weapon / Self |
| 8 | `SM_ENDURE` | Endure | 10 | Swordman | 是 | SM_PROVOKE Lv5 | Weapon / Self |
| 144 | `SM_MOVINGRECOVERY` | Moving HP-Recovery | 1 | Swordman | 是 | — | None / Passive |
| 145 | `SM_FATALBLOW` | Fatal Blow | 1 | Swordman | 是 | — | Weapon / Passive |
| 146 | `SM_AUTOBERSERK` | Auto Berserk | 1 | Swordman | 是 | — | Weapon / Self |

## 技能详情

### Sword Mastery (`SM_SWORD`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2335
damage += (skill * 3);
// src/map/battle.cpp:2339
damage += (skill * 4);
// src/map/battle.cpp:2341
damage += skill * 10;
// src/map/battle.cpp:2345
damage += (skill * 4);
```

### Two-Handed Sword Mastery (`SM_TWOHAND`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：SM_SWORD Lv1
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2335
damage += (skill * 3);
// src/map/battle.cpp:2339
damage += (skill * 4);
// src/map/battle.cpp:2341
damage += skill * 10;
// src/map/battle.cpp:2345
damage += (skill * 4);
// src/map/battle.cpp:2351
damage += (skill * 4);
// src/map/battle.cpp:2353
damage += (skill * 5);
// src/map/battle.cpp:2356
damage += (skill * 10);
```

### Increase HP Recovery (`SM_RECOVERY`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skills/merchant/aidberserkpotion.cpp`, `src/map/skills/merchant/aidcondensedpotion.cpp`, `src/map/skills/merchant/aidpotion.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:10688
* Heal player HP and/or SP linearly. Calculate any bonus based on active statuses.
// src/map/pc.cpp:10691
* @param hp: HP to heal
// src/map/pc.cpp:10692
* @param sp: SP to heal
// src/map/pc.cpp:10693
* @return Amount healed to an object
// src/map/pc.cpp:10695
int32 pc_itemheal(map_session_data *sd, t_itemid itemid, int32 hp, int32 sp)
// src/map/pc.cpp:10699
if (hp) {
// src/map/pc.cpp:10705
bonus += bonus; // Receive an additional +100% effect from ranked potions to HP only
// src/map/pc.cpp:10708
bonus += sd->bonus.itemhealrate2;
// src/map/pc.cpp:10710
bonus += bonus * pc_get_itemgroup_bonus(sd, itemid, sd->itemgrouphealrate) / 100;
// src/map/pc.cpp:10712
for(const auto &it : sd->itemhealrate) {
// src/map/skills/merchant/aidberserkpotion.cpp:57
hp = tstatus->max_hp * potion_per_hp / 100;
// src/map/skills/merchant/aidberserkpotion.cpp:58
hp = hp * (100 + pc_checkskill(sd,AM_POTIONPITCHER)*10 + pc_checkskill(sd,AM_LEARNINGPOTION)*5)*bonus/10000;
```

### Bash (`SM_BASH`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-1；命中类型：Single；段数：1；属性：Weapon；持续时间2：5000 ms；消耗/限制：SP Lv1-5=8; Lv6-10=15；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；关联状态：Stun。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/custom/skill_factory_custom.cpp`, `src/map/skills/swordman/banishingpoint.cpp`, `src/map/skills/swordman/bash.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/custom/skill_factory_custom.cpp:25
void calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const override{
// src/map/skills/swordman/banishingpoint.cpp:14
void SkillBanishingPoint::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& skillratio, int32 mflag) const {
// src/map/skills/swordman/banishingpoint.cpp:15
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/swordman/banishingpoint.cpp:16
const status_change* sc = status_get_sc(src);
// src/map/skills/swordman/banishingpoint.cpp:18
skillratio += -100 + (100 * skill_lv);
// src/map/skills/swordman/banishingpoint.cpp:21
skillratio += pc_checkskill(sd, SM_BASH) * 70;
// src/map/skills/swordman/banishingpoint.cpp:25
skillratio += 800;
// src/map/skills/swordman/banishingpoint.cpp:31
void SkillBanishingPoint::modifyHitRate(int16& hit_rate, const block_list* src, const block_list* target, uint16 skill_lv) const {
// src/map/skills/swordman/banishingpoint.cpp:32
hit_rate += 5 * skill_lv;
// src/map/skills/swordman/bash.cpp:12
void SkillBash::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/swordman/bash.cpp:14
base_skillratio += 30 * skill_lv;
// src/map/skills/swordman/bash.cpp:17
void SkillBash::modifyHitRate(int16& hit_rate, const block_list* src, const block_list* target, uint16 skill_lv) const {
```

### Provoke (`SM_PROVOKE`)

非伤害技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；冷却：1000 ms；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=4; Lv2=5; Lv3=6; Lv4=7; Lv5=8; Lv6=9; Lv7=10; Lv8=11; Lv9=12; Lv10=13；关联状态：Provoke。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/swordman/provoke.cpp`, `src/map/skills/swordman/selfprovoke.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:7270
skill_attack(BF_MISC, ss, unit, bl, sg->skill_id, sg->skill_lv, tick, i);
// src/map/skill.cpp:7273
sc_start(ss, bl, SC_CURSE, 100, 1, 1800000); //30 minutes
// src/map/skill.cpp:7276
sc_start(ss, bl, SC_BLIND, 100, 1, 1800000); //30 minutes
// src/map/skill.cpp:7279
sc_start2(ss, bl, SC_POISON, 100, 1, ss->id, 1800000); //30 minutes
// src/map/skill.cpp:7282
clif_skill_nodamage(nullptr, *bl, SM_PROVOKE, 10, sc_start(ss, bl, SC_PROVOKE, 100, 10, INFINITE_TICK)); //Infinite
// src/map/skill.cpp:7284
case 6: // DEF -100%
// src/map/skill.cpp:7285
sc_start(ss, bl, SC_INCDEFRATE, 100, -100, 20000); //20 seconds
// src/map/skill.cpp:7287
case 7: // ATK -100%
// src/map/skill.cpp:7288
sc_start(ss, bl, SC_INCATKRATE, 100, -100, 20000); //20 seconds
// src/map/skill.cpp:7290
case 8: // Flee -100%
// src/map/skill.cpp:7291
sc_start(ss, bl, SC_INCFLEERATE, 100, -100, 20000); //20 seconds
// src/map/skill.cpp:7293
case 9: // Speed/ASPD -25%
```

### Magnum Break (`SM_MAGNUM`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；属性：Fire；范围：Lv1-10=2; Lv11=4；击退：2；技能后摇：2000 ms；持续时间2：10000 ms；伤害标记：Splash；消耗/限制：HP Lv1-2=20; Lv3-4=19; Lv5-6=18; Lv7-8=17; Lv9-10=16；SP 30；关联状态：Watk_Element。

- 技能树最高等级：`10`
- 前置技能：SM_BASH Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/swordman/magnum.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:3526
* @param bl Object from which HP/SP/AP are consumed
// src/map/skill.cpp:3528
* @param hp Original HP requirement to use skill
// src/map/skill.cpp:3529
* @param sp Original SP requirement to use skill
// src/map/skill.cpp:3532
void skill_consume_hpspap(block_list* bl, uint16 skill_id, int32 hp, int32 sp, int32 ap)
// src/map/skill.cpp:3540
hp = 0;
// src/map/skill.cpp:3544
status_zap(bl, hp, sp, ap);
// src/map/skill.cpp:3548
* Checks that you have the requirements for casting a skill for homunculus/mercenary.
// src/map/skill.cpp:3550
* &1: finished casting the skill (invoke hp/sp/item consumption)
// src/map/skills/swordman/magnum.cpp:17
void SkillMagnumBreak::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const
// src/map/skills/swordman/magnum.cpp:21
base_skillratio += 20 * skill_lv;
// src/map/skills/swordman/magnum.cpp:24
base_skillratio += 10 * skill_lv;
```

### Endure (`SM_ENDURE`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；冷却：10000 ms；持续时间1：Lv1=10000; Lv2=13000; Lv3=16000; Lv4=19000; Lv5=22000; Lv6=25000; Lv7=28000; Lv8=31000; Lv9=34000; Lv10=37000 ms；持续时间2：10000 ms；伤害标记：NoDamage；消耗/限制：SP 10；关联状态：Endure。

- 技能树最高等级：`10`
- 前置技能：SM_PROVOKE Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/skill_factory_swordman.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Moving HP-Recovery (`SM_MOVINGRECOVERY`)

非伤害技能；目标：被动；最高等级 1。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/status.cpp:4644
if(battle_config.pc_damage_delay_rate != 100)
// src/map/status.cpp:4645
base_status->dmotion = base_status->dmotion*battle_config.pc_damage_delay_rate/100;
// src/map/status.cpp:4660
sd->dsprate -= 4*skill;
// src/map/status.cpp:4663
sd->dsprate -= sc->getSCE(SC_SERVICE4U)->val3;
```

### Fatal Blow (`SM_FATALBLOW`)

武器/物理技能；目标：被动；最高等级 1。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/swordman/bash.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/swordman/bash.cpp:14
base_skillratio += 30 * skill_lv;
// src/map/skills/swordman/bash.cpp:17
void SkillBash::modifyHitRate(int16& hit_rate, const block_list* src, const block_list* target, uint16 skill_lv) const {
// src/map/skills/swordman/bash.cpp:20
hit_rate += hit_rate * 5 * skill_lv / 100;
// src/map/skills/swordman/bash.cpp:23
void SkillBash::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/swordman/bash.cpp:24
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/swordman/bash.cpp:26
if (sd != nullptr && skill_lv > 5 && pc_checkskill(sd, SM_FATALBLOW) > 0) {
// src/map/skills/swordman/bash.cpp:28
int32 stun_chance = (skill_lv - 5) * sd->status.base_level * 10;
// src/map/skills/swordman/bash.cpp:29
status_change_start(src, target, SC_STUN, stun_chance, skill_lv, 0, 0, 0, skill_get_time2(getSkillId(), skill_lv), SCSTART_NONE);
```

### Auto Berserk (`SM_AUTOBERSERK`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：AutoBerserk。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/swordman/autoberserk.cpp`, `src/map/skills/swordman/skill_factory_swordman.cpp`

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
// src/map/skills/swordman/autoberserk.cpp:13
void SkillAutoBerserk::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
// src/map/skills/swordman/autoberserk.cpp:16
status_change *tsc = status_get_sc(bl);
// src/map/skills/swordman/autoberserk.cpp:17
status_change_entry *tsce = (tsc) ? tsc->getSCE(type) : nullptr;
// src/map/skills/swordman/autoberserk.cpp:21
i = status_change_end(bl, type);
```
