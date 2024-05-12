FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(x=-230, y=260)
        self.color("black")
        self.update()

    def update(self):
        self.write(f"Level:{self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.clear()
        self.home()
        self.write(f"     GAME OVER\nyou reached level:{self.level}", align="center", font=FONT)
