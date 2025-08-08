# Python File Handling Notes

## 1. Opening and Reading a File

```python
file = open("Practice_File.txt")  # "" are important to open a file.
contents = file.read()            # To read the file.
print(contents)                   # Display the file content in terminal.
file.close()                      # Always close the file after opening to free system resources.
```

**Key Point:**  
The `open()` function opens a file, but you must manually close it using `file.close()`.

---

## 2. Using `with` for Automatic File Closing

```python
with open("Practice_File.txt") as file:
    contents = file.read()
    print(contents)
```

**Why use `with`?**  
- Automatically closes the file once the block ends.  
- Prevents resource leaks.

---

## 3. Attempting to Write in Read Mode

```python
with open("Practice_File.txt") as file:
    file.write("My surname is sandula")
```
**Output:**  
```
io.UnsupportedOperation: not writable
```
**Reason:** Default mode is **read-only** (`"r"`), so writing is not allowed.

---

## 4. Writing to a File

```python
with open("Practice_File.txt", mode="w") as file:
    file.write("My surname is sandula\n")
    contents = file.read()  # This will cause an error since the file is in write mode.
```

**Notes:**  
- `"w"` mode overwrites the file.  
- You cannot read immediately after writing without reopening in read mode.

---

## 5. Reading the Updated File

```python
with open("Practice_File.txt") as file:
    contents = file.read()
    print(contents)
```

---

## 6. Appending to a File

```python
with open("Practice_File.txt", mode="a") as file:
    file.write("\nMy Last Name is Vinay")
```
- `"a"` mode **adds** to the file instead of replacing its contents.

---

## 7. Creating a New File and Writing Data

```python
with open("New Practice File.txt", mode="w") as file:
    file.write("This file is created through Python with 'with open'...")
```

- `"w"` mode will create the file if it does not exist.

---

## 8. Clearing File Contents

```python
with open("New Practice File.txt", mode="w") as file:
    file.write("")  # This clears the file.
```

---

## 9. Challenge 1: Reading a File from Absolute Path

```python
with open(r"C:\Users\indup\Desktop\Power BI Challanges\Python Challange.txt") as file:
    content = file.read()
    print(content)
```

---

## 10. Challenge 2: Attempting Relative Path with Absolute Reference (Incorrect)

```python
with open(r"..\..\..\C:\Users\indup\Desktop\Power BI Challanges\Python Challange.txt") as file:
    content = file.read()
    print(content)
```
**Note:** This is not a valid relative path; mixing relative and absolute references is incorrect.
