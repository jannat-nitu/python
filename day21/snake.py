from turtle import Turtle

STARTING = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.SEGMENTS = []
        self.create_snake()
        self.head = self.SEGMENTS[0]

    def create_snake(self):
        for position in STARTING:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.SEGMENTS.append(snake)

    def snake_reset(self):
        for seg in self.SEGMENTS:
            seg.goto(1000, 1000)
        self.SEGMENTS.clear()
        self.create_snake()
        self.head = self.SEGMENTS[0]


    def extend(self):
        self.add_segment(self.SEGMENTS[-1].position())

    def move(self):
        for segment in range(len(self.SEGMENTS) - 1, 0, -1):
            x_seg = self.SEGMENTS[segment - 1].xcor()
            y_seg = self.SEGMENTS[segment - 1].ycor()
            self.SEGMENTS[segment].goto(x_seg, y_seg)
        self.SEGMENTS[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.SEGMENTS[0].heading() != 270:
            self.SEGMENTS[0].setheading(90)

    def down(self):
        if self.SEGMENTS[0].heading() != 90:
            self.SEGMENTS[0].setheading(270)

    def left(self):
        if self.SEGMENTS[0].heading() != 0:
            self.SEGMENTS[0].setheading(180)

    def right(self):
        if self.SEGMENTS[0].heading() != 180:
            self.SEGMENTS[0].setheading(0)
