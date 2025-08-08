class Quiz_logic:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question = question_list

    def pending_questions(self):                               # Created for true or false based on this while loop runs in main.py
        return self.question_number < len(self.question)       
    
    def next_question(self):
        current_question = self.question[self.question_number]  # ✅ This gets the current Questions object from the list (based on question_number) and assigns it to current_question
        self.question_number += 1                               # ✅ This increases the question_number by 1, so next time we get the next question
        print(f"\nQ{self.question_number}: {current_question.question}")
        for options in current_question.option:
            print(f"-{options}")
        user_input = input("Please Input your answer:").lower()        
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input == correct_answer:
            self.score += 1
            print("You are correct.")
            print(f"Current Score:{self.score}/{self.question_number}")
        else:
            print(f"You are wrong! \nThe correct Answer: {correct_answer}") 
            print(f"Current Score {self.score}/{self.question_number}")





"""
🔍 Example to Visualize
Lets say you have 3 questions, and this is your list:

python
self.question = [Q1, Q2, Q3]
self.question_number = 0
First Call:
current_question = self.question[0] → gets Q1

self.question_number += 1 → now it's 1

Second Call:
current_question = self.question[1] → gets Q2

self.question_number += 1 → now it's 2

and so on…

To check the question number and question in next question method.
        print(f"Q{self.question_number}: {current_question.question}")
        for option in current_question.option:
            print(f"- {option}")

"""        

    
