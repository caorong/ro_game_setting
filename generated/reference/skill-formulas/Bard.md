# Bard 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 315 | `BA_MUSICALLESSON` / Music Lessons | `core-source-references` | `` | src/map/battle.cpp, src/map/skill.cpp, src/map/status.cpp |
| 316 | `BA_MUSICALSTRIKE` / Melody Strike | `exact-class-methods` | `SkillMelodyStrike` | src/map/skills/archer/melodystrike.cpp |
| 317 | `BA_DISSONANCE` / Unchained Serenade | `exact-class-methods` | `SkillUnchainedSerenade` | src/map/skills/archer/unchainedserenade.cpp |
| 318 | `BA_FROSTJOKER` / Unbarring Octave | `exact-class-methods` | `SkillUnbarringOctave` | src/map/skills/archer/unbarringoctave.cpp |
| 319 | `BA_WHISTLE` / Perfect Tablature | `exact-class-methods` | `SkillPerfectTablature` | src/map/skills/archer/perfecttablature.cpp |
| 320 | `BA_ASSASSINCROSS` / Impressive Riff | `exact-class-methods` | `SkillImpressiveRiff` | src/map/skills/archer/impressiveriff.cpp |
| 321 | `BA_POEMBRAGI` / Magic Strings | `exact-class-methods` | `SkillMagicStrings` | src/map/skills/archer/magicstrings.cpp |
| 322 | `BA_APPLEIDUN` / Song of Lutie | `exact-class-methods` | `SkillSongofLutie` | src/map/skills/archer/songoflutie.cpp |
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
| 1010 | `BA_PANGVOICE` / Pang Voice | `exact-class-methods` | `SkillPangVoice` | src/map/skills/archer/pangvoice.cpp |

## 详细公式与效果实现

### Music Lessons (`BA_MUSICALLESSON`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2371
damage += (skill * 4);
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
// src/map/battle.cpp:6391
DAMAGE_DIV_FIX2(md.damage, skill_get_num(HT_BLITZBEAT, 5));
// src/map/battle.cpp:6393
md.damage = md.damage * (150 + 70 * skill_lv) / 100;
// src/map/battle.cpp:6399
md.damage = 30 + 10 * skill_lv;
// src/map/battle.cpp:6400
md.damage += skill_lv * pc_checkskill(sd, BA_MUSICALLESSON);
// src/map/battle.cpp:6404
md.damage = sstatus->hp;
// src/map/battle.cpp:6407
md.damage = 3;
// src/map/battle.cpp:6410
md.damage = skill_calc_heal(src,target,skill_id,skill_lv,false);
// src/map/skill.cpp:524
map_session_data *sd = BL_CAST(BL_PC, src);
// src/map/skill.cpp:525
map_session_data *tsd = BL_CAST(BL_PC, target);
// src/map/skill.cpp:526
status_change *sc, *tsc;
```

### Melody Strike (`BA_MUSICALSTRIKE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Weapon；吟唱：1500 ms；消耗/限制：SP Lv1=1; Lv2=3; Lv3=5; Lv4=7; Lv5=9；弹药数 1；武器 Musical；弹药 Arrow。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMelodyStrike`
- 实现文件：`src/map/skills/archer/melodystrike.cpp`

#### `SkillMelodyStrike::SkillMelodyStrike`

来源：`src/map/skills/archer/melodystrike.cpp:8-9`

```cpp
SkillMelodyStrike::SkillMelodyStrike() : WeaponSkillImpl(BA_MUSICALSTRIKE) {
}
```

#### `SkillMelodyStrike::calculateSkillRatio`

来源：`src/map/skills/archer/melodystrike.cpp:11-17`

```cpp
void SkillMelodyStrike::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 10 + 40 * skill_lv;
#else
	base_skillratio += -40 + 40 * skill_lv;
