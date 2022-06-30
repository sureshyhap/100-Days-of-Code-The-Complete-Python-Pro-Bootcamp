import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

screen = t.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(n=0)

snake = Snake()
food = Food(screen)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    # Collision with wall
    if snake.snake[0].xcor() > WIDTH // 2 or snake.snake[0].xcor() < -WIDTH // 2 or \
        snake.snake[0].ycor() > HEIGHT // 2 or snake.snake[0].ycor() < -HEIGHT // 2:
        game_is_on = False
    # Collision with tail
    for i in range(1, len(snake.snake)):
        if snake.snake[0].distance(snake.snake[i]) < 15:
            game_is_on = False
            break
    # Collision with food
    if snake.snake[0].distance(food) <= 15:
        scoreboard.update_score()
        if snake.snake[-1].heading() == RIGHT:
            snake.grow(snake.snake[-1].xcor() - 20, snake.snake[-1].ycor())
        elif snake.snake[-1].heading() == LEFT:
            snake.grow(snake.snake[-1].xcor() + 20, snake.snake[-1].ycor())
        elif snake.snake[-1].heading() == UP:
            snake.grow(snake.snake[-1].xcor(), snake.snake[-1].ycor() - 20)
        elif snake.snake[-1].heading() == DOWN:
            snake.grow(snake.snake[-1].xcor(), snake.snake[-1].ycor() + 20)
        food.set_random_position()
scoreboard.game_over()


screen.exitonclick()