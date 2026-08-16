# Taekwon 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 411 | `TK_RUN` / Running | `exact-class-methods` | `SkillRun` | src/map/skills/taekwon/run.cpp |
| 412 | `TK_READYSTORM` / Tornado Stance | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 413 | `TK_STORMKICK` / Tornado Kick | `exact-class-methods` | `SkillStormKick` | src/map/skills/taekwon/stormkick.cpp |
| 414 | `TK_READYDOWN` / Heel Drop Stance | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 415 | `TK_DOWNKICK` / Heel Drop | `exact-class-methods` | `SkillDownKick` | src/map/skills/taekwon/downkick.cpp |
| 416 | `TK_READYTURN` / Roundhouse Stance | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 417 | `TK_TURNKICK` / Roundhouse Kick | `exact-class-methods` | `SkillTurnKick` | src/map/skills/taekwon/turnkick.cpp |
| 418 | `TK_READYCOUNTER` / Counter Kick Stance | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 419 | `TK_COUNTER` / Counter Kick | `exact-class-methods` | `SkillCounter` | src/map/skills/taekwon/counter.cpp |
| 420 | `TK_DODGE` / Tumbling | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 421 | `TK_JUMPKICK` / Flying Kick | `exact-class-methods` | `SkillJumpKick` | src/map/skills/taekwon/jumpkick.cpp |
| 422 | `TK_HPTIME` / Peaceful Break | `core-source-references` | `` | src/map/skill.cpp, src/map/status.cpp |
| 423 | `TK_SPTIME` / Happy Break | `core-source-references` | `` | src/map/skill.cpp, src/map/status.cpp |
| 424 | `TK_POWER` / Kihop | `core-source-references` | `` | src/map/battle.cpp |
| 425 | `TK_SEVENWIND` / Mild Wind | `exact-class-methods` | `SkillSevenWind` | src/map/skills/taekwon/sevenwind.cpp |
| 426 | `TK_HIGHJUMP` / Taekwon Jump | `exact-class-methods` | `SkillHighJump` | src/map/skills/taekwon/highjump.cpp |
| 493 | `TK_MISSION` / Taekwon Mission | `exact-class-methods` | `SkillMission` | src/map/skills/taekwon/mission.cpp |

## 详细公式与效果实现

### Running (`TK_RUN`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；击退：4；吟唱：Lv1=6000; Lv2=5000; Lv3=4000; Lv4=3000; Lv5=2000; Lv6=1000 ms；持续时间1：1000 ms；持续时间2：150000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=100; Lv2=90; Lv3=80; Lv4=70; Lv5=60; Lv6=50; Lv7=40; Lv8=30; Lv9=20; Lv10=10；状态 Move_Enable；关联状态：Run。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRun`
- 实现文件：`src/map/skills/taekwon/run.cpp`

#### `SkillRun::SkillRun`

来源：`src/map/skills/taekwon/run.cpp:9-10`

```cpp
SkillRun::SkillRun() : SkillImpl(TK_RUN) {
}
```

#### `SkillRun::castendNoDamageId`

来源：`src/map/skills/taekwon/run.cpp:12-26`

```cpp
void SkillRun::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	sc_type type = skill_get_sc(getSkillId());
	status_change *tsc = status_get_sc(target);
	status_change_entry *tsce = (tsc && type != SC_NONE) ? tsc->getSCE(type) : nullptr;
	map_session_data *sd = BL_CAST(BL_PC, src);

	if (tsce) {
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv, status_change_end(target, type));
		return;
	}

	clif_skill_nodamage(src, *target, getSkillId(), skill_lv, sc_start4(src, target, type, 100, skill_lv, unit_getdir(target), 0, 0, 0));
	if (sd) // If the client receives a skill-use packet inmediately before a walkok packet, it will discard the walk packet! [Skotlex]
		clif_walkok(*sd); // So aegis has to resend the walk ok.
}
```

