import turtle, random

timmy = turtle.Turtle()
turtle.colormode(255)
timmy.speed("fastest")


def get_random_color():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return (r, g, b)


increment = 5
num_circles = 360 // increment
for i in range(num_circles):
    timmy.color(get_random_color())
    timmy.circle(100)
    timmy.left(increment)

screen = turtle.Screen()
screen.exitonclick()
