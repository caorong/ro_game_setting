# Wizard 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 80 | `WZ_FIREPILLAR` / Fire Pillar | `exact-class-methods` | `SkillFirePillar` | src/map/skills/mage/firepillar.cpp |
| 81 | `WZ_SIGHTRASHER` / Sightrasher | `exact-class-methods` | `SkillSightRasher` | src/map/skills/mage/sightrasher.cpp |
| 83 | `WZ_METEOR` / Meteor Storm | `exact-class-methods` | `SkillMeteorStorm` | src/map/skills/mage/meteorstorm.cpp |
| 84 | `WZ_JUPITEL` / Jupitel Thunder | `exact-class-methods` | `SkillJupitelThunder` | src/map/skills/mage/jupitelthunder.cpp |
| 85 | `WZ_VERMILION` / Lord of Vermilion | `exact-class-methods` | `SkillLordOfVermilion` | src/map/skills/mage/lordofvermilion.cpp |
| 86 | `WZ_WATERBALL` / Water Ball | `exact-class-methods` | `SkillWaterBall` | src/map/skills/mage/waterball.cpp |
| 87 | `WZ_ICEWALL` / Ice Wall | `exact-class-methods` | `SkillIceWall` | src/map/skills/mage/icewall.cpp |
| 88 | `WZ_FROSTNOVA` / Frost Nova | `exact-class-methods` | `SkillFrostNova` | src/map/skills/mage/frostnova.cpp |
| 89 | `WZ_STORMGUST` / Storm Gust | `exact-class-methods` | `SkillStormGust` | src/map/skills/mage/stormgust.cpp |
| 90 | `WZ_EARTHSPIKE` / Earth Spike | `exact-class-methods` | `SkillEarthSpike` | src/map/skills/mage/earthspike.cpp |
| 91 | `WZ_HEAVENDRIVE` / Heaven's Drive | `exact-class-methods` | `SkillHeavensDrive` | src/map/skills/mage/heavensdrive.cpp |
| 92 | `WZ_QUAGMIRE` / Quagmire | `exact-class-methods` | `SkillQuagmire` | src/map/skills/mage/quagmire.cpp |
| 93 | `WZ_ESTIMATION` / Sense | `exact-class-methods` | `SkillSense` | src/map/skills/mage/sense.cpp |
| 1006 | `WZ_SIGHTBLASTER` / Sight Blaster | `exact-class-methods` | `SkillSightBlaster` | src/map/skills/mage/sightblaster.cpp |

## 详细公式与效果实现

### Fire Pillar (`WZ_FIREPILLAR`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=3; Lv2=4; Lv3=5; Lv4=6; Lv5=7; Lv6=8; Lv7=9; Lv8=10; Lv9=11; Lv10=12；属性：Fire；范围：Lv1-5=1; Lv6-11=2；吟唱：Lv1=3000; Lv2=2700; Lv3=2400; Lv4=2100; Lv5=1800; Lv6=1500; Lv7=1200; Lv8=900; Lv9=600; Lv10=300 ms；技能后摇：1000 ms；持续时间1：30000 ms；持续时间2：Lv1=600; Lv2=800; Lv3=1000; Lv4=1200; Lv5=1400; Lv6=1600; Lv7=1800; Lv8=2000; Lv9=2200; Lv10=2400 ms；伤害标记：IgnoreDefense；消耗/限制：SP 75；道具 Blue_Gemstone×1@Lv6, Blue_Gemstone×1@Lv7, Blue_Gemstone×1@Lv8, Blue_Gemstone×1@Lv9, Blue_Gemstone×1@Lv10。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFirePillar`
- 实现文件：`src/map/skills/mage/firepillar.cpp`

#### `SkillFirePillar::SkillFirePillar`

来源：`src/map/skills/mage/firepillar.cpp:9-10`

```cpp
SkillFirePillar::SkillFirePillar() : SkillImpl(WZ_FIREPILLAR) {
}
```

#### `SkillFirePillar::castendPos2`

来源：`src/map/skills/mage/firepillar.cpp:12-17`

```cpp
void SkillFirePillar::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillFirePillar::calculateSkillRatio`

来源：`src/map/skills/mage/firepillar.cpp:19-21`

```cpp
void SkillFirePillar::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += -60 + 20 * skill_lv; //20% MATK each hit
}
```

#### `SkillFirePillar::applyAdditionalEffects`

