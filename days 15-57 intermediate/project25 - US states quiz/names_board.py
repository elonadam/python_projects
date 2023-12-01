FONT = ("Courier", 12, "bold")
ALIGNMENT = "center"

from turtle import Turtle


class NamesBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")

    def write_name(self, x, y, state_name):
        self.goto(x, y)
        self.write(state_name, align=ALIGNMENT, font=FONT)
