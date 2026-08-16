# Hunter 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 115 | `HT_SKIDTRAP` / Skid Trap | `exact-class-methods` | `SkillSkidTrap` | src/map/skills/archer/skidtrap.cpp |
| 116 | `HT_LANDMINE` / Land Mine | `exact-class-methods` | `SkillLandMine` | src/map/skills/archer/landmine.cpp |
| 117 | `HT_ANKLESNARE` / Ankle Snare | `exact-class-methods` | `SkillAnkleSnare` | src/map/skills/archer/anklesnare.cpp |
| 118 | `HT_SHOCKWAVE` / Shockwave Trap | `exact-class-methods` | `SkillShockwaveTrap` | src/map/skills/archer/shockwavetrap.cpp |
| 119 | `HT_SANDMAN` / Sandman | `exact-class-methods` | `SkillSandman` | src/map/skills/archer/sandman.cpp |
| 120 | `HT_FLASHER` / Flasher | `exact-class-methods` | `SkillFlasher` | src/map/skills/archer/flasher.cpp |
| 121 | `HT_FREEZINGTRAP` / Freezing Trap | `exact-class-methods` | `SkillFreezingTrap` | src/map/skills/archer/freezingtrap.cpp |
| 122 | `HT_BLASTMINE` / Blast Mine | `exact-class-methods` | `SkillBlastMine` | src/map/skills/archer/blastmine.cpp |
| 123 | `HT_CLAYMORETRAP` / Claymore Trap | `exact-class-methods` | `SkillClaymoreTrap` | src/map/skills/archer/claymoretrap.cpp |
| 124 | `HT_REMOVETRAP` / Remove Trap | `exact-class-methods` | `SkillRemoveTrap` | src/map/skills/archer/removetrap.cpp |
| 125 | `HT_TALKIEBOX` / Talkie Box | `exact-class-methods` | `SkillTalkieBox` | src/map/skills/archer/talkiebox.cpp |
| 126 | `HT_BEASTBANE` / Beast Bane | `core-source-references` | `` | src/map/battle.cpp |
| 127 | `HT_FALCON` / Falconry Mastery | `core-source-references` | `` | src/map/pc.cpp |
| 128 | `HT_STEELCROW` / Steel Crow | `core-source-references` | `` | src/map/battle.cpp, src/map/skills/archer/wildwalk.cpp |
| 129 | `HT_BLITZBEAT` / Blitz Beat | `exact-class-methods` | `SkillBlitzBeat` | src/map/skills/archer/blitzbeat.cpp |
| 130 | `HT_DETECTING` / Detect | `exact-class-methods` | `SkillDetect` | src/map/skills/archer/detect.cpp |
| 131 | `HT_SPRINGTRAP` / Spring Trap | `exact-class-methods` | `SkillSpringTrap` | src/map/skills/archer/springtrap.cpp |
| 1009 | `HT_PHANTASMIC` / Phantasmic Arrow | `exact-class-methods` | `SkillPhantasmicArrow` | src/map/skills/archer/phantasmicarrow.cpp |
| 499 | `HT_POWER` / Beast Strafing | `exact-class-methods` | `SkillBeastStrafing` | src/map/skills/archer/beaststrafing.cpp |

## 详细公式与效果实现

### Skid Trap (`HT_SKIDTRAP`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；击退：Lv1=6; Lv2=7; Lv3=8; Lv4=9; Lv5=10；持续时间1：Lv1=300000; Lv2=240000; Lv3=180000; Lv4=120000; Lv5=60000 ms；伤害标记：NoDamage；消耗/限制：SP 10；道具 Booby_Trap×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSkidTrap`
- 实现文件：`src/map/skills/archer/skidtrap.cpp`

#### `SkillSkidTrap::SkillSkidTrap`

来源：`src/map/skills/archer/skidtrap.cpp:6-7`

```cpp
SkillSkidTrap::SkillSkidTrap() : SkillImpl(HT_SKIDTRAP) {
}
```

#### `SkillSkidTrap::castendPos2`

来源：`src/map/skills/archer/skidtrap.cpp:9-14`

