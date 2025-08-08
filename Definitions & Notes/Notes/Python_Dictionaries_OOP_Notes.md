# 📘 Python Dictionaries from Basics to OOP – Notes

---

## 🔰 What Is a Dictionary in Python?

A **dictionary** is a way to store **key-value pairs**, like a real-life dictionary:

```python
my_dict = {
    "apple": "a fruit",
    "book": "something you read"
}
```

---

## ✅ Basics

### 1. Create a Dictionary
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

### 2. Access Values
```python
print(person["name"])  # Output: Alice
```

### 3. Add a New Pair
```python
person["job"] = "Engineer"
```

### 4. Change a Value
```python
person["age"] = 26
```

### 5. Delete a Pair
```python
del person["city"]
```

---

## 🛠 Dictionary Functions

| Function   | Use                         | Example                         |
|------------|------------------------------|----------------------------------|
| `.get()`   | Safe way to get a value     | `person.get("name")`             |
| `.keys()`  | Get all keys                | `person.keys()`                  |
| `.values()`| Get all values              | `person.values()`                |
| `.items()` | Get all key-value pairs     | `person.items()`                 |
| `.update()`| Add/update multiple values  | `person.update({"age": 30})`     |
| `.pop()`   | Remove a key and return it  | `person.pop("age")`              |

---

## 🔁 Looping Through a Dictionary

```python
for key, value in person.items():
    print(f"{key} is {value}")
```

---

## ✅ Check if a Key Exists

```python
if "name" in person:
    print("Name exists!")
```

---

## 🧰 Nested Dictionary

```python
users = {
    "alice": {"age": 25, "job": "Engineer"},
    "bob": {"age": 30, "job": "Doctor"}
}
print(users["bob"]["job"])  # Output: Doctor
```

---

## 🚀 Advanced Tips

### Dictionary Comprehension

```python
squares = {x: x**2 for x in range(1, 6)}
```

### Swap Keys and Values

```python
original = {'a': 1, 'b': 2}
swapped = {v: k for k, v in original.items()}
```

---

# ⚙️ OOP + Dictionaries (Real Project Example)

### 🗂 FILE STRUCTURE

```
project/
├── main.py
├── data.py
```

---

### 📁 data.py

```python
people_data = {
    "alice": {"age": 25, "job": "Engineer", "city": "New York"},
    "bob": {"age": 30, "job": "Doctor", "city": "Chicago"},
    "carol": {"age": 28, "job": "Designer", "city": "Boston"}
}
```

---

### 🧠 main.py

```python
from data import people_data

class Person:
    def __init__(self, name, info_dict):
        self.name = name
        self.age = info_dict.get("age")
        self.job = info_dict.get("job")
        self.city = info_dict.get("city")

    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.age}-year-old {self.job} from {self.city}.")

    def relocate(self, new_city):
        self.city = new_city
        print(f"{self.name} moved to {self.city}.")

# Create Person objects
people_objects = {}

for name, info in people_data.items():
    person = Person(name.capitalize(), info)
    people_objects[name] = person

# Use the objects
people_objects["alice"].introduce()
people_objects["bob"].relocate("San Francisco")
people_objects["carol"].introduce()
```

---

## 🧠 Concept Summary

- Dictionary = data storage
- OOP (classes) = behavior + structure
- Combine both for real-world modeling
- Use `.items()` to loop through dictionary
- Use `.get()` to safely access data