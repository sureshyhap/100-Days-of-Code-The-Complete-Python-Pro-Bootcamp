import turtle

tim = turtle.Turtle()
for i in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)


screen = turtle.Screen()
screen.exitonclick()