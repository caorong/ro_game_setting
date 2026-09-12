# Priest 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 9 | `MG_SRECOVERY` / Increase SP Recovery | `core-source-references` | `` | src/map/pc.cpp, src/map/skill.cpp, src/map/skills/acolyte/competentia.cpp, src/map/skills/merchant/aidberserkpotion.cpp, src/map/skills/merchant/aidcondensedpotion.cpp, src/map/skills/merchant/aidpotion.cpp, src/map/skills/other/netsupport.cpp, src/map/status.cpp |
| 12 | `MG_SAFETYWALL` / Safety Wall | `exact-class-methods` | `SkillSafetyWall` | src/map/skills/mage/safetywall.cpp |
| 54 | `ALL_RESURRECTION` / Resurrection | `exact-class-methods` | `SkillResurrection` | src/map/skills/acolyte/resurrection.cpp |
| 65 | `PR_MACEMASTERY` / Mace Mastery | `core-source-references` | `` | src/map/battle.cpp, src/map/status.cpp |
| 66 | `PR_IMPOSITIO` / Impositio Manus | `exact-class-methods` | `SkillImpositioManus` | src/map/skills/acolyte/impositiomanus.cpp |
| 67 | `PR_SUFFRAGIUM` / Suffragium | `exact-class-methods` | `SkillSuffragium` | src/map/skills/acolyte/suffragium.cpp |
| 68 | `PR_ASPERSIO` / Aspersio | `exact-class-methods` | `SkillAspersio` | src/map/skills/acolyte/aspersio.cpp |
| 69 | `PR_BENEDICTIO` / B.S. Sacramenti | `exact-class-methods` | `SkillBenedictioSanctissimiSacramenti` | src/map/skills/acolyte/bssacramenti.cpp |
| 70 | `PR_SANCTUARY` / Sanctuary | `exact-class-methods` | `SkillSanctuary` | src/map/skills/acolyte/sanctuary.cpp |
| 71 | `PR_SLOWPOISON` / Slow Poison | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 72 | `PR_STRECOVERY` / Status Recovery | `exact-class-methods` | `SkillStatusRecovery` | src/map/skills/acolyte/statusrecovery.cpp |
| 73 | `PR_KYRIE` / Kyrie Eleison | `exact-class-methods` | `SkillKyrieEleison` | src/map/skills/acolyte/kyrieeleison.cpp |
| 74 | `PR_MAGNIFICAT` / Magnificat | `exact-class-methods` | `SkillMagnificat` | src/map/skills/acolyte/magnificat.cpp |
| 75 | `PR_GLORIA` / Gloria | `exact-class-methods` | `SkillGloria` | src/map/skills/acolyte/gloria.cpp |
| 76 | `PR_LEXDIVINA` / Lex Divina | `exact-class-methods` | `SkillLexDivina` | src/map/skills/acolyte/lexdivina.cpp |
| 77 | `PR_TURNUNDEAD` / Turn Undead | `exact-class-methods` | `SkillTurnUndead` | src/map/skills/acolyte/turnundead.cpp |
| 78 | `PR_LEXAETERNA` / Lex Aeterna | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 79 | `PR_MAGNUS` / Magnus Exorcismus | `exact-class-methods` | `SkillMagnusExorcismus` | src/map/skills/acolyte/magnusexorcismus.cpp |
| 1014 | `PR_REDEMPTIO` / Redemptio | `exact-class-methods` | `SkillRedemptio` | src/map/skills/acolyte/redemptio.cpp |

## 详细公式与效果实现

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

### Resurrection (`ALL_RESURRECTION`)

