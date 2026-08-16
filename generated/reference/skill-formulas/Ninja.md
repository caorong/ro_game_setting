# Ninja 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 522 | `NJ_TOBIDOUGU` / Shuriken Training | `core-source-references` | `` | src/map/battle.cpp, src/map/skills/ninja/kunaiexplosion.cpp |
| 523 | `NJ_SYURIKEN` / Throw Shuriken | `exact-class-methods` | `SkillThrowShuriken` | src/map/skills/ninja/throwshuriken.cpp |
| 524 | `NJ_KUNAI` / Throw Kunai | `exact-class-methods` | `SkillThrowKunai` | src/map/skills/ninja/throwkunai.cpp |
| 525 | `NJ_HUUMA` / Throw Huuma Shuriken | `exact-class-methods` | `SkillThrowHuumaShuriken` | src/map/skills/ninja/throwhuumashuriken.cpp |
| 526 | `NJ_ZENYNAGE` / Throw Zeny | `exact-class-methods` | `SkillThrowZeny` | src/map/skills/ninja/throwzeny.cpp |
| 527 | `NJ_TATAMIGAESHI` / Improvised Defense | `exact-class-methods` | `SkillImprovisedDefense` | src/map/skills/ninja/improviseddefense.cpp |
| 528 | `NJ_KASUMIKIRI` / Vanishing Slash | `exact-class-methods` | `SkillVanishingSlash` | src/map/skills/ninja/vanishingslash.cpp |
| 529 | `NJ_SHADOWJUMP` / Shadow Leap | `exact-class-methods` | `SkillShadowLeap` | src/map/skills/ninja/shadowleap.cpp |
| 530 | `NJ_KIRIKAGE` / Shadow Slash | `exact-class-methods` | `SkillShadowSlash` | src/map/skills/ninja/shadowslash.cpp |
| 531 | `NJ_UTSUSEMI` / Cicada Skin Sheeding | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 532 | `NJ_BUNSINJYUTSU` / Mirror Image | `exact-class-methods` | `SkillMirrorImage` | src/map/skills/ninja/mirrorimage.cpp |
| 533 | `NJ_NINPOU` / Spirit of the Blade | `core-source-references` | `` | src/map/status.cpp |
| 534 | `NJ_KOUENKA` / Crimson Fire Petal | `exact-class-methods` | `SkillCrimsonFirePetal` | src/map/skills/ninja/crimsonfirepetal.cpp |
| 535 | `NJ_KAENSIN` / Crimson Fire Formation | `exact-class-methods` | `SkillCrimsonFireFormation` | src/map/skills/ninja/crimsonfireformation.cpp |
| 536 | `NJ_BAKUENRYU` / Raging Fire Dragon | `exact-class-methods` | `SkillRagingFireDragon` | src/map/skills/ninja/ragingfiredragon.cpp |
| 537 | `NJ_HYOUSENSOU` / Spear of Ice | `exact-class-methods` | `SkillSpearOfIce` | src/map/skills/ninja/spearofice.cpp |
| 538 | `NJ_SUITON` / Hidden Water | `exact-class-methods` | `SkillHiddenWater` | src/map/skills/ninja/hiddenwater.cpp |
| 539 | `NJ_HYOUSYOURAKU` / Ice Meteor | `exact-class-methods` | `SkillIceMeteor` | src/map/skills/ninja/icemeteor.cpp |
| 540 | `NJ_HUUJIN` / Wind Blade | `exact-class-methods` | `SkillWindBlade` | src/map/skills/ninja/windblade.cpp |
| 541 | `NJ_RAIGEKISAI` / Lightning Strike of Destruction | `exact-class-methods` | `SkillLightningStrikeOfDestruction` | src/map/skills/ninja/lightningstrikeofdestruction.cpp |
| 542 | `NJ_KAMAITACHI` / Kamaitachi | `exact-class-methods` | `SkillKamaitachi` | src/map/skills/ninja/kamaitachi.cpp |
| 543 | `NJ_NEN` / Soul | `generic-or-class-mapped` | `StatusSkillImpl` |  |
| 544 | `NJ_ISSEN` / Final Strike | `exact-class-methods` | `SkillFinalStrike` | src/map/skills/ninja/finalstrike.cpp |

## 详细公式与效果实现

### Shuriken Training (`NJ_TOBIDOUGU`)

