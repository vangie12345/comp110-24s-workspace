"""Recursion Challenge Question."""

__author__ = "730418328"


def f(n: int, k: int) -> int:
    """Defining a function recursively."""
    if n == 0:  # base case
        return 0
    else:  # recursive rule
        return f(n - 1, k) + k