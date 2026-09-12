# Merchant 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Merchant` 公式页](../skill-formulas/Merchant.md)

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 36 | `MC_INCCARRY` | Enlarge Weight Limit | 10 | Merchant | 是 | — | None / Passive |
| 37 | `MC_DISCOUNT` | Discount | 10 | Merchant | 是 | MC_INCCARRY Lv3 | None / Passive |
| 38 | `MC_OVERCHARGE` | Overcharge | 10 | Merchant | 是 | MC_DISCOUNT Lv3 | None / Passive |
| 39 | `MC_PUSHCART` | Pushcart | 10 | Merchant | 是 | MC_INCCARRY Lv5 | None / Passive |
| 40 | `MC_IDENTIFY` | Item Appraisal | 1 | Merchant | 是 | — | None / Self |
| 41 | `MC_VENDING` | Vending | 10 | Merchant | 是 | MC_PUSHCART Lv3 | None / Self |
| 42 | `MC_MAMMONITE` | Mammonite | 10 | Merchant | 是 | — | Weapon / Attack |
| 153 | `MC_CARTREVOLUTION` | Cart Revolution | 1 | Merchant | 是 | — | Weapon / Attack |
| 154 | `MC_CHANGECART` | Change Cart | 1 | Merchant | 是 | — | None / Self |
| 155 | `MC_LOUD` | Crazy Uproar | 1 | Merchant | 是 | — | Weapon / Self |
| 2535 | `ALL_BUYING_STORE` | Open Buying Store | 1 | Merchant | 是 | MC_VENDING Lv1 | None / Self |
| 2544 | `MC_CARTDECORATE` | Decorate Cart | 1 | Merchant | 是 | — | None / Self |

## 技能详情

### Enlarge Weight Limit (`MC_INCCARRY`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/status.cpp`

> 此技能没有独立伤害表达式；效果由技能元数据、状态数据库、物品脚本或通用战斗管线驱动。

### Discount (`MC_DISCOUNT`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：MC_INCCARRY Lv3
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:5691
int32 skill,val = orig_value,rate1 = 0,rate2 = 0;
// src/map/pc.cpp:5693
rate1 = 5+skill*2-((skill==10)? 1:0);
// src/map/pc.cpp:5695
rate2 = 5+skill*4;
// src/map/pc.cpp:5696
if(rate1 < rate2) rate1 = rate2;
// src/map/pc.cpp:5697
if(rate1)
// src/map/pc.cpp:5698
val = (int32)((double)orig_value*(double)(100-rate1)/100.);
```

### Overcharge (`MC_OVERCHARGE`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：MC_DISCOUNT Lv3
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:5710
int32 skill,val = orig_value,rate = 0;
// src/map/pc.cpp:5712
rate = 5+skill*2-((skill==10)? 1:0);
// src/map/pc.cpp:5713
if(rate)
// src/map/pc.cpp:5714
val = (int32)((double)orig_value*(double)(100+rate)/100.);
```

### Pushcart (`MC_PUSHCART`)

非伤害技能；目标：被动；最高等级 10；射程：1。

- 技能树最高等级：`10`
- 前置技能：MC_INCCARRY Lv5
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:11047
status_change_end(sd, SC_SPRITEMABLE);
// src/map/pc.cpp:11049
status_change_end(sd, SC_SOULATTACK);
// src/map/pc.cpp:11279
status_change_end(sd,SC_PUSH_CART);
// src/map/pc.cpp:11288
sc_start(sd, sd, SC_PUSH_CART, 100, type, 0);
// src/map/status.cpp:8199
if( sd && sd->bonus.speed_rate + sd->bonus.speed_add_rate < 0 ) // Permanent item-based speedup
// src/map/status.cpp:8200
val = max( val, -(sd->bonus.speed_rate + sd->bonus.speed_add_rate) );
// src/map/status.cpp:8202
speed_rate -= val;
// src/map/status.cpp:8204
if( speed_rate < 40 )
// src/map/status.cpp:8205
speed_rate = 40;
// src/map/status.cpp:8213
if( speed_rate != 100 )
// src/map/status.cpp:8214
speed = speed * speed_rate / 100;
```

### Item Appraisal (`MC_IDENTIFY`)

非伤害技能；目标：自身；最高等级 1；射程：1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 10。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/itemappraisal.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

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
// src/map/skill.cpp:9687
if (require.hp || require.sp || require.ap)
// src/map/skill.cpp:9688
skill_consume_hpspap(sd, skill_id, require.hp, require.sp, require.ap);
// src/map/skill.cpp:9692
status_change *sc = &sd->sc;
// src/map/skills/merchant/itemappraisal.cpp:13
void SkillItemAppraisal::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/itemappraisal.cpp:14
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/skill_factory_merchant.cpp:266
case MC_CARTDECORATE:
// src/map/skills/merchant/skill_factory_merchant.cpp:267
return std::make_unique<SkillDecorateCart>();
```

### Vending (`MC_VENDING`)

非伤害技能；目标：自身；最高等级 10；射程：1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 30；状态 Cart。