来源：`src/map/skills/mage/firepillar.cpp:23-25`

```cpp
void SkillFirePillar::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	unit_set_walkdelay(target, tick, skill_get_time2(getSkillId(), skill_lv), 1);
}
```

#### `SkillFirePillar::modifyDamageData`

来源：`src/map/skills/mage/firepillar.cpp:27-32`

```cpp
void SkillFirePillar::modifyDamageData(Damage& dmg, const block_list& src, const block_list& target, uint16 skill_lv) const {
	const map_session_data* sd = BL_CAST(BL_PC, &src);

	if (sd != nullptr && dmg.div_ > 0)
		dmg.div_ *= -1; // For players, damage is divided by number of hits
}
```

### Sightrasher (`WZ_SIGHTRASHER`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；属性：Fire；范围：7；击退：5；吟唱：500 ms；技能后摇：2000 ms；持续时间1：500 ms；伤害标记：Splash；消耗/限制：SP Lv1=35; Lv2=37; Lv3=39; Lv4=41; Lv5=43; Lv6=45; Lv7=47; Lv8=49; Lv9=51; Lv10=53；前置状态 Sight。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSightRasher`
- 实现文件：`src/map/skills/mage/sightrasher.cpp`

#### `SkillSightRasher::SkillSightRasher`

来源：`src/map/skills/mage/sightrasher.cpp:9-10`

```cpp
SkillSightRasher::SkillSightRasher() : SkillImpl(WZ_SIGHTRASHER) {
}
```

#### `SkillSightRasher::castendNoDamageId`

来源：`src/map/skills/mage/sightrasher.cpp:12-20`

```cpp
void SkillSightRasher::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Passive side of the attack.
	status_change_end(src, SC_SIGHT);
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
	map_foreachinshootrange(skill_area_sub,src,
		skill_get_splash(getSkillId(), skill_lv),BL_CHAR|BL_SKILL,
		src,getSkillId(),skill_lv,tick, flag|BCT_ENEMY|SD_ANIMATION|1,
		skill_castend_damage_id);
}
```

#### `SkillSightRasher::castendDamageId`

来源：`src/map/skills/mage/sightrasher.cpp:22-24`

```cpp
void SkillSightRasher::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_attack(BF_MAGIC,src,src,target,getSkillId(),skill_lv,tick,flag);
}
```

#### `SkillSightRasher::calculateSkillRatio`

来源：`src/map/skills/mage/sightrasher.cpp:26-28`

```cpp
void SkillSightRasher::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += 20 * skill_lv;
}
```

### Meteor Storm (`WZ_METEOR`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1-2=1; Lv3-4=2; Lv5-6=3; Lv7-8=4; Lv9-10=5; Lv11=15；属性：Fire；范围：Lv1-10=3; Lv11=16；吟唱：15000 ms；技能后摇：Lv1=2000; Lv2-3=3000; Lv4-5=4000; Lv6-7=5000; Lv8-9=6000; Lv10=7000 ms；持续时间1：Lv1=2000; Lv2-3=3000; Lv4-5=4000; Lv6-7=5000; Lv8-9=6000; Lv10=7000; Lv11=10000 ms；持续时间2：5000 ms；消耗/限制：SP Lv1=20; Lv2=24; Lv3=30; Lv4=34; Lv5=40; Lv6=44; Lv7=50; Lv8=54; Lv9=60; Lv10=64；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMeteorStorm`
- 实现文件：`src/map/skills/mage/meteorstorm.cpp`

#### `SkillMeteorStorm::SkillMeteorStorm`

来源：`src/map/skills/mage/meteorstorm.cpp:10-11`

```cpp
SkillMeteorStorm::SkillMeteorStorm() : SkillImpl(WZ_METEOR) {
}
```

#### `SkillMeteorStorm::castendPos2`

来源：`src/map/skills/mage/meteorstorm.cpp:13-23`

```cpp
void SkillMeteorStorm::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	int32 area = skill_get_splash(getSkillId(), skill_lv);
	int16 tmpx = 0, tmpy = 0;

	for (int32 i = 1; i <= skill_get_time(getSkillId(), skill_lv) / skill_get_unit_interval(getSkillId()); i++) {
		// Creates a random Cell in the Splash Area
		tmpx = x - area + rnd() % (area * 2 + 1);
		tmpy = y - area + rnd() % (area * 2 + 1);
		skill_unitsetting(src, getSkillId(), skill_lv, tmpx, tmpy, flag + i * skill_get_unit_interval(getSkillId()));
	}
}
```

