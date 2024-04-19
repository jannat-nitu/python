from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-200, 200)
        self.update()
    def update(self):
        self.clear()
        self.write(f"level:{self.level}", align="center", font= FONT)

    def increase_level(self):
        self.level += 1
        self.update()
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over:{self.level}", align="center", font=FONT)