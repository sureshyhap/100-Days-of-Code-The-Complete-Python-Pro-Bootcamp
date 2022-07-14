import turtle as t

class Name(t.Turtle):
    def __init__(self, state_name, x, y):
        super().__init__()
        super().penup()
        super().hideturtle()
        super().setposition(x, y)
        super().write(state_name)


