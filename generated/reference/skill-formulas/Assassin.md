# Assassin 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 132 | `AS_RIGHT` / Righthand Mastery | `core-source-references` | `` | src/map/battle.cpp |
| 133 | `AS_LEFT` / Lefthand Mastery | `core-source-references` | `` | src/map/battle.cpp, src/map/pc.cpp |
| 134 | `AS_KATAR` / Katar Mastery | `core-source-references` | `` | src/map/battle.cpp |
| 135 | `AS_CLOAKING` / Cloaking | `exact-class-methods` | `SkillCloaking` | src/map/skills/thief/cloaking.cpp |
| 136 | `AS_SONICBLOW` / Sonic Blow | `exact-class-methods` | `SkillSonicBlow` | src/map/skills/thief/sonicblow.cpp |
| 137 | `AS_GRIMTOOTH` / Grimtooth | `exact-class-methods` | `SkillGrimtooth` | src/map/skills/thief/grimtooth.cpp |
| 138 | `AS_ENCHANTPOISON` / Enchant Poison | `exact-class-methods` | `SkillEnchantPoison` | src/map/skills/thief/enchantpoison.cpp |
| 139 | `AS_POISONREACT` / Poison React | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 140 | `AS_VENOMDUST` / Venom Dust | `exact-class-methods` | `SkillVenomDust` | src/map/skills/thief/venomdust.cpp |
| 141 | `AS_SPLASHER` / Venom Splasher | `exact-class-methods` | `SkillVenomSplasher` | src/map/skills/thief/venomsplasher.cpp |
| 1003 | `AS_SONICACCEL` / Sonic Acceleration | `core-source-references` | `` | src/map/battle.cpp, src/map/skills/thief/sonicblow.cpp |
| 1004 | `AS_VENOMKNIFE` / Throw Venom Knife | `exact-class-methods` | `SkillThrowVenomKnife` | src/map/skills/thief/throwvenomknife.cpp |

## 详细公式与效果实现

### Righthand Mastery (`AS_RIGHT`)

