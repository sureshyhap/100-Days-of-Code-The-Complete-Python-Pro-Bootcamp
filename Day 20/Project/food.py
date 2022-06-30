import turtle as t
import random

class Food(t.Turtle):
    def __init__(self, screen):
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5, outline=1)
        self.bound_x = screen.canvwidth
        self.bound_y = screen.canvheight
        self.color("blue")
        self.speed("fastest")
        self.random_x = 0
        self.random_y = 0
        self.set_random_position()

    def set_random_position(self):
        self.random_x = random.randint(-self.bound_x // 2, self.bound_x // 2)
        self.random_y = random.randint(-self.bound_y // 2, self.bound_y // 2)
        self.setposition(self.random_x, self.random_y)