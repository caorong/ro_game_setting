# Crusader 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 63 | `KN_RIDING` / Peco Peco Riding | `core-source-references` | `` | src/map/pc.cpp, src/map/status.cpp |
| 64 | `KN_CAVALIERMASTERY` / Cavalier Mastery | `core-source-references` | `` | src/map/status.cpp |
| 55 | `KN_SPEARMASTERY` / Spear Mastery | `core-source-references` | `` | src/map/battle.cpp, src/map/skills/swordman/phantomthrust.cpp |
| 35 | `AL_CURE` / Cure | `exact-class-methods` | `SkillCure` | src/map/skills/acolyte/cure.cpp |
| 22 | `AL_DP` / Divine Protection | `core-source-references` | `` | src/map/battle.cpp |
| 23 | `AL_DEMONBANE` / Demon Bane | `core-source-references` | `` | src/map/battle.cpp |
| 28 | `AL_HEAL` / Heal | `exact-class-methods` | `SkillHeal` | src/map/skills/acolyte/heal.cpp |
| 248 | `CR_TRUST` / Faith | `core-source-references` | `` | src/map/status.cpp |
| 249 | `CR_AUTOGUARD` / Guard | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 250 | `CR_SHIELDCHARGE` / Smite | `exact-class-methods` | `SkillSmite` | src/map/skills/swordman/smite.cpp |
| 251 | `CR_SHIELDBOOMERANG` / Shield Boomerang | `exact-class-methods` | `SkillShieldBoomerang` | src/map/skills/swordman/shieldboomerang.cpp |
| 252 | `CR_REFLECTSHIELD` / Shield Reflect | `exact-class-methods` | `SkillShieldReflect` | src/map/skills/swordman/shieldreflect.cpp |
| 253 | `CR_HOLYCROSS` / Holy Cross | `exact-class-methods` | `SkillHolyCross` | src/map/skills/swordman/holycross.cpp |
| 254 | `CR_GRANDCROSS` / Grand Cross | `exact-class-methods` | `SkillGrandCross` | src/map/skills/swordman/grandcross.cpp |
| 255 | `CR_DEVOTION` / Sacrifice | `exact-class-methods` | `SkillSacrifice` | src/map/skills/swordman/sacrifice.cpp |
| 256 | `CR_PROVIDENCE` / Resistant Souls | `exact-class-methods` | `SkillResistantSouls` | src/map/skills/swordman/resistantsouls.cpp |
| 257 | `CR_DEFENDER` / Defending Aura | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 258 | `CR_SPEARQUICKEN` / Spear Quicken | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 1002 | `CR_SHRINK` / Shrink | `generic-or-class-mapped` | `StatusSkillImpl` |  |

## 详细公式与效果实现

### Peco Peco Riding (`KN_RIDING`)

武器/物理技能；目标：被动；最高等级 1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/pc.cpp`, `src/map/status.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Cavalier Mastery (`KN_CAVALIERMASTERY`)

