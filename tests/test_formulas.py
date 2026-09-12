from __future__ import annotations

import pytest

from ro_pre_re.formulas import (
    attack_delay_ms,
    attack_motion_ms,
    attacks_per_second,
    critical_internal,
    matk_max,
    matk_min,
    multiply_final_hit_rate,
    natural_hp_regen,
    natural_sp_regen,
    normal_hit_rate,
    perfect_flee_internal,
    player_soft_def_roll,
    pre_re_base_attack_motion,
    pre_re_cast_time_ms,
    stat_point_cost,
    stat_points_at_level,
    status_atk,
)


def test_status_atk_main_stat_breakpoint() -> None:
    assert status_atk(19, 0, 0) == 20
    assert status_atk(20, 0, 0) == 24


def test_status_atk_secondary_and_luk() -> None:
    assert status_atk(50, 25, 20) == 84


def test_matk_breakpoints() -> None:
    assert matk_min(49) == 98
    assert matk_max(50) == 150


def test_critical_and_perfect_flee_internal_units() -> None:
    assert critical_internal(0) == 10
    assert critical_internal(30) == 110
    assert perfect_flee_internal(30) == 40


@pytest.mark.parametrize(
    ("current", "expected"),
    [(1, 2), (9, 2), (10, 2), (11, 3), (20, 3), (21, 4), (91, 11)],
)
def test_stat_point_cost(current: int, expected: int) -> None:
    assert stat_point_cost(current) == expected


def test_cumulative_stat_points() -> None:
    assert stat_points_at_level(1) == 48
    assert stat_points_at_level(2) == 51
    assert stat_points_at_level(99) == 1273


def test_regeneration() -> None:
    assert natural_hp_regen(vit=50, max_hp=4000) == 30
    assert natural_sp_regen(intelligence=60, max_sp=1000) == 21
    assert natural_sp_regen(intelligence=120, max_sp=1000) == 35


def test_pre_re_base_attack_motion() -> None:
    assert pre_re_base_attack_motion(600, agi=50, dex=30) == 462


def test_aspd_time_conversion() -> None:
    assert attack_motion_ms(190) == 100
    assert attack_delay_ms(190) == 200
    assert attacks_per_second(190) == pytest.approx(5.0)


def test_normal_hit_rate_and_caps() -> None:
    assert normal_hit_rate(100, 80) == 100
    assert normal_hit_rate(1, 200) == 5


def test_bash_final_hit_rate_multiplier() -> None:
    assert multiply_final_hit_rate(60, 50) == 90


def test_cast_time() -> None:
    assert pre_re_cast_time_ms(1000, dex=0) == 1000
    assert pre_re_cast_time_ms(1000, dex=75) == 500
    assert pre_re_cast_time_ms(1000, dex=150) == 0
    assert pre_re_cast_time_ms(1000, dex=200) == 0


def test_player_soft_def_roll_bounds() -> None:
    roll = player_soft_def_roll(100)
    assert roll.minimum == 80
    assert roll.maximum == 115
