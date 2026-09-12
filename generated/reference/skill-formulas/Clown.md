# Clown 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 394 | `CG_ARROWVULCAN` / Vulcan Arrow | `exact-class-methods` | `SkillVulcanArrow` | src/map/skills/archer/vulcanarrow.cpp |
| 395 | `CG_MOONLIT` / Sheltering Bliss | `exact-class-methods` | `SkillShelteringBliss` | src/map/skills/archer/shelteringbliss.cpp |
| 396 | `CG_MARIONETTE` / Marionette Control | `exact-class-methods` | `SkillMarionetteControl` | src/map/skills/archer/marionettecontrol.cpp |
| 487 | `CG_LONGINGFREEDOM` / Longing for Freedom | `exact-class-methods` | `SkillLongingForFreedom` | src/map/skills/archer/longingforfreedom.cpp |
| 488 | `CG_HERMODE` / Wand of Hermode | `exact-class-methods` | `SkillWandOfHermode` | src/map/skills/archer/wandofhermode.cpp |
| 489 | `CG_TAROTCARD` / Tarot Card of Fate | `exact-class-methods` | `SkillTarotCardOfFate` | src/map/skills/archer/tarotcardoffate.cpp |

## 详细公式与效果实现

### Vulcan Arrow (`CG_ARROWVULCAN`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：-9；属性：Weapon；吟唱：Lv1=2000; Lv2=2200; Lv3=2400; Lv4=2600; Lv5=2800; Lv6=3000; Lv7=3200; Lv8=3400; Lv9=3600; Lv10=3800 ms；技能后摇：Lv1-5=2800; Lv6-10=3000 ms；移动后摇：2000 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30；弹药数 1；武器 Musical, Whip；弹药 Arrow。

- 覆盖：`exact-class-methods`
- 实现类：`SkillVulcanArrow`
- 实现文件：`src/map/skills/archer/vulcanarrow.cpp`

#### `SkillVulcanArrow::SkillVulcanArrow`

来源：`src/map/skills/archer/vulcanarrow.cpp:10-11`

```cpp
SkillVulcanArrow::SkillVulcanArrow() : WeaponSkillImpl(CG_ARROWVULCAN) {
}
```

#### `SkillVulcanArrow::calculateSkillRatio`

来源：`src/map/skills/archer/vulcanarrow.cpp:13-20`

```cpp
void SkillVulcanArrow::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
#ifdef RENEWAL
	skillratio += 400 + 100 * skill_lv;
	RE_LVL_DMOD(100);
#else
	skillratio += 100 + 100 * skill_lv;
#endif
}
```

### Sheltering Bliss (`CG_MOONLIT`)

特殊技能；目标：自身；最高等级 5；段数：1；范围：3；击退：2；持续时间1：Lv1=20000; Lv2=25000; Lv3=30000; Lv4=35000; Lv5=40000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=30; Lv2=40; Lv3=50; Lv4=60; Lv5=70；武器 Musical, Whip。

- 覆盖：`exact-class-methods`
- 实现类：`SkillShelteringBliss`
- 实现文件：`src/map/skills/archer/shelteringbliss.cpp`

#### `SkillShelteringBliss::SkillShelteringBliss`

来源：`src/map/skills/archer/shelteringbliss.cpp:6-7`

```cpp
SkillShelteringBliss::SkillShelteringBliss() : SkillImpl(CG_MOONLIT) {
}
```

#### `SkillShelteringBliss::castendPos2`

来源：`src/map/skills/archer/shelteringbliss.cpp:9-12`

```cpp
void SkillShelteringBliss::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag |= 1; // Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src, getSkillId(), skill_lv, x, y, 0);
}
```

### Marionette Control (`CG_MARIONETTE`)

