"""EX01 - Simply Battleship - A cute step toward Battleship."""

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
# if int(p1_game) == "1" or "2" or "3" or "4":

p2_game: str = input("Guess a number between 1 and 4: ")
if int(p2_game) > 4:
    print("Error! " + p2_game + " too high! ")
    exit()
if int(p2_game) < 1:
    print("Error! " + p2_game + " too low! ")
    exit()
if int(p2_game) == int(p1_game) == 1: 
    print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    print("Correct! You hit the ship. ")
if int(p2_game) == int(p1_game) == 2: 
    print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
    print("Correct! You hit the ship. ")
if int(p2_game) == int(p1_game) == 3: 
    print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
    print("Correct! You hit the ship. ")
if int(p2_game) == int(p1_game) == 4: 
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
    print("Correct! You hit the ship. ")
if int(p1_game) != int(p2_game) and int(p2_game) == 1: 
    print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
if int(p1_game) != int(p2_game) and int(p2_game) == 2: 
    print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
if int(p1_game) != int(p2_game) and int(p2_game) == 3: 
    print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
if int(p1_game) != int(p2_game) and int(p2_game) == 4: 
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)
if int(p2_game) != int(p1_game): 
    print("Incorrect! You missed the ship.")
