# 13. 装备、卡片与精炼

## 13.1 装备记录

装备静态字段主要包括：

```text
Id / AegisName / Name
Type / SubType
Buy / Sell / Weight
Attack / MagicAttack / Defense
Range / Slots / WeaponLevel / ArmorLevel
EquipLevelMin / EquipLevelMax
Jobs / Classes / Gender / Locations
Refineable / Gradable
Script / EquipScript / UnEquipScript
```

Pre-Renewal 实际数据位于 `item_db_equip.yml`，公共包装表负责导入。

## 13.2 卡片不是单独的固定属性表

卡片效果通常由 Item Script 表达，可包含：

- STR/AGI 等固定属性；
- 按种族、属性、体型、阶级增伤/减伤；
- 自动施法；
- 状态施加与抗性；
- 技能等级或技能增伤；
- 掉落率与吸血；
- 套装条件。

因此“卡片效果完整数据”必须保留脚本和解释器语义，不能只抽 `atk + x`。

## 13.3 精炼数据单位

rAthena 精炼表中的 `Bonus` 和 `RandomBonus` 使用百分之一单位存储，载入后除以 100。

经典常见基础增量：

| 类型 | 每级基础收益 |
|---|---:|
| Armor | +0.7 DEF（所有装备精炼防御先汇总再取整） |
| Weapon Lv1 | +2 ATK |
| Weapon Lv2 | +3 ATK |
| Weapon Lv3 | +5 ATK |
| Weapon Lv4 | +7 ATK |

安全精炼等级、成功率、材料、费用、破坏率和过精炼随机攻击必须读取 `db/pre-re/refine.yml`。

## 13.4 过精炼随机攻击

超过安全等级后，武器可获得 `RandomBonus` 上限。实际攻击中从对应范围随机取得，并在经典物理 DEF 后阶段追加。

## 13.5 防具精炼取整

单件 +1 的 0.7 DEF 不一定立刻显示为 1。服务端先累计所有防具精炼的百分之一防御，再按源码规则统一四舍五入/取整。因此不要逐件先取整后相加。

## 13.6 装备损坏

自然损坏默认关闭，但技能、锻造和状态仍可导致武器/防具损坏。损坏与精炼失败破坏是不同系统。
