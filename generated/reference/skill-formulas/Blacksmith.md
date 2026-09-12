# Blacksmith 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 94 | `BS_IRON` / Iron Tempering | `core-source-references` | `` | src/map/skill.cpp |
| 95 | `BS_STEEL` / Steel Tempering | `core-source-references` | `` | src/map/skill.cpp |
| 96 | `BS_ENCHANTEDSTONE` / Enchanted Stone Craft | `core-source-references` | `` | src/map/skill.cpp |
| 97 | `BS_ORIDEOCON` / Oridecon Research | `core-source-references` | `` | src/map/skill.cpp |
| 98 | `BS_DAGGER` / Smith Dagger | `core-source-references` | `` | src/map/skill.cpp |
| 99 | `BS_SWORD` / Smith Sword | `core-source-references` | `` | src/map/skill.cpp |
| 100 | `BS_TWOHANDSWORD` / Smith Two-handed Sword | `core-source-references` | `` | src/map/skill.cpp |
| 101 | `BS_AXE` / Smith Axe | `core-source-references` | `` | src/map/skill.cpp |
| 102 | `BS_MACE` / Smith Mace | `core-source-references` | `` | src/map/skill.cpp |
| 103 | `BS_KNUCKLE` / Smith Knucklebrace | `core-source-references` | `` | src/map/skill.cpp |
| 104 | `BS_SPEAR` / Smith Spear | `core-source-references` | `` | src/map/skill.cpp |
| 105 | `BS_HILTBINDING` / Hilt Binding | `core-source-references` | `` | src/map/battle.cpp, src/map/status.cpp |
| 106 | `BS_FINDINGORE` / Ore Discovery | `core-source-references` | `` | src/map/mob.cpp |
| 107 | `BS_WEAPONRESEARCH` / Weaponry Research | `core-source-references` | `` | src/map/battle.cpp, src/map/skill.cpp, src/map/status.cpp |
| 108 | `BS_REPAIRWEAPON` / Weapon Repair | `exact-class-methods` | `SkillWeaponRepair` | src/map/skills/merchant/weaponrepair.cpp |
| 109 | `BS_SKINTEMPER` / Skin Tempering | `core-source-references` | `` | src/map/status.cpp |
| 110 | `BS_HAMMERFALL` / Hammer Fall | `exact-class-methods` | `SkillHammerFall` | src/map/skills/merchant/hammerfall.cpp |
| 111 | `BS_ADRENALINE` / Adrenaline Rush | `exact-class-methods` | `SkillAdrenalineRush` | src/map/skills/merchant/adrenalinerush.cpp |
| 112 | `BS_WEAPONPERFECT` / Weapon Perfection | `exact-class-methods` | `SkillWeaponPerfection` | src/map/skills/merchant/weaponperfection.cpp |
| 113 | `BS_OVERTHRUST` / Power-Thrust | `exact-class-methods` | `SkillPowerThrust` | src/map/skills/merchant/powerthrust.cpp |
| 114 | `BS_MAXIMIZE` / Maximize Power | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 1012 | `BS_UNFAIRLYTRICK` / Unfair Trick | `core-source-references` | `` | src/map/skill.cpp |
| 1013 | `BS_GREED` / Greed | `exact-class-methods` | `SkillGreed` | src/map/skills/merchant/greed.cpp |
| 459 | `BS_ADRENALINE2` / Advanced Adrenaline Rush | `exact-class-methods` | `SkillAdvancedAdrenalineRush` | src/map/skills/merchant/advancedadrenalinerush.cpp |

## 详细公式与效果实现

### Iron Tempering (`BS_IRON`)

武器/物理技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:13436
case ASC_CDP: //25% Damage yourself, and display same effect as failed potion.
// src/map/skill.cpp:13437
status_percent_damage(nullptr, sd, -25, 0, true);
```

### Steel Tempering (`BS_STEEL`)

武器/物理技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:13437
status_percent_damage(nullptr, sd, -25, 0, true);
```

### Enchanted Stone Craft (`BS_ENCHANTEDSTONE`)

