# Soul_Linker 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 445 | `SL_ALCHEMIST` / Spirit of the Alchemist | `exact-class-methods` | `SkillSpiritoftheAlchemist` | src/map/skills/taekwon/spiritofthealchemist.cpp |
| 447 | `SL_MONK` / Spirit of the Monk | `exact-class-methods` | `SkillSpiritoftheMonk` | src/map/skills/taekwon/spiritofthemonk.cpp |
| 448 | `SL_STAR` / Spirit of the Star Gladiator | `exact-class-methods` | `SkillSpiritoftheStarGladiator` | src/map/skills/taekwon/spiritofthestargladiator.cpp |
| 449 | `SL_SAGE` / Spirit of the Sage | `exact-class-methods` | `SkillSpiritoftheSage` | src/map/skills/taekwon/spiritofthesage.cpp |
| 450 | `SL_CRUSADER` / Spirit of the Crusader | `exact-class-methods` | `SkillSpiritoftheCrusader` | src/map/skills/taekwon/spiritofthecrusader.cpp |
| 451 | `SL_SUPERNOVICE` / Spirit of the Supernovice | `exact-class-methods` | `SkillSpiritoftheSupernovice` | src/map/skills/taekwon/spiritofthesupernovice.cpp |
| 452 | `SL_KNIGHT` / Spirit of the Knight | `exact-class-methods` | `SkillSpiritoftheKnight` | src/map/skills/taekwon/spiritoftheknight.cpp |
| 453 | `SL_WIZARD` / Spirit of the Wizard | `exact-class-methods` | `SkillSpiritoftheWizard` | src/map/skills/taekwon/spiritofthewizard.cpp |
| 454 | `SL_PRIEST` / Spirit of the Priest | `exact-class-methods` | `SkillSpiritofthePriest` | src/map/skills/taekwon/spiritofthepriest.cpp |
| 455 | `SL_BARDDANCER` / Spirit of the Artist | `exact-class-methods` | `SkillSpiritoftheArtist` | src/map/skills/taekwon/spiritoftheartist.cpp |
| 456 | `SL_ROGUE` / Spirit of the Rogue | `exact-class-methods` | `SkillSpiritoftheRogue` | src/map/skills/taekwon/spiritoftherogue.cpp |
| 457 | `SL_ASSASIN` / Spirit of the Assasin | `exact-class-methods` | `SkillSpiritoftheAssasin` | src/map/skills/taekwon/spiritoftheassasin.cpp |
| 458 | `SL_BLACKSMITH` / Spirit of the Blacksmith | `exact-class-methods` | `SkillSpiritoftheBlacksmith` | src/map/skills/taekwon/spiritoftheblacksmith.cpp |
| 460 | `SL_HUNTER` / Spirit of the Hunter | `exact-class-methods` | `SkillSpiritoftheHunter` | src/map/skills/taekwon/spiritofthehunter.cpp |
| 461 | `SL_SOULLINKER` / Spirit of the Soul Linker | `exact-class-methods` | `SkillSpiritoftheSoulLinker` | src/map/skills/taekwon/spiritofthesoullinker.cpp |
| 462 | `SL_KAIZEL` / Kaizel | `exact-class-methods` | `SkillKaizel` | src/map/skills/taekwon/kaizel.cpp |
| 463 | `SL_KAAHI` / Kaahi | `exact-class-methods` | `SkillKaahi` | src/map/skills/taekwon/kaahi.cpp |
| 464 | `SL_KAUPE` / Kaupe | `exact-class-methods` | `SkillKaupe` | src/map/skills/taekwon/kaupe.cpp |
| 465 | `SL_KAITE` / Kaite | `exact-class-methods` | `SkillKaite` | src/map/skills/taekwon/kaite.cpp |
| 466 | `SL_KAINA` / Kaina | `core-source-references` | `` | src/map/skill.cpp, src/map/status.cpp |
| 467 | `SL_STIN` / Estin | `exact-class-methods` | `SkillEstin` | src/map/skills/taekwon/estin.cpp |
| 468 | `SL_STUN` / Estun | `exact-class-methods` | `SkillEstun` | src/map/skills/taekwon/estun.cpp |
| 469 | `SL_SMA` / Esma | `exact-class-methods` | `SkillEsma` | src/map/skills/taekwon/esma.cpp |
| 470 | `SL_SWOO` / Eswoo | `exact-class-methods` | `SkillEswoo` | src/map/skills/taekwon/eswoo.cpp |
| 471 | `SL_SKE` / Eske | `exact-class-methods` | `SkillEske` | src/map/skills/taekwon/eske.cpp |
| 472 | `SL_SKA` / Eska | `exact-class-methods` | `SkillEska` | src/map/skills/taekwon/eska.cpp |
| 494 | `SL_HIGH` / Spirit of Rebirth | `exact-class-methods` | `SkillSpiritofRebirth` | src/map/skills/taekwon/spiritofrebirth.cpp |

