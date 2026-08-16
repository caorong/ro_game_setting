# Knight 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 55 | `KN_SPEARMASTERY` / Spear Mastery | `core-source-references` | `` | src/map/battle.cpp, src/map/skills/swordman/phantomthrust.cpp |
| 56 | `KN_PIERCE` / Pierce | `exact-class-methods` | `SkillPierce` | src/map/skills/swordman/pierce.cpp |
| 57 | `KN_BRANDISHSPEAR` / Brandish Spear | `exact-class-methods` | `SkillBrandishSpear` | src/map/skills/swordman/brandishspear.cpp |
| 58 | `KN_SPEARSTAB` / Spear Stab | `exact-class-methods` | `SkillSpearStab` | src/map/skills/swordman/spearstab.cpp |
| 59 | `KN_SPEARBOOMERANG` / Spear Boomerang | `exact-class-methods` | `SkillSpearBoomerang` | src/map/skills/swordman/spearboomerang.cpp |
| 60 | `KN_TWOHANDQUICKEN` / Twohand Quicken | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 61 | `KN_AUTOCOUNTER` / Counter Attack | `exact-class-methods` | `SkillCounterAttack` | src/map/skills/swordman/counterattack.cpp |
| 62 | `KN_BOWLINGBASH` / Bowling Bash | `exact-class-methods` | `SkillBowlingBash` | src/map/skills/swordman/bowlingbash.cpp |
| 63 | `KN_RIDING` / Peco Peco Riding | `core-source-references` | `` | src/map/pc.cpp, src/map/status.cpp |
| 64 | `KN_CAVALIERMASTERY` / Cavalier Mastery | `core-source-references` | `` | src/map/status.cpp |
| 1001 | `KN_CHARGEATK` / Charge Attack | `exact-class-methods` | `SkillChargeAttack` | src/map/skills/swordman/chargeattack.cpp |
| 495 | `KN_ONEHAND` / Onehand Quicken | `generic-or-class-mapped` | `StatusSkillImpl` |  |

## 详细公式与效果实现

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

### Pierce (`KN_PIERCE`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-2；命中类型：Multi_Hit；段数：3；属性：Weapon；消耗/限制：SP 7；武器 1hSpear, 2hSpear。

- 覆盖：`exact-class-methods`
- 实现类：`SkillPierce`
- 实现文件：`src/map/skills/swordman/pierce.cpp`

#### `SkillPierce::SkillPierce`

来源：`src/map/skills/swordman/pierce.cpp:8-9`

```cpp
SkillPierce::SkillPierce() : WeaponSkillImpl(KN_PIERCE) {
}
```

#### `SkillPierce::modifyDamageData`

来源：`src/map/skills/swordman/pierce.cpp:11-15`

```cpp
void SkillPierce::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const status_data* tstatus = status_get_status_data(target);

	dmg.div_= (dmg.div_> 0 ? tstatus->size+1 : -(tstatus->size+1));
}
```

#### `SkillPierce::calculateSkillRatio`

来源：`src/map/skills/swordman/pierce.cpp:17-24`

```cpp
void SkillPierce::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	const status_change* sc = status_get_sc(src);

	base_skillratio += 10 * skill_lv;

	if (sc && sc->getSCE(SC_CHARGINGPIERCE_COUNT) && sc->getSCE(SC_CHARGINGPIERCE_COUNT)->val1 >= 10)
		base_skillratio *= 2;
}
```

#### `SkillPierce::modifyHitRate`

来源：`src/map/skills/swordman/pierce.cpp:26-28`

```cpp
void SkillPierce::modifyHitRate(int16& hit_rate, const block_list* src, const block_list* target, uint16 skill_lv) const {
	hit_rate += hit_rate * 5 * skill_lv / 100;
}
```

### Brandish Spear (`KN_BRANDISHSPEAR`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-2；命中类型：Single；段数：1；属性：Weapon；范围：2；击退：2；吟唱：700 ms；持续时间1：1000 ms；伤害标记：NoDamage；消耗/限制：SP 12；武器 1hSpear, 2hSpear；状态 Riding。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBrandishSpear`
- 实现文件：`src/map/skills/swordman/brandishspear.cpp`

#### `SkillBrandishSpear::SkillBrandishSpear`

来源：`src/map/skills/swordman/brandishspear.cpp:11-12`

```cpp
SkillBrandishSpear::SkillBrandishSpear() : SkillImpl(KN_BRANDISHSPEAR) {
}
```

#### `SkillBrandishSpear::castendNoDamageId`

