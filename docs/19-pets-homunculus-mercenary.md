# 19. 宠物、人工生命体与佣兵

## 19.1 宠物

`pet_db.yml` 包含：

- 捕捉道具与蛋；
- 饲料与亲密度；
- 饥饿变化；
- 进化材料；
- 宠物脚本；
- 战斗与掉落相关开关。

宠物战斗属性和主人加成还会经过 `pet.cpp`、`status.cpp` 与 battle config。

## 19.2 人工生命体

经典 Alchemist 系统包括：

- 基础种类和进化形态；
- 等级 EXP；
- 六维成长随机区间；
- HP/SP/ATK/MATK/DEF 派生；
- 技能树与亲密度；
- 主人经验/掉落归属。

数据：`homunculus_db.yml`、`exp_homun.yml`，逻辑：`homunculus.cpp`。

## 19.3 佣兵

佣兵记录包括：

- 等级、HP/SP、ATK、DEF、MDEF；
- 攻击/移动动作；
- 技能；
- 契约时间、忠诚与击杀计数。

数据：`mercenary_db.yml`，逻辑：`mercenary.cpp`。

## 19.4 不复用玩家公式

宠物、人工生命体、佣兵和怪物在 `status_base_atk`、MATK、HIT/FLEE、软防等位置都有独立分支。不能把玩家的 STR 平方断点公式直接套给所有单位。
