# 04. 攻击速度 ASPD

## 4.1 职业与武器基础延迟

Pre-Renewal 的基础不是统一 ASPD，而是：

```text
职业 × 武器类型 -> BaseMotion
```

数据来源：`db/pre-re/job_aspd.yml`。表中值是攻击动作延迟基线，数值越低越快。

双持时：

```text
BaseMotion = floor((主手基础延迟 + 副手基础延迟) * 7 / 10)
```

## 4.2 AGI / DEX 对基础动作延迟

```text
BaseMotion = BaseMotion
           - floor(BaseMotion * (4 * AGI + DEX) / 1000)
           + RawASPDAdjustment
```

这之后还会依次应用：

- 被动技能与骑乘惩罚；
- 百分比 ASPD 变化；
- 固定动作延迟变化；
- 状态效果；
- 最终攻速上限。

默认玩家上限：

```text
ASPD <= 190
```

## 4.3 面板 ASPD 与时间

```text
AttackMotion_ms = 2000 - 10 * ASPD
AttackDelay_ms  = 2 * AttackMotion_ms
AttacksPerSecond = 1000 / AttackDelay_ms
                 = 50 / (200 - ASPD)
```

| ASPD | 普攻间隔 | 理论每秒攻击 |
|---:|---:|---:|
| 170 | 600 ms | 1.667 |
| 180 | 400 ms | 2.5 |
| 185 | 300 ms | 3.333 |
| 190 | 200 ms | 5.0 |

## 4.4 ASPD 不等于技能 DPS

技能还受以下时间轴限制：

```text
CastTime
AfterCastActDelay
Cooldown
Animation / walk delay
skill-specific reuse
```

有些技能客户端表现受动作动画限制，但服务端复用规则并不等同于普通攻击间隔。

## 4.5 表驱动原则

不要把“剑士拿剑”和“刺客拿拳刃”的基础攻速写成固定职业常量。正确输入至少需要：

```text
job + main weapon + offhand + AGI + DEX + skills + statuses + config
```
