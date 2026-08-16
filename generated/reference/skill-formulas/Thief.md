# Thief 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 48 | `TF_DOUBLE` / Double Attack | `exact-class-methods` | `SkillDoubleAttack` | src/map/skills/thief/doubleattack.cpp |
| 49 | `TF_MISS` / Improve Dodge | `core-source-references` | `` | src/map/status.cpp |
| 50 | `TF_STEAL` / Steal | `exact-class-methods` | `SkillSteal` | src/map/skills/thief/steal.cpp |
| 51 | `TF_HIDING` / Hiding | `exact-class-methods` | `SkillHiding` | src/map/skills/thief/hiding.cpp |
| 52 | `TF_POISON` / Envenom | `exact-class-methods` | `SkillEnvenom` | src/map/skills/thief/envenom.cpp |
| 53 | `TF_DETOXIFY` / Detoxify | `exact-class-methods` | `SkillDetoxify` | src/map/skills/thief/detoxify.cpp |
| 149 | `TF_SPRINKLESAND` / Sand Attack | `exact-class-methods` | `SkillSandAttack` | src/map/skills/thief/sandattack.cpp |
| 150 | `TF_BACKSLIDING` / Back Slide | `exact-class-methods` | `SkillBackSlide` | src/map/skills/thief/backslide.cpp |
| 151 | `TF_PICKSTONE` / Find Stone | `exact-class-methods` | `SkillFindStone` | src/map/skills/thief/findstone.cpp |
| 152 | `TF_THROWSTONE` / Stone Fling | `exact-class-methods` | `SkillStoneFling` | src/map/skills/thief/stonefling.cpp |

## 详细公式与效果实现

### Double Attack (`TF_DOUBLE`)

武器/物理技能；目标：被动；最高等级 10；射程：-1；命中类型：Multi_Hit；段数：2；属性：Weapon。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDoubleAttack`
- 实现文件：`src/map/skills/thief/doubleattack.cpp`

#### `SkillDoubleAttack::SkillDoubleAttack`

来源：`src/map/skills/thief/doubleattack.cpp:8-9`

```cpp
SkillDoubleAttack::SkillDoubleAttack() : WeaponSkillImpl(TF_DOUBLE) {
}
```

#### `SkillDoubleAttack::modifyDamageData`

来源：`src/map/skills/thief/doubleattack.cpp:11-14`

```cpp
void SkillDoubleAttack::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	// For NPC used skill.
	dmg.type = DMG_MULTI_HIT;
}
```

### Improve Dodge (`TF_MISS`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:4505
base_status->hit += 20;
// src/map/status.cpp:4507
base_status->hit += skill * 3;
// src/map/status.cpp:4509
base_status->hit += skill * 3;
// src/map/status.cpp:4518
base_status->flee += skill*(sd->class_&JOBL_2 && (sd->class_&MAPID_FIRSTMASK) == MAPID_THIEF? 4 : 3);
// src/map/status.cpp:4520
base_status->flee += (skill*3) / 2;
// src/map/status.cpp:4522
base_status->flee += 20;
// src/map/status.cpp:4524
base_status->flee += skill * 10;
// src/map/status.cpp:8143
if( sc->getSCE(SC_MARSHOFABYSS) && speed_rate > 150 )
// src/map/status.cpp:8144
speed_rate = 150;
```

### Steal (`TF_STEAL`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 10。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSteal`
- 实现文件：`src/map/skills/thief/steal.cpp`

#### `SkillSteal::SkillSteal`

来源：`src/map/skills/thief/steal.cpp:10-11`

```cpp
SkillSteal::SkillSteal() : SkillImpl(TF_STEAL) {
}
```

#### `SkillSteal::castendNoDamageId`

来源：`src/map/skills/thief/steal.cpp:13-22`

```cpp
void SkillSteal::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32 &flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);

	if (sd) {
		if (pc_steal_item(sd, bl, skill_lv))
			clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);
		else
			clif_skill_fail(*sd, getSkillId(), USESKILL_FAIL);
	}
}
```

### Hiding (`TF_HIDING`)

