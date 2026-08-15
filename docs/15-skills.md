# 15. 全技能设定与公式覆盖

## 15.1 一条技能的完整来源

```text
skill_tree.yml      谁能学、最大等级、前置条件
skill_db.yml        类型、目标、范围、段数、属性、吟唱、消耗、持续时间
skills/**/*.cpp     倍率、命中、状态、召唤、位移和条件分支
battle.cpp          通用物理/魔法/Misc 管线
status.cpp          Buff/Debuff 与属性重算
item scripts        装备与卡片对技能的修改
```

## 15.2 技能分类

静态层至少区分：

- Weapon / Magic / Misc；
- 单体 / 地面 / 自身 / 无目标；
- 主动 / 被动 / Toggle；
- Damage / Heal / Buff / Debuff / Summon / Movement / Production；
- Short / Long；
- 固定属性 / 武器属性 / 状态决定；
- 真多段 / 显示多段 / 周期伤害。

## 15.3 为什么不声称自动抽取全部代数式

很多技能逻辑包含：

```cpp
if (目标状态)
    使用倍率 A;
else if (武器类型)
    使用倍率 B;
再根据 BaseLv、目标数量、地图、队伍和状态追加效果;
```

把这种逻辑强行压成一个字符串公式会丢信息。因此完整覆盖采用两级：

1. **完整静态数据 + 每个技能实现源码索引**；
2. **对常用技能进行人工规范化公式**。

## 15.4 生成完整索引

```bash
python scripts/sync_rathena.py --include-skill-source
python scripts/build_reference.py
```

输出：

```text
generated/skills/metadata.jsonl
generated/skills/tree.jsonl
generated/skills/source_index.json
generated/skills/coverage.json
```

## 15.5 狂击示例

```text
DamageRatio% = 100 + 30 * SkillLv
HitRate      = HitRate + floor(HitRate * 5 * SkillLv / 100)
```

学习 Fatal Blow，且 Bash Lv>5 时：

```text
StunRateInternal = (SkillLv - 5) * BaseLv * 10
```

这个内部概率随后还进入目标状态抗性管线。

## 15.6 技能审校清单

每个规范化技能至少记录：

```text
伤害类型、倍率、固定项、段数
命中/暴击规则、属性、范围
施法、后摇、冷却、资源与材料
状态概率、持续时间、抗性
召唤/地面单位/位移
前置、最大等级、被动条件
取整、随机、最小/最大值
源码路径、commit、已知例外
```
