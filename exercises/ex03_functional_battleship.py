"""EX03 - Functional Battleship."""

__author__ = "730418328"

import random 


def input_guess(gridsize: int, rowcol: str) -> int:
    """1st step: Setting Grid parameters."""
    assert rowcol == "row" or rowcol == "column"
    gridguess = int(input(f"Guess a { rowcol }: "))

    while (gridguess > gridsize) or (gridguess < 1):
        gridguess = int(input(f"The grid is only {gridsize} by {gridsize}. Try again: "))
    return gridguess


def print_grid(gridsize: int, rowguess: int, colguess: int, corr_guess: bool) -> None:
    """2nd step: Print Corresponding Boxes using code from Ex02."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"

    box_is: str = ""

    if corr_guess: 
        box_is += RED_BOX
    else:
        box_is += WHITE_BOX

    row_number: int = 1

    while row_number <= gridsize: 
        emoji: str = ""
        column_number: int = 1
        if rowguess == row_number:
            while column_number <= gridsize:
                if colguess == column_number:
                    emoji += box_is
                else:
                    emoji += BLUE_BOX
                column_number += 1 
        else:
            while column_number <= gridsize:
                emoji += BLUE_BOX
                column_number += 1
        print(emoji)
        row_number += 1


def correct_guess(secrow: int, seccol: int, rowguess: int, colguess: int) -> bool:
    """3rd step: True False Statements."""
    if rowguess == secrow and colguess == seccol:
        return True
    else:
        return False


def main(gridsize: int, secrow: int, seccol: int) -> None:
    """Final game."""
    game = 1
    win: bool = False
    '#when player wins, bool = true'

    while game < 6 and not win:
        print(f"=== Turn {game}/5 ===")
        rowguess: int = input_guess(gridsize, "row")
        colguess: int = input_guess(gridsize, "column")

        corr_guess: bool = correct_guess(secrow, seccol, rowguess, colguess)

        print_grid(gridsize, rowguess, colguess, corr_guess)

        if corr_guess:
            print("Hit!")
            print(f"You won in {game}/5 turns!")

            win = True
        else:
            print("Miss!")
            game += 1
            if game > 5:
                print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))