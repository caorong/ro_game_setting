# 16. 来源索引

## 16.1 核心源码

| 主题 | 路径 |
|---|---|
| 编译模式 | `src/config/renewal.hpp` |
| 面板属性、HP/SP、恢复、状态 | `src/map/status.cpp` |
| 物理/魔法/Misc、命中、暴击、卡片修正 | `src/map/battle.cpp` |
| 属性点、职业数据库、经验 | `src/map/pc.cpp` |
| 吟唱、后摇、技能单位 | `src/map/skill.cpp` |
| 分拆技能实现 | `src/map/skills/**/*.cpp` |
| 装备与道具脚本加载 | `src/map/itemdb.cpp` |
| 怪物与掉落 | `src/map/mob.cpp` |
| 宠物 | `src/map/pet.cpp` |
| 人工生命体 | `src/map/homunculus.cpp` |
| 佣兵 | `src/map/mercenary.cpp` |
| 队伍 | `src/map/party.cpp` |
| 公会 | `src/map/guild.cpp` |

## 16.2 Pre-Renewal 数据表

| 主题 | 路径 |
|---|---|
| 职业属性 | `db/pre-re/job_stats.yml` |
| HP/SP 基础表 | `db/pre-re/job_basepoints.yml` |
| 职业经验 | `db/pre-re/job_exp.yml` |
| 武器动作延迟 | `db/pre-re/job_aspd.yml` |
| 属性点累计 | `db/pre-re/statpoint.yml` |
| 技能静态数据 | `db/pre-re/skill_db.yml` |
| 技能树 | `db/pre-re/skill_tree.yml` |
| 怪物 | `db/pre-re/mob_db.yml` |
| 怪物技能 | `db/pre-re/mob_skill_db.txt` |
| 装备/消耗品/材料 | `db/pre-re/item_db*.yml` |
| 卡片/装备套装 | `db/pre-re/item_combos.yml` |
| 精炼 | `db/pre-re/refine.yml` |
| 属性矩阵 | `db/pre-re/attr_fix.yml` |
| 体型覆盖 | `db/pre-re/size_fix.yml` |
| 状态元数据 | `db/pre-re/status.yml` |
| 宠物 | `db/pre-re/pet_db.yml` |
| 人工生命体 | `db/pre-re/homunculus_db.yml` |
| 佣兵 | `db/pre-re/mercenary_db.yml` |
| 制造配方 | `db/pre-re/produce_db.txt` |

## 16.3 默认配置

```text
conf/battle/battle.conf
conf/battle/player.conf
conf/battle/skill.conf
conf/battle/items.conf
conf/battle/monster.conf
conf/battle/drops.conf
conf/battle/exp.conf
```

## 16.4 固定链接

所有来源链接都应使用完整 SHA，例如：

```text
https://github.com/rathena/rathena/blob/2fe6ab3dc4d830b11d93fb44c3b48436571890bd/src/map/status.cpp
```

不要链接 `master`，否则文档会在上游更新后悄悄改变含义。