#endif
}
```

### Unchained Serenade (`BA_DISSONANCE`)

特殊技能；目标：自身；最高等级 5；命中类型：Multi_Hit；段数：1；持续时间1：30000 ms；持续时间2：3000 ms；伤害标记：NoDamage, IgnoreFlee；消耗/限制：SP Lv1=18; Lv2=21; Lv3=24; Lv4=27; Lv5=30；武器 Musical。

- 覆盖：`exact-class-methods`
- 实现类：`SkillUnchainedSerenade`
- 实现文件：`src/map/skills/archer/unchainedserenade.cpp`

#### `SkillUnchainedSerenade::SkillUnchainedSerenade`

来源：`src/map/skills/archer/unchainedserenade.cpp:10-11`

```cpp
SkillUnchainedSerenade::SkillUnchainedSerenade() : WeaponSkillImpl(BA_DISSONANCE) {
}
```

#### `SkillUnchainedSerenade::calculateSkillRatio`

来源：`src/map/skills/archer/unchainedserenade.cpp:13-21`

```cpp
void SkillUnchainedSerenade::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	const map_session_data* sd = BL_CAST( BL_PC, src );

	base_skillratio += 10 + skill_lv * 50;
	if (sd != nullptr)
		base_skillratio = base_skillratio * sd->status.job_level / 10;
#endif
}
```

#### `SkillUnchainedSerenade::castendNoDamageId`

来源：`src/map/skills/archer/unchainedserenade.cpp:23-27`

```cpp
void SkillUnchainedSerenade::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillUnchainedSerenade::castendPos2`

来源：`src/map/skills/archer/unchainedserenade.cpp:29-35`

```cpp
void SkillUnchainedSerenade::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	// Ammo should be deleted right away.
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Unbarring Octave (`BA_FROSTJOKER`)

特殊技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；技能后摇：4000 ms；持续时间1：15000 ms；持续时间2：12000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20；关联状态：Freeze。

- 覆盖：`exact-class-methods`
- 实现类：`SkillUnbarringOctave`
- 实现文件：`src/map/skills/archer/unbarringoctave.cpp`

#### `SkillUnbarringOctave::SkillUnbarringOctave`

来源：`src/map/skills/archer/unbarringoctave.cpp:11-12`

```cpp
SkillUnbarringOctave::SkillUnbarringOctave() : SkillImpl(BA_FROSTJOKER) {
}
```

#### `SkillUnbarringOctave::applyAdditionalEffects`

来源：`src/map/skills/archer/unbarringoctave.cpp:14-23`

```cpp
void SkillUnbarringOctave::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	int32 rate = 150 + 50 * skill_lv; // Aegis accuracy (1000 = 100%)
	int32 duration = skill_get_time2(getSkillId(), skill_lv);
	if (battle_check_target(src, target, BCT_PARTY) > 0) {
		// On party members: Chance is divided by 4 and duration is fixed to 15000ms
		rate /= 4;
		duration = skill_get_time(getSkillId(), skill_lv);
	}
	status_change_start(src, target, skill_get_sc(getSkillId()), rate*10, skill_lv, 0, 0, 0, duration, SCSTART_NONE);
}
```

#### `SkillUnbarringOctave::castendNoDamageId`

来源：`src/map/skills/archer/unbarringoctave.cpp:25-38`

