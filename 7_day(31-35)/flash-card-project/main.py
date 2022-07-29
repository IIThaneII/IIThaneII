from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
a = window.after(3000)

true_image = PhotoImage(file="/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/7_day(31-35)/flash-card-project/images/right.png")
wrong_image = PhotoImage(file="/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/7_day(31-35)/flash-card-project/images/wrong.png")
card_front = PhotoImage(file="/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/7_day(31-35)/flash-card-project/images/card_front.png")
card_back = PhotoImage(file="/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/7_day(31-35)/flash-card-project/images/card_back.png")

words = pandas.read_csv("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/7_day(31-35)/flash-card-project/data/eng.csv")
list_words = words["Eng"].to_list()
word = words[words.Eng == random.choice(list_words)]

def show_word():
    global word, a
    window.after_cancel(a)
    word = words[words.Eng == random.choice(list_words)]
    canvas.delete("all")
    canvas.create_image(400, 283, image=card_front)
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
    canvas.create_text(400, 263, text=f"{word.Eng.to_string(index=False)}", font=("Ariel", 60, "bold"))
    canvas.create_text(400, 380, text=f"{word.Form.to_string(index=False)}", font=("Ariel", 60))
    a = window.after(2000, func=flip_card)

def flip_card():
    global word
    canvas.delete("all")
    canvas.create_image(400, 283, image=card_back)
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.create_text(400, 150, text="Viet Nam", font=("Ariel", 40, "italic"), fill="white")
    canvas.create_text(400, 263, text=f"{word.VN.to_string(index=False)}", font=("Ariel", 60, "bold"), fill="white")

canvas = Canvas(width=800, height=526)
canvas.grid(column=0, row=0, columnspan=2)

a = window.after(2000, func=flip_card)
show_word()

true_b = Button(image=true_image, highlightthickness=0, command=show_word)
true_b.grid(column=0, row=1)
wrong_b = Button(image=wrong_image, highlightthickness=0, command=show_word)
wrong_b.grid(column=1, row=1)

window.mainloop()