# Super_Baby 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 2 | `SM_SWORD` / Sword Mastery | `core-source-references` | `` | src/map/battle.cpp |
| 4 | `SM_RECOVERY` / Increase HP Recovery | `core-source-references` | `` | src/map/pc.cpp, src/map/skills/merchant/aidberserkpotion.cpp, src/map/skills/merchant/aidcondensedpotion.cpp, src/map/skills/merchant/aidpotion.cpp, src/map/status.cpp |
| 5 | `SM_BASH` / Bash | `exact-class-methods` | `SkillBash` | src/map/skills/swordman/bash.cpp |
| 6 | `SM_PROVOKE` / Provoke | `exact-class-methods` | `SkillProvoke` | src/map/skills/swordman/provoke.cpp |
| 7 | `SM_MAGNUM` / Magnum Break | `exact-class-methods` | `SkillMagnumBreak` | src/map/skills/swordman/magnum.cpp |
| 8 | `SM_ENDURE` / Endure | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 9 | `MG_SRECOVERY` / Increase SP Recovery | `core-source-references` | `` | src/map/pc.cpp, src/map/skill.cpp, src/map/skills/acolyte/competentia.cpp, src/map/skills/merchant/aidberserkpotion.cpp, src/map/skills/merchant/aidcondensedpotion.cpp, src/map/skills/merchant/aidpotion.cpp, src/map/skills/other/netsupport.cpp, src/map/status.cpp |
| 10 | `MG_SIGHT` / Sight | `exact-class-methods` | `SkillSight` | src/map/skills/mage/sight.cpp |
| 11 | `MG_NAPALMBEAT` / Napalm Beat | `exact-class-methods` | `SkillNapalmBeat` | src/map/skills/mage/napalmbeat.cpp |
| 12 | `MG_SAFETYWALL` / Safety Wall | `exact-class-methods` | `SkillSafetyWall` | src/map/skills/mage/safetywall.cpp |
| 13 | `MG_SOULSTRIKE` / Soul Strike | `exact-class-methods` | `SkillSoulStrike` | src/map/skills/mage/soulstrike.cpp |
| 14 | `MG_COLDBOLT` / Cold Bolt | `exact-class-methods` | `SkillColdBolt` | src/map/skills/mage/coldbolt.cpp |
| 15 | `MG_FROSTDIVER` / Frost Diver | `exact-class-methods` | `SkillFrostDiver` | src/map/skills/mage/frostdiver.cpp |
| 16 | `MG_STONECURSE` / Stone Curse | `exact-class-methods` | `SkillStoneCurse` | src/map/skills/mage/stonecurse.cpp |
| 17 | `MG_FIREBALL` / Fire Ball | `exact-class-methods` | `SkillFireBall` | src/map/skills/mage/fireball.cpp |
| 18 | `MG_FIREWALL` / Fire Wall | `exact-class-methods` | `SkillFireWall` | src/map/skills/mage/firewall.cpp |
| 19 | `MG_FIREBOLT` / Fire Bolt | `exact-class-methods` | `SkillFireBolt` | src/map/skills/mage/firebolt.cpp |
| 20 | `MG_LIGHTNINGBOLT` / Lightning Bolt | `exact-class-methods` | `SkillLightningBolt` | src/map/skills/mage/lightningbolt.cpp |
| 21 | `MG_THUNDERSTORM` / Thunderstorm | `exact-class-methods` | `SkillThunderStorm` | src/map/skills/mage/thunderstorm.cpp |
| 22 | `AL_DP` / Divine Protection | `core-source-references` | `` | src/map/battle.cpp |
| 23 | `AL_DEMONBANE` / Demon Bane | `core-source-references` | `` | src/map/battle.cpp |
| 24 | `AL_RUWACH` / Ruwach | `exact-class-methods` | `SkillRuwach` | src/map/skills/acolyte/ruwach.cpp |
| 25 | `AL_PNEUMA` / Pneuma | `exact-class-methods` | `SkillPneuma` | src/map/skills/acolyte/pneuma.cpp |
| 26 | `AL_TELEPORT` / Teleport | `exact-class-methods` | `SkillTeleport` | src/map/skills/acolyte/teleport.cpp |
| 27 | `AL_WARP` / Warp Portal | `exact-class-methods` | `SkillWarpPortal` | src/map/skills/acolyte/warpportal.cpp |
| 28 | `AL_HEAL` / Heal | `exact-class-methods` | `SkillHeal` | src/map/skills/acolyte/heal.cpp |
| 29 | `AL_INCAGI` / Increase AGI | `exact-class-methods` | `SkillIncreaseAgi` | src/map/skills/acolyte/incagi.cpp |
| 30 | `AL_DECAGI` / Decrease AGI | `exact-class-methods` | `SkillDecreaseAgi` | src/map/skills/acolyte/decagi.cpp |
| 31 | `AL_HOLYWATER` / Aqua Benedicta | `exact-class-methods` | `SkillHolyWater` | src/map/skills/acolyte/holywater.cpp |
| 32 | `AL_CRUCIS` / Signum Crucis | `exact-class-methods` | `SkillCrucis` | src/map/skills/acolyte/crucis.cpp |
| 33 | `AL_ANGELUS` / Angelus | `exact-class-methods` | `SkillAngelus` | src/map/skills/acolyte/angelus.cpp |
| 34 | `AL_BLESSING` / Blessing | `exact-class-methods` | `SkillBlessing` | src/map/skills/acolyte/blessing.cpp |
| 35 | `AL_CURE` / Cure | `exact-class-methods` | `SkillCure` | src/map/skills/acolyte/cure.cpp |
| 36 | `MC_INCCARRY` / Enlarge Weight Limit | `core-source-references` | `` | src/map/status.cpp |
| 37 | `MC_DISCOUNT` / Discount | `core-source-references` | `` | src/map/pc.cpp |
| 38 | `MC_OVERCHARGE` / Overcharge | `core-source-references` | `` | src/map/pc.cpp |
| 39 | `MC_PUSHCART` / Pushcart | `core-source-references` | `` | src/map/pc.cpp, src/map/status.cpp |
| 40 | `MC_IDENTIFY` / Item Appraisal | `exact-class-methods` | `SkillItemAppraisal` | src/map/skills/merchant/itemappraisal.cpp |
| 41 | `MC_VENDING` / Vending | `exact-class-methods` | `SkillVending` | src/map/skills/merchant/skill_vending.cpp |
| 42 | `MC_MAMMONITE` / Mammonite | `exact-class-methods` | `SkillMammonite` | src/map/skills/merchant/mammonite.cpp |
| 43 | `AC_OWL` / Owl's Eye | `core-source-references` | `` | src/map/skill.cpp, src/map/status.cpp |
| 44 | `AC_VULTURE` / Vulture's Eye | `core-source-references` | `` | src/map/battle.cpp, src/map/skill.cpp, src/map/status.cpp |
| 45 | `AC_CONCENTRATION` / Improve Concentration | `exact-class-methods` | `SkillConcentration` | src/map/skills/archer/concentration.cpp |
| 48 | `TF_DOUBLE` / Double Attack | `exact-class-methods` | `SkillDoubleAttack` | src/map/skills/thief/doubleattack.cpp |
| 49 | `TF_MISS` / Improve Dodge | `core-source-references` | `` | src/map/status.cpp |
| 50 | `TF_STEAL` / Steal | `exact-class-methods` | `SkillSteal` | src/map/skills/thief/steal.cpp |
| 51 | `TF_HIDING` / Hiding | `exact-class-methods` | `SkillHiding` | src/map/skills/thief/hiding.cpp |
| 52 | `TF_POISON` / Envenom | `exact-class-methods` | `SkillEnvenom` | src/map/skills/thief/envenom.cpp |
| 53 | `TF_DETOXIFY` / Detoxify | `exact-class-methods` | `SkillDetoxify` | src/map/skills/thief/detoxify.cpp |
| 2535 | `ALL_BUYING_STORE` / Open Buying Store | `exact-class-methods` | `SkillOpenBuyingStore` | src/map/skills/other/openbuyingstore.cpp |
| 2544 | `MC_CARTDECORATE` / Decorate Cart | `exact-class-methods` | `SkillDecorateCart` | src/map/skills/merchant/decoratecart.cpp |

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

