from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
def pass_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letter + password_number + password_symbol
    shuffle(password_list)

    password = "".join(password_list)
    entry_pass.insert(0, password)
    pyperclip.copy(password)

def save():
    password = entry_pass.get()
    email = entry_email.get()
    website = entry_web.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo("opps", "you left field empty, please enter")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_web.delete(0, END)
            entry_pass.delete(0, END)
    
def find_password():
    website = entry_web.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="/home/santanu/PycharmProjects/pythonProject/game_day29/logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
email = Label(text="Email/user:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)
entry_web = Entry(width=21)
entry_web.grid(row=1, column=1)
entry_web.focus()
entry_email = Entry(width=36)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "jannat@gmail.com")
entry_pass = Entry(width=21)
entry_pass.grid(row=3, column=1)
search_button = Button(text="Search", width=12 ,command=find_password)
search_button.grid(row=1, column= 2)
button1 = Button(text="Generate Pass", width=12, command=pass_generate)
button1.grid(row=3, column=2)
button = Button(text="Add", width=36, command=save)
button.grid(row=4, column=1, columnspan=2)





window.mainloop()