from ctypes import alignment
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.score = 0

    def score_board(self):
        self.clear()
        self.write(f"Score Board: {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", font=FONT, align=ALIGNMENT)