### Increase SP Recovery (`MG_SRECOVERY`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/acolyte/competentia.cpp`, `src/map/skills/merchant/aidberserkpotion.cpp`, `src/map/skills/merchant/aidcondensedpotion.cpp`, `src/map/skills/merchant/aidpotion.cpp`, `src/map/skills/other/netsupport.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/pc.cpp:10719
if (sd->sc.getSCE(SC_INCHEALRATE))
// src/map/pc.cpp:10720
bonus += bonus * sd->sc.getSCE(SC_INCHEALRATE)->val1 / 100;
// src/map/pc.cpp:10722
tmp = hp * bonus / 100; // Overflow check
// src/map/pc.cpp:10723
if (bonus != 100 && tmp > hp)
// src/map/pc.cpp:10724
hp = tmp;
// src/map/pc.cpp:10726
if (sp) {
// src/map/pc.cpp:10733
bonus += sd->bonus.itemsphealrate2;
// src/map/pc.cpp:10735
bonus += bonus * pc_get_itemgroup_bonus( sd, itemid, sd->itemgroupsphealrate ) / 100;
// src/map/pc.cpp:10737
for( const auto &it : sd->itemsphealrate ){
// src/map/skill.cpp:7337
int32 hp, sp;
// src/map/skill.cpp:7339
switch( sg->skill_lv ) {
// src/map/skill.cpp:7340
case 1: case 2: hp = 3; sp = 2; break;
// src/map/skill.cpp:7341
case 3: case 4: hp = 4; sp = 3; break;
// src/map/skill.cpp:7342
case 5: default: hp = 5; sp = 4; break;
// src/map/skill.cpp:7344
hp = tstatus->max_hp * hp / 100;
// src/map/skill.cpp:7345
sp = tstatus->max_sp * sp / 100;
```

### Sight (`MG_SIGHT`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；段数：1；属性：Fire；范围：3；持续时间1：10000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 10；关联状态：Sight。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSight`
- 实现文件：`src/map/skills/mage/sight.cpp`

#### `SkillSight::SkillSight`

来源：`src/map/skills/mage/sight.cpp:9-10`

```cpp
SkillSight::SkillSight() : SkillImpl(MG_SIGHT) {
}
```

#### `SkillSight::castendNoDamageId`

来源：`src/map/skills/mage/sight.cpp:12-17`

```cpp
void SkillSight::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	sc_type type = skill_get_sc(getSkillId());

	clif_skill_nodamage(src, *target, getSkillId(), skill_lv,
	                    sc_start2(src, target, type, 100, skill_lv, getSkillId(), skill_get_time(getSkillId(), skill_lv)));
}
```

### Napalm Beat (`MG_NAPALMBEAT`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Ghost；范围：1；吟唱：1000 ms；技能后摇：Lv1-3=1000; Lv4-5=900; Lv6-7=800; Lv8=700; Lv9=600; Lv10=500 ms；伤害标记：Splash, SplashSplit；消耗/限制：SP Lv1-3=9; Lv4-6=12; Lv7-9=15; Lv10=18。

- 覆盖：`exact-class-methods`
- 实现类：`SkillNapalmBeat`
- 实现文件：`src/map/skills/mage/napalmbeat.cpp`

#### `SkillNapalmBeat::SkillNapalmBeat`

来源：`src/map/skills/mage/napalmbeat.cpp:6-7`

```cpp
SkillNapalmBeat::SkillNapalmBeat() : SkillImplRecursiveDamageSplash(MG_NAPALMBEAT) {
}
```

#### `SkillNapalmBeat::calculateSkillRatio`

来源：`src/map/skills/mage/napalmbeat.cpp:9-11`

```cpp
void SkillNapalmBeat::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += -30 + 10 * skill_lv;
}
```

#### `SkillNapalmBeat::castendDamageId`

来源：`src/map/skills/mage/napalmbeat.cpp:13-15`

```cpp
void SkillNapalmBeat::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	SkillImplRecursiveDamageSplash::castendDamageId(src, target, skill_lv, tick, flag);
}
```

### Safety Wall (`MG_SAFETYWALL`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：1；属性：Ghost；吟唱：Lv1=4000; Lv2-3=3500; Lv4=2500; Lv5=2000; Lv6=1500; Lv7-10=1000 ms；持续时间1：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000; Lv6=30000; Lv7=35000; Lv8=40000; Lv9=45000; Lv10=50000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-3=30; Lv4-6=35; Lv7-10=40；道具 Blue_Gemstone×1；关联状态：Safetywall。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSafetyWall`
- 实现文件：`src/map/skills/mage/safetywall.cpp`

#### `SkillSafetyWall::SkillSafetyWall`

来源：`src/map/skills/mage/safetywall.cpp:6-7`

```cpp
SkillSafetyWall::SkillSafetyWall() : SkillImpl(MG_SAFETYWALL) {
}
```

#### `SkillSafetyWall::castendPos2`

来源：`src/map/skills/mage/safetywall.cpp:9-23`

```cpp
void SkillSafetyWall::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	int32 dummy = 1;

	if (map_foreachincell(skill_cell_overlap, src->m, x, y, BL_SKILL, getSkillId(), &dummy, src)) {
		skill_unitsetting(src, getSkillId(), skill_lv, x, y, 0);
		// Don't consume gems if cast on Land Protector
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}

	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Soul Strike (`MG_SOULSTRIKE`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1-2=1; Lv3-4=2; Lv5-6=3; Lv7-8=4; Lv9-10=5；属性：Ghost；吟唱：500 ms；技能后摇：Lv1=1200; Lv2=1000; Lv3=1400; Lv4=1200; Lv5=1600; Lv6=1400; Lv7=1800; Lv8=1600; Lv9=2000; Lv10=1800 ms；消耗/限制：SP Lv1=18; Lv2=14; Lv3=24; Lv4=20; Lv5=30; Lv6=26; Lv7=36; Lv8=32; Lv9=42; Lv10=38。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSoulStrike`
- 实现文件：`src/map/skills/mage/soulstrike.cpp`

#### `SkillSoulStrike::SkillSoulStrike`

来源：`src/map/skills/mage/soulstrike.cpp:8-9`

```cpp
SkillSoulStrike::SkillSoulStrike() : SkillImpl(MG_SOULSTRIKE) {
}
```

#### `SkillSoulStrike::calculateSkillRatio`

来源：`src/map/skills/mage/soulstrike.cpp:11-16`

```cpp
void SkillSoulStrike::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_data *tstatus = status_get_status_data(*target);

	if (battle_check_undead(tstatus->race, tstatus->def_ele))
		base_skillratio += 5 * skill_lv;
}
```

#### `SkillSoulStrike::castendDamageId`

来源：`src/map/skills/mage/soulstrike.cpp:18-20`

```cpp
void SkillSoulStrike::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

### Cold Bolt (`MG_COLDBOLT`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Water；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800; Lv6=2000; Lv7=2200; Lv8=2400; Lv9=2600; Lv10=2800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30。

- 覆盖：`exact-class-methods`
- 实现类：`SkillColdBolt`
- 实现文件：`src/map/skills/mage/coldbolt.cpp`

#### `SkillColdBolt::SkillColdBolt`

来源：`src/map/skills/mage/coldbolt.cpp:9-10`

```cpp
SkillColdBolt::SkillColdBolt() : SkillImpl(MG_COLDBOLT) {
}
```

#### `SkillColdBolt::calculateSkillRatio`

来源：`src/map/skills/mage/coldbolt.cpp:12-24`

```cpp
void SkillColdBolt::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_change *sc = status_get_sc(src);

	if (sc) {
		if (sc->getSCE(SC_COLD_FORCE_OPTION))
			base_skillratio *= 5;

		if (sc->getSCE(SC_SPELLFIST) && mflag & BF_SHORT) {
			base_skillratio += (sc->getSCE(SC_SPELLFIST)->val3 * 100) + (sc->getSCE(SC_SPELLFIST)->val1 * 50 - 50) - 100;
			// val3 = used bolt level, val1 = used spellfist level. [Rytech]
		}
	}
}
```

#### `SkillColdBolt::castendDamageId`

来源：`src/map/skills/mage/coldbolt.cpp:26-28`

```cpp
void SkillColdBolt::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

#### `SkillColdBolt::modifyDamageData`

来源：`src/map/skills/mage/coldbolt.cpp:30-40`

```cpp
void SkillColdBolt::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const status_change* sc = status_get_sc(&src);

	if (sc != nullptr) {
		if (sc->hasSCE(SC_SPELLFIST) && (dmg.miscflag & BF_SHORT)) {
			dmg.div_ = 1; // ad mods, to make it work similar to regular hits [Xazax]
			dmg.flag = BF_WEAPON | BF_SHORT;
			dmg.type = DMG_NORMAL;
		}
	}
}
```

### Frost Diver (`MG_FROSTDIVER`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Water；吟唱：800 ms；技能后摇：1500 ms；持续时间2：Lv1=3000; Lv2=6000; Lv3=9000; Lv4=12000; Lv5=15000; Lv6=18000; Lv7=21000; Lv8=24000; Lv9=27000; Lv10-11=30000 ms；消耗/限制：SP Lv1=25; Lv2=24; Lv3=23; Lv4=22; Lv5=21; Lv6=20; Lv7=19; Lv8=18; Lv9=17; Lv10=16；关联状态：Freeze。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFrostDiver`
- 实现文件：`src/map/skills/mage/frostdiver.cpp`

#### `SkillFrostDiver::SkillFrostDiver`

来源：`src/map/skills/mage/frostdiver.cpp:10-11`

```cpp
SkillFrostDiver::SkillFrostDiver() : SkillImpl(MG_FROSTDIVER) {
}
```

#### `SkillFrostDiver::calculateSkillRatio`

来源：`src/map/skills/mage/frostdiver.cpp:13-15`

```cpp
void SkillFrostDiver::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 10 * skill_lv;
}
```

#### `SkillFrostDiver::castendDamageId`

来源：`src/map/skills/mage/frostdiver.cpp:17-19`

```cpp
void SkillFrostDiver::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

#### `SkillFrostDiver::applyAdditionalEffects`

来源：`src/map/skills/mage/frostdiver.cpp:21-25`

```cpp
void SkillFrostDiver::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	if (!sc_start(src, target, SC_FREEZE, min(skill_lv * 3 + 35, skill_lv + 60), skill_lv, skill_get_time2(getSkillId(), skill_lv)) && sd)
		clif_skill_fail(*sd, getSkillId());
}
```

### Stone Curse (`MG_STONECURSE`)

魔法技能；目标：敌方目标；最高等级 10；射程：2；命中类型：Single；段数：1；属性：Earth；吟唱：1000 ms；持续时间1：5000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=25; Lv2=24; Lv3=23; Lv4=22; Lv5=21; Lv6=20; Lv7=19; Lv8=18; Lv9=17; Lv10=16；道具 Red_Gemstone×1；关联状态：StoneWait。

- 覆盖：`exact-class-methods`
- 实现类：`SkillStoneCurse`
- 实现文件：`src/map/skills/mage/stonecurse.cpp`

#### `SkillStoneCurse::SkillStoneCurse`

来源：`src/map/skills/mage/stonecurse.cpp:10-11`

```cpp
SkillStoneCurse::SkillStoneCurse() : SkillImpl(MG_STONECURSE) {
}
```

#### `SkillStoneCurse::castendNoDamageId`

来源：`src/map/skills/mage/stonecurse.cpp:13-45`

```cpp
void SkillStoneCurse::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	map_session_data *sd = BL_CAST(BL_PC, src);
	status_data *tstatus = status_get_status_data(*target);
	status_change *tsc = status_get_sc(&*target);
	sc_type type = skill_get_sc(getSkillId());

	if (status_has_mode(tstatus, MD_STATUSIMMUNE)) {
		if (sd)
			clif_skill_fail(*sd, getSkillId());
		return;
	}

	if (status_isimmune(target) || !tsc)
		return;

	int32 brate = 0;

	if (sd && sd->sc.getSCE(SC_PETROLOGY_OPTION))
		brate = sd->sc.getSCE(SC_PETROLOGY_OPTION)->val3;

	// Except for players, the skill animation shows even if the status change doesn't start
	// Players get a skill has failed message instead
	if (sc_start2(src, target, type, (skill_lv * 4 + 20) + brate, skill_lv, src->id, skill_get_time2(getSkillId(), skill_lv), skill_get_time(getSkillId(), skill_lv)) || sd == nullptr)
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
	else {
		clif_skill_fail( *sd, getSkillId() );
		// Level 6-10 doesn't consume a red gem if it fails [celest]
		if (skill_lv > 5)
		{ // not to consume items
			flag |= SKILL_NOCONSUME_REQ;
		}
	}
}
```

### Fire Ball (`MG_FIREBALL`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Fire；范围：Lv1-10=2; Lv11=3；吟唱：Lv1-5=1500; Lv6-10=1000 ms；技能后摇：Lv1-5=1500; Lv6-10=1000 ms；伤害标记：Splash；消耗/限制：SP 25。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFireBall`
- 实现文件：`src/map/skills/mage/fireball.cpp`

