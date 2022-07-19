"""Test Turtle from https://docs.python.org/fr/3/library/turtle.html"""
from turtle import *

DEBUG = False
DIAMETER = 300

speed(10)
color('red', 'yellow')

penup()
back(DIAMETER / 2)
pendown()
initial_pos = pos()

begin_fill()
while True:
    if DEBUG:
        print(f"{pos()}: {abs(pos())}")
    forward(DIAMETER)
    left(170)
    if abs(initial_pos - pos()) < 1:
        if DEBUG:
            print(f"{pos()}: {abs(pos())}")
        break
end_fill()
done()