魔法技能；目标：友方目标；最高等级 4；射程：9；命中类型：Single；段数：1；属性：Holy；吟唱：Lv1=6000; Lv2=4000; Lv3=2000 ms；技能后摇：Lv2=1000; Lv3=2000; Lv4=3000 ms；伤害标记：NoDamage；消耗/限制：SP 60；道具 Blue_Gemstone×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillResurrection`
- 实现文件：`src/map/skills/acolyte/resurrection.cpp`

#### `SkillResurrection::SkillResurrection`

来源：`src/map/skills/acolyte/resurrection.cpp:12-13`

```cpp
SkillResurrection::SkillResurrection() : SkillImpl(ALL_RESURRECTION) {
}
```

#### `SkillResurrection::castendDamageId`

来源：`src/map/skills/acolyte/resurrection.cpp:15-21`

```cpp
void SkillResurrection::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);

	if (!battle_check_undead(tstatus->race, tstatus->def_ele))
		return;
	skill_attack(BF_MAGIC,src,src,target,getSkillId(),skill_lv,tick,flag);
}
```

#### `SkillResurrection::castendNoDamageId`

来源：`src/map/skills/acolyte/resurrection.cpp:23-74`

```cpp
void SkillResurrection::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_change *tsc = status_get_sc(target);
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if(map_flag_gvg2(target->m) || map_getmapflag(target->m, MF_BATTLEGROUND))
	{	//No reviving in WoE grounds!
		if( sd != nullptr ){
			clif_skill_fail( *sd, getSkillId() );
		}
		return;
	}
	if (!status_isdead(*target))
		return;

	int32 per = 0, sper = 0;
	if (tsc && tsc->getSCE(SC_HELLPOWER)) {
		clif_skill_nodamage(src, *target, ALL_RESURRECTION, skill_lv);
		return;
	}

	if (map_getmapflag(target->m, MF_PVP) && dstsd && dstsd->pvp_point < 0)
		return;

	switch(skill_lv){
	case 1: per=10; break;
	case 2: per=30; break;
	case 3: per=50; break;
	case 4: per=80; break;
	}
	if(dstsd && dstsd->special_state.restart_full_recover)
		per = sper = 100;
	if (status_revive(target, per, sper))
	{
		clif_skill_nodamage(src,*target,ALL_RESURRECTION,skill_lv); //Both Redemptio and Res show this skill-animation.
		if(sd && dstsd && battle_config.resurrection_exp > 0)
		{
			t_exp exp = 0,jexp = 0;
			int32 lv = dstsd->status.base_level - sd->status.base_level, jlv = dstsd->status.job_level - sd->status.job_level;
			if(lv > 0 && pc_nextbaseexp(dstsd)) {
				exp = (t_exp)(dstsd->status.base_exp * lv * battle_config.resurrection_exp / 1000000.);
				if (exp < 1) exp = 1;
			}
			if(jlv > 0 && pc_nextjobexp(dstsd)) {
				jexp = (t_exp)(dstsd->status.job_exp * lv * battle_config.resurrection_exp / 1000000.);
				if (jexp < 1) jexp = 1;
			}
			if(exp > 0 || jexp > 0)
				pc_gainexp (sd, target, exp, jexp, 0);
		}
	}
}
```

### Mace Mastery (`PR_MACEMASTERY`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2356
damage += (skill * 10);
// src/map/battle.cpp:2362
damage += (skill * 3);
// src/map/battle.cpp:2364
damage += (skill * 5);
// src/map/battle.cpp:2369
damage += (skill * 3);
// src/map/battle.cpp:2371
damage += (skill * 4);
// src/map/battle.cpp:2375
damage += (skill * 10);
// src/map/battle.cpp:2379
damage += (skill * 3);
// src/map/status.cpp:4520
base_status->flee += (skill*3) / 2;
// src/map/status.cpp:4522
base_status->flee += 20;
// src/map/status.cpp:4524
base_status->flee += skill * 10;
// src/map/status.cpp:4530
base_status->cri += skill * 10;
// src/map/status.cpp:4532
base_status->cri += skill * 10;
// src/map/status.cpp:4538
base_status->cri += 100 + skill * 40;
// src/map/status.cpp:4540
base_status->cri += 50 + skill * 20;
```

### Impositio Manus (`PR_IMPOSITIO`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；技能后摇：3000 ms；持续时间1：60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=13; Lv2=16; Lv3=19; Lv4=22; Lv5=25；关联状态：Impositio。