#### `SkillFireBall::SkillFireBall`

来源：`src/map/skills/mage/fireball.cpp:8-9`

```cpp
SkillFireBall::SkillFireBall() : SkillImplRecursiveDamageSplash(MG_FIREBALL) {
}
```

#### `SkillFireBall::calculateSkillRatio`

来源：`src/map/skills/mage/fireball.cpp:11-19`

```cpp
void SkillFireBall::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 40 + 20 * skill_lv;
#else
	base_skillratio += -30 + 10 * skill_lv;
#endif
	if (wd->miscflag == 2) //Enemies at the edge of the area will take 75% of the damage
		base_skillratio = base_skillratio * 3 / 4;
}
```

#### `SkillFireBall::castendDamageId`

来源：`src/map/skills/mage/fireball.cpp:21-23`

```cpp
void SkillFireBall::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	SkillImplRecursiveDamageSplash::castendDamageId(src, target, skill_lv, tick, flag);
}
```

#### `SkillFireBall::splashDamage`

来源：`src/map/skills/mage/fireball.cpp:25-34`

```cpp
int64 SkillFireBall::splashDamage(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 flag) const {
	// For players, the distance between original target and splash target determines the damage
	if( map_session_data* sd = BL_CAST( BL_PC, src ); sd != nullptr ){
		if (block_list* orig_bl = map_id2bl(skill_area_temp[1]); orig_bl != nullptr)
			flag |= distance_bl(orig_bl, target);
	}

	// Call default implementation
	return SkillImplRecursiveDamageSplash::splashDamage(src, target, skill_lv, tick, flag);
}
```

