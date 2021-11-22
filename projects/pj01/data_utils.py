"""Utility functions."""

__author__ = "730400371"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column based table wiht only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        column_list: list[str] = []
        i = 0
        while i < rows:
            column_list.append(table[column][i])
            i += 1 
        result[column] = column_list
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset to the original columns."""
    result: dict[str, list[str]] = {}
    for each in names:
        result[each] = table[each]
    return result


def concat(first_dict: dict[str, list[str]], second_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for each in first_dict:
        result[each] = first_dict[each]
    for each in second_dict:
        if each in result:
            result[each] = result[each] + second_dict[each]
        else:
            result[each] = second_dict[each]
    return result


def count(list_1: list[str]) -> dict[str, int]:
    """Count the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for each in list_1:
        if each in result:
            result[each] += 1
        else:
            result[each] = 1
    return result


def count_2var(data: dict[str, list[str]], var_1: str, var_2: str) -> int:
    """Counts the number of times that two values appear at the same time in a dictionary."""
    count: int = 0
    i: int = 0

    while i < len(data[var_1]):
        current_var_1: str = data[var_1][i]
        current_var_2: str = data[var_2][i]
        current_var_1_int: int = int(current_var_1)
        current_var_2_int: int = int(current_var_2)
        if current_var_1_int > 4:
            if current_var_2_int > 4:
                count += 1
                i += 1
            else:
                i += 1
        else:
            i += 1
    return count