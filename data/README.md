# 机器可读数据

此目录只存放已经人工规范化、适合直接消费的数据。完整 rAthena 数据通过同步脚本进入 `vendor/rathena`，然后生成到 `generated`。

## 状态标记

- `verified`：已经按锁定提交的实际执行路径审校；
- `table-driven`：值必须从上游表生成，不能硬编码概括；
- `source-indexed`：完整逻辑已通过源码定位，但不适合压成单一代数式；
- `uncertain`：存在版本争议或证据不足。

## 为什么不直接复制全部上游文件

上游数据量很大，且遵循 GPL-3.0。仓库默认保存来源锁、同步器、生成器和原创规范化数据，避免悄悄复制一份难以更新的快照。需要完整数据时运行：

```bash
python scripts/sync_rathena.py --include-skill-source
python scripts/build_reference.py
```
