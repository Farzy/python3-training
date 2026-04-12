"""Misc Python tests"""

import turtle

turtle.speed(0)

left_turn_angle = 45
nb_turn_steps = 20


def left_turn(length):
    for _ in range(nb_turn_steps):
        turtle.forward(length / nb_turn_steps)
        turtle.left(left_turn_angle / nb_turn_steps)


def petal(size):
    turtle.begin_fill()
    left_turn(size)
    turtle.left(180 - left_turn_angle)  # replace the magic number here...
    left_turn(size)
    turtle.left(180 - left_turn_angle)  # ...and here
    turtle.end_fill()


petal(100)

turtle.hideturtle()
turtle.exitonclick()