- 覆盖：`exact-class-methods`
- 实现类：`SkillImpositioManus`
- 实现文件：`src/map/skills/acolyte/impositiomanus.cpp`

#### `SkillImpositioManus::SkillImpositioManus`

来源：`src/map/skills/acolyte/impositiomanus.cpp:12-13`

```cpp
SkillImpositioManus::SkillImpositioManus() : SkillImpl(PR_IMPOSITIO) {
}
```

#### `SkillImpositioManus::castendNoDamageId`

来源：`src/map/skills/acolyte/impositiomanus.cpp:15-28`

```cpp
void SkillImpositioManus::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd == nullptr || sd->status.party_id == 0 || (flag & 1)) {

		// Animations don't play when outside visible range
		if (check_distance_bl(src, target, AREA_SIZE))
			clif_skill_nodamage(target, *target, getSkillId(), skill_lv);

		sc_start(src, target, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
	}
	else if (sd)
		party_foreachsamemap(skill_area_sub, sd, skill_get_splash(getSkillId(), skill_lv), src, getSkillId(), skill_lv, tick, flag | BCT_PARTY | 1, skill_castend_nodamage_id);
}
```

#### `SkillImpositioManus::SkillImpositioManus`

来源：`src/map/skills/acolyte/impositiomanus.cpp:30-31`

```cpp
SkillImpositioManus::SkillImpositioManus() : StatusSkillImpl(PR_IMPOSITIO) {
}
```

### Suffragium (`PR_SUFFRAGIUM`)

魔法技能；目标：友方目标；最高等级 3；射程：9；命中类型：Single；段数：1；技能后摇：2000 ms；持续时间1：Lv1=30000; Lv2=20000; Lv3=10000 ms；伤害标记：NoDamage；消耗/限制：SP 8；关联状态：Suffragium。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSuffragium`
- 实现文件：`src/map/skills/acolyte/suffragium.cpp`

#### `SkillSuffragium::SkillSuffragium`

来源：`src/map/skills/acolyte/suffragium.cpp:12-13`

```cpp
SkillSuffragium::SkillSuffragium() : SkillImpl(PR_SUFFRAGIUM) {
}
```

#### `SkillSuffragium::castendNoDamageId`

来源：`src/map/skills/acolyte/suffragium.cpp:15-28`

```cpp
void SkillSuffragium::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd == nullptr || sd->status.party_id == 0 || (flag & 1)) {

		// Animations don't play when outside visible range
		if (check_distance_bl(src, target, AREA_SIZE))
			clif_skill_nodamage(target, *target, getSkillId(), skill_lv);

		sc_start(src, target, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
	}
	else if (sd)
		party_foreachsamemap(skill_area_sub, sd, skill_get_splash(getSkillId(), skill_lv), src, getSkillId(), skill_lv, tick, flag | BCT_PARTY | 1, skill_castend_nodamage_id);
}
```

#### `SkillSuffragium::SkillSuffragium`

来源：`src/map/skills/acolyte/suffragium.cpp:30-31`

```cpp
SkillSuffragium::SkillSuffragium() : StatusSkillImpl(PR_SUFFRAGIUM) {
}
```

### Aspersio (`PR_ASPERSIO`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Holy；技能后摇：2000 ms；持续时间1：Lv1=60000; Lv2=90000; Lv3=120000; Lv4=150000; Lv5=180000 ms；伤害标记：NoDamage, IgnoreElement, IgnoreDefense；消耗/限制：SP Lv1=14; Lv2=18; Lv3=22; Lv4=26; Lv5=30；道具 Holy_Water×1；关联状态：Aspersio。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAspersio`
- 实现文件：`src/map/skills/acolyte/aspersio.cpp`

#### `SkillAspersio::SkillAspersio`

来源：`src/map/skills/acolyte/aspersio.cpp:11-12`

```cpp
SkillAspersio::SkillAspersio() : SkillImpl(PR_ASPERSIO) {
}
```

#### `SkillAspersio::castendNoDamageId`

