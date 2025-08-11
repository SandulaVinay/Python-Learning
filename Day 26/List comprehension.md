# Python List Comprehension – Beginner to Advanced Notes

List comprehension in Python is a concise way to create new lists by applying an expression to each item in an iterable (like lists, tuples, or strings), optionally including a condition for filtering.

---

## 📌 Syntax

```python
new_list = [expression for item in iterable if condition]
````

* **expression** → The operation or value to add to the new list.
* **item** → The variable representing each element in the iterable.
* **iterable** → A sequence (list, tuple, string, etc.) you loop through.
* **condition** *(optional)* → A filter to include only certain items.

### ✅ Real-Time Example

```python
numbers = [1, 2, 3, 4, 5]
squared_even_numbers = [n * n for n in numbers if n % 2 == 0]
print(squared_even_numbers)  # Output: [4, 16]
```

---

## **Q1: Normal Loop vs List Comprehension**

**Question:**
Write a Python program to add 1 to each number in a given list using:

1. A normal `for` loop
2. List comprehension.

**Answer:**

```python
# Normal for loop
numbers = [1, 2, 3]
for n in numbers:
    add = n + 1
    print(add)

# List comprehension
numbers = [1, 2, 3]
list_comprehension = [n + 1 for n in numbers]
print(list_comprehension)
```

---

## **Q2: String Iteration**

**Question:**
Convert the word `"vinay"` into a list of individual characters using list comprehension.

**Answer:**

```python
name = "vinay"
list_comprehension = [letter for letter in name]
print(list_comprehension)  # Output: ['v', 'i', 'n', 'a', 'y']
```

---

## **Q3: Range with List Comprehension**

**Question:**
Generate a list of numbers from 1 to 5 using `range()` inside a list comprehension.

**Answer:**

```python
list_comprehensive = [num for num in range(1, 6)]
print(list_comprehensive)  # Output: [1, 2, 3, 4, 5]
```

---

## **Q4: Filter Short Names**

**Question:**
Given a list of names, filter and return only those with less than 4 characters using list comprehension.

**Answer:**

```python
names = ["vinay", "Shankari", "Pallavi", "Sruthi", "Indhu", "Sid", "sui"]
short_names = [name for name in names if len(name) < 4]
print(short_names)  # Output: ['Sid', 'sui']
```

---

## **Q5: Transform Long Names to Uppercase**

**Question:**
From a list of names, create a new list with only names having more than 5 characters, and convert them to uppercase using list comprehension.

**Answer:**

```python
names = ["vinay", "Shankari", "Pallavi", "Sruthi", "Indhu", "Sid", "sui"]
long_names_upper = [name.upper() for name in names if len(name) > 5]
print(long_names_upper)  # Output: ['SHANKARI', 'PALLAVI', 'SRUTHI']
```

---

## **Q6: Squaring Numbers**

**Question:**
Given a list of numbers, return a list containing the square of each number using list comprehension.

Example input:
`[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]`
Expected output:
`[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]`

**Answer:**

```python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)
```

---

## **Q7: Filtering Even Numbers**

**Question:**
Given a list of strings containing numbers,

1. Convert them into integers.
2. Create a new list containing only even numbers.
   Use list comprehension for both steps.

**Answer:**

```python
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)  # Output: [0, 32, 8, 2, 8, 64, 42]
```

---

## **Q8: Data Overlap from Files**

**Question:**
Two text files, `file1.txt` and `file2.txt`, each contain a list of numbers (one per line).
Write a Python program to:

1. Read both files.
2. Find the numbers common to both files.
3. Store them in a list of integers.
   Use list comprehension to solve this.

Example:

**file1.txt**

```
3
6
5
8
33
12
7
4
72
2
42
13
```

**file2.txt**

```
3
6
13
5
7
89
12
3
33
34
1
344
42
```

Expected output:
`[3, 6, 5, 33, 12, 7, 42, 13]`

**Answer:**

```python
with open("file1.txt") as f1:
    file1_numbers = [int(line.strip()) for line in f1]

with open("file2.txt") as f2:
    file2_numbers = [int(line.strip()) for line in f2]

result = [num for num in file1_numbers if num in file2_numbers]
print(result)
```

---

## **Q9: Square Only Even Numbers**

**Question:**
From a list of numbers, return a new list containing the square of only the even numbers.

**Answer:**

```python
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)  # Output: [4, 16, 36]
```

---

## **Q10: Convert Names to Uppercase**

**Question:**
Given a list of names, return a new list where each name is converted to uppercase using list comprehension.

**Answer:**

```python
names = ["vinay", "Angela", "Varun"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)  # Output: ['VINAY', 'ANGELA', 'VARUN']
```

---

## **Q11: First Letter of Each Word**

**Question:**
Given a list of words, create a list of their first letters using list comprehension.

**Answer:**

```python
words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]
print(first_letters)  # Output: ['a', 'b', 'c']
```

---

## **Q12: Filter Numbers Greater than 10**

**Question:**
From a list of numbers, create a list containing only numbers greater than 10 using list comprehension.

**Answer:**

```python
numbers = [5, 12, 7, 18, 3, 25]
greater_than_10 = [n for n in numbers if n > 10]
print(greater_than_10)  # Output: [12, 18, 25]
```

---

## 📝 Summary Table – List Comprehension Patterns

| Pattern                    | Example                                           | Description                   |
| -------------------------- | ------------------------------------------------- | ----------------------------- |
| Basic transformation       | `[n+1 for n in numbers]`                          | Adds 1 to each element        |
| Filtering                  | `[n for n in numbers if n%2==0]`                  | Keeps only even numbers       |
| String to list             | `[ch for ch in "vinay"]`                          | Breaks string into characters |
| Conditional transformation | `[name.upper() for name in names if len(name)>5]` | Uppercase long names          |

---

**💡 Tip:** Always start with a normal `for` loop to understand the logic, then rewrite it as a list comprehension for cleaner, shorter code.
