import turtle

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("red")
for i in range(4):
    tim.forward(100)
    tim.right(90)

screen = turtle.Screen()
screen.exitonclick()