非伤害技能；目标：友方目标；最高等级 1；射程：7；命中类型：Single；段数：1；持续时间1：1000 ms；伤害标记：NoDamage；消耗/限制：SP 100；关联状态：Marionette。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMarionetteControl`
- 实现文件：`src/map/skills/archer/marionettecontrol.cpp`

#### `SkillMarionetteControl::SkillMarionetteControl`

来源：`src/map/skills/archer/marionettecontrol.cpp:10-11`

```cpp
SkillMarionetteControl::SkillMarionetteControl() : SkillImpl(CG_MARIONETTE) {
}
```

#### `SkillMarionetteControl::castendNoDamageId`

来源：`src/map/skills/archer/marionettecontrol.cpp:13-46`

```cpp
void SkillMarionetteControl::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	map_session_data *dstsd = BL_CAST(BL_PC, target);
	status_change *sc = status_get_sc(src);
	status_change *tsc = status_get_sc(target);

	if ((sd && dstsd && (dstsd->class_ & MAPID_SECONDMASK) == MAPID_BARDDANCER && dstsd->status.sex == sd->status.sex) ||
		(tsc && (tsc->getSCE(SC_CURSE) || tsc->getSCE(SC_QUAGMIRE)))) {
		// Cannot cast on another bard/dancer-type class of the same gender as caster, or targets under Curse/Quagmire
		if (sd != nullptr) {
			clif_skill_fail(*sd, getSkillId());
		}
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}

	if (sc && tsc) {
		if (!sc->getSCE(SC_MARIONETTE) && !tsc->getSCE(SC_MARIONETTE2)) {
			sc_start(src, src, SC_MARIONETTE, 100, target->id, skill_get_time(getSkillId(), skill_lv));
			sc_start(src, target, SC_MARIONETTE2, 100, src->id, skill_get_time(getSkillId(), skill_lv));
			clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
		} else if (sc->getSCE(SC_MARIONETTE) && sc->getSCE(SC_MARIONETTE)->val1 == target->id &&
			tsc->getSCE(SC_MARIONETTE2) && tsc->getSCE(SC_MARIONETTE2)->val1 == src->id) {
			status_change_end(src, SC_MARIONETTE);
			status_change_end(target, SC_MARIONETTE2);
		} else {
			if (sd != nullptr) {
				clif_skill_fail(*sd, getSkillId());
			}
			flag |= SKILL_NOCONSUME_REQ;
			return;
		}
	}
}
```

### Longing for Freedom (`CG_LONGINGFREEDOM`)

非伤害技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 15；关联状态：Longing。

- 覆盖：`exact-class-methods`
- 实现类：`SkillLongingForFreedom`
- 实现文件：`src/map/skills/archer/longingforfreedom.cpp`

#### `SkillLongingForFreedom::SkillLongingForFreedom`

来源：`src/map/skills/archer/longingforfreedom.cpp:11-12`

```cpp
SkillLongingForFreedom::SkillLongingForFreedom() : SkillImpl(CG_LONGINGFREEDOM) {
}
```

#### `SkillLongingForFreedom::castendNoDamageId`

来源：`src/map/skills/archer/longingforfreedom.cpp:14-27`

```cpp
void SkillLongingForFreedom::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	sc_type type = skill_get_sc(getSkillId());
	status_change *tsc = status_get_sc(target);
	status_change_entry *tsce = (tsc != nullptr && type != SC_NONE) ? tsc->getSCE(type) : nullptr;

	if (tsc && !tsce && (tsce=tsc->getSCE(SC_DANCING)) && tsce->val4
		&& (tsce->val1&0xFFFF) != CG_MOONLIT) //Can't use Longing for Freedom while under Moonlight Petals. [Skotlex]
	{
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
			sc_start(src,target,type,100,skill_lv,skill_get_time(getSkillId(),skill_lv)));
	}
#endif
}
```

### Wand of Hermode (`CG_HERMODE`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：1；持续时间1：Lv1=10000; Lv2=15000; Lv3=20000; Lv4=25000; Lv5=30000 ms；持续时间2：Lv1=10000; Lv2=15000; Lv3=20000; Lv4=25000; Lv5=30000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=20; Lv2=30; Lv3=40; Lv4=50; Lv5=60；武器 Musical, Whip；关联状态：Hermode。

- 覆盖：`exact-class-methods`
- 实现类：`SkillWandOfHermode`
- 实现文件：`src/map/skills/archer/wandofhermode.cpp`

#### `SkillWandOfHermode::SkillWandOfHermode`

来源：`src/map/skills/archer/wandofhermode.cpp:10-11`

```cpp
SkillWandOfHermode::SkillWandOfHermode() : SkillImpl(CG_HERMODE) {
}
```

#### `SkillWandOfHermode::castendNoDamageId`

来源：`src/map/skills/archer/wandofhermode.cpp:13-17`

```cpp
void SkillWandOfHermode::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillWandOfHermode::castendPos2`

来源：`src/map/skills/archer/wandofhermode.cpp:19-26`

```cpp
void SkillWandOfHermode::castendPos2(block_list *src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32 &flag) const {
#ifndef RENEWAL
	skill_clear_unitgroup(src);
	if (auto sg = skill_unitsetting(src, getSkillId(), skill_lv, x, y, 0); sg != nullptr)
		sc_start4(src, src, SC_DANCING, 100, getSkillId(), 0, skill_lv, sg->group_id, skill_get_time(getSkillId(), skill_lv));
	flag |= 1;
#endif
}
```

### Tarot Card of Fate (`CG_TAROTCARD`)

特殊技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：3000 ms；持续时间2：30000 ms；伤害标记：NoDamage, IgnoreFlee；消耗/限制：SP 40；关联状态：TarotCard。

- 覆盖：`exact-class-methods`
- 实现类：`SkillTarotCardOfFate`
- 实现文件：`src/map/skills/archer/tarotcardoffate.cpp`

#### `SkillTarotCardOfFate::SkillTarotCardOfFate`

来源：`src/map/skills/archer/tarotcardoffate.cpp:20-21`

```cpp
SkillTarotCardOfFate::SkillTarotCardOfFate() : SkillImpl(CG_TAROTCARD) {
}
```

#### `SkillTarotCardOfFate::castendNoDamageId`

来源：`src/map/skills/archer/tarotcardoffate.cpp:23-49`

```cpp
void SkillTarotCardOfFate::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	mob_data *dstmd = BL_CAST(BL_MOB, target);
	status_change *tsc = status_get_sc(target);

	if (tsc && tsc->getSCE(SC_TAROTCARD)) {
		// Target currently has the SUN tarot card effect and is immune to any other effect.
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}

	if (rnd() % 100 > skill_lv * 8 ||
#ifndef RENEWAL
		(tsc && tsc->getSCE(SC_BASILICA)) ||
#endif
		(dstmd && ((dstmd->guardian_data && dstmd->mob_id == MOBID_EMPERIUM) || status_get_class_(target) == CLASS_BATTLEFIELD))) {
		if (sd != nullptr)
			clif_skill_fail(*sd, getSkillId());
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}

	status_zap(src, 0, skill_get_sp(getSkillId(), skill_lv)); // Consume SP only on success.
	int32 card = skill_tarotcard(src, target, getSkillId(), skill_lv, tick); // Actual effect is executed here.
	clif_specialeffect((card == 6) ? src : target, EF_TAROTCARD1 + card - 1, AREA);
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
}
```
