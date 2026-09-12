# Archer 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 43 | `AC_OWL` / Owl's Eye | `core-source-references` | `` | src/map/skill.cpp, src/map/status.cpp |
| 44 | `AC_VULTURE` / Vulture's Eye | `core-source-references` | `` | src/map/battle.cpp, src/map/skill.cpp, src/map/status.cpp |
| 45 | `AC_CONCENTRATION` / Improve Concentration | `exact-class-methods` | `SkillConcentration` | src/map/skills/archer/concentration.cpp |
| 46 | `AC_DOUBLE` / Double Strafe | `exact-class-methods` | `SkillDoubleStrafe` | src/map/skills/archer/doublestrafe.cpp |
| 47 | `AC_SHOWER` / Arrow Shower | `exact-class-methods` | `SkillArrowShower` | src/map/skills/archer/arrowshower.cpp |
| 147 | `AC_MAKINGARROW` / Arrow Crafting | `exact-class-methods` | `SkillMakingArrow` | src/map/skills/archer/makingarrow.cpp |
| 148 | `AC_CHARGEARROW` / Arrow Repel | `exact-class-methods` | `SkillChargeArrow` | src/map/skills/archer/chargearrow.cpp |

## 详细公式与效果实现

### Owl's Eye (`AC_OWL`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:311
return CAST_NODAMAGE;
// src/map/skill.cpp:315
return CAST_DAMAGE; //Combo skill.
// src/map/skill.cpp:316
return CAST_NODAMAGE;
// src/map/skill.cpp:318
if (skill->nk[NK_NODAMAGE])
// src/map/skill.cpp:319
return CAST_NODAMAGE;
// src/map/skill.cpp:320
return CAST_DAMAGE;
// src/map/skill.cpp:324
int32 skill_get_range2(const block_list* bl, uint16 skill_id, uint16 skill_lv, bool isServer) {
// src/map/skill.cpp:328
int32 range = skill_get_range(skill_id, skill_lv);
```

### Vulture's Eye (`AC_VULTURE`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:3278
hitrate += sstatus->hit - flee;
// src/map/battle.cpp:3282
hitrate -= 50;
// src/map/battle.cpp:3285
hitrate += sd->bonus.arrow_hit;
// src/map/battle.cpp:3288
if (sd) //in Renewal hit bonus from Vultures Eye is not anymore shown in status window
// src/map/battle.cpp:3289
hitrate += pc_checkskill(sd,AC_VULTURE);
// src/map/battle.cpp:3295
skill->impl->modifyHitRate(hitrate, src, target, skill_lv);
// src/map/battle.cpp:3297
} else if (sd && wd->type&DMG_MULTI_HIT && wd->div_ == 2) // +1 hit per level of Double Attack on a successful double attack (making sure other multi attack skills do not trigger this) [helvetica]
// src/map/battle.cpp:3298
hitrate += pc_checkskill(sd,TF_DOUBLE);
// src/map/battle.cpp:6618
flee = (flee * (100 - (attacker_count - (battle_config.agi_penalty_count - 1))*battle_config.agi_penalty_num))/100;
// src/map/battle.cpp:6620
flee -= (attacker_count - (battle_config.agi_penalty_count - 1))*battle_config.agi_penalty_num;
// src/map/battle.cpp:6621
if(flee < 1)
// src/map/battle.cpp:6622
flee = 1;
// src/map/battle.cpp:6626
hitrate += sstatus->hit - flee;
// src/map/battle.cpp:6628
if( sd ) //in Renewal hit bonus from Vultures Eye is not shown anymore in status window
// src/map/battle.cpp:6629
hitrate += pc_checkskill(sd,AC_VULTURE);
// src/map/battle.cpp:6631
hitrate = cap_value(hitrate, battle_config.min_hitrate, battle_config.max_hitrate);
```

### Improve Concentration (`AC_CONCENTRATION`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；范围：3；持续时间1：Lv1=60000; Lv2=80000; Lv3=100000; Lv4=120000; Lv5=140000; Lv6=160000; Lv7=180000; Lv8=200000; Lv9=220000; Lv10=240000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=25; Lv2=30; Lv3=35; Lv4=40; Lv5=45; Lv6=50; Lv7=55; Lv8=60; Lv9=65; Lv10=70；关联状态：Concentrate。

- 覆盖：`exact-class-methods`
- 实现类：`SkillConcentration`
- 实现文件：`src/map/skills/archer/concentration.cpp`

#### `SkillConcentration::SkillConcentration`

来源：`src/map/skills/archer/concentration.cpp:9-11`

```cpp
SkillConcentration::SkillConcentration() : SkillImpl(AC_CONCENTRATION)
{
}
```

#### `SkillConcentration::castendNoDamageId`

来源：`src/map/skills/archer/concentration.cpp:13-21`

```cpp
void SkillConcentration::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const
{
	sc_type type = skill_get_sc(getSkillId());

	int32 splash = skill_get_splash(getSkillId(), skill_lv);
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv, sc_start(src, target, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
	skill_reveal_trap_inarea(src, splash, src->x, src->y);
	map_foreachinallrange(status_change_timer_sub, src, splash, BL_CHAR, src, nullptr, type, tick);
}
```

### Double Strafe (`AC_DOUBLE`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-9；命中类型：Multi_Hit；段数：2；属性：Weapon；持续时间1：100 ms；消耗/限制：SP 12；弹药数 1；武器 Bow；弹药 Arrow。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDoubleStrafe`
- 实现文件：`src/map/skills/archer/doublestrafe.cpp`

#### `SkillDoubleStrafe::SkillDoubleStrafe`

来源：`src/map/skills/archer/doublestrafe.cpp:6-7`

```cpp
SkillDoubleStrafe::SkillDoubleStrafe() : WeaponSkillImpl(AC_DOUBLE) {
}
```

#### `SkillDoubleStrafe::calculateSkillRatio`

来源：`src/map/skills/archer/doublestrafe.cpp:9-11`

```cpp
void SkillDoubleStrafe::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += 10 * (skill_lv - 1);
}
```

### Arrow Shower (`AC_SHOWER`)

武器/物理技能；目标：地面区域；最高等级 10；射程：-9；命中类型：Single；段数：1；属性：Weapon；范围：2；击退：2；持续时间1：100 ms；伤害标记：Splash；消耗/限制：SP 15；弹药数 1；武器 Bow；弹药 Arrow。

- 覆盖：`exact-class-methods`
- 实现类：`SkillArrowShower`
- 实现文件：`src/map/skills/archer/arrowshower.cpp`

#### `SkillArrowShower::SkillArrowShower`

来源：`src/map/skills/archer/arrowshower.cpp:8-9`

```cpp
SkillArrowShower::SkillArrowShower() : SkillImplRecursiveDamageSplash(AC_SHOWER) {
}
```

#### `SkillArrowShower::calculateSkillRatio`

来源：`src/map/skills/archer/arrowshower.cpp:11-17`

```cpp
void SkillArrowShower::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 50 + 10 * skill_lv;
#else
	base_skillratio += -25 + 5 * skill_lv;
#endif
}
```

#### `SkillArrowShower::castendPos2`

来源：`src/map/skills/archer/arrowshower.cpp:19-23`

```cpp
void SkillArrowShower::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_change_end(src, SC_CAMOUFLAGE);

	SkillImplRecursiveDamageSplash::castendPos2(src, x, y, skill_lv, tick, flag);
}
```

### Arrow Crafting (`AC_MAKINGARROW`)

武器/物理技能；目标：自身；最高等级 1；伤害标记：NoDamage；消耗/限制：SP 10；状态 Recover_Weight_Rate。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMakingArrow`
- 实现文件：`src/map/skills/archer/makingarrow.cpp`

#### `SkillMakingArrow::SkillMakingArrow`

来源：`src/map/skills/archer/makingarrow.cpp:9-11`

```cpp
SkillMakingArrow::SkillMakingArrow() : SkillImpl(AC_MAKINGARROW)
{
}
```

#### `SkillMakingArrow::castendNoDamageId`

来源：`src/map/skills/archer/makingarrow.cpp:13-22`

```cpp
void SkillMakingArrow::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const
{
	map_session_data *sd = BL_CAST(BL_PC, src);

	if (sd != nullptr)
	{
		clif_arrow_create_list(*sd);
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
	}
}
```

### Arrow Repel (`AC_CHARGEARROW`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：-9；命中类型：Single；段数：1；属性：Weapon；击退：6；吟唱：1500 ms；伤害标记：Splash；消耗/限制：SP 15；弹药数 1；武器 Bow；弹药 Arrow。

- 覆盖：`exact-class-methods`
- 实现类：`SkillChargeArrow`
- 实现文件：`src/map/skills/archer/chargearrow.cpp`

#### `SkillChargeArrow::SkillChargeArrow`

来源：`src/map/skills/archer/chargearrow.cpp:6-8`

```cpp
SkillChargeArrow::SkillChargeArrow() : WeaponSkillImpl(AC_CHARGEARROW)
{
}
```

#### `SkillChargeArrow::calculateSkillRatio`

来源：`src/map/skills/archer/chargearrow.cpp:10-13`

```cpp
void SkillChargeArrow::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const
{
	base_skillratio += 50;
}
```
