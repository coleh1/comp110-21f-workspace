"""Unit tests for list utility functions."""


__author__ = "123456789"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_standard() -> None:
    """Test with standard input."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_repeat_int() -> None:
    """Test with repeat integers."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_only_evens_no_evens() -> None:
    """Test without evens."""
    assert only_evens([1, 5, 3]) == []
    

def test_sub_standard() -> None:
    """test for a standard list."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub_negative_start() -> None:
    """Test for a negative start."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, -3, 3) == [10, 20, 30]


def test_sub_empty_list() -> None:
    """Test for empty list."""
    a_list = []
    assert sub(a_list, 1, 3) == []

    
def test_concat_simple() -> None:
    """Test for simple lists."""
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [6, 7, 8, 9, 10]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_concat_complex() -> None:
    """Test for complex lists."""
    list_1 = [132, 2342, 2342, 23423]
    list_2 = [674, 44565, 67567]
    assert concat(list_1, list_2) == [132, 2342, 2342, 23423, 674, 44565, 67567]


def test_concat_empty() -> None:
    """Test for empty lists."""
    list_1 = []
    list_2 = []
    assert concat(list_1, list_2) == []