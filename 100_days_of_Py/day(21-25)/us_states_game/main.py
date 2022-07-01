import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/day(21-25)/us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.penup()
t.hideturtle()

data = pandas.read_csv("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/day(21-25)/us_states_game/50_states.csv")
all_states = data.state.to_list()

game_is_on = True
guessed_state = 0
while game_is_on:
    answer_state = screen.textinput(title=f"{guessed_state}/50 State Correct", prompt="What's another state's name?").title()
    if answer_state in all_states:
        all_states.remove(answer_state)
        guessed_state += 1
        t.goto(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
        t.write(answer_state)
    if len(all_states) == 0 or answer_state == "Exit":
        game_is_on = False
    
states_to_learn = pandas.DataFrame(all_states)
states_to_learn.to_csv("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/day(21-25)/us_states_game/states_to_learn.csv")