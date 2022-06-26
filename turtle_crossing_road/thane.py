from turtle import Turtle
STARTING_POSITION = (0, -280)

class Thane(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.refresh()
    
    def move(self):
        self.forward(10)

    def refresh(self):
        self.goto(STARTING_POSITION)