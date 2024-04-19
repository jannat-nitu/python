class QuizBrain:
    def __init__(self, q_list):
        self.questions_number = 0
        self.score = 0
        self.questions_list = q_list

    def still_has_questions(self):
        if self.questions_number < len(self.questions_list):
            return True
        else:
            print("you have completed the game")
            print(f"your final score is {self.score}/{self.questions_number}")
            return False

    def next_question(self):
        current_question = self.questions_list[self.questions_number]
        self.questions_number += 1
        user_choice = input(f"Q. {self.questions_number}: {current_question.text} (True/False)").lower()
        self.check_answer(user_choice, current_question.answer)

    def check_answer(self, user_choice, answer):
        if user_choice == answer:
            self.score += 1
            print(f"Correct! {self.score}/{self.questions_number}")
        else:
            print(f"Incorrect! {self.score}/{self.questions_number}")
        print(f"correct answer: {answer}")