## 详细公式与效果实现

### Spirit of the Alchemist (`SL_ALCHEMIST`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheAlchemist`
- 实现文件：`src/map/skills/taekwon/spiritofthealchemist.cpp`

#### `SkillSpiritoftheAlchemist::SkillSpiritoftheAlchemist`

来源：`src/map/skills/taekwon/spiritofthealchemist.cpp:10-11`

```cpp
SkillSpiritoftheAlchemist::SkillSpiritoftheAlchemist() : SkillImpl(SL_ALCHEMIST) {
}
```

#### `SkillSpiritoftheAlchemist::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritofthealchemist.cpp:13-26`

```cpp
void SkillSpiritoftheAlchemist::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Monk (`SL_MONK`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheMonk`
- 实现文件：`src/map/skills/taekwon/spiritofthemonk.cpp`

#### `SkillSpiritoftheMonk::SkillSpiritoftheMonk`

来源：`src/map/skills/taekwon/spiritofthemonk.cpp:10-11`

```cpp
SkillSpiritoftheMonk::SkillSpiritoftheMonk() : SkillImpl(SL_MONK) {
}
```

#### `SkillSpiritoftheMonk::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritofthemonk.cpp:13-26`

```cpp
void SkillSpiritoftheMonk::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Star Gladiator (`SL_STAR`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheStarGladiator`
- 实现文件：`src/map/skills/taekwon/spiritofthestargladiator.cpp`

#### `SkillSpiritoftheStarGladiator::SkillSpiritoftheStarGladiator`

来源：`src/map/skills/taekwon/spiritofthestargladiator.cpp:10-11`

```cpp
SkillSpiritoftheStarGladiator::SkillSpiritoftheStarGladiator() : SkillImpl(SL_STAR) {
}
```

#### `SkillSpiritoftheStarGladiator::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritofthestargladiator.cpp:13-26`

```cpp
void SkillSpiritoftheStarGladiator::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Sage (`SL_SAGE`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheSage`
- 实现文件：`src/map/skills/taekwon/spiritofthesage.cpp`

#### `SkillSpiritoftheSage::SkillSpiritoftheSage`

来源：`src/map/skills/taekwon/spiritofthesage.cpp:10-11`

```cpp
SkillSpiritoftheSage::SkillSpiritoftheSage() : SkillImpl(SL_SAGE) {
}
```

#### `SkillSpiritoftheSage::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritofthesage.cpp:13-26`

```cpp
void SkillSpiritoftheSage::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Crusader (`SL_CRUSADER`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheCrusader`
- 实现文件：`src/map/skills/taekwon/spiritofthecrusader.cpp`

#### `SkillSpiritoftheCrusader::SkillSpiritoftheCrusader`

来源：`src/map/skills/taekwon/spiritofthecrusader.cpp:10-11`

```cpp
SkillSpiritoftheCrusader::SkillSpiritoftheCrusader() : SkillImpl(SL_CRUSADER) {
}
```

#### `SkillSpiritoftheCrusader::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritofthecrusader.cpp:13-26`

```cpp
void SkillSpiritoftheCrusader::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Supernovice (`SL_SUPERNOVICE`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheSupernovice`
- 实现文件：`src/map/skills/taekwon/spiritofthesupernovice.cpp`

#### `SkillSpiritoftheSupernovice::SkillSpiritoftheSupernovice`

来源：`src/map/skills/taekwon/spiritofthesupernovice.cpp:10-11`

```cpp
SkillSpiritoftheSupernovice::SkillSpiritoftheSupernovice() : SkillImpl(SL_SUPERNOVICE) {
}
```

#### `SkillSpiritoftheSupernovice::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritofthesupernovice.cpp:13-34`

