"""Functions that implement sorting algorithms."""

__author__ = "730418328"


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    idx: int = 0
    while idx < len(x): 
        nidx: int = idx + 1
        min: int = x[idx]
        min_idx: int = idx
        while nidx < len(x): # minimum must be set before the loop
            if x[nidx] < min:
                min_idx = nidx
            nidx += 1
        new = x[min_idx] # new is minimum
        x[min_idx] = x[idx]
        x[idx] = new 
        idx += 1


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    unsorted_idx: int = 0
    while unsorted_idx < (len(x) - 1): 
        sorted_idx: int = unsorted_idx + 1
        while sorted_idx > 0 and x[sorted_idx] < x[sorted_idx - 1]:
            holder = x[sorted_idx - 1]
            x[sorted_idx - 1] = x[sorted_idx]
            x[sorted_idx] = holder 
            sorted_idx -= 1
        unsorted_idx += 1