```cpp
void SkillSkidTrap::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Land Mine (`HT_LANDMINE`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；属性：Earth；持续时间1：Lv1=200000; Lv2=160000; Lv3=120000; Lv4=80000; Lv5=40000 ms；持续时间2：5000 ms；伤害标记：IgnoreFlee, IgnoreDefCard；消耗/限制：SP 10；道具 Booby_Trap×1；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillLandMine`
- 实现文件：`src/map/skills/archer/landmine.cpp`

#### `SkillLandMine::SkillLandMine`

来源：`src/map/skills/archer/landmine.cpp:8-9`

```cpp
SkillLandMine::SkillLandMine() : SkillImpl(HT_LANDMINE) {
}
```

#### `SkillLandMine::castendPos2`

来源：`src/map/skills/archer/landmine.cpp:11-16`

```cpp
void SkillLandMine::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	// Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillLandMine::applyAdditionalEffects`

来源：`src/map/skills/archer/landmine.cpp:18-20`

```cpp
void SkillLandMine::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src, target, SC_STUN, 10, skill_lv, skill_get_time2(getSkillId(), skill_lv), 1000);
}
```

### Ankle Snare (`HT_ANKLESNARE`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；持续时间1：Lv1=250000; Lv2=200000; Lv3=150000; Lv4=100000; Lv5=50000 ms；持续时间2：Lv1=4000; Lv2=8000; Lv3=12000; Lv4=16000; Lv5=20000 ms；伤害标记：NoDamage；消耗/限制：SP 12；道具 Booby_Trap×1；关联状态：Ankle。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAnkleSnare`
- 实现文件：`src/map/skills/archer/anklesnare.cpp`

#### `SkillAnkleSnare::SkillAnkleSnare`

来源：`src/map/skills/archer/anklesnare.cpp:6-7`

```cpp
SkillAnkleSnare::SkillAnkleSnare() : SkillImpl(HT_ANKLESNARE) {
}
```

#### `SkillAnkleSnare::castendPos2`

来源：`src/map/skills/archer/anklesnare.cpp:9-14`

```cpp
void SkillAnkleSnare::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Shockwave Trap (`HT_SHOCKWAVE`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；持续时间1：Lv1=200000; Lv2=160000; Lv3=120000; Lv4=80000; Lv5=40000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 45；道具 Booby_Trap×2。

- 覆盖：`exact-class-methods`
- 实现类：`SkillShockwaveTrap`
- 实现文件：`src/map/skills/archer/shockwavetrap.cpp`

#### `SkillShockwaveTrap::SkillShockwaveTrap`

来源：`src/map/skills/archer/shockwavetrap.cpp:8-9`

```cpp
SkillShockwaveTrap::SkillShockwaveTrap() : SkillImpl(HT_SHOCKWAVE) {
}
```

#### `SkillShockwaveTrap::castendPos2`

来源：`src/map/skills/archer/shockwavetrap.cpp:11-16`

```cpp
void SkillShockwaveTrap::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillShockwaveTrap::applyAdditionalEffects`

来源：`src/map/skills/archer/shockwavetrap.cpp:18-20`

```cpp
void SkillShockwaveTrap::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	status_percent_damage(src, target, 0, -(15*skill_lv+5), false);
}
```

### Sandman (`HT_SANDMAN`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；范围：2；持续时间1：Lv1=150000; Lv2=120000; Lv3=90000; Lv4=60000; Lv5=30000 ms；持续时间2：30000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 12；道具 Booby_Trap×1；关联状态：Sleep。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSandman`
- 实现文件：`src/map/skills/archer/sandman.cpp`

#### `SkillSandman::SkillSandman`

来源：`src/map/skills/archer/sandman.cpp:8-9`

```cpp
SkillSandman::SkillSandman() : SkillImpl(HT_SANDMAN) {
}
```

#### `SkillSandman::castendPos2`

来源：`src/map/skills/archer/sandman.cpp:11-16`

```cpp
void SkillSandman::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	// Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillSandman::applyAdditionalEffects`

来源：`src/map/skills/archer/sandman.cpp:18-20`

```cpp
void SkillSandman::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src, target, SC_SLEEP, (10 * skill_lv + 40), skill_lv, skill_get_time2(getSkillId(), skill_lv), 1000);
}
```

