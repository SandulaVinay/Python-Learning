# Python List Comprehension – Complete Notes

---

## **Definition**
**List comprehension** is a concise way to create lists in Python.  
It combines loops and conditional logic into a single line, making code shorter and more readable.

---

## **General Syntax**
```python
new_list = [expression for item in iterable if condition]

````

### **Parts:**

* **expression** → The operation or value to store in the new list.
* **item** → Variable representing each element from the iterable.
* **iterable** → Sequence to loop through (e.g., list, tuple, string, range).
* **condition** *(optional)* → Filter elements (only include items that satisfy it).

---

## **Basic Examples**

### **1. Normal Loop vs List Comprehension**

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
# Output: [2, 3, 4]
```

---

### **2. String Iteration**

```python
name = "vinay"
letters = [letter for letter in name]
print(letters)
# Output: ['v', 'i', 'n', 'a', 'y']
```

---

### **3. Range with List Comprehension**

```python
list_comp = [num * 1 for num in range(1, 6)]
print(list_comp)
# Output: [1, 2, 3, 4, 5]
```

---

## **Conditional List Comprehension**

### **4. Filter Short Names**

```python
names = ["vinay", "Shankari", "Pallavi", "Sruthi", "Indhu", "Sid", "sui"]
short_names = [name for name in names if len(name) < 4]
print(short_names)
# Output: ['Sid', 'sui']
```

---

### **5. Transform Long Names to Uppercase**

```python
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
# Output: ['SHANKARI', 'PALLAVI', 'SRUTHI']
```

---

## **Practical Exercises**

### **6. Squaring Numbers**

```python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)
# Output: [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
```

---

### **7. Filtering Even Numbers**

```python
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)
# Output: [0, 32, 8, 2, 8, 64, 42]
```

---

### **8. Data Overlap from Files**

```python
# Read and strip lines from both files
with open("file1.txt") as f1:
    file1_numbers = [int(line.strip()) for line in f1]

with open("file2.txt") as f2:
    file2_numbers = [int(line.strip()) for line in f2]

# Find common numbers
result = [num for num in file1_numbers if num in file2_numbers]
print(result)
# Example Output: [3, 6, 5, 33, 12, 7, 42, 13]
```

---

## **Extra Examples for Clarity**

### **9. Square Only Even Numbers**

```python
numbers = [1, 2, 3, 4, 5, 6]
new_list = [n * n for n in numbers if n % 2 == 0]
print(new_list)
# Output: [4, 16, 36]
```

---

### **10. Convert Names to Uppercase**

```python
names = ["vinay", "pallavi", "sruthi"]
upper_names = [name.upper() for name in names]
print(upper_names)
# Output: ['VINAY', 'PALLAVI', 'SRUTHI']
```

---

### **11. First Letter of Each Word**

```python
words = ["Apple", "Banana", "Cherry"]
first_letters = [word[0] for word in words]
print(first_letters)
# Output: ['A', 'B', 'C']
```

---

### **12. Filter Numbers Greater than 10**

```python
numbers = [4, 11, 7, 15, 2]
greater_than_10 = [n for n in numbers if n > 10]
print(greater_than_10)
# Output: [11, 15]
```

---

## **Key Benefits of List Comprehension**

* **Cleaner Code:** One line instead of multiple loop lines.
* **Faster Execution:** Optimized in Python for speed.
* **More Readable:** Shows the intent clearly.

✅ **Tip:** Keep it simple—avoid overcomplicating list comprehensions with too many conditions or nested loops.

---

```
```