```cpp
void SkillSpiritoftheSupernovice::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );
	map_session_data *dstsd = BL_CAST( BL_PC, target );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		// 1% chance to erase death count on successful cast
		if( dstsd && dstsd->die_counter && rnd_chance( 1, 100 )  ){
			pc_setparam( dstsd, SP_PCDIECOUNTER, 0 );
			clif_specialeffect( target, EF_ANGEL2, AREA );
			status_calc_pc( dstsd, SCO_NONE );
		}

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Knight (`SL_KNIGHT`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheKnight`
- 实现文件：`src/map/skills/taekwon/spiritoftheknight.cpp`

#### `SkillSpiritoftheKnight::SkillSpiritoftheKnight`

来源：`src/map/skills/taekwon/spiritoftheknight.cpp:10-11`

```cpp
SkillSpiritoftheKnight::SkillSpiritoftheKnight() : SkillImpl(SL_KNIGHT) {
}
```

#### `SkillSpiritoftheKnight::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritoftheknight.cpp:13-26`

```cpp
void SkillSpiritoftheKnight::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Wizard (`SL_WIZARD`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheWizard`
- 实现文件：`src/map/skills/taekwon/spiritofthewizard.cpp`

#### `SkillSpiritoftheWizard::SkillSpiritoftheWizard`

来源：`src/map/skills/taekwon/spiritofthewizard.cpp:10-11`

```cpp
SkillSpiritoftheWizard::SkillSpiritoftheWizard() : SkillImpl(SL_WIZARD) {
}
```

#### `SkillSpiritoftheWizard::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritofthewizard.cpp:13-26`

```cpp
void SkillSpiritoftheWizard::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Priest (`SL_PRIEST`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritofthePriest`
- 实现文件：`src/map/skills/taekwon/spiritofthepriest.cpp`

#### `SkillSpiritofthePriest::SkillSpiritofthePriest`

来源：`src/map/skills/taekwon/spiritofthepriest.cpp:10-11`

```cpp
SkillSpiritofthePriest::SkillSpiritofthePriest() : SkillImpl(SL_PRIEST) {
}
```

#### `SkillSpiritofthePriest::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritofthepriest.cpp:13-26`

```cpp
void SkillSpiritofthePriest::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Artist (`SL_BARDDANCER`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheArtist`
- 实现文件：`src/map/skills/taekwon/spiritoftheartist.cpp`

#### `SkillSpiritoftheArtist::SkillSpiritoftheArtist`

来源：`src/map/skills/taekwon/spiritoftheartist.cpp:10-11`

```cpp
SkillSpiritoftheArtist::SkillSpiritoftheArtist() : SkillImpl(SL_BARDDANCER) {
}
```

#### `SkillSpiritoftheArtist::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritoftheartist.cpp:13-26`

```cpp
void SkillSpiritoftheArtist::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Rogue (`SL_ROGUE`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheRogue`
- 实现文件：`src/map/skills/taekwon/spiritoftherogue.cpp`

#### `SkillSpiritoftheRogue::SkillSpiritoftheRogue`

来源：`src/map/skills/taekwon/spiritoftherogue.cpp:10-11`

```cpp
SkillSpiritoftheRogue::SkillSpiritoftheRogue() : SkillImpl(SL_ROGUE) {
}
```

#### `SkillSpiritoftheRogue::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritoftherogue.cpp:13-26`

```cpp
void SkillSpiritoftheRogue::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Assasin (`SL_ASSASIN`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheAssasin`
- 实现文件：`src/map/skills/taekwon/spiritoftheassasin.cpp`

#### `SkillSpiritoftheAssasin::SkillSpiritoftheAssasin`

来源：`src/map/skills/taekwon/spiritoftheassasin.cpp:10-11`

```cpp
SkillSpiritoftheAssasin::SkillSpiritoftheAssasin() : SkillImpl(SL_ASSASIN) {
}
```

#### `SkillSpiritoftheAssasin::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritoftheassasin.cpp:13-26`

```cpp
void SkillSpiritoftheAssasin::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Blacksmith (`SL_BLACKSMITH`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheBlacksmith`
- 实现文件：`src/map/skills/taekwon/spiritoftheblacksmith.cpp`

#### `SkillSpiritoftheBlacksmith::SkillSpiritoftheBlacksmith`

