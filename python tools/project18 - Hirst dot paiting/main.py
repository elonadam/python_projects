# day 18/100 of coding, recreating Hirst dot painting.
# used colorgram to extract the original colors from the painting, lines 8-16

import colorgram
import random
from turtle import Turtle, Screen

tommy = Turtle()
# colors = colorgram.extract('image.jpg', 120)
# colors_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     curr_rgb = (r , g, b)
#     colors_list.append(curr_rgb)

color_bank = [
    (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
    (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64),
    (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77),
    (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158),
    (235, 166, 171), (177, 204, 185), (49, 62, 84), (164, 203, 208), (183, 190, 204), (83, 70, 40),
    (11, 112, 106)
]

def change_color():
    color = random.choice(color_bank)
    tommy.pencolor(color[0] / 255, color[1] / 255, color[2] / 255)

def draw_dots_line():
    tommy.hideturtle()
    start_place = -200
    new_row_place = -200
    tommy.penup()
    tommy.goto(start_place,new_row_place)
    tommy.pensize(20)
    for column in range(10):
        for i in range(10):
            change_color()  # bug
            tommy.pendown()
            tommy.forward(0)
            tommy.penup()
            tommy.forward(50)
            tommy.pendown()
        tommy.penup()
        new_row_place += 50
        tommy.goto(start_place, new_row_place)


draw_dots_line()
screen = Screen()
screen.exitonclick()