### Tornado Stance (`TK_READYSTORM`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：ReadyStorm。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:13310
clif_skill_nodamage(bl,*bl,TK_READYSTORM,1);
// src/map/status.cpp:13314
clif_skill_nodamage(bl,*bl,TK_READYDOWN,1);
// src/map/status.cpp:13318
clif_skill_nodamage(bl,*bl,TK_READYTURN,1);
// src/map/status.cpp:13322
clif_skill_nodamage(bl,*bl,TK_READYCOUNTER,1);
```

### Tornado Kick (`TK_STORMKICK`)

武器/物理技能；目标：自身；最高等级 7；射程：-2；命中类型：Multi_Hit；段数：-3；属性：Weapon；范围：2；伤害标记：Splash；消耗/限制：SP Lv1=14; Lv2=12; Lv3=10; Lv4=8; Lv5=6; Lv6=4; Lv7=2。

- 覆盖：`exact-class-methods`
- 实现类：`SkillStormKick`
- 实现文件：`src/map/skills/taekwon/stormkick.cpp`

#### `SkillStormKick::SkillStormKick`

来源：`src/map/skills/taekwon/stormkick.cpp:8-9`

```cpp
SkillStormKick::SkillStormKick() : SkillImpl(TK_STORMKICK) {
}
```

#### `SkillStormKick::calculateSkillRatio`

来源：`src/map/skills/taekwon/stormkick.cpp:11-13`

```cpp
void SkillStormKick::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 60 + 20 * skill_lv;
}
```

#### `SkillStormKick::castendDamageId`

来源：`src/map/skills/taekwon/stormkick.cpp:15-21`

```cpp
void SkillStormKick::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
	skill_area_temp[1] = 0;
	map_foreachinshootrange(skill_attack_area, src,
	                        skill_get_splash(getSkillId(), skill_lv), BL_CHAR | BL_SKILL,
	                        BF_WEAPON, src, src, getSkillId(), skill_lv, tick, flag, BCT_ENEMY);
}
```

### Heel Drop Stance (`TK_READYDOWN`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：ReadyDown。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:13310
clif_skill_nodamage(bl,*bl,TK_READYSTORM,1);
// src/map/status.cpp:13314
clif_skill_nodamage(bl,*bl,TK_READYDOWN,1);
// src/map/status.cpp:13318
clif_skill_nodamage(bl,*bl,TK_READYTURN,1);
// src/map/status.cpp:13322
clif_skill_nodamage(bl,*bl,TK_READYCOUNTER,1);
```

### Heel Drop (`TK_DOWNKICK`)

武器/物理技能；目标：自身；最高等级 7；射程：-2；命中类型：Multi_Hit；段数：-3；属性：Weapon；持续时间2：3000 ms；消耗/限制：SP Lv1=14; Lv2=12; Lv3=10; Lv4=8; Lv5=6; Lv6=4; Lv7=2；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDownKick`
- 实现文件：`src/map/skills/taekwon/downkick.cpp`

#### `SkillDownKick::SkillDownKick`

来源：`src/map/skills/taekwon/downkick.cpp:8-9`

```cpp
SkillDownKick::SkillDownKick() : WeaponSkillImpl(TK_DOWNKICK) {
}
```

#### `SkillDownKick::calculateSkillRatio`

来源：`src/map/skills/taekwon/downkick.cpp:11-13`

```cpp
void SkillDownKick::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 60 + 20 * skill_lv;
}
```

#### `SkillDownKick::applyAdditionalEffects`

来源：`src/map/skills/taekwon/downkick.cpp:15-17`

```cpp
void SkillDownKick::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src, target, SC_STUN, 3333, skill_lv, skill_get_time2(getSkillId(), skill_lv));
}
```

### Roundhouse Stance (`TK_READYTURN`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：ReadyTurn。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:13310
clif_skill_nodamage(bl,*bl,TK_READYSTORM,1);
// src/map/status.cpp:13314
clif_skill_nodamage(bl,*bl,TK_READYDOWN,1);
// src/map/status.cpp:13318
clif_skill_nodamage(bl,*bl,TK_READYTURN,1);
// src/map/status.cpp:13322
clif_skill_nodamage(bl,*bl,TK_READYCOUNTER,1);
```

### Roundhouse Kick (`TK_TURNKICK`)

武器/物理技能；目标：自身；最高等级 7；射程：-2；命中类型：Multi_Hit；段数：-3；属性：Weapon；范围：1；击退：2；持续时间1：5000 ms；持续时间2：2000 ms；伤害标记：Splash；消耗/限制：SP Lv1=14; Lv2=12; Lv3=10; Lv4=8; Lv5=6; Lv6=4; Lv7=2。

