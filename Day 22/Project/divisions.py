import turtle as t

STRETCH_WIDTH = .5
STRETCH_HEIGHT = .25
SKIP = 25


class Bar(t.Turtle):
    def __init__(self):
        super().__init__()
        super().penup()
        super().shape("square")
        super().color("white")
        super().shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_HEIGHT)


class Divisions:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Dividing line of dashes
        self.vertical_bars = []
        for i in range(-height // 2, height // 2, SKIP):
            next_bar = Bar()
            next_bar.sety(i);
            self.vertical_bars.append(next_bar)