import turtle as t
import time
from paddle import Paddle
from ball import Ball
from score import Score
from divisions import Divisions

WIDTH = 300
HEIGHT = 300

screen = t.Screen()
screen.screensize(canvwidth=WIDTH * 2, canvheight=HEIGHT * 2, bg="black")
screen.tracer(n=0)

left_paddle = Paddle(which_side="left", width=screen.canvwidth * 2, height=screen.canvheight * 2)
right_paddle = Paddle(which_side="right", width=screen.canvwidth * 2, height=screen.canvheight * 2)

ball = Ball(width=screen.canvwidth * 2, height=screen.canvheight * 2)

divisions = Divisions(width=screen.canvwidth * 2, height=screen.canvheight * 2)

left_score = Score(which_side="left", width=WIDTH * 2, height=HEIGHT * 2)
right_score = Score(which_side="right", width=WIDTH * 2, height=HEIGHT * 2)

screen.update()
screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    side_scored = ball.move_ball()
    if side_scored == "left":
        left_score.update_score()
    elif side_scored == "right":
        right_score.update_score()
    time.sleep(.01)


screen.exitonclick()