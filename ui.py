from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question",
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.score_label.grid(column=1, row=0)

        true = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You´ve reached the end of the quiz.\n "
                                                            f"Final score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green", highlightthickness=0)
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red", highlightthickness=0)
            self.canvas.itemconfig(self.question_text, fill="white")

        self.window.after(1000, self.get_next_question)