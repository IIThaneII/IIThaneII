from turtle import Screen
from thane import Thane
from cars import Cars
from level import Level
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Road")
screen.tracer(0)

thane_turtle = Thane()
level = Level()
cars = Cars()

screen.listen()
screen.onkeypress(thane_turtle.move, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(cars.move_speed)
    cars.cars_move()
    cars.create_car()

    #Detect if turtle had crossed the road
    if thane_turtle.ycor() == 300:
        thane_turtle.refresh()
        level.cur_level += 1
        level.update()
        cars.level_up()

    #Detect if car hit turtle
    for car in cars.cars_list:
        if thane_turtle.distance(car) < 20:
            game_is_on = False
            level.game_over()

screen.exitonclick()