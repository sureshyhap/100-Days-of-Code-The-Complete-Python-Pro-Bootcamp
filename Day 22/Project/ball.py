import turtle as t
import random

BALL_SPEED = 1
BALL_WIDTH = 20
PERCENT_OF_SCREEN_HEIGHT = .667
PERCENT_OF_SCREEN_WIDTH = .9
FULL_CIRCLE_DEGREES = 360

class Ball(t.Turtle):
    def __init__(self, width, height):
        super().__init__()
        super().penup()
        super().shape("square")
        super().color("white")
        random_direction = random.randrange(360)
        super().setheading(random_direction)
        super().settiltangle(-random_direction)
        self.width = width
        self.height = height

    def move_ball(self):
        if super().xcor() >= self.width / 2:
            super().reset()
            self.__init__(self.width, self.height)
            return "left"
        elif super().xcor() <= -self.width / 2:
            super().reset()
            self.__init__(self.width, self.height)
            return "right"
        if super().ycor() + (BALL_WIDTH / 2) + BALL_SPEED <= PERCENT_OF_SCREEN_HEIGHT * (self.height / 2) and \
                super().ycor() - (BALL_WIDTH / 2) >= PERCENT_OF_SCREEN_HEIGHT * (-self.height / 2):
            super().forward(BALL_SPEED)
        else:
            self.bounce()
            super().forward(BALL_SPEED)

    def bounce(self):
        old_angle = super().heading()
        new_angle = FULL_CIRCLE_DEGREES - old_angle
        super().setheading(new_angle)
        super().settiltangle(-new_angle)