来源：`src/map/skills/taekwon/spiritoftheblacksmith.cpp:10-11`

```cpp
SkillSpiritoftheBlacksmith::SkillSpiritoftheBlacksmith() : SkillImpl(SL_BLACKSMITH) {
}
```

#### `SkillSpiritoftheBlacksmith::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritoftheblacksmith.cpp:13-26`

```cpp
void SkillSpiritoftheBlacksmith::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Hunter (`SL_HUNTER`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheHunter`
- 实现文件：`src/map/skills/taekwon/spiritofthehunter.cpp`

#### `SkillSpiritoftheHunter::SkillSpiritoftheHunter`

来源：`src/map/skills/taekwon/spiritofthehunter.cpp:10-11`

```cpp
SkillSpiritoftheHunter::SkillSpiritoftheHunter() : SkillImpl(SL_HUNTER) {
}
```

#### `SkillSpiritoftheHunter::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritofthehunter.cpp:13-26`

```cpp
void SkillSpiritoftheHunter::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Spirit of the Soul Linker (`SL_SOULLINKER`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritoftheSoulLinker`
- 实现文件：`src/map/skills/taekwon/spiritofthesoullinker.cpp`

#### `SkillSpiritoftheSoulLinker::SkillSpiritoftheSoulLinker`

来源：`src/map/skills/taekwon/spiritofthesoullinker.cpp:10-11`

```cpp
SkillSpiritoftheSoulLinker::SkillSpiritoftheSoulLinker() : SkillImpl(SL_SOULLINKER) {
}
```

#### `SkillSpiritoftheSoulLinker::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritofthesoullinker.cpp:13-26`

```cpp
void SkillSpiritoftheSoulLinker::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```

### Kaizel (`SL_KAIZEL`)

魔法技能；目标：友方目标；最高等级 7；射程：9；命中类型：Single；段数：1；吟唱：Lv1=4500; Lv2=4000; Lv3=3500; Lv4=3000; Lv5=2500; Lv6=2000; Lv7=1500 ms；持续时间1：1800000 ms；持续时间2：2000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=120; Lv2=110; Lv3=100; Lv4=90; Lv5=80; Lv6=70; Lv7=60；关联状态：Kaizel。

- 覆盖：`exact-class-methods`
- 实现类：`SkillKaizel`
- 实现文件：`src/map/skills/taekwon/kaizel.cpp`

#### `SkillKaizel::SkillKaizel`

来源：`src/map/skills/taekwon/kaizel.cpp:10-11`

```cpp
SkillKaizel::SkillKaizel() : StatusSkillImpl(SL_KAIZEL) {
}
```

#### `SkillKaizel::castendNoDamageId`

来源：`src/map/skills/taekwon/kaizel.cpp:13-32`

```cpp
void SkillKaizel::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );
	map_session_data *dstsd = BL_CAST( BL_PC, target );

	if (sd) {
		if (!dstsd || !(
			(sd->sc.getSCE(SC_SPIRIT) && sd->sc.getSCE(SC_SPIRIT)->val2 == SL_SOULLINKER) ||
			(dstsd->class_&MAPID_SECONDMASK) == MAPID_SOUL_LINKER ||
			dstsd->status.char_id == sd->status.char_id ||
			dstsd->status.char_id == sd->status.partner_id ||
			dstsd->status.char_id == sd->status.child
		)) {
			status_change_start(src,src,SC_STUN,10000,skill_lv,0,0,0,500,SCSTART_NORATEDEF);
			clif_skill_fail( *sd, getSkillId() );
			return;
		}
	}

	StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
}
```

### Kaahi (`SL_KAAHI`)

魔法技能；目标：友方目标；最高等级 7；射程：9；命中类型：Single；段数：1；技能后摇：500 ms；持续时间1：350000 ms；伤害标记：NoDamage；消耗/限制：SP 30；关联状态：Kaahi。

- 覆盖：`exact-class-methods`
- 实现类：`SkillKaahi`
- 实现文件：`src/map/skills/taekwon/kaahi.cpp`

#### `SkillKaahi::SkillKaahi`

来源：`src/map/skills/taekwon/kaahi.cpp:10-11`

```cpp
SkillKaahi::SkillKaahi() : StatusSkillImpl(SL_KAAHI) {
}
```

