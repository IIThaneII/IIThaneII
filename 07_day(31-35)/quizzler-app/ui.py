from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler") 
        self.window.config(bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        self.questions_canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.questions_canvas.create_text(150, 125, 
        text="Test", 
        font=("Arial", 20, "italic"), 
        width=280)
        self.questions_canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        true_img = PhotoImage(file="/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/7_day(31-35)/quizzler-app/images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        false_img = PhotoImage(file="/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/7_day(31-35)/quizzler-app/images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.questions_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.questions_canvas.itemconfig(self.question_text, text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        is_true = self.quiz.check_answer("True")
        self.give_feedback(is_true)
        self.get_next_question()

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.get_next_question()

    def give_feedback(self, is_true):
        if is_true:
            self.questions_canvas.config(bg="green")
        else:
            self.questions_canvas.config(bg="red")
        self.window.update()
        self.window.after(1000)
        self.questions_canvas.config(bg="white")
