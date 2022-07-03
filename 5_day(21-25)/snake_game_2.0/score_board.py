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
        with open("my_file.txt", mode = "r") as file:
            self.high_score = int(file.read())

    def score_board(self):
        self.clear()
        self.write(f"Score Board: {self.score} High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def reset(self):
        if self.score > self.high_score:
            with open("my_file.txt", mode = "w") as file:
                self.high_score = self.score
                file.write(f"{self.high_score}")
        self.score = 0
        self.score_board()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over.", font=FONT, align=ALIGNMENT)

