# Professor 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 373 | `PF_HPCONVERSION` / Indulge | `exact-class-methods` | `SkillIndulge` | src/map/skills/mage/indulge.cpp |
| 374 | `PF_SOULCHANGE` / Soul Exhale | `exact-class-methods` | `SkillSoulExhale` | src/map/skills/mage/soulexhale.cpp |
| 375 | `PF_SOULBURN` / Soul Siphon | `exact-class-methods` | `SkillSoulSiphon` | src/map/skills/mage/soulsiphon.cpp |
| 402 | `PF_MINDBREAKER` / Mind Breaker | `exact-class-methods` | `SkillMindBreaker` | src/map/skills/mage/mindbreaker.cpp |
| 403 | `PF_MEMORIZE` / Foresight | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 404 | `PF_FOGWALL` / Blinding Mist | `exact-class-methods` | `SkillBlindingMist` | src/map/skills/mage/blindingmist.cpp |
| 405 | `PF_SPIDERWEB` / Fiber Lock | `exact-class-methods` | `SkillFiberLock` | src/map/skills/mage/fiberlock.cpp |
| 482 | `PF_DOUBLECASTING` / Double Casting | `generic-or-class-mapped` | `StatusSkillImpl` |  |

## 详细公式与效果实现

### Indulge (`PF_HPCONVERSION`)

魔法技能；目标：自身；最高等级 5；命中类型：Single；段数：1；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5。

- 覆盖：`exact-class-methods`
- 实现类：`SkillIndulge`
- 实现文件：`src/map/skills/mage/indulge.cpp`

#### `SkillIndulge::SkillIndulge`

来源：`src/map/skills/mage/indulge.cpp:10-11`

```cpp
SkillIndulge::SkillIndulge() : SkillImpl(PF_HPCONVERSION) {
}
```

#### `SkillIndulge::castendNoDamageId`

来源：`src/map/skills/mage/indulge.cpp:13-28`

```cpp
void SkillIndulge::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	const status_data* sstatus = status_get_status_data(*src);
	map_session_data* sd = BL_CAST(BL_PC, src);
	int32 hp = sstatus->max_hp / 10;
	int32 sp = hp * skill_lv;

	if (!status_charge(src, hp, 0)) {
		if (sd != nullptr) {
			clif_skill_fail(*sd, getSkillId());
		}
		return;
	}

	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
	status_heal(target, 0, sp, 2);
}
```

### Soul Exhale (`PF_SOULCHANGE`)

非伤害技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；吟唱：3000 ms；技能后摇：5000 ms；伤害标记：NoDamage；消耗/限制：SP 5。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSoulExhale`
- 实现文件：`src/map/skills/mage/soulexhale.cpp`

#### `SkillSoulExhale::SkillSoulExhale`

来源：`src/map/skills/mage/soulexhale.cpp:13-14`

```cpp
SkillSoulExhale::SkillSoulExhale() : SkillImpl(PF_SOULCHANGE) {
}
```

#### `SkillSoulExhale::castendNoDamageId`

来源：`src/map/skills/mage/soulexhale.cpp:16-55`

```cpp
void SkillSoulExhale::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	const status_data* sstatus = status_get_status_data(*src);
	const status_data* tstatus = status_get_status_data(*target);
	status_change* tsc = status_get_sc(target);
	mob_data* dstmd = BL_CAST(BL_MOB, target);
	map_session_data* sd = BL_CAST(BL_PC, src);
	uint32 sp1 = 0, sp2 = 0;

	if (dstmd != nullptr) {
		if (dstmd->state.soul_change_flag) {
			if (sd != nullptr) {
				clif_skill_fail(*sd, getSkillId());
			}
			return;
		}

		dstmd->state.soul_change_flag = 1;
		sp2 = sstatus->max_sp * 3 / 100;
		status_heal(src, 0, sp2, 2);
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
		return;
	}

	sp1 = sstatus->sp;
	sp2 = tstatus->sp;
#ifdef RENEWAL
	sp1 /= 2;
	sp2 /= 2;
	if (tsc != nullptr && tsc->hasSCE(SC_EXTREMITYFIST)) {
		sp1 = tstatus->sp;
	}
#endif
	if (tsc != nullptr && tsc->hasSCE(SC_NORECOVER_STATE)) {
		sp1 = tstatus->sp;
	}

	status_set_sp(src, sp2, 3);
	status_set_sp(target, sp1, 3);
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
}
```

### Soul Siphon (`PF_SOULBURN`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；冷却：Lv1-4=10000; Lv5=15000 ms；伤害标记：IgnoreAtkCard, IgnoreElement, IgnoreDefCard；消耗/限制：SP Lv1=80; Lv2=90; Lv3=100; Lv4=110; Lv5=120。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSoulSiphon`
- 实现文件：`src/map/skills/mage/soulsiphon.cpp`

#### `SkillSoulSiphon::SkillSoulSiphon`

来源：`src/map/skills/mage/soulsiphon.cpp:9-10`

```cpp
SkillSoulSiphon::SkillSoulSiphon() : SkillImpl(PF_SOULBURN) {
}
```

#### `SkillSoulSiphon::castendDamageId`

来源：`src/map/skills/mage/soulsiphon.cpp:12-26`

