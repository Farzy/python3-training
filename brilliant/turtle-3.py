"""Test Turtle from https://docs.python.org/fr/3/library/turtle.html"""

import turtle

turtle.width(2)


def draw_circle(radius):
    turtle.penup()
    turtle.forward(radius)
    turtle.pendown()
    turtle.left(90)
    turtle.begin_fill()
    for _ in range(60):
        turtle.forward(3.14 * radius / 30)
        turtle.left(6)
    turtle.end_fill()
    turtle.right(90)
    turtle.penup()
    turtle.back(radius)
    turtle.pendown()


def eye():
    # white of the eye
    turtle.color("black", "white")
    turtle.begin_fill()
    draw_circle(50)
    turtle.end_fill()
    turtle.forward(25)
    # pupil
    turtle.color("black", "black")
    turtle.begin_fill()
    draw_circle(25)
    turtle.end_fill()
    turtle.back(25)


# your code here
turtle.color("red", "antique white")
draw_circle(200)

turtle.penup()
turtle.left(140)
turtle.forward(70)
turtle.pendown()
eye()
turtle.penup()
turtle.back(70)
turtle.right(100)
turtle.forward(70)
turtle.pendown()
eye()

turtle.hideturtle()
turtle.exitonclick()
