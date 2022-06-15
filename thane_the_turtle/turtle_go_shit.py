from turtle import Turtle, Screen
import random

screen = Screen()
thane_the_turtle = Turtle()
thane_the_turtle.shape("turtle")
thane_the_turtle.color("coral")

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    thane_the_turtle.color(R, G, B)

def set_position():
    thane_the_turtle.penup()
    thane_the_turtle.goto(-50,250)
    thane_the_turtle.pendown()

def go_dash():
    for i in range(25):
        thane_the_turtle.pendown()
        thane_the_turtle.forward(2)
        thane_the_turtle.penup()
        thane_the_turtle.forward(2)

def go_shit():
    set_position()
    for i in range(3,11):
        num_sides = i
        change_color()
        for _ in range(num_sides):
            thane_the_turtle.forward(100)
            thane_the_turtle.right(360/num_sides)

go_shit()

screen.exitonclick()