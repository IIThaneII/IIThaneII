from turtle import Turtle
import random
import turtle

turtle.colormode(255)
cars_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (127, 0, 255), (255, 128, 0), (255, 0, 255), (255, 255, 0)]

class Cars:
    def __init__(self):
        self.cars_list = []
        self.move_speed = 0.2

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(cars_colors))
        new_car.setheading(180)
        new_car.penup()
        ran_y = random.randint(-250, 250)
        new_car.goto(300, ran_y)
        self.cars_list.append(new_car)

    def cars_move(self):
        for car in self.cars_list:
            car.forward(10)

    def level_up(self):
        self.move_speed *= 0.8