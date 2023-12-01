import turtle
import pandas
from names_board import NamesBoard

# In order to get the x,y coordinates of the states on the image I used this code
# def get_mouse_clic_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_clic_cor)
# turtle.mainloop()
#

# Screen settings
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# Data structures and Objects
names_board = NamesBoard()
data = pandas.read_csv("50_states.csv")
states_name = data["state"]
states_dic = pandas.DataFrame.to_dict(data)
correct_guess = []


def print_state_name(name):
    """finds the state's x,y coordinates and print the state's name on the map"""
    for i in range(len(states_name)):
        if states_dic['state'][i] == name:
            x_cor_state = states_dic['x'][i]
            y_cor_state = states_dic['y'][i]

            names_board.write_name(x=x_cor_state, y=y_cor_state, state_name=name)


game_is_on = True
names_board.write_name(260, -263, "type exit to quit")
num = 0  # will hold count on success guess

while game_is_on:

    answer_state = screen.textinput(title=f"{num}/50 states correct", prompt="What's another state name?").title()
    for state in states_name:
        # if answer_state in correct_guess:
        #     print("already guessed")

        if answer_state == state:
            print("yay")
            num += 1
            print_state_name(answer_state)
            correct_guess.append(answer_state)  # add state to correct guess list
        elif answer_state == "Exit":
            game_is_on = False
            print("why?! game was closed by user")
            print(correct_guess)
            break

        else:
            pass

# if answer_state == data[]