#### `SkillKaahi::castendNoDamageId`

来源：`src/map/skills/taekwon/kaahi.cpp:13-32`

```cpp
void SkillKaahi::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );
	map_session_data *dstsd = BL_CAST( BL_PC, target );

	if (sd) {
		if (!dstsd || !(
			(sd->sc.getSCE(SC_SPIRIT) && sd->sc.getSCE(SC_SPIRIT)->val2 == SL_SOULLINKER) ||
			(dstsd->class_&MAPID_SECONDMASK) == MAPID_SOUL_LINKER ||
			dstsd->status.char_id == sd->status.char_id ||
			dstsd->status.char_id == sd->status.partner_id ||
			dstsd->status.char_id == sd->status.child
		)) {
			status_change_start(src,src,SC_STUN,10000,skill_lv,0,0,0,500,SCSTART_NORATEDEF);
			clif_skill_fail( *sd, getSkillId() );
			return;
		}
	}

	StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
}
```

### Kaupe (`SL_KAUPE`)

魔法技能；目标：友方目标；最高等级 3；射程：9；命中类型：Single；段数：1；吟唱：500 ms；技能后摇：500 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=20; Lv2=30; Lv3=40；关联状态：Kaupe。

- 覆盖：`exact-class-methods`
- 实现类：`SkillKaupe`
- 实现文件：`src/map/skills/taekwon/kaupe.cpp`

#### `SkillKaupe::SkillKaupe`

来源：`src/map/skills/taekwon/kaupe.cpp:10-11`

```cpp
SkillKaupe::SkillKaupe() : StatusSkillImpl(SL_KAUPE) {
}
```

#### `SkillKaupe::castendNoDamageId`

来源：`src/map/skills/taekwon/kaupe.cpp:13-32`

```cpp
void SkillKaupe::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );
	map_session_data *dstsd = BL_CAST( BL_PC, target );

	if (sd) {
		if (!dstsd || !(
			(sd->sc.getSCE(SC_SPIRIT) && sd->sc.getSCE(SC_SPIRIT)->val2 == SL_SOULLINKER) ||
			(dstsd->class_&MAPID_SECONDMASK) == MAPID_SOUL_LINKER ||
			dstsd->status.char_id == sd->status.char_id ||
			dstsd->status.char_id == sd->status.partner_id ||
			dstsd->status.char_id == sd->status.child
		)) {
			status_change_start(src,src,SC_STUN,10000,skill_lv,0,0,0,500,SCSTART_NORATEDEF);
			clif_skill_fail( *sd, getSkillId() );
			return;
		}
	}

	StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
}
```

### Kaite (`SL_KAITE`)

魔法技能；目标：友方目标；最高等级 7；射程：9；命中类型：Single；段数：1；吟唱：Lv1=6000; Lv2=5500; Lv3=5000; Lv4=4500; Lv5=4000; Lv6=3500; Lv7=3000 ms；持续时间1：Lv1=60000; Lv2=120000; Lv3=180000; Lv4=240000; Lv5=300000; Lv6=360000; Lv7=600000 ms；伤害标记：NoDamage；消耗/限制：SP 70；关联状态：Kaite。

- 覆盖：`exact-class-methods`
- 实现类：`SkillKaite`
- 实现文件：`src/map/skills/taekwon/kaite.cpp`

#### `SkillKaite::SkillKaite`

来源：`src/map/skills/taekwon/kaite.cpp:10-11`

```cpp
SkillKaite::SkillKaite() : StatusSkillImpl(SL_KAITE) {
}
```

#### `SkillKaite::castendNoDamageId`

来源：`src/map/skills/taekwon/kaite.cpp:13-32`

```cpp
void SkillKaite::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );
	map_session_data *dstsd = BL_CAST( BL_PC, target );

	if (sd) {
		if (!dstsd || !(
			(sd->sc.getSCE(SC_SPIRIT) && sd->sc.getSCE(SC_SPIRIT)->val2 == SL_SOULLINKER) ||
			(dstsd->class_&MAPID_SECONDMASK) == MAPID_SOUL_LINKER ||
			dstsd->status.char_id == sd->status.char_id ||
			dstsd->status.char_id == sd->status.partner_id ||
			dstsd->status.char_id == sd->status.child
		)) {
			status_change_start(src,src,SC_STUN,10000,skill_lv,0,0,0,500,SCSTART_NORATEDEF);
			clif_skill_fail( *sd, getSkillId() );
			return;
		}
	}

	StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
}
```

