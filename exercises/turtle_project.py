"""Sunny day on the lawn."""

__author__ = "730418328"

from turtle import Turtle, colormode, done
colormode(255)

def draw_square(a_turtle: Turtle, x: float, y: float) -> None: 
    """Draw a sun shape."""
    i: int = 0
    while i < 4:
        a_turtle.goto(x, y)
        a_turtle.pendown()
        a_turtle.color()
        a_turtle.pencolor("blue")
        a_turtle.begin_fill()
        a_turtle.forward(x)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()

    i: int = 0
    while i < 15:
        a_turtle.color()
        a_turtle.pencolor("green")
        a_turtle.left(45)
        a_turtle.forward(x)
        a_turtle.right(150)
        a_turtle.forward(x)
        i = i + 1
        
    a_turtle.end_fill()

def draw_rays(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw rays of the sun."""
if __name__ == "__main__":
    a_turtle = Turtle()

    draw_tomato(a_turtle, 50, 30)
    done()



# def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
#     """Draw a square of the given width whose top-left corner is located at x, y."""
#     a_turtle.penup(Turtle)
#     a_turtle.goto(x, y) 
#     a_turtle.setheading(0.0)
#     a_turtle.pendown()
#     i: int = 0
#     while i < 5:
#         a_turtle.forward(width)
#         a_turtle.right(100)
#         i = i + 1