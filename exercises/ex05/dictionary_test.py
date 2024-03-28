"""Dict Unit Tests."""

__author__ = "730418328"

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance
import pytest


def test_invert_use1() -> None:
    """When a dictionary is inputted, it should invert the values."""
    old: dict[str, str] = {"A": "a", "B": "b", "C": "c"}
    assert invert(old) == {"a": "A", "b": "B", "c": "C"}


def test_invert_use2() -> None:
    """When a duplicate value is found, it returns KeyError."""
    with pytest.raises(KeyError):
        old: dict[str, str] = {"vegetables": "carrots", "plant": "carrots", "orange": "carrots"}
        invert(old)


def test_invert_edge() -> None:
    """When an empty list is put in, nothing will be inverted."""
    old: dict[str, str] = {}
    assert invert(old) == {}


def test_favorite_color_use1() -> None:
    """The color repeated the most is returned."""
    pretty: dict[str, str] = {"Cassie": "purple", "Lauren": "orange", "Li": "black", "Joyce": "black"}
    assert favorite_color(pretty) == "black"


def test_favorite_color_use2() -> None:
    """If it is the same number for two colors, the one that appears first is printed."""
    pretty: dict[str, str] = {"Cassie": "purple", "Lauren": "orange", "Li": "purple", "Joyce": "orange"}
    assert favorite_color(pretty) == "purple"


def test_favorite_color_edge() -> None:
    """If integers are put in, it will not be correct."""
    pretty: dict[str, str] = {"Marc": 2, "Ezri": 3, "Kris": 3}
    assert favorite_color(pretty) != ({3})
    

def test_count_use1() -> None:
    """When a list if given, it will count the number of times the values show up."""
    unique: list[str] = ["blue", "red", "purple", "red", "green", "orange", "purple"]
    assert count(unique) == ({"blue": 1, "red": 2, "purple": 2, "green": 1, "orange": 1})


def test_count_use2() -> None:
    """When there is only one item, it will count that one up in one entry."""
    unique: list[str] = ["blue"]
    assert count(unique) == ({"blue": 1})


def test_count_edge() -> None:
    """When nothing is input, it will count nothing."""
    unique: list[str] = []
    assert count(unique) == ({})


def test_alphabetizer_use1() -> None:
    """For a list, it will sort it by the starting letter."""
    alf: list[str] = ["apple", "bear", "cat", "dog", "dolly", "door"]
    assert alphabetizer(alf) == ({"a": ["apple"], "b": ["bear"], "c": ["cat"], "d": ["dog", "dolly", "door"]})


def test_alphabetizer_use2() -> None:
    """When one is capitalized, it lowers the letter and adds it into the same list."""
    alf: list[str] = ["apple", "Bear", "cat", "dog", "Dolly", "door"]
    assert alphabetizer(alf) == ({"a": ["apple"], "b": ["Bear"], "c": ["cat"], "d": ["dog", "Dolly", "door"]})


def test_alphabetizer_edge() -> None:
    """When a number is inputed, it will still take it and create a list."""
    alf: list[str] = ["1", "Bear", "2", "dog", "3", "door"]
    assert alphabetizer(alf) == ({"1": ["1"], "b": ["Bear"], "2": ["2"], "d": ["dog", "door"], "3": ["3"]})


def test_update_attendance_use1() -> None:
    """When new people are added to the list, they show up in the final log."""
    attendance_log: dict = {"Monday": ["Eva", "Kevin"], "Tuesday": ["Kevin"], "Wednesday": ["Eva", "Kevin"]}
    update_attendance(attendance_log, "Tuesday", "Li")
    update_attendance(attendance_log, "Wednesday", "Joyce")
    assert attendance_log == {"Monday": ["Eva", "Kevin"], "Tuesday": ["Kevin", "Li"], "Wednesday": ["Eva", "Kevin", "Joyce"]}


def test_update_attendance_use2() -> None:
    """When a day is not added, it will add the day and people."""
    attendance_log: dict = {"Monday": ["Eva", "Kevin"], "Tuesday": ["Kevin"], "Wednesday": ["Eva", "Kevin"]}
    update_attendance(attendance_log, "Thursday", "Li")
    update_attendance(attendance_log, "Thursday", "Joyce")
    assert attendance_log == {"Monday": ["Eva", "Kevin"], "Tuesday": ["Kevin"], "Wednesday": ["Eva", "Kevin"], "Thursday": ["Li", "Joyce"]}


def test_update_attendance_edge() -> None:
    """If a duplicate name is added, it will still add it into the list."""
    attendance_log: dict = {"Monday": ["Eva", "Kevin"], "Tuesday": ["Kevin"], "Wednesday": ["Eva", "Kevin"]}
    update_attendance(attendance_log, "Thursday", "Kevin")
    update_attendance(attendance_log, "Thursday", "Kevin")
    assert attendance_log == {"Monday": ["Eva", "Kevin"], "Tuesday": ["Kevin"], "Wednesday": ["Eva", "Kevin"], "Thursday": ["Kevin"]}