来源：`src/map/skills/acolyte/aspersio.cpp:14-24`

```cpp
void SkillAspersio::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	mob_data* dstmd = BL_CAST(BL_MOB, target);

	if (sd && dstmd) {
		clif_skill_nodamage(src,*target,getSkillId(), skill_lv, false);
		return;
	}
	clif_skill_nodamage(src,*target, getSkillId(),skill_lv,
		sc_start(src,target,skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
}
```

#### `SkillAspersio::castendDamageId`

来源：`src/map/skills/acolyte/aspersio.cpp:26-28`

```cpp
void SkillAspersio::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

### B.S. Sacramenti (`PR_BENEDICTIO`)

魔法技能；目标：地面区域；最高等级 5；射程：9；命中类型：Single；段数：1；范围：1；持续时间1：Lv1=40000; Lv2=80000; Lv3=120000; Lv4=160000; Lv5=200000 ms；伤害标记：NoDamage, Splash, IgnoreDefense；消耗/限制：SP 20；关联状态：Benedictio。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBenedictioSanctissimiSacramenti`
- 实现文件：`src/map/skills/acolyte/bssacramenti.cpp`

#### `SkillBenedictioSanctissimiSacramenti::SkillBenedictioSanctissimiSacramenti`

来源：`src/map/skills/acolyte/bssacramenti.cpp:9-10`

```cpp
SkillBenedictioSanctissimiSacramenti::SkillBenedictioSanctissimiSacramenti() : SkillImpl(PR_BENEDICTIO) {
}
```

#### `SkillBenedictioSanctissimiSacramenti::castendNoDamageId`

来源：`src/map/skills/acolyte/bssacramenti.cpp:12-17`

```cpp
void SkillBenedictioSanctissimiSacramenti::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);

	if (!battle_check_undead(tstatus->race, tstatus->def_ele) && tstatus->race != RC_DEMON)
		clif_skill_nodamage(src, *target, getSkillId(), skill_lv, sc_start(src, target, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
}
```

#### `SkillBenedictioSanctissimiSacramenti::castendDamageId`

来源：`src/map/skills/acolyte/bssacramenti.cpp:19-25`

```cpp
void SkillBenedictioSanctissimiSacramenti::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);

	//Should attack undead and demons. [Skotlex]
	if (battle_check_undead(tstatus->race, tstatus->def_ele) || tstatus->race == RC_DEMON)
		skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

#### `SkillBenedictioSanctissimiSacramenti::castendPos2`

来源：`src/map/skills/acolyte/bssacramenti.cpp:27-38`

```cpp
void SkillBenedictioSanctissimiSacramenti::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_area_temp[1] = src->id;
	int32 i = skill_get_splash(getSkillId(), skill_lv);
	map_foreachinallarea(skill_area_sub,
		src->m, x-i, y-i, x+i, y+i, BL_PC,
		src, getSkillId(), skill_lv, tick, flag|BCT_ALL|1,
		skill_castend_nodamage_id);
	map_foreachinallarea(skill_area_sub,
		src->m, x-i, y-i, x+i, y+i, BL_CHAR,
		src, getSkillId(), skill_lv, tick, flag|BCT_ENEMY|1,
		skill_castend_damage_id);
}
```

### Sanctuary (`PR_SANCTUARY`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Holy；击退：2；吟唱：5000 ms；持续时间1：Lv1=3900; Lv2=6900; Lv3=9900; Lv4=12900; Lv5=15900; Lv6=18900; Lv7=21900; Lv8=24900; Lv9=27900; Lv10=30900 ms；伤害标记：NoDamage, IgnoreDefense；消耗/限制：SP Lv1=15; Lv2=18; Lv3=21; Lv4=24; Lv5=27; Lv6=30; Lv7=33; Lv8=36; Lv9=39; Lv10=42；道具 Blue_Gemstone×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSanctuary`
- 实现文件：`src/map/skills/acolyte/sanctuary.cpp`

#### `SkillSanctuary::SkillSanctuary`

来源：`src/map/skills/acolyte/sanctuary.cpp:6-7`

