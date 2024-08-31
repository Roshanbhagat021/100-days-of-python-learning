from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for ques in question_data:
    question_text = ques["question"]
    question_answer = ques['correct_answer']
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
# print(question_bank)
while quiz.still_has_question():
    quiz.next_question()

quiz.quiz_completed()