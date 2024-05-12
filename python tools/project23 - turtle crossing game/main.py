import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.traffic()
    car_manager.car_move()

    # Detect if a car hit the player
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()



    # Detect if player passed the level
    if player.ycor() > 280:
        player.level_up()
        scoreboard.increase_level()
        car_manager.level_up()

screen.exitonclick()
