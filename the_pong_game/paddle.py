from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.color("white")
        self.penup()
        self.goto(pos)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.forward(-20)

