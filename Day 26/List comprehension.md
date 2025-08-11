# Python Comprehensions – Study Notes

This guide covers **List Comprehension** and **Dictionary Comprehension** in Python with clear explanations, syntax, examples, and real-time use cases.

---

## 📌 Table of Contents
1. [List Comprehension](#1-list-comprehension)
    - [Definition](#definition)
    - [Syntax](#syntax)
    - [Basic Examples](#basic-examples)
    - [Conditional Comprehension](#conditional-comprehension)
    - [Exercises](#exercises)
2. [Dictionary Comprehension](#2-dictionary-comprehension)
    - [Definition](#definition-1)
    - [Syntax](#syntax-1)
    - [Examples](#examples)
    - [Summary Table](#summary-table)

---

## 1. List Comprehension

### Definition
**List comprehension** is a concise way to create lists in Python using a single line of code.  
It replaces the need for writing multiple lines with loops and `append()`.


---

### Syntax
```python
new_list = [expression for item in iterable if condition]
````

* **expression** → The operation or value to store in the list.
* **item** → Variable that takes each value from the iterable.
* **iterable** → Any Python sequence (list, range, string, etc.).
* **condition** *(optional)* → Filter which items to include.

---

### Basic Examples

**Example 1: Normal loop vs. List comprehension**

```python
numbers = [1, 2, 3]
# Normal loop
result = []
for n in numbers:
    result.append(n + 1)
print(result)

# List comprehension
result = [n + 1 for n in numbers]
print(result)
```

**Example 2: String into list of characters**

```python
name = "vinay"
letters = [letter for letter in name]
print(letters)   # ['v', 'i', 'n', 'a', 'y']
```

**Example 3: Range in list comprehension**

```python
nums = [n * 1 for n in range(1, 6)]
print(nums)  # [1, 2, 3, 4, 5]
```

---

### Conditional Comprehension

**Example 4: Filter short names**

```python
names = ["vinay", "Shankari", "Pallavi", "Sruthi", "Indhu", "Sid", "sui"]
short_names = [name for name in names if len(name) < 4]
print(short_names)  # ['Sid', 'sui']
```

**Example 5: Convert long names to uppercase**

```python
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)  # ['SHANKARI', 'PALLAVI', 'SRUTHI', 'INDHU']
```

---

### Exercises

**Q1: Squaring Numbers**
*Create a list of squared values from an existing list.*

```python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)
```

**Output:**

```
[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
```

---

**Q2: Filtering Even Numbers**
*Convert strings to integers, then filter only even numbers.*

```python
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)
```

**Output:**

```
[0, 32, 8, 2, 8, 64, 42]
```

---

**Q3: Data Overlap**
*Find numbers that appear in both `file1.txt` and `file2.txt`.*

```python
with open("file1.txt") as f1:
    file1_numbers = [int(line.strip()) for line in f1]

with open("file2.txt") as f2:
    file2_numbers = [int(line.strip()) for line in f2]

result = [num for num in file1_numbers if num in file2_numbers]
print(result)
```

**Example Output:**

```
[3, 6, 5, 33, 12, 7, 42, 13]
```

---

## 2. Dictionary Comprehension

### Definition

**Dictionary comprehension** allows you to create dictionaries in a single line, just like list comprehension but with key-value pairs.

---

### Syntax

```python
new_dict = {key_expression: value_expression for item in iterable if condition}
```

* **key\_expression** → Defines dictionary key.
* **value\_expression** → Defines dictionary value.
* **iterable** → Any iterable like list or dictionary.
* **condition** *(optional)* → Filters which items to include.

---

### Examples

**Example 1: Assign Random Scores to Students**

```python
import random

names = ["vinay", "Shankari", "Pallavi", "Sruthi"]
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)
```

**Output Example:**

```
{'vinay': 87, 'Shankari': 45, 'Pallavi': 93, 'Sruthi': 62}
```

---

**Example 2: Filter Passed Students**

```python
passed_students = {student: score for (student, score) in student_scores.items() if score > 60}
print(passed_students)
```

**Output Example:**

```
{'vinay': 87, 'Pallavi': 93, 'Sruthi': 62}
```

---

**Example 3: Filter Failed Students**

```python
failed_students = {student: score for (student, score) in student_scores.items() if score < 60}
print(f"Failed Students: {failed_students}")
```

**Output Example:**

```
Failed Students: {'Shankari': 45}
```

---

### Summary Table

| Pattern        | Example                                            | Description                      |
| -------------- | -------------------------------------------------- | -------------------------------- |
| Basic creation | `{n: n**2 for n in range(5)}`                      | Creates keys & values from range |
| With function  | `{name: random.randint(1, 100) for name in names}` | Assigns random values            |
| With filter    | `{k: v for k, v in dict.items() if v > 60}`        | Keeps only matching items        |

---

**💡 Tip:** Comprehensions make your code shorter, cleaner, and more Pythonic. Use them for quick transformations and filtering instead of writing long loops.

```

Do you want me to also **merge this comprehension study file** into your **existing GitHub SQL_Interview_QA.md** so that **all your Python & SQL prep is in a single file** for uploads? That way you have one mega study guide.
```
