# Champion 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 370 | `CH_PALMSTRIKE` / Raging Palm Strike | `exact-class-methods` | `SkillRagingPalmStrike` | src/map/skills/acolyte/ragingpalmstrike.cpp |
| 371 | `CH_TIGERFIST` / Glacier Fist | `exact-class-methods` | `SkillGlacierFist` | src/map/skills/acolyte/glacierfist.cpp |
| 372 | `CH_CHAINCRUSH` / Chain Crush Combo | `exact-class-methods` | `SkillChainCrushCombo` | src/map/skills/acolyte/chaincrushcombo.cpp |
| 401 | `CH_SOULCOLLECT` / Zen | `exact-class-methods` | `SkillZen` | src/map/skills/acolyte/zen.cpp |

## 详细公式与效果实现

### Raging Palm Strike (`CH_PALMSTRIKE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：-2；命中类型：Single；段数：1；属性：Weapon；击退：3；技能后摇：300 ms；消耗/限制：SP Lv1=2; Lv2=4; Lv3=6; Lv4=8; Lv5=10；前置状态 Explosionspirits。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRagingPalmStrike`
- 实现文件：`src/map/skills/acolyte/ragingpalmstrike.cpp`

#### `SkillRagingPalmStrike::SkillRagingPalmStrike`

来源：`src/map/skills/acolyte/ragingpalmstrike.cpp:11-12`

```cpp
SkillRagingPalmStrike::SkillRagingPalmStrike() : SkillImpl(CH_PALMSTRIKE) {
}
```

#### `SkillRagingPalmStrike::castendDamageId`

来源：`src/map/skills/acolyte/ragingpalmstrike.cpp:14-19`

```cpp
void SkillRagingPalmStrike::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	//	Palm Strike takes effect 1sec after casting. [Skotlex]
	// clif_skill_nodamage(src,*target,getSkillId(),skill_lv,false); //Can't make this one display the correct attack animation delay :/
	clif_damage(*src, *target, tick, status_get_amotion(src), 0, -1, 1, DMG_ENDURE, 0, false); //Display an absorbed damage attack.
	skill_addtimerskill(src, tick + (1000 + status_get_amotion(src)), target->id, 0, 0, getSkillId(), skill_lv, BF_WEAPON, flag);
}
```

#### `SkillRagingPalmStrike::calculateSkillRatio`

来源：`src/map/skills/acolyte/ragingpalmstrike.cpp:21-30`

```cpp
void SkillRagingPalmStrike::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& skillratio, int32 mflag) const {
#ifdef RENEWAL
	const status_data* sstatus = status_get_status_data(*src);

	skillratio += 100 + 100 * skill_lv + sstatus->str; // !TODO: How does STR play a role?
	RE_LVL_DMOD(100);
#else
	skillratio += 100 + 100 * skill_lv;
#endif
}
```

### Glacier Fist (`CH_TIGERFIST`)

武器/物理技能；目标：自身；最高等级 5；射程：-2；命中类型：Multi_Hit；段数：1；属性：Weapon；持续时间1：Lv1=2000; Lv2=4000; Lv3=6000; Lv4=8000; Lv5=10000 ms；消耗/限制：SP Lv1=4; Lv2=6; Lv3=8; Lv4=10; Lv5=12；气弹 1；关联状态：Ankle。

- 覆盖：`exact-class-methods`
- 实现类：`SkillGlacierFist`
- 实现文件：`src/map/skills/acolyte/glacierfist.cpp`

#### `SkillGlacierFist::SkillGlacierFist`

来源：`src/map/skills/acolyte/glacierfist.cpp:10-11`

```cpp
SkillGlacierFist::SkillGlacierFist() : WeaponSkillImpl(CH_TIGERFIST) {
}
```

#### `SkillGlacierFist::calculateSkillRatio`

来源：`src/map/skills/acolyte/glacierfist.cpp:13-22`

```cpp
void SkillGlacierFist::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& skillratio, int32 mflag) const {
#ifdef RENEWAL
	skillratio += 400 + 150 * skill_lv;
	RE_LVL_DMOD(100);
#else
	skillratio += -60 + 100 * skill_lv;
#endif
	if (const status_change* sc = status_get_sc(src); sc != nullptr && sc->getSCE(SC_GT_ENERGYGAIN))
		skillratio += skillratio * 50 / 100;
}
```

#### `SkillGlacierFist::applyAdditionalEffects`

来源：`src/map/skills/acolyte/glacierfist.cpp:24-32`

```cpp
void SkillGlacierFist::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	t_tick basetime = skill_get_time(getSkillId(), skill_lv);
	t_tick mintime = 15 * (status_get_lv(src) + 100);

	if (status_bl_has_mode(target, MD_STATUSIMMUNE))
		basetime /= 5;
	basetime = std::max((basetime * status_get_agi(target)) / -200 + basetime, mintime);
	sc_start(src, target, SC_ANKLE, (1 + skill_lv) * 10, 0, basetime);
}
```

### Chain Crush Combo (`CH_CHAINCRUSH`)

武器/物理技能；目标：自身；最高等级 10；射程：-2；命中类型：Multi_Hit；段数：Lv1-2=-1; Lv3-4=-2; Lv5-6=-3; Lv7-8=-4; Lv9-10=-5；属性：Weapon；消耗/限制：SP Lv1=4; Lv2=6; Lv3=8; Lv4=10; Lv5=12; Lv6=14; Lv7=16; Lv8=18; Lv9=20; Lv10=22；气弹 2。

- 覆盖：`exact-class-methods`
- 实现类：`SkillChainCrushCombo`
- 实现文件：`src/map/skills/acolyte/chaincrushcombo.cpp`

#### `SkillChainCrushCombo::SkillChainCrushCombo`

来源：`src/map/skills/acolyte/chaincrushcombo.cpp:10-11`

```cpp
SkillChainCrushCombo::SkillChainCrushCombo() : WeaponSkillImpl(CH_CHAINCRUSH) {
}
```

#### `SkillChainCrushCombo::calculateSkillRatio`

来源：`src/map/skills/acolyte/chaincrushcombo.cpp:13-22`

```cpp
void SkillChainCrushCombo::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& skillratio, int32 mflag) const {
#ifdef RENEWAL
	skillratio += -100 + 200 * skill_lv;
	RE_LVL_DMOD(100);
#else
	skillratio += 300 + 100 * skill_lv;
#endif
	if (const status_change* sc = status_get_sc(src); sc != nullptr && sc->getSCE(SC_GT_ENERGYGAIN))
		skillratio += skillratio * 50 / 100;
}
```

### Zen (`CH_SOULCOLLECT`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 20。

- 覆盖：`exact-class-methods`
- 实现类：`SkillZen`
- 实现文件：`src/map/skills/acolyte/zen.cpp`

#### `SkillZen::SkillZen`

来源：`src/map/skills/acolyte/zen.cpp:10-11`

```cpp
SkillZen::SkillZen() : SkillImpl(CH_SOULCOLLECT) {
}
```

#### `SkillZen::castendNoDamageId`

来源：`src/map/skills/acolyte/zen.cpp:13-24`

```cpp
void SkillZen::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if(sd) {
		int32 limit = 5;
		if( sd->sc.getSCE(SC_RAISINGDRAGON) )
			limit += sd->sc.getSCE(SC_RAISINGDRAGON)->val1;
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
		for (int32 i = 0; i < limit; i++)
			pc_addspiritball(sd,skill_get_time(getSkillId(),skill_lv),limit);
	}
}
```
