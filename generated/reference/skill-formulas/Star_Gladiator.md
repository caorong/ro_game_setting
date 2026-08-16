# Star_Gladiator 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 427 | `SG_FEEL` / Feeling the Sun Moon and Stars | `exact-class-methods` | `SkillFeelingtheSunMoonandStars` | src/map/skills/taekwon/feelingthesunmoonandstars.cpp |
| 428 | `SG_SUN_WARM` / Warmth of the Sun | `exact-class-methods` | `SkillWarmthoftheSun` | src/map/skills/taekwon/warmthofthesun.cpp |
| 429 | `SG_MOON_WARM` / Warmth of the Moon | `exact-class-methods` | `SkillWarmthoftheMoon` | src/map/skills/taekwon/warmthofthemoon.cpp |
| 430 | `SG_STAR_WARM` / Warmth of the Stars | `exact-class-methods` | `SkillWarmthoftheStars` | src/map/skills/taekwon/warmthofthestars.cpp |
| 431 | `SG_SUN_COMFORT` / Comfort of the Sun | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 432 | `SG_MOON_COMFORT` / Comfort of the Moon | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 433 | `SG_STAR_COMFORT` / Comfort of the Stars | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 434 | `SG_HATE` / Hatred of the Sun Moon and Stars | `exact-class-methods` | `SkillHatredoftheSunMoonandStars` | src/map/skills/taekwon/hatredofthesunmoonandstars.cpp |
| 435 | `SG_SUN_ANGER` / Anger of the Sun | `core-source-references` | `` | src/map/pc.cpp |
| 436 | `SG_MOON_ANGER` / Anger of the Moon | `core-source-references` | `` | src/map/pc.cpp |
| 437 | `SG_STAR_ANGER` / Anger of the Stars | `core-source-references` | `` | src/map/battle.cpp, src/map/pc.cpp |
| 438 | `SG_SUN_BLESS` / Blessing of the Sun | `core-source-references` | `` | src/map/pc.cpp |
| 439 | `SG_MOON_BLESS` / Blessing of the Moon | `core-source-references` | `` | src/map/pc.cpp |
| 440 | `SG_STAR_BLESS` / Blessing of the Stars | `core-source-references` | `` | src/map/pc.cpp |
| 441 | `SG_DEVIL` / Demon of the Sun Moon and Stars | `core-source-references` | `` | src/map/pc.cpp, src/map/status.cpp |
| 442 | `SG_FRIEND` / Friend of the Sun Moon and Stars | `core-source-references` | `` | src/map/skill.cpp |
| 443 | `SG_KNOWLEDGE` / Knowledge of the Sun Moon and Stars | `metadata-only` | `` |  |
| 444 | `SG_FUSION` / Union of the Sun Moon and Stars | `generic-or-class-mapped` | `StatusSkillImpl` |  |

## 详细公式与效果实现

### Feeling the Sun Moon and Stars (`SG_FEEL`)

