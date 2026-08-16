# Dancer 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 323 | `DC_DANCINGLESSON` / Dance Lessons | `core-source-references` | `` | src/map/battle.cpp, src/map/skill.cpp, src/map/skills/archer/hipshaker.cpp, src/map/status.cpp |
| 324 | `DC_THROWARROW` / Slinging Arrow | `exact-class-methods` | `SkillSlingingArrow` | src/map/skills/archer/slingingarrow.cpp |
| 325 | `DC_UGLYDANCE` / Hip Shaker | `exact-class-methods` | `SkillHipShaker` | src/map/skills/archer/hipshaker.cpp |
| 326 | `DC_SCREAM` / Dazzler | `exact-class-methods` | `SkillDazzler` | src/map/skills/archer/dazzler.cpp |
| 327 | `DC_HUMMING` / Focus Ballet | `exact-class-methods` | `SkillFocusBallet` | src/map/skills/archer/focusballet.cpp |
| 328 | `DC_DONTFORGETME` / Slow Grace | `exact-class-methods` | `SkillSlowGrace` | src/map/skills/archer/slowgrace.cpp |
| 329 | `DC_FORTUNEKISS` / Lady Luck | `exact-class-methods` | `SkillLadyLuck` | src/map/skills/archer/ladyluck.cpp |
| 330 | `DC_SERVICEFORYOU` / Gypsy's Kiss | `exact-class-methods` | `SkillGypsysKiss` | src/map/skills/archer/gypsyskiss.cpp |
| 304 | `BD_ADAPTATION` / Amp | `exact-class-methods` | `SkillAmp` | src/map/skills/archer/amp.cpp |
| 305 | `BD_ENCORE` / Encore | `exact-class-methods` | `SkillEncore` | src/map/skills/archer/encore.cpp |
| 306 | `BD_LULLABY` / Lullaby | `exact-class-methods` | `SkillLullaby` | src/map/skills/archer/lullaby.cpp |
| 307 | `BD_RICHMANKIM` / Mental Sensing | `exact-class-methods` | `SkillMentalSensing` | src/map/skills/archer/mentalsensing.cpp |
| 308 | `BD_ETERNALCHAOS` / Down Tempo | `exact-class-methods` | `SkillDownTempo` | src/map/skills/archer/downtempo.cpp |
| 309 | `BD_DRUMBATTLEFIELD` / Battle Theme | `exact-class-methods` | `SkillBattleTheme` | src/map/skills/archer/battletheme.cpp |
| 310 | `BD_RINGNIBELUNGEN` / Harmonic Lick | `exact-class-methods` | `SkillHarmonicLick` | src/map/skills/archer/harmoniclick.cpp |
| 311 | `BD_ROKISWEIL` / Classical Pluck | `exact-class-methods` | `SkillClassicalPluck` | src/map/skills/archer/classicalpluck.cpp |
| 312 | `BD_INTOABYSS` / Power Chord | `exact-class-methods` | `SkillPowerChord` | src/map/skills/archer/powerchord.cpp |
| 313 | `BD_SIEGFRIED` / Acoustic Rhythm | `exact-class-methods` | `SkillAcousticRhythm` | src/map/skills/archer/acousticrhythm.cpp |
| 1011 | `DC_WINKCHARM` / Wink of Charm | `exact-class-methods` | `SkillWinkofCharm` | src/map/skills/archer/winkofcharm.cpp |

## 详细公式与效果实现

