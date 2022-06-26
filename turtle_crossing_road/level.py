from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.cur_level = 1
        self.update()
        
    def update(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level: {self.cur_level}", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=("Courier", 20, "normal"))