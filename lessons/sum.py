"""Summing the elements of a list using different loops."""

__author__ = "730418328"


def w_sum(vals: list[float]) -> float:
    """Return the sum using while loop."""
    index: int = 0
    sum_elements: float = 0.0
    while index < len(vals):
        sum_elements += vals[index]
        index += 1
    print(sum_elements)
    return sum_elements 
    

def f_sum(vals: list[float]) -> float:
    """Return the sum using for in."""
    new_vals: float = 0.0
    for elem in vals:
        new_vals += elem
    print(new_vals)
    return new_vals


def f_range_sum(vals: list[float]) -> float:
    """Return the sum using for in range."""
    index = 0
    sum_new: float = 0.0
    for index in range(0, len(vals)):
        sum_new += vals[index] 
    print(sum_new)
    return sum_new