来源：`src/map/skills/swordman/brandishspear.cpp:14-45`

```cpp
void SkillBrandishSpear::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	map_foreachindir(skill_area_sub, src->m, src->x, src->y, target->x, target->y,
		skill_get_splash(getSkillId(), skill_lv), skill_get_maxcount(getSkillId(), skill_lv), 0, splash_target(src),
		src, getSkillId(), skill_lv, tick, flag | BCT_ENEMY | 0,
		skill_castend_damage_id);
#else
	map_session_data* sd = BL_CAST(BL_PC, src);

	skill_area_temp[1] = target->id;

	if(skill_lv >= 10)
		map_foreachindir(skill_area_sub, src->m, src->x, src->y, target->x, target->y,
			skill_get_splash(getSkillId(), skill_lv), 1, skill_get_maxcount(getSkillId(), skill_lv)-1, splash_target(src),
			src, getSkillId(), skill_lv, tick, flag | BCT_ENEMY | (sd?3:0),
			skill_castend_damage_id);
	if(skill_lv >= 7)
		map_foreachindir(skill_area_sub, src->m, src->x, src->y, target->x, target->y,
			skill_get_splash(getSkillId(), skill_lv), 1, skill_get_maxcount(getSkillId(), skill_lv)-2, splash_target(src),
			src, getSkillId(), skill_lv, tick, flag | BCT_ENEMY | (sd?2:0),
			skill_castend_damage_id);
	if(skill_lv >= 4)
		map_foreachindir(skill_area_sub, src->m, src->x, src->y, target->x, target->y,
			skill_get_splash(getSkillId(), skill_lv), 1, skill_get_maxcount(getSkillId(), skill_lv)-3, splash_target(src),
			src, getSkillId(), skill_lv, tick, flag | BCT_ENEMY | (sd?1:0),
			skill_castend_damage_id);
	map_foreachindir(skill_area_sub, src->m, src->x, src->y, target->x, target->y,
		skill_get_splash(getSkillId(), skill_lv), skill_get_maxcount(getSkillId(), skill_lv)-3, 0, splash_target(src),
		src, getSkillId(), skill_lv, tick, flag | BCT_ENEMY | 0,
		skill_castend_damage_id);
#endif
}
```

#### `SkillBrandishSpear::castendDamageId`

来源：`src/map/skills/swordman/brandishspear.cpp:47-57`

```cpp
void SkillBrandishSpear::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_attack(skill_get_type(getSkillId()), src, src, target, getSkillId(), skill_lv, tick, flag);
#else
	//Coded apart for it needs the flag passed to the damage calculation.
	if (skill_area_temp[1] != target->id)
		skill_attack(skill_get_type(getSkillId()), src, src, target, getSkillId(), skill_lv, tick, flag|SD_ANIMATION);
	else
		skill_attack(skill_get_type(getSkillId()), src, src, target, getSkillId(), skill_lv, tick, flag);
#endif
}
```

#### `SkillBrandishSpear::calculateSkillRatio`

来源：`src/map/skills/swordman/brandishspear.cpp:59-81`

```cpp
void SkillBrandishSpear::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const status_data* sstatus = status_get_status_data(*src);

	base_skillratio += -100 + 400 + 100 * skill_lv + sstatus->str * 3;
#else
	int32 ratio = 100 + 20 * skill_lv;

	base_skillratio += -100 + ratio;
	if (skill_lv > 3 && wd->miscflag == 0)
		base_skillratio += ratio / 2;
	if (skill_lv > 6 && wd->miscflag == 0)
		base_skillratio += ratio / 4;
	if (skill_lv > 9 && wd->miscflag == 0)
		base_skillratio += ratio / 8;
	if (skill_lv > 6 && wd->miscflag == 1)
		base_skillratio += ratio / 2;
	if (skill_lv > 9 && wd->miscflag == 1)
		base_skillratio += ratio / 4;
	if (skill_lv > 9 && wd->miscflag == 2)
		base_skillratio += ratio / 2;
#endif
}
```

### Spear Stab (`KN_SPEARSTAB`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-4；命中类型：Single；段数：1；属性：Weapon；击退：6；伤害标记：Splash；消耗/限制：SP 9；武器 1hSpear, 2hSpear。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpearStab`
- 实现文件：`src/map/skills/swordman/spearstab.cpp`

#### `SkillSpearStab::SkillSpearStab`

来源：`src/map/skills/swordman/spearstab.cpp:8-9`

```cpp
SkillSpearStab::SkillSpearStab() : SkillImpl(KN_SPEARSTAB) {
}
```