武器/物理技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:13462
int32 rate = rnd() % 1000 + 1;
```

### Oridecon Research (`BS_ORIDEOCON`)

武器/物理技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Smith Dagger (`BS_DAGGER`)

武器/物理技能；目标：被动；最高等级 3。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Smith Sword (`BS_SWORD`)

武器/物理技能；目标：被动；最高等级 3。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Smith Two-handed Sword (`BS_TWOHANDSWORD`)

武器/物理技能；目标：被动；最高等级 3。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Smith Axe (`BS_AXE`)

武器/物理技能；目标：被动；最高等级 3。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Smith Mace (`BS_MACE`)

武器/物理技能；目标：被动；最高等级 3。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Smith Knucklebrace (`BS_KNUCKLE`)

武器/物理技能；目标：被动；最高等级 3。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Smith Spear (`BS_SPEAR`)

武器/物理技能；目标：被动；最高等级 3。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Hilt Binding (`BS_HILTBINDING`)

武器/物理技能；目标：被动；最高等级 1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:3804
wd->damage2 = battle_addmastery(sd,target,wd->damage2,1);
// src/map/battle.cpp:3812
if(skill_id == TF_POISON) //Additional ATK from Envenom is treated as mastery type damage [helvetica]
// src/map/battle.cpp:3813
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, 15 * skill_lv);
// src/map/battle.cpp:3819
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, battle_get_spiritball_damage(*wd, *src, skill_id));
// src/map/battle.cpp:3822
ATK_ADD(wd->damage, wd->damage2, 3 * skill);
// src/map/battle.cpp:5715
wd.damage = 0;
// src/map/battle.cpp:5724
ATK_ADD(wd.damage, wd.damage2, skill * 2);
// src/map/battle.cpp:5726
ATK_ADD(wd.damage, wd.damage2, 50 * skill_lv);
// src/map/battle.cpp:5728
ATK_ADD(wd.damage, wd.damage2, 4);
// src/map/battle.cpp:5735
wd.damage = wd.damage * (100 + sd->bonus.long_attack_atk_rate) / 100;
// src/map/battle.cpp:5737
wd.damage2 = wd.damage2 * (100 + sd->bonus.long_attack_atk_rate) / 100;
// src/map/status.cpp:4355
if(battle_config.hp_rate != 100)
// src/map/status.cpp:4356
base_status->max_hp = (uint32)(battle_config.hp_rate * (base_status->max_hp/100.));
// src/map/status.cpp:11593
map_session_data * s_sd = BL_CAST(BL_PC, src);
// src/map/status.cpp:11603
val3 = (val2) ? 300 : 200; // Aspd increase
// src/map/status.cpp:11606
tick += tick / 10; //If caster has Hilt Binding, duration increases by 10%
```

### Ore Discovery (`BS_FINDINGORE`)

