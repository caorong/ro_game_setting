# 02. Pre-Renewal 完整职业路线

## 2.1 六大主职业系

```text
Novice
├─ Swordman
│  ├─ Knight ──(Rebirth)── Lord Knight
│  └─ Crusader ─(Rebirth)─ Paladin
├─ Mage
│  ├─ Wizard ───(Rebirth)─ High Wizard
│  └─ Sage ─────(Rebirth)─ Professor
├─ Archer
│  ├─ Hunter ───(Rebirth)─ Sniper
│  ├─ Bard ─────(Rebirth)─ Clown       [male]
│  └─ Dancer ───(Rebirth)─ Gypsy       [female]
├─ Acolyte
│  ├─ Priest ───(Rebirth)─ High Priest
│  └─ Monk ─────(Rebirth)─ Champion
├─ Merchant
│  ├─ Blacksmith (Rebirth)─ Whitesmith
│  └─ Alchemist ─(Rebirth)─ Creator
└─ Thief
   ├─ Assassin ──(Rebirth)─ Assassin Cross
   └─ Rogue ─────(Rebirth)─ Stalker
```

“Rebirth”中间实际经过：

```text
普通二转 -> Novice High -> High 一转 -> 转生二转
```

## 2.2 经典扩展职业

```text
Novice
├─ Super Novice
├─ TaeKwon
│  ├─ Star Gladiator
│  └─ Soul Linker
├─ Gunslinger
└─ Ninja
```

本仓库不继续连接到 Rebellion、Kagerou/Oboro、三转或四转。

## 2.3 技术变体

rAthena 中存在一些额外 Job ID：

- `Knight2`、`Lord_Knight2` 等骑乘外观；
- `Star_Gladiator2` 等状态外观；
- Baby 职业；
- High 一转职业；
- 男女职业分支。

设计层路线图应折叠纯外观 ID，但生成数据必须保留原始 ID，防止装备限制和技能树匹配出错。

## 2.4 职业数值不写死在路线图

每个职业的以下数据由表驱动：

```text
MaxWeight       job_stats.yml
HP/SP growth    job_basepoints.yml + job_stats.yml
Job Bonus       job_stats.yml
weapon delay    job_aspd.yml
Base/Job EXP    job_exp.yml
skill tree      skill_tree.yml
```

路线与完整机器数据见 `data/jobs/job_paths.yml` 和生成目录。