### Flasher (`HT_FLASHER`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；持续时间1：Lv1=150000; Lv2=120000; Lv3=90000; Lv4=60000; Lv5=30000 ms；持续时间2：30000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 12；道具 Booby_Trap×1；关联状态：Blind。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFlasher`
- 实现文件：`src/map/skills/archer/flasher.cpp`

#### `SkillFlasher::SkillFlasher`

来源：`src/map/skills/archer/flasher.cpp:8-9`

```cpp
SkillFlasher::SkillFlasher() : SkillImpl(HT_FLASHER) {
}
```

#### `SkillFlasher::castendPos2`

来源：`src/map/skills/archer/flasher.cpp:11-16`

```cpp
void SkillFlasher::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	// Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillFlasher::applyAdditionalEffects`

来源：`src/map/skills/archer/flasher.cpp:18-20`

```cpp
void SkillFlasher::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src, target, SC_BLIND, 100, skill_lv, skill_get_time2(getSkillId(), skill_lv), 1000);
}
```

### Freezing Trap (`HT_FREEZINGTRAP`)

武器/物理技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；属性：Water；范围：1；持续时间1：Lv1=150000; Lv2=120000; Lv3=90000; Lv4=60000; Lv5=30000 ms；持续时间2：Lv1=3000; Lv2=6000; Lv3=9000; Lv4=12000; Lv5=15000 ms；伤害标记：Splash, IgnoreAtkCard；消耗/限制：SP 10；道具 Booby_Trap×1；关联状态：Freeze。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFreezingTrap`
- 实现文件：`src/map/skills/archer/freezingtrap.cpp`

#### `SkillFreezingTrap::SkillFreezingTrap`

来源：`src/map/skills/archer/freezingtrap.cpp:8-9`

```cpp
SkillFreezingTrap::SkillFreezingTrap() : SkillImpl(HT_FREEZINGTRAP) {
}
```

#### `SkillFreezingTrap::castendPos2`

来源：`src/map/skills/archer/freezingtrap.cpp:11-16`

```cpp
void SkillFreezingTrap::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	// Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillFreezingTrap::applyAdditionalEffects`

来源：`src/map/skills/archer/freezingtrap.cpp:18-22`

```cpp
void SkillFreezingTrap::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	status_data* sstatus = status_get_status_data(*src);

	sc_start(src, target, SC_FREEZE, 100, skill_lv, skill_get_time2(getSkillId(), skill_lv), sstatus->amotion + 100);
}
```

### Blast Mine (`HT_BLASTMINE`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；属性：Wind；范围：1；持续时间1：Lv1=25000; Lv2=20000; Lv3=15000; Lv4=10000; Lv5=5000 ms；伤害标记：Splash, IgnoreFlee, IgnoreDefCard；消耗/限制：SP 10；道具 Booby_Trap×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBlastMine`
- 实现文件：`src/map/skills/archer/blastmine.cpp`

#### `SkillBlastMine::SkillBlastMine`

来源：`src/map/skills/archer/blastmine.cpp:6-7`

```cpp
SkillBlastMine::SkillBlastMine() : SkillImpl(HT_BLASTMINE) {
}
```

#### `SkillBlastMine::castendPos2`

来源：`src/map/skills/archer/blastmine.cpp:9-14`

```cpp
void SkillBlastMine::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	// Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Claymore Trap (`HT_CLAYMORETRAP`)

特殊技能；目标：地面区域；最高等级 5；射程：3；命中类型：Single；段数：1；属性：Fire；范围：2；持续时间1：Lv1=20000; Lv2=40000; Lv3=60000; Lv4=80000; Lv5=100000 ms；伤害标记：Splash, IgnoreFlee, IgnoreDefCard；消耗/限制：SP 15；道具 Booby_Trap×2。

- 覆盖：`exact-class-methods`
- 实现类：`SkillClaymoreTrap`
- 实现文件：`src/map/skills/archer/claymoretrap.cpp`

#### `SkillClaymoreTrap::SkillClaymoreTrap`

来源：`src/map/skills/archer/claymoretrap.cpp:6-7`

```cpp
SkillClaymoreTrap::SkillClaymoreTrap() : SkillImpl(HT_CLAYMORETRAP) {
}
```

#### `SkillClaymoreTrap::castendPos2`

来源：`src/map/skills/archer/claymoretrap.cpp:9-14`

```cpp
void SkillClaymoreTrap::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	// Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Remove Trap (`HT_REMOVETRAP`)

