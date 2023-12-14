from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
GREY = '#BBBBBB'
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

    final_pass = "".join(pass_list) # Adds all the pieces to a string

    print(f"Your password is: " + final_pass)
    password_input.insert(0, final_pass)
    pyperclip.copy(final_pass) # Copy the password to the computer clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #

def clear_input(*args):
    for entry in args:
        entry.delete(0, END)


def save_to_file():
    """Getting a string input and append that in a text file"""
    web_data = website_input.get()  # Get input from the entry field
    email_data = email_input.get()
    pass_data = password_input.get()

    if len(web_data) == 0 or len(email_data) == 0 or len(pass_data) == 0:
        messagebox.showerror(title="Error", message="Please fill all the fields")
    else:
        want_to_save = messagebox.askokcancel(title=f"New login details for {web_data}",
                                              message=f"These are the details"
                                                      f" entered:\nEmail: {email_data}\nPassword: {pass_data}\nDo you want to save it ?")

        if want_to_save:  # this argument has boolean value based on what was clicked in the alert box
            with open("data.txt", "a") as file:
                file.write(f"{web_data} | {email_data} | {pass_data} \n")  # get input from func and append it
            clear_input(website_input, password_input)


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

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.insert(END, string="elon@python3.com")
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=16)
password_input.grid(row=3, column=1, columnspan=1)

# Buttons

generate_button = Button(text="Generate Passwords", bg=LIGHT_GREY, width=15, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", bg=LIGHT_GREY, width=30, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
