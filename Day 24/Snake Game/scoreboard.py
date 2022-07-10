import turtle as t

WIDTH = 600


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(0, WIDTH // 2 - 30)
        self.color("white")
        self.hideturtle()
        self.score = -1
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "bold"))

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center",
                   font=("Arial", 16, "bold"))


class HighScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", "r") as high_score_file:
            self.high_score = int(high_score_file.read())
        super().penup()
        super().setposition(0, -WIDTH // 2 + 30)
        super().color("white")
        super().hideturtle()
        self.update_score(self.high_score)

    def update_score(self, new_high_score):
        self.high_score = new_high_score
        super().clear()
        super().write(f"High Score: {self.high_score}", align="center", font=("Arial", 16, "bold"))
        with open("data.txt", mode="w") as high_score_file:
            high_score_file.write(str(self.high_score))