- 覆盖：`exact-class-methods`
- 实现类：`SkillTurnKick`
- 实现文件：`src/map/skills/taekwon/turnkick.cpp`

#### `SkillTurnKick::SkillTurnKick`

来源：`src/map/skills/taekwon/turnkick.cpp:9-10`

```cpp
SkillTurnKick::SkillTurnKick() : SkillImpl(TK_TURNKICK) {
}
```

#### `SkillTurnKick::modifyDamageData`

来源：`src/map/skills/taekwon/turnkick.cpp:12-14`

```cpp
void SkillTurnKick::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	dmg.blewcount = 0;
}
```

#### `SkillTurnKick::calculateSkillRatio`

来源：`src/map/skills/taekwon/turnkick.cpp:16-18`

```cpp
void SkillTurnKick::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 90 + 30 * skill_lv;
}
```

#### `SkillTurnKick::applyAdditionalEffects`

来源：`src/map/skills/taekwon/turnkick.cpp:20-27`

```cpp
void SkillTurnKick::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	// Note: attack_type is passed as BF_WEAPON for the actual target, BF_MISC for the splash-affected mobs.
	if (attack_type & BF_MISC) {
		sc_start(src, target, SC_STUN, 200, skill_lv, skill_get_time(getSkillId(), skill_lv));
		clif_specialeffect(target, EF_SPINEDBODY, AREA);
		sc_start(src, target, SC_NOACTION, 100, 1, skill_get_time2(getSkillId(), skill_lv));
	}
}
```

#### `SkillTurnKick::castendDamageId`

来源：`src/map/skills/taekwon/turnkick.cpp:29-39`

```cpp
void SkillTurnKick::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	// Active part of the attack.
	// Note: skill_area_temp[1] is used in castendNoDamageId to avoid affecting the target.
	skill_area_temp[1] = target->id;

	if (skill_attack(BF_WEAPON, src, src, target, getSkillId(), skill_lv, tick, flag))
		map_foreachinallrange(skill_area_sub, target,
		                      skill_get_splash(getSkillId(), skill_lv), BL_MOB,
		                      src, getSkillId(), skill_lv, tick, flag | BCT_ENEMY | 1,
		                      skill_castend_nodamage_id);
}
```

#### `SkillTurnKick::castendNoDamageId`

来源：`src/map/skills/taekwon/turnkick.cpp:41-47`

```cpp
void SkillTurnKick::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	// Passive part of the attack. Splash knock-back+stun.
	if (skill_area_temp[1] != target->id) {
		skill_blown(src, target, skill_get_blewcount(getSkillId(), skill_lv), -1, BLOWN_NONE);
		skill_additional_effect(src, target, getSkillId(), skill_lv, BF_MISC, ATK_DEF, tick); // Use Misc rather than weapon to signal passive pushback
	}
}
```

### Counter Kick Stance (`TK_READYCOUNTER`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：ReadyCounter。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:13310
clif_skill_nodamage(bl,*bl,TK_READYSTORM,1);
// src/map/status.cpp:13314
clif_skill_nodamage(bl,*bl,TK_READYDOWN,1);
// src/map/status.cpp:13318
clif_skill_nodamage(bl,*bl,TK_READYTURN,1);
// src/map/status.cpp:13322
clif_skill_nodamage(bl,*bl,TK_READYCOUNTER,1);
```

### Counter Kick (`TK_COUNTER`)

武器/物理技能；目标：自身；最高等级 7；射程：-2；命中类型：Multi_Hit；段数：-3；属性：Weapon；伤害标记：IgnoreFlee；消耗/限制：SP Lv1=14; Lv2=12; Lv3=10; Lv4=8; Lv5=6; Lv6=4; Lv7=2。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCounter`
- 实现文件：`src/map/skills/taekwon/counter.cpp`

#### `SkillCounter::SkillCounter`

来源：`src/map/skills/taekwon/counter.cpp:6-7`

```cpp
SkillCounter::SkillCounter() : WeaponSkillImpl(TK_COUNTER) {
}
```

#### `SkillCounter::calculateSkillRatio`

来源：`src/map/skills/taekwon/counter.cpp:9-11`

```cpp
void SkillCounter::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 90 + 30 * skill_lv;
}
```

