from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score} High score: {self.high_score}', font=("Arial", 10, "normal"), align="center")

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.write_score()

    #def game_over(self):
        #self.goto(0, 0)
        #self.write("game over", font=("Arial", 10, "normal"), align="center")
    def increase_score(self):
        self.score += 1
        self.write_score()
