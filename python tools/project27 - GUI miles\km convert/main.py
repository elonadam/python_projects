from tkinter import *

window = Tk()  # creates the tk window
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(background="cyan")
window.config(padx=80, pady=20)

# labels

# label for miles
label = Label(text="Miles")
label.config(background="cyan")
label.grid(row=0, column=4)

# label for "is equal to"
label = Label(text="is equal to")
label.config(background="cyan")
label.grid(row=2, column=0)

# label for Km
label = Label(text="Km")
label.config(background="cyan")
label.grid(row=2, column=4)

# label for result
res_label = Label(text="0")
res_label.config(background="cyan")
res_label.grid(row=2, column=1)

# entry
miles_input = Entry(width=5)
miles_input.insert(END, string="0")  # Add some text to begin with
print(miles_input.get())  # Gets text in entry
miles_input.grid(row=0, column=2)


# button
def clicked():
    km_result = float(miles_input.get()) * 0.621371
    res_label.config(text=km_result.__round__(3))


# calls clicked() when pressed
button = Button(text="Convert", command=clicked)
button.grid(row=3, column=2)

window.mainloop()
