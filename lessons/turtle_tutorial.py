from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

i: int = 0
while i < 4:
    leo.forward(50)
    leo.right(90)
    i = i + 1
leo.penup()
leo.goto(45,60)
leo.pendown()
i: int = 0
while i < 4:
    leo.forward(50)
    leo.right(90)
    i = i + 1
done()