```cpp
SkillSanctuary::SkillSanctuary() : SkillImpl(PR_SANCTUARY) {
}
```

#### `SkillSanctuary::castendPos2`

来源：`src/map/skills/acolyte/sanctuary.cpp:9-13`

```cpp
void SkillSanctuary::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;
	skill_unitsetting(src, getSkillId(), skill_lv, x, y, 0);
}
```

### Slow Poison (`PR_SLOWPOISON`)

魔法技能；目标：友方目标；最高等级 4；射程：9；命中类型：Single；段数：1；持续时间1：Lv1=10000; Lv2=20000; Lv3=30000; Lv4=40000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=6; Lv2=8; Lv3=10; Lv4=12；关联状态：SlowPoison。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Status Recovery (`PR_STRECOVERY`)

魔法技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；技能后摇：2000 ms；持续时间2：30000 ms；伤害标记：NoDamage；消耗/限制：SP 5；关联状态：Blind。

- 覆盖：`exact-class-methods`
- 实现类：`SkillStatusRecovery`
- 实现文件：`src/map/skills/acolyte/statusrecovery.cpp`

#### `SkillStatusRecovery::SkillStatusRecovery`

来源：`src/map/skills/acolyte/statusrecovery.cpp:10-11`

```cpp
SkillStatusRecovery::SkillStatusRecovery() : SkillImpl(PR_STRECOVERY) {
}
```

#### `SkillStatusRecovery::castendNoDamageId`

来源：`src/map/skills/acolyte/statusrecovery.cpp:13-46`

```cpp
void SkillStatusRecovery::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);
	status_change* tsc = status_get_sc(target);
	mob_data* dstmd = BL_CAST(BL_MOB, target);

	if(status_isimmune(target)) {
		clif_skill_nodamage(src,*target,getSkillId(), skill_lv, false);
		return;
	}
	if (battle_check_undead(tstatus->race, tstatus->def_ele))
		skill_addtimerskill(src, tick + 1000, target->id, 0, 0, getSkillId(), skill_lv, 100, flag);
	else {
		// Bodystate is reset to "normal" for non-undead
		if (tsc) {
			// The following are bodystate status changes
			status_change_end(target, SC_STONE);
			status_change_end(target, SC_FREEZE);
			status_change_end(target, SC_STUN);
			status_change_end(target, SC_SLEEP);
			status_change_end(target, SC_STONEWAIT);
			status_change_end(target, SC_BURNING);
			status_change_end(target, SC_WHITEIMPRISON);
		}
		// Resetting bodystate to normal always also resets the monster AI to idle
		if (dstmd)
			mob_unlocktarget(dstmd, tick);
	}
	if (tsc) {
		// Ends SC_NETHERWORLD and SC_NORECOVER_STATE (even on undead)
		status_change_end(target, SC_NETHERWORLD);
		status_change_end(target, SC_NORECOVER_STATE);
	}
	clif_skill_nodamage(src,*target, getSkillId(),skill_lv);
}
```

### Kyrie Eleison (`PR_KYRIE`)

魔法技能；目标：友方目标；最高等级 10；射程：9；命中类型：Single；段数：1；吟唱：2000 ms；技能后摇：2000 ms；持续时间1：120000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-3=20; Lv4-6=25; Lv7-9=30; Lv10=35；关联状态：Kyrie。

- 覆盖：`exact-class-methods`
- 实现类：`SkillKyrieEleison`
- 实现文件：`src/map/skills/acolyte/kyrieeleison.cpp`

#### `SkillKyrieEleison::SkillKyrieEleison`

来源：`src/map/skills/acolyte/kyrieeleison.cpp:9-10`

```cpp
SkillKyrieEleison::SkillKyrieEleison() : SkillImpl(PR_KYRIE) {
}
```

#### `SkillKyrieEleison::castendNoDamageId`

来源：`src/map/skills/acolyte/kyrieeleison.cpp:12-15`

