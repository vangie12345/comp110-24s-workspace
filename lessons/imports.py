"""The File where I import stuff!"""

from lessons import my_functions

# __name__ = "__main__"
print(my_functions.add(4,5))
#it prints out everything from the module you bring in 

print(my_functions.my_variable)

______________________________________________________________

# or to make things simpler 
from lessons.my_functions import add, my_variable 

# __name__ = "__main__"
print(add(4,5))

print(my_variable)

