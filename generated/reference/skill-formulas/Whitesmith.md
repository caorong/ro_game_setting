# Whitesmith 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 384 | `WS_MELTDOWN` / Shattering Strike | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 387 | `WS_CARTBOOST` / Cart Boost | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 477 | `WS_WEAPONREFINE` / Upgrade Weapon | `exact-class-methods` | `SkillUpgradeWeapon` | src/map/skills/merchant/upgradeweapon.cpp |
| 485 | `WS_CARTTERMINATION` / Cart Termination | `exact-class-methods` | `SkillCartTermination` | src/map/skills/merchant/carttermination.cpp |
| 486 | `WS_OVERTHRUSTMAX` / Maximum Power Thrust | `generic-or-class-mapped` | `StatusSkillImpl` |  |

## 详细公式与效果实现

### Shattering Strike (`WS_MELTDOWN`)

武器/物理技能；目标：自身；最高等级 10；段数：1；吟唱：Lv1-2=500; Lv3-4=600; Lv5-6=700; Lv7-8=800; Lv9=900; Lv10=1000 ms；持续时间1：Lv1=15000; Lv2=20000; Lv3=25000; Lv4=30000; Lv5=35000; Lv6=40000; Lv7=45000; Lv8=50000; Lv9=55000; Lv10=60000 ms；持续时间2：5000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-2=50; Lv3-4=60; Lv5-6=70; Lv7-8=80; Lv9-10=90；关联状态：Meltdown。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:1940
- rate goes from 0 to 10000 (100.00%)
// src/map/skill.cpp:1944
int32 skill_break_equip(block_list *src, block_list *bl, uint16 where, int32 rate, int32 flag)
// src/map/skill.cpp:1946
status_change *src_sc = status_get_sc(src);
// src/map/skill.cpp:1956
status_change *sc = status_get_sc(bl);
// src/map/skill.cpp:1959
sd = BL_CAST(BL_PC, bl);
```

### Cart Boost (`WS_CARTBOOST`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：60000 ms；伤害标记：NoDamage；消耗/限制：SP 20；状态 Cart；关联状态：CartBoost。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Upgrade Weapon (`WS_WEAPONREFINE`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 5。

- 覆盖：`exact-class-methods`
- 实现类：`SkillUpgradeWeapon`
- 实现文件：`src/map/skills/merchant/upgradeweapon.cpp`

#### `SkillUpgradeWeapon::SkillUpgradeWeapon`

来源：`src/map/skills/merchant/upgradeweapon.cpp:9-10`

```cpp
SkillUpgradeWeapon::SkillUpgradeWeapon() : SkillImpl(WS_WEAPONREFINE) {
}
```

#### `SkillUpgradeWeapon::castendNoDamageId`

来源：`src/map/skills/merchant/upgradeweapon.cpp:12-18`

```cpp
void SkillUpgradeWeapon::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sd != nullptr ){
		clif_item_refine_list( *sd );
	}
}
```

### Cart Termination (`WS_CARTTERMINATION`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-2；命中类型：Single；段数：1；属性：Weapon；持续时间2：5000 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP 15；Zeny Lv1=600; Lv2=700; Lv3=800; Lv4=900; Lv5=1000; Lv6=1100; Lv7=1200; Lv8=1300; Lv9=1400; Lv10=1500；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；前置状态 Cartboost；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCartTermination`
- 实现文件：`src/map/skills/merchant/carttermination.cpp`

#### `SkillCartTermination::SkillCartTermination`

来源：`src/map/skills/merchant/carttermination.cpp:9-10`

```cpp
SkillCartTermination::SkillCartTermination() : WeaponSkillImpl(WS_CARTTERMINATION) {
}
```

#### `SkillCartTermination::calculateSkillRatio`

来源：`src/map/skills/merchant/carttermination.cpp:12-22`

```cpp
void SkillCartTermination::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const map_session_data* sd = BL_CAST( BL_PC, src );

	int32 i = 10 * (16 - skill_lv);
	if (i < 1) i = 1;
	//Preserve damage ratio when max cart weight is changed.
	if (sd && sd->cart_weight)
		base_skillratio += sd->cart_weight / i * 80000 / battle_config.max_cart_weight - 100;
	else if (!sd)
		base_skillratio += 80000 / i - 100;
}
```

#### `SkillCartTermination::applyAdditionalEffects`

来源：`src/map/skills/merchant/carttermination.cpp:24-26`

```cpp
void SkillCartTermination::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src,target,SC_STUN,5*skill_lv,skill_lv,skill_get_time2(getSkillId(),skill_lv));
}
```

### Maximum Power Thrust (`WS_OVERTHRUSTMAX`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 15；Zeny Lv1=3000; Lv2=3500; Lv3=4000; Lv4=4500; Lv5=5000；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；关联状态：MaxOverThrust。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。
