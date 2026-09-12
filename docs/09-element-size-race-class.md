# 09. 属性、体型、种族与阶级

## 9.1 十种防御属性

```text
Neutral, Water, Earth, Fire, Wind,
Poison, Holy, Dark, Ghost, Undead
```

防御属性还有等级 1～4。完整 4×10×10 矩阵见：

```text
data/tables/element_modifiers.yml
```

## 9.2 属性倍率

```text
DamageAfterElement = trunc(Damage * ModifierPercent / 100)
```

矩阵允许 0 和负值。默认 `attribute_recover=no`，负倍率如何落地还取决于调用路径和服务器配置，不能简单解释成“必定吸收回血”。

## 9.3 攻击属性来源

物理攻击可能来自：

```text
武器属性
弹药属性
属性附魔
技能强制属性
状态覆盖
特殊技能实现
```

魔法和 Misc 技能各有独立取属性函数。

## 9.4 体型

目标分为 Small / Medium / Large。武器体型表见：

```text
data/tables/size_modifiers.yml
```

典型值：

| 武器 | 小 | 中 | 大 |
|---|---:|---:|---:|
| Dagger | 100 | 75 | 50 |
| 1hSword | 75 | 100 | 75 |
| 2hSword | 75 | 75 | 100 |
| Spear | 75 | 75 | 100 |
| Axe | 50 | 75 | 100 |
| Bow | 100 | 100 | 75 |
| Katar | 75 | 100 | 75 |
| Knuckle | 100 | 75 | 50 |

公共表先给默认，`db/pre-re/size_fix.yml` 再覆盖拳套和鞭等值；只读覆盖文件会得到不完整结果。

## 9.5 种族、阶级与 Boss

装备脚本可按以下维度加减伤：

- Race；
- Class（普通 / Boss 等）；
- Size；
- Element；
- Range（short / long）；
- Skill ID；
- Monster ID；
- weapon/magic/misc 类型。

同类修正是相加还是分组相乘，由 `battle.cpp` 的 card-fix 分组决定。实现时不要把所有百分比简单相加。
