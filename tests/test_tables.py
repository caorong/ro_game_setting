from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(path: str):
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def test_element_matrix_is_complete() -> None:
    data = load("data/tables/element_modifiers.yml")
    elements = data["elements"]
    assert len(elements) == 10
    for level in range(1, 5):
        matrix = data["matrix"][level]
        assert set(matrix) == set(elements)
        for attack in elements:
            assert set(matrix[attack]) == set(elements)


def test_known_element_values() -> None:
    matrix = load("data/tables/element_modifiers.yml")["matrix"]
    assert matrix[1]["Fire"]["Earth"] == 150
    assert matrix[4]["Holy"]["Undead"] == 200
    assert matrix[4]["Neutral"]["Ghost"] == 0


def test_size_overrides_are_merged() -> None:
    weapons = load("data/tables/size_modifiers.yml")["weapons"]
    assert weapons["Dagger"] == {"Small": 100, "Medium": 75, "Large": 50}
    assert weapons["Knuckle"] == {"Small": 100, "Medium": 75, "Large": 50}
    assert weapons["Whip"] == {"Small": 75, "Medium": 100, "Large": 50}


def test_no_active_renewal_jobs() -> None:
    jobs = load("data/jobs/job_paths.yml")
    active = str(jobs["routes"]) + str(jobs["expanded_routes"])
    for job in ["Rune_Knight", "Warlock", "Ranger", "Arch_Bishop", "Mechanic", "Genetic"]:
        assert job not in active
