"""Mutating functions."""

__author__ = "730418328"


def manual_append(word: list[int], num: int) -> None:
    """Adding a number to the end of the list."""
    word.append(num)
    return word


a: list[int] = [1, 2, 3]
manual_append(a, 2)
print(a)


def double(nums: list[int]) -> None:
    """Multiplying the numbers of the list by 2."""
    count = 0
    while count < len(nums): 
        nums[count] = nums[count] * 2
        count += 1
    return nums


a: list[int] = [1, 2, 3]
double(a)
print(a)