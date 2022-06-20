from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(5)

def move_backward():
    tim.forward(-5)

def turn_rights():
    tim.right(3)

def turn_left():
    tim.left(3)

def clear_screen():
    tim.penup()
    tim.setpos(0, 0)
    tim.clear()
    tim.pendown()

screen.listen()
screen.onkeypress(key = "w", fun = move_forward)
screen.onkeypress(key = "s", fun = move_backward)
screen.onkeypress(key = "d", fun = turn_rights)
screen.onkeypress(key = "a", fun = turn_left)
screen.onkeypress(key = "c", fun = clear_screen)
screen.exitonclick()