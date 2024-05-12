from turtle import Turtle

RIGHT_PADDLE_POS = (350, 0)
LEFT_PADDLE_POS = (-350, 0)
paddle = []
MOVE_STEP = 50
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)
        self.setheading(90)

    # def create_paddle(self, position):
    #     self.penup()
    #     self.shape("square")
    #     self.color("white")
    #     self.shapesize(stretch_wid=1, stretch_len=5)
    #     self.goto(position)
    #     self.setheading(90)

    def up(self):
        if not self.ycor() > 240:
            self.setheading(UP)
            self.forward(MOVE_STEP)

    def down(self):
        if not self.ycor() < -240:
            self.setheading(DOWN)
            self.forward(MOVE_STEP)
