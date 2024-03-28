"""Splitting a dictionary into two lists."""

__author__ = "730418328"


def get_keys(returned: dict[str, int]) -> list[str]:
    """Returning a list of strings, producing a list of all the keys in the input dictionary."""
    if len(returned) == 0:
        return list()
    else:
        new_list: list[str] = []
        for key in returned:
            new_list.append(key)
        return new_list


def get_values(returns: dict[str, int]) -> list[int]:
    """Returning list of values of the dictionary."""
    if len(returns) == 0:
        return list()
    else:
        new_lists: list[int] = []
        for key in returns:
            new_lists.append(returns[key])
        return new_lists