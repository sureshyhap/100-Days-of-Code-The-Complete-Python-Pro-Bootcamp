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

snake_obj = Snake()
food_obj = Food(screen)
scoreboard_obj = Scoreboard()

screen.listen()
screen.onkey(snake_obj.turn_up, "Up")
screen.onkey(snake_obj.turn_down, "Down")
screen.onkey(snake_obj.turn_left, "Left")
screen.onkey(snake_obj.turn_right, "Right")


def wall_collision(snake):
    return snake.snake[0].xcor() > WIDTH // 2 or snake.snake[0].xcor() < -WIDTH // 2 or \
        snake.snake[0].ycor() > HEIGHT // 2 or snake.snake[0].ycor() < -HEIGHT // 2


def tail_collision(snake):
    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) <= 10:
            return True
    return False


def food_collision(snake, food):
    return snake.snake[0].distance(food) <= 15


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake_obj.move()
    # Collision with wall
    if wall_collision(snake_obj):
        game_is_on = False
    # Collision with tail
    if tail_collision(snake_obj):
        game_is_on = False
    # Collision with food
    if food_collision(snake_obj, food_obj):
        scoreboard_obj.update_score()
        snake_obj.growth()
        food_obj.set_random_position()
scoreboard_obj.game_over()


screen.exitonclick()
