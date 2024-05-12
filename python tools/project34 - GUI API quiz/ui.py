from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Ariel", 20, "italic")


class QuizzInterFace:

    def __init__(self, quiz_brain: QuizBrain):  # the input is the quiz itself in order to display it
        # the : after the parameter declare which type it expected to get, QuizBrain type it this case
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        # Canvas
        self.canvas = Canvas()
        self.canvas.config(bg="white", width=300, height=250, highlightthickness=0)
        self.canvas_quest = self.canvas.create_text(
            150,
            125,
            width=280,
            text="default text",
            font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2)

        # Labels
        self.score_label = Label(bg=THEME_COLOR, fg="white", text=f"Score: 0", font=20,
                                 highlightthickness=0)  # {score_points}")
        self.score_label.grid(row=0, column=1, pady=20)

        # Buttons
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.clicked_true)
        self.true_button.grid(row=2, column=0, pady=20)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.clicked_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()  # display first question

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()  # gets the output
            self.canvas.itemconfig(self.canvas_quest, text=q_text)  # updates question to the screen
        else:
            self.canvas.itemconfig(self.canvas_quest, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def clicked_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def clicked_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
