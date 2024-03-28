"""list Utility Functions."""

__author__ = "730418328"


def all(list_int: list[int], num: int) -> bool:
    """All numbers must be same as num."""
    if len(list_int,) == 0:
        return False
    for elem in list_int:
        if elem != num:
            return False
    return True


def max(new_list: list[int]) -> int: 
    """Of the numbers, return the max."""
    if len(new_list) == 0:
        raise ValueError("max() arg is an empty List")
    else: 
        max = new_list[0] 
        for elem in new_list:
            if elem >= max:
                max = elem
        return max 


def is_equal(flist: list[int], slist: list[int]) -> bool:
    """Comparing Two lists."""
    if len(flist) != len(slist):
        return False 
    else:
        index = 0
        while index < len(flist):
            if flist[index] == slist[index]:
                index += 1        
            else:
                return False
        return True 


def extend(alist: list[int], blist: list[int]) -> None:
    """Combining Lists of Numbers."""
    for elem in blist:
        alist.append(elem)
