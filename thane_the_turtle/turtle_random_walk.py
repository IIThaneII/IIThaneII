from turtle import Turtle, Screen
import random

thane_the_turtle = Turtle()
thane_the_turtle.shape("turtle")
thane_the_turtle.color("coral")
thane_the_turtle.pensize(10)
thane_the_turtle.speed(10)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    thane_the_turtle.color(R, G, B)

a = [90, 270, 180, 0]
def change_direction(c):
    b = random.choice(c)
    thane_the_turtle.right(b)

moves = 1000
while moves > 0:
    thane_the_turtle.forward(20)
    change_direction(a)
    change_color()
    moves -= 1


screen = Screen()
screen.exitonclick()  