### Kaina (`SL_KAINA`)

魔法技能；目标：被动；最高等级 7。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:9986
req.sp -= req.sp*7*kaina_lv/100;
// src/map/skill.cpp:9988
req.sp -= req.sp*5*kaina_lv/100;
// src/map/skill.cpp:9990
req.sp -= req.sp*3*kaina_lv/100;
// src/map/status.cpp:3302
status_change *sc = status_get_sc(bl);
// src/map/status.cpp:3307
uint16 skill_lv;
// src/map/status.cpp:3309
bonus += sd->bonus.sp;
// src/map/status.cpp:3310
if ((skill_lv = pc_checkskill(sd,SL_KAINA)) > 0)
// src/map/status.cpp:3311
bonus += 30 * skill_lv;
// src/map/status.cpp:3312
if ((skill_lv = pc_checkskill(sd,RA_RESEARCHTRAP)) > 0)
// src/map/status.cpp:3313
bonus += 200 + 20 * skill_lv;
// src/map/status.cpp:3314
if ((skill_lv = pc_checkskill(sd,WM_LESSON)) > 0)
// src/map/status.cpp:3315
bonus += 30 * skill_lv;
// src/map/status.cpp:5333
sregen->hp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5343
sregen->sp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5349
val = regen->hp*(100+5*skill)/100;
// src/map/status.cpp:5350
regen->hp = cap_value(val, 1, SHRT_MAX);
```

### Estin (`SL_STIN`)

魔法技能；目标：敌方目标；最高等级 7；射程：9；命中类型：Single；段数：1；属性：Endowed；击退：2；吟唱：100 ms；技能后摇：500 ms；消耗/限制：SP Lv1=18; Lv2=20; Lv3=22; Lv4=24; Lv5=26; Lv6=28; Lv7=30。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEstin`
- 实现文件：`src/map/skills/taekwon/estin.cpp`

#### `SkillEstin::SkillEstin`

来源：`src/map/skills/taekwon/estin.cpp:10-11`

```cpp
SkillEstin::SkillEstin() : SkillImpl(SL_STIN) {
}
```

#### `SkillEstin::calculateSkillRatio`

来源：`src/map/skills/taekwon/estin.cpp:13-18`

```cpp
void SkillEstin::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const status_data* tstatus = status_get_status_data(*target);

	// Target size must be small (0) for full damage
	base_skillratio += (tstatus->size != SZ_SMALL ? -99 : 10 * skill_lv);
}
```

#### `SkillEstin::castendDamageId`

来源：`src/map/skills/taekwon/estin.cpp:20-29`

```cpp
void SkillEstin::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	if (sd && !battle_config.allow_es_magic_pc && target->type != BL_MOB) {
		status_change_start(src,src,SC_STUN,10000,skill_lv,0,0,0,500,SCSTART_NOTICKDEF|SCSTART_NORATEDEF);
		clif_skill_fail( *sd, getSkillId() );
		return;
	}
	skill_attack(BF_MAGIC,src,src,target,getSkillId(),skill_lv,tick,flag);
}
```

### Estun (`SL_STUN`)

