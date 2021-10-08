"""Practice with dictionaries."""

__author__ = "730400371"


def invert(dict_input: dict[str, str]) -> dict[str, str]:
    """Inverts a list."""
    inverted_dict_input = {}
    if dict_input == {}:
        return{}
    for key in dict_input:
        value_from_dict = dict_input[key]
        inverted_dict_input[value_from_dict] = key
    if len(dict_input) > len(inverted_dict_input):
        raise KeyError("Duplicates found in dictionary input")
    else:
        return inverted_dict_input


def favorite_color(dict_input: dict[str, str]) -> str:
    """Finds the most popular color."""
    inverted_dict_input = {}
    for key in dict_input:
        if dict_input[key] in inverted_dict_input:
            return dict_input[key]
        else:
            value_from_dict = dict_input[key]
            inverted_dict_input[value_from_dict] = key
    return ""


def count(xs: list[str]) -> dict[str, int]:
    """Counts repeated values in a string."""
    dict_output = {}
    i: int = 0
    if xs == []:
        return {}
    for item in xs:
        if xs[i] in dict_output:
            dict_output[xs[i]] += 1
            i += 1
        else:
            dict_output[xs[i]] = 1
            i += 1
    return dict_output