"""Misc Python tests"""

from turtle import *
import math

speed(0)

left_turn_angle = 45
nb_turn_steps = 20

def left_turn(length):
    for i in range(nb_turn_steps):
        forward(length/nb_turn_steps)
        left(left_turn_angle/nb_turn_steps)

def petal(size):
    begin_fill()
    left_turn(size)
    left(180 - left_turn_angle) # replace the magic number here...
    left_turn(size)
    left(180 - left_turn_angle) # ...and here
    end_fill()

petal(100)

hideturtle()
exitonclick()
