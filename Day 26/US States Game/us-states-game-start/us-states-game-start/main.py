import turtle as t
import pandas
from name import Name

screen = t.Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.register_shape(image)
map = t.Turtle()
map.shape(image)

df = pandas.read_csv("50_states.csv")

num_correct = 0
game_is_on = True
already_guessed = []
while game_is_on:
    guess = screen.textinput(title=f"{num_correct}/50 States Correct", prompt="What's another state name?").title()
    if guess == "Exit":
        remaining = [state for state in df.state if state not in already_guessed]
        pandas.Series(remaining).to_csv("remaining.csv")
        exit()
    for state in df["state"]:
        if guess == state:
            if guess in already_guessed:
                break
            else:
                already_guessed.append(guess)
            num_correct += 1
            row = df[df.state == state]
            Name(row.state.item(), int(row.x), int(row.y))
    if num_correct == 50:
        game_is_on = False
game_over = t.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.setposition(-125, 0)
game_over.write("You Win!", font=("Arial", 40, "bold"))

screen.exitonclick()