#### `SkillMeteorStorm::calculateSkillRatio`

来源：`src/map/skills/mage/meteorstorm.cpp:25-29`

```cpp
void SkillMeteorStorm::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 25;
#endif
}
```

#### `SkillMeteorStorm::applyAdditionalEffects`

来源：`src/map/skills/mage/meteorstorm.cpp:31-33`

```cpp
void SkillMeteorStorm::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src,target,SC_STUN,3*skill_lv,skill_lv,skill_get_time2(getSkillId(),skill_lv));
}
```

### Jupitel Thunder (`WZ_JUPITEL`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=3; Lv2=4; Lv3=5; Lv4=6; Lv5=7; Lv6=8; Lv7=9; Lv8=10; Lv9=11; Lv10=12；属性：Wind；击退：Lv1=2; Lv2-3=3; Lv4-5=4; Lv6-7=5; Lv8-9=6; Lv10=7；吟唱：Lv1=2500; Lv2=3000; Lv3=3500; Lv4=4000; Lv5=4500; Lv6=5000; Lv7=5500; Lv8=6000; Lv9=6500; Lv10=7000 ms；消耗/限制：SP Lv1=20; Lv2=23; Lv3=26; Lv4=29; Lv5=32; Lv6=35; Lv7=38; Lv8=41; Lv9=44; Lv10=47。

- 覆盖：`exact-class-methods`
- 实现类：`SkillJupitelThunder`
- 实现文件：`src/map/skills/mage/jupitelthunder.cpp`

#### `SkillJupitelThunder::SkillJupitelThunder`

来源：`src/map/skills/mage/jupitelthunder.cpp:6-7`

```cpp
SkillJupitelThunder::SkillJupitelThunder() : SkillImpl(WZ_JUPITEL) {
}
```

#### `SkillJupitelThunder::castendDamageId`

来源：`src/map/skills/mage/jupitelthunder.cpp:9-12`

```cpp
void SkillJupitelThunder::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Jupitel Thunder is delayed by 150ms, you can cast another spell before the knockback
	skill_addtimerskill(src, tick + TIMERSKILL_INTERVAL, target->id, 0, 0, getSkillId(), skill_lv, 1, flag);
}
```

### Lord of Vermilion (`WZ_VERMILION`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：-10；属性：Wind；吟唱：Lv1=15000; Lv2=14500; Lv3=14000; Lv4=13500; Lv5=13000; Lv6=12500; Lv7=12000; Lv8=11500; Lv9=11000; Lv10=10500 ms；技能后摇：5000 ms；持续时间1：4000 ms；持续时间2：30000 ms；消耗/限制：SP Lv1=60; Lv2=64; Lv3=68; Lv4=72; Lv5=76; Lv6=80; Lv7=84; Lv8=88; Lv9=92; Lv10=96；关联状态：Blind。

- 覆盖：`exact-class-methods`
- 实现类：`SkillLordOfVermilion`
- 实现文件：`src/map/skills/mage/lordofvermilion.cpp`

#### `SkillLordOfVermilion::SkillLordOfVermilion`

来源：`src/map/skills/mage/lordofvermilion.cpp:11-12`

```cpp
SkillLordOfVermilion::SkillLordOfVermilion() : SkillImpl(WZ_VERMILION) {
}
```

#### `SkillLordOfVermilion::castendPos2`

来源：`src/map/skills/mage/lordofvermilion.cpp:14-19`

```cpp
void SkillLordOfVermilion::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src, getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillLordOfVermilion::calculateSkillRatio`

来源：`src/map/skills/mage/lordofvermilion.cpp:21-32`

```cpp
void SkillLordOfVermilion::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const map_session_data* sd = BL_CAST(BL_PC, src);

	if(sd)
		base_skillratio += 300 + skill_lv * 100;
	else
		base_skillratio += 20 * skill_lv - 20; //Monsters use old formula
#else
	base_skillratio += 20 * skill_lv - 20;
#endif
}
```

#### `SkillLordOfVermilion::applyAdditionalEffects`

来源：`src/map/skills/mage/lordofvermilion.cpp:34-40`

