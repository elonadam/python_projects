from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.total_snake = []
        self.create_snake()
        self.head = self.total_snake[0]  # instead of calling total_snake[0] each time

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_new_part(position)

    def add_new_part(self, position):
        """extend the snake in one part"""
        snake_part = Turtle(shape="square")
        snake_part.color("beige")
        snake_part.penup()
        snake_part.goto(position)
        self.total_snake.append(snake_part)

    def extend(self):  # add new part to tail
        self.add_new_part(self.total_snake[-1].position())

    def move(self):
        """changing the location of the parts from tail to head
        each part moving to the last location of the previous"""
        for snake_part in range(len(self.total_snake) - 1, 0, -1):  # start, stop, step
            new_x = self.total_snake[snake_part - 1].xcor()
            new_y = self.total_snake[snake_part - 1].ycor()
            self.total_snake[snake_part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