### Fire Wall (`MG_FIREWALL`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Fire；击退：2；吟唱：Lv1=2000; Lv2=1850; Lv3=1700; Lv4=1550; Lv5=1400; Lv6=1250; Lv7=1100; Lv8=950; Lv9=800; Lv10=650 ms；持续时间1：Lv1=5000; Lv2=6000; Lv3=7000; Lv4=8000; Lv5=9000; Lv6=10000; Lv7=11000; Lv8=12000; Lv9=13000; Lv10=14000 ms；消耗/限制：SP 40。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFireWall`
- 实现文件：`src/map/skills/mage/firewall.cpp`

#### `SkillFireWall::SkillFireWall`

来源：`src/map/skills/mage/firewall.cpp:8-9`

```cpp
SkillFireWall::SkillFireWall() : SkillImpl(MG_FIREWALL) {
}
```

#### `SkillFireWall::castendPos2`

来源：`src/map/skills/mage/firewall.cpp:11-16`

```cpp
void SkillFireWall::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillFireWall::calculateSkillRatio`

来源：`src/map/skills/mage/firewall.cpp:18-20`

```cpp
void SkillFireWall::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio -= 50;
}
```

#### `SkillFireWall::modifyDamageData`

来源：`src/map/skills/mage/firewall.cpp:22-28`

```cpp
void SkillFireWall::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const status_data* tstatus = status_get_status_data(target);

	if (tstatus->def_ele == ELE_FIRE || battle_check_undead(tstatus->race, tstatus->def_ele)) {
		dmg.blewcount = 0; // No knockback
	}
}
```