### Dance Lessons (`DC_DANCINGLESSON`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/archer/hipshaker.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2375
damage += (skill * 10);
// src/map/battle.cpp:2379
damage += (skill * 3);
// src/map/battle.cpp:2383
damage += (skill * 3);
// src/map/battle.cpp:2387
damage += (skill * 3);
// src/map/battle.cpp:2391
damage += (skill * 3);
// src/map/battle.cpp:2395
damage += (skill * 3);
// src/map/skill.cpp:5911
val1 = skill_lv + status->agi / 10; // Flee increase
// src/map/skill.cpp:5912
val2 = (skill_lv + 1) / 2 + status->luk / 30; // Perfect dodge increase
// src/map/skill.cpp:5919
val1 = 1 + 2 * skill_lv + status->dex / 10; // Hit increase
// src/map/skill.cpp:5924
val1 = 3 * skill_lv + status->dex / 10; // Casting time reduction
// src/map/skill.cpp:5926
val2 = (skill_lv < 10 ? 3 * skill_lv : 50) + status->int_ / 5; // After-cast delay reduction
// src/map/skill.cpp:5934
val1 = 3 * skill_lv + status->dex / 15; // ASPD decrease
// src/map/skill.cpp:5935
val2 = 2 * skill_lv + status->agi / 20; // Movement speed adjustment.
// src/map/skill.cpp:5937
val1 = 5 + 3 * skill_lv + status->dex / 10; // ASPD decrease
// src/map/skill.cpp:5938
val2 = 5 + 3 * skill_lv + status->agi / 10; // Movement speed adjustment.
// src/map/skill.cpp:5948
val1 *= 10; //Because 10 is actually 1% aspd
```

### Slinging Arrow (`DC_THROWARROW`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Weapon；吟唱：1500 ms；消耗/限制：SP Lv1=1; Lv2=3; Lv3=5; Lv4=7; Lv5=9；弹药数 1；武器 Whip；弹药 Arrow。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSlingingArrow`
- 实现文件：`src/map/skills/archer/slingingarrow.cpp`

#### `SkillSlingingArrow::SkillSlingingArrow`

来源：`src/map/skills/archer/slingingarrow.cpp:8-9`

```cpp
SkillSlingingArrow::SkillSlingingArrow() : WeaponSkillImpl(DC_THROWARROW) {
}
```

#### `SkillSlingingArrow::calculateSkillRatio`

来源：`src/map/skills/archer/slingingarrow.cpp:11-17`

```cpp
void SkillSlingingArrow::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 10 + 40 * skill_lv;
#else
	base_skillratio += -40 + 40 * skill_lv;
#endif
}
```

### Hip Shaker (`DC_UGLYDANCE`)

特殊技能；目标：自身；最高等级 5；命中类型：Multi_Hit；段数：1；持续时间1：30000 ms；持续时间2：3000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=23; Lv2=26; Lv3=29; Lv4=32; Lv5=35；武器 Whip。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHipShaker`
- 实现文件：`src/map/skills/archer/hipshaker.cpp`

#### `SkillHipShaker::SkillHipShaker`

来源：`src/map/skills/archer/hipshaker.cpp:10-11`

```cpp
SkillHipShaker::SkillHipShaker() : SkillImpl(DC_UGLYDANCE) {
}
```

#### `SkillHipShaker::applyAdditionalEffects`

来源：`src/map/skills/archer/hipshaker.cpp:13-24`

```cpp
void SkillHipShaker::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
#ifdef RENEWAL
	// !TODO: How does caster's DEX/AGI play a role?
	status_zap( target, 0, 2 * skill_lv + 10 );
#else
	map_session_data* sd = BL_CAST( BL_PC, src );

	int32 rate = 5 + 5 * skill_lv;
	rate += skill_lv * pc_checkskill(sd, DC_DANCINGLESSON);
	status_zap( target, 0, rate );
