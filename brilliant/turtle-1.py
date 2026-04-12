"""Test Turtle from https://docs.python.org/fr/3/library/turtle.html"""

import turtle

DEBUG = False
DIAMETER = 300

turtle.speed(10)
turtle.color("red", "yellow")

turtle.penup()
turtle.back(DIAMETER / 2)
turtle.pendown()
initial_pos = turtle.pos()

turtle.begin_fill()
while True:
    if DEBUG:
        print(f"{turtle.pos()}: {abs(turtle.pos())}")
    turtle.forward(DIAMETER)
    turtle.left(170)
    if abs(initial_pos - turtle.pos()) < 1:
        if DEBUG:
            print(f"{turtle.pos()}: {abs(turtle.pos())}")
        break
turtle.end_fill()
turtle.done()
