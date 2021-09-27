"""List utility functions."""

__author__ = "730400371"


def all(x: list[int], y: int) -> None:
    z = sum(x) / len(x)
    if z == y:
        print("True")
    else:
        print("False")


def is_equal(x: list[int], y: list[int]) -> None:
    z = sum(x) / len(x)
    t = sum(y) / len(y)
    if z == t:
        print("True")
    else:
        print("False")


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    max_value: int = 0
    i: int = 0
    compared_input: int = 0

    if input[0] > input[1]:
        max_value = input[0]
    else:
        max_value = input[1]
    
    while i != len(input):
        if max_value >= input[compared_input]:
            compared_input += 1
            i += 1
        else:
            max_value = input[compared_input]
            compared_input = 0
            i = 0
    return max_value