```cpp
void SkillLordOfVermilion::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
#ifdef RENEWAL
	sc_start(src,target,SC_BLIND,10 + 5 * skill_lv,skill_lv,skill_get_time2(getSkillId(),skill_lv));
#else
	sc_start(src,target,SC_BLIND,min(4*skill_lv,40),skill_lv,skill_get_time2(getSkillId(),skill_lv));
#endif
}
```

### Water Ball (`WZ_WATERBALL`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：1；属性：Water；吟唱：Lv1=1000; Lv2=2000; Lv3=3000; Lv4=4000; Lv5=5000; Lv6=6000; Lv7=7000; Lv8=8000; Lv9=9000; Lv10=10000 ms；持续时间1：10000 ms；消耗/限制：SP Lv1=15; Lv2-3=20; Lv4-10=25；状态 Water。

- 覆盖：`exact-class-methods`
- 实现类：`SkillWaterBall`
- 实现文件：`src/map/skills/mage/waterball.cpp`

#### `SkillWaterBall::SkillWaterBall`

来源：`src/map/skills/mage/waterball.cpp:6-7`

```cpp
SkillWaterBall::SkillWaterBall() : SkillImpl(WZ_WATERBALL) {
}
```

#### `SkillWaterBall::castendDamageId`

来源：`src/map/skills/mage/waterball.cpp:9-13`

```cpp
void SkillWaterBall::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Deploy waterball cells, these are used and turned into waterballs via the timerskill
	skill_unitsetting(src, getSkillId(), skill_lv, src->x, src->y, 0);
	skill_addtimerskill(src, tick, target->id, src->x, src->y, getSkillId(), skill_lv, 0, flag);
}
```

#### `SkillWaterBall::calculateSkillRatio`

来源：`src/map/skills/mage/waterball.cpp:15-17`

```cpp
void SkillWaterBall::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	base_skillratio += 30 * skill_lv;
}
```

### Ice Wall (`WZ_ICEWALL`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Water；伤害标记：NoDamage；消耗/限制：SP 20。

- 覆盖：`exact-class-methods`
- 实现类：`SkillIceWall`
- 实现文件：`src/map/skills/mage/icewall.cpp`

#### `SkillIceWall::SkillIceWall`

来源：`src/map/skills/mage/icewall.cpp:8-9`

```cpp
SkillIceWall::SkillIceWall() : SkillImpl(WZ_ICEWALL) {
}
```

#### `SkillIceWall::castendPos2`

来源：`src/map/skills/mage/icewall.cpp:11-15`

```cpp
void SkillIceWall::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag|=1;
	if(skill_unitsetting(src,getSkillId(),skill_lv,x,y,0))
		clif_skill_poseffect( *src, getSkillId(), skill_lv, x, y, tick );
}
```

### Frost Nova (`WZ_FROSTNOVA`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；属性：Water；范围：2；吟唱：Lv1-2=6000; Lv3-4=5500; Lv5-6=5000; Lv7-8=4500; Lv9-10=4000 ms；技能后摇：1000 ms；持续时间2：Lv1=1500; Lv2=3000; Lv3=4500; Lv4=6000; Lv5=7500; Lv6=9000; Lv7=10500; Lv8=12000; Lv9=13500; Lv10=15000 ms；伤害标记：Splash；消耗/限制：SP Lv1=45; Lv2=43; Lv3=41; Lv4=39; Lv5=37; Lv6=35; Lv7=33; Lv8=31; Lv9=29; Lv10=27；关联状态：Freeze。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFrostNova`
- 实现文件：`src/map/skills/mage/frostnova.cpp`

#### `SkillFrostNova::SkillFrostNova`

来源：`src/map/skills/mage/frostnova.cpp:12-13`

```cpp
SkillFrostNova::SkillFrostNova() : SkillImpl(WZ_FROSTNOVA) {
}
```

#### `SkillFrostNova::castendNoDamageId`

来源：`src/map/skills/mage/frostnova.cpp:15-21`

```cpp
void SkillFrostNova::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
	skill_area_temp[1] = 0;
	map_foreachinshootrange(skill_attack_area, src,
		skill_get_splash(getSkillId(), skill_lv), splash_target(src),
		BF_MAGIC, src, src, getSkillId(), skill_lv, tick, flag, BCT_ENEMY);
}
```

#### `SkillFrostNova::calculateSkillRatio`

来源：`src/map/skills/mage/frostnova.cpp:23-30`

