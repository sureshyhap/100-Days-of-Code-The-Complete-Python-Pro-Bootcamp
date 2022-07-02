import turtle as t

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
        self.last_input = None

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setposition(self.snake[i - 1].position())
            self.snake[i].setheading(self.snake[i - 1].heading())
        self.snake[0].forward(20)
        self.last_input = self.snake[0].heading()

    def turn_up(self):
        if self.last_input != DOWN:
            self.snake[0].setheading(UP)

    def turn_down(self):
        if self.last_input != UP:
            self.snake[0].setheading(DOWN)

    def turn_left(self):
        if self.last_input != RIGHT:
            self.snake[0].setheading(LEFT)

    def turn_right(self):
        if self.last_input != LEFT:
            self.snake[0].setheading(RIGHT)

    def grow(self, x, y):
        self.snake.append(t.Turtle())
        self.snake[-1].penup()
        self.snake[-1].setposition(x, y)
        self.snake[-1].color("white")
        self.snake[-1].shape("square")

    def growth(self):
        if self.snake[-1].heading() == RIGHT:
            self.grow(self.snake[-1].xcor() - 20, self.snake[-1].ycor())
        elif self.snake[-1].heading() == LEFT:
            self.grow(self.snake[-1].xcor() + 20, self.snake[-1].ycor())
        elif self.snake[-1].heading() == UP:
            self.grow(self.snake[-1].xcor(), self.snake[-1].ycor() - 20)
        elif self.snake[-1].heading() == DOWN:
            self.grow(self.snake[-1].xcor(), self.snake[-1].ycor() + 20)