魔法技能；目标：自身；最高等级 3；命中类型：Single；段数：1；吟唱：1000 ms；伤害标记：NoDamage；消耗/限制：SP 100。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFeelingtheSunMoonandStars`
- 实现文件：`src/map/skills/taekwon/feelingthesunmoonandstars.cpp`

#### `SkillFeelingtheSunMoonandStars::SkillFeelingtheSunMoonandStars`

来源：`src/map/skills/taekwon/feelingthesunmoonandstars.cpp:9-10`

```cpp
SkillFeelingtheSunMoonandStars::SkillFeelingtheSunMoonandStars() : SkillImpl(SG_FEEL) {
}
```

#### `SkillFeelingtheSunMoonandStars::castendNoDamageId`

来源：`src/map/skills/taekwon/feelingthesunmoonandstars.cpp:12-22`

```cpp
void SkillFeelingtheSunMoonandStars::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	//AuronX reported you CAN memorize the same map as all three. [Skotlex]
	if (sd) {
		if(!sd->feel_map[skill_lv-1].index)
			clif_feel_req(sd->fd,sd, skill_lv);
		else
			clif_feel_info(sd, skill_lv-1, 1);
	}
}
```

### Warmth of the Sun (`SG_SUN_WARM`)

武器/物理技能；目标：自身；最高等级 3；射程：1；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：2；持续时间1：Lv1=10000; Lv2=20000; Lv3=60000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 20；关联状态：Warm。

- 覆盖：`exact-class-methods`
- 实现类：`SkillWarmthoftheSun`
- 实现文件：`src/map/skills/taekwon/warmthofthesun.cpp`

#### `SkillWarmthoftheSun::SkillWarmthoftheSun`

来源：`src/map/skills/taekwon/warmthofthesun.cpp:10-11`

```cpp
SkillWarmthoftheSun::SkillWarmthoftheSun() : SkillImpl(SG_SUN_WARM) {
}
```

#### `SkillWarmthoftheSun::modifyDamageData`

来源：`src/map/skills/taekwon/warmthofthesun.cpp:13-16`

```cpp
void SkillWarmthoftheSun::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	// A random 0~3 knockback bonus is added to the base knockback
	dmg.blewcount += rnd_value(0, 3);
}
```

#### `SkillWarmthoftheSun::castendPos2`

来源：`src/map/skills/taekwon/warmthofthesun.cpp:18-26`

```cpp
void SkillWarmthoftheSun::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	std::shared_ptr<s_skill_unit_group> sg;

	skill_clear_unitgroup(src);
	if ((sg = skill_unitsetting(src,getSkillId(),skill_lv,src->x,src->y,0)))
		sc_start4(src,src,type,100,skill_lv,0,0,sg->group_id,skill_get_time(getSkillId(),skill_lv));
	flag|=1;
}
```

### Warmth of the Moon (`SG_MOON_WARM`)

武器/物理技能；目标：自身；最高等级 3；射程：1；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：2；持续时间1：Lv1=10000; Lv2=20000; Lv3=60000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 20；关联状态：Warm。

- 覆盖：`exact-class-methods`
- 实现类：`SkillWarmthoftheMoon`
- 实现文件：`src/map/skills/taekwon/warmthofthemoon.cpp`

#### `SkillWarmthoftheMoon::SkillWarmthoftheMoon`

来源：`src/map/skills/taekwon/warmthofthemoon.cpp:10-11`

```cpp
SkillWarmthoftheMoon::SkillWarmthoftheMoon() : SkillImpl(SG_MOON_WARM) {
}
```

#### `SkillWarmthoftheMoon::modifyDamageData`

来源：`src/map/skills/taekwon/warmthofthemoon.cpp:13-16`

```cpp
void SkillWarmthoftheMoon::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	// A random 0~3 knockback bonus is added to the base knockback
	dmg.blewcount += rnd_value(0, 3);
}
```

#### `SkillWarmthoftheMoon::castendPos2`

来源：`src/map/skills/taekwon/warmthofthemoon.cpp:18-26`

```cpp
void SkillWarmthoftheMoon::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	std::shared_ptr<s_skill_unit_group> sg;

	skill_clear_unitgroup(src);
	if ((sg = skill_unitsetting(src,getSkillId(),skill_lv,src->x,src->y,0)))
		sc_start4(src,src,type,100,skill_lv,0,0,sg->group_id,skill_get_time(getSkillId(),skill_lv));
	flag|=1;
}
```

### Warmth of the Stars (`SG_STAR_WARM`)

武器/物理技能；目标：自身；最高等级 3；射程：1；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：2；持续时间1：Lv1=10000; Lv2=20000; Lv3=60000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 10；关联状态：Warm。

- 覆盖：`exact-class-methods`
- 实现类：`SkillWarmthoftheStars`
- 实现文件：`src/map/skills/taekwon/warmthofthestars.cpp`

#### `SkillWarmthoftheStars::SkillWarmthoftheStars`

来源：`src/map/skills/taekwon/warmthofthestars.cpp:10-11`

```cpp
SkillWarmthoftheStars::SkillWarmthoftheStars() : SkillImpl(SG_STAR_WARM) {
}
```

#### `SkillWarmthoftheStars::modifyDamageData`

来源：`src/map/skills/taekwon/warmthofthestars.cpp:13-16`

```cpp
void SkillWarmthoftheStars::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	// A random 0~3 knockback bonus is added to the base knockback
	dmg.blewcount += rnd_value(0, 3);
}
```

#### `SkillWarmthoftheStars::castendPos2`

来源：`src/map/skills/taekwon/warmthofthestars.cpp:18-26`

```cpp
void SkillWarmthoftheStars::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	std::shared_ptr<s_skill_unit_group> sg;

	skill_clear_unitgroup(src);
	if ((sg = skill_unitsetting(src,getSkillId(),skill_lv,src->x,src->y,0)))
		sc_start4(src,src,type,100,skill_lv,0,0,sg->group_id,skill_get_time(getSkillId(),skill_lv));
	flag|=1;
}
```

### Comfort of the Sun (`SG_SUN_COMFORT`)

魔法技能；目标：自身；最高等级 4；段数：1；技能后摇：1000 ms；持续时间1：Lv1=80000; Lv2=160000; Lv3=240000; Lv4=320000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=70; Lv2=60; Lv3=50; Lv4=40；关联状态：Sun_Comfort。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
// src/map/skill.cpp:8622
if (!party_skill_check(&sd, sd.status.party_id, skill_id, skill_lv)) {
// src/map/skill.cpp:8643
if( require.sp > 0 ) {
// src/map/skill.cpp:8644
if (status->sp < (uint32)require.sp)
```

