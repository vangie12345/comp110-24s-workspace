"""Example functions to learn definition and calling syntax."""

def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out of two numbers."""
    if number1 >= number2:
        return number1
    else: #number1 < number2
        return number2
    
max_number: int = my_max(1,10)
other_max_number: int = my_max(11,3)
print(other_max_number) 


def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string."""
    return my_words

def main():
    """Main code of program"""
    y: float = double(2.0)
    print(halve(y))

def halve(x:float) -> float:
    """Returns half the value of x"""
    print(f"halve({x})")
    return x / 2.0

def double(x:float) -> float:
    """Double a value"""
    print(f"double({x})")
    return x * 2.0
