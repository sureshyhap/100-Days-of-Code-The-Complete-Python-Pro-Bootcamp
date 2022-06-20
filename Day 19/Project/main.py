import turtle as t
import random

WIDTH = 600
HEIGHT = 300

turtles = {
    "red" : t.Turtle(),
    "orange" : t.Turtle(),
    "yellow" : t.Turtle(),
    "green" : t.Turtle(),
    "blue" : t.Turtle(),
    "purple" : t.Turtle()
}

screen = t.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
predicted_winner = screen.textinput(title="Make your bet",prompt="Who will win the race? Enter a color: ")

x_pos = -WIDTH / 2 + WIDTH * .05
y_pos = -120
for color, turt in turtles.items():
    turt.penup()
    turt.color(color)
    turt.shape("turtle")
    turt.setposition(x_pos, y_pos)
    y_pos += 40


race_not_over = True
while race_not_over:
    for color, turt in turtles.items():
        turt.forward(random.randrange(11))
        if turt.xcor() > (WIDTH / 2 - (40 / 2)):
            race_not_over = False
            winner = color
            break

if winner == predicted_winner:
    print(f"You win! Winner is {winner}!")
else:
    print(f"You lose. Winner is {winner}.")

screen.exitonclick()