#### `SkillSpearStab::modifyDamageData`

来源：`src/map/skills/swordman/spearstab.cpp:11-13`

```cpp
void SkillSpearStab::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	dmg.blewcount = 0;
}
```

#### `SkillSpearStab::castendDamageId`

来源：`src/map/skills/swordman/spearstab.cpp:15-36`

```cpp
void SkillSpearStab::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	if(flag&1) {
		if (target->id==skill_area_temp[1])
			return;
		if (skill_attack(BF_WEAPON,src,src,target,getSkillId(), skill_lv, tick, SD_ANIMATION))
			skill_blown(src,target,skill_area_temp[2],-1,BLOWN_NONE);
	} else {
		int32 x=target->x,y=target->y,i,dir;
		dir = map_calc_dir(target,src->x,src->y);
		skill_area_temp[1] = target->id;
		skill_area_temp[2] = skill_get_blewcount(getSkillId(),skill_lv);
		// all the enemies between the caster and the target are hit, as well as the target
		if (skill_attack(BF_WEAPON,src,src,target, getSkillId(),skill_lv,tick,0))
			skill_blown(src,target,skill_area_temp[2],-1,BLOWN_NONE);
		for (i=0;i<4;i++) {
			map_foreachincell(skill_area_sub,target->m,x,y,BL_CHAR,
				src, getSkillId(),skill_lv,tick,flag|BCT_ENEMY|1,skill_castend_damage_id);
			x += dirx[dir];
			y += diry[dir];
		}
	}
}
```

#### `SkillSpearStab::calculateSkillRatio`

来源：`src/map/skills/swordman/spearstab.cpp:38-40`

```cpp
void SkillSpearStab::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += 20 * skill_lv;
}
```

### Spear Boomerang (`KN_SPEARBOOMERANG`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：Lv1=3; Lv2=5; Lv3=7; Lv4=9; Lv5=11；命中类型：Single；段数：1；属性：Weapon；技能后摇：1000 ms；消耗/限制：SP 10；武器 1hSpear, 2hSpear。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpearBoomerang`
- 实现文件：`src/map/skills/swordman/spearboomerang.cpp`

#### `SkillSpearBoomerang::SkillSpearBoomerang`

来源：`src/map/skills/swordman/spearboomerang.cpp:6-7`

```cpp
SkillSpearBoomerang::SkillSpearBoomerang() : WeaponSkillImpl(KN_SPEARBOOMERANG) {
}
```

#### `SkillSpearBoomerang::calculateSkillRatio`

来源：`src/map/skills/swordman/spearboomerang.cpp:9-11`

```cpp
void SkillSpearBoomerang::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += 50 * skill_lv;
}
```

### Twohand Quicken (`KN_TWOHANDQUICKEN`)

武器/物理技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000; Lv6=180000; Lv7=210000; Lv8=240000; Lv9=270000; Lv10-11=300000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=14; Lv2=18; Lv3=22; Lv4=26; Lv5=30; Lv6=34; Lv7=38; Lv8=42; Lv9=46; Lv10=50；武器 2hSword；关联状态：TwoHandQuicken。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Counter Attack (`KN_AUTOCOUNTER`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；属性：Weapon；持续时间1：Lv1=400; Lv2=800; Lv3=1200; Lv4=1600; Lv5=2000 ms；伤害标记：IgnoreDefense, Critical；消耗/限制：SP 3；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma；关联状态：AutoCounter。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCounterAttack`
- 实现文件：`src/map/skills/swordman/counterattack.cpp`

#### `SkillCounterAttack::SkillCounterAttack`

来源：`src/map/skills/swordman/counterattack.cpp:8-9`

```cpp
SkillCounterAttack::SkillCounterAttack() : SkillImpl(KN_AUTOCOUNTER) {
}
```

#### `SkillCounterAttack::modifyDamageData`

来源：`src/map/skills/swordman/counterattack.cpp:11-13`

```cpp
void SkillCounterAttack::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	dmg.flag = (dmg.flag&~BF_SKILLMASK)|BF_NORMAL;
}
```

#### `SkillCounterAttack::castendNoDamageId`

来源：`src/map/skills/swordman/counterattack.cpp:15-18`

```cpp
void SkillCounterAttack::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_start(src, target, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
	skill_addtimerskill(src, tick + 100, target->id, 0, 0, getSkillId(), skill_lv, BF_WEAPON, flag);
}
```

#### `SkillCounterAttack::modifyHitRate`

来源：`src/map/skills/swordman/counterattack.cpp:20-22`

```cpp
void SkillCounterAttack::modifyHitRate(int16& hit_rate, const block_list* src, const block_list* target, uint16 skill_lv) const {
	hit_rate += hit_rate * 20 / 100;
}
```

### Bowling Bash (`KN_BOWLINGBASH`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-2；命中类型：Single；段数：1；属性：Weapon；范围：1；击退：1；吟唱：700 ms；伤害标记：Splash；消耗/限制：SP Lv1=13; Lv2=14; Lv3=15; Lv4=16; Lv5=17; Lv6=18; Lv7=19; Lv8=20; Lv9=21; Lv10=22。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBowlingBash`
- 实现文件：`src/map/skills/swordman/bowlingbash.cpp`

