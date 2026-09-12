# Baby_Sage 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Baby_Sage` 公式页](../skill-formulas/Baby_Sage.md)

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Baby | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Baby | 否 | — | None / Self |
| 408 | `WE_BABY` | Baby | 1 | Baby | 否 | — | None / Self |
| 409 | `WE_CALLPARENT` | Call Parent | 1 | Baby | 否 | — | None / Self |
| 9 | `MG_SRECOVERY` | Increase SP Recovery | 10 | Mage | 否 | — | None / Passive |
| 10 | `MG_SIGHT` | Sight | 1 | Mage | 否 | — | Magic / Self |
| 11 | `MG_NAPALMBEAT` | Napalm Beat | 10 | Mage | 否 | — | Magic / Attack |
| 12 | `MG_SAFETYWALL` | Safety Wall | 10 | Mage | 否 | MG_NAPALMBEAT Lv7, MG_SOULSTRIKE Lv5 | Magic / Ground |
| 13 | `MG_SOULSTRIKE` | Soul Strike | 10 | Mage | 否 | MG_NAPALMBEAT Lv4 | Magic / Attack |
| 14 | `MG_COLDBOLT` | Cold Bolt | 10 | Mage | 否 | — | Magic / Attack |
| 15 | `MG_FROSTDIVER` | Frost Diver | 10 | Mage | 否 | MG_COLDBOLT Lv5 | Magic / Attack |
| 16 | `MG_STONECURSE` | Stone Curse | 10 | Mage | 否 | — | Magic / Attack |
| 17 | `MG_FIREBALL` | Fire Ball | 10 | Mage | 否 | MG_FIREBOLT Lv4 | Magic / Attack |
| 18 | `MG_FIREWALL` | Fire Wall | 10 | Mage | 否 | MG_FIREBALL Lv5, MG_SIGHT Lv1 | Magic / Ground |
| 19 | `MG_FIREBOLT` | Fire Bolt | 10 | Mage | 否 | — | Magic / Attack |
| 20 | `MG_LIGHTNINGBOLT` | Lightning Bolt | 10 | Mage | 否 | — | Magic / Attack |
| 21 | `MG_THUNDERSTORM` | Thunderstorm | 10 | Mage | 否 | MG_LIGHTNINGBOLT Lv4 | Magic / Ground |
| 157 | `MG_ENERGYCOAT` | Energy Coat | 1 | Mage | 否 | — | Magic / Self |
| 93 | `WZ_ESTIMATION` | Sense | 1 | Sage | 否 | — | Magic / Attack |
| 90 | `WZ_EARTHSPIKE` | Earth Spike | 5 | Sage | 否 | SA_SEISMICWEAPON Lv1 | Magic / Attack |
| 91 | `WZ_HEAVENDRIVE` | Heaven's Drive | 5 | Sage | 否 | WZ_EARTHSPIKE Lv1 | Magic / Ground |
| 274 | `SA_ADVANCEDBOOK` | Study | 10 | Sage | 否 | — | Weapon / Passive |
| 275 | `SA_CASTCANCEL` | Cast Cancel | 5 | Sage | 否 | SA_ADVANCEDBOOK Lv2 | Magic / Self |
| 276 | `SA_MAGICROD` | Magic Rod | 5 | Sage | 否 | SA_ADVANCEDBOOK Lv4 | Magic / Self |
| 277 | `SA_SPELLBREAKER` | Spell Breaker | 5 | Sage | 否 | SA_MAGICROD Lv1 | Magic / Attack |
| 278 | `SA_FREECAST` | Free Cast | 10 | Sage | 否 | SA_CASTCANCEL Lv1 | Magic / Passive |
| 279 | `SA_AUTOSPELL` | Hindsight | 10 | Sage | 否 | SA_FREECAST Lv4 | Magic / Self |
| 280 | `SA_FLAMELAUNCHER` | Endow Blaze | 5 | Sage | 否 | MG_FIREBOLT Lv1, SA_ADVANCEDBOOK Lv5 | Magic / Support |
| 281 | `SA_FROSTWEAPON` | Endow Tsunami | 5 | Sage | 否 | MG_COLDBOLT Lv1, SA_ADVANCEDBOOK Lv5 | Magic / Support |
| 282 | `SA_LIGHTNINGLOADER` | Endow Tornado | 5 | Sage | 否 | MG_LIGHTNINGBOLT Lv1, SA_ADVANCEDBOOK Lv5 | Magic / Support |
| 283 | `SA_SEISMICWEAPON` | Endow Quake | 5 | Sage | 否 | MG_STONECURSE Lv1, SA_ADVANCEDBOOK Lv5 | Magic / Support |
| 284 | `SA_DRAGONOLOGY` | Dragonology | 5 | Sage | 否 | SA_ADVANCEDBOOK Lv9 | Weapon / Passive |
| 285 | `SA_VOLCANO` | Volcano | 5 | Sage | 否 | SA_FLAMELAUNCHER Lv2 | Magic / Ground |
| 286 | `SA_DELUGE` | Deluge | 5 | Sage | 否 | SA_FROSTWEAPON Lv2 | Magic / Ground |
| 287 | `SA_VIOLENTGALE` | Whirlwind | 5 | Sage | 否 | SA_LIGHTNINGLOADER Lv2 | Magic / Ground |
| 288 | `SA_LANDPROTECTOR` | Magnetic Earth | 5 | Sage | 否 | SA_VOLCANO Lv3, SA_DELUGE Lv3, SA_VIOLENTGALE Lv3 | Magic / Ground |
| 289 | `SA_DISPELL` | Dispell | 5 | Sage | 否 | SA_SPELLBREAKER Lv3 | Magic / Attack |
| 290 | `SA_ABRACADABRA` | Hocus-pocus | 10 | Sage | 否 | SA_AUTOSPELL Lv5, SA_DISPELL Lv1, SA_LANDPROTECTOR Lv1 | Magic / Self |
| 1007 | `SA_CREATECON` | Create Elemental Converter | 1 | Sage | 否 | — | None / Self |
| 1008 | `SA_ELEMENTWATER` | Elemental Change Water | 1 | Sage | 否 | — | Magic / Attack |
| 1017 | `SA_ELEMENTGROUND` | Elemental Change Earth | 1 | Sage | 否 | — | Magic / Attack |
| 1018 | `SA_ELEMENTFIRE` | Elemental Change Fire | 1 | Sage | 否 | — | Magic / Attack |
| 1019 | `SA_ELEMENTWIND` | Elemental Change Wind | 1 | Sage | 否 | — | Magic / Attack |

## 技能详情
