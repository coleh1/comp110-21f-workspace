"""Unit tests for dictionary functions."""


__author__ = "730400371"

from exercises.ex06.dictionaries import invert, favorite_color, count


def test_insert_standard() -> None:
    """Test with standard input."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_insert_long() -> None:
    """Test with long list."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_insert_edge() -> None:
    """Test edge case."""
    assert invert({}) == {}
    

def test_favorite_color_standard() -> None:
    """Test for a standard dict input."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_long() -> None:
    """Test for a long dict input."""
    favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "John": "green", "Kassidy": "tan", "Robert": "camoflage"}) == "blue"


def test_favorite_color_edge() -> None:
    """Test for a tie."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "John": "yellow"}) == "blue"

    
def test_count_simple() -> None:
    """Test for simple lists."""
    assert count(["ten", "four", "tenty-five", "ten", "two"]) == {'ten': 2, 'four': 1, 'tenty-five': 1, 'two': 1}


def test_count_long() -> None:
    """Test for complex lists."""
    assert count(["ten", "four", "tenty-five", "four", "ten", "four", "two"]) == {'ten': 2, 'four': 3, 'tenty-five': 1, 'two': 1}


def test_count_edge() -> None:
    """Test for empty lists."""
    assert count([]) == {}