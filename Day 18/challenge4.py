import turtle, random

timmy = turtle.Turtle()

timmy.pensize(15)
timmy.speed(10)
while True:
    turns = random.randrange(4)
    for i in range(turns):
        timmy.right(90)
    timmy.color(random.random(), random.random(), random.random())
    timmy.forward(25)

screen = turtle.Screen()
screen.exitonclick()