特殊技能；目标：陷阱；最高等级 1；射程：2；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 5。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRemoveTrap`
- 实现文件：`src/map/skills/archer/removetrap.cpp`

#### `SkillRemoveTrap::SkillRemoveTrap`

来源：`src/map/skills/archer/removetrap.cpp:10-11`

```cpp
SkillRemoveTrap::SkillRemoveTrap() : SkillImpl(HT_REMOVETRAP) {
}
```

#### `SkillRemoveTrap::castendNoDamageId`

来源：`src/map/skills/archer/removetrap.cpp:13-67`

```cpp
void SkillRemoveTrap::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if( sd == nullptr ){
		return;
	}

	skill_unit* su = BL_CAST(BL_SKILL, target);
	std::shared_ptr<s_skill_unit_group> sg;
	std::shared_ptr<s_skill_db> skill_group;

	// Players can only remove their own traps or traps on Vs maps.
	if( su && (sg = su->group) && (sg->src_id == src->id || map_flag_vs(target->m)) && ( skill_group = skill_db.find(sg->skill_id) ) && skill_group->inf2[INF2_ISTRAP] )
	{
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
		if( !(sg->unit_id == UNT_USED_TRAPS || (sg->unit_id == UNT_ANKLESNARE && sg->val2 != 0 )) )
		{ // prevent picking up expired traps
			if( battle_config.skill_removetrap_type )
			{ // get back all items used to deploy the trap
				for( int32 i = 0; i < MAX_SKILL_ITEM_REQUIRE; i++ )
				{
					if( skill_group->require.itemid[i] > 0 )
					{
						int32 flag2;
						struct item item_tmp;
						memset(&item_tmp,0,sizeof(item_tmp));
						item_tmp.nameid = skill_group->require.itemid[i];
						item_tmp.identify = 1;
						item_tmp.amount = skill_group->require.amount[i];
						if( item_tmp.nameid && (flag2=pc_additem(sd,&item_tmp,item_tmp.amount,LOG_TYPE_OTHER)) ){
							clif_additem(sd,0,0,flag2);
							if (battle_config.skill_drop_items_full)
								map_addflooritem(&item_tmp,item_tmp.amount,sd->m,sd->x,sd->y,0,0,0,4,0);
						}
					}
				}
			}
			else
			{ // get back 1 trap
				struct item item_tmp;
				memset(&item_tmp,0,sizeof(item_tmp));
				item_tmp.nameid = su->group->item_id?su->group->item_id:ITEMID_TRAP;
				item_tmp.identify = 1;
				if( item_tmp.nameid && (flag=pc_additem(sd,&item_tmp,1,LOG_TYPE_OTHER)) )
				{
					clif_additem(sd,0,0,flag);
					if (battle_config.skill_drop_items_full)
						map_addflooritem(&item_tmp,1,sd->m,sd->x,sd->y,0,0,0,4,0);
				}
			}
		}
		skill_delunit(su);
	}else
		clif_skill_fail( *sd, getSkillId() );
}
```

### Talkie Box (`HT_TALKIEBOX`)

特殊技能；目标：地面区域；最高等级 1；射程：3；命中类型：Single；段数：1；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 1；道具 Booby_Trap×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillTalkieBox`
- 实现文件：`src/map/skills/archer/talkiebox.cpp`

#### `SkillTalkieBox::SkillTalkieBox`

来源：`src/map/skills/archer/talkiebox.cpp:6-7`

```cpp
SkillTalkieBox::SkillTalkieBox() : SkillImpl(HT_TALKIEBOX) {
}
```

#### `SkillTalkieBox::castendPos2`

来源：`src/map/skills/archer/talkiebox.cpp:9-14`