武器/物理技能；目标：被动；最高等级 10；段数：1。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/battle.cpp`, `src/map/skills/ninja/kunaiexplosion.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/battle.cpp:3716
ATK_ADD(wd->damage, wd->damage2, battle_get_spiritball_damage(*wd, *src, skill_id));
// src/map/battle.cpp:3721
ATK_ADD(wd->damage, wd->damage2, 15 * skill_lv);
// src/map/battle.cpp:3723
wd->damage = battle_attr_fix(src, target, wd->damage, right_element, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3726
ATK_ADD(wd->damage, wd->damage2, 4 * skill_lv);
// src/map/battle.cpp:3728
ATK_ADD(wd->damage, wd->damage2, 3 * pc_checkskill(sd, NJ_TOBIDOUGU));
// src/map/battle.cpp:3729
ATK_ADD(wd->damage, wd->damage2, sd->bonus.arrow_atk);
// src/map/battle.cpp:3732
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3736
ATK_ADD(wd->damage, wd->damage2, 3 * sd->bonus.arrow_atk);
// src/map/battle.cpp:3739
wd->damage = battle_attr_fix(src, target, wd->damage, ELE_NEUTRAL, tstatus->def_ele, tstatus->ele_lv, 1);
// src/map/battle.cpp:3812
if(skill_id == TF_POISON) //Additional ATK from Envenom is treated as mastery type damage [helvetica]
// src/map/battle.cpp:3813
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, 15 * skill_lv);
// src/map/battle.cpp:3819
ATK_ADD(wd->masteryAtk, wd->masteryAtk2, battle_get_spiritball_damage(*wd, *src, skill_id));
// src/map/battle.cpp:3822
ATK_ADD(wd->damage, wd->damage2, 3 * skill);
// src/map/battle.cpp:6487
md.damage /= 2;
// src/map/battle.cpp:6491
md.damage = skill_get_zeny( skill_id, skill_lv );
// src/map/battle.cpp:6493
if( md.damage == 0 ){
```

### Throw Shuriken (`NJ_SYURIKEN`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Weapon；伤害标记：IgnoreAtkCard；消耗/限制：SP 2；弹药数 1；弹药 Shuriken。

- 覆盖：`exact-class-methods`
- 实现类：`SkillThrowShuriken`
- 实现文件：`src/map/skills/ninja/throwshuriken.cpp`

#### `SkillThrowShuriken::SkillThrowShuriken`

来源：`src/map/skills/ninja/throwshuriken.cpp:8-9`

```cpp
SkillThrowShuriken::SkillThrowShuriken() : WeaponSkillImpl(NJ_SYURIKEN) {
}
```

#### `SkillThrowShuriken::calculateSkillRatio`

来源：`src/map/skills/ninja/throwshuriken.cpp:11-15`

```cpp
void SkillThrowShuriken::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 5 * skill_lv;
#endif
}
```

### Throw Kunai (`NJ_KUNAI`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：3；属性：Weapon；技能后摇：1000 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP Lv1=30; Lv2=25; Lv3=20; Lv4=15; Lv5=10；弹药数 1；弹药 Kunai。

- 覆盖：`exact-class-methods`
- 实现类：`SkillThrowKunai`
- 实现文件：`src/map/skills/ninja/throwkunai.cpp`

#### `SkillThrowKunai::SkillThrowKunai`

来源：`src/map/skills/ninja/throwkunai.cpp:8-9`

```cpp
SkillThrowKunai::SkillThrowKunai() : WeaponSkillImpl(NJ_KUNAI) {
}
```

#### `SkillThrowKunai::calculateSkillRatio`

来源：`src/map/skills/ninja/throwkunai.cpp:11-15`

```cpp
void SkillThrowKunai::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += -100 + 100 * skill_lv;
#endif
}
```

### Throw Huuma Shuriken (`NJ_HUUMA`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：Lv1-2=-3; Lv3-4=-4; Lv5=-5；属性：Weapon；范围：1；吟唱：3000 ms；技能后摇：2000 ms；伤害标记：Splash, SplashSplit；消耗/限制：SP Lv1=20; Lv2=25; Lv3=30; Lv4=35; Lv5=40；武器 Huuma。

- 覆盖：`exact-class-methods`
- 实现类：`SkillThrowHuumaShuriken`
- 实现文件：`src/map/skills/ninja/throwhuumashuriken.cpp`

#### `SkillThrowHuumaShuriken::SkillThrowHuumaShuriken`

来源：`src/map/skills/ninja/throwhuumashuriken.cpp:10-11`

```cpp
SkillThrowHuumaShuriken::SkillThrowHuumaShuriken() : SkillImplRecursiveDamageSplash(NJ_HUUMA) {
}
```

#### `SkillThrowHuumaShuriken::calculateSkillRatio`

来源：`src/map/skills/ninja/throwhuumashuriken.cpp:13-19`

```cpp
void SkillThrowHuumaShuriken::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += -150 + 250 * skill_lv;
#else
	base_skillratio += 50 + 150 * skill_lv;
