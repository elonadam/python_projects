from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark_sym = "☑"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_click():
    global timer
    global reps
    marks = ""
    reps = 0
    check_mark.config(text=marks)
    timer_title.config(text="Timer")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_click():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        count_down(work_sec)
        timer_title.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        timer_title.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        timer_title.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    minutes = count // 60
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"  # in order to make 00 instead of 0
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count:  # while count > 0
        global timer
        timer = window.after(1000, count_down, count - 1) # the timer itself
    else:
        start_click()  # make the timer fo to next rep
        marks = ""
        for i in range(reps // 2):  # count total work sessions and adds another check mark
            marks += check_mark_sym
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Labels
timer_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50), highlightthickness=0)
timer_title.grid(row=0, column=1)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"), highlightthickness=0)
check_mark.grid(row=4, column=1)

# Buttons

start_button = Button(text="Start", command=start_click)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=reset_click)
reset_button.grid(row=2, column=2)

canvas = Canvas(width=208, height=224, bg=YELLOW,
                highlightthickness=0)  # the last attribute remove the border around the canvas
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)

window.mainloop()
