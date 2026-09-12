# Swordman 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 2 | `SM_SWORD` / Sword Mastery | `core-source-references` | `` | src/map/battle.cpp |
| 3 | `SM_TWOHAND` / Two-Handed Sword Mastery | `core-source-references` | `` | src/map/battle.cpp |
| 4 | `SM_RECOVERY` / Increase HP Recovery | `core-source-references` | `` | src/map/pc.cpp, src/map/skills/merchant/aidberserkpotion.cpp, src/map/skills/merchant/aidcondensedpotion.cpp, src/map/skills/merchant/aidpotion.cpp, src/map/status.cpp |
| 5 | `SM_BASH` / Bash | `exact-class-methods` | `SkillBash` | src/map/skills/swordman/bash.cpp |
| 6 | `SM_PROVOKE` / Provoke | `exact-class-methods` | `SkillProvoke` | src/map/skills/swordman/provoke.cpp |
| 7 | `SM_MAGNUM` / Magnum Break | `exact-class-methods` | `SkillMagnumBreak` | src/map/skills/swordman/magnum.cpp |
| 8 | `SM_ENDURE` / Endure | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 144 | `SM_MOVINGRECOVERY` / Moving HP-Recovery | `core-source-references` | `` | src/map/status.cpp |
| 145 | `SM_FATALBLOW` / Fatal Blow | `core-source-references` | `` | src/map/skills/swordman/bash.cpp |
| 146 | `SM_AUTOBERSERK` / Auto Berserk | `exact-class-methods` | `SkillAutoBerserk` | src/map/skills/swordman/autoberserk.cpp |

## 详细公式与效果实现

### Sword Mastery (`SM_SWORD`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2335
damage += (skill * 3);
// src/map/battle.cpp:2339
damage += (skill * 4);
// src/map/battle.cpp:2341
damage += skill * 10;
// src/map/battle.cpp:2345
damage += (skill * 4);
```

### Two-Handed Sword Mastery (`SM_TWOHAND`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2335
damage += (skill * 3);
// src/map/battle.cpp:2339
damage += (skill * 4);
// src/map/battle.cpp:2341
damage += skill * 10;
// src/map/battle.cpp:2345
damage += (skill * 4);
// src/map/battle.cpp:2351
damage += (skill * 4);
// src/map/battle.cpp:2353
damage += (skill * 5);
// src/map/battle.cpp:2356
damage += (skill * 10);
```