### Tumbling (`TK_DODGE`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：Dodge。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:1591
clif_skill_nodamage(target, *target, LK_PARRYING, sce->val1);
// src/map/battle.cpp:1592
unit_set_attackdelay(*target, gettick(), DELAY_EVENT_PARRY);
// src/map/battle.cpp:1601
clif_skill_nodamage(target, *target, TK_DODGE, 1);
// src/map/battle.cpp:1602
sc_start4(src, target, SC_COMBO, 100, TK_JUMPKICK, src->id, 1, 0, 2000);
// src/map/battle.cpp:1606
if ((sce = sc->getSCE(SC_KAUPE)) && (skill_id != NPC_EARTHQUAKE || (skill_id == NPC_EARTHQUAKE && flag & NPC_EARTHQUAKE_FLAG)) && rnd() % 100 < sce->val2) { //Kaupe blocks damage (skill or otherwise) from players, mobs, homuns, mercenaries.
// src/map/battle.cpp:1613
status_change_end(target, SC_KAUPE);
```

### Flying Kick (`TK_JUMPKICK`)

武器/物理技能；目标：敌方目标；最高等级 7；射程：9；命中类型：Multi_Hit；段数：-3；属性：Weapon；伤害标记：NoDamage；消耗/限制：SP Lv1=70; Lv2=60; Lv3=50; Lv4=40; Lv5=30; Lv6=20; Lv7=10。

- 覆盖：`exact-class-methods`
- 实现类：`SkillJumpKick`
- 实现文件：`src/map/skills/taekwon/jumpkick.cpp`

#### `SkillJumpKick::SkillJumpKick`

来源：`src/map/skills/taekwon/jumpkick.cpp:11-12`

```cpp
SkillJumpKick::SkillJumpKick() : SkillImpl(TK_JUMPKICK) {
}
```

#### `SkillJumpKick::calculateSkillRatio`

来源：`src/map/skills/taekwon/jumpkick.cpp:14-25`

```cpp
void SkillJumpKick::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_change *sc = status_get_sc(src);
	// Different damage formulas depending on damage trigger
	if (sc && sc->getSCE(SC_COMBO) && sc->getSCE(SC_COMBO)->val1 == getSkillId())
		base_skillratio += -100 + 4 * status_get_lv(src); // Tumble formula [4%*baselevel]
	else if (wd->miscflag) {
		base_skillratio += -100 + 4 * status_get_lv(src); // Running formula [4%*baselevel]
		if (sc && sc->getSCE(SC_SPURT)) // Spurt formula [8%*baselevel]
			base_skillratio *= 2;
	} else
		base_skillratio += -70 + 10 * skill_lv;
}
```

#### `SkillJumpKick::applyAdditionalEffects`

来源：`src/map/skills/taekwon/jumpkick.cpp:27-47`

```cpp
void SkillJumpKick::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	status_change *tsc = status_get_sc(target);
	map_session_data *dstsd = BL_CAST(BL_PC, target);

	// debuff the following statuses
	if (dstsd && dstsd->class_ != MAPID_SOUL_LINKER && tsc != nullptr && !tsc->getSCE(SC_PRESERVE)) {
		status_change_end(target, SC_SPIRIT);
		status_change_end(target, SC_ADRENALINE2);
		status_change_end(target, SC_KAITE);
		status_change_end(target, SC_KAAHI);
		status_change_end(target, SC_ONEHAND);
		status_change_end(target, SC_ASPDPOTION2);
		// New soul links confirmed to not dispell with this skill
		// but thats likely a bug since soul links can't stack and
		// soul cutter skill works on them. So ill add this here for now. [Rytech]
		status_change_end(target, SC_SOULGOLEM);
		status_change_end(target, SC_SOULSHADOW);
		status_change_end(target, SC_SOULFALCON);
		status_change_end(target, SC_SOULFAIRY);
	}
}
```

#### `SkillJumpKick::castendNoDamageId`

来源：`src/map/skills/taekwon/jumpkick.cpp:49-61`

```cpp
void SkillJumpKick::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);

	/* Check if the target is an enemy; if not, skill should fail so the character doesn't unit_movepos (exploitable) */
	if (battle_check_target(src, target, BCT_ENEMY) > 0) {
		if (unit_movepos(src, target->x, target->y, 2, 1)) {
			skill_attack(BF_WEAPON, src, src, target, getSkillId(), skill_lv, tick, flag);
			clif_blown(src);
		}
	} else if (sd) {
		clif_skill_fail(*sd, getSkillId(), USESKILL_FAIL);
	}
}
```

### Peaceful Break (`TK_HPTIME`)

非伤害技能；目标：被动；最高等级 10；范围：1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:10799
status_calc_regen_rate(bl, &sd->regen, &sd->sc);
// src/map/status.cpp:5322
sregen->sp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5333
sregen->hp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5343
sregen->sp = cap_value(val, 0, SHRT_MAX);
```