#endif
}
```

#### `SkillThrowHuumaShuriken::splashSearch`

来源：`src/map/skills/ninja/throwhuumashuriken.cpp:21-26`

```cpp
void SkillThrowHuumaShuriken::splashSearch(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 flag) const {
#ifdef RENEWAL
	clif_skill_damage( *src, *target,tick, status_get_amotion(src), 0, DMGVAL_IGNORE, 1, getSkillId(), skill_lv, DMG_SINGLE );
#endif
	SkillImplRecursiveDamageSplash::splashSearch(src, target, skill_lv, tick, flag);
}
```

### Throw Zeny (`NJ_ZENYNAGE`)

特殊技能；目标：敌方目标；最高等级 10；射程：7；命中类型：Single；段数：1；技能后摇：5000 ms；伤害标记：IgnoreElement, IgnoreFlee；消耗/限制：SP 50；Zeny Lv1=500; Lv2=1000; Lv3=1500; Lv4=2000; Lv5=2500; Lv6=3000; Lv7=3500; Lv8=4000; Lv9=4500; Lv10=5000。

- 覆盖：`exact-class-methods`
- 实现类：`SkillThrowZeny`
- 实现文件：`src/map/skills/ninja/throwzeny.cpp`

#### `SkillThrowZeny::SkillThrowZeny`

来源：`src/map/skills/ninja/throwzeny.cpp:6-7`

```cpp
SkillThrowZeny::SkillThrowZeny() : SkillImpl(NJ_ZENYNAGE) {
}
```

#### `SkillThrowZeny::castendDamageId`

来源：`src/map/skills/ninja/throwzeny.cpp:9-11`

```cpp
void SkillThrowZeny::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_attack(skill_get_type(getSkillId()),src,src,target,getSkillId(),skill_lv,tick,flag);
}
```

### Improvised Defense (`NJ_TATAMIGAESHI`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；属性：Weapon；击退：3；技能后摇：3000 ms；持续时间1：3000 ms；持续时间2：3000 ms；伤害标记：IgnoreAtkCard；消耗/限制：SP 15；关联状态：Tatamigaeshi。

- 覆盖：`exact-class-methods`
- 实现类：`SkillImprovisedDefense`
- 实现文件：`src/map/skills/ninja/improviseddefense.cpp`

#### `SkillImprovisedDefense::SkillImprovisedDefense`

来源：`src/map/skills/ninja/improviseddefense.cpp:10-11`

```cpp
SkillImprovisedDefense::SkillImprovisedDefense() : SkillImpl(NJ_TATAMIGAESHI) {
}
```

#### `SkillImprovisedDefense::calculateSkillRatio`

来源：`src/map/skills/ninja/improviseddefense.cpp:13-18`

```cpp
void SkillImprovisedDefense::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += 10 * skill_lv;
#ifdef RENEWAL
	base_skillratio *= 2;
#endif
}
```

#### `SkillImprovisedDefense::castendPos2`

来源：`src/map/skills/ninja/improviseddefense.cpp:20-23`

```cpp
void SkillImprovisedDefense::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	if (skill_unitsetting(src,getSkillId(),skill_lv,src->x,src->y,0))
		sc_start(src,src,skill_get_sc(getSkillId()),100,skill_lv,skill_get_time2(getSkillId(),skill_lv));
}
```

### Vanishing Slash (`NJ_KASUMIKIRI`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-1；命中类型：Single；段数：1；属性：Weapon；技能后摇：1000 ms；持续时间1：Lv1=30000; Lv2=60000; Lv3=90000; Lv4=120000; Lv5=150000; Lv6=180000; Lv7=210000; Lv8=240000; Lv9=270000; Lv10=300000 ms；消耗/限制：SP Lv1=10; Lv2=12; Lv3=14; Lv4=16; Lv5=18; Lv6=20; Lv7=22; Lv8=24; Lv9=26; Lv10=28；关联状态：Hiding。

- 覆盖：`exact-class-methods`
- 实现类：`SkillVanishingSlash`
- 实现文件：`src/map/skills/ninja/vanishingslash.cpp`

#### `SkillVanishingSlash::SkillVanishingSlash`

来源：`src/map/skills/ninja/vanishingslash.cpp:10-11`

```cpp
SkillVanishingSlash::SkillVanishingSlash() : WeaponSkillImpl(NJ_KASUMIKIRI) {
}
```

#### `SkillVanishingSlash::applyAdditionalEffects`

来源：`src/map/skills/ninja/vanishingslash.cpp:13-15`

```cpp
void SkillVanishingSlash::applyAdditionalEffects(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src, src, skill_get_sc(getSkillId()), 100, skill_lv, skill_get_time(getSkillId(), skill_lv));
}
```

#### `SkillVanishingSlash::calculateSkillRatio`

来源：`src/map/skills/ninja/vanishingslash.cpp:17-23`

```cpp
void SkillVanishingSlash::calculateSkillRatio(const Damage* wd, const block_list* src, const block_list* target, uint16 skill_lv, int32& base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += 20 * skill_lv;
#else
	base_skillratio += 10 * skill_lv;
#endif
}
```

### Shadow Leap (`NJ_SHADOWJUMP`)

非伤害技能；目标：地面区域；最高等级 5；射程：Lv1=5; Lv2=6; Lv3=7; Lv4=8; Lv5=9；命中类型：Single；段数：1；技能后摇：1000 ms；伤害标记：NoDamage；消耗/限制：SP 10；前置状态 Hiding。

- 覆盖：`exact-class-methods`
- 实现类：`SkillShadowLeap`
- 实现文件：`src/map/skills/ninja/shadowleap.cpp`

#### `SkillShadowLeap::SkillShadowLeap`

来源：`src/map/skills/ninja/shadowleap.cpp:10-11`

```cpp
SkillShadowLeap::SkillShadowLeap() : SkillImpl(NJ_SHADOWJUMP) {
}
```

#### `SkillShadowLeap::castendPos2`

来源：`src/map/skills/ninja/shadowleap.cpp:13-17`

```cpp
void SkillShadowLeap::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	if( map_getcell(src->m,x,y,CELL_CHKREACH) && skill_check_unit_movepos(5, src, x, y, 1, 0) ) //You don't move on GVG grounds.
		clif_blown(src);
	status_change_end(src, SC_HIDING);
}
```

### Shadow Slash (`NJ_KIRIKAGE`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：Lv1=5; Lv2=6; Lv3=7; Lv4=8; Lv5=9；命中类型：Single；段数：1；属性：Weapon；伤害标记：Critical；消耗/限制：SP Lv1=14; Lv2=16; Lv3=18; Lv4=20; Lv5=22；前置状态 Hiding。

- 覆盖：`exact-class-methods`
- 实现类：`SkillShadowSlash`
- 实现文件：`src/map/skills/ninja/shadowslash.cpp`

#### `SkillShadowSlash::SkillShadowSlash`

来源：`src/map/skills/ninja/shadowslash.cpp:13-14`

```cpp
SkillShadowSlash::SkillShadowSlash() : WeaponSkillImpl(NJ_KIRIKAGE) {
}
```

#### `SkillShadowSlash::calculateSkillRatio`

来源：`src/map/skills/ninja/shadowslash.cpp:16-22`

```cpp
void SkillShadowSlash::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
#ifdef RENEWAL
	base_skillratio += -50 + 150 * skill_lv;
