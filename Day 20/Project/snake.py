import turtle as t
import time

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        x = 0
        y = 0
        self.snake = []
        for i in range(3):
            self.grow(x, y)
            x -= 20

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setposition(self.snake[i - 1].position())
            self.snake[i].setheading(self.snake[i - 1].heading())
        self.snake[0].forward(20)

    def turn_up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def turn_down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def turn_left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def turn_right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def grow(self, x, y):
        self.snake.append(t.Turtle())
        self.snake[-1].penup()
        self.snake[-1].setposition(x, y)
        self.snake[-1].color("white")
        self.snake[-1].shape("square")