- 技能树最高等级：`10`
- 前置技能：MC_PUSHCART Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/skills/merchant/skill_vending.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:892
return false; // gonna be checked in 'skill_castend_nodamage_id'
// src/map/skills/merchant/skill_factory_merchant.cpp:266
case MC_CARTDECORATE:
// src/map/skills/merchant/skill_factory_merchant.cpp:267
return std::make_unique<SkillDecorateCart>();
// src/map/skills/merchant/skill_vending.cpp:12
void SkillVending::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/skill_vending.cpp:13
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/skill_vending.cpp:22
sd->vend_skill_lv = skill_lv;
```

### Mammonite (`MC_MAMMONITE`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-1；命中类型：Single；段数：1；属性：Weapon；消耗/限制：SP 5；Zeny Lv1=100; Lv2=200; Lv3=300; Lv4=400; Lv5=500; Lv6=600; Lv7=700; Lv8=800; Lv9=900; Lv10=1000。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/mammonite.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/mammonite.cpp:9
void SkillMammonite::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
// src/map/skills/merchant/mammonite.cpp:10
base_skillratio += 50 * skill_lv;
// src/map/skills/merchant/skill_factory_merchant.cpp:266
case MC_CARTDECORATE:
// src/map/skills/merchant/skill_factory_merchant.cpp:267
return std::make_unique<SkillDecorateCart>();
```

### Cart Revolution (`MC_CARTREVOLUTION`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：1；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：2；伤害标记：Splash；消耗/限制：SP 12；状态 Cart。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/merchant/cartrevolution.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:3698
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3700
wd->damage2 = battle_attr_fix(src, target, wd->damage2, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3804
wd->damage2 = battle_addmastery(sd,target,wd->damage2,1);
// src/map/battle.cpp:3812
if(skill_id == TF_POISON) //Additional ATK from Envenom is treated as mastery type damage [helvetica]
// src/map/battle.cpp:3813
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, 15 * skill_lv);
// src/map/battle.cpp:3819
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, battle_get_spiritball_damage(*wd, *src, skill_id));
// src/map/battle.cpp:3822
ATK_ADD(wd->damage, wd->damage2, 3 * skill);
// src/map/battle.cpp:5715
wd.damage = 0;
// src/map/battle.cpp:5724
ATK_ADD(wd.damage, wd.damage2, skill * 2);
// src/map/battle.cpp:5726
ATK_ADD(wd.damage, wd.damage2, 50 * skill_lv);
// src/map/battle.cpp:5728
ATK_ADD(wd.damage, wd.damage2, 4);
// src/map/battle.cpp:5735
wd.damage = wd.damage * (100 + sd->bonus.long_attack_atk_rate) / 100;
```

### Change Cart (`MC_CHANGECART`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 40；状态 Cart。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/changecart.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/changecart.cpp:11
void SkillChangeCart::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/changecart.cpp:12
clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
// src/map/skills/merchant/skill_factory_merchant.cpp:266
case MC_CARTDECORATE:
// src/map/skills/merchant/skill_factory_merchant.cpp:267
return std::make_unique<SkillDecorateCart>();
```

### Crazy Uproar (`MC_LOUD`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP 8；关联状态：Loud。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/crazyuproar.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/crazyuproar.cpp:15
void SkillCrazyUproar::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/crazyuproar.cpp:16
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/crazyuproar.cpp:20
StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
// src/map/skills/merchant/crazyuproar.cpp:22
party_foreachsamemap(skill_area_sub, sd, skill_get_splash(getSkillId(), skill_lv), src, getSkillId(), skill_lv, tick, flag | BCT_PARTY | 1, skill_castend_nodamage_id);
// src/map/skills/merchant/skill_factory_merchant.cpp:266
case MC_CARTDECORATE:
// src/map/skills/merchant/skill_factory_merchant.cpp:267
return std::make_unique<SkillDecorateCart>();
```

### Open Buying Store (`ALL_BUYING_STORE`)

非伤害技能；目标：自身；最高等级 1；伤害标记：NoDamage；消耗/限制：SP 1；道具 Buy_Market_Permit×1。

- 技能树最高等级：`1`
- 前置技能：MC_VENDING Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/other/openbuyingstore.cpp`, `src/map/skills/other/skill_factory_other.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/other/openbuyingstore.cpp:12
void SkillOpenBuyingStore::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/other/openbuyingstore.cpp:13
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/other/openbuyingstore.cpp:17
clif_skill_nodamage(src, *target, getSkillId(), skill_lv, buyingstore_setup(sd, MAX_BUYINGSTORE_SLOTS) == 0);
```

### Decorate Cart (`MC_CARTDECORATE`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 40；状态 Cart。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/decoratecart.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/decoratecart.cpp:4
#include "decoratecart.hpp"
// src/map/skills/merchant/decoratecart.cpp:9
SkillDecorateCart::SkillDecorateCart() : SkillImpl(MC_CARTDECORATE) {
// src/map/skills/merchant/decoratecart.cpp:12
void SkillDecorateCart::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/decoratecart.cpp:13
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/decoratecart.cpp:14
clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
// src/map/skills/merchant/skill_factory_merchant.cpp:266
case MC_CARTDECORATE:
// src/map/skills/merchant/skill_factory_merchant.cpp:267
return std::make_unique<SkillDecorateCart>();
```
