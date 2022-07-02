import turtle as t

SEGMENT_SIZE = 20
NUM_SEGMENTS_IN_PADDLE = 6
PERCENT_OF_SCREEN_WIDTH = .9
PERCENT_OF_SCREEN_HEIGHT = .667
PERCENT_AWAY_EDGE = .2
UP = 90
DOWN = 270
INCREMENT = SEGMENT_SIZE


class PaddleSegment(t.Turtle):
    def __init__(self, which_segment):
        """ which_segment is 0, 1, or 2"""
        super().__init__()
        super().penup()
        super().shape("square")
        super().color("white")
        # Decreases y coordinate for each new segment to eventually form a rectangular paddle
        super().sety(super().ycor() - SEGMENT_SIZE * which_segment)


class Paddle:
    def __init__(self, which_side, width, height):
        self.width = width
        self.height = height
        self.paddle_body = []
        for i in range(NUM_SEGMENTS_IN_PADDLE):
            # Adds segments each with lower y values to form a whole paddle
            segment = PaddleSegment(i)
            self.paddle_body.append(segment)
        self.top = self.paddle_body[0]
        self.bottom = self.paddle_body[-1]
        for segment in self.paddle_body:
            if which_side == "left":
                # Positioning the left paddle
                segment.setx((PERCENT_OF_SCREEN_WIDTH * (-self.width / 2)) + (self.width / 2) * PERCENT_AWAY_EDGE)
            elif which_side == "right":
                # Positioning the right paddle
                segment.setx((PERCENT_OF_SCREEN_WIDTH * (self.width / 2)) - (self.width / 2) * PERCENT_AWAY_EDGE)

    def move_up(self):
        # Cannot move above the top of the screen
        if self.top.ycor() + INCREMENT <= PERCENT_OF_SCREEN_HEIGHT * (self.height / 2):
            for segment in self.paddle_body:
                segment.setheading(UP)
                segment.forward(INCREMENT)

    def move_down(self):
        # Cannot move below the bottom of the screen
        if self.bottom.ycor() - INCREMENT >= PERCENT_OF_SCREEN_HEIGHT * (-self.height / 2):
            for segment in self.paddle_body:
                segment.setheading(DOWN)
                segment.forward(INCREMENT)

