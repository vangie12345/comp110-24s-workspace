"""Practice writing a class."""

class Profile:

    username: str
    private: bool

    def __init__(self, username_input: str):
        """Create a new Profile object."""
        self.username = username_input
        self.private = True 

    # want it to be part of the class, so you indent it
    
    def tweet(self, msg: str) -> None: 
        """If profile is public, print msg."""
        if self.private is False: # not self.private
            print(msg)
        else:
            print("No")

"""Instantiating."""

# Create new variable "user1" that is reference to a Proile object with the username "110_rules"

# Update user1's provate attribute to be False

# Use the tweet method call to tweet the message "OOP is cool!"
user1: Profile = Profile("110_rules") # calls __init__()
user1.private = False # setting it to new thing - now False, before it was true. 
user1.tweet("OOP is cool!") 




Dong, Evangelina Jiayin
​
Thu 4/18/2024 3:24 PM
"""TODO: Describe your scene program."""

__author__ = "730399673"
 
from turtle import Turtle, colormode, done 


def draw_sun(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a sun at the given coordinates."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.color("yellow")
    a_turtle.begin_fill()
    a_turtle.circle(50)
    a_turtle.end_fill()


def draw_tree(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a tree at the given coordinates."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.color("green")
    a_turtle.begin_fill()
    a_turtle.forward(50)
    a_turtle.left(120)
    a_turtle.forward(100)
    a_turtle.left(120)
    a_turtle.forward(100)
    a_turtle.left(120)
    a_turtle.forward(50)
    a_turtle.end_fill()
    a_turtle.color("brown")
    a_turtle.begin_fill()
    a_turtle.left(225)
    a_turtle.forward(25)
    a_turtle.left(90)
    a_turtle.forward(50)
    a_turtle.left(90)
    a_turtle.forward(25)
    a_turtle.end_fill()


def draw_house(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a house at the given coordinates."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.color("blue")
    a_turtle.begin_fill()
    for _ in range(4):
        a_turtle.forward(100)
        a_turtle.left(90)
    a_turtle.end_fill()
    a_turtle.color("red")
    a_turtle.begin_fill()
    a_turtle.setheading(45)
    a_turtle.forward(70)
    a_turtle.setheading(0)
    a_turtle.forward(50)
    a_turtle.setheading(-45)
    a_turtle.forward(70)
    a_turtle.setheading(90)
    a_turtle.end_fill()


def draw_car(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a car at the given coordinates."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.color("yellow")
    a_turtle.begin_fill()
    a_turtle.forward(100)
    a_turtle.left(90)
    a_turtle.forward(20)
    a_turtle.left(90)
    a_turtle.forward(50)
    a_turtle.right(90)
    a_turtle.forward(100)
    a_turtle.right(90)
    a_turtle.forward(100)
    a_turtle.left(90)
    a_turtle.forward(100)
    a_turtle.left(90)
    a_turtle.forward(30)
    a_turtle.left(90)
    a_turtle.forward(20)
    a_turtle.end_fill()
    a_turtle.color("black")
    a_turtle.penup()
    a_turtle.goto(x + 25, y + 20)
    a_turtle.pendown()
    a_turtle.circle(15)
    a_turtle.penup()
    a_turtle.goto(x + 75, y + 20)
    a_turtle.pendown()
    a_turtle.circle(15)