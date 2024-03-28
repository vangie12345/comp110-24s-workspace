"""Dictionary Utils."""

__author__ = "730418328" 


def invert(old: dict[str, str]) -> dict[str, str]:
    """Returns a dict that inverts the keys and the values."""
    new: dict[str, str] = {}
    for key in old: 
        value = old[key]
        if value in new:  # old list has multiple of same value
            raise KeyError
        # value of old = key of new
        # key of old = value of new 
        new[value] = key
    return new 


def favorite_color(pretty: dict[str, str]) -> str:
    """Takes names and colors, returning most frequently seen color."""
    color_dict: dict[str, int] = {}
    for key in pretty: 
        # going through the key of old dict
        # if value is in new dict, which it shouldn't, the new value is now 1
        if pretty[key] in color_dict: 
            color_dict[pretty[key]] += 1
        else:
            color_dict[pretty[key]] = 1  # pretty[key] = 1
    counter: int = 0
    for key in color_dict:
        if color_dict[key] > counter:  # number
            counter = color_dict[key]
            favoritecolor = key
        elif color_dict[key] == counter and favoritecolor == []:
            favoritecolor = key  
    return favoritecolor

    
def count(unique: list[str]) -> dict[str, int]:
    """Unique value in given list associated with count of # of times value in the list."""
    new: dict[str, int] = {}
    for values in unique:  # iterates through each str in list 
        if values in new:  # this replaces the value with the variable name of the current value
            # "new" replaces old dictionary with the new name of the result
            new[values] += 1
        else:
            new[values] = 1
    return new


def alphabetizer(alf: list[str]) -> dict[str, list[str]]: 
    """Each key is unique letter in alphabet, each value is list of words that begin with that letter."""
    letter_list: dict[str, list[str]] = {}
    for key in alf:  # iterate through each item in list (["cat", "apple", "boy", "bad"])
        first_letter = key[0].lower()
        if first_letter in letter_list: 
            letter_list[first_letter].append(key)
        else:
            letter_list[first_letter] = [key]
    return letter_list


def update_attendance(attendance_log: dict[str, list[str]], dayofw: str, at_class: str) -> None:
    """Record attendance of students and pass new attendance information."""
    if dayofw in attendance_log and at_class in attendance_log:
        attendance_log[dayofw].append(at_class)
    elif dayofw in attendance_log:
        attendance_log[dayofw].append(at_class)
    else:
        attendance_log[dayofw] = [at_class]