#### `SkillBowlingBash::SkillBowlingBash`

来源：`src/map/skills/swordman/bowlingbash.cpp:13-14`

```cpp
SkillBowlingBash::SkillBowlingBash() : SkillImpl(KN_BOWLINGBASH) {
}
```

#### `SkillBowlingBash::modifyDamageData`

来源：`src/map/skills/swordman/bowlingbash.cpp:16-29`

```cpp
void SkillBowlingBash::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
#ifdef RENEWAL
	const map_session_data* sd = BL_CAST(BL_PC, &src);

	if (sd != nullptr && sd->status.weapon == W_2HSWORD) {
		if (dmg.miscflag >= 4)
			dmg.div_ = 4;
		else if (dmg.miscflag >= 2)
			dmg.div_ = 3;
	}
#else
	dmg.blewcount = 0;
#endif
}
```

#### `SkillBowlingBash::calculateSkillRatio`

来源：`src/map/skills/swordman/bowlingbash.cpp:31-33`

```cpp
void SkillBowlingBash::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += 40 * skill_lv;
}
```

#### `SkillBowlingBash::castendDamageId`

来源：`src/map/skills/swordman/bowlingbash.cpp:35-116`

```cpp
void SkillBowlingBash::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	if (flag & 1) {
		skill_attack(skill_get_type(getSkillId()), src, src, target, getSkillId(), skill_lv, tick, (skill_area_temp[0]) > 0 ? SD_ANIMATION | skill_area_temp[0] : skill_area_temp[0]);
	} else {
		skill_area_temp[0] = map_foreachinallrange(skill_area_sub, target, skill_get_splash(getSkillId(), skill_lv), BL_CHAR, src, getSkillId(), skill_lv, tick, BCT_ENEMY, skill_area_sub_count);
		map_foreachinrange(skill_area_sub, target, skill_get_splash(getSkillId(), skill_lv), BL_CHAR|BL_SKILL, src, getSkillId(), skill_lv, tick, flag | BCT_ENEMY | SD_SPLASH | 1, skill_castend_damage_id);
	}
#else
	int32 min_x,max_x,min_y,max_y,i,c,dir,tx,ty;
	// Chain effect and check range gets reduction by recursive depth, as this can reach 0, we don't use blowcount
	c = (skill_lv-(flag&0xFFF)+1)/2;
	// Determine the Bowling Bash area depending on configuration
	if (battle_config.bowling_bash_area == 0) {
		// Gutter line system
		min_x = ((src->x)-c) - ((src->x)-c)%40;
		if(min_x < 0) min_x = 0;
		max_x = min_x + 39;
		min_y = ((src->y)-c) - ((src->y)-c)%40;
		if(min_y < 0) min_y = 0;
		max_y = min_y + 39;
	} else if (battle_config.bowling_bash_area == 1) {
		// Gutter line system without demi gutter bug
		min_x = src->x - (src->x)%40;
		max_x = min_x + 39;
		min_y = src->y - (src->y)%40;
		max_y = min_y + 39;
	} else {
		// Area around caster
		min_x = src->x - battle_config.bowling_bash_area;
		max_x = src->x + battle_config.bowling_bash_area;
		min_y = src->y - battle_config.bowling_bash_area;
		max_y = src->y + battle_config.bowling_bash_area;
	}
	// Initialization, break checks, direction
	if((flag&0xFFF) > 0) {
		// Ignore monsters outside area
		if(target->x < min_x || target->x > max_x || target->y < min_y || target->y > max_y)
			return;
		// Ignore monsters already in list
		if(idb_exists(bowling_db, target->id))
			return;
		// Random direction
		dir = rnd()%8;
	} else {
		// Create an empty list of already hit targets
		db_clear(bowling_db);
		// Direction is walkpath
		dir = (unit_getdir(src)+4)%8;
	}
	// Add current target to the list of already hit targets
	idb_put(bowling_db, target->id, target);
	// Keep moving target in direction square by square
	tx = target->x;
	ty = target->y;
	for(i=0;i<c;i++) {
		// Target coordinates (get changed even if knockback fails)
		tx -= dirx[dir];
		ty -= diry[dir];
		// If target cell is a wall then break
		if(map_getcell(target->m,tx,ty,CELL_CHKWALL))
			break;
		skill_blown(src,target,1,dir,BLOWN_NONE);

		int32 count;

		// Splash around target cell, but only cells inside area; we first have to check the area is not negative
		if((max(min_x,tx-1) <= min(max_x,tx+1)) &&
			(max(min_y,ty-1) <= min(max_y,ty+1)) &&
			(count = map_foreachinallarea(skill_area_sub, target->m, max(min_x,tx-1), max(min_y,ty-1), min(max_x,tx+1), min(max_y,ty+1), splash_target(src), src, getSkillId(), skill_lv, tick, flag|BCT_ENEMY, skill_area_sub_count))) {
			// Recursive call
			map_foreachinallarea(skill_area_sub, target->m, max(min_x,tx-1), max(min_y,ty-1), min(max_x,tx+1), min(max_y,ty+1), splash_target(src), src, getSkillId(), skill_lv, tick, (flag|BCT_ENEMY)+1, skill_castend_damage_id);
			// Self-collision
			if(target->x >= min_x && target->x <= max_x && target->y >= min_y && target->y <= max_y)
				skill_attack(BF_WEAPON,src,src,target,getSkillId(),skill_lv,tick,(flag&0xFFF)>0?SD_ANIMATION|count:count);
			break;
		}
	}
	// Original hit or chain hit depending on flag
	skill_attack(BF_WEAPON,src,src,target,getSkillId(),skill_lv,tick,(flag&0xFFF)>0?SD_ANIMATION:0);
#endif
}
```

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

