#29/100 days of code, was edited on the 30th day, added search for passwords and change the data file form txt to json


from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

LIGHT_GREY = '#E2D5D5'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [(choice(letters)) for _ in range(randint(8, 10))]
    number_list = [(choice(numbers)) for _ in range(randint(2, 4))]
    sym_list = [(choice(symbols)) for _ in range(randint(2, 4))]

    pass_list = letter_list + number_list + sym_list
    shuffle(pass_list)  # Order of characters randomised:

    final_pass = "".join(pass_list)  # Adds all the pieces to a string

    print(f"Your password is: " + final_pass)
    password_input.insert(0, final_pass)
    pyperclip.copy(final_pass)  # Copy the password to the computer clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #

def clear_input(*args):
    for entry in args:
        entry.delete(0, END)


small_data = {
    "start_value": {
        "email": "elon@python.com",
        "password": "goodPassword"
    }
}

with open("data.json", "w") as data_file:
    json.dump(small_data, data_file, indent=4)


def save_to_file():
    """Getting a string input and append that in a text file"""
    web_data = website_input.get()  # Get input from the entry field
    email_data = email_input.get()
    pass_data = password_input.get()
    new_data = {
        web_data: {
            "email": email_data,
            "password": pass_data,
        }
    }
    if len(web_data) == 0 or len(email_data) == 0 or len(pass_data) == 0:
        messagebox.showerror(title="Error", message="Please fill all the fields")
    else:
        want_to_save = messagebox.askokcancel(title=f"New login details for {web_data}",
                                              message=f"These are the details"
                                                      f" entered:\nEmail: {email_data}\nPassword: {pass_data}\nDo you want to save it ?")

        if want_to_save:  # this argument has boolean value based on what was clicked in the alert box
            with open("data.json", "a") as file:
                try:
                    with open("data.json", "r") as data_file:
                        # Reading old data
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    # Updating old data with new data
                    data.update(new_data)

                    with open("data.json", "w") as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)
                finally:
                    clear_input(website_input, password_input)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Pass Manager")
window.config(padx=50, pady=50, bg=LIGHT_GREY)

canvas = Canvas(width=220, height=220, bg=LIGHT_GREY, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg=LIGHT_GREY, highlightthickness=0)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg=LIGHT_GREY, highlightthickness=0)
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=LIGHT_GREY, highlightthickness=0)
password_label.grid(row=3, column=0)

# Entries

website_input = Entry(width=16)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(END, string="elon@python3.com")

password_input = Entry(width=16)
password_input.grid(row=3, column=1)

# Buttons

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Passwords", width=15, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