#else
	base_skillratio += 100 * (skill_lv - 1);
#endif
}
```

#### `SkillShadowSlash::castendDamageId`

来源：`src/map/skills/ninja/shadowslash.cpp:24-36`

```cpp
void SkillShadowSlash::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	if( !map_flag_gvg2(src->m) && !map_getmapflag(src->m, MF_BATTLEGROUND) )
	{	//You don't move on GVG grounds.
		int16 x, y;
		map_search_freecell(target, 0, &x, &y, 1, 1, 0);
		if (unit_movepos(src, x, y, 0, 0)) {
			clif_blown(src);
		}
	}
	status_change_end(src, SC_HIDING);

	WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, flag);
}
```

### Cicada Skin Sheeding (`NJ_UTSUSEMI`)

非伤害技能；目标：自身；最高等级 5；命中类型：Single；段数：1；击退：7；技能后摇：1000 ms；持续时间1：Lv1=20000; Lv2=30000; Lv3=40000; Lv4=50000; Lv5=60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=12; Lv2=15; Lv3=18; Lv4=21; Lv5=24；关联状态：Utsusemi。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:11724
val3=skill_get_blewcount(NJ_UTSUSEMI, val1); // knockback value.
// src/map/status.cpp:11735
tick /= 5; // !TODO: Reduce skill's duration. But for how long?
```

### Mirror Image (`NJ_BUNSINJYUTSU`)

魔法技能；目标：自身；最高等级 10；命中类型：Single；段数：1；吟唱：Lv1=4000; Lv2=3500; Lv3=3000; Lv4=2500; Lv5=2000; Lv6=1500; Lv7-10=1000 ms；技能后摇：1000 ms；持续时间1：Lv1=60000; Lv2=80000; Lv3=100000; Lv4=120000; Lv5=140000; Lv6=160000; Lv7=180000; Lv8=200000; Lv9=220000; Lv10=240000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=30; Lv2=32; Lv3=34; Lv4=36; Lv5=38; Lv6=40; Lv7=42; Lv8=44; Lv9=46; Lv10=48；道具 Shadow_Orb×1；关联状态：Bunsinjyutsu。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMirrorImage`
- 实现文件：`src/map/skills/ninja/mirrorimage.cpp`

#### `SkillMirrorImage::SkillMirrorImage`

来源：`src/map/skills/ninja/mirrorimage.cpp:8-9`

```cpp
SkillMirrorImage::SkillMirrorImage() : StatusSkillImpl(NJ_BUNSINJYUTSU) {
}
```

#### `SkillMirrorImage::castendNoDamageId`

来源：`src/map/skills/ninja/mirrorimage.cpp:11-16`

```cpp
void SkillMirrorImage::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	// TODO: refactor into status.yml
	status_change_end(target, SC_BUNSINJYUTSU); // on official recasting cancels existing mirror image [helvetica]
	StatusSkillImpl::castendNoDamageId(src, target, skill_lv, tick, flag);
	status_change_end(target, SC_NEN);
}
```

### Spirit of the Blade (`NJ_NINPOU`)

非伤害技能；目标：被动；最高等级 10；消耗/限制：SP 10。

- 覆盖：`core-source-references`
- 实现类：`N/A`
- 实现文件：`src/map/status.cpp`

精确源码候选（该技能没有独立实现类）：

```cpp
// src/map/status.cpp:5307
sregen->hp = cap_value(val, 0, SHRT_MAX);
// src/map/status.cpp:5322
sregen->sp = cap_value(val, 0, SHRT_MAX);
```

### Crimson Fire Petal (`NJ_KOUENKA`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2=2; Lv3=3; Lv4=4; Lv5=5; Lv6=6; Lv7=7; Lv8=8; Lv9=9; Lv10=10；属性：Fire；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；消耗/限制：SP Lv1=18; Lv2=20; Lv3=22; Lv4=24; Lv5=26; Lv6=28; Lv7=30; Lv8=32; Lv9=34; Lv10=36。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCrimsonFirePetal`
- 实现文件：`src/map/skills/ninja/crimsonfirepetal.cpp`