```cpp
void SkillFrostNova::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	// In renewal the damage formula is identical to MG_FROSTDIVER
	base_skillratio += 10 * skill_lv;
#else
	base_skillratio += -100 + (100 + skill_lv * 10) * 2 / 3;
#endif
}
```

#### `SkillFrostNova::applyAdditionalEffects`

来源：`src/map/skills/mage/frostnova.cpp:32-36`

```cpp
void SkillFrostNova::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	sc_start(src,target,SC_FREEZE,(sd!=nullptr)?skill_lv*5+33:skill_lv*3+35,skill_lv,skill_get_time2(getSkillId(), skill_lv));
}
```

### Storm Gust (`WZ_STORMGUST`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Water；击退：2；吟唱：Lv1=6000; Lv2=7000; Lv3=8000; Lv4=9000; Lv5=10000; Lv6=11000; Lv7=12000; Lv8=13000; Lv9=14000; Lv10=15000 ms；技能后摇：5000 ms；持续时间1：4600 ms；持续时间2：12000 ms；消耗/限制：SP 78；关联状态：Freeze。

- 覆盖：`exact-class-methods`
- 实现类：`SkillStormGust`
- 实现文件：`src/map/skills/mage/stormgust.cpp`

#### `SkillStormGust::SkillStormGust`

来源：`src/map/skills/mage/stormgust.cpp:10-11`

```cpp
SkillStormGust::SkillStormGust() : SkillImpl(WZ_STORMGUST) {
}
```

#### `SkillStormGust::castendPos2`

来源：`src/map/skills/mage/stormgust.cpp:13-18`

```cpp
void SkillStormGust::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillStormGust::calculateSkillRatio`

来源：`src/map/skills/mage/stormgust.cpp:20-27`

```cpp
void SkillStormGust::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio -= 30; // Offset only once
	base_skillratio += 50 * skill_lv;
#else
	base_skillratio += 40 * skill_lv;
#endif
}
```

#### `SkillStormGust::applyAdditionalEffects`

来源：`src/map/skills/mage/stormgust.cpp:29-46`

```cpp
void SkillStormGust::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	// Storm Gust counter was dropped in renewal
#ifdef RENEWAL
	sc_start(src,target,SC_FREEZE,65-(5*skill_lv),skill_lv,skill_get_time2(getSkillId(),skill_lv));
#else
	status_change* tsc = status_get_sc( target );

	if (tsc != nullptr) {
		//On third hit, there is a 150% to freeze the target
		if(tsc->sg_counter >= 3 &&
			sc_start(src,target,SC_FREEZE,150,skill_lv,skill_get_time2(getSkillId(),skill_lv)))
			tsc->sg_counter = 0;
		// Being it only resets on success it'd keep stacking and eventually overflowing on mvps, so we reset at a high value
		else if( tsc->sg_counter > 250 )
			tsc->sg_counter = 0;
	}
#endif
}
```

### Earth Spike (`WZ_EARTHSPIKE`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；属性：Earth；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500 ms；技能后摇：Lv1=1000; Lv2=1200; Lv3=1400; Lv4=1600; Lv5=1800 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEarthSpike`
- 实现文件：`src/map/skills/mage/earthspike.cpp`

#### `SkillEarthSpike::SkillEarthSpike`

来源：`src/map/skills/mage/earthspike.cpp:10-11`

```cpp
SkillEarthSpike::SkillEarthSpike() : SkillImpl(WZ_EARTHSPIKE) {
}
```

#### `SkillEarthSpike::castendDamageId`

来源：`src/map/skills/mage/earthspike.cpp:13-15`

```cpp
void SkillEarthSpike::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_attack(BF_MAGIC,src,src,target,getSkillId(),skill_lv,tick,flag);
}
```

#### `SkillEarthSpike::calculateSkillRatio`

来源：`src/map/skills/mage/earthspike.cpp:17-25`

```cpp
void SkillEarthSpike::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const status_change* sc = status_get_sc(src);

	base_skillratio += 100;
	if (sc && sc->getSCE(SC_EARTH_CARE_OPTION))
		base_skillratio += base_skillratio * 800 / 100;
#endif
}
```

### Heaven's Drive (`WZ_HEAVENDRIVE`)

