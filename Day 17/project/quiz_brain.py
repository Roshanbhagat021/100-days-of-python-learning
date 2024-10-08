class QuizBrain:
    def __init__(self , q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
       current_question = self.question_list[self.question_number]
       self.question_number += 1
       user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
       correct_answer = current_question.answer
       self.check_answer(user_answer, correct_answer)


    def check_answer(self,user_ans, c_ans):
        if user_ans.lower() == c_ans.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("You got it wrong!")
            print(f"The correct answer was: {c_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n"*1)

    def quiz_completed(self):
        print("You have completed the Quiz!")
        print(f'Your final score is {self.score}/{self.question_number}')


