import turtle as t

PERCENT_OF_SCREEN_WIDTH = .3
PERCENT_OF_SCREEN_HEIGHT = 1.0

class Score(t.Turtle):
    def __init__(self, which_side, width, height):
        super().__init__()
        self.score = 0
        self.which_side = which_side
        self.width = width
        self.height = height
        super().hideturtle()
        super().penup()
        super().color("white")
        if self.which_side == "left":
            super().setx(PERCENT_OF_SCREEN_WIDTH * (-self.width / 2))
            super().sety(PERCENT_OF_SCREEN_HEIGHT * (self.height / 2))
        elif self.which_side == "right":
            super().setx(PERCENT_OF_SCREEN_WIDTH * (self.width / 2))
            super().sety(PERCENT_OF_SCREEN_HEIGHT * (self.height / 2))
        super().write(arg=f"{self.score}", align=self.which_side, font=("Arial", 48, "bold"))

    def update_score(self):
        self.score += 1
        super().clear()
        super().write(arg=f"{self.score}", align=self.which_side, font=("Arial", 48, "bold"))