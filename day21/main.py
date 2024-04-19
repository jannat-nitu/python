from turtle import Screen, Turtle
import time

import segment

from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.SEGMENTS[0].distance(food) < 20:
        snake.extend()
        score.increase_score()
        food.refresh()
    if not (not (290 < snake.SEGMENTS[0].xcor()) and not (snake.SEGMENTS[0].xcor() < -290) and not (
            snake.SEGMENTS[0].ycor() > 290) and not (snake.SEGMENTS[0].ycor() < -290)):
        score.reset_score()
        snake.snake_reset()

    for segment in snake.SEGMENTS[1:]:
        if snake.SEGMENTS[0].distance(segment) < 10:
            score.reset_score()
            snake.snake_reset()


screen.exitonclick()
