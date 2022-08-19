class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0                    # Attributes
        self.question_list = q_list                 # Attributes
        self.score = 0                              # Attributes

#TODO: checking if we're the end of the quiz

    def still_have_question(self):                  # Methods
        return self.question_number < len(self.question_list)

#TODO: asking the question

    def next_question(self):                        # Methods
        cur_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {cur_question.text} (True/False): ")
        self.check_answer(user_answer, cur_question.answer)

#TODO: checking if the answer was correct

    def check_answer(self, user_answer, answer):    # Methods
        if user_answer.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The amswer is: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.")     
        print("\n")    