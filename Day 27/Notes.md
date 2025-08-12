# 🐍 Python Study Notes — Tkinter, Functions, *args & **kwargs

This file contains concepts about GUI programming with Tkinter, Python function arguments, and variable-length arguments (`*args` and `**kwargs`).

---

## 1️⃣ Tkinter — Creating a Basic GUI

**Tkinter** is Python’s built-in library for creating Graphical User Interfaces (GUI).

```python
import tkinter

# Create the main window
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Add a label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="bottom")  # Can be: "left", "right", "top", or use expand=True for center

# Keep the window open
window.mainloop()

````

**Key points:**

* `Tk()` → Creates the main window.
* `.title()` → Sets the window title.
* `.minsize()` → Sets the minimum size of the window.
* `.Label()` → Creates a text label.
* `.pack()` → Places the widget inside the window.
* `.mainloop()` → Keeps the GUI running until closed.

---

## 2️⃣ Default Parameters in Functions

Default parameters let you set a value for a parameter in case the caller doesn’t provide one.

```python
def foo(a, b=4, c=6):
    print(a, b, c)

foo(1)       # Output: 1 4 6
foo(1, 2)    # Output: 1 2 6
foo(1, 2, 3) # Output: 1 2 3
```

### ❗ Rules for Default Parameters

1. Non-default parameters **must** come before default parameters.
2. You cannot have a default parameter **followed by** a non-default one.

❌ This will cause an error:

```python
def example(a=1, b, c=20):  # ❌
    print(a, b, c)
```

✅ This is valid:

```python
def example(a, b=20, c=30):
    print(a, b, c)
```

---

## 3️⃣ `*args` — Unlimited Positional Arguments

* `*args` allows a function to accept **any number of positional arguments**.
* Inside the function, `args` is stored as a **tuple**.

```python
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(3, 5, 6))        # Output: 14
print(add(1, 2, 3, 4, 5))  # Output: 15
```

💡 **Tip:** The `*` means “gather all extra positional arguments into a tuple.”

### How `*args` stores data internally:

```
Function call: add(3, 5, 6)

args  -->  (3, 5, 6)    # A tuple containing all positional arguments
```

Visualized as:

| args (tuple) |
| ------------ |
| 3            |
| 5            |
| 6            |

---

## 4️⃣ `**kwargs` — Unlimited Keyword Arguments

* `**kwargs` lets you accept any number of **named (keyword) arguments**.
* Inside the function, `kwargs` is stored as a **dictionary**.

```python
def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))

calculate(add=3, sub=5, multiply=6)
# Output:
# {'add': 3, 'sub': 5, 'multiply': 6}
# <class 'dict'>
```

💡 **Tip:** The `**` means “gather all extra keyword arguments into a dictionary.”

### How `**kwargs` stores data internally:

```
Function call: calculate(add=3, sub=5, multiply=6)

kwargs  -->  {
    "add": 3,
    "sub": 5,
    "multiply": 6
}
```

Visualized as:

| Key        | Value |
| ---------- | ----- |
| "add"      | 3     |
| "sub"      | 5     |
| "multiply" | 6     |

---

### Example: Using `**kwargs` in a Calculation

```python
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=4)  
# Step-by-step:
# 2 + 3 = 5
# 5 * 4 = 20
# Output: 20
```

---

## 5️⃣ Using `**kwargs` in Classes

```python
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")     # .get() avoids errors if key is missing
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)   # Nissan
print(my_car.model)  # GT-R
```

If you used `kw["model"]` instead of `kw.get("model")` and `"model"` was missing,
Python would throw a **KeyError**.

---

## 📌 Summary Table — Arguments in Python

| Type       | Syntax     | Stored As | When to Use                         |
| ---------- | ---------- | --------- | ----------------------------------- |
| Positional | `a, b`     | variables | When the exact number is known      |
| Default    | `b=10`     | variables | When some arguments can be optional |
| `*args`    | `*args`    | tuple     | Unlimited positional arguments      |
| `**kwargs` | `**kwargs` | dict      | Unlimited keyword arguments         |

---

## 🧠 Pro Tip

* Avoid using names like `sum`, `list`, or `dict` as variable names — they overwrite Python’s built-in functions.
* Keep indentation correct — especially for `return` statements inside loops.

```
```
