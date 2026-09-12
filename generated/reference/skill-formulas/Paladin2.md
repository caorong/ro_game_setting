# Paladin2 技能公式与实现

> Pre-Renewal / PRERE；来源提交：`2fe6ab3dc4d830b11d93fb44c3b48436571890bd`。

| ID | 技能 | 覆盖 | 实现类 | 文件 |
|---:|---|---|---|---|
| 368 | `PA_SACRIFICE` / Martyr's Reckoning | `exact-class-methods` | `SkillMartyrsReckoning` | src/map/skills/swordman/martyrsreckoning.cpp |

## 详细公式与效果实现

### Martyr's Reckoning (`PA_SACRIFICE`)

武器/物理技能；目标：自身；最高等级 5；命中类型：Single；段数：1；技能后摇：2000 ms；伤害标记：NoDamage, IgnoreDefense, IgnoreFlee；消耗/限制：SP 100；关联状态：Sacrifice。

- 覆盖：`exact-class-methods`
- 实现类：`SkillMartyrsReckoning`
- 实现文件：`src/map/skills/swordman/martyrsreckoning.cpp`

#### `SkillMartyrsReckoning::SkillMartyrsReckoning`

来源：`src/map/skills/swordman/martyrsreckoning.cpp:9-10`

```cpp
SkillMartyrsReckoning::SkillMartyrsReckoning() : WeaponSkillImpl(PA_SACRIFICE) {
}
```

#### `SkillMartyrsReckoning::calculateSkillRatio`

来源：`src/map/skills/swordman/martyrsreckoning.cpp:12-14`

```cpp
void SkillMartyrsReckoning::calculateSkillRatio(const Damage *wd, const block_list *src, const block_list *target, uint16 skill_lv, int32 &base_skillratio, int32 mflag) const {
	base_skillratio += -10 + 10 * skill_lv;
}
```

#### `SkillMartyrsReckoning::castendNoDamageId`

来源：`src/map/skills/swordman/martyrsreckoning.cpp:16-21`

```cpp
void SkillMartyrsReckoning::castendNoDamageId(block_list *src, block_list *target, uint16 skill_lv, t_tick tick, int32& flag) const {
	sc_type type = skill_get_sc(getSkillId());

	clif_skill_nodamage(src,*target,getSkillId(),skill_lv,
		sc_start(src,target,type,100,skill_lv,skill_get_time(getSkillId(),skill_lv)));
}
```