非伤害技能；目标：自身；最高等级 10；射程：1；命中类型：Single；段数：1；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000; Lv6=180000; Lv7=210000; Lv8=240000; Lv9=270000; Lv10=300000 ms；伤害标记：NoDamage；消耗/限制：SP 10；关联状态：Hiding。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHiding`
- 实现文件：`src/map/skills/thief/hiding.cpp`

#### `SkillHiding::SkillHiding`

来源：`src/map/skills/thief/hiding.cpp:9-10`

```cpp
SkillHiding::SkillHiding() : SkillImpl(TF_HIDING) {
}
```

#### `SkillHiding::castendNoDamageId`

来源：`src/map/skills/thief/hiding.cpp:12-23`

```cpp
void SkillHiding::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32 &flag) const {
	sc_type type = skill_get_sc(getSkillId());
	status_change *tsc = status_get_sc(bl);
	status_change_entry *tsce = tsc ? tsc->getSCE(SC_HIDING) : nullptr;

	if (tsce) {
		clif_skill_nodamage(src, *bl, getSkillId(), -1, status_change_end(bl, type)); // Hide skill-scream animation.
		return;
	}

	clif_skill_nodamage(src, *bl, getSkillId(), -1, sc_start(src, bl, SC_HIDING, 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
}
```

### Envenom (`TF_POISON`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-2；命中类型：Single；段数：1；属性：Poison；持续时间2：60000 ms；消耗/限制：SP 12；关联状态：Poison。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEnvenom`
- 实现文件：`src/map/skills/thief/envenom.cpp`

#### `SkillEnvenom::SkillEnvenom`

来源：`src/map/skills/thief/envenom.cpp:10-11`

```cpp
SkillEnvenom::SkillEnvenom() : WeaponSkillImpl(TF_POISON) {
}
```

#### `SkillEnvenom::applyAdditionalEffects`

来源：`src/map/skills/thief/envenom.cpp:13-17`

```cpp
void SkillEnvenom::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	if (!sc_start2(src, target, SC_POISON, (4 * skill_lv + 10), skill_lv, src->id, skill_get_time2(getSkillId(), skill_lv)) && sd)
		clif_skill_fail(*sd, getSkillId());
}
```

### Detoxify (`TF_DETOXIFY`)

武器/物理技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Poison；伤害标记：NoDamage；消耗/限制：SP 10。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDetoxify`
- 实现文件：`src/map/skills/thief/detoxify.cpp`

#### `SkillDetoxify::SkillDetoxify`

来源：`src/map/skills/thief/detoxify.cpp:9-10`

```cpp
SkillDetoxify::SkillDetoxify() : SkillImpl(TF_DETOXIFY) {
}
```

#### `SkillDetoxify::castendNoDamageId`

来源：`src/map/skills/thief/detoxify.cpp:12-16`

```cpp
void SkillDetoxify::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32 &flag) const {
	clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);
	status_change_end(bl, SC_POISON);
	status_change_end(bl, SC_DPOISON);
}
```

### Sand Attack (`TF_SPRINKLESAND`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：1；命中类型：Single；段数：1；属性：Earth；持续时间2：30000 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP 9；关联状态：Blind。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSandAttack`
- 实现文件：`src/map/skills/thief/sandattack.cpp`

#### `SkillSandAttack::SkillSandAttack`

来源：`src/map/skills/thief/sandattack.cpp:9-10`

```cpp
SkillSandAttack::SkillSandAttack() : WeaponSkillImpl(TF_SPRINKLESAND) {
}
```

#### `SkillSandAttack::calculateSkillRatio`

来源：`src/map/skills/thief/sandattack.cpp:12-14`

```cpp
void SkillSandAttack::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 30;
}
```

#### `SkillSandAttack::applyAdditionalEffects`

来源：`src/map/skills/thief/sandattack.cpp:16-19`

```cpp
void SkillSandAttack::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	sc_start(src, target, SC_BLIND, (sd != nullptr) ? 20 : 15, skill_lv, skill_get_time2(getSkillId(), skill_lv));
}
```

### Back Slide (`TF_BACKSLIDING`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；击退：5；伤害标记：NoDamage；消耗/限制：SP 7。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBackSlide`
- 实现文件：`src/map/skills/thief/backslide.cpp`

#### `SkillBackSlide::SkillBackSlide`

来源：`src/map/skills/thief/backslide.cpp:10-11`

```cpp
SkillBackSlide::SkillBackSlide() : SkillImpl(TF_BACKSLIDING) {
}
```

#### `SkillBackSlide::castendNoDamageId`

来源：`src/map/skills/thief/backslide.cpp:13-32`