### Comfort of the Moon (`SG_MOON_COMFORT`)

魔法技能；目标：自身；最高等级 4；段数：1；技能后摇：1000 ms；持续时间1：Lv1=80000; Lv2=160000; Lv3=240000; Lv4=320000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=70; Lv2=60; Lv3=50; Lv4=40；关联状态：Moon_Comfort。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
// src/map/skill.cpp:8622
if (!party_skill_check(&sd, sd.status.party_id, skill_id, skill_lv)) {
```

### Comfort of the Stars (`SG_STAR_COMFORT`)

魔法技能；目标：自身；最高等级 4；段数：1；技能后摇：1000 ms；持续时间1：Lv1=80000; Lv2=160000; Lv3=240000; Lv4=320000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=70; Lv2=60; Lv3=50; Lv4=40；关联状态：Star_Comfort。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
// src/map/skill.cpp:8622
if (!party_skill_check(&sd, sd.status.party_id, skill_id, skill_lv)) {
```

### Hatred of the Sun Moon and Stars (`SG_HATE`)

魔法技能；目标：敌方目标；最高等级 3；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；伤害标记：NoDamage；消耗/限制：SP 100。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHatredoftheSunMoonandStars`
- 实现文件：`src/map/skills/taekwon/hatredofthesunmoonandstars.cpp`

#### `SkillHatredoftheSunMoonandStars::SkillHatredoftheSunMoonandStars`

来源：`src/map/skills/taekwon/hatredofthesunmoonandstars.cpp:9-10`

```cpp
SkillHatredoftheSunMoonandStars::SkillHatredoftheSunMoonandStars() : SkillImpl(SG_HATE) {
}
```

#### `SkillHatredoftheSunMoonandStars::castendNoDamageId`

来源：`src/map/skills/taekwon/hatredofthesunmoonandstars.cpp:12-20`

```cpp
void SkillHatredoftheSunMoonandStars::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	if (sd) {
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
		if (!pc_set_hate_mob(sd, skill_lv-1, target))
			clif_skill_fail( *sd, getSkillId() );
	}
}
```

### Anger of the Sun (`SG_SUN_ANGER`)

非伤害技能；目标：被动；最高等级 3。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
```

### Anger of the Moon (`SG_MOON_ANGER`)

非伤害技能；目标：被动；最高等级 3。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
```

### Anger of the Stars (`SG_STAR_ANGER`)

非伤害技能；目标：被动；最高等级 3。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/pc.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:4684
RE_ALLATK_ADDRATE(wd, 20);
// src/map/battle.cpp:4693
int32 skillratio = sd->status.base_level + sstatus->dex + sstatus->luk;
// src/map/battle.cpp:4696
skillratio += sstatus->str; // SG_STAR_ANGER additionally has STR added in its formula.
// src/map/battle.cpp:4698
skillratio /= 12 - 3 * anger_level;
// src/map/battle.cpp:4702
skillratio = min( skillratio, 25 * anger_level );
// src/map/battle.cpp:4705
ATK_ADDRATE(wd->damage, wd->damage2, skillratio);
// src/map/battle.cpp:4707
RE_ALLATK_ADDRATE(wd, skillratio);
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
```

### Blessing of the Sun (`SG_SUN_BLESS`)

非伤害技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
```

### Blessing of the Moon (`SG_MOON_BLESS`)

非伤害技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
```

### Blessing of the Stars (`SG_STAR_BLESS`)