魔法技能；目标：地面区域；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5；属性：Earth；吟唱：Lv1=1000; Lv2=2000; Lv3=3000; Lv4=4000; Lv5=5000 ms；技能后摇：1000 ms；持续时间1：100 ms；消耗/限制：SP Lv1=28; Lv2=32; Lv3=36; Lv4=40; Lv5=44。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHeavensDrive`
- 实现文件：`src/map/skills/mage/heavensdrive.cpp`

#### `SkillHeavensDrive::SkillHeavensDrive`

来源：`src/map/skills/mage/heavensdrive.cpp:10-11`

```cpp
SkillHeavensDrive::SkillHeavensDrive() : SkillImpl(WZ_HEAVENDRIVE) {
}
```

#### `SkillHeavensDrive::castendPos2`

来源：`src/map/skills/mage/heavensdrive.cpp:13-18`

```cpp
void SkillHeavensDrive::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag|=1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

#### `SkillHeavensDrive::calculateSkillRatio`

来源：`src/map/skills/mage/heavensdrive.cpp:20-24`

```cpp
void SkillHeavensDrive::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 25;
#endif
}
```

#### `SkillHeavensDrive::applyAdditionalEffects`

来源：`src/map/skills/mage/heavensdrive.cpp:26-28`

```cpp
void SkillHeavensDrive::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	status_change_end(target, SC_SV_ROOTTWIST);
}
```

### Quagmire (`WZ_QUAGMIRE`)

魔法技能；目标：地面区域；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Earth；技能后摇：1000 ms；持续时间1：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000 ms；持续时间2：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=5; Lv2=10; Lv3=15; Lv4=20; Lv5=25；关联状态：Quagmire。

- 覆盖：`exact-class-methods`
- 实现类：`SkillQuagmire`
- 实现文件：`src/map/skills/mage/quagmire.cpp`

#### `SkillQuagmire::SkillQuagmire`

来源：`src/map/skills/mage/quagmire.cpp:6-7`

```cpp
SkillQuagmire::SkillQuagmire() : SkillImpl(WZ_QUAGMIRE) {
}
```

#### `SkillQuagmire::castendPos2`

来源：`src/map/skills/mage/quagmire.cpp:9-14`

```cpp
void SkillQuagmire::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag|=1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Sense (`WZ_ESTIMATION`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 10。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSense`
- 实现文件：`src/map/skills/mage/sense.cpp`

#### `SkillSense::SkillSense`

来源：`src/map/skills/mage/sense.cpp:10-11`

```cpp
SkillSense::SkillSense() : SkillImpl(WZ_ESTIMATION) {
}
```

#### `SkillSense::castendNoDamageId`

来源：`src/map/skills/mage/sense.cpp:13-30`

```cpp
void SkillSense::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);
	mob_data* dstmd = BL_CAST(BL_MOB, target);

	if( sd == nullptr )
		return;
	if( dstsd )
	{ // Fail on Players
		clif_skill_fail( *sd, getSkillId() );
		return;
	}

	if (dstmd != nullptr)
		clif_skill_estimation( *sd, *dstmd );

	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
}
```

### Sight Blaster (`WZ_SIGHTBLASTER`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；段数：1；属性：Fire；范围：1；击退：3；吟唱：2000 ms；持续时间1：120000 ms；消耗/限制：SP 40；关联状态：SightBlaster。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSightBlaster`
- 实现文件：`src/map/skills/mage/sightblaster.cpp`

#### `SkillSightBlaster::SkillSightBlaster`

来源：`src/map/skills/mage/sightblaster.cpp:11-12`

```cpp
SkillSightBlaster::SkillSightBlaster() : SkillImpl(WZ_SIGHTBLASTER) {
}
```

#### `SkillSightBlaster::castendNoDamageId`

来源：`src/map/skills/mage/sightblaster.cpp:14-17`

```cpp
void SkillSightBlaster::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start2(src,target,skill_get_sc(getSkillId()),100,skill_lv,getSkillId(),skill_get_time(getSkillId(),skill_lv)));
}
```

#### `SkillSightBlaster::castendDamageId`

来源：`src/map/skills/mage/sightblaster.cpp:19-21`

```cpp
void SkillSightBlaster::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_attack(BF_MAGIC,src,src,target,getSkillId(),skill_lv,tick,flag);
}
```

#### `SkillSightBlaster::calculateSkillRatio`

来源：`src/map/skills/mage/sightblaster.cpp:23-27`

```cpp
void SkillSightBlaster::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 500;
#endif
}
```
