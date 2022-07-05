import turtle as t

class Score(t.Turtle):
    def __init__(self, level, width, height):
        super().__init__()
        self.level = level
        super().hideturtle()
        super().penup()
        super().setposition(.9 * (-width / 2), .8 * (height / 2))
        self.update_level(level)

    def update_level(self, new_level):
        super().clear()
        self.level = new_level
        super().write(arg=f"Level: {self.level}", align="left", font=("Arial", 24, "bold"))