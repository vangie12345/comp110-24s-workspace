"""Demonstrate Basic List Syntax."""

# initializing an empty list - <list name>: list[<item type>] - list()
# list() - called a "list constructor" : equivalent to [] (called a literal)
# example - grocery_list: list[str] - list()

#adding an item to a list - <list name>.append(<item>); this is a method (function that belongs to the list class) add things to the end of the list
# example - grocery_list.append("bananas")


# initialize an empty list
grocery_list: list[str] = list()
print(grocery_list)

# Add item to a list 
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

# Create an already populated list: you can have duplicates in a list
grocery_list2: list[str] = ["banannas", "milk", "bread"]
print("Populated list: ")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list)

# indexing: you can index with lists but not strings
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Print first element of string")
print(grocery_list[0])

# Modifying by index
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Before the change: ")
print(grocery_list2)
grocery_list2[1] = "almond milk"
print("After the change: ")
print(grocery_list2)

# Measuring length
print("Length of list: ")
print(len(grocery_list2))

# Removing an item
grocery_list2.pop(1) # pop is an argument to a method
print("After removing almond milk: ")
print(grocery_list2)

# Lists + Functions - functions can modify lists 
# Function name: display; Parameter: list[str]; Goal: print out the list

def display(word: list[str]) -> None: #signature
    print(word)

display(grocery_list)