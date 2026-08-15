# 11. MaxHP、MaxSP 与恢复

## 11.1 MaxHP

玩家基础 HP 先按职业和 Base Level 查 `job_basepoints.yml`：

```text
BaseHP = JobBaseHP[BaseLv]
```

核心倍率：

```text
HP_after_VIT = BaseHP * (1 + VIT / 100)
转生职业再乘 1.25
```

随后加入：

- 装备提供的 VIT 固定补偿；
- 固定 MaxHP 加成；
- 装备、道具、状态百分比加成；
- 全局 HP rate；
- 上限裁剪。

每层存在独立取整，不能把所有百分比合并后一次计算。

## 11.2 MaxSP

同理：

```text
BaseSP = JobBaseSP[BaseLv]
SP_after_INT = BaseSP * (1 + INT / 100)
转生职业再乘 1.25
```

随后进入固定、装备、状态和全局倍率。

## 11.3 自然恢复

默认自然恢复量：

```text
HP_per_tick = floor(VIT / 5) + max(1, floor(MaxHP / 200))
SP_per_tick = 1 + floor(INT / 6) + floor(MaxSP / 100)
```

若 `INT >= 120`：

```text
SP_per_tick += floor((INT - 120) / 2) + 4
```

默认周期：

```text
HP: 6 秒
SP: 8 秒
被动恢复技能: 10 秒
```

## 11.4 被动技能示例

剑士 HP Recovery：

```text
SkillHP = 5 * SkillLv + floor(SkillLv * MaxHP / 500)
```

法师 SP Recovery：

```text
SkillSP = 3 * SkillLv + floor(SkillLv * MaxSP / 500)
```

## 11.5 重量状态

Pre-Renewal 官方默认在负重达到 50% 后停止自然恢复；90% 为 major overweight，通常进一步限制攻击和技能。配置文件里某些默认值采用注释回退，生成器应解析“模式默认”，而不是只读取显式行。
