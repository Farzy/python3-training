"""Test Turtle from https://docs.python.org/fr/3/library/turtle.html"""

from turtle import *

from turtle import *

from turtle import *

width(3)
speed(0)


# how to draw a centered circle
def circle(radius):
    penup()
    forward(radius)
    pendown()
    left(90)
    for i in range(60):
        forward(3.14*radius/30)
        left(6)
    right(90)
    penup()
    back(radius)


# how to draw an eye
def eye():
    color('orange', 'white')
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


def right_arc(radius, angle):
    for i in range(angle):
        forward(2*3.14*radius/360)
        right(1)


def centered_arc(radius, angle):
    penup()
    left(angle/2)
    forward(radius)
    right(90)
    pendown()
    right_arc(radius, angle)
    penup()
    left(90)
    back(radius)
    left(angle/2)


# drawing the head
color('orange', 'yellow')
begin_fill()
circle(300)
end_fill()

# drawing the left eye
left(90)
forward(150)
left(90)
forward(100)
right(270)
eye()

# drawing the right eye
left(90)
forward(200)
right(90)
eye()

# move back into the middle
right(90)
forward(100)
left(90)

# drawing the mouth
width(15)
forward(200)
# left(180)
color('red')
centered_arc(50, 180)

hideturtle()
exitonclick()