#### `SkillCrimsonFirePetal::SkillCrimsonFirePetal`

来源：`src/map/skills/ninja/crimsonfirepetal.cpp:8-9`

```cpp
SkillCrimsonFirePetal::SkillCrimsonFirePetal() : SkillImpl(NJ_KOUENKA) {
}
```

#### `SkillCrimsonFirePetal::calculateSkillRatio`

来源：`src/map/skills/ninja/crimsonfirepetal.cpp:11-17`

```cpp
void SkillCrimsonFirePetal::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const map_session_data* sd = BL_CAST(BL_PC, src);

	base_skillratio -= 10;
	if(sd && sd->spiritcharm_type == CHARM_TYPE_FIRE && sd->spiritcharm > 0)
		base_skillratio += 10 * sd->spiritcharm;
}
```

#### `SkillCrimsonFirePetal::castendDamageId`

来源：`src/map/skills/ninja/crimsonfirepetal.cpp:19-21`

```cpp
void SkillCrimsonFirePetal::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

### Crimson Fire Formation (`NJ_KAENSIN`)

魔法技能；目标：自身；最高等级 10；命中类型：Multi_Hit；段数：1；属性：Fire；吟唱：Lv1=6000; Lv2=5500; Lv3=5000; Lv4=4500; Lv5=4000; Lv6=3500; Lv7=3000; Lv8=2500; Lv9=2000; Lv10=1500 ms；技能后摇：1000 ms；持续时间1：20000 ms；消耗/限制：SP 25；道具 Flame_Stone×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillCrimsonFireFormation`
- 实现文件：`src/map/skills/ninja/crimsonfireformation.cpp`

#### `SkillCrimsonFireFormation::SkillCrimsonFireFormation`

来源：`src/map/skills/ninja/crimsonfireformation.cpp:8-9`

```cpp
SkillCrimsonFireFormation::SkillCrimsonFireFormation() : SkillImpl(NJ_KAENSIN) {
}
```

#### `SkillCrimsonFireFormation::calculateSkillRatio`

来源：`src/map/skills/ninja/crimsonfireformation.cpp:11-17`

```cpp
void SkillCrimsonFireFormation::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const map_session_data* sd = BL_CAST(BL_PC, src);

	base_skillratio -= 50;
	if(sd && sd->spiritcharm_type == CHARM_TYPE_FIRE && sd->spiritcharm > 0)
		base_skillratio += 20 * sd->spiritcharm;
}
```

#### `SkillCrimsonFireFormation::castendPos2`

来源：`src/map/skills/ninja/crimsonfireformation.cpp:19-22`

```cpp
void SkillCrimsonFireFormation::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Raging Fire Dragon (`NJ_BAKUENRYU`)

魔法技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Multi_Hit；段数：-3；属性：Fire；吟唱：3000 ms；技能后摇：2000 ms；持续时间1：100 ms；消耗/限制：SP Lv1=20; Lv2=25; Lv3=30; Lv4=35; Lv5=40；道具 Flame_Stone×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillRagingFireDragon`
- 实现文件：`src/map/skills/ninja/ragingfiredragon.cpp`

#### `SkillRagingFireDragon::SkillRagingFireDragon`

来源：`src/map/skills/ninja/ragingfiredragon.cpp:9-10`

```cpp
SkillRagingFireDragon::SkillRagingFireDragon() : SkillImpl(NJ_BAKUENRYU) {
}
```

#### `SkillRagingFireDragon::calculateSkillRatio`

来源：`src/map/skills/ninja/ragingfiredragon.cpp:12-18`

```cpp
void SkillRagingFireDragon::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const map_session_data* sd = BL_CAST(BL_PC, src);

	base_skillratio += 50 + 150 * skill_lv;
	if(sd && sd->spiritcharm_type == CHARM_TYPE_FIRE && sd->spiritcharm > 0)
		base_skillratio += 100 * sd->spiritcharm;
}
```

#### `SkillRagingFireDragon::castendDamageId`

来源：`src/map/skills/ninja/ragingfiredragon.cpp:20-24`

```cpp
void SkillRagingFireDragon::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Place units around target
	clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
	skill_unitsetting(src, getSkillId(), skill_lv, target->x, target->y, 0);
}
```

#### `SkillRagingFireDragon::castendPos2`

来源：`src/map/skills/ninja/ragingfiredragon.cpp:26-29`

