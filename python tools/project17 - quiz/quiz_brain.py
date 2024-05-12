class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_q(self):
        # curr_q get question type variable that has 2 attributes txt and ans
        curr_q = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {curr_q.text} True/False?: ")
        self.check_answer(user_answer, curr_q.answer)

    def still_have_questions(self):
        return self.question_num < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_num} \n")


