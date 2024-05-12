from turtle import Turtle
ALIGNMENT = "center"
FONT = ("ROG fonts", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.goto(0, 260)
        self.color("beige")
        self.update()

    def update(self):
        self.write(f"{self.l_score} | {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, xcor):
        if xcor > 300:
            self.l_score += 1
        else:
            self.r_score += 1

        self.clear()
        self.update()