#endif
}
```

#### `SkillHipShaker::castendNoDamageId`

来源：`src/map/skills/archer/hipshaker.cpp:26-30`

```cpp
void SkillHipShaker::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillHipShaker::castendPos2`

来源：`src/map/skills/archer/hipshaker.cpp:32-38`

```cpp
void SkillHipShaker::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	// Ammo should be deleted right away.
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Dazzler (`DC_SCREAM`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；技能后摇：4000 ms；持续时间1：5000 ms；持续时间2：5000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDazzler`
- 实现文件：`src/map/skills/archer/dazzler.cpp`

#### `SkillDazzler::SkillDazzler`

来源：`src/map/skills/archer/dazzler.cpp:11-12`

```cpp
SkillDazzler::SkillDazzler() : SkillImpl(DC_SCREAM) {
}
```

#### `SkillDazzler::applyAdditionalEffects`

来源：`src/map/skills/archer/dazzler.cpp:14-25`

```cpp
void SkillDazzler::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	int32 rate = 150 + 50 * skill_lv + 100; // Aegis accuracy (1000 = 100%). DC_SCREAM has a 10% higher base chance than BA_FROSTJOKER
	int32 duration = skill_get_time2(getSkillId(), skill_lv);
	if (battle_check_target(src, target, BCT_PARTY) > 0) {
		// TODO: check DC_SCREAM rate and duration.
		// DC_SCREAM and BA_FROSTJOKER initially shared the same code but the original comment only applies to BA_FROSTJOKER :
		// "On party members: Chance is divided by 4 and BA_FROSTJOKER duration is fixed to 15000ms"
		rate /= 4;
		duration = skill_get_time(getSkillId(), skill_lv);
	}
	status_change_start(src, target, skill_get_sc(getSkillId()), rate*10, skill_lv, 0, 0, 0, duration, SCSTART_NONE);
}
```

#### `SkillDazzler::castendNoDamageId`

来源：`src/map/skills/archer/dazzler.cpp:27-40`

```cpp
void SkillDazzler::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	mob_data* md = BL_CAST(BL_MOB, src);

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
	skill_addtimerskill(src,tick+3000,target->id,src->x,src->y,getSkillId(),skill_lv,0,flag);

	if (md) {
		// custom hack to make the mob display the skill, because these skills don't show the skill use text themselves
		//NOTE: mobs don't have the sprite animation that is used when performing this skill (will cause glitches)
		char temp[70];
		snprintf(temp, sizeof(temp), "%s : %s !!",md->name,skill_get_desc(getSkillId()));
		clif_disp_overhead(md,temp);
	}
}
```

### Focus Ballet (`DC_HUMMING`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=22; Lv2=24; Lv3=26; Lv4=28; Lv5=30; Lv6=32; Lv7=34; Lv8=36; Lv9=38; Lv10=40；武器 Musical, Whip；关联状态：Humming。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFocusBallet`
- 实现文件：`src/map/skills/archer/focusballet.cpp`

#### `SkillFocusBallet::SkillFocusBallet`

来源：`src/map/skills/archer/focusballet.cpp:8-9`

```cpp
SkillFocusBallet::SkillFocusBallet() : SkillImpl(DC_HUMMING) {
}
```

#### `SkillFocusBallet::castendNoDamageId`

来源：`src/map/skills/archer/focusballet.cpp:11-15`

```cpp
void SkillFocusBallet::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillFocusBallet::castendPos2`

来源：`src/map/skills/archer/focusballet.cpp:17-23`

```cpp
void SkillFocusBallet::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	// Ammo should be deleted right away.
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Slow Grace (`DC_DONTFORGETME`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：180000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=28; Lv2=31; Lv3=34; Lv4=37; Lv5=40; Lv6=43; Lv7=46; Lv8=49; Lv9=52; Lv10=55；武器 Musical, Whip；关联状态：DontForgetMe。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSlowGrace`
- 实现文件：`src/map/skills/archer/slowgrace.cpp`

#### `SkillSlowGrace::SkillSlowGrace`

来源：`src/map/skills/archer/slowgrace.cpp:8-9`

```cpp
SkillSlowGrace::SkillSlowGrace() : SkillImpl(DC_DONTFORGETME) {
}
```

#### `SkillSlowGrace::castendNoDamageId`

来源：`src/map/skills/archer/slowgrace.cpp:11-15`

```cpp
void SkillSlowGrace::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillSlowGrace::castendPos2`

来源：`src/map/skills/archer/slowgrace.cpp:17-23`

```cpp
void SkillSlowGrace::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	// Ammo should be deleted right away.
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Lady Luck (`DC_FORTUNEKISS`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：120000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=43; Lv2=46; Lv3=49; Lv4=52; Lv5=55; Lv6=58; Lv7=61; Lv8=64; Lv9=67; Lv10=70；武器 Musical, Whip；关联状态：Fortune。

- 覆盖：`exact-class-methods`
- 实现类：`SkillLadyLuck`
- 实现文件：`src/map/skills/archer/ladyluck.cpp`

#### `SkillLadyLuck::SkillLadyLuck`

来源：`src/map/skills/archer/ladyluck.cpp:8-9`

```cpp
SkillLadyLuck::SkillLadyLuck() : SkillImpl(DC_FORTUNEKISS) {
}
```

#### `SkillLadyLuck::castendNoDamageId`

来源：`src/map/skills/archer/ladyluck.cpp:11-15`

```cpp
void SkillLadyLuck::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillLadyLuck::castendPos2`

来源：`src/map/skills/archer/ladyluck.cpp:17-23`

```cpp
void SkillLadyLuck::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	// Ammo should be deleted right away.
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Gypsy's Kiss (`DC_SERVICEFORYOU`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：180000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=40; Lv2=45; Lv3=50; Lv4=55; Lv5=60; Lv6=65; Lv7=70; Lv8=75; Lv9=80; Lv10=85；武器 Musical, Whip；关联状态：Service4U。

