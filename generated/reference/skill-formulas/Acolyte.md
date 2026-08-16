# Acolyte 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
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
| 156 | `AL_HOLYLIGHT` / Holy Light | `exact-class-methods` | `SkillHolyLight` | src/map/skills/acolyte/holylight.cpp |

## 详细公式与效果实现

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

### Holy Light (`AL_HOLYLIGHT`)

魔法技能；目标：敌方目标；最高等级 1；射程：9；命中类型：Single；段数：1；属性：Holy；吟唱：2000 ms；消耗/限制：SP 15。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHolyLight`
- 实现文件：`src/map/skills/acolyte/holylight.cpp`

#### `SkillHolyLight::SkillHolyLight`

来源：`src/map/skills/acolyte/holylight.cpp:10-11`

```cpp
SkillHolyLight::SkillHolyLight() : SkillImpl(AL_HOLYLIGHT) {
}
```

#### `SkillHolyLight::castendDamageId`

来源：`src/map/skills/acolyte/holylight.cpp:13-16`

```cpp
void SkillHolyLight::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	status_change_end(target, SC_P_ALTER);
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

#### `SkillHolyLight::calculateSkillRatio`

来源：`src/map/skills/acolyte/holylight.cpp:18-24`

```cpp
void SkillHolyLight::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
	const map_session_data* sd = BL_CAST(BL_PC, src);

	base_skillratio += 25;
	if (sd && sd->sc.getSCE(SC_SPIRIT) && sd->sc.getSCE(SC_SPIRIT)->val2 == SL_PRIEST)
		base_skillratio *= 5; //Does 5x damage include bonuses from other skills?
}
```
