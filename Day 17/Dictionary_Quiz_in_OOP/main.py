from Quiz_data import Data
from Question_Model import Questions
from Quiz_Logic import Quiz_logic


question_bank = []
for item in Data:
    new_q = Questions(item["question"], item["options"], item["answer"])
    question_bank.append(new_q)

quiz = Quiz_logic(question_bank)

# quiz.next_question()

while quiz.pending_questions():
    quiz.next_question()
print("Game Complete")
print(f"The Final Score {quiz.score}/{quiz.question_number}")