- 覆盖：`exact-class-methods`
- 实现类：`SkillGypsysKiss`
- 实现文件：`src/map/skills/archer/gypsyskiss.cpp`

#### `SkillGypsysKiss::SkillGypsysKiss`

来源：`src/map/skills/archer/gypsyskiss.cpp:8-9`

```cpp
SkillGypsysKiss::SkillGypsysKiss() : SkillImpl(DC_SERVICEFORYOU) {
}
```

#### `SkillGypsysKiss::castendNoDamageId`

来源：`src/map/skills/archer/gypsyskiss.cpp:11-15`

```cpp
void SkillGypsysKiss::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillGypsysKiss::castendPos2`

来源：`src/map/skills/archer/gypsyskiss.cpp:17-23`

```cpp
void SkillGypsysKiss::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	// Ammo should be deleted right away.
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Amp (`BD_ADAPTATION`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间2：5000 ms；伤害标记：NoDamage；消耗/限制：SP 1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAmp`
- 实现文件：`src/map/skills/archer/amp.cpp`

#### `SkillAmp::SkillAmp`

来源：`src/map/skills/archer/amp.cpp:11-12`

```cpp
SkillAmp::SkillAmp() : StatusSkillImpl(BD_ADAPTATION) {
}
```

#### `SkillAmp::castendNoDamageId`

来源：`src/map/skills/archer/amp.cpp:14-25`

```cpp
void SkillAmp::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
#else
	status_change *tsc = status_get_sc(target);

	if(tsc && tsc->getSCE(SC_DANCING)){
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
		status_change_end(target, SC_DANCING);
	}
#endif
}
```

### Encore (`BD_ENCORE`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；伤害标记：NoDamage；消耗/限制：SP 1；武器 Musical, Whip；关联状态：Dancing。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEncore`
- 实现文件：`src/map/skills/archer/encore.cpp`

#### `SkillEncore::SkillEncore`

来源：`src/map/skills/archer/encore.cpp:9-10`

```cpp
SkillEncore::SkillEncore() : SkillImpl(BD_ENCORE) {
}
```

#### `SkillEncore::castendNoDamageId`

来源：`src/map/skills/archer/encore.cpp:12-19`

```cpp
void SkillEncore::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
	if (sd != nullptr) {
		unit_skilluse_id(src,src->id,sd->skill_id_dance,sd->skill_lv_dance);
	}
}
```

### Lullaby (`BD_LULLABY`)

特殊技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：30000 ms；伤害标记：NoDamage；消耗/限制：SP 20；武器 Musical, Whip；关联状态：Sleep。

- 覆盖：`exact-class-methods`
- 实现类：`SkillLullaby`
- 实现文件：`src/map/skills/archer/lullaby.cpp`

#### `SkillLullaby::SkillLullaby`

来源：`src/map/skills/archer/lullaby.cpp:10-11`

```cpp
SkillLullaby::SkillLullaby() : SkillImpl(BD_LULLABY) {
}
```

#### `SkillLullaby::applyAdditionalEffects`

来源：`src/map/skills/archer/lullaby.cpp:13-31`

```cpp
void SkillLullaby::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
#ifndef RENEWAL
	status_change *sc = status_get_sc(src);
	status_data* sstatus = status_get_status_data(*src);

	if (sc != nullptr && sc->getSCE(SC_DANCING) != nullptr) {
		block_list* partner = map_id2bl(sc->getSCE(SC_DANCING)->val4);
		if (partner == nullptr)
			return;
		status_data* pstatus = status_get_status_data(*partner);
		if (pstatus == nullptr)
			return;
		status_change_start(src, target, skill_get_sc(getSkillId()), (sstatus->int_ + pstatus->int_ + rnd_value(100, 300)) * 10, skill_lv, 0, 0, 0, skill_get_time2(getSkillId(), skill_lv), SCSTART_NONE);
	}
#else
	// In renewal the chance is simply 100% and uses the original song duration as sleep duration
	sc_start(src, target, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
#endif
}
```

#### `SkillLullaby::castendNoDamageId`

来源：`src/map/skills/archer/lullaby.cpp:33-37`

