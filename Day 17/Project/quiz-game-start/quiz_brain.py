class QuizBrain:
    def __init__(self, list_of_questions):
        self.num_correct = 0
        self.question_num = 0
        self.question_list = list_of_questions


    def run_quiz(self):
        num_questions = len(self.question_list)
        for i in range(num_questions):
            self.ask_next_question()


    def ask_next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        choice = input(f"Q.{self.question_num}: {current_question.text}. (True/False)?: ").title()
        if current_question.answer == choice:
            self.num_correct += 1
            print("You got it right!")
        else:
            print("Sorry, that's incorrect.")
        print(f"The correct answer was {current_question.answer}")
        print(f"Your current score is: {self.num_correct} / {self.question_num}.")
        print("\n")