武器/物理技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
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
// src/map/status.cpp:2406
? (job->aspd_base[sd->status.weapon]) // Single weapon
// src/map/status.cpp:2407
: (job->aspd_base[sd->weapontype1] + job->aspd_base[sd->weapontype2]) * 7 / 10; // Dual-wield
// src/map/status.cpp:4624
#ifndef RENEWAL_ASPD
// src/map/status.cpp:4626
base_status->aspd_rate -= 5*skill;
// src/map/status.cpp:4628
base_status->aspd_rate -= 30*skill;
```

### Spear Mastery (`KN_SPEARMASTERY`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/swordman/phantomthrust.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
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
// src/map/battle.cpp:2362
damage += (skill * 3);
// src/map/battle.cpp:2364
damage += (skill * 5);
// src/map/skills/swordman/phantomthrust.cpp:18
void SkillPhantomThrust::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
// src/map/skills/swordman/phantomthrust.cpp:19
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/swordman/phantomthrust.cpp:22
skillratio += -100 + 50 * skill_lv + 10 * (sd ? pc_checkskill(sd,KN_SPEARMASTERY) : 5);
// src/map/skills/swordman/phantomthrust.cpp:26
void SkillPhantomThrust::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/swordman/phantomthrust.cpp:28
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/swordman/phantomthrust.cpp:32
WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, flag);
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

### Faith (`CR_TRUST`)

非伤害技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:3142
status_change *sc = status_get_sc(bl);
// src/map/status.cpp:3147
uint16 skill_lv;
// src/map/status.cpp:3149
bonus += sd->bonus.hp;
// src/map/status.cpp:3150
if ((skill_lv = pc_checkskill(sd,CR_TRUST)) > 0)
// src/map/status.cpp:3151
bonus += skill_lv * 200;
// src/map/status.cpp:3159
if ((skill_lv = pc_checkskill(sd, NV_BREAKTHROUGH)) > 0)
// src/map/status.cpp:3160
bonus += 350 * skill_lv + (skill_lv > 4 ? 250 : 0);
// src/map/status.cpp:3161
if ((skill_lv = pc_checkskill(sd, NV_TRANSCENDENCE)) > 0)
// src/map/status.cpp:3162
bonus += 350 * skill_lv + (skill_lv > 4 ? 250 : 0);
// src/map/status.cpp:4666
if(sd->dsprate < 0)
// src/map/status.cpp:4667
sd->dsprate = 0;
// src/map/status.cpp:4668
if(sd->castrate < 0)
// src/map/status.cpp:4669
sd->castrate = 0;
// src/map/status.cpp:4670
if(sd->hprecov_rate < 0)
// src/map/status.cpp:4671
sd->hprecov_rate = 0;
// src/map/status.cpp:4672
if(sd->sprecov_rate < 0)
```

### Guard (`CR_AUTOGUARD`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30；状态 Shield；关联状态：AutoGuard。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:1532
delay = 100;
// src/map/battle.cpp:1542
{ //If player is target of devotion, show guard effect on the devotion caster rather than the target
// src/map/battle.cpp:1543
clif_skill_nodamage(d_bl, *d_bl, CR_AUTOGUARD, sce->val1);
// src/map/battle.cpp:1544
unit_set_walkdelay(d_bl, gettick(), delay, 1);
// src/map/battle.cpp:1548
clif_skill_nodamage(target, *target, CR_AUTOGUARD, sce->val1);
// src/map/battle.cpp:1549
unit_set_walkdelay(target, gettick(), delay, 1);
// src/map/battle.cpp:1552
sc_start(target, src, SC_STUN, 50, skill_lv, skill_get_time2(skill_id, skill_lv));
```

### Smite (`CR_SHIELDCHARGE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：3；命中类型：Single；段数：1；击退：Lv1=5; Lv2=6; Lv3=7; Lv4=8; Lv5=9；持续时间2：5000 ms；消耗/限制：SP 10；状态 Shield；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSmite`
- 实现文件：`src/map/skills/swordman/smite.cpp`

#### `SkillSmite::SkillSmite`

来源：`src/map/skills/swordman/smite.cpp:8-9`

```cpp
SkillSmite::SkillSmite() : WeaponSkillImpl(CR_SHIELDCHARGE) {
}
```

#### `SkillSmite::calculateSkillRatio`

来源：`src/map/skills/swordman/smite.cpp:11-13`

```cpp
void SkillSmite::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += 20 * skill_lv;
}
```

#### `SkillSmite::applyAdditionalEffects`

来源：`src/map/skills/swordman/smite.cpp:15-17`

```cpp
void SkillSmite::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src,target,SC_STUN,(15+skill_lv*5),skill_lv,skill_get_time2(getSkillId(),skill_lv));
}
```

### Shield Boomerang (`CR_SHIELDBOOMERANG`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：Lv1=3; Lv2=5; Lv3=7; Lv4=9; Lv5=11；命中类型：Single；段数：1；技能后摇：700 ms；消耗/限制：SP 12；状态 Shield。

- 覆盖：`exact-class-methods`
- 实现类：`SkillShieldBoomerang`
- 实现文件：`src/map/skills/swordman/shieldboomerang.cpp`

#### `SkillShieldBoomerang::SkillShieldBoomerang`

来源：`src/map/skills/swordman/shieldboomerang.cpp:8-9`

```cpp
SkillShieldBoomerang::SkillShieldBoomerang() : WeaponSkillImpl(CR_SHIELDBOOMERANG) {
}
```

#### `SkillShieldBoomerang::calculateSkillRatio`

来源：`src/map/skills/swordman/shieldboomerang.cpp:11-17`

```cpp
void SkillShieldBoomerang::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += -100 + skill_lv * 80;
#else
	base_skillratio += 30 * skill_lv;
