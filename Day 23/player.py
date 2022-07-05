import turtle as t

UP = 90
START_OFFSET = 25
PLAYER_MOVE_AMOUNT = 10
STARTING_PLAYER_OFFSET = .9

class Player(t.Turtle):
    def __init__(self, height):
        super().__init__()
        super().shape("turtle")
        super().penup()
        super().setheading(90)
        super().sety(STARTING_PLAYER_OFFSET * (-height / 2))

    def move_up(self):
        super().forward(PLAYER_MOVE_AMOUNT)