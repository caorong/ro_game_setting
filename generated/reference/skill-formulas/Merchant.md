# Merchant 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 36 | `MC_INCCARRY` / Enlarge Weight Limit | `core-source-references` | `` | src/map/status.cpp |
| 37 | `MC_DISCOUNT` / Discount | `core-source-references` | `` | src/map/pc.cpp |
| 38 | `MC_OVERCHARGE` / Overcharge | `core-source-references` | `` | src/map/pc.cpp |
| 39 | `MC_PUSHCART` / Pushcart | `core-source-references` | `` | src/map/pc.cpp, src/map/status.cpp |
| 40 | `MC_IDENTIFY` / Item Appraisal | `exact-class-methods` | `SkillItemAppraisal` | src/map/skills/merchant/itemappraisal.cpp |
| 41 | `MC_VENDING` / Vending | `exact-class-methods` | `SkillVending` | src/map/skills/merchant/skill_vending.cpp |
| 42 | `MC_MAMMONITE` / Mammonite | `exact-class-methods` | `SkillMammonite` | src/map/skills/merchant/mammonite.cpp |
| 153 | `MC_CARTREVOLUTION` / Cart Revolution | `exact-class-methods` | `SkillCartRevolution` | src/map/skills/merchant/cartrevolution.cpp |
| 154 | `MC_CHANGECART` / Change Cart | `exact-class-methods` | `SkillChangeCart` | src/map/skills/merchant/changecart.cpp |
| 155 | `MC_LOUD` / Crazy Uproar | `exact-class-methods` | `SkillCrazyUproar` | src/map/skills/merchant/crazyuproar.cpp |
| 2535 | `ALL_BUYING_STORE` / Open Buying Store | `exact-class-methods` | `SkillOpenBuyingStore` | src/map/skills/other/openbuyingstore.cpp |
| 2544 | `MC_CARTDECORATE` / Decorate Cart | `exact-class-methods` | `SkillDecorateCart` | src/map/skills/merchant/decoratecart.cpp |

## 详细公式与效果实现

### Enlarge Weight Limit (`MC_INCCARRY`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Discount (`MC_DISCOUNT`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`

精确源码候选（该技能没有独立实现类）：

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

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`

精确源码候选（该技能没有独立实现类）：

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

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

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

- 覆盖：`exact-class-methods`
- 实现类：`SkillItemAppraisal`
- 实现文件：`src/map/skills/merchant/itemappraisal.cpp`

#### `SkillItemAppraisal::SkillItemAppraisal`

来源：`src/map/skills/merchant/itemappraisal.cpp:10-11`

```cpp
SkillItemAppraisal::SkillItemAppraisal() : SkillImpl(MC_IDENTIFY) {
}
```

#### `SkillItemAppraisal::castendNoDamageId`

来源：`src/map/skills/merchant/itemappraisal.cpp:13-24`

```cpp
void SkillItemAppraisal::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);

	if (sd) {
		clif_item_identify_list(sd);
		if (sd->menuskill_id != getSkillId()) {
			// failed, dont consume anything
			flag |= SKILL_NOCONSUME_REQ;
			return;
		}
	}
}
```

### Vending (`MC_VENDING`)

非伤害技能；目标：自身；最高等级 10；射程：1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 30；状态 Cart。

- 覆盖：`exact-class-methods`
- 实现类：`SkillVending`
- 实现文件：`src/map/skills/merchant/skill_vending.cpp`

#### `SkillVending::SkillVending`

来源：`src/map/skills/merchant/skill_vending.cpp:9-10`

```cpp
SkillVending::SkillVending() : SkillImpl(MC_VENDING) {
}
```

#### `SkillVending::castendNoDamageId`

来源：`src/map/skills/merchant/skill_vending.cpp:12-35`

```cpp
void SkillVending::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	if (sd) {
		// Prevent vending of GMs with unnecessary Level to trade/drop. [Skotlex]
		if (!pc_can_give_items(sd))
			clif_skill_fail(*sd, MC_VENDING);
		else {
			int32 i = 0;
			sd->state.prevend = 1;
			sd->state.workinprogress = WIP_DISABLE_ALL;
			sd->vend_skill_lv = skill_lv;
			ARR_FIND(0, MAX_CART, i, sd->cart.u.items_cart[i].nameid && sd->cart.u.items_cart[i].id == 0);
			if (i < MAX_CART) {
				// Save the cart before opening the vending UI
				sd->state.pending_vending_ui = true;
				intif_storage_save(sd, &sd->cart);
			} else {
				// Instantly open the vending UI
				sd->state.pending_vending_ui = false;
				clif_openvendingreq(*sd, 2 + skill_lv);
			}
		}
	}
}
```

### Mammonite (`MC_MAMMONITE`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-1；命中类型：Single；段数：1；属性：Weapon；消耗/限制：SP 5；Zeny Lv1=100; Lv2=200; Lv3=300; Lv4=400; Lv5=500; Lv6=600; Lv7=700; Lv8=800; Lv9=900; Lv10=1000。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMammonite`
- 实现文件：`src/map/skills/merchant/mammonite.cpp`

#### `SkillMammonite::SkillMammonite`

来源：`src/map/skills/merchant/mammonite.cpp:6-7`

```cpp
SkillMammonite::SkillMammonite() : WeaponSkillImpl(MC_MAMMONITE) {
}
```

#### `SkillMammonite::calculateSkillRatio`

来源：`src/map/skills/merchant/mammonite.cpp:9-11`