#endif
}
```

#### `SkillShieldBoomerang::modifyElement`

来源：`src/map/skills/swordman/shieldboomerang.cpp:19-25`

```cpp
void SkillShieldBoomerang::modifyElement(const Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv, int32& element, int32 flag) const {
#ifdef RENEWAL
	// flag 1 means the element should be calculated for damage only
	if (flag & 1)
		element = ELE_NEUTRAL;
#endif
}
```

### Shield Reflect (`CR_REFLECTSHIELD`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=35; Lv2=40; Lv3=45; Lv4=50; Lv5=55; Lv6=60; Lv7=65; Lv8=70; Lv9=75; Lv10=80；状态 Shield；关联状态：ReflectShield。

- 覆盖：`exact-class-methods`
- 实现类：`SkillShieldReflect`
- 实现文件：`src/map/skills/swordman/shieldreflect.cpp`

#### `SkillShieldReflect::SkillShieldReflect`

来源：`src/map/skills/swordman/shieldreflect.cpp:10-11`

```cpp
SkillShieldReflect::SkillShieldReflect() : StatusSkillImpl(CR_REFLECTSHIELD) {
}
```

#### `SkillShieldReflect::castendNoDamageId`

来源：`src/map/skills/swordman/shieldreflect.cpp:13-24`

```cpp
void SkillShieldReflect::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	status_change* tsc = status_get_sc(target);

	if (tsc && tsc->getSCE(SC_DARKCROW)) { // SC_DARKCROW prevents using reflecting skills
		if (sd)
			clif_skill_fail( *sd, getSkillId(), USESKILL_FAIL );
		return;
	}

	StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
}
```

### Holy Cross (`CR_HOLYCROSS`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-2；命中类型：Multi_Hit；段数：-2；属性：Holy；持续时间2：30000 ms；消耗/限制：SP Lv1=11; Lv2=12; Lv3=13; Lv4=14; Lv5=15; Lv6=16; Lv7=17; Lv8=18; Lv9=19; Lv10=20；关联状态：Blind。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHolyCross`
- 实现文件：`src/map/skills/swordman/holycross.cpp`

#### `SkillHolyCross::SkillHolyCross`

来源：`src/map/skills/swordman/holycross.cpp:11-12`

```cpp
SkillHolyCross::SkillHolyCross() : WeaponSkillImpl(CR_HOLYCROSS) {
}
```

#### `SkillHolyCross::calculateSkillRatio`

来源：`src/map/skills/swordman/holycross.cpp:14-23`

```cpp
void SkillHolyCross::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const map_session_data* sd = BL_CAST(BL_PC, src);

	if(sd && sd->status.weapon == W_2HSPEAR)
		base_skillratio += 70 * skill_lv;
	else
#endif
		base_skillratio += 35 * skill_lv;
}
```

#### `SkillHolyCross::applyAdditionalEffects`

来源：`src/map/skills/swordman/holycross.cpp:25-27`

```cpp
void SkillHolyCross::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src,target,SC_BLIND,3*skill_lv,skill_lv,skill_get_time2(getSkillId(),skill_lv));
}
```

### Grand Cross (`CR_GRANDCROSS`)

魔法技能；目标：自身；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Holy；吟唱：3000 ms；技能后摇：1500 ms；移动后摇：1000 ms；持续时间1：950 ms；持续时间2：30000 ms；消耗/限制：SP Lv1=37; Lv2=44; Lv3=51; Lv4=58; Lv5=65; Lv6=72; Lv7=79; Lv8=86; Lv9=93; Lv10=100；HP% 20；关联状态：Blind。

