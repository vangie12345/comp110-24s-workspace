"""Number guessing game."""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False 

while correct == False: #not correct
    guess: int = int(input("Guess a number: "))
#SECRET is a constant - as the program runs, for the entirety of the program. but each time it's run again, it will reset.
     
    if guess == SECRET: 
        print(f"You got it right! {guess} is the secret number!")
        #f string take str(guess) to {guess}
        correct = True
    elif guess > 10:    
        print("Error! " + str(guess) + " is too high!")
    elif guess < 1:
         print("Error! " + str(guess) + " is too low!")
    else:
        print("Try again!")
