import turtle, random

timmy = turtle.Turtle()

for sides in range(3, 11):
    each_interior_angle = 180 * (sides - 2) / sides
    timmy.pencolor(random.random(), random.random(), random.random())
    for i in range(sides):
        timmy.forward(100)
        turning_angle = 180 - each_interior_angle
        timmy.right(turning_angle)


screen = turtle.Screen()
screen.exitonclick()