魔法技能；目标：敌方目标；最高等级 7；射程：9；命中类型：Single；段数：1；属性：Endowed；吟唱：100 ms；技能后摇：500 ms；持续时间1：2000 ms；消耗/限制：SP Lv1=18; Lv2=20; Lv3=22; Lv4=24; Lv5=26; Lv6=28; Lv7=30；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEstun`
- 实现文件：`src/map/skills/taekwon/estun.cpp`

#### `SkillEstun::SkillEstun`

来源：`src/map/skills/taekwon/estun.cpp:10-11`

```cpp
SkillEstun::SkillEstun() : SkillImpl(SL_STUN) {
}
```

#### `SkillEstun::calculateSkillRatio`

来源：`src/map/skills/taekwon/estun.cpp:13-15`

```cpp
void SkillEstun::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 5 * skill_lv;
}
```

#### `SkillEstun::castendDamageId`

来源：`src/map/skills/taekwon/estun.cpp:17-26`

```cpp
void SkillEstun::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	if (sd && !battle_config.allow_es_magic_pc && target->type != BL_MOB) {
		status_change_start(src,src,SC_STUN,10000,skill_lv,0,0,0,500,SCSTART_NOTICKDEF|SCSTART_NORATEDEF);
		clif_skill_fail( *sd, getSkillId() );
		return;
	}
	skill_attack(BF_MAGIC,src,src,target,getSkillId(),skill_lv,tick,flag);
}
```

#### `SkillEstun::applyAdditionalEffects`

来源：`src/map/skills/taekwon/estun.cpp:28-33`

```cpp
void SkillEstun::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	status_data* tstatus = status_get_status_data(*target);

	if (tstatus->size==SZ_MEDIUM) //Only stuns mid-sized mobs.
		sc_start(src,target,SC_STUN,(30+10*skill_lv),skill_lv,skill_get_time(getSkillId(),skill_lv));
}
```

### Esma (`SL_SMA`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Endowed；吟唱：2000 ms；技能后摇：500 ms；持续时间1：3000 ms；消耗/限制：SP Lv1=8; Lv2=16; Lv3=24; Lv4=32; Lv5=40; Lv6=48; Lv7=56; Lv8=64; Lv9=72; Lv10=80；关联状态：Sma。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEsma`
- 实现文件：`src/map/skills/taekwon/esma.cpp`

#### `SkillEsma::SkillEsma`

来源：`src/map/skills/taekwon/esma.cpp:10-11`

```cpp
SkillEsma::SkillEsma() : SkillImpl(SL_SMA) {
}
```

#### `SkillEsma::calculateSkillRatio`

来源：`src/map/skills/taekwon/esma.cpp:13-16`

```cpp
void SkillEsma::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	// Base damage is 40% + lv%
	base_skillratio += -60 + status_get_lv(src);
}
```

#### `SkillEsma::castendDamageId`

来源：`src/map/skills/taekwon/esma.cpp:18-28`

```cpp
void SkillEsma::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	status_change_end(src, SC_SMA);
	if (sd && !battle_config.allow_es_magic_pc && target->type != BL_MOB) {
		status_change_start(src,src,SC_STUN,10000,skill_lv,0,0,0,500,SCSTART_NOTICKDEF|SCSTART_NORATEDEF);
		clif_skill_fail( *sd, getSkillId() );
		return;
	}
	skill_attack(BF_MAGIC,src,src,target,getSkillId(),skill_lv,tick,flag);
}
```

### Eswoo (`SL_SWOO`)

魔法技能；目标：敌方目标；最高等级 7；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=1000; Lv2=2000; Lv3=3000; Lv4=4000; Lv5=5000; Lv6=6000; Lv7=7000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=75; Lv2=65; Lv3=55; Lv4=45; Lv5=35; Lv6=25; Lv7=15；关联状态：Swoo。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEswoo`
- 实现文件：`src/map/skills/taekwon/eswoo.cpp`

#### `SkillEswoo::SkillEswoo`

来源：`src/map/skills/taekwon/eswoo.cpp:10-11`

```cpp
SkillEswoo::SkillEswoo() : StatusSkillImpl(SL_SWOO) {
}
```

#### `SkillEswoo::castendNoDamageId`

来源：`src/map/skills/taekwon/eswoo.cpp:13-33`

```cpp
void SkillEswoo::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	status_change *tsc = status_get_sc(target);
	status_change_entry *tsce = (tsc && type != SC_NONE)?tsc->getSCE(type):nullptr;
	map_session_data* sd = BL_CAST( BL_PC, src );

	if (tsce) {
		if(sd)
			clif_skill_fail( *sd, getSkillId() );
		status_change_start(src,src,SC_STUN,10000,skill_lv,0,0,0,10000,SCSTART_NORATEDEF);
		status_change_end(target, SC_SWOO);
		return;
	}
	if (sd && !battle_config.allow_es_magic_pc && target->type != BL_MOB) {
		clif_skill_fail( *sd, getSkillId() );
		status_change_start(src,src,SC_STUN,10000,skill_lv,0,0,0,500,SCSTART_NOTICKDEF|SCSTART_NORATEDEF);
		return;
	}

	StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
}
```

### Eske (`SL_SKE`)

魔法技能；目标：敌方目标；最高等级 3；射程：9；命中类型：Single；段数：1；吟唱：Lv1=3000; Lv2=2000; Lv3=1000 ms；技能后摇：500 ms；持续时间1：Lv1=10000; Lv2=20000; Lv3=30000 ms；持续时间2：3000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=55; Lv2=35; Lv3=15；关联状态：Ske。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEske`
- 实现文件：`src/map/skills/taekwon/eske.cpp`

