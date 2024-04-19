import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.forward_s, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car_function()
    cars.move_up()

    for car in cars.MOVING_CARS:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False
        elif player.ycor() > 280:
            player.goto(0, -280)
            score.increase_level()



screen.exitonclick()
