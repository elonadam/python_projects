from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    new_question = Question(q_text, q_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_q()

print(f"You've completed the quizz\nYour final score was {quiz.score}/{len(question_bank)}")