```cpp
void SkillLullaby::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillLullaby::castendPos2`

来源：`src/map/skills/archer/lullaby.cpp:39-44`

```cpp
void SkillLullaby::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Mental Sensing (`BD_RICHMANKIM`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP 20；武器 Musical, Whip；关联状态：RichManKim。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMentalSensing`
- 实现文件：`src/map/skills/archer/mentalsensing.cpp`

#### `SkillMentalSensing::SkillMentalSensing`

来源：`src/map/skills/archer/mentalsensing.cpp:8-9`

```cpp
SkillMentalSensing::SkillMentalSensing() : SkillImpl(BD_RICHMANKIM) {
}
```

#### `SkillMentalSensing::castendNoDamageId`

来源：`src/map/skills/archer/mentalsensing.cpp:11-15`

```cpp
void SkillMentalSensing::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillMentalSensing::castendPos2`

来源：`src/map/skills/archer/mentalsensing.cpp:17-22`

```cpp
void SkillMentalSensing::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Down Tempo (`BD_ETERNALCHAOS`)

特殊技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP 30；武器 Musical, Whip；关联状态：EternalChaos。

- 覆盖：`exact-class-methods`
- 实现类：`SkillDownTempo`
- 实现文件：`src/map/skills/archer/downtempo.cpp`

#### `SkillDownTempo::SkillDownTempo`

来源：`src/map/skills/archer/downtempo.cpp:8-9`

```cpp
SkillDownTempo::SkillDownTempo() : SkillImpl(BD_ETERNALCHAOS) {
}
```

#### `SkillDownTempo::castendNoDamageId`

来源：`src/map/skills/archer/downtempo.cpp:11-15`

```cpp
void SkillDownTempo::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillDownTempo::castendPos2`

来源：`src/map/skills/archer/downtempo.cpp:17-22`

```cpp
void SkillDownTempo::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Battle Theme (`BD_DRUMBATTLEFIELD`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=40; Lv2=45; Lv3=50; Lv4=55; Lv5=60；武器 Musical, Whip；关联状态：DrumBattle。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBattleTheme`
- 实现文件：`src/map/skills/archer/battletheme.cpp`

#### `SkillBattleTheme::SkillBattleTheme`

来源：`src/map/skills/archer/battletheme.cpp:8-9`

```cpp
SkillBattleTheme::SkillBattleTheme() : SkillImpl(BD_DRUMBATTLEFIELD) {
}
```

#### `SkillBattleTheme::castendNoDamageId`

来源：`src/map/skills/archer/battletheme.cpp:11-15`

```cpp
void SkillBattleTheme::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillBattleTheme::castendPos2`

来源：`src/map/skills/archer/battletheme.cpp:17-22`

```cpp
void SkillBattleTheme::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Harmonic Lick (`BD_RINGNIBELUNGEN`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=38; Lv2=41; Lv3=44; Lv4=47; Lv5=50；武器 Musical, Whip；关联状态：Nibelungen。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHarmonicLick`
- 实现文件：`src/map/skills/archer/harmoniclick.cpp`

#### `SkillHarmonicLick::SkillHarmonicLick`

来源：`src/map/skills/archer/harmoniclick.cpp:8-9`

```cpp
SkillHarmonicLick::SkillHarmonicLick() : SkillImpl(BD_RINGNIBELUNGEN) {
}
```

#### `SkillHarmonicLick::castendNoDamageId`

来源：`src/map/skills/archer/harmoniclick.cpp:11-15`

```cpp
void SkillHarmonicLick::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillHarmonicLick::castendPos2`

来源：`src/map/skills/archer/harmoniclick.cpp:17-22`

```cpp
void SkillHarmonicLick::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Classical Pluck (`BD_ROKISWEIL`)

特殊技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP 15；武器 Musical, Whip；关联状态：RokisWeil。

- 覆盖：`exact-class-methods`
- 实现类：`SkillClassicalPluck`
- 实现文件：`src/map/skills/archer/classicalpluck.cpp`

#### `SkillClassicalPluck::SkillClassicalPluck`

来源：`src/map/skills/archer/classicalpluck.cpp:8-9`

```cpp
SkillClassicalPluck::SkillClassicalPluck() : SkillImpl(BD_ROKISWEIL) {
}
```

#### `SkillClassicalPluck::castendNoDamageId`

来源：`src/map/skills/archer/classicalpluck.cpp:11-15`

```cpp
void SkillClassicalPluck::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillClassicalPluck::castendPos2`

来源：`src/map/skills/archer/classicalpluck.cpp:17-22`

```cpp
void SkillClassicalPluck::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Power Chord (`BD_INTOABYSS`)

特殊技能；目标：自身；最高等级 1；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP 10；武器 Musical, Whip；关联状态：IntoAbyss。

- 覆盖：`exact-class-methods`
- 实现类：`SkillPowerChord`
- 实现文件：`src/map/skills/archer/powerchord.cpp`

#### `SkillPowerChord::SkillPowerChord`

来源：`src/map/skills/archer/powerchord.cpp:8-9`

```cpp
SkillPowerChord::SkillPowerChord() : SkillImpl(BD_INTOABYSS) {
}
```

#### `SkillPowerChord::castendNoDamageId`

来源：`src/map/skills/archer/powerchord.cpp:11-15`

```cpp
void SkillPowerChord::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillPowerChord::castendPos2`

来源：`src/map/skills/archer/powerchord.cpp:17-22`

```cpp
void SkillPowerChord::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Acoustic Rhythm (`BD_SIEGFRIED`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：60000 ms；伤害标记：NoDamage；消耗/限制：SP 20；武器 Musical, Whip；关联状态：Siegfried。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAcousticRhythm`
- 实现文件：`src/map/skills/archer/acousticrhythm.cpp`

#### `SkillAcousticRhythm::SkillAcousticRhythm`

来源：`src/map/skills/archer/acousticrhythm.cpp:8-9`

```cpp
SkillAcousticRhythm::SkillAcousticRhythm() : SkillImpl(BD_SIEGFRIED) {
}
```

#### `SkillAcousticRhythm::castendNoDamageId`

来源：`src/map/skills/archer/acousticrhythm.cpp:11-15`

```cpp
void SkillAcousticRhythm::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillAcousticRhythm::castendPos2`

来源：`src/map/skills/archer/acousticrhythm.cpp:17-22`

```cpp
void SkillAcousticRhythm::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Wink of Charm (`DC_WINKCHARM`)

特殊技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；吟唱：1000 ms；技能后摇：2000 ms；持续时间1：30000 ms；持续时间2：10000 ms；伤害标记：NoDamage；消耗/限制：SP 40；关联状态：WinkCharm。

- 覆盖：`exact-class-methods`
- 实现类：`SkillWinkofCharm`
- 实现文件：`src/map/skills/archer/winkofcharm.cpp`

#### `SkillWinkofCharm::SkillWinkofCharm`

来源：`src/map/skills/archer/winkofcharm.cpp:14-15`

```cpp
SkillWinkofCharm::SkillWinkofCharm() : SkillImpl(DC_WINKCHARM) {
}
```

#### `SkillWinkofCharm::castendNoDamageId`

来源：`src/map/skills/archer/winkofcharm.cpp:17-42`

```cpp
void SkillWinkofCharm::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* dstsd = BL_CAST(BL_PC, target);
	mob_data* dstmd = BL_CAST(BL_MOB, target);

	if( dstsd ) {
#ifdef RENEWAL
		// In Renewal it causes Confusion and Hallucination to 100% base chance
		sc_start(src, target, SC_CONFUSION, 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
		sc_start(src, target, SC_HALLUCINATION, 100, skill_lv, skill_get_time2(getSkillId(), skill_lv));
#else
		// In Pre-Renewal it only causes Wink Charm, if Confusion was successfully started
		if (sc_start(src, target, SC_CONFUSION, 10, skill_lv, skill_get_time(getSkillId(), skill_lv)))
			sc_start(src, target, type, 100, skill_lv, skill_get_time2(getSkillId(), skill_lv));
#endif
	} else
	if( dstmd )
	{
		// For monsters it causes Wink Charm with a chance depending on the level difference
		if (sc_start2(src, target, type, (status_get_lv(src) - status_get_lv(target)) + 40, skill_lv, src->id, skill_get_time2(getSkillId(), skill_lv))) {
			// This triggers a 0 damage event and might make the monster switch target to caster
			battle_damage(src, target, 0, 1, skill_lv, 0, ATK_DEF, BF_WEAPON|BF_LONG|BF_NORMAL, true, tick, false);
		}
	}
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
}
```