```cpp
void SkillKyrieEleison::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	clif_skill_nodamage(target,*target,getSkillId(), skill_lv,
			sc_start(src,target,skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv)));
}
```

### Magnificat (`PR_MAGNIFICAT`)

魔法技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；吟唱：4000 ms；技能后摇：2000 ms；持续时间1：Lv1=30000; Lv2=45000; Lv3=60000; Lv4=75000; Lv5=90000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 40；关联状态：Magnificat。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMagnificat`
- 实现文件：`src/map/skills/acolyte/magnificat.cpp`

#### `SkillMagnificat::SkillMagnificat`

来源：`src/map/skills/acolyte/magnificat.cpp:11-12`

```cpp
SkillMagnificat::SkillMagnificat() : SkillImpl(PR_MAGNIFICAT) {
}
```

#### `SkillMagnificat::castendNoDamageId`

来源：`src/map/skills/acolyte/magnificat.cpp:14-27`

```cpp
void SkillMagnificat::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd == nullptr || sd->status.party_id == 0 || (flag & 1)) {

		// Animations don't play when outside visible range
		if (check_distance_bl(src, target, AREA_SIZE))
			clif_skill_nodamage(target, *target, getSkillId(), skill_lv);

		sc_start(src, target, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
	}
	else if (sd)
		party_foreachsamemap(skill_area_sub, sd, skill_get_splash(getSkillId(), skill_lv), src, getSkillId(), skill_lv, tick, flag | BCT_PARTY | 1, skill_castend_nodamage_id);
}
```

### Gloria (`PR_GLORIA`)

魔法技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；技能后摇：2000 ms；持续时间1：Lv1=10000; Lv2=15000; Lv3=20000; Lv4=25000; Lv5=30000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 20；关联状态：Gloria。

- 覆盖：`exact-class-methods`
- 实现类：`SkillGloria`
- 实现文件：`src/map/skills/acolyte/gloria.cpp`

#### `SkillGloria::SkillGloria`

来源：`src/map/skills/acolyte/gloria.cpp:11-12`

```cpp
SkillGloria::SkillGloria() : SkillImpl(PR_GLORIA) {
}
```

#### `SkillGloria::castendNoDamageId`

来源：`src/map/skills/acolyte/gloria.cpp:14-27`

```cpp
void SkillGloria::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if (sd == nullptr || sd->status.party_id == 0 || (flag & 1)) {

		// Animations don't play when outside visible range
		if (check_distance_bl(src, target, AREA_SIZE))
			clif_skill_nodamage(target, *target, getSkillId(), skill_lv);

		sc_start(src, target, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
	}
	else if (sd)
		party_foreachsamemap(skill_area_sub, sd, skill_get_splash(getSkillId(), skill_lv), src, getSkillId(), skill_lv, tick, flag | BCT_PARTY | 1, skill_castend_nodamage_id);
}
```

### Lex Divina (`PR_LEXDIVINA`)

魔法技能；目标：敌方目标；最高等级 10；射程：5；命中类型：Single；技能后摇：3000 ms；持续时间2：Lv1=30000; Lv2=35000; Lv3=40000; Lv4=45000; Lv5=50000; Lv6-10=60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1-5=20; Lv6=18; Lv7=16; Lv8=14; Lv9=12; Lv10=10；关联状态：Silence。

- 覆盖：`exact-class-methods`
- 实现类：`SkillLexDivina`
- 实现文件：`src/map/skills/acolyte/lexdivina.cpp`

#### `SkillLexDivina::SkillLexDivina`

来源：`src/map/skills/acolyte/lexdivina.cpp:9-10`

```cpp
SkillLexDivina::SkillLexDivina() : SkillImpl(PR_LEXDIVINA) {
}
```

#### `SkillLexDivina::castendNoDamageId`

来源：`src/map/skills/acolyte/lexdivina.cpp:12-22`

```cpp
void SkillLexDivina::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());
	status_change* tsc = status_get_sc(target);
	status_change_entry* tsce = (tsc && type != SC_NONE) ? tsc->getSCE(type) : nullptr;

	if (tsce)
		status_change_end(target, type);
	else
		skill_addtimerskill(src, tick+1000, target->id, 0, 0, getSkillId(), skill_lv, 100, flag);
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
}
```

### Turn Undead (`PR_TURNUNDEAD`)

魔法技能；目标：敌方目标；最高等级 10；射程：5；命中类型：Single；段数：1；属性：Holy；吟唱：1000 ms；技能后摇：3000 ms；伤害标记：IgnoreAtkCard, IgnoreDefense；消耗/限制：SP 20。

- 覆盖：`exact-class-methods`
- 实现类：`SkillTurnUndead`
- 实现文件：`src/map/skills/acolyte/turnundead.cpp`

#### `SkillTurnUndead::SkillTurnUndead`

来源：`src/map/skills/acolyte/turnundead.cpp:8-9`

```cpp
SkillTurnUndead::SkillTurnUndead() : SkillImpl(PR_TURNUNDEAD) {
}
```

#### `SkillTurnUndead::castendDamageId`

来源：`src/map/skills/acolyte/turnundead.cpp:11-17`

```cpp
void SkillTurnUndead::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_data* tstatus = status_get_status_data(*target);

	if (!battle_check_undead(tstatus->race, tstatus->def_ele))
		return;
	skill_attack(BF_MAGIC,src,src,target,getSkillId(), skill_lv, tick, flag);
}
```

### Lex Aeterna (`PR_LEXAETERNA`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；技能后摇：3000 ms；持续时间1：600000 ms；伤害标记：NoDamage；消耗/限制：SP 10；关联状态：Aeterna。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skills/npc/lexaeterna2.cpp:11
void SkillLexAeterna2::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/npc/lexaeterna2.cpp:12
int32 i = skill_get_splash(getSkillId(), skill_lv);
// src/map/skills/npc/lexaeterna2.cpp:13
map_foreachinallarea(skill_area_sub, src->m, x-i, y-i, x+i, y+i, BL_CHAR, src, PR_LEXAETERNA, 1, tick, flag|BCT_ENEMY|1, skill_castend_nodamage_id);
```

