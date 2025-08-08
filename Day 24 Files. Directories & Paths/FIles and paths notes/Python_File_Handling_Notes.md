
# 📁 Python File Handling – Notes and Examples

This document provides practical examples and notes on how to handle files in Python using both the traditional `open()` method and the `with` statement. You'll learn how to read, write, append, and create files.

---

## 📝 1. Opening and Reading a File

```python
file = open("Practice_File.txt")  # Opening file in default read mode
contents = file.read()           # Read the file content
print(contents)                  # Print contents to terminal
file.close()                     # Close the file manually to free system resources
```

> 🔒 Always remember to close the file when not using `with open`.

---

## ✅ 2. Using `with open()` (Recommended)

```python
with open("Practice_File.txt") as file:
    contents = file.read()
    print(contents)
```

> ✅ **`with`** automatically handles closing the file, even if an error occurs — it's cleaner and safer.

---

## ❌ 3. Writing Without Write Mode – Causes Error

```python
with open("Practice_File.txt") as file:
    file.write("My surname is sandula")  # ❌ Error: File not opened in write mode
```

> ❗ Default mode is read (`"r"`). Writing is not allowed unless explicitly set.

---

## ✍️ 4. Writing to a File (Overwrites)

```python
with open("Practice_File.txt", mode="w") as file:
    file.write("My surname is sandula\n")  # Overwrites existing content

with open("Practice_File.txt") as file:
    contents = file.read()
    print(contents)
```

> ✏️ `"w"` mode **overwrites** the file if it already exists.

---

## ➕ 5. Appending to an Existing File

```python
with open("Practice_File.txt", mode="a") as file:
    file.write("\nMy Last Name is Vinay")  # Appends new content without deleting existing text

with open("Practice_File.txt") as file:
    content = file.read()
    print(content)
```

> 📌 Use `"a"` mode to **append** without replacing existing content.

---

## 🆕 6. Creating a New File and Writing Content

```python
with open("New Practice File.txt", mode="w") as file:
    file.write("This file is created through below code in python\n")
    file.write("with open('New Practice File.txt', mode='w') as file:\n")
    file.write("    file.write('Give what you want in file with quotation marks')\n")
```

```python
with open("New Practice File.txt", mode="r") as file:
    contents = file.read()
    print(contents)
```

> ✅ If the file doesn’t exist, `"w"` will create it.

---

## 🧹 7. Clearing Contents of a File

```python
with open("New Practice File.txt", mode="w") as file:
    contents = file.write("")  # Empty string deletes content

with open("New Practice File.txt") as file:
    contents = file.read()
    print(contents)
```

> 🧽 Writing an empty string with `"w"` mode **clears** all contents in the file.

---

## 🔚 Summary of File Modes

| Mode | Description                         |
|------|-------------------------------------|
| `"r"` | Read (default)                     |
| `"w"` | Write (overwrites existing content)|
| `"a"` | Append to end of file              |
| `"x"` | Create file (error if exists)      |
| `"b"` | Binary mode (e.g., `"rb"`, `"wb"`) |
| `"t"` | Text mode (default)                |

---

## ✅ Best Practices

- Always use `with open(...)` to ensure the file is properly closed.
- Use `"w"` to overwrite and `"a"` to append.
- Handle exceptions for better fault tolerance (e.g., use `try...except`).
- Use `os.path.exists()` before deleting or overwriting critical files.

---

> 🔐 Proper file handling is crucial for reading logs, writing reports, saving state, and managing data pipelines in Python.
