"""Test Turtle from https://docs.python.org/fr/3/library/turtle.html"""
from turtle import *


title("Bonjour !")
speed(0)
color('blue', 'green')
pensize(3)

for i in range(1,20):
    circle(10 * i, 180)
    stamp()

write("Coucou !")
print(pen()['pencolor'])
hideturtle()
exitonclick()
