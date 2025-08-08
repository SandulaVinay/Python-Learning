# Object-Oriented Programming (OOP) in Python

## 📜 Table of Contents
<details>
<summary>📂 OOP Concepts</summary>

- [What is OOP?](#what-is-oop)
- [Basic Terms](#basic-terms)
  - [Class](#1-class)
  - [Object](#2-object)
  - [Changing Attributes](#3-changing-attributes)
  - [Methods in a Class](#4-methods-in-a-class)
  - [Constructor (`__init__`)](#5-constructor-__init__)
- [The Six Main OOP Concepts](#the-six-main-oop-concepts)
- [Full Example: All Concepts Together](#full-example-all-concepts-together)
- [Quick Analogy](#quick-analogy)

</details>

<details>
<summary>📂 Types of Inheritance in Python</summary>

- [Single Inheritance](#1-single-inheritance)
- [Multiple Inheritance](#2-multiple-inheritance)
- [Multilevel Inheritance](#3-multilevel-inheritance)
- [Hierarchical Inheritance](#4-hierarchical-inheritance)
- [Hybrid Inheritance](#5-hybrid-inheritance)
- [Method Resolution Order (MRO)](#6-method-resolution-order-mro)

</details>

---

## OOP Concepts
<details>
<summary>📂 Click to expand OOP Concepts (What is OOP → Quick Analogy)</summary>

### What is OOP?
OOP stands for **Object-Oriented Programming**, a way of structuring programs by grouping **data** (attributes) and **behavior** (methods) into reusable units called **objects**.

---

### Basic Terms

#### 1. Class
```python
class SampleClass:
    attribute1 = 10
    attribute2 = 20

print(SampleClass.attribute1)
print(SampleClass.attribute2)
```
**Output:**
```
10
20
```

#### 2. Object
```python
object1 = SampleClass()
object2 = SampleClass()
print(object1.attribute1)
print(object2.attribute2)
```
**Output:**
```
10
20
```

#### 3. Changing Attributes
```python
object1.attribute1 = 100
print(object1.attribute1)
print(object2.attribute1)

SampleClass.attribute1 = 1
print(object1.attribute1)
print(object2.attribute1)
```
**Output:**
```
100
10
100
1
```

#### 4. Methods in a Class
```python
class SampleClass1:
    def sample_method(self):
        print("This method demonstrates a method in a class.")

obj = SampleClass1()
obj.sample_method()
```
**Output:**
```
This method demonstrates a method in a class.
```

#### 5. Constructor (`__init__`)
```python
class ConstructorClass:
    def __init__(self):
        print("Constructor called automatically when the object is created.")

obj = ConstructorClass()
```
**Output:**
```
Constructor called automatically when the object is created.
```

---

### The Six Main OOP Concepts
1. **Class**
2. **Object**
3. **Inheritance**
4. **Polymorphism**
5. **Encapsulation**
6. **Abstraction**

---

### Full Example: All Concepts Together
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")

account = BankAccount(1000)
account.deposit(500)
print("Account balance:", account.get_balance())
```
**Output:**
```
Buddy says: Woof!
Whiskers says: Meow!
Account balance: 1500
```

---

### Quick Analogy
- **Class**: Blueprint of a car  
- **Object**: A specific car built from the blueprint  
- **Attributes**: Color, brand, speed  
- **Methods**: Drive, brake, turn  
- **Inheritance**: Sports car inherits from car  
- **Polymorphism**: `drive()` works differently for race car vs truck  
- **Encapsulation**: You use steering without touching the engine  
- **Abstraction**: You press "start" without knowing engine details  

</details>

---

## Types of Inheritance in Python
<details>
<summary>📂 Click to expand Types of Inheritance with Examples</summary>

### 1. Single Inheritance
```python
class Car:
    def start_engine(self):
        print("Engine started")

class SportsCar(Car):
    def turbo_mode(self):
        print("Turbo mode activated!")

ferrari = SportsCar()
ferrari.start_engine()
ferrari.turbo_mode()
```
**Output:**
```
Engine started
Turbo mode activated!
```

---

### 2. Multiple Inheritance
```python
class Father:
    def driving_skill(self):
        print("I can drive a car")

class Mother:
    def cooking_skill(self):
        print("I can cook delicious food")

class Child(Father, Mother):
    def play(self):
        print("I can play football")

tom = Child()
tom.driving_skill()
tom.cooking_skill()
tom.play()
```
**Output:**
```
I can drive a car
I can cook delicious food
I can play football
```

---

### 3. Multilevel Inheritance
```python
class Grandfather:
    def legacy(self):
        print("Owns family farm")

class Father(Grandfather):
    def profession(self):
        print("Works as a teacher")

class Son(Father):
    def hobby(self):
        print("Plays guitar")

adam = Son()
adam.legacy()
adam.profession()
adam.hobby()
```
**Output:**
```
Owns family farm
Works as a teacher
Plays guitar
```

---

### 4. Hierarchical Inheritance
```python
class Company:
    def company_name(self):
        print("TechCorp Ltd.")

class Developer(Company):
    def role(self):
        print("Writes code")

class Designer(Company):
    def role(self):
        print("Designs UI/UX")

dev = Developer()
designer = Designer()
dev.company_name()
dev.role()
designer.company_name()
designer.role()
```
**Output:**
```
TechCorp Ltd.
Writes code
TechCorp Ltd.
Designs UI/UX
```

---

### 5. Hybrid Inheritance
```python
class Person:
    def speak(self):
        print("I can speak")

class Employee(Person):
    def work(self):
        print("I work at a company")

class Gamer:
    def play_game(self):
        print("I play video games")

class WorkingGamer(Employee, Gamer):
    def stream(self):
        print("I stream my gameplay")

john = WorkingGamer()
john.speak()
john.work()
john.play_game()
john.stream()
```
**Output:**
```
I can speak
I work at a company
I play video games
I stream my gameplay
```

---

### 6. Method Resolution Order (MRO)
```python
class Father:
    def greet(self):
        print("Hello from Father")

class Mother:
    def greet(self):
        print("Hello from Mother")

class Child(Father, Mother):
    pass

c = Child()
c.greet()

print(Child.__mro__)
```
**Output:**
```
Hello from Father
(<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)
```

**Another example (with `super()`):**
```python
class A:
    def show(self):
        print("A.show()")

class B(A):
    def show(self):
        print("B.show()")
        super().show()

class C(A):
    def show(self):
        print("C.show()")
        super().show()

class D(B, C):
    def show(self):
        print("D.show()")
        super().show()

d = D()
d.show()
print(D.__mro__)
```
**Output:**
```
D.show()
B.show()
C.show()
A.show()
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

</details>
