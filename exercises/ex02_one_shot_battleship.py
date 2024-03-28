"""One Shot Battleship."""
__author__ = "730418328"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

row_guess: int = int(input("Guess a row: "))

while (row_guess > grid_size) or (row_guess < 1):
    row_guess = int(input(f"The grid is only { grid_size } by { grid_size }. Try again: "))
    
column_guess: int = int(input("Guess a column: "))

while (column_guess > grid_size) or (column_guess < 1):
    column_guess = int(input(f"The grid is only { grid_size } by { grid_size }. Try again: "))

box_is: str = ""

if (row_guess == secret_row) and (column_guess == secret_column):
    box_is += RED_BOX
else:
    box_is += WHITE_BOX

row_number: int = 1

while row_number <= grid_size:
    emoji: str = ""
    column_number: int = 1
    if row_guess == row_number:
        while column_number <= grid_size:
            if column_guess == column_number:
                emoji += box_is
            else:
                emoji += BLUE_BOX
            column_number += 1 
    else:
        while column_number <= grid_size:
            emoji += BLUE_BOX
            column_number += 1
    print(emoji)
    row_number += 1
    

if (row_guess == secret_row) and (column_guess == secret_column):
    print("Hit!")

if (row_guess != secret_row) and (column_guess == secret_column):
    print("Close! Correct column, wrong row.")

if (column_guess != secret_column) and (row_guess == secret_row):
    print("Close! Correct row, wrong column. ")

if (column_guess != secret_column) and (row_guess != secret_row):
    print("Miss!")