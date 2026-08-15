# 07. 魔法伤害管线

## 7.1 MATK 随机值

```text
MATK_MIN = INT + floor(INT / 7)^2
MATK_MAX = INT + floor(INT / 5)^2
```

普通魔法从区间取随机 MATK，再进入技能倍率。

## 7.2 通用管线

```text
1. 计算 MATK 随机值
2. 技能自身基础倍率 / 额外固定项
3. 技能增伤、装备增伤、卡片增伤
4. MDEF 忽略与穿透
5. Hard MDEF 百分比减伤
6. Soft MDEF 固定减伤
7. 最低伤害与技能例外
8. 属性倍率
9. 种族、阶级、Boss、技能专属与最终修正
10. 段数、范围分摊与显示
```

## 7.3 默认 MDEF 公式

在未启用替代 `magic_defense_type` 时：

```text
DamageAfterMDEF = floor(Damage * (100 - HardMDEF) / 100) - SoftMDEF
```

其中：

```text
SoftMDEF = INT + floor(VIT / 2) + bonuses
```

MDEF 忽略会在这之前修改有效 Hard MDEF。

## 7.4 属性和地面技能

法术属性可能来自：

- 技能固定属性；
- 技能等级；
- 当前状态或元素领域；
- 技能实现中的强制属性；
- 特殊技能先利用某属性、再把最终伤害视为另一属性。

地面技能还涉及单位持续时间、触发周期、每格命中、叠放限制和施法者死亡/换图后的清理。

## 7.5 特殊公式

以下技能类别常常不走纯 MATK 倍率：

- 固定伤害；
- 当前 HP / MaxHP 参与；
- 物理与魔法混合；
- 按目标数量分摊；
- 无视 MDEF 或强制 1 点；
- 复合属性或多阶段攻击。

因此“所有技能公式”必须索引技能源码，不能只读取 `skill_db.yml`。
