"""List utility functions part 2."""

__author__ = "7304400371"


def only_evens(xs: list[int]) -> list[int]:
    new_list = list()
    length_list = len(xs)
    current_item: int = 0
    i: int = 0
    while i < length_list:
        if xs[current_item] % 2 == 0:
            new_list.append(xs[current_item])
        i += 1
        current_item += 1
    
    return new_list


def sub(xs: list[int], start_index: int, end_index: int) -> list[int]:
    if start_index < 0:
        start_index = 0
    if end_index > len(xs) - 1:
        end_index = len(xs)
    if len(xs) == 0:
        return []
    if start_index > len(xs) - 1:
        return []
    if end_index <= 0:
        return []
    new_list = list()
    start_index2 = start_index
    end_index2 = end_index - 1
    while start_index2 <= end_index2:
        new_list.append(xs[start_index2])
        start_index2 += 1
    return new_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    new_list = xs
    if len(xs) == 0:
        if len(ys) == 0:
            return xs
    i: int = 0
    while i < len(ys):
        new_list.append(ys[i])
        i += 1
    return new_list