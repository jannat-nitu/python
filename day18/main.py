import turtle
from turtle import Turtle,Screen
import random
timmy = Turtle()
turtle.colormode(255)
colors = [(202, 164, 109), (238, 240, 245),
(150, 75, 49), (52, 93, 124), (140, 30, 19), (47, 94, 142)]
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
dots = 109
for dot in range(1, dots):
    timmy.dot(15, random.choice(colors))
    timmy.forward(30)
    if dot % 12 == 0:
      timmy.setheading(90)
      timmy.forward(30)
      timmy.setheading(180)
      timmy.forward(360)
      timmy.setheading(0)

my_screen = Screen()
my_screen.exitonclick()
