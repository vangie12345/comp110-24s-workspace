"""One Shot Battleship."""

__author__ = "730418328"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

row_guess: int = int(input("Guess a row: "))

while row_guess > grid_size:
    error: int = int(input(f"The grid is only { grid_size } by { grid_size }. Try again: "))
    row_guess = error
column_guess: int = int(input("Guess a column: "))

while column_guess > grid_size:
    error: int = int(input(f"The grid is only { grid_size } by { grid_size }. Try again: "))
    column_guess = error

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
    exit()

if (row_guess != secret_row) and (column_guess == secret_column):
    print("Close! Correct column, wrong row.")
    quit()

if (column_guess != secret_column) and (row_guess == secret_row):
    print("Close! Correct row, wrong column. ")
    quit()

if (column_guess != secret_column) and (row_guess != secret_row):
    print("Miss!")
    quit()


# while (row_guess == secret_row) and (column_guess != secret_column):
#     print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
#     print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
#     if column_guess == 1:
#         print(f" { WHITE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
#     elif column_guess == 3:
#         print(f" { BLUE_BOX }{ BLUE_BOX }{ WHITE_BOX }{ BLUE_BOX }")
#     else:
#         print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ WHITE_BOX }")
#     print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
#     # while index <= grid_size: 
#     #     if index != column_guess:
#     #         print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
#     #     else:
#     #         print(f" { BLUE_BOX }{ BLUE_BOX }{ WHITE_BOX }{ BLUE_BOX }")
#         # index += 1
#     print("Close! Correct row, wrong column. ")
#     quit()


# # while (row_guess != secret_row) and (column_guess != secret_column):
# #     index: int = 1
# #     while index <= grid_size:
# #         while row_guess == 1:
# #             if column_guess != 1:
# #                 print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# #             else:
# #                 print(f" { WHITE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# #             index += 1
# #         while row_guess == 2:
# #             if column_guess != 1:
# #                 print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# #             else:
# #                 print(f" { WHITE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# #             index += 1
# #         while row_guess == 1:
# #             if column_guess != 1:
# #                 print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# #             else:
# #                 print(f" { WHITE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# #             index += 1
# #         while row_guess == 1:
# #             if column_guess != 1:
# #                 print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# #             else:
# #                 print(f" { WHITE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# #             index += 1
# # index: int = 1

# # under correct_row guess: 3
# # while index <= grid_size: 
# #     if index == correct_row guess 
# #         print  
# #         index += 1
# #     else:
# #         print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# #         index += 1
# print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# print(f" { WHITE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# print(f" { BLUE_BOX }{ WHITE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# print(f" { BLUE_BOX }{ BLUE_BOX }{ WHITE_BOX }{ BLUE_BOX }")
# print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ WHITE_BOX }")
# print(f" { RED_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# print(f" { BLUE_BOX }{ RED_BOX }{ BLUE_BOX }{ BLUE_BOX }")
# print(f" { BLUE_BOX }{ BLUE_BOX }{ RED_BOX }{ BLUE_BOX }")
# print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ RED_BOX }")