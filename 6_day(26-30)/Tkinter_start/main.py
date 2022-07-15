from tkinter import * # all 

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=30)
window.config(padx=20, pady=20) # add padding to the window

# Label
my_label = Label(text="I'm a label", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)
my_label.config(padx = 30, pady = 30)

# my_label["text"] = "New text" or
my_label.config(text="New text") # to change content of the text

# Button
def button_click():
    print("I got clicked.")
    a = input.get()
    my_label["text"] = a
button = Button(text="Click me", command=button_click)
button.grid(row=1, column=1)
button2 = Button(text="New button")
button2.grid(row=0, column=2)

# Entry
input = Entry(width=10)
input.grid(row=2, column=3)

window.mainloop()