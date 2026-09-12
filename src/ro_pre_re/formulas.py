from __future__ import annotations

import math
from dataclasses import dataclass


def cxx_div(numerator: int, denominator: int) -> int:
    """C++ integer division: truncate toward zero."""
    if denominator == 0:
        raise ZeroDivisionError("denominator must not be zero")
    return math.trunc(numerator / denominator)


def clamp(value: int, minimum: int, maximum: int) -> int:
    if minimum > maximum:
        raise ValueError("minimum must be <= maximum")
    return max(minimum, min(maximum, value))


def status_atk(main: int, secondary: int, luk: int) -> int:
    """Pre-Re Status ATK for PCs; main is STR or DEX depending on weapon."""
    return main + cxx_div(main, 10) ** 2 + cxx_div(secondary, 5) + cxx_div(luk, 5)


def matk_min(intelligence: int) -> int:
    return intelligence + cxx_div(intelligence, 7) ** 2


def matk_max(intelligence: int) -> int:
    return intelligence + cxx_div(intelligence, 5) ** 2


def hit(base_level: int, dex: int, bonus: int = 0) -> int:
    return max(1, bonus + base_level + dex)


def flee(base_level: int, agi: int, bonus: int = 0) -> int:
    return max(1, bonus + base_level + agi)


def soft_def(vit: int, bonus: int = 0) -> int:
    return max(0, bonus + vit)


def soft_mdef(intelligence: int, vit: int, bonus: int = 0) -> int:
    return max(0, bonus + intelligence + cxx_div(vit, 2))


def critical_internal(luk: int, bonus: int = 0) -> int:
    """Internal unit: 10 = 1%."""
    return max(1, bonus + 10 + cxx_div(luk * 10, 3))


def perfect_flee_internal(luk: int, bonus: int = 0) -> int:
    """Internal unit: 10 = 1%."""
    return max(0, bonus + luk + 10)


def stat_point_cost(current_base_stat: int) -> int:
    if current_base_stat < 1:
        raise ValueError("current_base_stat must be >= 1")
    return 1 + cxx_div(current_base_stat + 9, 10)


def stat_points_at_level(base_level: int) -> int:
    """Cumulative non-trans status points, matching pre-re statpoint.yml through Lv99."""
    if base_level < 1:
        raise ValueError("base_level must be >= 1")
    total = 48
    for level in range(2, base_level + 1):
        total += 3 + cxx_div(level - 1, 5)
    return total


def natural_hp_regen(vit: int, max_hp: int) -> int:
    return cxx_div(vit, 5) + max(1, cxx_div(max_hp, 200))


def natural_sp_regen(intelligence: int, max_sp: int) -> int:
    value = 1 + cxx_div(intelligence, 6) + cxx_div(max_sp, 100)
    if intelligence >= 120:
        value += cxx_div(intelligence - 120, 2) + 4
    return value


def passive_hp_recovery(skill_level: int, max_hp: int) -> int:
    return skill_level * 5 + cxx_div(skill_level * max_hp, 500)


def passive_sp_recovery(skill_level: int, max_sp: int) -> int:
    return skill_level * 3 + cxx_div(skill_level * max_sp, 500)


def pre_re_base_attack_motion(base_weapon_delay: int, agi: int, dex: int, raw_adjustment: int = 0) -> int:
    reduction = cxx_div(base_weapon_delay * (4 * agi + dex), 1000)
    return base_weapon_delay - reduction + raw_adjustment


def attack_motion_ms(aspd: int) -> int:
    return 2000 - 10 * aspd


def attack_delay_ms(aspd: int) -> int:
    return 2 * attack_motion_ms(aspd)


def attacks_per_second(aspd: int) -> float:
    delay = attack_delay_ms(aspd)
    if delay <= 0:
        raise ValueError("ASPD produces a non-positive attack delay")
    return 1000.0 / delay


def normal_hit_rate(attacker_hit: int, target_flee: int, modifier: int = 0, minimum: int = 5, maximum: int = 100) -> int:
    return clamp(80 + attacker_hit - target_flee + modifier, minimum, maximum)


def multiply_final_hit_rate(hit_rate: int, bonus_percent: int) -> int:
    """Used by skills such as Bash after base hit-rate construction."""
    return hit_rate + cxx_div(hit_rate * bonus_percent, 100)


def effective_swarm_value(value: int, attacker_count: int, threshold: int, penalty_percent: int) -> int:
    """Default rAthena percentage swarm-penalty shape for FLEE/DEF values."""
    if attacker_count < threshold:
        return value
    steps = attacker_count - (threshold - 1)
    return max(1, cxx_div(value * (100 - steps * penalty_percent), 100))


@dataclass(frozen=True)
class SoftDefRoll:
    minimum: int
    maximum: int


def player_soft_def_roll(soft_def_value: int) -> SoftDefRoll:
    """Inclusive bounds of the Pre-Re PC VIT-defense random roll."""
    d = max(0, soft_def_value)
    three_tenths = cxx_div(3 * d, 10)
    base = three_tenths + cxx_div(d, 2)
    span = max(0, cxx_div(d * d, 150) - three_tenths - 1)
    return SoftDefRoll(base, base + span)


def physical_after_def(damage: int, hard_def: int, rolled_soft_def: int) -> int:
    return cxx_div(damage * (100 - hard_def), 100) - rolled_soft_def


def magic_after_mdef(damage: int, hard_mdef: int, soft_mdef_value: int) -> int:
    return cxx_div(damage * (100 - hard_mdef), 100) - soft_mdef_value


def pre_re_cast_time_ms(base_cast_ms: int, dex: int, dex_scale: int = 150) -> int:
    if base_cast_ms < 0:
        raise ValueError("base_cast_ms must be >= 0")
    remaining = max(0, dex_scale - dex)
    return cxx_div(base_cast_ms * remaining, dex_scale)


def apply_percent(value: int, percent: int) -> int:
    return cxx_div(value * percent, 100)


def element_damage(damage: int, modifier_percent: int) -> int:
    return apply_percent(damage, modifier_percent)


def size_damage(damage: int, modifier_percent: int) -> int:
    return apply_percent(damage, modifier_percent)
