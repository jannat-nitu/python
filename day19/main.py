import turtle
from turtle import Turtle, Screen
import random
is_race_on =False
screen = Screen()
screen.setup(width=800, height=600)
user_input = screen.textinput("What is your turtle color?: ", "which color you bet for")
colors = ["red", "orange", "yellow", "green", "violet", "purple"]
y_position = [-100, -50, 0, 50, 100]
al_turtle = []
for index in range(0, 5):
    timmy = Turtle("turtle")
    timmy.color(colors[index])
    timmy.penup()
    timmy.goto(x=-250, y=y_position[index])
    al_turtle.append(timmy)

if user_input:
    is_race_on = True

while is_race_on:
    for t in al_turtle:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_input:
                print("You won!")
            else:
                print("You lost!")
        random_distance = random.randint(0,10)
        t.forward(random_distance)


screen.exitonclick()