### Fire Bolt (`MG_FIREBOLT`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Fire；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800; Lv6=2000; Lv7=2200; Lv8=2400; Lv9=2600; Lv10=2800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFireBolt`
- 实现文件：`src/map/skills/mage/firebolt.cpp`

#### `SkillFireBolt::SkillFireBolt`

来源：`src/map/skills/mage/firebolt.cpp:9-10`

```cpp
SkillFireBolt::SkillFireBolt() : SkillImpl(MG_FIREBOLT) {
}
```

#### `SkillFireBolt::calculateSkillRatio`

来源：`src/map/skills/mage/firebolt.cpp:12-24`

```cpp
void SkillFireBolt::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_change *sc = status_get_sc(src);

	if (sc) {
		if (sc->getSCE(SC_FLAMETECHNIC_OPTION))
			base_skillratio *= 5;

		if (sc->getSCE(SC_SPELLFIST) && mflag & BF_SHORT) {
			base_skillratio += (sc->getSCE(SC_SPELLFIST)->val3 * 100) + (sc->getSCE(SC_SPELLFIST)->val1 * 50 - 50) - 100;
			// val3 = used bolt level, val1 = used spellfist level. [Rytech]
		}
	}
}
```

#### `SkillFireBolt::castendDamageId`

来源：`src/map/skills/mage/firebolt.cpp:26-28`

```cpp
void SkillFireBolt::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

#### `SkillFireBolt::modifyDamageData`

来源：`src/map/skills/mage/firebolt.cpp:30-40`

```cpp
void SkillFireBolt::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const status_change* sc = status_get_sc(&src);

	if (sc != nullptr) {
		if (sc->hasSCE(SC_SPELLFIST) && (dmg.miscflag & BF_SHORT)) {
			dmg.div_ = 1; // ad mods, to make it work similar to regular hits [Xazax]
			dmg.flag = BF_WEAPON | BF_SHORT;
			dmg.type = DMG_NORMAL;
		}
	}
}
```

### Lightning Bolt (`MG_LIGHTNINGBOLT`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Wind；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800; Lv6=2000; Lv7=2200; Lv8=2400; Lv9=2600; Lv10=2800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30。

- 覆盖：`exact-class-methods`
- 实现类：`SkillLightningBolt`
- 实现文件：`src/map/skills/mage/lightningbolt.cpp`

#### `SkillLightningBolt::SkillLightningBolt`

来源：`src/map/skills/mage/lightningbolt.cpp:9-10`

```cpp
SkillLightningBolt::SkillLightningBolt() : SkillImpl(MG_LIGHTNINGBOLT) {
}
```

#### `SkillLightningBolt::calculateSkillRatio`

来源：`src/map/skills/mage/lightningbolt.cpp:12-24`

```cpp
void SkillLightningBolt::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_change *sc = status_get_sc(src);

	if (sc) {
		if (sc->getSCE(SC_GRACE_BREEZE_OPTION))
			base_skillratio *= 5;

		if (sc->getSCE(SC_SPELLFIST) && mflag & BF_SHORT) {
			base_skillratio += (sc->getSCE(SC_SPELLFIST)->val3 * 100) + (sc->getSCE(SC_SPELLFIST)->val1 * 50 - 50) - 100;
			// val3 = used bolt level, val1 = used spellfist level. [Rytech]
		}
	}
}
```

#### `SkillLightningBolt::castendDamageId`

来源：`src/map/skills/mage/lightningbolt.cpp:26-28`

```cpp
void SkillLightningBolt::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

#### `SkillLightningBolt::modifyDamageData`

来源：`src/map/skills/mage/lightningbolt.cpp:30-40`

```cpp
void SkillLightningBolt::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const status_change* sc = status_get_sc(&src);

	if (sc != nullptr) {
		if (sc->hasSCE(SC_SPELLFIST) && (dmg.miscflag & BF_SHORT)) {
			dmg.div_ = 1; // ad mods, to make it work similar to regular hits [Xazax]
			dmg.flag = BF_WEAPON | BF_SHORT;
			dmg.type = DMG_NORMAL;
		}
	}
}
```

### Thunderstorm (`MG_THUNDERSTORM`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Wind；吟唱：Lv1=1000; Lv2=2000; Lv3=3000; Lv4=4000; Lv5=5000; Lv6=6000; Lv7=7000; Lv8=8000; Lv9=9000; Lv10=10000 ms；技能后摇：2000 ms；持续时间1：100 ms；消耗/限制：SP Lv1=29; Lv2=34; Lv3=39; Lv4=44; Lv5=49; Lv6=54; Lv7=59; Lv8=64; Lv9=69; Lv10=74。

- 覆盖：`exact-class-methods`
- 实现类：`SkillThunderStorm`
- 实现文件：`src/map/skills/mage/thunderstorm.cpp`

#### `SkillThunderStorm::SkillThunderStorm`

来源：`src/map/skills/mage/thunderstorm.cpp:6-7`

```cpp
SkillThunderStorm::SkillThunderStorm() : SkillImpl(MG_THUNDERSTORM) {
}
```

#### `SkillThunderStorm::castendPos2`

来源：`src/map/skills/mage/thunderstorm.cpp:9-14`

```cpp
void SkillThunderStorm::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillThunderStorm::calculateSkillRatio`

来源：`src/map/skills/mage/thunderstorm.cpp:16-21`

```cpp
void SkillThunderStorm::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	// in Renewal Thunder Storm boost is 100% (in pre-re, 80%)
#ifndef RENEWAL
	base_skillratio -= 20;
#endif
}
```

### Divine Protection (`AL_DP`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Demon Bane (`AL_DEMONBANE`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2279
int64 damage;
// src/map/battle.cpp:2284
damage = 0;
// src/map/battle.cpp:2286
damage = dmg;
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
```

### Ruwach (`AL_RUWACH`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；段数：1；属性：Holy；范围：2；持续时间1：10000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 10；关联状态：Ruwach。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRuwach`
- 实现文件：`src/map/skills/acolyte/ruwach.cpp`

#### `SkillRuwach::SkillRuwach`

来源：`src/map/skills/acolyte/ruwach.cpp:9-11`

