"""Test my garden functions."""

__author__ = "730418328"


from lessons.garden.garden_helpers import add_by_kind 
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_use() -> None:
    """If the new plant isn't in the dict, it should add it."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia", "daisy"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "herbs", "oregano") 
    assert by_kind == {"flower": ["marigold", "zinnia", "daisy"], "vegetable": ["carrots"], "herbs": ["oregano"]}


def test_add_by_kind_edge() -> None:
    """If the list is empty, the addition will just add to the existing empty list."""
    by_kind: dict[str, list[str]] = {}
    add_by_kind(by_kind, "vegetable", "carrots")
    assert by_kind == {"vegetable": ["carrots"]}


def test_add_by_date_use() -> None:
    """If a new month and plant are added, it will enter the dict."""
    by_date: dict[str, list[str]] = {"November": ["marigold", "zinnia", "daisy"], "December": ["carrots"]}
    add_by_date(by_date, "January", "basil") 
    assert by_date == {"November": ["marigold", "zinnia", "daisy"], "December": ["carrots"], "January": ["basil"]}


def test_add_by_date_edge() -> None:
    """If an empty list is presented, the new entries will populate the empty list."""
    by_date: dict[str, list[str]] = {"November": []}
    add_by_date(by_date, "November", "marigold")
    assert by_date == {"November": ["marigold"]}


def test_lookup_by_kind_and_date_use() -> None: 
    """If a dict and list is given, it will filter out what is good to plant in that specific month."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"], "herbs": ["oregano"]}
    plants_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    correct = lookup_by_kind_and_date(plants_by_kind, plants_by_date, "vegetable", "June") 
    assert correct == "vegetables to plant in June: ['carrots']"


def test_lookup_by_kind_and_date_edge() -> None: 
    """If a dict and list is given, it will filter out what is good to plant in that specific month."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"], "herbs": ["oregano"]}
    plants_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    correct = lookup_by_kind_and_date(plants_by_kind, plants_by_date, "vegetable", "March") 
    assert correct == "No vegetables to plant in March."