#### `SkillEske::SkillEske`

来源：`src/map/skills/taekwon/eske.cpp:10-11`

```cpp
SkillEske::SkillEske() : StatusSkillImpl(SL_SKE) {
}
```

#### `SkillEske::castendNoDamageId`

来源：`src/map/skills/taekwon/eske.cpp:13-25`

```cpp
void SkillEske::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST( BL_PC, src );

	if (sd && !battle_config.allow_es_magic_pc && target->type != BL_MOB) {
		clif_skill_fail( *sd, getSkillId() );
		status_change_start(src,src,SC_STUN,10000,skill_lv,0,0,0,500,SCSTART_NOTICKDEF|SCSTART_NORATEDEF);
		return;
	}

	StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);

	sc_start(src,src,SC_SMA,100,skill_lv,skill_get_time(SL_SMA,skill_lv));
}
```

### Eska (`SL_SKA`)

魔法技能；目标：敌方目标；最高等级 3；射程：9；命中类型：Single；段数：1；吟唱：Lv1=3000; Lv2=2000; Lv3=1000 ms；技能后摇：500 ms；持续时间1：Lv1=10000; Lv2=20000; Lv3=30000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=100; Lv2=80; Lv3=60；关联状态：Ska。

- 覆盖：`exact-class-methods`
- 实现类：`SkillEska`
- 实现文件：`src/map/skills/taekwon/eska.cpp`

#### `SkillEska::SkillEska`

来源：`src/map/skills/taekwon/eska.cpp:10-11`

```cpp
SkillEska::SkillEska() : StatusSkillImpl(SL_SKA) {
}
```

#### `SkillEska::castendNoDamageId`

来源：`src/map/skills/taekwon/eska.cpp:13-33`

```cpp
void SkillEska::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	status_change *tsc = status_get_sc(target);
	status_change_entry *tsce = (tsc && type != SC_NONE)?tsc->getSCE(type):nullptr;
	map_session_data* sd = BL_CAST( BL_PC, src );

	if (tsce) {
		if(sd)
			clif_skill_fail( *sd, getSkillId() );
		status_change_start(src,src,SC_STUN,10000,skill_lv,0,0,0,10000,SCSTART_NORATEDEF);
		status_change_end(target, SC_SWOO);
		return;
	}
	if (sd && !battle_config.allow_es_magic_pc && target->type != BL_MOB) {
		clif_skill_fail( *sd, getSkillId() );
		status_change_start(src,src,SC_STUN,10000,skill_lv,0,0,0,500,SCSTART_NOTICKDEF|SCSTART_NORATEDEF);
		return;
	}

	StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
}
```

### Spirit of Rebirth (`SL_HIGH`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；技能后摇：500 ms；持续时间1：Lv1=150000; Lv2=200000; Lv3=250000; Lv4=300000; Lv5=350000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=460; Lv2=360; Lv3=260; Lv4=160; Lv5=60；关联状态：Spirit。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpiritofRebirth`
- 实现文件：`src/map/skills/taekwon/spiritofrebirth.cpp`

#### `SkillSpiritofRebirth::SkillSpiritofRebirth`

来源：`src/map/skills/taekwon/spiritofrebirth.cpp:10-11`

```cpp
SkillSpiritofRebirth::SkillSpiritofRebirth() : SkillImpl(SL_HIGH) {
}
```

#### `SkillSpiritofRebirth::castendNoDamageId`

来源：`src/map/skills/taekwon/spiritofrebirth.cpp:13-26`

```cpp
void SkillSpiritofRebirth::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	map_session_data* sd = BL_CAST( BL_PC, src );

	if( sc_start2( src, target, type, 100, skill_lv, getSkillId(), skill_get_time( getSkillId(), skill_lv ) ) ){
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv);

		sc_start( src, src, SC_SMA, 100, skill_lv, skill_get_time( SL_SMA, skill_lv ) );
	}else{
		if( sd ){
			clif_skill_fail( *sd, getSkillId() );
		}
	}
}
```