```cpp
void SkillSoulSiphon::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	if (rnd() % 100 < (skill_lv < 5 ? 30 + skill_lv * 10 : 70)) {
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
		if (skill_lv == 5) {
			skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
		}
		status_percent_damage(src, target, 0, 100, false);
	} else {
		clif_skill_nodamage(src, *src, getSkillId(), skill_lv);
		if (skill_lv == 5) {
			skill_attack(BF_MAGIC, src, src, src, getSkillId(), skill_lv, tick, flag);
		}
		status_percent_damage(src, src, 0, 100, false);
	}
}
```

### Mind Breaker (`PF_MINDBREAKER`)

非伤害技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；技能后摇：Lv1=800; Lv2=900; Lv3=1000; Lv4=1100; Lv5=1200 ms；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=12; Lv2=15; Lv3=18; Lv4=21; Lv5=24；关联状态：MindBreaker。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMindBreaker`
- 实现文件：`src/map/skills/mage/mindbreaker.cpp`

#### `SkillMindBreaker::SkillMindBreaker`

来源：`src/map/skills/mage/mindbreaker.cpp:13-14`

```cpp
SkillMindBreaker::SkillMindBreaker() : SkillImpl(PF_MINDBREAKER) {
}
```

#### `SkillMindBreaker::castendNoDamageId`

来源：`src/map/skills/mage/mindbreaker.cpp:16-51`

```cpp
void SkillMindBreaker::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	const status_data* tstatus = status_get_status_data(*target);
	status_change* tsc = status_get_sc(target);
	sc_type type = skill_get_sc(getSkillId());
	status_change_entry *tsce = (tsc != nullptr && type != SC_NONE) ? tsc->getSCE(type) : nullptr;
	map_session_data* sd = BL_CAST(BL_PC, src);
	mob_data* dstmd = BL_CAST(BL_MOB, target);

	if (status_has_mode(tstatus, MD_STATUSIMMUNE) || battle_check_undead(tstatus->race, tstatus->def_ele)) {
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}

	if (tsce != nullptr)
	{	//HelloKitty2 (?) explained that this silently fails when target is
		//already inflicted. [Skotlex]
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}

	//Has a 55% + skill_lv*5% success chance.
	if (!clif_skill_nodamage(src, *target, getSkillId(), skill_lv,
			sc_start(src, target, type, 55 + 5 * skill_lv, skill_lv, skill_get_time(getSkillId(), skill_lv)))) {
		if (sd != nullptr) {
			clif_skill_fail(*sd, getSkillId());
		}
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}

	unit_skillcastcancel(target, 0);

	if (dstmd != nullptr) {
		mob_target(dstmd, src, skill_get_range2(src, getSkillId(), skill_lv, true));
	}
}
```

### Foresight (`PF_MEMORIZE`)

魔法技能；目标：自身；最高等级 1；段数：1；吟唱：5000 ms；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：Memorize。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skills/mage/skill_factory_mage.cpp:285
case PF_DOUBLECASTING:
```

### Blinding Mist (`PF_FOGWALL`)

魔法技能；目标：地面区域；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Earth；持续时间1：20000 ms；持续时间2：10000 ms；伤害标记：NoDamage；消耗/限制：SP 25；关联状态：FogWall。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBlindingMist`
- 实现文件：`src/map/skills/mage/blindingmist.cpp`

#### `SkillBlindingMist::SkillBlindingMist`

来源：`src/map/skills/mage/blindingmist.cpp:8-9`

```cpp
SkillBlindingMist::SkillBlindingMist() : SkillImpl(PF_FOGWALL) {
}
```

#### `SkillBlindingMist::applyAdditionalEffects`

来源：`src/map/skills/mage/blindingmist.cpp:11-17`

```cpp
void SkillBlindingMist::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	status_change* tsc = status_get_sc(target);

	if (src != target && (tsc == nullptr || !tsc->hasSCE(SC_DELUGE))) {
		sc_start(src, target, SC_BLIND, 100, skill_lv, skill_get_time2(getSkillId(), skill_lv));
	}
}
```

#### `SkillBlindingMist::castendPos2`

来源：`src/map/skills/mage/blindingmist.cpp:19-22`

```cpp
void SkillBlindingMist::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag |= 1;	// Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src, getSkillId(), skill_lv, x, y, 0);
}
```

### Fiber Lock (`PF_SPIDERWEB`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；持续时间1：16000 ms；持续时间2：8000 ms；伤害标记：NoDamage；消耗/限制：SP 50；道具 Spiderweb×1；关联状态：SpiderWeb。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFiberLock`
- 实现文件：`src/map/skills/mage/fiberlock.cpp`

#### `SkillFiberLock::SkillFiberLock`

来源：`src/map/skills/mage/fiberlock.cpp:6-7`

```cpp
SkillFiberLock::SkillFiberLock() : SkillImpl(PF_SPIDERWEB) {
}
```

#### `SkillFiberLock::castendPos2`

来源：`src/map/skills/mage/fiberlock.cpp:9-12`

```cpp
void SkillFiberLock::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag |= 1; // Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src, getSkillId(), skill_lv, x, y, 0);
}
```

### Double Casting (`PF_DOUBLECASTING`)

魔法技能；目标：自身；最高等级 5；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：90000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=40; Lv2=45; Lv3=50; Lv4=55; Lv5=60；关联状态：DoubleCast。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skills/mage/skill_factory_mage.cpp:285
case PF_DOUBLECASTING:
```
