# 21. 维护、生成与扩展规范

## 21.1 更新来源

不要直接改 `data/sources/rathena.lock.yml` 后结束。升级上游提交时必须：

1. 同步新提交；
2. 生成旧/新索引；
3. 比较职业、技能、公式源码、装备、怪物和配置；
4. 更新人工文档；
5. 增加回归测试；
6. 在 PR 中列出行为变化。

## 21.2 添加技能公式

1. 在生成索引中定位技能 ID；
2. 读取 `skill_tree`、`skill_db`；
3. 定位 `skills/**` 或 `battle.cpp` 分支；
4. 追踪命中、伤害、状态、消耗和时间；
5. 用分步整数表达式记录；
6. 加入至少一个边界测试；
7. 标记 `verified`。

## 21.3 自动化产物

`generated/` 不作为唯一事实来源，它只是锁定上游数据的可重建视图。任何规范化记录都必须保留：

```text
source_commit
source_path
source_record_id 或 symbol
```

## 21.4 禁止混入 Renewal

校验脚本会拒绝：

- manifest ruleset 不是 `pre-renewal`；
- mode 不是 `PRERE`；
- job path 包含三转/四转；
- normalized formula 使用 POW/STA/WIS/SPL/CON/CRT；
- source path 指向 `db/re/` 或 `npc/re/`。

## 21.5 设计项目如何引用

下游游戏不应直接修改参考公式。建议：

```text
ro_game_setting = 原始参考
idle_ro game_balance = 最终游戏参数
mapping/decisions = 说明哪些照搬、简化或重做
```

这样上游事实和自研平衡不会混在一起。
