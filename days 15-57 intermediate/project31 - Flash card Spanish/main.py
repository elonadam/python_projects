from tkinter import *
import pandas
from random import choice

BK_COLOR = "#B1DDC6"
# TODO 1 switch to better spanish csv
# ---------------------------- CHANGE CARD MECHANISM ------------------------------- #

data = pandas.read_csv("es_en.csv")
words_to_learn = pandas.DataFrame.to_dict(data,
                    orient="records")  # orient records allow to pull data as [{column -> value}, … , {column -> value}]

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Let's Learn Spanish")
window.config(padx=50, pady=50, bg=BK_COLOR)

card_canvas = Canvas(width=800, height=526, bg=BK_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_canvas.create_image(410, 270, image=card_front_img)
card_title = card_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = card_canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
card_canvas.grid(row=0, column=0, columnspan=2)


# Buttons
def switch_card():
    current_card = choice(words_to_learn)
    card_canvas.itemconfig(card_title, text="Spanish")
    card_canvas.itemconfig(card_word, text= current_card["spanish"])


right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=switch_card)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=switch_card)
wrong_button.grid(row=1, column=0)

switch_card()
window.mainloop()