武器/物理技能；目标：被动；最高等级 1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/mob.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/mob.cpp:3346
if (first_sd != nullptr && entry->rate <= battle_config.rare_drop_announce) {
// src/map/mob.cpp:3348
sprintf(message, msg_txt(nullptr, 541), first_sd->status.name, md->name, it->ename.c_str(), (float)drop_rate / 100);
// src/map/mob.cpp:3350
intif_broadcast(message, strlen(message) + 1, BC_DEFAULT);
// src/map/mob.cpp:3354
mob_item_drop(md, dlist, ditem, 0, battle_config.autoloot_adjust ? drop_rate : entry->rate, homkillonly || merckillonly);
// src/map/mob.cpp:3364
mobdrop->rate = entry->adj_rate;
// src/map/mob.cpp:3368
mob_item_drop(md, dlist, ditem, 0, mobdrop->rate, homkillonly || merckillonly);
```

### Weaponry Research (`BS_WEAPONRESEARCH`)

武器/物理技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:2298
damage += (skill * 10);
// src/map/battle.cpp:2300
damage += (15 * pc_checkskill(sd, NC_MADOLICENCE)); // Attack bonus is granted even without the Madogear
// src/map/battle.cpp:2303
damage += (skill * 4);
// src/map/battle.cpp:2305
damage += sd->status.str;
// src/map/battle.cpp:2311
damage += (skill * 2);
// src/map/battle.cpp:2315
damage += 15 * skill + (skill > 4 ? 25 : 0);
// src/map/battle.cpp:3295
skill->impl->modifyHitRate(hitrate, src, target, skill_lv);
// src/map/battle.cpp:3297
} else if (sd && wd->type&DMG_MULTI_HIT && wd->div_ == 2) // +1 hit per level of Double Attack on a successful double attack (making sure other multi attack skills do not trigger this) [helvetica]
// src/map/battle.cpp:3298
hitrate += pc_checkskill(sd,TF_DOUBLE);
// src/map/battle.cpp:3305
hitrate += hitrate * ( 2 * skill ) / 100;
// src/map/battle.cpp:3309
hitrate += 3 * skill;
// src/map/battle.cpp:3312
hitrate = cap_value(hitrate, battle_config.min_hitrate, battle_config.max_hitrate);
// src/map/battle.cpp:3315
hitrate += 20; //Rapid Smiting gives a flat +20 hit after the hitrate was capped
// src/map/battle.cpp:5711
wd.damage = sce->val3 * skill_lv / 10;
// src/map/battle.cpp:5715
wd.damage = 0;
// src/map/battle.cpp:5724
ATK_ADD(wd.damage, wd.damage2, skill * 2);
```

### Weapon Repair (`BS_REPAIRWEAPON`)

武器/物理技能；目标：友方目标；最高等级 1；射程：2；命中类型：Single；段数：1；吟唱：7500 ms；伤害标记：NoDamage；消耗/限制：SP 30。

- 覆盖：`exact-class-methods`
- 实现类：`SkillWeaponRepair`
- 实现文件：`src/map/skills/merchant/weaponrepair.cpp`

#### `SkillWeaponRepair::SkillWeaponRepair`

来源：`src/map/skills/merchant/weaponrepair.cpp:9-10`

```cpp
SkillWeaponRepair::SkillWeaponRepair() : SkillImpl(BS_REPAIRWEAPON) {
}
```

#### `SkillWeaponRepair::castendNoDamageId`

来源：`src/map/skills/merchant/weaponrepair.cpp:12-18`

```cpp
void SkillWeaponRepair::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if(sd && dstsd)
		clif_item_repair_list( *sd, *dstsd, skill_lv );
}
```

### Skin Tempering (`BS_SKINTEMPER`)

武器/物理技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
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
// src/map/status.cpp:4673
sd->sprecov_rate = 0;
// src/map/status.cpp:4683
uint8 dragon_matk = skill * 2;
```

### Hammer Fall (`BS_HAMMERFALL`)

武器/物理技能；目标：地面区域；最高等级 5；射程：1；命中类型：Single；段数：1；范围：Lv1-5=2; Lv6=12；持续时间2：5000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 10；武器 Dagger, 1hSword, 1hAxe, 2hAxe, Mace；关联状态：Stun。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHammerFall`
- 实现文件：`src/map/skills/merchant/hammerfall.cpp`

#### `SkillHammerFall::SkillHammerFall`

来源：`src/map/skills/merchant/hammerfall.cpp:6-7`

```cpp
SkillHammerFall::SkillHammerFall() : SkillImpl(BS_HAMMERFALL) {
}
```

#### `SkillHammerFall::castendNoDamageId`

来源：`src/map/skills/merchant/hammerfall.cpp:9-11`

```cpp
void SkillHammerFall::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_addtimerskill(src, tick+1000, target->id, 0, 0, getSkillId(), skill_lv, min(20+10*skill_lv, 50+5*skill_lv), flag);
}
```

#### `SkillHammerFall::castendPos2`

来源：`src/map/skills/merchant/hammerfall.cpp:13-19`

```cpp
void SkillHammerFall::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	int32 i = skill_get_splash(getSkillId(), skill_lv);
	map_foreachinallarea(skill_area_sub,
		src->m, x-i, y-i, x+i, y+i, BL_CHAR,
		src, getSkillId(), skill_lv, tick, flag|BCT_ENEMY|2,
		skill_castend_nodamage_id);
}
```

### Adrenaline Rush (`BS_ADRENALINE`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=20; Lv2=23; Lv3=26; Lv4=29; Lv5=32；武器 1hAxe, 2hAxe, Mace；关联状态：Adrenaline。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAdrenalineRush`
- 实现文件：`src/map/skills/merchant/adrenalinerush.cpp`

#### `SkillAdrenalineRush::SkillAdrenalineRush`

来源：`src/map/skills/merchant/adrenalinerush.cpp:10-11`

```cpp
SkillAdrenalineRush::SkillAdrenalineRush() : SkillImpl(BS_ADRENALINE) {
}
```

#### `SkillAdrenalineRush::castendNoDamageId`

来源：`src/map/skills/merchant/adrenalinerush.cpp:13-29`

```cpp
void SkillAdrenalineRush::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if (sd == nullptr || sd->status.party_id == 0 || (flag & 1)) {
		int32 weapontype = skill_get_weapontype(getSkillId());
		if (!weapontype || !dstsd || pc_check_weapontype(dstsd, weapontype)) {
			clif_skill_nodamage(target, *target, getSkillId(), skill_lv,
				sc_start2(src, target, skill_get_sc(getSkillId()), 100, skill_lv, (src == target) ? 1 : 0, skill_get_time(getSkillId(), skill_lv)));
		}
	} else if (sd) {
		party_foreachsamemap(skill_area_sub,
			sd,skill_get_splash(getSkillId(), skill_lv),
			src,getSkillId(),skill_lv,tick, flag|BCT_PARTY|1,
			skill_castend_nodamage_id);
	}
}
```

### Weapon Perfection (`BS_WEAPONPERFECT`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；持续时间1：Lv1=10000; Lv2=20000; Lv3=30000; Lv4=40000; Lv5=50000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=18; Lv2=16; Lv3=14; Lv4=12; Lv5=10；关联状态：WeaponPerfection。

- 覆盖：`exact-class-methods`
- 实现类：`SkillWeaponPerfection`
- 实现文件：`src/map/skills/merchant/weaponperfection.cpp`

#### `SkillWeaponPerfection::SkillWeaponPerfection`

来源：`src/map/skills/merchant/weaponperfection.cpp:10-11`

```cpp
SkillWeaponPerfection::SkillWeaponPerfection() : SkillImpl(BS_WEAPONPERFECT) {
}
```

#### `SkillWeaponPerfection::castendNoDamageId`

来源：`src/map/skills/merchant/weaponperfection.cpp:13-29`

```cpp
void SkillWeaponPerfection::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if (sd == nullptr || sd->status.party_id == 0 || (flag & 1)) {
		int32 weapontype = skill_get_weapontype(getSkillId());
		if (!weapontype || !dstsd || pc_check_weapontype(dstsd, weapontype)) {
			clif_skill_nodamage(target, *target, getSkillId(), skill_lv,
				sc_start2(src, target, skill_get_sc(getSkillId()), 100, skill_lv, (src == target) ? 1 : 0, skill_get_time(getSkillId(), skill_lv)));
		}
	} else if (sd) {
		party_foreachsamemap(skill_area_sub,
			sd,skill_get_splash(getSkillId(), skill_lv),
			src,getSkillId(),skill_lv,tick, flag|BCT_PARTY|1,
			skill_castend_nodamage_id);
	}
}
```

### Power-Thrust (`BS_OVERTHRUST`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；范围：-1；持续时间1：Lv1=20000; Lv2=40000; Lv3=60000; Lv4=80000; Lv5=100000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP Lv1=18; Lv2=16; Lv3=14; Lv4=12; Lv5=10；武器 Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Bow, Knuckle, Musical, Whip, Book, Katar, Revolver, Rifle, Gatling, Shotgun, Grenade, Huuma, 2hStaff；关联状态：Overthrust。

- 覆盖：`exact-class-methods`
- 实现类：`SkillPowerThrust`
- 实现文件：`src/map/skills/merchant/powerthrust.cpp`

#### `SkillPowerThrust::SkillPowerThrust`

来源：`src/map/skills/merchant/powerthrust.cpp:10-11`

```cpp
SkillPowerThrust::SkillPowerThrust() : SkillImpl(BS_OVERTHRUST) {
}
```

#### `SkillPowerThrust::castendNoDamageId`

来源：`src/map/skills/merchant/powerthrust.cpp:13-29`

```cpp
void SkillPowerThrust::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if (sd == nullptr || sd->status.party_id == 0 || (flag & 1)) {
		int32 weapontype = skill_get_weapontype(getSkillId());
		if (!weapontype || !dstsd || pc_check_weapontype(dstsd, weapontype)) {
			clif_skill_nodamage(target, *target, getSkillId(), skill_lv,
				sc_start2(src, target, skill_get_sc(getSkillId()), 100, skill_lv, (src == target) ? 1 : 0, skill_get_time(getSkillId(), skill_lv)));
		}
	} else if (sd) {
		party_foreachsamemap(skill_area_sub,
			sd,skill_get_splash(getSkillId(), skill_lv),
			src,getSkillId(),skill_lv,tick, flag|BCT_PARTY|1,
			skill_castend_nodamage_id);
	}
}
```

### Maximize Power (`BS_MAXIMIZE`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；持续时间1：Lv1=1000; Lv2=2000; Lv3=3000; Lv4=4000; Lv5=5000 ms；伤害标记：NoDamage；消耗/限制：SP 10；关联状态：MaximizePower。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skills/merchant/skill_factory_merchant.cpp:214
case CR_ACIDDEMONSTRATION:
// src/map/skills/merchant/skill_factory_merchant.cpp:215
return std::make_unique<SkillAcidDemonstration>();
```

### Unfair Trick (`BS_UNFAIRLYTRICK`)

武器/物理技能；目标：被动；最高等级 1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Greed (`BS_GREED`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；范围：2；技能后摇：1000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 10。

- 覆盖：`exact-class-methods`
- 实现类：`SkillGreed`
- 实现文件：`src/map/skills/merchant/greed.cpp`

#### `SkillGreed::SkillGreed`

来源：`src/map/skills/merchant/greed.cpp:9-10`

```cpp
SkillGreed::SkillGreed() : SkillImpl(BS_GREED) {
}
```

#### `SkillGreed::castendNoDamageId`

来源：`src/map/skills/merchant/greed.cpp:12-20`

```cpp
void SkillGreed::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);

	if(sd){
		clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
		map_foreachinallrange(skill_greed,target,
			skill_get_splash(getSkillId(), skill_lv),BL_ITEM,target);
	}
}
```

### Advanced Adrenaline Rush (`BS_ADRENALINE2`)

武器/物理技能；目标：自身；最高等级 1；命中类型：Single；段数：1；范围：-1；持续时间1：150000 ms；伤害标记：NoDamage, Splash；消耗/限制：SP 64；武器 Fist, Dagger, 1hSword, 2hSword, 1hSpear, 2hSpear, 1hAxe, 2hAxe, Mace, 2hMace, Staff, Knuckle, Musical, Whip, Book, Katar；关联状态：Adrenaline2。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAdvancedAdrenalineRush`
- 实现文件：`src/map/skills/merchant/advancedadrenalinerush.cpp`

