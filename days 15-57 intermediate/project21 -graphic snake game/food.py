from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # creating 10X10 circle
        self.color("yellow")
        self.speed("fastest")
        self.food_relocated()

    def food_relocated(self):
        """generate new food in random location"""
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