```cpp
void SkillTalkieBox::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	// Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Beast Bane (`HT_BEASTBANE`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2294
damage += static_cast<decltype(damage)>(skill * (sd->status.base_level / 20.0 + 3.0));
// src/map/battle.cpp:2296
damage += (skill * 5);
// src/map/battle.cpp:2298
damage += (skill * 10);
// src/map/battle.cpp:2300
damage += (15 * pc_checkskill(sd, NC_MADOLICENCE)); // Attack bonus is granted even without the Madogear
// src/map/battle.cpp:2303
damage += (skill * 4);
// src/map/battle.cpp:2305
damage += sd->status.str;
// src/map/battle.cpp:2311
damage += (skill * 2);
```

### Falconry Mastery (`HT_FALCON`)

特殊技能；目标：被动；最高等级 1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Steel Crow (`HT_STEELCROW`)

特殊技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/archer/wildwalk.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:6368
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex / 2.0 + 50.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6371
md.damage = static_cast<decltype(md.damage)>(skill_lv * (sstatus->dex / 2.0 + 75.0) * (100.0 + sstatus->int_) / 100.0);
// src/map/battle.cpp:6383
md.damage = skill_lv * 20 + skill * 6 + ((sstatus->agi / 2) *2) + ((sstatus->dex / 10) *2);
// src/map/battle.cpp:6385
md.damage = (sstatus->dex / 10 + sstatus->int_ / 2 + skill * 3 + 40) * 2;
// src/map/battle.cpp:6386
if(mflag > 1) //Autocasted Blitz
// src/map/battle.cpp:6391
DAMAGE_DIV_FIX2(md.damage, skill_get_num(HT_BLITZBEAT, 5));
// src/map/skills/archer/wildwalk.cpp:15
void SkillWildWalk::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
// src/map/skills/archer/wildwalk.cpp:17
const map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/archer/wildwalk.cpp:19
skillratio += -100 + 1800 + 2800 * skill_lv;
// src/map/skills/archer/wildwalk.cpp:21
skillratio += 5 * sstatus->con;
// src/map/skills/archer/wildwalk.cpp:22
skillratio += skillratio * pc_checkskill(sd, WH_NATUREFRIENDLY) / 10;
// src/map/skills/archer/wildwalk.cpp:23
skillratio += skillratio * pc_checkskill(sd, HT_STEELCROW) / 10;
// src/map/skills/archer/wildwalk.cpp:27
void SkillWildWalk::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/archer/wildwalk.cpp:28
clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
// src/map/skills/archer/wildwalk.cpp:29
WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, flag);
// src/map/skills/archer/wildwalk.cpp:30
sc_start(src, src, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(),skill_lv));
```

### Blitz Beat (`HT_BLITZBEAT`)

特殊技能；目标：敌方目标；最高等级 5；射程：5；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；范围：1；吟唱：1500 ms；技能后摇：1000 ms；伤害标记：Splash, IgnoreFlee；消耗/限制：SP Lv1=10; Lv2=13; Lv3=16; Lv4=19; Lv5=22；状态 Falcon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBlitzBeat`
- 实现文件：`src/map/skills/archer/blitzbeat.cpp`

#### `SkillBlitzBeat::SkillBlitzBeat`

来源：`src/map/skills/archer/blitzbeat.cpp:6-7`

```cpp
SkillBlitzBeat::SkillBlitzBeat() : SkillImplRecursiveDamageSplash(HT_BLITZBEAT) {
}
```

### Detect (`HT_DETECTING`)

特殊技能；目标：地面区域；最高等级 4；射程：Lv1=3; Lv2=5; Lv3=7; Lv4=9；命中类型：Single；段数：1；范围：3；伤害标记：NoDamage, Splash；消耗/限制：SP 8；状态 Falcon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDetect`
- 实现文件：`src/map/skills/archer/detect.cpp`

#### `SkillDetect::SkillDetect`

来源：`src/map/skills/archer/detect.cpp:8-9`

```cpp
SkillDetect::SkillDetect() : SkillImpl(HT_DETECTING) {
}
```

#### `SkillDetect::castendPos2`

来源：`src/map/skills/archer/detect.cpp:11-17`

```cpp
void SkillDetect::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	int32 i = skill_get_splash(getSkillId(), skill_lv);
	map_foreachinallarea( status_change_timer_sub,
		src->m, x-i, y-i, x+i,y+i,BL_CHAR,
		src,nullptr,SC_SIGHT,tick);
	skill_reveal_trap_inarea(src, i, x, y);
}
```

### Spring Trap (`HT_SPRINGTRAP`)

特殊技能；目标：陷阱；最高等级 5；射程：Lv1=4; Lv2=5; Lv3=6; Lv4=7; Lv5=8；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 10；状态 Falcon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpringTrap`
- 实现文件：`src/map/skills/archer/springtrap.cpp`

