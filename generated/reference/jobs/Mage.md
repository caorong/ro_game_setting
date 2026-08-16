# Mage 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 9 | `MG_SRECOVERY` | Increase SP Recovery | 10 | Mage | 是 | — | None / Passive |
| 10 | `MG_SIGHT` | Sight | 1 | Mage | 是 | — | Magic / Self |
| 11 | `MG_NAPALMBEAT` | Napalm Beat | 10 | Mage | 是 | — | Magic / Attack |
| 12 | `MG_SAFETYWALL` | Safety Wall | 10 | Mage | 是 | MG_NAPALMBEAT Lv7, MG_SOULSTRIKE Lv5 | Magic / Ground |
| 13 | `MG_SOULSTRIKE` | Soul Strike | 10 | Mage | 是 | MG_NAPALMBEAT Lv4 | Magic / Attack |
| 14 | `MG_COLDBOLT` | Cold Bolt | 10 | Mage | 是 | — | Magic / Attack |
| 15 | `MG_FROSTDIVER` | Frost Diver | 10 | Mage | 是 | MG_COLDBOLT Lv5 | Magic / Attack |
| 16 | `MG_STONECURSE` | Stone Curse | 10 | Mage | 是 | — | Magic / Attack |
| 17 | `MG_FIREBALL` | Fire Ball | 10 | Mage | 是 | MG_FIREBOLT Lv4 | Magic / Attack |
| 18 | `MG_FIREWALL` | Fire Wall | 10 | Mage | 是 | MG_FIREBALL Lv5, MG_SIGHT Lv1 | Magic / Ground |
| 19 | `MG_FIREBOLT` | Fire Bolt | 10 | Mage | 是 | — | Magic / Attack |
| 20 | `MG_LIGHTNINGBOLT` | Lightning Bolt | 10 | Mage | 是 | — | Magic / Attack |
| 21 | `MG_THUNDERSTORM` | Thunderstorm | 10 | Mage | 是 | MG_LIGHTNINGBOLT Lv4 | Magic / Ground |
| 157 | `MG_ENERGYCOAT` | Energy Coat | 1 | Mage | 是 | — | Magic / Self |

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

### Sight (`MG_SIGHT`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；段数：1；属性：Fire；范围：3；持续时间1：10000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 10；关联状态：Sight。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/mage/sight.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/sight.cpp:12
void SkillSight::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/mage/sight.cpp:15
clif_skill_nodamage(src, *target, getSkillId(), skill_lv,
// src/map/skills/mage/sight.cpp:16
sc_start2(src, target, type, 100, skill_lv, getSkillId(), skill_get_time(getSkillId(), skill_lv)));
// src/map/skills/mage/skill_factory_mage.cpp:285
case PF_DOUBLECASTING:
```

### Napalm Beat (`MG_NAPALMBEAT`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Ghost；范围：1；吟唱：1000 ms；技能后摇：Lv1-3=1000; Lv4-5=900; Lv6-7=800; Lv8=700; Lv9=600; Lv10=500 ms；伤害标记：Splash, SplashSplit；消耗/限制：SP Lv1-3=9; Lv4-6=12; Lv7-9=15; Lv10=18。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/mage/hindsight.cpp`, `src/map/skills/mage/napalmbeat.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1489
if (sc->getSCE(SC_WHITEIMPRISON)) { // Gravitation and Pressure do damage without removing the effect
// src/map/battle.cpp:1493
(skill_id && skill_get_ele(skill_id, skill_lv) == ELE_GHOST) ||
// src/map/battle.cpp:1497
damage *= 2; // If used against a player in White Imprison, the skill deals double damage.
// src/map/battle.cpp:1498
status_change_end(target, SC_WHITEIMPRISON); // Those skills do damage and removes effect
// src/map/skill.cpp:10716
uint16 lv = pc_checkskill(sd, skill_id), skill_lv = sd->menuskill_val;
// src/map/skill.cpp:10719
if (skill_lv == 0 || lv == 0)
// src/map/skill.cpp:10726
maxlv = skill_lv / 2; // Half of Autospell's level unless player learned a lower level (capped below)
// src/map/skill.cpp:10732
else if(skill_lv==2) maxlv=1;
// src/map/skill.cpp:10733
else if(skill_lv==3) maxlv=2;
// src/map/skill.cpp:10734
else if(skill_lv>=4) maxlv=3;
// src/map/skill.cpp:10737
if(skill_lv==5) maxlv=1;
// src/map/skill.cpp:10738
else if(skill_lv==6) maxlv=2;
```

