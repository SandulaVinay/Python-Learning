# 🧾 Python Objects: Attributes vs Methods (Short Notes)

## 🔹 What is an Object?
An **object** in Python is an instance of a class. It bundles together:
- **Attributes** (data)
- **Methods** (functions/behavior)

---

## 🔸 Attributes
- Act like **variables** inside an object.
- Hold **data/state** of the object.
- Can be **accessed or modified** using dot (`.`) notation.

```python
person.name = "Alice"
print(person.name)
```

---

## 🔸 Methods
- Are **functions defined inside a class**.
- Describe **behavior** or **actions** of the object.
- Can **use or modify attributes**.

```python
person.update_name("Bob")
```

---

## 🔁 Reusability of Objects
- Once an object is created, it can be:
  - **Reused** across your code.
  - **Called** to perform actions via methods.
  - **Modified** using its attributes or methods.

---

## ✅ Final Summary

> An object in Python has both **attributes** and **methods**.  
> **Attributes** store data, while **methods** define behavior.  
> Objects can be **reused**, and their data or behavior can be **accessed or changed** as needed.



# 📘 Python: Attributes vs Methods

This document explains the difference between **attributes** and **methods** in Python using examples, diagrams, and comparisons.

---

## 🔸 Attributes

### ➤ Definition:
Attributes are **variables** that belong to an **object** or **class**. They **hold data** or **state** about the object.

### ✅ Example:
```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand      # Attribute
        self.color = color      # Attribute

my_car = Car("Toyota", "Red")
print(my_car.brand)  # Output: Toyota
print(my_car.color)  # Output: Red
```

Here, `brand` and `color` are **attributes** of the `Car` class.

---

## 🔸 Methods

### ➤ Definition:
Methods are **functions defined inside a class** that operate on **objects (instances)** of that class. They can **access and modify attributes**.

### ✅ Example:
```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):            # Method
        print(f"{self.brand} engine started.")

my_car = Car("Toyota", "Red")
my_car.start_engine()  # Output: Toyota engine started.
```

Here, `start_engine()` is a **method** that operates on the `Car` object.

---

## 🧠 Summary Table

| Aspect       | Attribute                          | Method                               |
|--------------|-------------------------------------|---------------------------------------|
| What is it?  | Variable associated with an object  | Function associated with an object    |
| Purpose      | Stores data/state                  | Performs actions/behaviors            |
| Syntax       | `object.attribute`                 | `object.method()`                     |
| Example      | `my_car.color`                     | `my_car.start_engine()`               |

---

## 🧩 Visual Diagram: Attributes vs Methods

```
          +-----------------------+
          |       Car (Class)     |
          +-----------------------+
          | - brand               |  <-- Attribute (data)
          | - color               |  <-- Attribute (data)
          +-----------------------+
          | + start_engine()      |  <-- Method (behavior)
          | + repaint(new_color)  |  <-- Method (behavior)
          +-----------------------+
```

---

## 📌 Real-World Analogy

Imagine a **car object**:
- **Attributes** = characteristics → `"Red"`, `"Toyota"`
- **Methods** = actions → `start the engine`, `repaint the car`

---

## 🧪 Example: Attributes and Methods in Action

```python
class Car:
    wheels = 4   # Class Attribute (shared by all cars)

    def __init__(self, brand, color):   # Constructor method
        self.brand = brand              # Instance Attribute
        self.color = color              # Instance Attribute

    def start_engine(self):             # Instance Method
        print(f"{self.brand} engine started.")

    def repaint(self, new_color):       # Instance Method
        self.color = new_color
        print(f"Car repainted to {self.color}.")
```

```python
my_car = Car("Honda", "Blue")
my_car.start_engine()       # Output: Honda engine started.
print(my_car.color)         # Output: Blue
my_car.repaint("Black")     # Output: Car repainted to Black.
print(Car.wheels)           # Output: 4
```

---

## 🧠 Instance vs Class Attributes and Methods

| Type               | Definition                                  | Accessed via         | Example                          |
|--------------------|---------------------------------------------|-----------------------|----------------------------------|
| **Instance Attribute** | Belongs to one specific object             | `self.attribute`      | `self.brand`, `self.color`       |
| **Class Attribute**    | Shared across all instances of the class  | `ClassName.attribute` | `Car.wheels`                     |
| **Instance Method**    | Uses `self`, can access instance data     | `object.method()`     | `my_car.start_engine()`          |
| **Class Method**       | Uses `@classmethod` and `cls`             | `ClassName.method()`  | `@classmethod def show_info(cls)`|
| **Static Method**      | No `self` or `cls` used, like utility     | `ClassName.method()`  | `@staticmethod def utility()`    |

---

## 💡 Summary

- 📦 **Attributes** store **data** (e.g., color, brand).
- ⚙️ **Methods** define **behavior** (e.g., start_engine, repaint).
- 🔁 Use **`self`** to access instance-level data/methods.
- 🧩 Think of a class like a blueprint; attributes = properties, methods = actions.

---

> ✅ Tip: Practice by creating your own classes and experimenting with attributes and methods!
