question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

#from question_data import question_data

# Define the Question class
class Question: 
    def __init__(self, q_text, q_answer):
        self.q_text = q_text
        self.q_answer = q_answer

# Create a list of Question objects
question_bank = []
for item in question_data:
    question = item["text"]
    answer = item["answer"]
    new_question = Question(q_text=question, q_answer=answer)
    question_bank.append(new_question)

# Define the quiz logic
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.q_text} (True/False): ")
        self.check_answer(user_answer, current_question.q_answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().lower() == correct_answer.lower():
            print("✅ Correct!")
            self.score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print("-" * 40)

# Run the quiz
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("🎉 You've completed the quiz!")
print(f"Your final score: {quiz.score}/{len(quiz.question_list)}")

# Explanation
That's awesome, Vinay! 🙌 I'm really glad you're understanding it well. Here's your complete **notes with detailed explanation** of the entire quiz code — perfect for learning and revision. I've organized it step by step, like a personal learning notebook.

---

## 🧠 Python OOP Quiz App – Detailed Notes

---

### ✅ 1. `question_data` – List of Dictionaries

```python
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    ...
]
```

- This is a list of **questions** where each item is a dictionary with two keys:
  - `"text"`: The actual question
  - `"answer"`: Correct answer ("True" or "False")
- This acts as the **raw data** for the quiz.

---

### ✅ 2. Creating a `Question` Class

```python
class Question: 
    def __init__(self, q_text, q_answer):
        self.q_text = q_text
        self.q_answer = q_answer
```

- A **class** is a blueprint for creating objects.
- The `__init__` method is called when a new object is created.
- `self.q_text` stores the question text.
- `self.q_answer` stores the correct answer.
- The keyword `self` refers to the **current instance** of the class.

---

### ✅ 3. Creating a List of `Question` Objects

```python
question_bank = []
for item in question_data:
    question = item["text"]
    answer = item["answer"]
    new_question = Question(q_text=question, q_answer=answer)
    question_bank.append(new_question)
```

- We loop through each item in `question_data`.
- Extract the `text` and `answer`.
- Create a new `Question` object using `Question(q_text, q_answer)`.
- Append it to the list `question_bank`.
- ✅ Now, `question_bank` is a list of `Question` objects, not dictionaries.

---

### ✅ 4. Creating the `QuizBrain` Class

```python
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
```

- This class manages the **quiz logic**.
- `q_list` will receive the `question_bank` list when an object is created.
- `self.question_number` tracks which question the user is on.
- `self.score` keeps count of correct answers.

---

### ✅ 5. Method: `still_has_question()`

```python
def still_has_question(self):
    return self.question_number < len(self.question_list)
```

- This checks if there are more questions left.
- Compares current `question_number` with total number of questions using `len()`.
- Returns `True` or `False`.

---

### ✅ 6. Method: `next_question()`

```python
def next_question(self):
    current_question = self.question_list[self.question_number]
    user_answer = input(f"Q.{self.question_number + 1}: {current_question.q_text} (True/False): ")
    self.check_answer(user_answer, current_question.q_answer)
    self.question_number += 1
```

- Fetches the current question using index.
- Asks the user for input (True/False).
- Calls `check_answer()` to verify.
- Increments the question number for the next round.

---

### ✅ 7. Method: `check_answer()`

```python
def check_answer(self, user_answer, correct_answer):
    if user_answer.strip().lower() == correct_answer.lower():
        print("✅ Correct!")
        self.score += 1
    else:
        print(f"❌ Wrong! The correct answer was: {correct_answer}")
    print(f"Your current score is: {self.score}/{self.question_number + 1}")
    print("-" * 40)
```

- Compares user input with the correct answer.
- `strip()` removes extra spaces, `lower()` ignores case.
- Increments the score if correct.
- Prints whether the answer was right or wrong.
- Displays the updated score.

---

### ✅ 8. Running the Quiz

```python
quiz = QuizBrain(question_bank)
```

- Creates an object of `QuizBrain` and passes the list of `Question` objects (`question_bank`).

---

### ✅ 9. Quiz Loop

```python
while quiz.still_has_question():
    quiz.next_question()
```

- While there are still questions left (`True`), keep asking next question.

---

### ✅ 10. After Quiz Ends

```python
print("🎉 You've completed the quiz!")
print(f"Your final score: {quiz.score}/{len(quiz.question_list)}")
```

- Shows final message and score.

---

## 💡 OOP Concepts Used

| Concept | Used In | Description |
|--------|---------|-------------|
| Class | `Question`, `QuizBrain` | Blueprint for objects |
| Object | `new_question`, `quiz` | Created using classes |
| Constructor | `__init__()` | Initializes object attributes |
| Encapsulation | Attributes like `self.score` | Keeps data and behavior together |
| Methods | `next_question()`, `check_answer()` | Functions inside a class |
| Self | `self.attribute` | Refers to current object instance |

---

## 📘 Summary

- `question_data`: raw question list
- `Question`: converts raw data into objects
- `question_bank`: stores all question objects
- `QuizBrain`: handles quiz logic
- `quiz.next_question()`: runs until all questions are done
- Final score is printed at the end

---

Would you like me to convert this into a **PDF format** or a downloadable note for your reference? Or maybe create a flashcard-style version for quick review? 😊
