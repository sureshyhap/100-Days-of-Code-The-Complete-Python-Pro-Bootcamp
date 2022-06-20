import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_counter_clock():
    tim.left(5)


def turn_clock():
    tim.right(5)


def clear():
    tim.reset()


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_counter_clock, key="a")
screen.onkey(fun=turn_clock, key="d")
screen.onkey(fun=clear, key="c")
screen.exitonclick()