#### `SkillAdvancedAdrenalineRush::SkillAdvancedAdrenalineRush`

来源：`src/map/skills/merchant/advancedadrenalinerush.cpp:10-11`

```cpp
SkillAdvancedAdrenalineRush::SkillAdvancedAdrenalineRush() : SkillImpl(BS_ADRENALINE2) {
}
```

#### `SkillAdvancedAdrenalineRush::castendNoDamageId`

来源：`src/map/skills/merchant/advancedadrenalinerush.cpp:13-29`

```cpp
void SkillAdvancedAdrenalineRush::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	map_session_data* dstsd = BL_CAST(BL_PC, target);

	if (sd == nullptr || sd->status.party_id == 0 || (flag & 1)) {
		int32 weapontype = skill_get_weapontype(getSkillId());
		if (!weapontype || !dstsd || pc_check_weapontype(dstsd, weapontype)) {
			clif_skill_nodamage(target, *target, getSkillId(), skill_lv,
				sc_start2(src, target, skill_get_sc(getSkillId()), 100, skill_lv, (src == target) ? 1 : 0, skill_get_time(getSkillId(), skill_lv)));
		}
	} else if (sd) {
		party_foreachsamemap(skill_area_sub,
			sd,skill_get_splash(getSkillId(), skill_lv),
			src,getSkillId(),skill_lv,tick, flag|BCT_PARTY|1,
			skill_castend_nodamage_id);
	}
}
```
