"""Test Turtle from https://docs.python.org/fr/3/library/turtle.html"""

import turtle

turtle.title("Bonjour !")
turtle.speed(0)
turtle.color("blue", "green")
turtle.pensize(3)

for i in range(1, 20):
    turtle.circle(10 * i, 180)
    turtle.stamp()

turtle.write("Coucou !")
print(turtle.pen()["pencolor"])
turtle.hideturtle()
turtle.exitonclick()
