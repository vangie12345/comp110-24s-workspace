""""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730418328"


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

p1_game: str = input("Pick a secret boat location between 1 and 4: ")
if int(p1_game) > 4:
    print("Error! " + p1_game + " too high! ")
    exit()
if int(p1_game) < 1:
    print("Error! " + p1_game + " too low! ")
    exit()
if int(p1_game) == "1" or "2" or "3" or "4" :

    p2_game: str = input("Guess a number between 1 and 4: ")
    if int(p2_game) > 4:
        print("Error! " + p2_game + " too high! ")
    if int(p2_game) < 1:
        print("Error! " + p2_game + " too low! ")
    if int(p2_game) == int(p1_game):
        print(RED_BOX)
        print("Correct! You hit the ship. ")
    if int(p2_game) != int(p1_game):
        print("Incorrect! You missed the ship.")

