import math

from data import question_data
from question_model import Question

score = 0
for  count, item in enumerate(question_data, start=1):
    question = Question(item['question'], item['correct_answer'])

    given_ans = input(f"Q.{count} {question.text} (True/False): ").lower()
    if given_ans == question.answer.lower():
        score += 1
        print("You got it right!")
        print(f"The correct answer was: {question.answer}")
        print(f"Your current score is: {score}/{count}")
        print("\n" * 2)

    else:
        print("That' wrong.")
        print(f"The correct answer was: {question.answer}")
        print(f"Your current score is: {score}/{count}")
        print("\n" * 2)



passing_percentage = 33
grade_b = 66
grade_a = 80
if score > math.ceil((len(question_data)*grade_a)/100):
    print(f"You done it very well and your final score {score}")
elif score > math.ceil((len(question_data)*grade_b)/100):
    print(f"You can do better , Your final score {score}")
elif score >= math.ceil((len(question_data)*passing_percentage)/100):
    print(f"Abe jake padd le sale phone chala riya 🤬 your score {score}")
else:
    print(f"Fail")