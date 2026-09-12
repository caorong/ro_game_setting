# 03. 六维属性与派生属性

## 3.1 主攻击属性

以下远程武器以 DEX 为主、STR 为副：

```text
Bow, Musical, Whip,
Revolver, Rifle, Gatling, Shotgun, Grenade
```

其他武器以 STR 为主、DEX 为副。

令：

```text
M = 主攻击属性
S = 副攻击属性
```

## 3.2 Status ATK

```text
StatusATK = M + floor(M / 10)^2 + floor(S / 5) + floor(LUK / 5)
```

经典版的主属性十点断点来自平方项。例如只看主属性部分：

```text
M=19: 19 + 1² = 20
M=20: 20 + 2² = 24
```

因此 19→20 会增加 4 点，而不是 1 点。

## 3.3 MATK 区间

```text
MATK_MIN = INT + floor(INT / 7)^2
MATK_MAX = INT + floor(INT / 5)^2
```

魔法伤害会在此区间随机取值，再进入技能倍率、MDEF、属性和装备修正。

## 3.4 面板派生属性

```text
HIT       = BonusHIT  + BaseLv + DEX
FLEE      = BonusFLEE + BaseLv + AGI
SoftDEF   = BonusSoftDEF + VIT
SoftMDEF  = BonusSoftMDEF + INT + floor(VIT / 2)
```

暴击和完全回避在源码内部以 0.1% 为单位：

```text
CRI_internal   = BonusCRI   + 10 + floor(LUK * 10 / 3)
FLEE2_internal = BonusFLEE2 + 10 + LUK
```

转换成百分比需除以 10。

## 3.5 六维属性的主要影响

| 属性 | 主要直接影响 |
|---|---|
| STR | 近战 Status ATK、负重、部分技能公式 |
| AGI | FLEE、ASPD、部分延迟或技能条件 |
| VIT | Soft DEF、MaxHP、HP 恢复、异常抗性 |
| INT | MATK、Soft MDEF、MaxSP、SP 恢复、部分异常抗性 |
| DEX | HIT、远程 Status ATK、ASPD、经典吟唱时间、武器最小攻击 |
| LUK | Status ATK、暴击、Perfect Flee、异常成功/抵抗与部分制造公式 |

## 3.6 基础属性、总属性和装备属性

源码会区分：

- 玩家投入的基础属性；
- Job Bonus；
- 装备与状态加成；
- “装备提供的 VIT/INT”对 MaxHP/MaxSP 的特殊固定补偿。

因此实现 MaxHP/SP 或状态点成本时，不得只传一个“总 VIT/INT”就结束。
