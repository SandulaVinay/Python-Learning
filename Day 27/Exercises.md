### Question 1

```python
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(1, 2)
````

**What is the output?**

* `spam` = 1 (positional)
* `eggs` = 2 (positional)
* `toast` = default value `'yes please!'` (not provided, so default used)
* `ham` = default value `0` (not provided, so default used)

**Output:**

```
1 2 yes please! 0
```

---

### Question 2

```python
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(toast='nah', spam=4, eggs=2)
```

**What is the output?**

Arguments passed with keywords:

* `toast='nah'` overrides default
* `spam=4`
* `eggs=2`
* `ham` is not provided, so default `0` is used

**Output:**

```
4 2 nah 0
```

---

### Question 3

```python
def test(*args):
    print(args)
 
test(1,2,3,5)
```

**What is the data type of `args`?**

* `*args` collects all positional arguments into a **tuple**.

So the data type of `args` is:

```python
tuple
```

---

### Question 4

```python
def test(*args):
    print(args)
 
test(1,2,3,5)
```

**What is the output?**

Since `args` is a tuple containing `(1, 2, 3, 5)`, the output will be:

```
(1, 2, 3, 5)
```

---

### Question 5

```python
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)
```

**What is the output?**

* `a` gets the first positional argument: `4`
* `*args` collects all other positional arguments as a tuple: `(7, 3, 0)`
* `**kw` collects keyword arguments into a dictionary: `{'x': 10, 'y': 64}`

**Output:**

```
4 (7, 3, 0) {'x': 10, 'y': 64}
```

---
