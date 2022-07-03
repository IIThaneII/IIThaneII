from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

Question_bank = []

for Q in question_data:
    Question_bank.append(Question(Q["text"], Q["answer"]))

quiz = QuizBrain(Question_bank)
quiz.next_question()
while quiz.still_have_question() == True:
    quiz.next_question()

print("Congratulation you've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(Question_bank)}")