### Magnus Exorcismus (`PR_MAGNUS`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Holy；吟唱：15000 ms；技能后摇：4000 ms；持续时间1：Lv1=5000; Lv2=6000; Lv3=7000; Lv4=8000; Lv5=9000; Lv6=10000; Lv7=11000; Lv8=12000; Lv9=13000; Lv10=14000 ms；消耗/限制：SP Lv1=40; Lv2=42; Lv3=44; Lv4=46; Lv5=48; Lv6=50; Lv7=52; Lv8=54; Lv9=56; Lv10=58；道具 Blue_Gemstone×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMagnusExorcismus`
- 实现文件：`src/map/skills/acolyte/magnusexorcismus.cpp`

#### `SkillMagnusExorcismus::SkillMagnusExorcismus`

来源：`src/map/skills/acolyte/magnusexorcismus.cpp:8-9`

```cpp
SkillMagnusExorcismus::SkillMagnusExorcismus() : SkillImpl(PR_MAGNUS) {
}
```

#### `SkillMagnusExorcismus::castendPos2`

来源：`src/map/skills/acolyte/magnusexorcismus.cpp:11-16`

```cpp
void SkillMagnusExorcismus::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src, getSkillId(), skill_lv, x, y, 0);
}
```

#### `SkillMagnusExorcismus::calculateSkillRatio`

来源：`src/map/skills/acolyte/magnusexorcismus.cpp:18-23`

```cpp
void SkillMagnusExorcismus::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	const status_data* tstatus = status_get_status_data(*target);

	if (battle_check_undead(tstatus->race, tstatus->def_ele) || tstatus->race == RC_DEMON)
		base_skillratio += 30;
}
```

### Redemptio (`PR_REDEMPTIO`)

