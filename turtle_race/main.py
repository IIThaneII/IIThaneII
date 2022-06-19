from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]
y_positions = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_i in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for tur in all_turtles:
        if tur.xcor() > 230:
            winning_color = tur.pencolor()
            if winning_color == user_bet:
                print(f"Your bet was right! The turtle is {winning_color}")
            else:
                print(f"Your bet was wrong! The turtle is {winning_color}")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        tur.forward(rand_distance)


screen.exitonclick()