### Safety Wall (`MG_SAFETYWALL`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：1；属性：Ghost；吟唱：Lv1=4000; Lv2-3=3500; Lv4=2500; Lv5=2000; Lv6=1500; Lv7-10=1000 ms；持续时间1：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000; Lv6=30000; Lv7=35000; Lv8=40000; Lv9=45000; Lv10=50000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-3=30; Lv4-6=35; Lv7-10=40；道具 Blue_Gemstone×1；关联状态：Safetywall。

- 技能树最高等级：`10`
- 前置技能：MG_NAPALMBEAT Lv7, MG_SOULSTRIKE Lv5
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

### Soul Strike (`MG_SOULSTRIKE`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1-2=1; Lv3-4=2; Lv5-6=3; Lv7-8=4; Lv9-10=5；属性：Ghost；吟唱：500 ms；技能后摇：Lv1=1200; Lv2=1000; Lv3=1400; Lv4=1200; Lv5=1600; Lv6=1400; Lv7=1800; Lv8=1600; Lv9=2000; Lv10=1800 ms；消耗/限制：SP Lv1=18; Lv2=14; Lv3=24; Lv4=20; Lv5=30; Lv6=26; Lv7=36; Lv8=32; Lv9=42; Lv10=38。

- 技能树最高等级：`10`
- 前置技能：MG_NAPALMBEAT Lv4
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/mage/hindsight.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/skills/mage/soulstrike.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:1489
if (sc->getSCE(SC_WHITEIMPRISON)) { // Gravitation and Pressure do damage without removing the effect
// src/map/battle.cpp:1493
(skill_id && skill_get_ele(skill_id, skill_lv) == ELE_GHOST) ||
// src/map/battle.cpp:1497
damage *= 2; // If used against a player in White Imprison, the skill deals double damage.
// src/map/battle.cpp:1498
status_change_end(target, SC_WHITEIMPRISON); // Those skills do damage and removes effect
// src/map/skill.cpp:10726
maxlv = skill_lv / 2; // Half of Autospell's level unless player learned a lower level (capped below)
// src/map/skill.cpp:10732
else if(skill_lv==2) maxlv=1;
// src/map/skill.cpp:10733
else if(skill_lv==3) maxlv=2;
// src/map/skill.cpp:10734
else if(skill_lv>=4) maxlv=3;
// src/map/skill.cpp:10737
if(skill_lv==5) maxlv=1;
// src/map/skill.cpp:10738
else if(skill_lv==6) maxlv=2;
// src/map/skill.cpp:10739
else if(skill_lv>=7) maxlv=3;
// src/map/skill.cpp:10742
if(skill_lv==8) maxlv=1;
```

### Cold Bolt (`MG_COLDBOLT`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Water；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800; Lv6=2000; Lv7=2200; Lv8=2400; Lv9=2600; Lv10=2800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/homunculus/homunculus_caprice.cpp`, `src/map/skills/mage/coldbolt.cpp`, `src/map/skills/mage/hindsight.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6217
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6222
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6227
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6232
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:7737
skill_castend_pos2( src, target->x, target->y, skill_id, skill_lv, tick, flag );
// src/map/battle.cpp:7738
battle_autocast_aftercast( src, skill_id, skill_lv, tick );
// src/map/battle.cpp:7739
sd->state.autocast = 0;
// src/map/battle.cpp:7747
battle_autocast_elembuff_skill(sd, target, MG_FIREBOLT, tick, flag);
// src/map/battle.cpp:7749
battle_autocast_elembuff_skill(sd, target, MG_COLDBOLT, tick, flag);
// src/map/battle.cpp:7751
battle_autocast_elembuff_skill(sd, target, MG_LIGHTNINGBOLT, tick, flag);
// src/map/battle.cpp:7753
battle_autocast_elembuff_skill(sd, target, WZ_EARTHSPIKE, tick, flag);
// src/map/battle.cpp:7755
battle_autocast_elembuff_skill(sd, target, SO_POISON_BUSTER, tick, flag);
```

### Frost Diver (`MG_FROSTDIVER`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Water；吟唱：800 ms；技能后摇：1500 ms；持续时间2：Lv1=3000; Lv2=6000; Lv3=9000; Lv4=12000; Lv5=15000; Lv6=18000; Lv7=21000; Lv8=24000; Lv9=27000; Lv10-11=30000 ms；消耗/限制：SP Lv1=25; Lv2=24; Lv3=23; Lv4=22; Lv5=21; Lv6=20; Lv7=19; Lv8=18; Lv9=17; Lv10=16；关联状态：Freeze。

- 技能树最高等级：`10`
- 前置技能：MG_COLDBOLT Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/mage/frostdiver.cpp`, `src/map/skills/mage/frostnova.cpp`, `src/map/skills/mage/hindsight.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6217
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6222
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6227
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6232
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/skill.cpp:10733
else if(skill_lv==3) maxlv=2;
// src/map/skill.cpp:10734
else if(skill_lv>=4) maxlv=3;
// src/map/skill.cpp:10737
if(skill_lv==5) maxlv=1;
// src/map/skill.cpp:10738
else if(skill_lv==6) maxlv=2;
// src/map/skill.cpp:10739
else if(skill_lv>=7) maxlv=3;
// src/map/skill.cpp:10742
if(skill_lv==8) maxlv=1;
// src/map/skill.cpp:10743
else if(skill_lv>=9) maxlv=2;
// src/map/skill.cpp:10751
sc_start4(sd,sd,SC_AUTOSPELL,100,skill_lv,skill_id,maxlv,0,
```

### Stone Curse (`MG_STONECURSE`)

魔法技能；目标：敌方目标；最高等级 10；射程：2；命中类型：Single；段数：1；属性：Earth；吟唱：1000 ms；持续时间1：5000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=25; Lv2=24; Lv3=23; Lv4=22; Lv5=21; Lv6=20; Lv7=19; Lv8=18; Lv9=17; Lv10=16；道具 Red_Gemstone×1；关联状态：StoneWait。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/mage/skill_factory_mage.cpp`, `src/map/skills/mage/stonecurse.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/mage/skill_factory_mage.cpp:285
case PF_DOUBLECASTING:
// src/map/skills/mage/stonecurse.cpp:13
void SkillStoneCurse::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
// src/map/skills/mage/stonecurse.cpp:14
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/mage/stonecurse.cpp:16
status_change *tsc = status_get_sc(&*target);
```

### Fire Ball (`MG_FIREBALL`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Fire；范围：Lv1-10=2; Lv11=3；吟唱：Lv1-5=1500; Lv6-10=1000 ms；技能后摇：Lv1-5=1500; Lv6-10=1000 ms；伤害标记：Splash；消耗/限制：SP 25。

- 技能树最高等级：`10`
- 前置技能：MG_FIREBOLT Lv4
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/mage/fireball.cpp`, `src/map/skills/mage/hindsight.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:10732
else if(skill_lv==2) maxlv=1;
// src/map/skill.cpp:10733
else if(skill_lv==3) maxlv=2;
// src/map/skill.cpp:10734
else if(skill_lv>=4) maxlv=3;
// src/map/skill.cpp:10737
if(skill_lv==5) maxlv=1;
// src/map/skill.cpp:10738
else if(skill_lv==6) maxlv=2;
// src/map/skill.cpp:10739
else if(skill_lv>=7) maxlv=3;
// src/map/skill.cpp:10742
if(skill_lv==8) maxlv=1;
// src/map/skill.cpp:10743
else if(skill_lv>=9) maxlv=2;
// src/map/skill.cpp:10751
sc_start4(sd,sd,SC_AUTOSPELL,100,skill_lv,skill_id,maxlv,0,
// src/map/skill.cpp:10752
skill_get_time(SA_AUTOSPELL,skill_lv));
// src/map/skills/mage/fireball.cpp:8
SkillFireBall::SkillFireBall() : SkillImplRecursiveDamageSplash(MG_FIREBALL) {
// src/map/skills/mage/fireball.cpp:11
void SkillFireBall::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
```

### Fire Wall (`MG_FIREWALL`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Fire；击退：2；吟唱：Lv1=2000; Lv2=1850; Lv3=1700; Lv4=1550; Lv5=1400; Lv6=1250; Lv7=1100; Lv8=950; Lv9=800; Lv10=650 ms；持续时间1：Lv1=5000; Lv2=6000; Lv3=7000; Lv4=8000; Lv5=9000; Lv6=10000; Lv7=11000; Lv8=12000; Lv9=13000; Lv10=14000 ms；消耗/限制：SP 40。

- 技能树最高等级：`10`
- 前置技能：MG_FIREBALL Lv5, MG_SIGHT Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/mage/firewall.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6209
if(ad.damage<1)
// src/map/battle.cpp:6210
ad.damage=1;
// src/map/battle.cpp:6211
else if(sc) { //only applies when hit
// src/map/battle.cpp:6217
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6222
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6227
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6232
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/skill.cpp:1171
if (src->type == BL_MOB && skill_lv >= 10) {
// src/map/skill.cpp:1192
ShowError("skill_get_unit_layout: unknown unit layout for skill %d (level %d)\n", skill_id, skill_lv);
// src/map/skill.cpp:2619
void skill_attack_blow(block_list *src, block_list *dsrc, block_list *target, uint8 blewcount, uint16 skill_id, uint16 skill_lv, int64 damage, t_tick tick, int32 flag) {
// src/map/skill.cpp:2635
if(!battle_config.stormgust_knockback)
// src/map/skill.cpp:2639
if (battle_config.cart_revo_knockback)
```

### Fire Bolt (`MG_FIREBOLT`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Fire；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800; Lv6=2000; Lv7=2200; Lv8=2400; Lv9=2600; Lv10=2800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/homunculus/homunculus_caprice.cpp`, `src/map/skills/mage/firebolt.cpp`, `src/map/skills/mage/hindsight.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6209
if(ad.damage<1)
// src/map/battle.cpp:6210
ad.damage=1;
// src/map/battle.cpp:6211
else if(sc) { //only applies when hit
// src/map/battle.cpp:6217
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6222
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6227
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:7735
if( skill_lv > 0 && rnd_chance( 10, 100 ) ){
// src/map/battle.cpp:7736
sd->state.autocast = 1;
// src/map/battle.cpp:7737
skill_castend_pos2( src, target->x, target->y, skill_id, skill_lv, tick, flag );
// src/map/battle.cpp:7738
battle_autocast_aftercast( src, skill_id, skill_lv, tick );
// src/map/battle.cpp:7739
sd->state.autocast = 0;
// src/map/battle.cpp:7747
battle_autocast_elembuff_skill(sd, target, MG_FIREBOLT, tick, flag);
```

### Lightning Bolt (`MG_LIGHTNINGBOLT`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Wind；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800; Lv6=2000; Lv7=2200; Lv8=2400; Lv9=2600; Lv10=2800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/homunculus/homunculus_caprice.cpp`, `src/map/skills/mage/hindsight.cpp`, `src/map/skills/mage/lightningbolt.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6202
battle_calc_defense_reduction(&ad, src, target, skill_id, skill_lv);
// src/map/battle.cpp:6203
ad.damage -= (tstatus->mdef + tstatus->mdef2);
// src/map/battle.cpp:6209
if(ad.damage<1)
// src/map/battle.cpp:6210
ad.damage=1;
// src/map/battle.cpp:6211
else if(sc) { //only applies when hit
// src/map/battle.cpp:6217
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6222
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:7739
sd->state.autocast = 0;
// src/map/battle.cpp:7747
battle_autocast_elembuff_skill(sd, target, MG_FIREBOLT, tick, flag);
// src/map/battle.cpp:7749
battle_autocast_elembuff_skill(sd, target, MG_COLDBOLT, tick, flag);
// src/map/battle.cpp:7751
battle_autocast_elembuff_skill(sd, target, MG_LIGHTNINGBOLT, tick, flag);
// src/map/battle.cpp:7753
battle_autocast_elembuff_skill(sd, target, WZ_EARTHSPIKE, tick, flag);
```

### Thunderstorm (`MG_THUNDERSTORM`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Wind；吟唱：Lv1=1000; Lv2=2000; Lv3=3000; Lv4=4000; Lv5=5000; Lv6=6000; Lv7=7000; Lv8=8000; Lv9=9000; Lv10=10000 ms；技能后摇：2000 ms；持续时间1：100 ms；消耗/限制：SP Lv1=29; Lv2=34; Lv3=39; Lv4=44; Lv5=49; Lv6=54; Lv7=59; Lv8=64; Lv9=69; Lv10=74。

- 技能树最高等级：`10`
- 前置技能：MG_LIGHTNINGBOLT Lv4
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`, `src/map/skills/mage/thunderstorm.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:6203
ad.damage -= (tstatus->mdef + tstatus->mdef2);
// src/map/battle.cpp:6209
if(ad.damage<1)
// src/map/battle.cpp:6210
ad.damage=1;
// src/map/battle.cpp:6211
else if(sc) { //only applies when hit
// src/map/battle.cpp:6217
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6222
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/battle.cpp:6227
ad.damage += (6 + sstatus->int_ / 4) + max(sstatus->dex - 10, 0) / 30;
// src/map/skills/mage/skill_factory_mage.cpp:285
case PF_DOUBLECASTING:
// src/map/skills/mage/thunderstorm.cpp:9
void SkillThunderStorm::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/mage/thunderstorm.cpp:13
skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
// src/map/skills/mage/thunderstorm.cpp:16
void SkillThunderStorm::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
```

### Energy Coat (`MG_ENERGYCOAT`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：5000 ms；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP 30；关联状态：EnergyCoat。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/mage/energycoat.cpp`, `src/map/skills/mage/skill_factory_mage.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。
