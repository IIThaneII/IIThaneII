from tkinter import *

window = Tk()
window.title("Miles to Kilometers converter")
window.minsize(width=250, height=130)
window.config(padx=20, pady=20) # add padding to the window

def calculate():
    a = input.get()
    l4["text"] = round(float(a)*1.609, 2)

input = Entry(width=10)
input.grid(row=0, column=2)
input.insert(END, string="0")

l1 = Label(text="Miles", font=(15))
l1.grid(row=0, column=3)

l2 = Label(text="is equal to", font=(15))
l2.grid(row=1, column=0)

l3 = Label(text="Km", font=(15))
l3.grid(row=1, column=3)

l4 = Label(text="0", font=(15))
l4.grid(row=1, column=2)

button = Button(text="Calculate", font=(15), command=calculate)
button.grid(row=2, column=2)

window.mainloop()