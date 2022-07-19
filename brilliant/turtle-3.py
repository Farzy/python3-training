"""Test Turtle from https://docs.python.org/fr/3/library/turtle.html"""

from turtle import *

from turtle import *

width(2)


def circle(radius):
    penup()
    forward(radius)
    pendown()
    left(90)
    begin_fill()
    for i in range(60):
        forward(3.14 * radius / 30)
        left(6)
    end_fill()
    right(90)
    penup()
    back(radius)
    pendown()


def eye():
    # white of the eye
    color('black', 'white')
    begin_fill()
    circle(50)
    end_fill()
    forward(25)
    # pupil
    color('black', 'black')
    begin_fill()
    circle(25)
    end_fill()
    back(25)

# your code here
color('red','antique white')
circle(200)

penup()
left(140)
forward(70)
pendown()
eye()
penup()
back(70)
right(100)
forward(70)
pendown()
eye()

hideturtle()
exitonclick()
