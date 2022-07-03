import turtle
from colors_extracted import rgb_colors
from turtle import Turtle, Screen
import random

turtle.colormode(255)
thane_the_turtle = Turtle()
thane_the_turtle.shape("turtle")
thane_the_turtle.speed(10)
thane_the_turtle.penup()
thane_the_turtle.goto(-370,-305)
# thane_the_turtle.hideturtle()

def change_color():
    a = random.choice(rgb_colors)
    thane_the_turtle.color(a)

def draw(space, n_dots):
    for i in range(n_dots):
        for j in range(n_dots):
            change_color()
            thane_the_turtle.dot(20)
            thane_the_turtle.forward(space)
        if i % 2 == 1:    
            thane_the_turtle.right(90)
            thane_the_turtle.forward(space)
            thane_the_turtle.right(90)
            thane_the_turtle.forward(space)
        else:
            thane_the_turtle.left(90)
            thane_the_turtle.forward(space)
            thane_the_turtle.left(90)
            thane_the_turtle.forward(space)

draw(40, 19)

screen = Screen()
screen.exitonclick()  