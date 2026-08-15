# 12. 状态异常与抗性

## 12.1 通用概率管线

状态概率内部通常使用 0～10000：

```text
1 = 0.01%
10000 = 100%
```

通用阶段：

```text
rate -= rate * sc_def / 10000
rate -= sc_def2
应用装备/道具抗性
正概率向上对齐到 10
应用最低成功率
random(0..9999) < rate
```

持续时间：

```text
tick -= tick * tick_def / 10000
tick -= tick_def2
应用最低持续时间
```

## 12.2 常见自然抗性

完整机器数据：`data/formulas/status_effects.yml`。

| 状态 | 百分比抗性主属性 | 固定概率项常见组成 |
|---|---|---|
| Poison | VIT | LUK、双方等级差 |
| Stun | VIT | LUK、双方等级差 |
| Silence | VIT | LUK、双方等级差 |
| Bleeding | VIT | LUK、双方等级差 |
| Sleep | INT | LUK、双方等级差 |
| Freeze | Hard MDEF | LUK、双方等级差 |
| StoneWait | Hard MDEF | LUK、双方等级差 |
| Curse | LUK | 目标 LUK、施法者等级 |
| Blind | VIT + INT | LUK、双方等级差 |
| Confusion | STR + INT | 状态专属固定项 |

## 12.3 为什么不能写“100 VIT 免疫一切”

- 不同状态读取不同属性；
- 技能可能绕过自然抗性；
- Boss/怪物可能有 mode 或状态免疫；
- 装备抗性和自然抗性顺序不同；
- 最低成功率与最低持续时间可阻止绝对免疫；
- 状态的施加、持续伤害和解除是不同逻辑。

## 12.4 状态本体

`db/pre-re/status.yml` 描述图标、状态标志、计算触发和显示等元数据；真正抗性与效果则分布在 `status.cpp`、技能实现和 battle config 中。
