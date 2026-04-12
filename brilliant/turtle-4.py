"""Test Turtle from https://docs.python.org/fr/3/library/turtle.html"""

import turtle

turtle.width(3)
turtle.speed(0)


# how to draw a centered circle
def draw_circle(radius):
    turtle.penup()
    turtle.forward(radius)
    turtle.pendown()
    turtle.left(90)
    for _ in range(60):
        turtle.forward(3.14 * radius / 30)
        turtle.left(6)
    turtle.right(90)
    turtle.penup()
    turtle.back(radius)


# how to draw an eye
def eye():
    turtle.color("orange", "white")
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


def right_arc(radius, angle):
    for _ in range(angle):
        turtle.forward(2 * 3.14 * radius / 360)
        turtle.right(1)


def centered_arc(radius, angle):
    turtle.penup()
    turtle.left(angle / 2)
    turtle.forward(radius)
    turtle.right(90)
    turtle.pendown()
    right_arc(radius, angle)
    turtle.penup()
    turtle.left(90)
    turtle.back(radius)
    turtle.left(angle / 2)


# drawing the head
turtle.color("orange", "yellow")
turtle.begin_fill()
draw_circle(300)
turtle.end_fill()

# drawing the left eye
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(100)
turtle.right(270)
eye()

# drawing the right eye
turtle.left(90)
turtle.forward(200)
turtle.right(90)
eye()

# move back into the middle
turtle.right(90)
turtle.forward(100)
turtle.left(90)

# drawing the mouth
turtle.width(15)
turtle.forward(200)
# turtle.left(180)
turtle.color("red")
centered_arc(50, 180)

turtle.hideturtle()
turtle.exitonclick()
