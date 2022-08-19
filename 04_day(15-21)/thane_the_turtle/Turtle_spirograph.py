from turtle import Turtle, Screen
import random

thane_the_turtle = Turtle()
thane_the_turtle.shape("turtle")
thane_the_turtle.color("coral")
thane_the_turtle.speed(10)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    thane_the_turtle.color(R, G, B)

for d in range(0,361,10):
    thane_the_turtle.circle(100)
    thane_the_turtle.setheading(d)
    change_color()

screen = Screen()
screen.exitonclick()  