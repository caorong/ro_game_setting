# AGENTS.md

## 仓库目标

维护一套严格限定为 **RO Pre-Renewal / PRERE** 的可量化规则参考。

## 强制约束

1. 不得引入 Renewal、三转、四转、地区服或私服规则。
2. 默认来源锁定为 rAthena commit `2fe6ab3dc4d830b11d93fb44c3b48436571890bd`；升级来源必须单独 PR，并更新来源锁、变更说明和测试。
3. 所有公式必须标明：单位、取整方式、适用对象、执行顺序、例外和源码路径。
4. C/C++ 整数除法按“向零截断”处理；不要把分步整数运算擅自合并成浮点近似。
5. “网上常见公式”不能作为单一依据。无法从锁定来源确认时，标记 `uncertain`，不要补猜。
6. 技能静态数据与技能实现必须分开记录。`skill_db.yml` 不是完整技能公式。
7. 公共 DB 与 `db/pre-re` 存在继承/覆盖关系，读取时必须遵循上游导入顺序。
8. 不提交整个 `vendor/rathena`；使用同步脚本重建，并保留哈希清单。
9. 中文文档保留英文常量与职业名，避免地区译名歧义。
10. 修改核心公式必须增加或更新回归测试。

## 公式记录模板

```yaml
id: pre_re.status_atk
status: verified
expression: main + floor(main / 10)^2 + floor(secondary / 5) + floor(luk / 5)
inputs:
  main: 主攻击属性
  secondary: 副攻击属性
  luk: LUK
rounding: each integer division truncates toward zero
unit: ATK points
source:
  repository: rathena/rathena
  commit: 2fe6ab3dc4d830b11d93fb44c3b48436571890bd
  path: src/map/status.cpp
  symbol: status_base_atk
exceptions: []
```

## 验证命令

```bash
python scripts/validate_reference.py
pytest
```
