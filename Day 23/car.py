import turtle as t
import random

LEFT = 180
CAR_MOVE_AMOUNT = 5
STARTING_CAR_OFFSET = .8
CAR_SIZE = 2


class Car(t.Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.car_size = CAR_SIZE
        self.colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        super().color(random.choice(self.colors))
        super().penup()
        super().shape("square")
        super().shapesize(stretch_len=self.car_size)
        super().setheading(LEFT)
        self.x = random.randint(-self.width / 2, self.width / 2)
        self.y = random.randint(STARTING_CAR_OFFSET * (-self.height / 2), STARTING_CAR_OFFSET * (self.height / 2))
        super().setposition(self.x, self.y)

    def move_left(self):
        super().forward(CAR_MOVE_AMOUNT)
        # If reached left side, move the car to the right side with a random y coordinate
        if abs(super().xcor() - -self.width / 2) < 20:
            self.x = self.width / 2
            self.y = random.randint(STARTING_CAR_OFFSET * (-self.height / 2), STARTING_CAR_OFFSET * (self.height / 2))
            super().setposition(self.x, self.y)