```cpp
void SkillUnbarringOctave::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	mob_data *md = BL_CAST(BL_MOB, src);

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

### Perfect Tablature (`BA_WHISTLE`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：60000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=24; Lv2=28; Lv3=32; Lv4=36; Lv5=40; Lv6=44; Lv7=48; Lv8=52; Lv9=56; Lv10=60；武器 Musical, Whip；关联状态：Whistle。

- 覆盖：`exact-class-methods`
- 实现类：`SkillPerfectTablature`
- 实现文件：`src/map/skills/archer/perfecttablature.cpp`

#### `SkillPerfectTablature::SkillPerfectTablature`

来源：`src/map/skills/archer/perfecttablature.cpp:8-9`

```cpp
SkillPerfectTablature::SkillPerfectTablature() : SkillImpl(BA_WHISTLE) {
}
```

#### `SkillPerfectTablature::castendNoDamageId`

来源：`src/map/skills/archer/perfecttablature.cpp:11-15`

```cpp
void SkillPerfectTablature::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillPerfectTablature::castendPos2`

来源：`src/map/skills/archer/perfecttablature.cpp:17-22`

```cpp
void SkillPerfectTablature::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Impressive Riff (`BA_ASSASSINCROSS`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：120000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=38; Lv2=41; Lv3=44; Lv4=47; Lv5=50; Lv6=53; Lv7=56; Lv8=59; Lv9=62; Lv10=65；武器 Musical, Whip；关联状态：AssnCros。

- 覆盖：`exact-class-methods`
- 实现类：`SkillImpressiveRiff`
- 实现文件：`src/map/skills/archer/impressiveriff.cpp`

#### `SkillImpressiveRiff::SkillImpressiveRiff`

来源：`src/map/skills/archer/impressiveriff.cpp:8-9`

```cpp
SkillImpressiveRiff::SkillImpressiveRiff() : SkillImpl(BA_ASSASSINCROSS) {
}
```

#### `SkillImpressiveRiff::castendNoDamageId`

来源：`src/map/skills/archer/impressiveriff.cpp:11-15`

```cpp
void SkillImpressiveRiff::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillImpressiveRiff::castendPos2`

来源：`src/map/skills/archer/impressiveriff.cpp:17-22`

```cpp
void SkillImpressiveRiff::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Magic Strings (`BA_POEMBRAGI`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：180000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=40; Lv2=45; Lv3=50; Lv4=55; Lv5=60; Lv6=65; Lv7=70; Lv8=75; Lv9=80; Lv10=85；武器 Musical, Whip；关联状态：PoemBragi。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMagicStrings`
- 实现文件：`src/map/skills/archer/magicstrings.cpp`

#### `SkillMagicStrings::SkillMagicStrings`

来源：`src/map/skills/archer/magicstrings.cpp:8-9`

```cpp
SkillMagicStrings::SkillMagicStrings() : SkillImpl(BA_POEMBRAGI) {
}
```

#### `SkillMagicStrings::castendNoDamageId`

来源：`src/map/skills/archer/magicstrings.cpp:11-15`

```cpp
void SkillMagicStrings::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillMagicStrings::castendPos2`

来源：`src/map/skills/archer/magicstrings.cpp:17-22`

```cpp
void SkillMagicStrings::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
#endif
}
```

### Song of Lutie (`BA_APPLEIDUN`)

特殊技能；目标：自身；最高等级 10；命中类型：Single；段数：1；持续时间1：180000 ms；持续时间2：20000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=40; Lv2=45; Lv3=50; Lv4=55; Lv5=60; Lv6=65; Lv7=70; Lv8=75; Lv9=80; Lv10=85；武器 Musical, Whip；关联状态：AppleIdun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSongofLutie`
- 实现文件：`src/map/skills/archer/songoflutie.cpp`

#### `SkillSongofLutie::SkillSongofLutie`

来源：`src/map/skills/archer/songoflutie.cpp:8-9`

```cpp
SkillSongofLutie::SkillSongofLutie() : SkillImpl(BA_APPLEIDUN) {
}
```

#### `SkillSongofLutie::castendNoDamageId`

来源：`src/map/skills/archer/songoflutie.cpp:11-15`

```cpp
void SkillSongofLutie::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	skill_castend_song(src, getSkillId(), skill_lv, tick);
#endif
}
```

#### `SkillSongofLutie::castendPos2`

来源：`src/map/skills/archer/songoflutie.cpp:17-22`

```cpp
void SkillSongofLutie::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
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

### Pang Voice (`BA_PANGVOICE`)

特殊技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；吟唱：1000 ms；技能后摇：2000 ms；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP 20。

- 覆盖：`exact-class-methods`
- 实现类：`SkillPangVoice`
- 实现文件：`src/map/skills/archer/pangvoice.cpp`

#### `SkillPangVoice::SkillPangVoice`

来源：`src/map/skills/archer/pangvoice.cpp:11-12`

```cpp
SkillPangVoice::SkillPangVoice() : SkillImpl(BA_PANGVOICE) {
}
```

#### `SkillPangVoice::castendNoDamageId`

来源：`src/map/skills/archer/pangvoice.cpp:14-24`

```cpp
void SkillPangVoice::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	// In Renewal it causes Confusion and Bleeding to 100% base chance
	sc_start(src, target, SC_CONFUSION, 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
	sc_start(src, target, SC_BLEEDING, 100, skill_lv, skill_get_time2(getSkillId(), skill_lv));
#else
	// In Pre-renewal it causes Confusion to 70% base chance
	sc_start(src, target, SC_CONFUSION, 70, skill_lv, skill_get_time(getSkillId(), skill_lv));
#endif
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
}
```