武器/物理技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:5034
if(sd->status.weapon == W_KATAR && !skill_id) { //Katars (offhand damage only applies to normal attacks, tested on Aegis 10.2)
// src/map/battle.cpp:5036
wd->damage2 = (int64)wd->damage * (1 + (skill * 2))/100;
// src/map/battle.cpp:5043
if (is_attack_right_handed(src, skill_id) && wd->damage) {
// src/map/battle.cpp:5046
ATK_RATER(wd->damage, 50 + (skill * 10))
// src/map/battle.cpp:5050
ATK_RATER(wd->damage, 70 + (skill * 10))
// src/map/battle.cpp:5052
if(wd->damage < 1)
// src/map/battle.cpp:5053
wd->damage = 1;
// src/map/battle.cpp:5056
if (wd->damage2) {
```

### Lefthand Mastery (`AS_LEFT`)

武器/物理技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/pc.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:5046
ATK_RATER(wd->damage, 50 + (skill * 10))
// src/map/battle.cpp:5050
ATK_RATER(wd->damage, 70 + (skill * 10))
// src/map/battle.cpp:5052
if(wd->damage < 1)
// src/map/battle.cpp:5053
wd->damage = 1;
// src/map/battle.cpp:5056
if (wd->damage2) {
// src/map/battle.cpp:5059
ATK_RATEL(wd->damage2, 30 + (skill * 10))
// src/map/battle.cpp:5063
ATK_RATEL(wd->damage2, 50 + (skill * 10))
// src/map/battle.cpp:5065
if(wd->damage2 < 1)
// src/map/battle.cpp:5066
wd->damage2 = 1;
```

### Katar Mastery (`AS_KATAR`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2383
damage += (skill * 3);
// src/map/battle.cpp:2387
damage += (skill * 3);
// src/map/battle.cpp:2391
damage += (skill * 3);
// src/map/battle.cpp:2395
damage += (skill * 3);
// src/map/battle.cpp:2399
return damage;
// src/map/battle.cpp:2402
/** Calculates overrefine damage bonus and weapon related bonuses (unofficial)
// src/map/battle.cpp:2404
* @param damage Current damage
```

### Cloaking (`AS_CLOAKING`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：Lv1=500; Lv2=1000; Lv3=2000; Lv4=3000; Lv5=4000; Lv6=5000; Lv7=6000; Lv8=7000; Lv9=8000; Lv10=9000 ms；伤害标记：NoDamage；消耗/限制：SP 15；关联状态：Cloaking。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCloaking`
- 实现文件：`src/map/skills/thief/cloaking.cpp`

#### `SkillCloaking::SkillCloaking`

来源：`src/map/skills/thief/cloaking.cpp:10-11`

```cpp
SkillCloaking::SkillCloaking() : SkillImpl(AS_CLOAKING) {
}
```

#### `SkillCloaking::castendNoDamageId`

来源：`src/map/skills/thief/cloaking.cpp:13-33`

```cpp
void SkillCloaking::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );
	sc_type type = skill_get_sc(getSkillId());
	status_change *tsc = status_get_sc(target);
	status_change_entry *tsce = (tsc && type != SC_NONE)?tsc->getSCE(type):nullptr;
	int32 i = 0;

	if (tsce) {
		i = status_change_end(target, type);
		if( i )
			clif_skill_nodamage(src,*target,getSkillId(),-1,i);
		else if( sd )
			clif_skill_fail( *sd, getSkillId() );
		return;
	}
	i = sc_start(src,target,type,100,skill_lv,skill_get_time(getSkillId(),skill_lv));
	if( i )
		clif_skill_nodamage(src,*target,getSkillId(),-1,i);
	else if( sd )
		clif_skill_fail( *sd, getSkillId(),  USESKILL_FAIL_LEVEL );
}
```

### Sonic Blow (`AS_SONICBLOW`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：1；命中类型：Multi_Hit；段数：-8；属性：Weapon；技能后摇：2000 ms；移动后摇：2000 ms；持续时间2：5000 ms；消耗/限制：SP Lv1=16; Lv2=18; Lv3=20; Lv4=22; Lv5=24; Lv6=26; Lv7=28; Lv8=30; Lv9=32; Lv10=34；武器 Katar；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSonicBlow`
- 实现文件：`src/map/skills/thief/sonicblow.cpp`

#### `SkillSonicBlow::SkillSonicBlow`

来源：`src/map/skills/thief/sonicblow.cpp:11-12`

```cpp
SkillSonicBlow::SkillSonicBlow() : WeaponSkillImpl(AS_SONICBLOW) {
}
```

#### `SkillSonicBlow::calculateSkillRatio`

来源：`src/map/skills/thief/sonicblow.cpp:14-28`

```cpp
void SkillSonicBlow::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const status_data* tstatus = status_get_status_data(*target);

	base_skillratio += 100 + 100 * skill_lv;
	if (tstatus->hp < (tstatus->max_hp / 2))
		base_skillratio += base_skillratio / 2;
#else
	const map_session_data* sd = BL_CAST( BL_PC, src );

	base_skillratio += 200 + 50 * skill_lv;
	if (sd && pc_checkskill(sd, AS_SONICACCEL) > 0)
		base_skillratio += base_skillratio / 10;
#endif
}
```

#### `SkillSonicBlow::applyAdditionalEffects`

来源：`src/map/skills/thief/sonicblow.cpp:30-37`

```cpp
void SkillSonicBlow::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	status_change *sc = status_get_sc(src);

	if (!map_flag_gvg2(target->m) && !map_getmapflag(target->m, MF_BATTLEGROUND) && sc && sc->getSCE(SC_SPIRIT) && sc->getSCE(SC_SPIRIT)->val2 == SL_ASSASIN)
		sc_start(src, target, SC_STUN, (4 * skill_lv + 20), skill_lv, skill_get_time2(getSkillId(), skill_lv)); //Link gives double stun chance outside GVG/BG
	else
		sc_start(src, target, SC_STUN, (2 * skill_lv + 10), skill_lv, skill_get_time2(getSkillId(), skill_lv));
}
```

#### `SkillSonicBlow::modifyHitRate`

来源：`src/map/skills/thief/sonicblow.cpp:39-48`

```cpp
void SkillSonicBlow::modifyHitRate(int16& hit_rate, const block_list* src, const block_list* target, uint16 skill_lv) const {
	const map_session_data* sd = BL_CAST( BL_PC, src );

	if(sd && pc_checkskill(sd,AS_SONICACCEL) > 0)
#ifdef RENEWAL
		hit_rate += hit_rate * 90 / 100;
#else
		hit_rate += hit_rate * 50 / 100;
#endif
}
```

### Grimtooth (`AS_GRIMTOOTH`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：Lv1=3; Lv2=4; Lv3=5; Lv4=6; Lv5=7；命中类型：Single；段数：1；属性：Weapon；范围：1；持续时间2：1000 ms；伤害标记：Splash；消耗/限制：SP 3；武器 Katar；前置状态 Hiding。

- 覆盖：`exact-class-methods`
- 实现类：`SkillGrimtooth`
- 实现文件：`src/map/skills/thief/grimtooth.cpp`

#### `SkillGrimtooth::SkillGrimtooth`

来源：`src/map/skills/thief/grimtooth.cpp:9-10`

```cpp
SkillGrimtooth::SkillGrimtooth() : SkillImplRecursiveDamageSplash(AS_GRIMTOOTH) {
}
```

#### `SkillGrimtooth::calculateSkillRatio`

来源：`src/map/skills/thief/grimtooth.cpp:12-14`

```cpp
void SkillGrimtooth::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 20 * skill_lv;
}
```

#### `SkillGrimtooth::castendDamageId`

来源：`src/map/skills/thief/grimtooth.cpp:16-20`

```cpp
void SkillGrimtooth::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag |= SD_PREAMBLE; // a fake packet will be sent for the first target to be hit

	SkillImplRecursiveDamageSplash::castendDamageId(src, target, skill_lv, tick, flag);
}
```

#### `SkillGrimtooth::applyAdditionalEffects`

来源：`src/map/skills/thief/grimtooth.cpp:22-28`

```cpp
void SkillGrimtooth::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	status_data* tstatus = status_get_status_data(*target);
	mob_data* dstmd = BL_CAST(BL_MOB, target);

	if (dstmd && !status_has_mode(tstatus,MD_STATUSIMMUNE))
		sc_start(src,target,SC_QUAGMIRE,100,0,skill_get_time2(getSkillId(),skill_lv));
}
```

### Enchant Poison (`AS_ENCHANTPOISON`)

武器/物理技能；目标：友方目标；最高等级 10；射程：1；命中类型：Single；段数：1；属性：Poison；持续时间1：Lv1=30000; Lv2=45000; Lv3=60000; Lv4=75000; Lv5=90000; Lv6=105000; Lv7=120000; Lv8=135000; Lv9=150000; Lv10=165000 ms；持续时间2：Lv1=10000; Lv2=20000; Lv3=30000; Lv4=40000; Lv5=50000; Lv6=60000; Lv7=70000; Lv8=80000; Lv9=90000; Lv10=100000 ms；伤害标记：NoDamage；消耗/限制：SP 20；关联状态：EncPoison。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEnchantPoison`
- 实现文件：`src/map/skills/thief/enchantpoison.cpp`

#### `SkillEnchantPoison::SkillEnchantPoison`

来源：`src/map/skills/thief/enchantpoison.cpp:10-11`

```cpp
SkillEnchantPoison::SkillEnchantPoison() : SkillImpl(AS_ENCHANTPOISON) {
}
```

#### `SkillEnchantPoison::castendNoDamageId`

来源：`src/map/skills/thief/enchantpoison.cpp:13-26`

```cpp
void SkillEnchantPoison::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start( src, target, type, 100, skill_lv, skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
	}else{
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv, false );

		if( sd != nullptr ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Poison React (`AS_POISONREACT`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：Lv1=20000; Lv2=25000; Lv3=30000; Lv4=35000; Lv5=40000; Lv6=45000; Lv7=50000; Lv8=55000; Lv9-10=60000 ms；持续时间2：60000 ms；消耗/限制：SP Lv1=25; Lv2=30; Lv3=35; Lv4=40; Lv5=45; Lv6=50; Lv7=55; Lv8=60; Lv9-10=45；关联状态：PoisonReact。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:4428
skillratio += sc->getSCE(SC_MAXOVERTHRUST)->val2;
// src/map/battle.cpp:4431
skillratio += 100;
// src/map/battle.cpp:4433
skillratio += 200;
// src/map/battle.cpp:4436
if (const status_change_entry* sce = sc->getSCE(SC_POISONREACT); sce != nullptr && sce->val4 == 1) {
// src/map/battle.cpp:4439
skillratio += 30 * pc_checkskill(sd, AS_POISONREACT);
// src/map/battle.cpp:4441
skillratio += 30 * sce->val1;
// src/map/battle.cpp:4443
sc_start2(src, target, SC_POISON, sce->val3, sce->val1, src->id, skill_get_time2(AS_POISONREACT, sce->val1), sstatus->amotion);
// src/map/battle.cpp:4444
status_change_end(src, SC_POISONREACT);
// src/map/battle.cpp:4447
if (sd) { //ATK [{Weapon Level * (Weapon Upgrade Level + 6) * 100} + (Weapon ATK) + (Weapon Weight)]%
// src/map/battle.cpp:4451
skillratio += -100 + sd->inventory_data[index]->weight / 10 + sd->inventory_data[index]->atk +
// src/map/battle.cpp:4454
status_change_end(src,SC_CRUSHSTRIKE);
// src/map/skills/thief/venomsplasher.cpp:12
SkillVenomSplasher::SkillVenomSplasher() : SkillImplRecursiveDamageSplash(AS_SPLASHER) {
// src/map/skills/thief/venomsplasher.cpp:15
void SkillVenomSplasher::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/thief/venomsplasher.cpp:16
const map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/thief/venomsplasher.cpp:19
base_skillratio += -100 + 400 + 100 * skill_lv;
// src/map/skills/thief/venomsplasher.cpp:21
base_skillratio += 400 + 50 * skill_lv;
```

### Venom Dust (`AS_VENOMDUST`)

武器/物理技能；目标：地面区域；最高等级 10；射程：2；命中类型：Single；段数：1；属性：Poison；持续时间1：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000; Lv6=30000; Lv7=35000; Lv8=40000; Lv9=45000; Lv10=50000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP 20；道具 Red_Gemstone×1；关联状态：Poison。

- 覆盖：`exact-class-methods`
- 实现类：`SkillVenomDust`
- 实现文件：`src/map/skills/thief/venomdust.cpp`

#### `SkillVenomDust::SkillVenomDust`

来源：`src/map/skills/thief/venomdust.cpp:7-8`

```cpp
SkillVenomDust::SkillVenomDust() : SkillImpl(AS_VENOMDUST) {
}
```

#### `SkillVenomDust::castendPos2`

来源：`src/map/skills/thief/venomdust.cpp:10-13`

```cpp
void SkillVenomDust::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Venom Splasher (`AS_SPLASHER`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：1；命中类型：Single；段数：1；属性：Weapon；范围：2；吟唱：1000 ms；冷却：Lv1=7500; Lv2=8000; Lv3=8500; Lv4=9000; Lv5=9500; Lv6=10000; Lv7=10500; Lv8=11000; Lv9=11500; Lv10=12000 ms；持续时间1：Lv1=11000; Lv2=10000; Lv3=9000; Lv4=8000; Lv5=7000; Lv6=6000; Lv7=5000; Lv8=4000; Lv9=3000; Lv10=2000 ms；持续时间2：60000 ms；伤害标记：NoDamage, IgnoreAtkCard, IgnoreFlee；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30；道具 Red_Gemstone×1；关联状态：Splasher。

- 覆盖：`exact-class-methods`
- 实现类：`SkillVenomSplasher`
- 实现文件：`src/map/skills/thief/venomsplasher.cpp`

#### `SkillVenomSplasher::SkillVenomSplasher`

来源：`src/map/skills/thief/venomsplasher.cpp:12-13`

```cpp
SkillVenomSplasher::SkillVenomSplasher() : SkillImplRecursiveDamageSplash(AS_SPLASHER) {
}
```

#### `SkillVenomSplasher::calculateSkillRatio`

来源：`src/map/skills/thief/venomsplasher.cpp:15-25`

```cpp
void SkillVenomSplasher::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const map_session_data* sd = BL_CAST( BL_PC, src );

#ifdef RENEWAL
	base_skillratio += -100 + 400 + 100 * skill_lv;
#else
	base_skillratio += 400 + 50 * skill_lv;
#endif
	if(sd)
		base_skillratio += 20 * pc_checkskill(sd,AS_POISONREACT);
}
```

#### `SkillVenomSplasher::castendNoDamageId`

来源：`src/map/skills/thief/venomsplasher.cpp:27-45`

```cpp
void SkillVenomSplasher::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( status_has_mode(tstatus,MD_STATUSIMMUNE)
	// Renewal dropped the 3/4 hp requirement
#ifndef RENEWAL
		|| tstatus-> hp > tstatus->max_hp*3/4
#endif
			) {
		if (sd) {
			clif_skill_fail( *sd, getSkillId() );
		}
		return;
	}
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start4(src,target,type,100,skill_lv,getSkillId(),src->id,skill_get_time(getSkillId(),skill_lv),1000));
}
```

#### `SkillVenomSplasher::castendDamageId`

来源：`src/map/skills/thief/venomsplasher.cpp:47-54`

```cpp
void SkillVenomSplasher::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	SkillImplRecursiveDamageSplash::castendDamageId(src, target, skill_lv, tick, flag);

	if (!(flag & 1)) {
		// Don't consume a second gemstone.
		flag |= SKILL_NOCONSUME_REQ;
	}
}
```

#### `SkillVenomSplasher::getSearchSize`

来源：`src/map/skills/thief/venomsplasher.cpp:56-59`

```cpp
int16 SkillVenomSplasher::getSearchSize(block_list* src, uint16 skill_lv) const {
	// Venom Splasher uses a different range for searching than for splashing
	return 1;
}
```

#### `SkillVenomSplasher::applyAdditionalEffects`

来源：`src/map/skills/thief/venomsplasher.cpp:61-63`

```cpp
void SkillVenomSplasher::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start2(src, target, SC_POISON, 100, skill_lv, src->id, skill_get_time2(getSkillId(), skill_lv));
}
```

### Sonic Acceleration (`AS_SONICACCEL`)

武器/物理技能；目标：被动；最高等级 1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/thief/sonicblow.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:4925
ATK_ADD(wd->damage, wd->damage2, 20 * sc->getSCE(SC_AURABLADE)->val1);
// src/map/battle.cpp:4931
battle_min_damage(*wd, *src, skill_id, 1);
// src/map/battle.cpp:4937
ATK_ADDRATE(wd->damage, wd->damage2, 90);
// src/map/battle.cpp:4944
* "Plant"-type (mobs that only take 1 damage from all sources) damage calculation
// src/map/skills/thief/sonicblow.cpp:14
void SkillSonicBlow::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
// src/map/skills/thief/sonicblow.cpp:18
base_skillratio += 100 + 100 * skill_lv;
// src/map/skills/thief/sonicblow.cpp:19
if (tstatus->hp < (tstatus->max_hp / 2))
// src/map/skills/thief/sonicblow.cpp:20
base_skillratio += base_skillratio / 2;
// src/map/skills/thief/sonicblow.cpp:22
const map_session_data* sd = BL_CAST( BL_PC, src );
// src/map/skills/thief/sonicblow.cpp:24
base_skillratio += 200 + 50 * skill_lv;
// src/map/skills/thief/sonicblow.cpp:26
base_skillratio += base_skillratio / 10;
// src/map/skills/thief/sonicblow.cpp:30
void SkillSonicBlow::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/thief/sonicblow.cpp:31
status_change *sc = status_get_sc(src);
// src/map/skills/thief/sonicblow.cpp:34
sc_start(src, target, SC_STUN, (4 * skill_lv + 20), skill_lv, skill_get_time2(getSkillId(), skill_lv)); //Link gives double stun chance outside GVG/BG
// src/map/skills/thief/sonicblow.cpp:36
sc_start(src, target, SC_STUN, (2 * skill_lv + 10), skill_lv, skill_get_time2(getSkillId(), skill_lv));
// src/map/skills/thief/sonicblow.cpp:39
void SkillSonicBlow::modifyHitRate(int16& hit_rate, const block_list* src, const block_list* target, uint16 skill_lv) const {
```

### Throw Venom Knife (`AS_VENOMKNIFE`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Multi_Hit；段数：1；持续时间2：60000 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP 15；弹药数 1；弹药 Dagger；关联状态：Poison。

- 覆盖：`exact-class-methods`
- 实现类：`SkillThrowVenomKnife`
- 实现文件：`src/map/skills/thief/throwvenomknife.cpp`

#### `SkillThrowVenomKnife::SkillThrowVenomKnife`

来源：`src/map/skills/thief/throwvenomknife.cpp:10-11`

```cpp
SkillThrowVenomKnife::SkillThrowVenomKnife() : WeaponSkillImpl(AS_VENOMKNIFE) {
}
```

#### `SkillThrowVenomKnife::calculateSkillRatio`

来源：`src/map/skills/thief/throwvenomknife.cpp:13-17`

```cpp
void SkillThrowVenomKnife::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 400;
#endif
}
```

#### `SkillThrowVenomKnife::applyAdditionalEffects`

来源：`src/map/skills/thief/throwvenomknife.cpp:19-21`

```cpp
void SkillThrowVenomKnife::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start2(src, target, SC_POISON, 100, skill_lv, src->id, skill_get_time2(getSkillId(), skill_lv));
}
```