- 覆盖：`exact-class-methods`
- 实现类：`SkillGrandCross`
- 实现文件：`src/map/skills/swordman/grandcross.cpp`

#### `SkillGrandCross::SkillGrandCross`

来源：`src/map/skills/swordman/grandcross.cpp:9-10`

```cpp
SkillGrandCross::SkillGrandCross() : SkillImpl(CR_GRANDCROSS) {
}
```

#### `SkillGrandCross::applyCounterAdditionalEffects`

来源：`src/map/skills/swordman/grandcross.cpp:12-18`

```cpp
void SkillGrandCross::applyCounterAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& attack_type) const {
	if (src == target) {
		// Grand Cross on self specifically only triggers "When hit by physical attack" autospells and ignores everything else
		attack_type |= BF_WEAPON;
		attack_type &= ~BF_MAGIC;
	}
}
```

#### `SkillGrandCross::castendPos2`

来源：`src/map/skills/swordman/grandcross.cpp:20-25`

```cpp
void SkillGrandCross::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag|=1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillGrandCross::applyAdditionalEffects`

来源：`src/map/skills/swordman/grandcross.cpp:27-34`

```cpp
void SkillGrandCross::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	map_session_data* dstsd = BL_CAST(BL_PC, target);
	status_data* tstatus = status_get_status_data(*target);

	//Chance to cause blind status vs demon and undead element, but not against players
	if(!dstsd && (battle_check_undead(tstatus->race,tstatus->def_ele) || tstatus->race == RC_DEMON))
		sc_start(src,target,SC_BLIND,100,skill_lv,skill_get_time2(getSkillId(),skill_lv));
}
```

### Sacrifice (`CR_DEVOTION`)

非伤害技能；目标：友方目标；最高等级 5；射程：Lv1=7; Lv2=8; Lv3=9; Lv4=10; Lv5=11；命中类型：Single；段数：1；吟唱：3000 ms；持续时间2：Lv1=30000; Lv2=45000; Lv3=60000; Lv4=75000; Lv5=90000 ms；伤害标记：NoDamage；消耗/限制：SP 25；关联状态：Devotion。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSacrifice`
- 实现文件：`src/map/skills/swordman/sacrifice.cpp`

#### `SkillSacrifice::SkillSacrifice`

来源：`src/map/skills/swordman/sacrifice.cpp:10-11`

```cpp
SkillSacrifice::SkillSacrifice() : SkillImpl(CR_DEVOTION) {
}
```

#### `SkillSacrifice::castendNoDamageId`

来源：`src/map/skills/swordman/sacrifice.cpp:13-60`

```cpp
void SkillSacrifice::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if (!sd) {
		return;
	}

	sc_type type = skill_get_sc(getSkillId());

	int32 count, lv;
	if( !dstsd )
	{ // Only players can be devoted
		clif_skill_fail( *sd, getSkillId() );
		return;
	}

	if( (lv = status_get_lv(src) - dstsd->status.base_level) < 0 )
		lv = -lv;
	if( lv > battle_config.devotion_level_difference || // Level difference requeriments
		(dstsd->sc.getSCE(type) && dstsd->sc.getSCE(type)->val1 != src->id) || // Cannot Devote a player devoted from another source
		(dstsd->class_&MAPID_SECONDMASK) == MAPID_CRUSADER || // Crusader Cannot be devoted
		(dstsd->sc.getSCE(SC_HELLPOWER))) // Players affected by SC_HELLPOWER cannot be devoted.
	{
		clif_skill_fail( *sd, getSkillId() );
		return;
	}

	int32 i = 0;
	count = min(skill_lv,MAX_DEVOTION);

	ARR_FIND(0, count, i, sd->devotion[i] == target->id );
	if( i == count )
	{
		ARR_FIND(0, count, i, sd->devotion[i] == 0 );
		if( i == count )
		{ // No free slots, skill Fail
			clif_skill_fail( *sd, getSkillId() );
			return;
		}
	}

	sd->devotion[i] = target->id;

	clif_skill_nodamage(src, *target, getSkillId(), skill_lv,
		sc_start4(src, target, type, 10000, src->id, i, skill_get_range2(src, getSkillId(), skill_lv, true), 0, skill_get_time2(getSkillId(), skill_lv)));
	clif_devotion(src, nullptr);
}
```

### Resistant Souls (`CR_PROVIDENCE`)

非伤害技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：3000 ms；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 30；关联状态：Providence。

- 覆盖：`exact-class-methods`
- 实现类：`SkillResistantSouls`
- 实现文件：`src/map/skills/swordman/resistantsouls.cpp`

#### `SkillResistantSouls::SkillResistantSouls`

来源：`src/map/skills/swordman/resistantsouls.cpp:10-11`

```cpp
SkillResistantSouls::SkillResistantSouls() : SkillImpl(CR_PROVIDENCE) {
}
```

#### `SkillResistantSouls::castendNoDamageId`

来源：`src/map/skills/swordman/resistantsouls.cpp:13-25`

```cpp
void SkillResistantSouls::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if(sd && dstsd){ //Check they are not another crusader [Skotlex]
		if ((dstsd->class_&MAPID_SECONDMASK) == MAPID_CRUSADER) {
			clif_skill_fail( *sd, getSkillId() );
			return;
		}
	}
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start(src,target,skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
}
```

### Defending Aura (`CR_DEFENDER`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；技能后摇：800 ms；持续时间1：180000 ms；伤害标记：NoDamage；消耗/限制：SP 30；状态 Shield；关联状态：Defender。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:12146
val2 = (status->int_ + status->luk) * val1 / 20 * status_get_lv(bl) / 200 + val1;	// Chance to evade magic damage.
// src/map/status.cpp:12150
val2 = 5; // 5% HP every 3 seconds
// src/map/status.cpp:12155
val2 = 3; // 3% SP every 5 seconds
```