魔法技能；目标：自身；最高等级 1；命中类型：Single；属性：Holy；范围：14；吟唱：4000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 400。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRedemptio`
- 实现文件：`src/map/skills/acolyte/redemptio.cpp`

#### `SkillRedemptio::SkillRedemptio`

来源：`src/map/skills/acolyte/redemptio.cpp:15-16`

```cpp
SkillRedemptio::SkillRedemptio() : SkillImpl(PR_REDEMPTIO) {
}
```

#### `SkillRedemptio::castendNoDamageId`

来源：`src/map/skills/acolyte/redemptio.cpp:18-99`

```cpp
void SkillRedemptio::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);
	status_change* tsc = status_get_sc(target);

	if (sd && !(flag&1)) {
		if (sd->status.party_id == 0) {
			clif_skill_fail( *sd, getSkillId() );
			return;
		}
		skill_area_temp[0] = 0;
		party_foreachsamemap(skill_area_sub,
			sd,skill_get_splash(getSkillId(), skill_lv),
			src,getSkillId(),skill_lv,tick, flag|BCT_PARTY|1,
			skill_castend_nodamage_id);
		if (skill_area_temp[0] == 0) {
			clif_skill_fail( *sd, getSkillId() );
			return;
		}
#ifndef RENEWAL
		skill_area_temp[0] = battle_config.exp_cost_redemptio_limit - skill_area_temp[0]; // The actual penalty...
		if (skill_area_temp[0] > 0 && !map_getmapflag(src->m, MF_NOEXPPENALTY) && battle_config.exp_cost_redemptio) { //Apply penalty
			//If total penalty is 1% => reduced 0.2% penalty per each revived player
			pc_lostexp(sd, u64min(sd->status.base_exp, (pc_nextbaseexp(sd) * skill_area_temp[0] * battle_config.exp_cost_redemptio / battle_config.exp_cost_redemptio_limit) / 100), 0);
		}
		status_set_sp(src, 0, 0);
#endif
		status_set_hp(src, 1, 0);
		return;
	} else if (!(status_isdead(*target) && flag&1)) { 
		//Invalid target, skip resurrection.
		return;
	}
	//Revive
	skill_area_temp[0]++; //Count it in, then fall-through to the Resurrection code.
	skill_lv = 3; //Resurrection level 3 is used

	if(sd && (map_flag_gvg2(target->m) || map_getmapflag(target->m, MF_BATTLEGROUND)))
	{	//No reviving in WoE grounds!
		clif_skill_fail( *sd, getSkillId() );
		return;
	}
	if (!status_isdead(*target))
		return;

	int32 per = 0, sper = 0;
	if (tsc && tsc->getSCE(SC_HELLPOWER)) {
		clif_skill_nodamage(src, *target, ALL_RESURRECTION, skill_lv);
		return;
	}

	if (map_getmapflag(target->m, MF_PVP) && dstsd && dstsd->pvp_point < 0)
		return;

	switch(skill_lv){
	case 1: per=10; break;
	case 2: per=30; break;
	case 3: per=50; break;
	case 4: per=80; break;
	}
	if(dstsd && dstsd->special_state.restart_full_recover)
		per = sper = 100;
	if (status_revive(target, per, sper))
	{
		clif_skill_nodamage(src,*target,ALL_RESURRECTION,skill_lv); //Both Redemptio and Res show this skill-animation.
		if(sd && dstsd && battle_config.resurrection_exp > 0)
		{
			t_exp exp = 0,jexp = 0;
			int32 lv = dstsd->status.base_level - sd->status.base_level, jlv = dstsd->status.job_level - sd->status.job_level;
			if(lv > 0 && pc_nextbaseexp(dstsd)) {
				exp = (t_exp)(dstsd->status.base_exp * lv * battle_config.resurrection_exp / 1000000.);
				if (exp < 1) exp = 1;
			}
			if(jlv > 0 && pc_nextjobexp(dstsd)) {
				jexp = (t_exp)(dstsd->status.job_exp * lv * battle_config.resurrection_exp / 1000000.);
				if (jexp < 1) jexp = 1;
			}
			if(exp > 0 || jexp > 0)
				pc_gainexp (sd, target, exp, jexp, 0);
		}
	}
}
```
