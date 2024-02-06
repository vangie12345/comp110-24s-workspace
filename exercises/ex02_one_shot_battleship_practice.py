"""EX02 One Shot Battleship."""

__author__ = "730418328"


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
correct: bool = False


grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

row_guess: int = input("Guess a row: ")
if row_guess < 1 or row_guess > 4: 
    error: str = input("The grid is only 4 by 4. Try again: ")
    print(error)
    while int(error) < 1 or int(error) > 4:
        print(error)
        if int(error) == 1 or int(error) == 2 or int(error) == 3 or int(error) == 4:
            column_guess: int = input("Guess a column: ")
            if column_guess == 2 and row_guess == 3:
                print("Hit!")
            elif column_guess == 2 and row_guess != 3:
                print("Miss!")
            else:
                print(error)


    while row_guess < 1 or row_guess > 4:
        input(error)
        if int(input(error)) < 1 or int(input(error)) > 4:
            int(row_guess) == int(input(error))
        while row_guess
        column_guess: int = int(input("Guess a column: "))
        if column_guess !=
            #go to line 33 
        elif column_guess > 4:
            input(error)
        if int(input(error)) < 1 or int(input(error)) > 4:
            print(error)
            
    else:   
        while correct == False: 
            column_guess: int = int(input("Guess a column: "))
            if column_guess < 1:
                print("The grid is only 4 by 4. Try again: ")
            elif column_guess > 4:
                print("The grid is only 4 by 4. Try again: ")
            else:
                if row_guess == 3 and column_guess == 2:
                    print("Hit!")
                    quit()
                else: 
                    print("Miss!")
                    quit()
                