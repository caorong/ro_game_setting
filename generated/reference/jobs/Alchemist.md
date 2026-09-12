# Alchemist 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Alchemist` 公式页](../skill-formulas/Alchemist.md)

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Novice | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Novice | 否 | — | None / Self |
| 410 | `WE_CALLBABY` | Call Baby | 1 | Novice | 否 | — | None / Self |
| 36 | `MC_INCCARRY` | Enlarge Weight Limit | 10 | Merchant | 否 | — | None / Passive |
| 37 | `MC_DISCOUNT` | Discount | 10 | Merchant | 否 | MC_INCCARRY Lv3 | None / Passive |
| 38 | `MC_OVERCHARGE` | Overcharge | 10 | Merchant | 否 | MC_DISCOUNT Lv3 | None / Passive |
| 39 | `MC_PUSHCART` | Pushcart | 10 | Merchant | 否 | MC_INCCARRY Lv5 | None / Passive |
| 40 | `MC_IDENTIFY` | Item Appraisal | 1 | Merchant | 否 | — | None / Self |
| 41 | `MC_VENDING` | Vending | 10 | Merchant | 否 | MC_PUSHCART Lv3 | None / Self |
| 42 | `MC_MAMMONITE` | Mammonite | 10 | Merchant | 否 | — | Weapon / Attack |
| 153 | `MC_CARTREVOLUTION` | Cart Revolution | 1 | Merchant | 否 | — | Weapon / Attack |
| 154 | `MC_CHANGECART` | Change Cart | 1 | Merchant | 否 | — | None / Self |
| 155 | `MC_LOUD` | Crazy Uproar | 1 | Merchant | 否 | — | Weapon / Self |
| 2535 | `ALL_BUYING_STORE` | Open Buying Store | 1 | Merchant | 否 | MC_VENDING Lv1 | None / Self |
| 2544 | `MC_CARTDECORATE` | Decorate Cart | 1 | Merchant | 否 | — | None / Self |
| 226 | `AM_AXEMASTERY` | Axe Mastery | 10 | Alchemist | 是 | — | Weapon / Passive |
| 227 | `AM_LEARNINGPOTION` | Potion Research | 10 | Alchemist | 是 | — | None / Passive |
| 228 | `AM_PHARMACY` | Prepare Potion | 10 | Alchemist | 是 | AM_LEARNINGPOTION Lv5 | None / Self |
| 229 | `AM_DEMONSTRATION` | Bomb | 5 | Alchemist | 是 | AM_PHARMACY Lv4 | Weapon / Ground |
| 230 | `AM_ACIDTERROR` | Acid Terror | 5 | Alchemist | 是 | AM_PHARMACY Lv5 | Weapon / Attack |
| 231 | `AM_POTIONPITCHER` | Aid Potion | 5 | Alchemist | 是 | AM_PHARMACY Lv3 | None / Support |
| 232 | `AM_CANNIBALIZE` | Summon Flora | 5 | Alchemist | 是 | AM_PHARMACY Lv6 | None / Ground |
| 233 | `AM_SPHEREMINE` | Summon Marine Sphere | 5 | Alchemist | 是 | AM_PHARMACY Lv2 | None / Ground |
| 234 | `AM_CP_WEAPON` | Alchemical Weapon | 5 | Alchemist | 是 | AM_CP_ARMOR Lv3 | Weapon / Support |
| 235 | `AM_CP_SHIELD` | Synthesized Shield | 5 | Alchemist | 是 | AM_CP_HELM Lv3 | Weapon / Support |
| 236 | `AM_CP_ARMOR` | Synthetic Armor | 5 | Alchemist | 是 | AM_CP_SHIELD Lv3 | Weapon / Support |
| 237 | `AM_CP_HELM` | Biochemical Helm | 5 | Alchemist | 是 | AM_PHARMACY Lv2 | Weapon / Support |
| 238 | `AM_BIOETHICS` | Bioethics | 1 | Alchemist | 是 | — | None / Passive |
| 243 | `AM_CALLHOMUN` | Call Homunculus | 1 | Alchemist | 是 | AM_REST Lv1 | None / Self |
| 244 | `AM_REST` | Vaporize | 1 | Alchemist | 是 | AM_BIOETHICS Lv1 | None / Self |
| 247 | `AM_RESURRECTHOMUN` | Homunculus Resurrection | 5 | Alchemist | 是 | AM_CALLHOMUN Lv1 | None / Self |
| 446 | `AM_BERSERKPITCHER` | Aid Berserk Potion | 1 | Alchemist | 是 | — | None / Support |
| 496 | `AM_TWILIGHT1` | Twilight Alchemy 1 | 1 | Alchemist | 是 | AM_PHARMACY Lv10 | None / Self |
| 497 | `AM_TWILIGHT2` | Twilight Alchemy 2 | 1 | Alchemist | 是 | AM_PHARMACY Lv10 | None / Self |
| 498 | `AM_TWILIGHT3` | Twilight Alchemy 3 | 1 | Alchemist | 是 | AM_PHARMACY Lv10 | None / Self |