```cpp
void SkillRagingFireDragon::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Spear of Ice (`NJ_HYOUSENSOU`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=3; Lv2=4; Lv3=5; Lv4=6; Lv5=7; Lv6=8; Lv7=9; Lv8=10; Lv9=11; Lv10=12；属性：Water；吟唱：Lv1=700; Lv2=1400; Lv3=2100; Lv4=2800; Lv5=3500; Lv6=4200; Lv7=4900; Lv8=5600; Lv9=6300; Lv10=7000 ms；消耗/限制：SP Lv1=15; Lv2=18; Lv3=21; Lv4=24; Lv5=27; Lv6=30; Lv7=33; Lv8=36; Lv9=39; Lv10=42。

- 覆盖：`exact-class-methods`
- 实现类：`SkillSpearOfIce`
- 实现文件：`src/map/skills/ninja/spearofice.cpp`

#### `SkillSpearOfIce::SkillSpearOfIce`

来源：`src/map/skills/ninja/spearofice.cpp:11-12`

```cpp
SkillSpearOfIce::SkillSpearOfIce() : SkillImpl(NJ_HYOUSENSOU) {
}
```

#### `SkillSpearOfIce::calculateSkillRatio`

来源：`src/map/skills/ninja/spearofice.cpp:14-26`

```cpp
void SkillSpearOfIce::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const map_session_data* sd = BL_CAST( BL_PC, src );

#ifdef RENEWAL
	const status_change *sc = status_get_sc(src);

	base_skillratio -= 30;
	if (sc && sc->getSCE(SC_SUITON))
		base_skillratio += 2 * skill_lv;
#endif
	if(sd && sd->spiritcharm_type == CHARM_TYPE_WATER && sd->spiritcharm > 0)
		base_skillratio += 20 * sd->spiritcharm;
}
```

#### `SkillSpearOfIce::castendDamageId`

来源：`src/map/skills/ninja/spearofice.cpp:28-30`

```cpp
void SkillSpearOfIce::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

### Hidden Water (`NJ_SUITON`)

魔法技能；目标：地面区域；最高等级 10；射程：9；命中类型：Single；段数：1；属性：Water；吟唱：3000 ms；持续时间1：Lv1=15000; Lv2=20000; Lv3=25000; Lv4=30000; Lv5=35000; Lv6=40000; Lv7=45000; Lv8=50000; Lv9=55000; Lv10=60000 ms；持续时间2：Lv1=15000; Lv2=20000; Lv3=25000; Lv4=30000; Lv5=35000; Lv6=40000; Lv7=45000; Lv8=50000; Lv9=55000; Lv10=60000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=15; Lv2=18; Lv3=21; Lv4=24; Lv5=27; Lv6=30; Lv7=33; Lv8=36; Lv9=39; Lv10=42；道具 Ice_Stone×1；关联状态：Suiton。

- 覆盖：`exact-class-methods`
- 实现类：`SkillHiddenWater`
- 实现文件：`src/map/skills/ninja/hiddenwater.cpp`

#### `SkillHiddenWater::SkillHiddenWater`

来源：`src/map/skills/ninja/hiddenwater.cpp:6-7`

```cpp
SkillHiddenWater::SkillHiddenWater() : SkillImpl(NJ_SUITON) {
}
```

#### `SkillHiddenWater::castendPos2`

来源：`src/map/skills/ninja/hiddenwater.cpp:9-14`

```cpp
void SkillHiddenWater::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Ice Meteor (`NJ_HYOUSYOURAKU`)

魔法技能；目标：自身；最高等级 5；命中类型：Single；段数：1；属性：Water；吟唱：Lv1=2000; Lv2=2500; Lv3=3000; Lv4=3500; Lv5=4000 ms；技能后摇：2000 ms；持续时间1：100 ms；持续时间2：Lv1=5000; Lv2=10000; Lv3=15000; Lv4=20000; Lv5=25000 ms；消耗/限制：SP Lv1=40; Lv2=45; Lv3=50; Lv4=55; Lv5=60；道具 Ice_Stone×1；关联状态：Freeze。

- 覆盖：`exact-class-methods`
- 实现类：`SkillIceMeteor`
- 实现文件：`src/map/skills/ninja/icemeteor.cpp`

#### `SkillIceMeteor::SkillIceMeteor`

来源：`src/map/skills/ninja/icemeteor.cpp:9-10`

```cpp
SkillIceMeteor::SkillIceMeteor() : SkillImpl(NJ_HYOUSYOURAKU) {
}
```

#### `SkillIceMeteor::applyAdditionalEffects`

来源：`src/map/skills/ninja/icemeteor.cpp:12-14`

```cpp
void SkillIceMeteor::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
	sc_start(src,target,SC_FREEZE,(10+10*skill_lv),skill_lv,skill_get_time2(getSkillId(),skill_lv));
}
```

#### `SkillIceMeteor::calculateSkillRatio`

来源：`src/map/skills/ninja/icemeteor.cpp:16-22`

```cpp
void SkillIceMeteor::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const map_session_data* sd = BL_CAST(BL_PC, src);

	base_skillratio += 50 * skill_lv;
	if(sd && sd->spiritcharm_type == CHARM_TYPE_WATER && sd->spiritcharm > 0)
		base_skillratio += 100 * sd->spiritcharm;
}
```

#### `SkillIceMeteor::castendPos2`

来源：`src/map/skills/ninja/icemeteor.cpp:24-27`

```cpp
void SkillIceMeteor::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	flag|=1;//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Wind Blade (`NJ_HUUJIN`)