```cpp
void SkillBackSlide::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32 &flag) const {
	//This is the correct implementation as per packet logging information. [Skotlex]

	// Backsliding makes you immune to being stopped for 200ms, but only if you don't have the endure effect yet
	if (unit_data *ud = unit_bl2ud(bl); ud != nullptr && !status_isendure(*bl, tick, true))
		ud->endure_tick = tick + 200;

#ifdef RENEWAL
	int16 blew_count = skill_blown(src, bl, skill_get_blewcount(getSkillId(), skill_lv), unit_getdir(bl),
	                               static_cast<enum e_skill_blown>(BLOWN_IGNORE_NO_KNOCKBACK | BLOWN_DONT_SEND_PACKET));
	clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);

	if (blew_count > 0)
		clif_blown(src); // Always blow, otherwise it shows a casting animation. [Lemongrass]
#else
	int16 blew_count = skill_blown(src, bl, skill_get_blewcount(getSkillId(), skill_lv), unit_getdir(bl), BLOWN_IGNORE_NO_KNOCKBACK);
	clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);
	clif_slide(*bl, bl->x, bl->y); //Show the casting animation on pre-re
#endif
}
```

### Find Stone (`TF_PICKSTONE`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：500 ms；伤害标记：NoDamage；消耗/限制：SP 3；状态 Recover_Weight_Rate；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFindStone`
- 实现文件：`src/map/skills/thief/findstone.cpp`

#### `SkillFindStone::SkillFindStone`

来源：`src/map/skills/thief/findstone.cpp:12-13`

```cpp
SkillFindStone::SkillFindStone() : SkillImpl(TF_PICKSTONE) {
}
```

#### `SkillFindStone::castendNoDamageId`

来源：`src/map/skills/thief/findstone.cpp:15-39`

```cpp
void SkillFindStone::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32 &flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);

	if (sd) {
		unsigned char eflag;
		item item_tmp;
		block_list tbl;
		clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);
		memset(&item_tmp, 0, sizeof(item_tmp));
		memset(&tbl, 0, sizeof(tbl)); // [MouseJstr]
		item_tmp.nameid = ITEMID_STONE;
		item_tmp.identify = 1;
		tbl.id = 0;
		// Commented because of duplicate animation [Lemongrass]
		// At the moment this displays the pickup animation a second time
		// If this is required in older clients, we need to add a version check here
		// clif_takeitem(*sd,tbl);
		eflag = pc_additem(sd, &item_tmp, 1, LOG_TYPE_PRODUCE);
		if (eflag) {
			clif_additem(sd, 0, 0, eflag);
			if (battle_config.skill_drop_items_full)
				map_addflooritem(&item_tmp, 1, sd->m, sd->x, sd->y, 0, 0, 0, 4, 0);
		}
	}
}
```

### Stone Fling (`TF_THROWSTONE`)

特殊技能；目标：敌方目标；最高等级 1；射程：7；命中类型：Single；段数：1；持续时间1：5000 ms；持续时间2：30000 ms；伤害标记：IgnoreFlee；消耗/限制：SP 2；道具 Stone×1；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillStoneFling`
- 实现文件：`src/map/skills/thief/stonefling.cpp`

#### `SkillStoneFling::SkillStoneFling`

来源：`src/map/skills/thief/stonefling.cpp:10-11`

```cpp
SkillStoneFling::SkillStoneFling() : SkillImpl(TF_THROWSTONE) {
}
```

#### `SkillStoneFling::applyAdditionalEffects`

来源：`src/map/skills/thief/stonefling.cpp:13-23`

```cpp
void SkillStoneFling::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	if (sd != nullptr) {
		// Only blind if used by player and stun failed
		if (!sc_start(src, target, SC_STUN, 3, skill_lv, skill_get_time(getSkillId(), skill_lv)))
			sc_start(src, target, SC_BLIND, 3, skill_lv, skill_get_time2(getSkillId(), skill_lv));
	} else {
		// 5% stun chance and no blind chance when used by monsters
		sc_start(src, target, SC_STUN, 5, skill_lv, skill_get_time(getSkillId(), skill_lv));
	}
}
```

#### `SkillStoneFling::castendDamageId`

来源：`src/map/skills/thief/stonefling.cpp:25-27`

```cpp
void SkillStoneFling::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	skill_attack(skill_get_type(getSkillId()), src, src, target, getSkillId(), skill_lv, tick, flag);
}
```
