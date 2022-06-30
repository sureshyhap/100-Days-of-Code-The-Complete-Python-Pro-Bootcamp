import turtle as t

WIDTH = 600

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(0, WIDTH // 2 - 20)
        self.color("white")
        self.hideturtle()
        self.score = -1
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", \
                   font=("Arial", 16, "bold"))

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", \
                   font=("Arial", 16, "bold"))