```cpp
SkillRuwach::SkillRuwach() : SkillImpl(AL_RUWACH)
{
}
```

#### `SkillRuwach::castendNoDamageId`

来源：`src/map/skills/acolyte/ruwach.cpp:13-18`

```cpp
void SkillRuwach::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
{
	sc_type type = skill_get_sc(getSkillId());

	clif_skill_nodamage(src, *bl, getSkillId(), skill_lv, sc_start2(src, bl, type, 100, skill_lv, getSkillId(), skill_get_time(getSkillId(), skill_lv)));
}
```

#### `SkillRuwach::calculateSkillRatio`

来源：`src/map/skills/acolyte/ruwach.cpp:20-22`

```cpp
void SkillRuwach::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += 45;
}
```

### Pneuma (`AL_PNEUMA`)

魔法技能；目标：地面区域；最高等级 1；射程：9；命中类型：Single；段数：1；持续时间1：10000 ms；伤害标记：NoDamage；消耗/限制：SP 10；关联状态：Pneuma。

- 覆盖：`exact-class-methods`
- 实现类：`SkillPneuma`
- 实现文件：`src/map/skills/acolyte/pneuma.cpp`

#### `SkillPneuma::SkillPneuma`

来源：`src/map/skills/acolyte/pneuma.cpp:6-7`

```cpp
SkillPneuma::SkillPneuma() : SkillImpl(AL_PNEUMA) {
}
```

#### `SkillPneuma::castendPos2`

来源：`src/map/skills/acolyte/pneuma.cpp:9-14`

```cpp
void SkillPneuma::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Teleport (`AL_TELEPORT`)

魔法技能；目标：自身；最高等级 2；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP Lv1=10; Lv2=9。

- 覆盖：`exact-class-methods`
- 实现类：`SkillTeleport`
- 实现文件：`src/map/skills/acolyte/teleport.cpp`

#### `SkillTeleport::SkillTeleport`

来源：`src/map/skills/acolyte/teleport.cpp:12-13`

```cpp
SkillTeleport::SkillTeleport() : SkillImpl(AL_TELEPORT) {
}
```

#### `SkillTeleport::castendNoDamageId`

来源：`src/map/skills/acolyte/teleport.cpp:15-54`

```cpp
void SkillTeleport::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if(sd != nullptr)
	{
		if (map_getmapflag(target->m, MF_NOTELEPORT) && skill_lv <= 2) {
			clif_skill_teleportmessage( *sd, NOTIFY_MAPINFO_CANT_TP );
			return;
		}
		if(!battle_config.duel_allow_teleport && sd->duel_group && skill_lv <= 2) { // duel restriction [LuzZza]
			char output[128]; sprintf(output, msg_txt(sd,365), skill_get_name(getSkillId()));
			clif_displaymessage(sd->fd, output); //"Duel: Can't use %s in duel."
			return;
		}

		if( sd->state.autocast || ( (sd->skillitem == getSkillId() || battle_config.skip_teleport_lv1_menu) && skill_lv == 1 ) || skill_lv == 3 )
		{
			if( skill_lv == 1 )
				pc_randomwarp(sd,CLR_TELEPORT);
			else
				pc_setpos( sd, mapindex_name2id( sd->status.save_point.map ), sd->status.save_point.x, sd->status.save_point.y, CLR_TELEPORT );
			return;
		}

		clif_skill_nodamage(src,*target,getSkillId(),skill_lv);

		std::vector<std::string> maps = {
			"Random"
		};

		if( skill_lv == 1 ){
			clif_skill_warppoint( *sd, getSkillId(), skill_lv, maps );
		}else{
			maps.push_back( sd->status.save_point.map );

			clif_skill_warppoint( *sd, getSkillId(), skill_lv, maps );
		}
	} else
		unit_warp(target,-1,-1,-1,CLR_TELEPORT);
}
```

### Warp Portal (`AL_WARP`)

魔法技能；目标：地面区域；最高等级 4；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；持续时间1：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000; Lv6=30000; Lv7=35000; Lv8=40000; Lv9=45000; Lv10=50000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=35; Lv2=32; Lv3=29; Lv4=26；道具 Blue_Gemstone×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillWarpPortal`
- 实现文件：`src/map/skills/acolyte/warpportal.cpp`

#### `SkillWarpPortal::SkillWarpPortal`

来源：`src/map/skills/acolyte/warpportal.cpp:10-11`

```cpp
SkillWarpPortal::SkillWarpPortal() : SkillImpl(AL_WARP) {
}
```

#### `SkillWarpPortal::castendPos2`

来源：`src/map/skills/acolyte/warpportal.cpp:13-40`

```cpp
void SkillWarpPortal::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	status_change* sc = status_get_sc(src);

	if(sd != nullptr) {
		std::vector<std::string> maps( MAX_MEMOPOINTS + 1 );

		maps.push_back( sd->status.save_point.map );

		if( skill_lv >= 2 ){
			maps.push_back( sd->status.memo_point[0].map );

			if( skill_lv >= 3 ){
				maps.push_back( sd->status.memo_point[1].map );

				if( skill_lv >= 4 ){
					maps.push_back( sd->status.memo_point[2].map );
				}
			}
		}

		clif_skill_warppoint( *sd, getSkillId(), skill_lv, maps );
	}
	if( sc && sc->getSCE(SC_CURSEDCIRCLE_ATKER) ) //Should only remove after the skill has been casted.
		status_change_end(src,SC_CURSEDCIRCLE_ATKER);
	// not to consume item.
	flag |= SKILL_NOCONSUME_REQ;
}
```

### Heal (`AL_HEAL`)