#### `SkillSpringTrap::SkillSpringTrap`

来源：`src/map/skills/archer/springtrap.cpp:8-9`

```cpp
SkillSpringTrap::SkillSpringTrap() : SkillImpl(HT_SPRINGTRAP) {
}
```

#### `SkillSpringTrap::castendNoDamageId`

来源：`src/map/skills/archer/springtrap.cpp:11-38`

```cpp
void SkillSpringTrap::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);

	skill_unit *su=nullptr;
	if((target->type==BL_SKILL) && (su=(skill_unit *)target) && (su->group) ){
		switch(su->group->unit_id){
			case UNT_ANKLESNARE:	// ankle snare
				if (su->group->val2 != 0)
					// if it is already trapping something don't spring it,
					// remove trap should be used instead
					break;
				[[fallthrough]];
			case UNT_BLASTMINE:
			case UNT_SKIDTRAP:
			case UNT_LANDMINE:
			case UNT_SHOCKWAVE:
			case UNT_SANDMAN:
			case UNT_FLASHER:
			case UNT_FREEZINGTRAP:
			case UNT_CLAYMORETRAP:
			case UNT_TALKIEBOX:
				su->group->unit_id = UNT_USED_TRAPS;
				clif_changetraplook(target, UNT_USED_TRAPS);
				su->group->limit=DIFF_TICK(tick+1500,su->group->tick);
				su->limit=DIFF_TICK(tick+1500,su->group->tick);
		}
	}
}
```

### Phantasmic Arrow (`HT_PHANTASMIC`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Single；段数：1；属性：Weapon；击退：3；消耗/限制：SP 10；武器 Bow。

- 覆盖：`exact-class-methods`
- 实现类：`SkillPhantasmicArrow`
- 实现文件：`src/map/skills/archer/phantasmicarrow.cpp`

#### `SkillPhantasmicArrow::SkillPhantasmicArrow`

来源：`src/map/skills/archer/phantasmicarrow.cpp:8-9`

```cpp
SkillPhantasmicArrow::SkillPhantasmicArrow() : WeaponSkillImpl(HT_PHANTASMIC) {
}
```

#### `SkillPhantasmicArrow::calculateSkillRatio`

来源：`src/map/skills/archer/phantasmicarrow.cpp:11-17`

```cpp
void SkillPhantasmicArrow::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 400;
#else
	base_skillratio += 50;
#endif
}
```

### Beast Strafing (`HT_POWER`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Multi_Hit；段数：2；属性：Weapon；持续时间1：100 ms；消耗/限制：SP 12；弹药数 1；武器 Bow；弹药 Arrow。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBeastStrafing`
- 实现文件：`src/map/skills/archer/beaststrafing.cpp`

#### `SkillBeastStrafing::SkillBeastStrafing`

来源：`src/map/skills/archer/beaststrafing.cpp:8-9`

```cpp
SkillBeastStrafing::SkillBeastStrafing() : SkillImpl(HT_POWER) {
}
```

#### `SkillBeastStrafing::castendDamageId`

来源：`src/map/skills/archer/beaststrafing.cpp:11-16`

```cpp
void SkillBeastStrafing::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);

	if( tstatus->race == RC_BRUTE || tstatus->race == RC_PLAYER_DORAM || tstatus->race == RC_INSECT )
		skill_attack(BF_WEAPON,src,src,target,getSkillId(),skill_lv,tick,flag);
}
```

#### `SkillBeastStrafing::calculateSkillRatio`

来源：`src/map/skills/archer/beaststrafing.cpp:18-22`

```cpp
void SkillBeastStrafing::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	const status_data* sstatus = status_get_status_data(*src);

	base_skillratio += -50 + 8 * sstatus->str;
}
```