### Happy Break (`TK_SPTIME`)

非伤害技能；目标：被动；最高等级 10；范围：1；持续时间1：1800000 ms；关联状态：EarthScroll。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:10799
status_calc_regen_rate(bl, &sd->regen, &sd->sc);
// src/map/status.cpp:5333
sregen->hp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5343
sregen->sp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:15626
sregen->tick.hp -= battle_config.natural_heal_skill_interval;
// src/map/status.cpp:15627
if(status_heal(bl, sregen->hp, 0, 3) < sregen->hp)
// src/map/status.cpp:15631
if(flag&RGN_SSP) { // Skill SP regen
// src/map/status.cpp:15632
sregen->tick.sp += (int32)(natural_heal_diff_tick * (sregen->rate.sp /100.));
// src/map/status.cpp:15633
while(sregen->tick.sp >= (uint32)battle_config.natural_heal_skill_interval) {
// src/map/status.cpp:15634
int32 val = sregen->sp;
// src/map/status.cpp:15638
if ((rate = pc_checkskill(sd,TK_SPTIME)))
// src/map/status.cpp:15639
sc_start(bl,bl,skill_get_sc(TK_SPTIME),
// src/map/status.cpp:15640
100,rate,skill_get_time(TK_SPTIME, rate));
// src/map/status.cpp:15643
rnd()%10000 < battle_config.sg_angel_skill_ratio
// src/map/status.cpp:15650
sregen->tick.sp -= battle_config.natural_heal_skill_interval;
// src/map/status.cpp:15651
if(status_heal(bl, 0, val, 3) < val)
```

### Kihop (`TK_POWER`)

武器/物理技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:4197
if (bflag & BDMG_CRIT) { // add +crit damage bonuses here in pre-renewal mode [helvetica]
// src/map/battle.cpp:4198
if (sd->bonus.crit_atk_rate > 0) {
// src/map/battle.cpp:4199
ATK_ADDRATE(wd->damage, wd->damage2, sd->bonus.crit_atk_rate);
// src/map/battle.cpp:4204
if (sd->bonus.non_crit_atk_rate > 0) {
// src/map/battle.cpp:4205
ATK_ADDRATE(wd->damage, wd->damage2, sd->bonus.non_crit_atk_rate);
// src/map/battle.cpp:4213
ATK_ADDRATE(wd->damage, wd->damage2, 2*skill*i);
// src/map/battle.cpp:4220
ATK_ADDRATE(wd->damage, wd->damage2, dmg_bonus);
// src/map/battle.cpp:4221
RE_ALLATK_ADDRATE(wd, dmg_bonus);
// src/map/battle.cpp:4226
if (tsd != nullptr && tsd->bonus.crit_def_rate != 0 && !skill_id && (bflag & BDMG_CRIT)) {
// src/map/battle.cpp:4227
ATK_ADDRATE(wd->damage, wd->damage2, -tsd->bonus.crit_def_rate);
```

### Mild Wind (`TK_SEVENWIND`)

武器/物理技能；目标：自身；最高等级 7；命中类型：Single；段数：1；属性：Lv1=Earth; Lv2=Wind; Lv3=Water; Lv4=Fire; Lv5=Ghost; Lv6=Dark; Lv7=Holy；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-4=20; Lv5-7=50；关联状态：SevenWind。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSevenWind`
- 实现文件：`src/map/skills/taekwon/sevenwind.cpp`

#### `SkillSevenWind::SkillSevenWind`

来源：`src/map/skills/taekwon/sevenwind.cpp:9-10`

```cpp
SkillSevenWind::SkillSevenWind() : SkillImpl(TK_SEVENWIND) {
}
```

#### `SkillSevenWind::castendNoDamageId`

来源：`src/map/skills/taekwon/sevenwind.cpp:12-41`

```cpp
void SkillSevenWind::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	sc_type type = SC_NONE;

	switch (skill_get_ele(getSkillId(), skill_lv)) {
		case ELE_EARTH:
			type = SC_EARTHWEAPON;
			break;
		case ELE_WIND:
			type = SC_WINDWEAPON;
			break;
		case ELE_WATER:
			type = SC_WATERWEAPON;
			break;
		case ELE_FIRE:
			type = SC_FIREWEAPON;
			break;
		case ELE_GHOST:
			type = SC_GHOSTWEAPON;
			break;
		case ELE_DARK:
			type = SC_SHADOWWEAPON;
			break;
		case ELE_HOLY:
			type = SC_ASPERSIO;
			break;
	}

	clif_skill_nodamage(src, *target, getSkillId(), skill_lv, sc_start(src, target, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
	sc_start(src, target, SC_SEVENWIND, 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
}
```

### Taekwon Jump (`TK_HIGHJUMP`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；吟唱：Lv1=5000; Lv2=4000; Lv3=3000; Lv4=2000; Lv5=1000 ms；伤害标记：NoDamage；消耗/限制：SP 50。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHighJump`
- 实现文件：`src/map/skills/taekwon/highjump.cpp`

#### `SkillHighJump::SkillHighJump`

来源：`src/map/skills/taekwon/highjump.cpp:9-10`

```cpp
SkillHighJump::SkillHighJump() : SkillImpl(TK_HIGHJUMP) {
}
```

#### `SkillHighJump::castendNoDamageId`

来源：`src/map/skills/taekwon/highjump.cpp:12-37`

```cpp
void SkillHighJump::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	int32 x, y, dir = unit_getdir(src);
	map_data *mapdata = map_getmapdata(src->m);

	// Fails on noteleport maps, except for GvG and BG maps [Skotlex]
	if (mapdata->getMapFlag(MF_NOTELEPORT) && !(mapdata->getMapFlag(MF_BATTLEGROUND) || mapdata_flag_gvg(mapdata))) {
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
		return;
	} else if (dir % 2) {
		// Diagonal
		x = src->x + dirx[dir] * (skill_lv * 4) / 3;
		y = src->y + diry[dir] * (skill_lv * 4) / 3;
	} else {
		x = src->x + dirx[dir] * skill_lv * 2;
		y = src->y + diry[dir] * skill_lv * 2;
	}

	int32 x1 = x + dirx[dir];
	int32 y1 = y + diry[dir];

	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
	if (!map_count_oncell(src->m, x, y, BL_PC | BL_NPC | BL_MOB, 0) && map_getcell(src->m, x, y, CELL_CHKREACH) &&
	    !map_count_oncell(src->m, x1, y1, BL_PC | BL_NPC | BL_MOB, 0) && map_getcell(src->m, x1, y1, CELL_CHKREACH) &&
	    unit_movepos(src, x, y, 1, 0))
		clif_blown(src);
}
```

### Taekwon Mission (`TK_MISSION`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：1000 ms；伤害标记：NoDamage；消耗/限制：SP 10。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMission`
- 实现文件：`src/map/skills/taekwon/mission.cpp`

#### `SkillMission::SkillMission`

来源：`src/map/skills/taekwon/mission.cpp:10-11`

```cpp
SkillMission::SkillMission() : SkillImpl(TK_MISSION) {
}
```

#### `SkillMission::castendNoDamageId`

来源：`src/map/skills/taekwon/mission.cpp:13-36`

```cpp
void SkillMission::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);

	if (sd) {
		if (sd->mission_mobid && (sd->mission_count || rnd() % 100)) {
			// Cannot change target when already have one
			clif_mission_info(sd, sd->mission_mobid, sd->mission_count);
			clif_skill_fail(*sd, getSkillId());
			return;
		}

		int32 id = mob_get_random_id(MOBG_TAEKWON_MISSION, RMF_NONE, 0);

		if (!id) {
			clif_skill_fail(*sd, getSkillId());
			return;
		}
		sd->mission_mobid = id;
		sd->mission_count = 0;
		pc_setglobalreg(sd, add_str(TKMISSIONID_VAR), id);
		clif_mission_info(sd, id, 0);
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
	}
}
```
