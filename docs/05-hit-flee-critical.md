# 05. 命中、回避、完全回避与暴击

## 5.1 普通命中率

面板：

```text
HIT  = BaseLv + DEX + BonusHIT
FLEE = BaseLv + AGI + BonusFLEE
```

默认普通命中率：

```text
HitRate = clamp(80 + AttackerHIT - EffectiveTargetFLEE + Modifiers, 5, 100)
```

## 5.2 围攻 FLEE 惩罚

默认配置对玩家生效：

```text
agi_penalty_type  = percentage
agi_penalty_count = 3
agi_penalty_num   = 10
```

目标被多名敌人锁定时，从阈值开始按攻击者数量降低 FLEE。实现必须调用源码相同的“被锁定目标计数”，不能简单按周围怪物数量估算。

## 5.3 Perfect Flee / Lucky Dodge

```text
FLEE2_internal = Bonus + LUK + 10
```

内部单位是 0.1%。它在普通攻击的普通 HIT/FLEE 判定之前检查，触发后直接 Lucky Dodge。

## 5.4 暴击率

攻击者基础：

```text
CRI_internal = BonusCRI + 10 + floor(LUK * 10 / 3)
```

普通玩家攻击还会减去目标 LUK 抵抗，常见主路径：

```text
EffectiveCRI_internal = CRI_internal - 2 * TargetLUK + race/weapon/skill/status modifiers
```

内部判定：

```text
random(0..999) < EffectiveCRI_internal
```

睡眠等状态和特定技能会修改概率。

## 5.5 判定优先级

普通武器攻击的核心顺序可概括为：

```text
Lucky Dodge
-> 多重攻击类判定
-> 暴击判定
-> 普通命中率判定
```

暴击通常绕过普通 HIT/FLEE，并使武器随机攻击取最大值；但技能必须检查 `NK_CRITICAL` 等标记，不是所有技能都能自然暴击。

## 5.6 技能命中修正

技能可以在普通命中管线不同阶段修改命中率。示例“狂击”：

```text
hit_rate += floor(hit_rate * 5 * SkillLv / 100)
```

这是对当前命中率做乘法增益，不是简单的 `+5*SkillLv`。

另有少数技能会在命中率封顶后再追加修正，所以最终实现不能只保存一个 `hit_bonus` 字段。