非伤害技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:729
* Item Cool Down Delay Saving
```

### Demon of the Sun Moon and Stars (`SG_DEVIL`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:8349
clif_status_change(sd, EFST_DEVIL1, 1, 0, 0, 0, 1); //Permanent blind effect from SG_DEVIL.
// src/map/pc.cpp:9174
clif_status_change(sd, EFST_DEVIL1, 1, 0, 0, 0, 1); //Permanent blind effect from SG_DEVIL.
// src/map/status.cpp:2381
temp_aspd = status->dex * status->dex / 7.0f + status->agi * status->agi * 0.5f;
// src/map/status.cpp:2384
temp_aspd = status->dex * status->dex / 5.0f + status->agi * status->agi * 0.5f;
// src/map/status.cpp:2387
temp_aspd = (float)(sqrt(temp_aspd) * 0.25f) + 196;
// src/map/status.cpp:2388
if ((skill_lv = pc_checkskill(sd,SA_ADVANCEDBOOK)) > 0 && sd->status.weapon == W_BOOK)
// src/map/status.cpp:2389
val += (skill_lv - 1) / 2 + 1;
// src/map/status.cpp:2390
if ((skill_lv = pc_checkskill(sd, SG_DEVIL)) > 0 && ((sd->class_&MAPID_THIRDMASK) == MAPID_STAR_EMPEROR || pc_is_maxjoblv(sd)))
// src/map/status.cpp:2391
val += 1 + skill_lv;
// src/map/status.cpp:2392
if ((skill_lv = pc_checkskill(sd,GS_SINGLEACTION)) > 0 && (sd->status.weapon >= W_REVOLVER && sd->status.weapon <= W_GRENADE))
// src/map/status.cpp:2393
val += ((skill_lv + 1) / 2);
// src/map/status.cpp:2398
aspd = ((int32)(temp_aspd + ((float)(status_calc_aspd(sd, &sd->sc, true) + val) * status->agi / 200)) - min(aspd, 200));
// src/map/status.cpp:2399
return aspd;
// src/map/status.cpp:2402
return AMOTION_ZERO_ASPD;
// src/map/status.cpp:4616
#ifdef RENEWAL_ASPD
// src/map/status.cpp:4618
i = AMOTION_ZERO_ASPD - i * AMOTION_INTERVAL;
```

### Friend of the Sun Moon and Stars (`SG_FRIEND`)

非伤害技能；目标：被动；最高等级 3；持续时间1：10000 ms；关联状态：SkillRate_Up。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:1235
sc_start4(src, src, SC_COMBO, 15, TK_DOWNKICK,
// src/map/skill.cpp:1240
sc_start4(src, src, SC_COMBO, 15, TK_TURNKICK,
// src/map/skill.cpp:1244
else if (sc->getSCE(SC_READYCOUNTER)) { //additional chance from SG_FRIEND [Komurka]
// src/map/skill.cpp:1245
int32 rate = 20;
// src/map/skill.cpp:1246
if (sc->getSCE(SC_SKILLRATE_UP) && sc->getSCE(SC_SKILLRATE_UP)->val1 == TK_COUNTER) {
// src/map/skill.cpp:1247
rate += rate*sc->getSCE(SC_SKILLRATE_UP)->val2 / 100;
// src/map/skill.cpp:1248
status_change_end(src, SC_SKILLRATE_UP);
// src/map/skill.cpp:1250
sc_start4(src, src, SC_COMBO, rate, TK_COUNTER,
// src/map/skill.cpp:2438
duration = 1;
// src/map/skill.cpp:2444
duration = 1;
// src/map/skill.cpp:2450
party_skill_check(sd, sd->status.party_id, skill_id, skill_lv);
// src/map/skill.cpp:2452
duration = 1;
// src/map/skill.cpp:2456
duration = 1;
// src/map/skill.cpp:2460
duration = 1;
// src/map/skill.cpp:2930
case NJ_TATAMIGAESHI: //For correct knockback.
// src/map/skill.cpp:2942
if (skill_lv >= 7) {
```

### Knowledge of the Sun Moon and Stars (`SG_KNOWLEDGE`)

非伤害技能；目标：被动；最高等级 10；持续时间1：600000 ms；关联状态：Knowledge。

- 覆盖：`metadata-only`
- 实现类：`N/A`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Union of the Sun Moon and Stars (`SG_FUSION`)

特殊技能；目标：自身；最高等级 1；命中类型：Single；段数：1；技能后摇：1000 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 100；关联状态：Fusion。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:8643
if( require.sp > 0 ) {
// src/map/skill.cpp:8644
if (status->sp < (uint32)require.sp)
// src/map/skill.cpp:8647
status_zap(&sd, 0, require.sp);
```
