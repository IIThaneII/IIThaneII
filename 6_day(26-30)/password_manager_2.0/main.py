from email import message
from gettext import find
from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    e_pass.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    e_pass.insert(END, password)
    pyperclip.copy(password) # copy your password into your clipboard instantly

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    e = e_email.get()
    w = e_website.get()
    p = e_pass.get()
    new_data = {
        w: {
            "email": e,
            "password": p,
        }
    }
    while p == "" or e == "":
        messagebox.showwarning(title="Erorr", message="Please enter your email address and password")

    try:
        with open("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/6_day(26-30)/password_manager_2.0/data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/6_day(26-30)/password_manager_2.0/data.json", mode="w") as file:

            is_ok = messagebox.askokcancel(title="Check", message="Are you sure you want to save this data?")
            if is_ok:
                json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)
        with open("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/6_day(26-30)/password_manager_2.0/data.json", mode="w") as file:

            is_ok = messagebox.askokcancel(title="Check", message="Are you sure you want to save this data?")
            if is_ok:
                json.dump(data, file, indent=4)
    finally:
        e_website.delete(0, END)
        e_pass.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def find_password():
    try:
        with open("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/6_day(26-30)/password_manager_2.0/data.json", mode="r") as file:
            data = json.load(file)
            w = e_website.get()
            if w in data:
                e = data[f"{w}"]["email"]
                p = data[f"{w}"]["password"]
                messagebox.showinfo(title=f"{w}", message=f"Email: {e}\nPassword: {p}")
            else:
                messagebox.showinfo(title=f"{w}", message="No details for the website")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas =  Canvas(width=200, height=200)
logo = PhotoImage(file="/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/6_day(26-30)/password_manager_2.0/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

l_website = Label(text="Website:")
l_website.grid(column=0, row=1)
l_email = Label(text="Email/Username:")
l_email.grid(column=0, row=2)
l_pass = Label(text="Password:")
l_pass.grid(column=0, row=3)

e_website = Entry(width=33)
e_website.grid(column=1, row=1)
e_website.focus()
e_email = Entry(width=51)
e_email.grid(column=1, row=2, columnspan=2)
e_email.insert(END, "nguyenngocthanh13022003@gmail.com")
e_pass = Entry(width=33)
e_pass.grid(column=1, row=3)

b_gen_pass = Button(text="Generate Password", command=generate_password)
b_gen_pass.grid(column=2, row=3)
b_add = Button(text="Add", width=43, command=save)
b_add.grid(column=1, row=4, columnspan=2)
b_email = Button(text="Search", width=14, command=find_password)
b_email.grid(column=2, row=1)

window.mainloop()