### Increase HP Recovery (`SM_RECOVERY`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`, `src/map/skills/merchant/aidberserkpotion.cpp`, `src/map/skills/merchant/aidcondensedpotion.cpp`, `src/map/skills/merchant/aidpotion.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:10688
* Heal player HP and/or SP linearly. Calculate any bonus based on active statuses.
// src/map/pc.cpp:10691
* @param hp: HP to heal
// src/map/pc.cpp:10692
* @param sp: SP to heal
// src/map/pc.cpp:10693
* @return Amount healed to an object
// src/map/pc.cpp:10695
int32 pc_itemheal(map_session_data *sd, t_itemid itemid, int32 hp, int32 sp)
// src/map/pc.cpp:10699
if (hp) {
// src/map/pc.cpp:10705
bonus += bonus; // Receive an additional +100% effect from ranked potions to HP only
// src/map/pc.cpp:10708
bonus += sd->bonus.itemhealrate2;
// src/map/pc.cpp:10710
bonus += bonus * pc_get_itemgroup_bonus(sd, itemid, sd->itemgrouphealrate) / 100;
// src/map/pc.cpp:10712
for(const auto &it : sd->itemhealrate) {
// src/map/skills/merchant/aidberserkpotion.cpp:57
hp = tstatus->max_hp * potion_per_hp / 100;
// src/map/skills/merchant/aidberserkpotion.cpp:58
hp = hp * (100 + pc_checkskill(sd,AM_POTIONPITCHER)*10 + pc_checkskill(sd,AM_LEARNINGPOTION)*5)*bonus/10000;
// src/map/skills/merchant/aidberserkpotion.cpp:60
sp = dstsd->status.max_sp * potion_per_sp / 100;
// src/map/skills/merchant/aidberserkpotion.cpp:61
sp = sp * (100 + pc_checkskill(sd,AM_POTIONPITCHER)*10 + pc_checkskill(sd,AM_LEARNINGPOTION)*5)*bonus/10000;
// src/map/skills/merchant/aidberserkpotion.cpp:65
hp = potion_hp * (100 + pc_checkskill(sd,AM_POTIONPITCHER)*10 + pc_checkskill(sd,AM_LEARNINGPOTION)*5)*bonus/10000;
// src/map/skills/merchant/aidberserkpotion.cpp:66
hp = hp * (100 + (tstatus->vit * 2)) / 100;
```

### Bash (`SM_BASH`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-1；命中类型：Single；段数：1；属性：Weapon；持续时间2：5000 ms；消耗/限制：SP Lv1-5=8; Lv6-10=15；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBash`
- 实现文件：`src/map/skills/swordman/bash.cpp`

#### `SkillBash::SkillBash`

来源：`src/map/skills/swordman/bash.cpp:9-10`

```cpp
SkillBash::SkillBash() : WeaponSkillImpl(SM_BASH) {
}
```

#### `SkillBash::calculateSkillRatio`

来源：`src/map/skills/swordman/bash.cpp:12-15`

```cpp
void SkillBash::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	// Base 100% + 30% per level
	base_skillratio += 30 * skill_lv;
}
```

#### `SkillBash::modifyHitRate`

来源：`src/map/skills/swordman/bash.cpp:17-21`

```cpp
void SkillBash::modifyHitRate(int16& hit_rate, const block_list* src, const block_list* target, uint16 skill_lv) const {
	// It is proven that bonus is applied on final hitrate, not hit.
	// +5% hit per level
	hit_rate += hit_rate * 5 * skill_lv / 100;
}
```

#### `SkillBash::applyAdditionalEffects`

来源：`src/map/skills/swordman/bash.cpp:23-31`

```cpp
void SkillBash::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd != nullptr && skill_lv > 5 && pc_checkskill(sd, SM_FATALBLOW) > 0) {
		// BaseChance gets multiplied with BaseLevel/50.0; 500/50 simplifies to 10 [Playtester]
		int32 stun_chance = (skill_lv - 5) * sd->status.base_level * 10;
		status_change_start(src, target, SC_STUN, stun_chance, skill_lv, 0, 0, 0, skill_get_time2(getSkillId(), skill_lv), SCSTART_NONE);
	}
}
```

### Provoke (`SM_PROVOKE`)

非伤害技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；冷却：1000 ms；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=4; Lv2=5; Lv3=6; Lv4=7; Lv5=8; Lv6=9; Lv7=10; Lv8=11; Lv9=12; Lv10=13；关联状态：Provoke。

- 覆盖：`exact-class-methods`
- 实现类：`SkillProvoke`
- 实现文件：`src/map/skills/swordman/provoke.cpp`

#### `SkillProvoke::SkillProvoke`

来源：`src/map/skills/swordman/provoke.cpp:12-14`

```cpp
SkillProvoke::SkillProvoke() : SkillImpl(SM_PROVOKE)
{
}
```

#### `SkillProvoke::castendNoDamageId`

来源：`src/map/skills/swordman/provoke.cpp:16-46`

```cpp
void SkillProvoke::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
{
	sc_type type = skill_get_sc(getSkillId());
	status_data *tstatus = status_get_status_data(*bl);
	map_session_data *sd = BL_CAST(BL_PC, src);
	mob_data *dstmd = BL_CAST(BL_MOB, bl);

	if (status_has_mode(tstatus, MD_STATUSIMMUNE) || battle_check_undead(tstatus->race, tstatus->def_ele))
	{
		return;
	}
	// Official chance is 70% + 3%*skill_lv + srcBaseLevel% - tarBaseLevel%
	int32 success = sc_start(src, bl, type, 70 + 3 * skill_lv + status_get_lv(src) - status_get_lv(bl), skill_lv, skill_get_time(getSkillId(), skill_lv));
	if (!success)
	{
		if (sd)
			clif_skill_fail(*sd, getSkillId());
		return;
	}
	clif_skill_nodamage(src, *bl, getSkillId(), skill_lv, success != 0);
	unit_skillcastcancel(bl, 2);

	if (dstmd)
	{
		dstmd->state.provoke_flag = src->id;
		mob_target(dstmd, src, skill_get_range2(src, getSkillId(), skill_lv, true));
	}
	// Provoke can cause Coma even though it's a nodamage skill
	if (sd && battle_check_coma(*sd, *bl, BF_MISC))
		status_change_start(src, bl, SC_COMA, 10000, skill_lv, 0, src->id, 0, 0, SCSTART_NONE);
}
```

### Magnum Break (`SM_MAGNUM`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；属性：Fire；范围：Lv1-10=2; Lv11=4；击退：2；技能后摇：2000 ms；持续时间2：10000 ms；伤害标记：Splash；消耗/限制：HP Lv1-2=20; Lv3-4=19; Lv5-6=18; Lv7-8=17; Lv9-10=16；SP 30；关联状态：Watk_Element。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMagnumBreak`
- 实现文件：`src/map/skills/swordman/magnum.cpp`

#### `SkillMagnumBreak::SkillMagnumBreak`

来源：`src/map/skills/swordman/magnum.cpp:13-15`

```cpp
SkillMagnumBreak::SkillMagnumBreak() : SkillImpl(SM_MAGNUM)
{
}
```

#### `SkillMagnumBreak::calculateSkillRatio`

来源：`src/map/skills/swordman/magnum.cpp:17-25`

```cpp
void SkillMagnumBreak::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const
{
	if (wd->miscflag == 1)
	 	// Inner 3x3 circle takes 100%+20%*level damage [Playtester]
		base_skillratio += 20 * skill_lv;
	else
		// Outer 5x5 circle takes 100%+10%*level damage [Playtester]
		base_skillratio += 10 * skill_lv;
}
```

#### `SkillMagnumBreak::modifyHitRate`

来源：`src/map/skills/swordman/magnum.cpp:27-30`

```cpp
void SkillMagnumBreak::modifyHitRate(int16 &hit_rate, const block_list *src, const block_list *target, uint16 skill_lv) const
{
	hit_rate += hit_rate * 10 * skill_lv / 100;
}
```

#### `SkillMagnumBreak::castendDamageId`

来源：`src/map/skills/swordman/magnum.cpp:32-42`

```cpp
void SkillMagnumBreak::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const
{
	map_session_data* sd = BL_CAST( BL_PC, src );

	if (flag & 1)
	{
		// For players, damage depends on distance, so add it to flag if it is > 1
		// Cannot hit hidden targets
		skill_attack(skill_get_type(getSkillId()), src, src, target, getSkillId(), skill_lv, tick, flag | SD_ANIMATION | (sd?distance_bl(src, target):0));
	}
}
```

#### `SkillMagnumBreak::castendNoDamageId`

来源：`src/map/skills/swordman/magnum.cpp:44-58`

```cpp
void SkillMagnumBreak::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
{
	// Passive Magnum, should had been casted on yourself.
	skill_area_temp[1] = 0;
	e_skill skillId = getSkillId();
	map_foreachinshootrange(skill_area_sub, src, skill_get_splash(skillId, skill_lv), BL_SKILL | BL_CHAR,
							src, skillId, skill_lv, tick, flag | BCT_ENEMY | 1, skill_castend_damage_id);
	clif_skill_nodamage(src, *src, skillId, skill_lv);
	// Initiate 20% of your damage becomes fire element.
#ifdef RENEWAL
	sc_start4(src, src, SC_SUB_WEAPONPROPERTY, 100, ELE_FIRE, 20, skillId, 0, skill_get_time2(skillId, skill_lv));
#else
	sc_start4(src, src, SC_WATK_ELEMENT, 100, ELE_FIRE, 20, 0, 0, skill_get_time2(skillId, skill_lv));
#endif
}
```

### Endure (`SM_ENDURE`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；冷却：10000 ms；持续时间1：Lv1=10000; Lv2=13000; Lv3=16000; Lv4=19000; Lv5=22000; Lv6=25000; Lv7=28000; Lv8=31000; Lv9=34000; Lv10=37000 ms；持续时间2：10000 ms；伤害标记：NoDamage；消耗/限制：SP 10；关联状态：Endure。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Moving HP-Recovery (`SM_MOVINGRECOVERY`)

非伤害技能；目标：被动；最高等级 1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:4644
if(battle_config.pc_damage_delay_rate != 100)
// src/map/status.cpp:4645
base_status->dmotion = base_status->dmotion*battle_config.pc_damage_delay_rate/100;
// src/map/status.cpp:4660
sd->dsprate -= 4*skill;
// src/map/status.cpp:4663
sd->dsprate -= sc->getSCE(SC_SERVICE4U)->val3;
```

### Fatal Blow (`SM_FATALBLOW`)

武器/物理技能；目标：被动；最高等级 1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skills/swordman/bash.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skills/swordman/bash.cpp:14
base_skillratio += 30 * skill_lv;
// src/map/skills/swordman/bash.cpp:17
void SkillBash::modifyHitRate(int16& hit_rate, const block_list* src, const block_list* target, uint16 skill_lv) const {
// src/map/skills/swordman/bash.cpp:20
hit_rate += hit_rate * 5 * skill_lv / 100;
// src/map/skills/swordman/bash.cpp:23
void SkillBash::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/swordman/bash.cpp:24
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/swordman/bash.cpp:26
if (sd != nullptr && skill_lv > 5 && pc_checkskill(sd, SM_FATALBLOW) > 0) {
// src/map/skills/swordman/bash.cpp:28
int32 stun_chance = (skill_lv - 5) * sd->status.base_level * 10;
// src/map/skills/swordman/bash.cpp:29
status_change_start(src, target, SC_STUN, stun_chance, skill_lv, 0, 0, 0, skill_get_time2(getSkillId(), skill_lv), SCSTART_NONE);
```

### Auto Berserk (`SM_AUTOBERSERK`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；关联状态：AutoBerserk。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAutoBerserk`
- 实现文件：`src/map/skills/swordman/autoberserk.cpp`

#### `SkillAutoBerserk::SkillAutoBerserk`

来源：`src/map/skills/swordman/autoberserk.cpp:9-11`

```cpp
SkillAutoBerserk::SkillAutoBerserk() : SkillImpl(SM_AUTOBERSERK)
{
}
```

#### `SkillAutoBerserk::castendNoDamageId`

来源：`src/map/skills/swordman/autoberserk.cpp:13-25`

```cpp
void SkillAutoBerserk::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
{
	sc_type type = skill_get_sc(getSkillId());
	status_change *tsc = status_get_sc(bl);
	status_change_entry *tsce = (tsc) ? tsc->getSCE(type) : nullptr;

	int32 i;
	if (tsce)
		i = status_change_end(bl, type);
	else
		i = sc_start(src, bl, type, 100, skill_lv, 60000);
	clif_skill_nodamage(src, *bl, getSkillId(), skill_lv, i);
}
```
