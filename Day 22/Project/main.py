import turtle as t
import time
from paddle import Paddle
from ball import Ball
from score import Score
from divisions import Divisions

WIDTH = 300
HEIGHT = 300
PADDLE_WIDTH = 20
BALL_WIDTH = 20
DELTA = 5
SCORE_LIMIT = 5

screen = t.Screen()
screen.screensize(canvwidth=WIDTH * 2, canvheight=HEIGHT * 2, bg="black")
screen.tracer(n=0)

left_paddle = Paddle(which_side="left", width=screen.canvwidth * 2, height=screen.canvheight * 2)
right_paddle = Paddle(which_side="right", width=screen.canvwidth * 2, height=screen.canvheight * 2)
LEFT_PADDLE_BALL_COLLISION_X_LOCATION = left_paddle.paddle_body[0].xcor() + PADDLE_WIDTH / 2
RIGHT_PADDLE_BALL_COLLISION_X_LOCATION = right_paddle.paddle_body[0].xcor() - PADDLE_WIDTH / 2

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

def paddle_ball_collision(left_pad, right_pad, ball_obj):
    if ball_obj.xcor() < 0:
        if abs((ball_obj.xcor() - BALL_WIDTH / 2) - (LEFT_PADDLE_BALL_COLLISION_X_LOCATION)) < DELTA:
            if ball_obj.ycor() > left_pad.bottom.ycor() - PADDLE_WIDTH / 2 and \
                ball_obj.ycor() < left_pad.top.ycor() + PADDLE_WIDTH / 2:
                ball_obj.bounce_left_or_right()
    elif ball_obj.xcor() > 0:
        if abs((ball_obj.xcor() + BALL_WIDTH / 2) - (RIGHT_PADDLE_BALL_COLLISION_X_LOCATION)) < DELTA:
            if ball_obj.ycor() > right_pad.bottom.ycor() - PADDLE_WIDTH / 2 and \
                ball_obj.ycor() < right_pad.top.ycor() + PADDLE_WIDTH / 2:
                ball_obj.bounce_left_or_right()



game_is_on = True
while game_is_on:
    screen.update()
    side_scored = ball.move_ball()
    paddle_ball_collision(left_paddle, right_paddle, ball)
    if side_scored == "left":
        left_score.update_score()
    elif side_scored == "right":
        right_score.update_score()
    if left_score.score == SCORE_LIMIT:
        winner_side = "Left"
        game_is_on = False
    elif right_score.score == SCORE_LIMIT:
        winner_side = "Right"
        game_is_on = False
    time.sleep(.01)
winner = t.Turtle()
winner.color("white")
winner.hideturtle()
winner.write(arg=f"{winner_side} wins!", align="center", font=("Arial", 48, "bold"))
screen.update()

screen.exitonclick()