### Spear Quicken (`CR_SPEARQUICKEN`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000; Lv6=180000; Lv7=210000; Lv8=240000; Lv9=270000; Lv10=300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=24; Lv2=28; Lv3=32; Lv4=36; Lv5=40; Lv6=44; Lv7=48; Lv8=52; Lv9=56; Lv10=60；武器 2hSpear；关联状态：SpearQuicken。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skills/swordman/overbrand.cpp:16
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/swordman/overbrand.cpp:17
skill_castend_damage_id(src, target, getSkillId(), skill_lv, tick, flag);
// src/map/skills/swordman/overbrand.cpp:20
void SkillOverBrand::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& skillratio, int32 mflag) const {
// src/map/skills/swordman/overbrand.cpp:21
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/swordman/overbrand.cpp:22
const status_change* sc = status_get_sc(src);
// src/map/skills/swordman/overbrand.cpp:25
skillratio += -100 + 500 * skill_lv;
// src/map/skills/swordman/overbrand.cpp:27
skillratio += -100 + 350 * skill_lv;
// src/map/skills/swordman/overbrand.cpp:28
skillratio += ((sd) ? pc_checkskill(sd, CR_SPEARQUICKEN) * 50 : 0);
```

### Shrink (`CR_SHRINK`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；击退：2；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP 15；状态 Shield；关联状态：Shrink。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:1543
clif_skill_nodamage(d_bl, *d_bl, CR_AUTOGUARD, sce->val1);
// src/map/battle.cpp:1544
unit_set_walkdelay(d_bl, gettick(), delay, 1);
// src/map/battle.cpp:1548
clif_skill_nodamage(target, *target, CR_AUTOGUARD, sce->val1);
// src/map/battle.cpp:1549
unit_set_walkdelay(target, gettick(), delay, 1);
// src/map/battle.cpp:1552
sc_start(target, src, SC_STUN, 50, skill_lv, skill_get_time2(skill_id, skill_lv));
// src/map/battle.cpp:1564
|| skill_id == CR_ACIDDEMONSTRATION
```
