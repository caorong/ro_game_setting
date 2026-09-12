# 10. 吟唱、后摇、冷却与动作限制

## 10.1 Pre-Renewal 吟唱

对可被 DEX 缩短的技能，核心阶段：

```text
CastTime = BaseCastTime * max(0, 150 - DEX) / 150
```

随后再按源码顺序应用：

- 技能和状态固定调整；
- 装备/卡片吟唱缩减；
- 百分比缩减；
- 全局 `casting_rate`；
- 特殊职业/技能例外。

默认：

```text
castrate_dex_scale = 150
casting_rate = 100%
```

DEX≥150 的常规可变吟唱阶段归零，但不能据此断言所有技能都无吟唱：技能可标记不可缩短、使用固定时间或走自定义实现。

## 10.2 后摇

`AfterCastActDelay` 是技能释放后的行动限制。默认官方式配置中：

```text
delay_dependon_dex = no
delay_dependon_agi = no
```

即 DEX/AGI 不自动减少通用后摇。

## 10.3 Cooldown

Cooldown 是同一技能再次使用的复用时间，与后摇不同：

- 后摇可阻止释放其他技能；
- Cooldown 只阻止对应技能；
- 怪物技能可能使用 `mob_skill_db` 自己的复用时间；
- 地面技能还受最大实例数和持续时间限制。

## 10.4 动作与移动延迟

服务端还可能应用：

- 攻击动作 `amotion`；
- 受击动作 `dmotion`；
- 多段受击附加 walk delay；
- 技能最小延迟；
- combo 特殊延迟；
- 客户端动画锁。

因此技能循环时间应建模为多个时钟，而不是 `max(吟唱, 冷却)` 的单一公式。
