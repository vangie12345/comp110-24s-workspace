"""One Shot Battleship Practice."""

__author__ = "730418328"


grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
correct: bool = True 

row_guess: int = int(input("Guess a row: "))
if row_guess == 1 or row_guess == 2 or row_guess == 3 or row_guess == 4:
    column_guess: int = int(input("Guess a column: "))
    while correct == True: 
        if column_guess == secret_column and row_guess == secret_row: 
            print("Hit!")
            correct = False
        elif column_guess == 1 or column_guess == 3 or column_guess == 4:
            print("Miss!") 
            correct = False
        elif column_guess == secret_column and row_guess != secret_row:
            print("Miss!")
            correct = False
        else:
            while correct == True:
                error: int = int(input("The grid is only 4 by 4. Try again: "))
                if (error > 1) or (error < 4):
                    correct == False
                else: 
                    column_guess: int = int(input("Guess a column: "))
                    while correct == True: 
                        if column_guess == secret_column and row_guess == secret_row: 
                            print("Hit!")
                            correct = False
                        elif column_guess == 1 or column_guess == 3 or column_guess == 4:
                            print("Miss!") 
                            correct = False
                        elif column_guess == secret_column and row_guess != secret_row:
                            print("Miss!")
                            correct = False

else:
    while correct == True: 
        error: int = int(input("The grid is only 4 by 4. Try again: "))
        if error < 1 or error > 4:
            j# ??input(error) 
        else:
            correct == True 
    column_guess: str = input("Guess a column: ")




    # while (guess < 1) or (guess > 4)



# set a result variable: if statement for blue or white 
#     if secret column == guess, then print this... else: print this box
# # set counter variable: int: counter = 1
#     # counter += 1
#     # to exit the while loop 
#     when counter < 5 (counter = 1)
#         functionality is over
#         counter += 1
    

    lines: 75 lines 

    print grid before hit or miss

    use counter variables!



   line 57-66
 # while (row_guess != secret_row):
#     index: int = 1
#     while index <= grid_size:
#         if column_guess == index:
#             print(f" { WHITE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
#         else: 
#             print(f" { BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }{ BLUE_BOX }")
#         index += 1
#     print("Miss!")
#     quit()


    