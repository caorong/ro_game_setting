# High_Priest 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 71 | `PR_SLOWPOISON` / Slow Poison | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 361 | `HP_ASSUMPTIO` / Assumptio | `exact-class-methods` | `SkillAssumptio` | src/map/skills/acolyte/assumptio.cpp |
| 362 | `HP_BASILICA` / Basilica | `exact-class-methods` | `SkillBasilica` | src/map/skills/acolyte/basilica.cpp |
| 363 | `HP_MEDITATIO` / Meditatio | `core-source-references` | `` | src/map/skill.cpp, src/map/status.cpp |
| 481 | `HP_MANARECHARGE` / Mana Recharge | `core-source-references` | `` | src/map/status.cpp |

## 详细公式与效果实现

### Slow Poison (`PR_SLOWPOISON`)

魔法技能；目标：友方目标；最高等级 4；射程：9；命中类型：Single；段数：1；持续时间1：Lv1=10000; Lv2=20000; Lv3=30000; Lv4=40000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=6; Lv2=8; Lv3=10; Lv4=12；关联状态：SlowPoison。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Assumptio (`HP_ASSUMPTIO`)

魔法技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；范围：1；吟唱：Lv1=1000; Lv2=1500; Lv3=2000; Lv4=2500; Lv5=3000 ms；技能后摇：Lv1=1100; Lv2=1200; Lv3=1300; Lv4=1400; Lv5=1500 ms；持续时间1：Lv1=20000; Lv2=40000; Lv3=60000; Lv4=80000; Lv5=100000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=20; Lv2=30; Lv3=40; Lv4=50; Lv5=60；关联状态：Assumptio。

- 覆盖：`exact-class-methods`
- 实现类：`SkillAssumptio`
- 实现文件：`src/map/skills/acolyte/assumptio.cpp`

#### `SkillAssumptio::SkillAssumptio`

来源：`src/map/skills/acolyte/assumptio.cpp:10-11`

```cpp
SkillAssumptio::SkillAssumptio() : StatusSkillImpl(HP_ASSUMPTIO) {
}
```

#### `SkillAssumptio::castendNoDamageId`

来源：`src/map/skills/acolyte/assumptio.cpp:13-21`

```cpp
void SkillAssumptio::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	map_session_data* sd = BL_CAST(BL_PC, src);
	mob_data* dstmd = BL_CAST(BL_MOB, target);

	if( sd && dstmd )
		clif_skill_fail( *sd, getSkillId() );
	else
		StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
}
```

### Basilica (`HP_BASILICA`)

魔法技能；目标：自身；最高等级 5；射程：4；命中类型：Single；段数：1；击退：2；吟唱：Lv1=5000; Lv2=6000; Lv3=7000; Lv4=8000; Lv5=9000 ms；技能后摇：Lv1=2000; Lv2=3000; Lv3=4000; Lv4=5000; Lv5=6000 ms；持续时间1：Lv1=20000; Lv2=25000; Lv3=30000; Lv4=35000; Lv5=40000 ms；持续时间2：Lv1=20000; Lv2=25000; Lv3=30000; Lv4=35000; Lv5=40000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=80; Lv2=90; Lv3=100; Lv4=110; Lv5=120；道具 Yellow_Gemstone×1, Red_Gemstone×1, Blue_Gemstone×1, Holy_Water×1；关联状态：Basilica。

- 覆盖：`exact-class-methods`
- 实现类：`SkillBasilica`
- 实现文件：`src/map/skills/acolyte/basilica.cpp`

#### `SkillBasilica::SkillBasilica`

来源：`src/map/skills/acolyte/basilica.cpp:13-14`

```cpp
SkillBasilica::SkillBasilica() : StatusSkillImpl(HP_BASILICA) {
}
```

#### `SkillBasilica::castendNoDamageId`

来源：`src/map/skills/acolyte/basilica.cpp:16-20`

```cpp
void SkillBasilica::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifdef RENEWAL
	StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
#endif
}
```

#### `SkillBasilica::castendPos2`

来源：`src/map/skills/acolyte/basilica.cpp:22-43`

```cpp
void SkillBasilica::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
#ifndef RENEWAL
	map_session_data* sd = BL_CAST(BL_PC, src);

	if( status_change *sc = status_get_sc(src); sc && sc->getSCE(SC_BASILICA) ) {
		status_change_end(src, SC_BASILICA); // Cancel Basilica and return so requirement isn't consumed again
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}
	if( map_getcell(src->m, x, y, CELL_CHKLANDPROTECTOR) ) {
		if (sd)
			clif_skill_fail( *sd, getSkillId(), USESKILL_FAIL );
		flag |= SKILL_NOCONSUME_REQ;
		return;
	}
	
	// Create Basilica
	skill_clear_unitgroup(src);
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
	flag|=1;
#endif
}
```

### Meditatio (`HP_MEDITATIO`)

魔法技能；目标：被动；最高等级 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/skill.cpp`, `src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/skill.cpp:540
hp = (skill_lv > 6) ? 777 : skill_lv * 100;
// src/map/skill.cpp:543
hp = (skill_lv > 6) ? 666 : skill_lv * 100;
// src/map/skill.cpp:545
case AB_HIGHNESSHEAL:
// src/map/skill.cpp:547
hp = ((status_get_int(src) + status_get_lv(src)) / 5) * 30;
// src/map/skill.cpp:552
hp = ((status_get_lv(src) + status_get_int(src)) / 8) * (4 + ((sd ? pc_checkskill(sd, AL_HEAL) : 1) * 8));
// src/map/skill.cpp:553
hp = (hp * (17 + 3 * skill_lv)) / 10;
// src/map/skill.cpp:557
hp = (status_get_lv(src) + status_get_int(src)) / 5 * 6;
// src/map/skill.cpp:560
hp = (status_get_lv(src) + status_get_int(src)) / 5 * 15;
// src/map/skill.cpp:562
case CD_MEDIALE_VOTUM:// Does the learned level of heal affect this skill?
// src/map/skill.cpp:563
case CD_DILECTIO_HEAL:// Same question for this one too. [Rytech]
// src/map/skill.cpp:565
hp = (status_get_lv(src) + status_get_int(src)) / 5 * 30;
// src/map/skill.cpp:573
hp = (500 + pc_checkskill(sd,SOA_TALISMAN_MASTERY) * 50) * skill_lv * status_get_lv(src) / 100;
// src/map/skill.cpp:574
hp += (status_get_lv(src) + status_get_int(src)) / 5 * 30 * status_get_crt(src) / 100;
// src/map/skill.cpp:578
if (skill_lv >= battle_config.max_heal_lv)
// src/map/skill.cpp:579
return battle_config.max_heal;
// src/map/skill.cpp:582
* Renewal Heal Formula
```

### Mana Recharge (`HP_MANARECHARGE`)

非伤害技能；目标：被动；最高等级 5。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:4660
sd->dsprate -= 4*skill;
// src/map/status.cpp:4663
sd->dsprate -= sc->getSCE(SC_SERVICE4U)->val3;
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
```
