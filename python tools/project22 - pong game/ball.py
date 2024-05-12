from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("cyan")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self, border):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.75

    def reset_position(self):
        self.move_speed = 0.1
        self.home()
        self.x_bounce()