## 技能详情

### Axe Mastery (`AM_AXEMASTERY`)

武器/物理技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2323
damage += damage * 30 / 100;
// src/map/battle.cpp:2335
damage += (skill * 3);
// src/map/battle.cpp:2339
damage += (skill * 4);
// src/map/battle.cpp:2341
damage += skill * 10;
// src/map/battle.cpp:2345
damage += (skill * 4);
// src/map/battle.cpp:2351
damage += (skill * 4);
// src/map/battle.cpp:2353
damage += (skill * 5);
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
```

### Potion Research (`AM_LEARNINGPOTION`)

非伤害技能；目标：被动；最高等级 10。

- 技能树最高等级：`10`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/merchant/acidterror.cpp`, `src/map/skills/merchant/aidberserkpotion.cpp`, `src/map/skills/merchant/aidcondensedpotion.cpp`, `src/map/skills/merchant/aidpotion.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:10688
* Heal player HP and/or SP linearly. Calculate any bonus based on active statuses.
// src/map/pc.cpp:10691
* @param hp: HP to heal
// src/map/pc.cpp:10692
* @param sp: SP to heal
// src/map/pc.cpp:10693
* @return Amount healed to an object
// src/map/pc.cpp:10695
int32 pc_itemheal(map_session_data *sd, t_itemid itemid, int32 hp, int32 sp)
// src/map/pc.cpp:10699
if (hp) {
// src/map/pc.cpp:10705
bonus += bonus; // Receive an additional +100% effect from ranked potions to HP only
// src/map/pc.cpp:10708
bonus += sd->bonus.itemhealrate2;
// src/map/pc.cpp:10710
bonus += bonus * pc_get_itemgroup_bonus(sd, itemid, sd->itemgrouphealrate) / 100;
// src/map/pc.cpp:10712
for(const auto &it : sd->itemhealrate) {
// src/map/pc.cpp:10719
if (sd->sc.getSCE(SC_INCHEALRATE))
// src/map/pc.cpp:10720
bonus += bonus * sd->sc.getSCE(SC_INCHEALRATE)->val1 / 100;
```

### Prepare Potion (`AM_PHARMACY`)

非伤害技能；目标：自身；最高等级 10；命中类型：Single；伤害标记：NoDamage；消耗/限制：SP 5；道具 Medicine_Bowl×1。

