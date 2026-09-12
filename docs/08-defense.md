# 08. DEF、MDEF 与围攻惩罚

## 8.1 物理防御的两层

- `Hard DEF`：装备防御，默认作为百分比减伤；
- `Soft DEF`：主要来自 VIT，作为防御后的固定/随机减伤。

## 8.2 玩家 Soft DEF 随机值

令 `D = SoftDEF`，玩家的经典 VIT 防御随机值可表示为：

```text
base = floor(3 * D / 10) + floor(D / 2)
span = max(0, floor(D^2 / 150) - floor(3 * D / 10) - 1)
rolled_soft_def = base + random_inclusive(0, span)
```

怪物/宠物采用另一条 Soft DEF 随机路径，不得复用玩家公式。

## 8.3 默认物理减伤

```text
DamageAfterDEF = floor(Damage * (100 - HardDEF) / 100) - RolledSoftDEF
```

默认配置：

```text
weapon_defense_type = 0
max_def = 99
```

超出最大硬防的处理受 `over_def_bonus` 等配置影响。

## 8.4 精炼与 Mastery 的顺序

经典物理管线中，武器精炼攻击和部分 Mastery 在普通 DEF 减伤之后追加。这意味着“+5 精炼 ATK”不等价于在总攻击最前面增加 5。

## 8.5 围攻防御惩罚

默认对玩家生效：

```text
vit_penalty_type  = percentage
vit_penalty_count = 3
vit_penalty_num   = 5
```

被多名敌人锁定时，Hard DEF 与 Soft DEF 会按攻击者数量降低。目标计数和阈值逻辑必须复用服务端实现。

## 8.6 魔法防御

```text
Hard MDEF -> 百分比减伤
Soft MDEF -> 固定减伤
```

默认：

```text
DamageAfterMDEF = floor(Damage * (100 - HardMDEF) / 100) - SoftMDEF
```

其中 `SoftMDEF = INT + floor(VIT/2) + bonuses`。

## 8.7 无视防御

装备、卡片、技能和状态可能：

- 按比例忽略 Hard DEF/MDEF；
- 完全无视；
- 把防御转成攻击；
- 使用替代防御公式；
- 仅对特定种族/阶级/属性生效。

这些效果的顺序必须保留来源实现，不能合并成一个“穿透率”字段。