### Charge Attack (`KN_CHARGEATK`)

武器/物理技能；目标：敌方目标；最高等级 1；射程：14；命中类型：Single；段数：1；属性：Weapon；吟唱：500 ms；消耗/限制：SP 40。

- 覆盖：`exact-class-methods`
- 实现类：`SkillChargeAttack`
- 实现文件：`src/map/skills/swordman/chargeattack.cpp`

#### `SkillChargeAttack::SkillChargeAttack`

来源：`src/map/skills/swordman/chargeattack.cpp:13-14`

```cpp
SkillChargeAttack::SkillChargeAttack() : SkillImpl(KN_CHARGEATK) {
}
```

#### `SkillChargeAttack::castendDamageId`

来源：`src/map/skills/swordman/chargeattack.cpp:16-40`

```cpp
void SkillChargeAttack::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	bool path = path_search_long(nullptr, src->m, src->x, src->y, target->x, target->y,CELL_CHKWALL);
#ifdef RENEWAL
	int32 dist = skill_get_blewcount(getSkillId(), skill_lv);
#else
	// Charge attack in pre-renewal calculates the distance mathetically
	int32 dist = static_cast<int32>(distance_math_bl(src, target));
#endif
	uint8 dir = map_calc_dir(target, src->x, src->y);

	// teleport to target (if not on WoE grounds)
	if (skill_check_unit_movepos(5, src, target->x + dirx[dir], target->y + diry[dir], 0, true))
		clif_blown(src);

	// cause damage and knockback if the path to target was a straight one
	if (path) {
		if(skill_attack(BF_WEAPON, src, src, target, getSkillId(), skill_lv, tick, dist)) {
#ifdef RENEWAL
			if (map_getmapdata(src->m)->getMapFlag(MF_PVP))
				dist += 2; // Knockback is 4 on PvP maps
#endif
			skill_blown(src, target, dist, dir, BLOWN_NONE);
		}
	}
}
```

#### `SkillChargeAttack::calculateSkillRatio`

来源：`src/map/skills/swordman/chargeattack.cpp:42-54`

```cpp
void SkillChargeAttack::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 600;
#else
	// +100% every 3 cells of distance but hard-limited to 500%
	int32 k = (wd->miscflag - 1) / 3;
	if (k < 0)
		k = 0;
	else if (k > 4)
		k = 4;
	base_skillratio += 100 * k;
#endif
}
```

### Onehand Quicken (`KN_ONEHAND`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：300000 ms；伤害标记：NoDamage；消耗/限制：SP 100；武器 1hSword；关联状态：OneHand。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。
