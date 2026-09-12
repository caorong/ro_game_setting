# 00. 范围、版本与解释口径

## 0.1 唯一规则集

本仓库只解释：

```text
rAthena @ 2fe6ab3dc4d830b11d93fb44c3b48436571890bd
compile mode: PRERE
```

`PRERE` 的含义不是“读取 `db/pre-re` 就结束”，而是关闭所有 Renewal 计算宏，同时加载公共数据库默认值和 Pre-Renewal 覆盖值。

被排除的宏包括：

```text
RENEWAL
RENEWAL_CAST
RENEWAL_DROP
RENEWAL_EXP
RENEWAL_LVDMG
RENEWAL_ASPD
RENEWAL_STAT
```

## 0.2 为什么必须锁提交

RO 公式经常随实现修复而变化。只写“rAthena 公式”无法复现结果，因此所有记录必须绑定完整 commit SHA。

## 0.3 来源层次

| 层次 | 内容 | 典型路径 |
|---|---|---|
| 编译模式 | 决定启用哪组公式 | `src/config/renewal.hpp` |
| 通用管线 | 命中、物理、魔法、状态 | `src/map/battle.cpp`, `status.cpp` |
| 静态数据库 | 职业、技能、怪物、装备 | `db/pre-re/*` + `db/*` |
| 服务器开关 | 命中上下限、围攻惩罚、攻速上限 | `conf/battle/*.conf` |
| 技能实现 | 倍率、例外、状态概率 | `src/map/skills/**/*.cpp` |
| 道具脚本 | 卡片、套装、装备效果 | `item_db*.yml` |

## 0.4 取整规则

默认采用 C++ 整数运算：

- 正整数除法向下等价于 `floor`；
- 负数除法按 C++ 向零截断；
- 每一步都可能截断，不能随意合并分式；
- 随机区间需区分包含上界与不包含上界。

例如：

```text
(a / 5) + (b / 5)
```

不能擅自改为：

```text
(a + b) / 5
```

## 0.5 可信度标签

| 标签 | 含义 |
|---|---|
| `verified` | 已按源码执行路径人工核对 |
| `table-driven` | 必须读取锁定表，文档只解释字段和规则 |
| `source-indexed` | 完整实现已定位，但条件复杂，不压成单一公式 |
| `uncertain` | 存在已知争议或不能从当前来源充分确认 |

## 0.6 不等同于官方历史服

rAthena 是社区服务端实现。它的价值在于可执行、可追踪和数据完整，但不能自动证明某个日期的 kRO 官方服采用完全相同的隐藏取整与例外。需要复刻特定历史官方版本时，应另建规则锁，而不是修改本仓库口径。
