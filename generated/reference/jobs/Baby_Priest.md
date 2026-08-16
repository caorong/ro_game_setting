# Baby_Priest 技能

> 规则集：Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。
> 精确公式与实现：[查看 `Baby_Priest` 公式页](../skill-formulas/Baby_Priest.md)

## 有效技能列表

| ID | 技能 | 英文名 | 最高等级 | 来源职业 | 直接学习 | 前置 | 类型 / 目标 |
|---:|---|---|---:|---|---|---|---|
| 1 | `NV_BASIC` | Basic Skill | 9 | Baby | 否 | — | None / Passive |
| 142 | `NV_FIRSTAID` | First Aid | 1 | Baby | 否 | — | None / Self |
| 408 | `WE_BABY` | Baby | 1 | Baby | 否 | — | None / Self |
| 409 | `WE_CALLPARENT` | Call Parent | 1 | Baby | 否 | — | None / Self |
| 22 | `AL_DP` | Divine Protection | 10 | Acolyte | 否 | — | Weapon / Passive |
| 23 | `AL_DEMONBANE` | Demon Bane | 10 | Acolyte | 否 | AL_DP Lv3 | Weapon / Passive |
| 24 | `AL_RUWACH` | Ruwach | 1 | Acolyte | 否 | — | Magic / Self |
| 25 | `AL_PNEUMA` | Pneuma | 1 | Acolyte | 否 | AL_WARP Lv4 | Magic / Ground |
| 26 | `AL_TELEPORT` | Teleport | 2 | Acolyte | 否 | AL_RUWACH Lv1 | Magic / Self |
| 27 | `AL_WARP` | Warp Portal | 4 | Acolyte | 否 | AL_TELEPORT Lv2 | Magic / Ground |
| 28 | `AL_HEAL` | Heal | 10 | Acolyte | 否 | — | Magic / Support |
| 29 | `AL_INCAGI` | Increase AGI | 10 | Acolyte | 否 | AL_HEAL Lv3 | Magic / Support |
| 30 | `AL_DECAGI` | Decrease AGI | 10 | Acolyte | 否 | AL_INCAGI Lv1 | Magic / Attack |
| 31 | `AL_HOLYWATER` | Aqua Benedicta | 1 | Acolyte | 否 | — | Magic / Self |
| 32 | `AL_CRUCIS` | Signum Crucis | 10 | Acolyte | 否 | AL_DEMONBANE Lv3 | Magic / Self |
| 33 | `AL_ANGELUS` | Angelus | 10 | Acolyte | 否 | AL_DP Lv3 | Magic / Self |
| 34 | `AL_BLESSING` | Blessing | 10 | Acolyte | 否 | AL_DP Lv5 | Magic / Support |
| 35 | `AL_CURE` | Cure | 1 | Acolyte | 否 | AL_HEAL Lv2 | Magic / Support |
| 156 | `AL_HOLYLIGHT` | Holy Light | 1 | Acolyte | 否 | — | Magic / Attack |
| 9 | `MG_SRECOVERY` | Increase SP Recovery | 10 | Priest | 否 | — | None / Passive |
| 12 | `MG_SAFETYWALL` | Safety Wall | 10 | Priest | 否 | PR_ASPERSIO Lv4, PR_SANCTUARY Lv3 | Magic / Ground |
| 54 | `ALL_RESURRECTION` | Resurrection | 4 | Priest | 否 | PR_STRECOVERY Lv1, MG_SRECOVERY Lv4 | Magic / Support |
| 65 | `PR_MACEMASTERY` | Mace Mastery | 10 | Priest | 否 | — | Weapon / Passive |
| 66 | `PR_IMPOSITIO` | Impositio Manus | 5 | Priest | 否 | — | Magic / Support |
| 67 | `PR_SUFFRAGIUM` | Suffragium | 3 | Priest | 否 | PR_IMPOSITIO Lv2 | Magic / Support |
| 68 | `PR_ASPERSIO` | Aspersio | 5 | Priest | 否 | AL_HOLYWATER Lv1, PR_IMPOSITIO Lv3 | Magic / Support |
| 69 | `PR_BENEDICTIO` | B.S. Sacramenti | 5 | Priest | 否 | PR_GLORIA Lv3, PR_ASPERSIO Lv5 | Magic / Ground |
| 70 | `PR_SANCTUARY` | Sanctuary | 10 | Priest | 否 | AL_HEAL Lv1 | Magic / Ground |
| 71 | `PR_SLOWPOISON` | Slow Poison | 4 | Priest | 否 | — | Magic / Support |
| 72 | `PR_STRECOVERY` | Status Recovery | 1 | Priest | 否 | — | Magic / Support |
| 73 | `PR_KYRIE` | Kyrie Eleison | 10 | Priest | 否 | AL_ANGELUS Lv2 | Magic / Support |
| 74 | `PR_MAGNIFICAT` | Magnificat | 5 | Priest | 否 | — | Magic / Self |
| 75 | `PR_GLORIA` | Gloria | 5 | Priest | 否 | PR_KYRIE Lv4, PR_MAGNIFICAT Lv3 | Magic / Self |
| 76 | `PR_LEXDIVINA` | Lex Divina | 10 | Priest | 否 | AL_RUWACH Lv1 | Magic / Attack |
| 77 | `PR_TURNUNDEAD` | Turn Undead | 10 | Priest | 否 | ALL_RESURRECTION Lv1, PR_LEXDIVINA Lv3 | Magic / Attack |
| 78 | `PR_LEXAETERNA` | Lex Aeterna | 1 | Priest | 否 | PR_LEXDIVINA Lv5 | Magic / Attack |
| 79 | `PR_MAGNUS` | Magnus Exorcismus | 10 | Priest | 否 | MG_SAFETYWALL Lv1, PR_LEXAETERNA Lv1, PR_TURNUNDEAD Lv3 | Magic / Ground |
| 1014 | `PR_REDEMPTIO` | Redemptio | 1 | Priest | 否 | — | Magic / Self |

## 技能详情