魔法技能；目标：友方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Holy；技能后摇：1000 ms；伤害标记：NoDamage, IgnoreDefense；消耗/限制：SP Lv1=13; Lv2=16; Lv3=19; Lv4=22; Lv5=25; Lv6=28; Lv7=31; Lv8=34; Lv9=37; Lv10=40。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHeal`
- 实现文件：`src/map/skills/acolyte/heal.cpp`

#### `SkillHeal::SkillHeal`

来源：`src/map/skills/acolyte/heal.cpp:9-11`

```cpp
SkillHeal::SkillHeal() : SkillImpl(AL_HEAL)
{
}
```

#### `SkillHeal::castendNoDamageId`

来源：`src/map/skills/acolyte/heal.cpp:13-59`

```cpp
void SkillHeal::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
{
	status_change *tsc = status_get_sc(bl);
	map_session_data *sd = BL_CAST(BL_PC, src);
	map_session_data *dstsd = nullptr;
	status_data* sstatus = status_get_status_data(*src);
	mob_data *dstmd = BL_CAST(BL_MOB, bl);

	int32 heal = skill_calc_heal(src, bl, getSkillId(), skill_lv, true);

	if (status_isimmune(bl) || (dstmd && (status_get_class(bl) == MOBID_EMPERIUM || status_get_class_(bl) == CLASS_BATTLEFIELD)))
		heal = 0;

	if (tsc != nullptr && !tsc->empty())
	{
		if (tsc->getSCE(SC_KAITE) && !status_has_mode(sstatus, MD_STATUSIMMUNE))
		{ // Bounce back heal
			if (--tsc->getSCE(SC_KAITE)->val2 <= 0)
				status_change_end(bl, SC_KAITE);
			if (src == bl)
				heal = 0; // When you try to heal yourself under Kaite, the heal is voided.
			else
			{
				bl = src;
				dstsd = sd;
			}
		}
		else if (tsc->getSCE(SC_BERSERK) || tsc->getSCE(SC_SATURDAYNIGHTFEVER))
		{
			heal = 0; // Needed so that it actually displays 0 when healing.
		}
	}

	status_change_end(bl, SC_BITESCAR);
	clif_skill_nodamage(src, *bl, getSkillId(), heal);
	if (tsc && tsc->getSCE(SC_AKAITSUKI) && heal)
		heal = ~heal + 1;
	t_exp heal_get_jobexp = status_heal(bl, heal, 0, 0);

	if (sd && dstsd && heal > 0 && sd != dstsd && battle_config.heal_exp > 0)
	{
		heal_get_jobexp = heal_get_jobexp * battle_config.heal_exp / 100;
		if (heal_get_jobexp <= 0)
			heal_get_jobexp = 1;
		pc_gainexp(sd, bl, 0, heal_get_jobexp, 0);
	}
}
```

#### `SkillHeal::castendDamageId`

来源：`src/map/skills/acolyte/heal.cpp:61-64`

```cpp
void SkillHeal::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const
{
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

### Increase AGI (`AL_INCAGI`)

魔法技能；目标：友方目标；最高等级 10；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：Lv1=60000; Lv2=80000; Lv3=100000; Lv4=120000; Lv5=140000; Lv6=160000; Lv7=180000; Lv8=200000; Lv9=220000; Lv10=240000 ms；伤害标记：NoDamage；消耗/限制：HP 15；SP Lv1=18; Lv2=21; Lv3=24; Lv4=27; Lv5=30; Lv6=33; Lv7=36; Lv8=39; Lv9=42; Lv10=45；关联状态：IncreaseAgi。

- 覆盖：`exact-class-methods`
- 实现类：`SkillIncreaseAgi`
- 实现文件：`src/map/skills/acolyte/incagi.cpp`

#### `SkillIncreaseAgi::SkillIncreaseAgi`

来源：`src/map/skills/acolyte/incagi.cpp:8-10`

```cpp
SkillIncreaseAgi::SkillIncreaseAgi() : SkillImpl(AL_INCAGI)
{
}
```

#### `SkillIncreaseAgi::castendNoDamageId`

来源：`src/map/skills/acolyte/incagi.cpp:12-29`

```cpp
void SkillIncreaseAgi::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
{
	map_session_data *dstsd = BL_CAST(BL_PC, bl);
	status_change *tsc = status_get_sc(bl);
	enum sc_type type = skill_get_sc(getSkillId());

	clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);
	if (dstsd != nullptr && tsc && tsc->getSCE(SC_CHANGEUNDEAD))
	{
		status_data *tstatus = status_get_status_data(*bl);
		if (tstatus->hp > 1)
		{
			skill_attack(BF_MISC, src, src, bl, getSkillId(), skill_lv, tick, flag);
		}
		return;
	}
	sc_start(src, bl, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
}
```

### Decrease AGI (`AL_DECAGI`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：1000 ms；持续时间1：Lv1=40000; Lv2=50000; Lv3=60000; Lv4=70000; Lv5=80000; Lv6=90000; Lv7=100000; Lv8=110000; Lv9=120000; Lv10-11=130000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=15; Lv2=17; Lv3=19; Lv4=21; Lv5=23; Lv6=25; Lv7=27; Lv8=29; Lv9=31; Lv10=33；关联状态：DecreaseAgi。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDecreaseAgi`
- 实现文件：`src/map/skills/acolyte/decagi.cpp`

#### `SkillDecreaseAgi::SkillDecreaseAgi`

来源：`src/map/skills/acolyte/decagi.cpp:9-11`

```cpp
SkillDecreaseAgi::SkillDecreaseAgi() : SkillImpl(AL_DECAGI)
{
}
```

#### `SkillDecreaseAgi::castendNoDamageId`

来源：`src/map/skills/acolyte/decagi.cpp:13-19`

```cpp
void SkillDecreaseAgi::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
{
	sc_type type = skill_get_sc(getSkillId());
	status_data *sstatus = status_get_status_data(*src);

	clif_skill_nodamage(src, *bl, getSkillId(), skill_lv, sc_start(src, bl, type, (50 + skill_lv * 3 + (status_get_lv(src) + sstatus->int_) / 5), skill_lv, skill_get_time(getSkillId(), skill_lv)));
}
```

### Aqua Benedicta (`AL_HOLYWATER`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；伤害标记：NoDamage；消耗/限制：SP 10；状态 Water。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHolyWater`
- 实现文件：`src/map/skills/acolyte/holywater.cpp`

#### `SkillHolyWater::SkillHolyWater`

来源：`src/map/skills/acolyte/holywater.cpp:8-10`

```cpp
SkillHolyWater::SkillHolyWater() : SkillImpl(AL_HOLYWATER)
{
}
```

#### `SkillHolyWater::castendNoDamageId`

来源：`src/map/skills/acolyte/holywater.cpp:12-27`

```cpp
void SkillHolyWater::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
{
	map_session_data *sd = BL_CAST(BL_PC, src);

	if (sd)
	{
		if (skill_produce_mix(sd, getSkillId(), ITEMID_HOLY_WATER, 0, 0, 0, 1, -1))
		{
			if (skill_unit* su = map_find_skill_unit_oncell(bl, bl->x, bl->y, NJ_SUITON, nullptr, 0); su != nullptr)
				skill_delunit(su);
			clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);
		}
		else
			clif_skill_fail(*sd, getSkillId());
	}
}
```

### Signum Crucis (`AL_CRUCIS`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；范围：15；吟唱：500 ms；技能后摇：2000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 35；关联状态：SignumCrucis。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCrucis`
- 实现文件：`src/map/skills/acolyte/crucis.cpp`

#### `SkillCrucis::SkillCrucis`

来源：`src/map/skills/acolyte/crucis.cpp:10-12`

```cpp
SkillCrucis::SkillCrucis() : SkillImpl(AL_CRUCIS)
{
}
```

#### `SkillCrucis::castendNoDamageId`

来源：`src/map/skills/acolyte/crucis.cpp:14-25`

```cpp
void SkillCrucis::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
{
	sc_type type = skill_get_sc(getSkillId());

	if (flag & 1)
		sc_start(src, bl, type, 25 + skill_lv * 4 + status_get_lv(src) - status_get_lv(bl), skill_lv, skill_get_time(getSkillId(), skill_lv));
	else
	{
		map_foreachinallrange(skill_area_sub, src, skill_get_splash(getSkillId(), skill_lv), BL_CHAR, src, getSkillId(), skill_lv, tick, flag | BCT_ENEMY | 1, skill_castend_nodamage_id);
		clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);
	}
}
```

### Angelus (`AL_ANGELUS`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；范围：-1；吟唱：500 ms；技能后摇：3500 ms；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000; Lv6=180000; Lv7=210000; Lv8=240000; Lv9=270000; Lv10=300000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=23; Lv2=26; Lv3=29; Lv4=32; Lv5=35; Lv6=38; Lv7=41; Lv8=44; Lv9=47; Lv10=50；关联状态：Angelus。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAngelus`
- 实现文件：`src/map/skills/acolyte/angelus.cpp`

#### `SkillAngelus::SkillAngelus`

来源：`src/map/skills/acolyte/angelus.cpp:10-12`

```cpp
SkillAngelus::SkillAngelus() : SkillImpl(AL_ANGELUS)
{
}
```

#### `SkillAngelus::castendNoDamageId`

来源：`src/map/skills/acolyte/angelus.cpp:14-33`

```cpp
void SkillAngelus::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
{
	map_session_data *sd = BL_CAST(BL_PC, src);

	if (sd == nullptr || sd->status.party_id == 0 || (flag & 1))
	{
		sc_type type = skill_get_sc(getSkillId());

		// Animations don't play when outside visible range
		if (check_distance_bl(src, bl, AREA_SIZE))
			clif_skill_nodamage(bl, *bl, getSkillId(), skill_lv);


		sc_start(src, bl, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
	}
	else if (sd != nullptr)
	{
		party_foreachsamemap(skill_area_sub, sd, skill_get_splash(getSkillId(), skill_lv), src, getSkillId(), skill_lv, tick, flag | BCT_PARTY | 1, skill_castend_nodamage_id);
	}
}
```

### Blessing (`AL_BLESSING`)

魔法技能；目标：友方目标；最高等级 10；射程：9；命中类型：Single；段数：1；持续时间1：Lv1=60000; Lv2=80000; Lv3=100000; Lv4=120000; Lv5=140000; Lv6=160000; Lv7=180000; Lv8=200000; Lv9=220000; Lv10=240000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=28; Lv2=32; Lv3=36; Lv4=40; Lv5=44; Lv6=48; Lv7=52; Lv8=56; Lv9=60; Lv10=64；关联状态：Blessing。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBlessing`
- 实现文件：`src/map/skills/acolyte/blessing.cpp`

#### `SkillBlessing::SkillBlessing`

来源：`src/map/skills/acolyte/blessing.cpp:10-12`

```cpp
SkillBlessing::SkillBlessing() : SkillImpl(AL_BLESSING)
{
}
```

#### `SkillBlessing::castendNoDamageId`

来源：`src/map/skills/acolyte/blessing.cpp:14-29`

```cpp
void SkillBlessing::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
{
	map_session_data *dstsd = BL_CAST(BL_PC, bl);
	status_change *tsc = status_get_sc(bl);
	sc_type type = skill_get_sc(getSkillId());

	clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);
	if (dstsd != nullptr && tsc && tsc->getSCE(SC_CHANGEUNDEAD))
	{
		status_data* tstatus = status_get_status_data(*bl);
		if (tstatus->hp > 1)
			skill_attack(BF_MISC, src, src, bl, getSkillId(), skill_lv, tick, flag);
		return;
	}
	sc_start(src, bl, type, 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
}
```

### Cure (`AL_CURE`)

魔法技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；技能后摇：1000 ms；持续时间2：6000 ms；伤害标记：NoDamage；消耗/限制：SP 15。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCure`
- 实现文件：`src/map/skills/acolyte/cure.cpp`

#### `SkillCure::SkillCure`

来源：`src/map/skills/acolyte/cure.cpp:9-11`

```cpp
SkillCure::SkillCure() : SkillImpl(AL_CURE)
{
}
```

#### `SkillCure::castendNoDamageId`

来源：`src/map/skills/acolyte/cure.cpp:13-25`

```cpp
void SkillCure::castendNoDamageId(block_list *src, block_list *bl, uint16 skill_lv, t_tick tick, int32& flag) const
{
	if (status_isimmune(bl))
	{
		clif_skill_nodamage(src, *bl, getSkillId(), skill_lv, false);
		return;
	}
	status_change_end(bl, SC_SILENCE);
	status_change_end(bl, SC_BLIND);
	status_change_end(bl, SC_CONFUSION);
	status_change_end(bl, SC_BITESCAR);
	clif_skill_nodamage(src, *bl, getSkillId(), skill_lv);
}
```

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
