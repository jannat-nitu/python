from turtle import Turtle, Screen
import random
game_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_input = screen.textinput("What is your turtle color?: ", "which color you bet for")
colors = ["red", "orange", "yellow", "green", "violet", "purple"]
y_space = [-100,-50, 0, 50, 100]

all_timmy = []
for index in range(0, 5):
    timmy = Turtle()
    timmy.penup()
    timmy.shape("turtle")
    timmy.color(colors[index])
    timmy.goto(x=-200, y=y_space[index])
    all_timmy.append(timmy)

if user_input:
    game_on = True
while game_on:
    for t in all_timmy:
        if t.xcor() > 230:
            game_on = False
            winning_color = t.pencolor()
            if winning_color == user_input:
                print("you win")
            else:
                print("you lose")
        run = random.randint(0,10)
        t.forward(run)













screen.exitonclick()
