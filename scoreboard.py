FONT = ("Courier", 14, "bold")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-280, 270)
        self.hideturtle()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)

        self.write(f"Game Over", align="left", font=FONT)
