import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = -10


class CarManager:
    def __init__(self):
        self.MOVING_CARS = []
            
    def car_function(self,):
        random_number = random.randint(1, 20)
        if random_number == 1:
            car = Turtle("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.MOVING_CARS.append(car)

    def move_up(self):
        for segment in self.MOVING_CARS:
            segment.forward(MOVE_INCREMENT)









