from turtle import Turtle
import random


COLORS = ["red", "orange", "grey", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def car_move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def traffic(self):
        rand_chance = random.randint(1, 4)
        if rand_chance == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            car.goto(300, rand_y)
            self.all_cars.append(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