魔法技能；目标：敌方目标；最高等级 10；射程：9；命中类型：Multi_Hit；段数：Lv1=1; Lv2-3=2; Lv4-5=3; Lv6-7=4; Lv8-9=5; Lv10=6；属性：Wind；吟唱：Lv1=1000; Lv2=1500; Lv3=2000; Lv4=2500; Lv5=3000; Lv6=3500; Lv7=4000; Lv8=4500; Lv9=5000; Lv10=5500 ms；技能后摇：1000 ms；消耗/限制：SP Lv1=12; Lv2=14; Lv3=16; Lv4=18; Lv5=20; Lv6=22; Lv7=24; Lv8=26; Lv9=28; Lv10=30。

- 覆盖：`exact-class-methods`
- 实现类：`SkillWindBlade`
- 实现文件：`src/map/skills/ninja/windblade.cpp`

#### `SkillWindBlade::SkillWindBlade`

来源：`src/map/skills/ninja/windblade.cpp:10-11`

```cpp
SkillWindBlade::SkillWindBlade() : SkillImpl(NJ_HUUJIN) {
}
```

#### `SkillWindBlade::calculateSkillRatio`

来源：`src/map/skills/ninja/windblade.cpp:13-21`

```cpp
void SkillWindBlade::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const map_session_data* sd = BL_CAST(BL_PC, src);

#ifdef RENEWAL
	base_skillratio += 50;
#endif
	if(sd && sd->spiritcharm_type == CHARM_TYPE_WIND && sd->spiritcharm > 0)
		base_skillratio += 10 * sd->spiritcharm;
}
```

#### `SkillWindBlade::castendDamageId`

来源：`src/map/skills/ninja/windblade.cpp:23-25`

```cpp
void SkillWindBlade::castendDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_attack(BF_MAGIC, src, src, target, getSkillId(), skill_lv, tick, flag);
}
```

### Lightning Strike of Destruction (`NJ_RAIGEKISAI`)

魔法技能；目标：自身；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Wind；吟唱：4000 ms；持续时间1：100 ms；消耗/限制：SP Lv1=16; Lv2=20; Lv3=24; Lv4=28; Lv5=32；道具 Wind_Stone×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillLightningStrikeOfDestruction`
- 实现文件：`src/map/skills/ninja/lightningstrikeofdestruction.cpp`

#### `SkillLightningStrikeOfDestruction::SkillLightningStrikeOfDestruction`

来源：`src/map/skills/ninja/lightningstrikeofdestruction.cpp:10-11`

```cpp
SkillLightningStrikeOfDestruction::SkillLightningStrikeOfDestruction() : SkillImpl(NJ_RAIGEKISAI) {
}
```

#### `SkillLightningStrikeOfDestruction::calculateSkillRatio`

来源：`src/map/skills/ninja/lightningstrikeofdestruction.cpp:13-23`

```cpp
void SkillLightningStrikeOfDestruction::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const map_session_data* sd = BL_CAST(BL_PC, src);

#ifdef RENEWAL
	base_skillratio += 100 * skill_lv;
#else
	base_skillratio += 60 + 40 * skill_lv;
#endif
	if(sd && sd->spiritcharm_type == CHARM_TYPE_WIND && sd->spiritcharm > 0)
		base_skillratio += 20 * sd->spiritcharm;
}
```

#### `SkillLightningStrikeOfDestruction::castendPos2`

来源：`src/map/skills/ninja/lightningstrikeofdestruction.cpp:25-30`

```cpp
void SkillLightningStrikeOfDestruction::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Kamaitachi (`NJ_KAMAITACHI`)

魔法技能；目标：敌方目标；最高等级 5；射程：Lv1=5; Lv2=6; Lv3=7; Lv4=8; Lv5=9；命中类型：Multi_Hit；段数：1；属性：Wind；范围：1；吟唱：4000 ms；消耗/限制：SP Lv1=24; Lv2=28; Lv3=32; Lv4=36; Lv5=40；道具 Wind_Stone×1。

- 覆盖：`exact-class-methods`
- 实现类：`SkillKamaitachi`
- 实现文件：`src/map/skills/ninja/kamaitachi.cpp`

#### `SkillKamaitachi::SkillKamaitachi`

来源：`src/map/skills/ninja/kamaitachi.cpp:10-11`

```cpp
SkillKamaitachi::SkillKamaitachi() : SkillImpl(NJ_KAMAITACHI) {
}
```

#### `SkillKamaitachi::calculateSkillRatio`

来源：`src/map/skills/ninja/kamaitachi.cpp:13-19`