- 技能树最高等级：`10`
- 前置技能：AM_LEARNINGPOTION Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/preparepotion.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:9351
switch( sd.menuskill_id ) { // Cast start or cast end??
// src/map/skill.cpp:12965
case AM_PHARMACY: // Potion Preparation - reviewed with the help of various Ragnainfo sources [DracoRPG]
// src/map/skill.cpp:13177
qty = 7 + skill_lv;
// src/map/skill.cpp:13179
qty = 10 + skill_lv;
// src/map/skill.cpp:13436
case ASC_CDP: //25% Damage yourself, and display same effect as failed potion.
// src/map/skill.cpp:13437
status_percent_damage(nullptr, sd, -25, 0, true);
// src/map/skills/merchant/preparepotion.cpp:12
void SkillPreparePotion::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/preparepotion.cpp:13
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/preparepotion.cpp:17
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
// src/map/skills/merchant/skill_factory_merchant.cpp:136
case AM_DEMONSTRATION:
```

### Bomb (`AM_DEMONSTRATION`)

武器/物理技能；目标：地面区域；最高等级 5；射程：9；命中类型：Single；段数：1；属性：Fire；吟唱：1000 ms；持续时间1：Lv1=40000; Lv2=45000; Lv3=50000; Lv4=55000; Lv5=60000 ms；伤害标记：NoDamage, IgnoreAtkCard；消耗/限制：SP 10；道具 Fire_Bottle×1。

- 技能树最高等级：`5`
- 前置技能：AM_PHARMACY Lv4
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/merchant/bomb.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:2671
static int32 battle_range_type(const block_list* src, const block_list* target, uint16 skill_id, uint16 skill_lv)
// src/map/battle.cpp:2679
case AM_DEMONSTRATION:
// src/map/skill.cpp:1262
{ // These statuses would be applied anyway even if the damage was blocked by some skills. [Inkfish]
// src/map/skill.cpp:1263
if( skill_id != WS_CARTTERMINATION && skill_id != AM_DEMONSTRATION && skill_id != CR_REFLECTSHIELD && skill_id != MS_REFLECTSHIELD && skill_id != GN_HELLS_PLANT_ATK
// src/map/skill.cpp:1270
int32 rate = it.rate;
// src/map/skill.cpp:1272
rate += it.arrow_rate;
// src/map/skill.cpp:1273
if( !rate )
// src/map/skill.cpp:3456
if( skill_id == AM_DEMONSTRATION && bl->type == BL_MOB && ((TBL_MOB*)bl)->mob_id == MOBID_EMPERIUM )
// src/map/skill.cpp:3457
return 0; //Allow casting Bomb/Demonstration Right under emperium [Skotlex]
// src/map/skill.cpp:3462
* Used to check range condition of the casted skill. Used if the skill has UF_NOFOOTSET or INF2_DISABLENEARNPC
// src/map/skill.cpp:3463
* @param bl Object that casted skill
// src/map/skill.cpp:3466
* @param skill_id The casted skill
```

### Acid Terror (`AM_ACIDTERROR`)

武器/物理技能；目标：敌方目标；最高等级 5；射程：9；命中类型：Single；段数：1；吟唱：1000 ms；持续时间1：Lv1=3; Lv2=7; Lv3=10; Lv4=12; Lv5=13 ms；持续时间2：120000 ms；伤害标记：IgnoreAtkCard, IgnoreDefense, IgnoreFlee；消耗/限制：SP 15；道具 Acid_Bottle×1；关联状态：Bleeding。

- 技能树最高等级：`5`
- 前置技能：AM_PHARMACY Lv5
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/battle.cpp`, `src/map/skill.cpp`, `src/map/skills/merchant/acidterror.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/battle.cpp:4220
ATK_ADDRATE(wd->damage, wd->damage2, dmg_bonus);
// src/map/battle.cpp:4221
RE_ALLATK_ADDRATE(wd, dmg_bonus);
// src/map/battle.cpp:4226
if (tsd != nullptr && tsd->bonus.crit_def_rate != 0 && !skill_id && (bflag & BDMG_CRIT)) {
// src/map/battle.cpp:4227
ATK_ADDRATE(wd->damage, wd->damage2, -tsd->bonus.crit_def_rate);
// src/map/battle.cpp:4231
ATK_ADD(wd->damage, wd->damage2, -tstatus->def2);
// src/map/battle.cpp:4238
#define DAMAGE_DIV_FIX(dmg, div) { if ((div) < 0) { (div) *= -1; (dmg) /= (div); } (dmg) *= (div); }
// src/map/battle.cpp:4239
#define DAMAGE_DIV_FIX2(dmg, div) { if ((div) > 1) (dmg) *= div; }
// src/map/battle.cpp:4242
* Applies DAMAGE_DIV_FIX and checks for min damage
// src/map/skill.cpp:1313
if (skill_id != it.skill_id || !it.rate)
// src/map/skill.cpp:1317
status_change_start(src, bl, it.sc, it.rate, 7, 0, 0, 0, it.duration, SCSTART_NONE, 100);
// src/map/skill.cpp:1319
status_change_start(src, src, it.sc, it.rate, 7, 0, 0, 0, it.duration, SCSTART_NONE, 100);
// src/map/skill.cpp:1323
sc_start2(src,bl,SC_BLEEDING,(skill_lv*3),skill_lv,src->id,skill_get_time2(skill_id,skill_lv));
```

### Aid Potion (`AM_POTIONPITCHER`)

非伤害技能；目标：友方目标；最高等级 5；射程：9；命中类型：Single；段数：1；技能后摇：500 ms；伤害标记：NoDamage；消耗/限制：SP 1；道具 Red_Potion×1, Orange_Potion×1, Yellow_Potion×1, White_Potion×1, Blue_Potion×1, Fruit_Of_Mastela×1, Royal_Jelly×1, Seed_Of_Yggdrasil×1, Yggdrasilberry×1, Berserk_Potion×1。

- 技能树最高等级：`5`
- 前置技能：AM_PHARMACY Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/merchant/aidberserkpotion.cpp`, `src/map/skills/merchant/aidcondensedpotion.cpp`, `src/map/skills/merchant/aidpotion.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:9607
int32 pc_skillheal_bonus(map_session_data *sd, uint16 skill_id) {
// src/map/pc.cpp:9608
int32 bonus = sd->bonus.add_heal_rate;
// src/map/pc.cpp:9616
case AL_HEAL:           if( !(battle_config.skill_add_heal_rate&1) ) bonus = 0; break;
// src/map/pc.cpp:9617
case PR_SANCTUARY:      if( !(battle_config.skill_add_heal_rate&2) ) bonus = 0; break;
// src/map/pc.cpp:9618
case AM_POTIONPITCHER:  if( !(battle_config.skill_add_heal_rate&4) ) bonus = 0; break;
// src/map/pc.cpp:9619
case CR_SLIMPITCHER:    if( !(battle_config.skill_add_heal_rate&8) ) bonus = 0; break;
// src/map/pc.cpp:9620
case BA_APPLEIDUN:      if( !(battle_config.skill_add_heal_rate&16)) bonus = 0; break;
// src/map/pc.cpp:9621
case AB_CHEAL:          if (!(battle_config.skill_add_heal_rate & 32)) bonus = 0; break;
// src/map/pc.cpp:9622
case AB_HIGHNESSHEAL:   if (!(battle_config.skill_add_heal_rate & 64)) bonus = 0; break;
// src/map/pc.cpp:9623
case CD_MEDIALE_VOTUM:  if (!(battle_config.skill_add_heal_rate & 128)) bonus = 0; break;
// src/map/pc.cpp:9624
case CD_DILECTIO_HEAL:  if (!(battle_config.skill_add_heal_rate & 256)) bonus = 0; break;
// src/map/pc.cpp:9628
for (auto &it : sd->skillheal) {
```

### Summon Flora (`AM_CANNIBALIZE`)

非伤害技能；目标：地面区域；最高等级 5；射程：4；命中类型：Single；段数：1；吟唱：2000 ms；技能后摇：500 ms；持续时间1：Lv1=300000; Lv2=240000; Lv3=180000; Lv4=120000; Lv5=60000 ms；伤害标记：NoDamage；消耗/限制：SP 20；道具 MenEater_Plant_Bottle×1。

- 技能树最高等级：`5`
- 前置技能：AM_PHARMACY Lv6
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/hellsplant.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/skills/merchant/summonflora.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:9389
skill_check_pc_partner(&sd, skill_id, &skill_lv, 1, 1);
// src/map/skill.cpp:9395
int32 maxcount = (skill_id==AM_CANNIBALIZE)? 6-skill_lv : skill_get_maxcount(skill_id,skill_lv);
// src/map/skill.cpp:9396
int32 mob_class = (skill_id==AM_CANNIBALIZE)? summons[skill_lv-1] :MOBID_MARINE_SPHERE;
// src/map/skills/merchant/hellsplant.cpp:16
SkillHellsPlantAttack::SkillHellsPlantAttack() : SkillImplRecursiveDamageSplash(GN_HELLS_PLANT_ATK) {
// src/map/skills/merchant/hellsplant.cpp:19
void SkillHellsPlantAttack::applyAdditionalEffects(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32 attack_type, enum damage_lv dmg_lv) const {
// src/map/skills/merchant/hellsplant.cpp:20
sc_start(src,target, SC_STUN,  20 + 10 * skill_lv, skill_lv, skill_get_time(getSkillId(), skill_lv));
// src/map/skills/merchant/hellsplant.cpp:21
sc_start2(src,target, SC_BLEEDING, 5 + 5 * skill_lv, skill_lv, src->id,skill_get_time(getSkillId(), skill_lv));
// src/map/skills/merchant/hellsplant.cpp:24
void SkillHellsPlantAttack::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &skillratio, int32 mflag) const {
// src/map/skills/merchant/hellsplant.cpp:26
const map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/hellsplant.cpp:28
skillratio += -100 + 100 * skill_lv + sstatus->int_ * (sd ? pc_checkskill(sd, AM_CANNIBALIZE) : 5); // !TODO: Confirm INT and Cannibalize bonus
// src/map/skills/merchant/skill_factory_merchant.cpp:136
case AM_DEMONSTRATION:
// src/map/skills/merchant/summonflora.cpp:11
void SkillSummonFlora::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
```

### Summon Marine Sphere (`AM_SPHEREMINE`)

非伤害技能；目标：地面区域；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：2000 ms；技能后摇：500 ms；持续时间1：30000 ms；伤害标记：NoDamage；消耗/限制：SP 10；道具 Mini_Bottle×1。

- 技能树最高等级：`5`
- 前置技能：AM_PHARMACY Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/skills/merchant/summonmarinesphere.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:9389
skill_check_pc_partner(&sd, skill_id, &skill_lv, 1, 1);
// src/map/skill.cpp:9395
int32 maxcount = (skill_id==AM_CANNIBALIZE)? 6-skill_lv : skill_get_maxcount(skill_id,skill_lv);
// src/map/skill.cpp:9396
int32 mob_class = (skill_id==AM_CANNIBALIZE)? summons[skill_lv-1] :MOBID_MARINE_SPHERE;
// src/map/skills/merchant/skill_factory_merchant.cpp:136
case AM_DEMONSTRATION:
// src/map/skills/merchant/summonmarinesphere.cpp:11
void SkillSummonMarineSphere::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/status.cpp:2921
if (flag&16 && mbl) { // Max HP setting from Summon Flora/marine Sphere
// src/map/status.cpp:2932
status->max_hp = 2000 + 400*ud->skill_lv;
// src/map/status.cpp:2935
status->max_hp = 3000 + 3000 * ud->skill_lv;
// src/map/status.cpp:2938
status->max_hp = 1500 + 200*ud->skill_lv + 10*status_get_lv(mbl);
// src/map/status.cpp:2939
status->mode = static_cast<e_mode>(status->mode|MD_CANATTACK|MD_AGGRESSIVE);
```

### Alchemical Weapon (`AM_CP_WEAPON`)

武器/物理技能；目标：友方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：Lv1=120000; Lv2=240000; Lv3=360000; Lv4=480000; Lv5=600000 ms；伤害标记：NoDamage；消耗/限制：SP 30；道具 Coating_Bottle×1；关联状态：Cp_Weapon。

- 技能树最高等级：`5`
- 前置技能：AM_CP_ARMOR Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/alchemicalweapon.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/alchemicalweapon.cpp:13
void SkillAlchemicalWeapon::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/alchemicalweapon.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/alchemicalweapon.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/merchant/alchemicalweapon.cpp:22
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
// src/map/skills/merchant/skill_factory_merchant.cpp:136
case AM_DEMONSTRATION:
```

### Synthesized Shield (`AM_CP_SHIELD`)

武器/物理技能；目标：友方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：Lv1=120000; Lv2=240000; Lv3=360000; Lv4=480000; Lv5=600000 ms；伤害标记：NoDamage；消耗/限制：SP 25；道具 Coating_Bottle×1；关联状态：Cp_Shield。

- 技能树最高等级：`5`
- 前置技能：AM_CP_HELM Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/skills/merchant/synthesizedshield.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/skill_factory_merchant.cpp:136
case AM_DEMONSTRATION:
// src/map/skills/merchant/synthesizedshield.cpp:13
void SkillSynthesizedShield::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/synthesizedshield.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/synthesizedshield.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/merchant/synthesizedshield.cpp:22
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
```

### Synthetic Armor (`AM_CP_ARMOR`)

武器/物理技能；目标：友方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：Lv1=120000; Lv2=240000; Lv3=360000; Lv4=480000; Lv5=600000 ms；伤害标记：NoDamage；消耗/限制：SP 25；道具 Coating_Bottle×1；关联状态：Cp_Armor。

- 技能树最高等级：`5`
- 前置技能：AM_CP_SHIELD Lv3
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/skills/merchant/syntheticarmor.cpp`, `src/map/status.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/skill_factory_merchant.cpp:136
case AM_DEMONSTRATION:
// src/map/skills/merchant/syntheticarmor.cpp:13
void SkillSyntheticArmor::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/syntheticarmor.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/syntheticarmor.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/merchant/syntheticarmor.cpp:22
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
// src/map/status.cpp:15335
void status_change_clear_buffs(block_list* bl, uint8 type)
// src/map/status.cpp:15337
status_change *sc= status_get_sc(bl);
// src/map/status.cpp:15344
sc_type status = static_cast<sc_type>(it.first);
```

### Biochemical Helm (`AM_CP_HELM`)

武器/物理技能；目标：友方目标；最高等级 5；射程：1；命中类型：Single；段数：1；吟唱：2000 ms；持续时间1：Lv1=120000; Lv2=240000; Lv3=360000; Lv4=480000; Lv5=600000 ms；伤害标记：NoDamage；消耗/限制：SP 25；道具 Coating_Bottle×1；关联状态：Cp_Helm。

- 技能树最高等级：`5`
- 前置技能：AM_PHARMACY Lv2
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/biochemicalhelm.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/biochemicalhelm.cpp:13
void SkillBiochemicalHelm::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/biochemicalhelm.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/biochemicalhelm.cpp:15
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/merchant/biochemicalhelm.cpp:22
clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
// src/map/skills/merchant/skill_factory_merchant.cpp:136
case AM_DEMONSTRATION:
```

### Bioethics (`AM_BIOETHICS`)

非伤害技能；目标：被动；最高等级 1。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`core-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:12779
pc_checkskill(sd,j) < skill_produce_db[i].req_skill_lv)
// src/map/skill.cpp:12780
continue; // must iterate again to check other skills that produce it. [malufett]
```

### Call Homunculus (`AM_CALLHOMUN`)

非伤害技能；目标：自身；最高等级 1；范围：1；伤害标记：NoDamage；消耗/限制：SP 10；道具 Germination_Breed×1。

- 技能树最高等级：`1`
- 前置技能：AM_REST Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/pc.cpp`, `src/map/skill.cpp`, `src/map/skills/merchant/callhomunculus.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/pc.cpp:9472
status_change_end(sd, SC_SPRITEMABLE);
// src/map/pc.cpp:9474
status_change_end(sd, SC_SOULATTACK);
// src/map/pc.cpp:11047
status_change_end(sd, SC_SPRITEMABLE);
// src/map/pc.cpp:11049
status_change_end(sd, SC_SOULATTACK);
// src/map/pc.cpp:11051
status_change_end( sd, SC_SPIRIT );
// src/map/skill.cpp:8699
if (status->sp == status->max_sp)
// src/map/skill.cpp:8700
return false; //Unusable when at full SP.
// src/map/skill.cpp:8703
if (status->hp < 30 * status->max_hp / 100) {
// src/map/skill.cpp:8714
case AM_REST: //Can't vapo homun if you don't have an active homunc or it's hp is < 80%
// src/map/skill.cpp:8715
if (!hom_is_active(sd.hd) || sd.hd->battle_status.hp < (sd.hd->battle_status.max_hp*80/100)) {
// src/map/skill.cpp:9886
if (i != skill_lv%11 - 1)
// src/map/skill.cpp:9914
if( itemdb_group.item_exists(IG_GEMSTONE, skill->require.itemid[i]) && (sd->special_state.no_gemstone == 2 || skill_check_pc_partner(sd,skill_id,&skill_lv, 1, 2)) )
```

### Vaporize (`AM_REST`)

非伤害技能；目标：自身；最高等级 1；伤害标记：NoDamage；消耗/限制：SP 50。

- 技能树最高等级：`1`
- 前置技能：AM_BIOETHICS Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/skills/merchant/vaporize.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:8703
if (status->hp < 30 * status->max_hp / 100) {
// src/map/skill.cpp:8714
case AM_REST: //Can't vapo homun if you don't have an active homunc or it's hp is < 80%
// src/map/skill.cpp:8715
if (!hom_is_active(sd.hd) || sd.hd->battle_status.hp < (sd.hd->battle_status.max_hp*80/100)) {
// src/map/skills/merchant/skill_factory_merchant.cpp:136
case AM_DEMONSTRATION:
// src/map/skills/merchant/vaporize.cpp:13
void SkillVaporize::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/vaporize.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/vaporize.cpp:18
clif_skill_nodamage(src, *target, getSkillId(), skill_lv);
```

### Homunculus Resurrection (`AM_RESURRECTHOMUN`)

非伤害技能；目标：自身；最高等级 5；命中类型：Single；范围：1；吟唱：2000 ms；伤害标记：NoDamage；消耗/限制：SP Lv1=74; Lv2=68; Lv3=62; Lv4=56; Lv5=50。

- 技能树最高等级：`5`
- 前置技能：AM_CALLHOMUN Lv1
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/homunculusresurrection.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:4964
int32 splash = skill_get_splash(ud->skill_id, ud->skill_lv);
// src/map/skill.cpp:4972
return skill_castend_pos(tid,tick,id,data);
// src/map/skills/merchant/homunculusresurrection.cpp:13
void SkillHomunculusResurrection::castendPos2(block_list* src, int32 x, int32 y, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/homunculusresurrection.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/homunculusresurrection.cpp:18
if (!hom_ressurect(sd, 20*skill_lv, x, y))
// src/map/skills/merchant/skill_factory_merchant.cpp:136
case AM_DEMONSTRATION:
```

### Aid Berserk Potion (`AM_BERSERKPITCHER`)

非伤害技能；目标：友方目标；最高等级 1；射程：9；命中类型：Single；段数：1；技能后摇：500 ms；伤害标记：NoDamage；消耗/限制：SP 10；SP% 8；道具 Berserk_Potion×2。

- 技能树最高等级：`1`
- 前置技能：—
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skills/merchant/aidberserkpotion.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skills/merchant/aidberserkpotion.cpp:16
void SkillAidBerserkPotion::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/aidberserkpotion.cpp:17
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/aidberserkpotion.cpp:19
map_session_data* dstsd = BL_CAST(BL_PC, target);
// src/map/skills/merchant/aidberserkpotion.cpp:20
mob_data* dstmd = BL_CAST(BL_MOB, target);
// src/map/skills/merchant/aidberserkpotion.cpp:22
status_change* tsc = status_get_sc(target);
// src/map/skills/merchant/aidberserkpotion.cpp:24
int32 j,hp = 0,sp = 0;
```

### Twilight Alchemy 1 (`AM_TWILIGHT1`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；吟唱：3000 ms；技能后摇：10000 ms；伤害标记：NoDamage；消耗/限制：SP 200；道具 Medicine_Bowl×200。

- 技能树最高等级：`1`
- 前置技能：AM_PHARMACY Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/skills/merchant/twilightalchemy1.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:9351
switch( sd.menuskill_id ) { // Cast start or cast end??
// src/map/skill.cpp:12965
case AM_PHARMACY: // Potion Preparation - reviewed with the help of various Ragnainfo sources [DracoRPG]
// src/map/skill.cpp:13436
case ASC_CDP: //25% Damage yourself, and display same effect as failed potion.
// src/map/skill.cpp:13437
status_percent_damage(nullptr, sd, -25, 0, true);
// src/map/skills/merchant/skill_factory_merchant.cpp:136
case AM_DEMONSTRATION:
// src/map/skills/merchant/twilightalchemy1.cpp:13
void SkillTwilightAlchemy1::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/twilightalchemy1.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/twilightalchemy1.cpp:17
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
```

### Twilight Alchemy 2 (`AM_TWILIGHT2`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；吟唱：3000 ms；技能后摇：10000 ms；伤害标记：NoDamage；消耗/限制：SP 200；道具 Medicine_Bowl×200。

- 技能树最高等级：`1`
- 前置技能：AM_PHARMACY Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/skills/merchant/twilightalchemy2.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:8622
if (!party_skill_check(&sd, sd.status.party_id, skill_id, skill_lv)) {
// src/map/skill.cpp:9351
switch( sd.menuskill_id ) { // Cast start or cast end??
// src/map/skill.cpp:12965
case AM_PHARMACY: // Potion Preparation - reviewed with the help of various Ragnainfo sources [DracoRPG]
// src/map/skill.cpp:13436
case ASC_CDP: //25% Damage yourself, and display same effect as failed potion.
// src/map/skill.cpp:13437
status_percent_damage(nullptr, sd, -25, 0, true);
// src/map/skills/merchant/twilightalchemy2.cpp:13
void SkillTwilightAlchemy2::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/twilightalchemy2.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
// src/map/skills/merchant/twilightalchemy2.cpp:17
clif_skill_nodamage(src,*target,getSkillId(),skill_lv);
```

### Twilight Alchemy 3 (`AM_TWILIGHT3`)

非伤害技能；目标：自身；最高等级 1；命中类型：Single；吟唱：3000 ms；技能后摇：10000 ms；伤害标记：NoDamage；消耗/限制：SP 200；道具 Medicine_Bowl×200。

- 技能树最高等级：`1`
- 前置技能：AM_PHARMACY Lv10
- 公式覆盖：`dedicated-source` / `source-indexed`
- 实现文件：`src/map/skill.cpp`, `src/map/skills/merchant/skill_factory_merchant.cpp`, `src/map/skills/merchant/twilightalchemy3.cpp`

公式/效果候选源码（保持原始 C++ 表达式）：

```cpp
// src/map/skill.cpp:8622
if (!party_skill_check(&sd, sd.status.party_id, skill_id, skill_lv)) {
// src/map/skill.cpp:9351
switch( sd.menuskill_id ) { // Cast start or cast end??
// src/map/skill.cpp:12965
case AM_PHARMACY: // Potion Preparation - reviewed with the help of various Ragnainfo sources [DracoRPG]
// src/map/skill.cpp:13436
case ASC_CDP: //25% Damage yourself, and display same effect as failed potion.
// src/map/skill.cpp:13437
status_percent_damage(nullptr, sd, -25, 0, true);
// src/map/skills/merchant/twilightalchemy3.cpp:13
void SkillTwilightAlchemy3::castendNoDamageId(block_list* src, block_list* target, uint16 skill_lv, t_tick tick, int32& flag) const {
// src/map/skills/merchant/twilightalchemy3.cpp:14
map_session_data* sd = BL_CAST(BL_PC, src);
```
