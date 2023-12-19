from tkinter import *
import pandas
from random import choice
BK_COLOR = "#B1DDC6"
current_card = {}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~Data extraction~~~~~~~~~~~~~~~~~~~~~~~~~~ #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/es_en_new.csv")
finally:
    words_bank = pandas.DataFrame.to_dict(data, orient="records")
# orient records allow to pull data as [{column -> value}, … , {column -> value}]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~CHANGE CARD MECHANISM~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def flip_card():
    print(current_card)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=current_card["english"], fill="white")
    card_canvas.itemconfig(card_image, image=card_back_img)


def switch_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # cancel the timer when card was replaced b4 time up
    current_card = choice(words_bank)
    card_canvas.itemconfig(card_title, text="Spanish", fill="black")
    card_canvas.itemconfig(card_word, text=current_card["spanish"], fill="black")
    card_canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(2000, func=flip_card)


def know_card():
    words_bank.remove(current_card)
    data = pandas.DataFrame(words_bank)
    data.to_csv("data/words_to_learn.csv", index=False)
    switch_card()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~UI SETUP~~~~~~~~~~~~~~~~~~~~~~~~~~ #
window = Tk()
window.title("Let's Learn Spanish")
window.config(padx=50, pady=50, bg=BK_COLOR)

flip_timer = window.after(2000, func=flip_card)  # flipping the card

# CANVAS CONFIG
card_canvas = Canvas(width=800, height=526, bg=BK_COLOR, highlightthickness=0)

# Canvas images, only have 1 each time
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_image = card_canvas.create_image(410, 270, image=card_front_img)

# Canvas texts attributes
card_title = card_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = card_canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
# Canvas place on board
card_canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=know_card)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=switch_card)
wrong_button.grid(row=1, column=0)

switch_card()  # to start with a card
window.mainloop()