```cpp
void SkillKamaitachi::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	const map_session_data* sd = BL_CAST(BL_PC, src);

	base_skillratio += 100 * skill_lv;
	if(sd && sd->spiritcharm_type == CHARM_TYPE_WIND && sd->spiritcharm > 0)
		base_skillratio += 100 * sd->spiritcharm;
}
```

#### `SkillKamaitachi::castendDamageId`

来源：`src/map/skills/ninja/kamaitachi.cpp:21-37`

```cpp
void SkillKamaitachi::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	skill_area_temp[1] = target->id;
	if (battle_config.skill_eightpath_algorithm) {
		//Use official AoE algorithm
		if (!(map_foreachindir(skill_attack_area, src->m, src->x, src->y, target->x, target->y,
		   skill_get_splash(getSkillId(), skill_lv), skill_get_maxcount(getSkillId(), skill_lv), 0, splash_target(src),
		   skill_get_type(getSkillId()), src, src, getSkillId(), skill_lv, tick, flag, BCT_ENEMY))) {

			//These skills hit at least the target if the AoE doesn't hit
			skill_attack(skill_get_type(getSkillId()), src, src, target, getSkillId(), skill_lv, tick, flag);
		}
	} else {
		map_foreachinpath(skill_attack_area, src->m, src->x, src->y, target->x, target->y,
			skill_get_splash(getSkillId(), skill_lv), skill_get_maxcount(getSkillId(), skill_lv), splash_target(src),
			skill_get_type(getSkillId()), src, src, getSkillId(), skill_lv, tick, flag, BCT_ENEMY);
	}
}
```

#### `SkillKamaitachi::castendPos2`

来源：`src/map/skills/ninja/kamaitachi.cpp:39-44`

```cpp
void SkillKamaitachi::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
	//Set flag to 1 to prevent deleting ammo (it will be deleted on group-delete).
	flag |= 1;

	skill_unitsetting(src,getSkillId(),skill_lv,x,y,0);
}
```

### Soul (`NJ_NEN`)

非伤害技能；目标：自身；最高等级 5；命中类型：Single；段数：1；吟唱：Lv1=5000; Lv2=4000; Lv3=3000; Lv4=2000; Lv5=1000 ms；持续时间1：Lv1=30000; Lv2=45000; Lv3=60000; Lv4=75000; Lv5=90000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=20; Lv2=30; Lv3=40; Lv4=50; Lv5=60；HP% -5；关联状态：Nen。

- 覆盖：`generic-or-class-mapped`
- 实现类：`StatusSkillImpl`

> 未发现独立伤害方法；该技能主要由技能数据库、状态数据库、通用技能处理或装备脚本驱动。

### Final Strike (`NJ_ISSEN`)

武器/物理技能；目标：敌方目标；最高等级 10；射程：-5；命中类型：Single；段数：1；伤害标记：IgnoreFlee；消耗/限制：SP Lv1=55; Lv2=60; Lv3=65; Lv4=70; Lv5=75; Lv6=80; Lv7=85; Lv8=90; Lv9=95; Lv10=100。

- 覆盖：`exact-class-methods`
- 实现类：`SkillFinalStrike`
- 实现文件：`src/map/skills/ninja/finalstrike.cpp`

#### `SkillFinalStrike::SkillFinalStrike`

来源：`src/map/skills/ninja/finalstrike.cpp:13-14`

```cpp
SkillFinalStrike::SkillFinalStrike() : WeaponSkillImpl(NJ_ISSEN) {
}
```

#### `SkillFinalStrike::castendDamageId`

来源：`src/map/skills/ninja/finalstrike.cpp:16-58`

```cpp
void SkillFinalStrike::castendDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 &flag) const {
	int16 x, y;
	int16 dir = map_calc_dir(src, target->x, target->y);

	int16 i = 2; // Move 2 cells (From target)

	if (dir > 0 && dir < 4)
		x = -i;
	else if (dir > 4)
		x = i;
	else
		x = 0;
	if (dir > 2 && dir < 6)
		y = -i;
	else if (dir == 7 || dir < 2)
		y = i;
	else
		y = 0;

#ifdef RENEWAL
	// Doesn't have slide effect in GVG
	if (skill_check_unit_movepos(5, src, target->x + x, target->y + y, 1, 1)) {
		clif_blown(src);
		clif_spiritball(src);
	}
	skill_attack(BF_MISC, src, src, target, getSkillId(), skill_lv, tick, flag);
	status_set_hp(src, umax(status_get_max_hp(src) / 100, 1), 0);
	status_change_end(src, SC_NEN);
	status_change_end(src, SC_HIDING);
#else
	WeaponSkillImpl::castendDamageId(src, target, skill_lv, tick, flag);

	status_set_hp(src, 1, 0);
	status_change_end(src, SC_NEN);
	status_change_end(src, SC_HIDING);

	// Doesn't have slide effect in GVG
	if (skill_check_unit_movepos(5, src, target->x + x, target->y + y, 1, 1)) {
		clif_blown(src);
		clif_spiritball(src);
	}
#endif
}
```
