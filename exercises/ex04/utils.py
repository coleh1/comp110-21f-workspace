"""List utility functions."""


__author__ = "730400371"


def all(input_list: list[int], input_int: int) -> None:
    """Tests the equality of a list and integer."""
    i: int = 0
    current_input: int = 0
    outcome: str = "begin"

    while i < len(input_list):
        if input_list[current_input] == input_int:
            i += 1
            current_input += 1
            outcome = "True"
        else:
            outcome = "False"
            i += 1
       
    print(outcome)
    

def is_equal(x: list[int], y: list[int]) -> None:
    """Tests the equality of two lists."""
    z = sum(x) / len(x)
    t = sum(y) / len(y)
    if z == t:
        print("True")
    else:
        print("False")


def max(input: list[int]) -> int:
    """Takes the Max Value."""
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


all([1, 2, 1], 1)