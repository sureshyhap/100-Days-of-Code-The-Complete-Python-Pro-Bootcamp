import turtle as t
import time
from player import Player
from car import Car
from score import Score

WIDTH = 600
HEIGHT = 600
NUM_CARS = 20
SIZE_TURTLE = 20

screen = t.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(n=0)

player = Player(HEIGHT)
cars = []
for _ in range(NUM_CARS):
    cars.append(Car(WIDTH, HEIGHT))

screen.listen()
screen.onkeypress(player.move_up, "Up")


def player_car_collision(player_obj, car_obj):
    # Size of player and car
    car_width = car_obj.car_size * SIZE_TURTLE
    car_height = SIZE_TURTLE
    turtle_width = SIZE_TURTLE
    turtle_height = SIZE_TURTLE

    # Player boundaries
    turtle_left_x = player_obj.xcor() - turtle_width / 2
    turtle_right_x = player_obj.xcor() + turtle_width / 2
    turtle_bottom_y = player_obj.ycor() - turtle_height / 2
    turtle_top_y = player_obj.ycor() + turtle_height / 2

    # Car boundaries
    car_left_x = car_obj.xcor() - car_width / 2
    car_right_x = car_obj.xcor() + car_width / 2
    car_bottom_y = car_obj.ycor() - car_height / 2
    car_top_y = car_obj.ycor() + car_height / 2

    # If piece of player is within the car, collision has occurred
    if ((turtle_right_x >= car_left_x and turtle_left_x <= car_left_x) or \
             (turtle_left_x <= car_right_x and turtle_right_x >= car_right_x)) and \
            ((turtle_top_y >= car_bottom_y and turtle_bottom_y <= car_bottom_y) or \
             (turtle_bottom_y <= car_top_y and turtle_top_y >= car_top_y)) and \
            (player_obj.distance(car_obj) < (turtle_width / 2 + car_width / 2)):
        return True
    else:
        return False



game_is_on = True
level = 1
sleep_time = .1
score_turtle = Score(level, WIDTH, HEIGHT)
while game_is_on:
    screen.update()
    # Cars will constantly move left
    for car in cars:
        car.move_left()
        if player_car_collision(player, car):
            game_is_on = False
            break
        # If reached top of screen, reset position and increase level
        if player.ycor() > HEIGHT / 2:
            level += 1
            score_turtle.update_level(level)
            player.reset()
            player.__init__(HEIGHT)
            sleep_time /= 1.5
    time.sleep(sleep_time)
game_over_message = t.Turtle()
game_over_message.write("Game Over", align="center", font=("Arial", 36, "bold"))

screen.exitonclick()