```cpp
void SkillMammonite::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += 50 * skill_lv;
}
```

### Cart Revolution (`MC_CARTREVOLUTION`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：1；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：2；伤害标记：Splash；消耗/限制：SP 12；状态 Cart。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCartRevolution`
- 实现文件：`src/map/skills/merchant/cartrevolution.cpp`

#### `SkillCartRevolution::SkillCartRevolution`

来源：`src/map/skills/merchant/cartrevolution.cpp:8-9`

```cpp
SkillCartRevolution::SkillCartRevolution() : SkillImplRecursiveDamageSplash(MC_CARTREVOLUTION) {
}
```

#### `SkillCartRevolution::calculateSkillRatio`

来源：`src/map/skills/merchant/cartrevolution.cpp:11-18`

```cpp
void SkillCartRevolution::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const map_session_data *sd = BL_CAST(BL_PC, src);
	base_skillratio += 50;
	if (sd && sd->cart_weight)
		base_skillratio += 100 * sd->cart_weight / sd->cart_weight_max; // +1% every 1% weight
	else if (!sd)
		base_skillratio += 100; // Max damage for non players.
}
```

#### `SkillCartRevolution::modifyHitRate`

来源：`src/map/skills/merchant/cartrevolution.cpp:20-25`

```cpp
void SkillCartRevolution::modifyHitRate(int16 &hit_rate, const block_list *src, const block_list *target, uint16 skill_lv) const {
	const map_session_data *sd = BL_CAST(BL_PC, src);

	if (sd && pc_checkskill(sd, GN_REMODELING_CART))
		hit_rate += pc_checkskill(sd, GN_REMODELING_CART) * 4;
}
```

#### `SkillCartRevolution::castendDamageId`

来源：`src/map/skills/merchant/cartrevolution.cpp:27-31`

```cpp
void SkillCartRevolution::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag |= SD_PREAMBLE; // a fake packet will be sent for the first target to be hit

	SkillImplRecursiveDamageSplash::castendDamageId(src, target, skill_lv, tick, flag);
}
```

### Change Cart (`MC_CHANGECART`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 40；状态 Cart。

- 覆盖：`exact-class-methods`
- 实现类：`SkillChangeCart`
- 实现文件：`src/map/skills/merchant/changecart.cpp`

#### `SkillChangeCart::SkillChangeCart`

来源：`src/map/skills/merchant/changecart.cpp:8-9`

```cpp
SkillChangeCart::SkillChangeCart() : SkillImpl(MC_CHANGECART) {
}
```

#### `SkillChangeCart::castendNoDamageId`

来源：`src/map/skills/merchant/changecart.cpp:11-13`

```cpp
void SkillChangeCart::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
}
```

### Crazy Uproar (`MC_LOUD`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP 8；关联状态：Loud。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCrazyUproar`
- 实现文件：`src/map/skills/merchant/crazyuproar.cpp`

#### `SkillCrazyUproar::SkillCrazyUproar`

来源：`src/map/skills/merchant/crazyuproar.cpp:11-12`

```cpp
SkillCrazyUproar::SkillCrazyUproar() : StatusSkillImpl(MC_LOUD) {
}
```

#### `SkillCrazyUproar::castendNoDamageId`

来源：`src/map/skills/merchant/crazyuproar.cpp:15-24`

```cpp
void SkillCrazyUproar::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	sc_type type = skill_get_sc(getSkillId());

	if (sd == nullptr || sd->status.party_id == 0 || (flag & 1)) {
		StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
	} else if (sd) {
		party_foreachsamemap(skill_area_sub, sd, skill_get_splash(getSkillId(), skill_lv), src, getSkillId(), skill_lv, tick, flag | BCT_PARTY | 1, skill_castend_nodamage_id);
	}
}
```

### Open Buying Store (`ALL_BUYING_STORE`)

非伤害技能；目标：自身；最高等级 1；伤害标记：NoDamage；消耗/限制：SP 1；道具 Buy_Market_Permit×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillOpenBuyingStore`
- 实现文件：`src/map/skills/other/openbuyingstore.cpp`

#### `SkillOpenBuyingStore::SkillOpenBuyingStore`

来源：`src/map/skills/other/openbuyingstore.cpp:9-10`

```cpp
SkillOpenBuyingStore::SkillOpenBuyingStore() : SkillImpl(ALL_BUYING_STORE) {
}
```

#### `SkillOpenBuyingStore::castendNoDamageId`

来源：`src/map/skills/other/openbuyingstore.cpp:12-19`

```cpp
void SkillOpenBuyingStore::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if( sd )
	{// players only, skill allows 5 buying slots
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv, buyingstore_setup(sd, MAX_BUYINGSTORE_SLOTS) == 0);
	}
}
```

### Decorate Cart (`MC_CARTDECORATE`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 40；状态 Cart。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDecorateCart`
- 实现文件：`src/map/skills/merchant/decoratecart.cpp`

#### `SkillDecorateCart::SkillDecorateCart`

来源：`src/map/skills/merchant/decoratecart.cpp:9-10`

```cpp
SkillDecorateCart::SkillDecorateCart() : SkillImpl(MC_CARTDECORATE) {
}
```

#### `SkillDecorateCart::castendNoDamageId`

来源：`src/map/skills/merchant/decoratecart.cpp:12-18`

```cpp
void SkillDecorateCart::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
	if (sd) {
		clif_SelectCart(sd);
	}
}
```
