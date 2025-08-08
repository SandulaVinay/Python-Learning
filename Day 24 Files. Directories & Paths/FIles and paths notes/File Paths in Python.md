# 📂 File Paths in Python

## **1. Understanding Paths**

A **path** is a way to tell Python where a file is located on your computer.

- `/` → Root folder (top-most directory in a file system)
- **Absolute Path** → Full path from the root folder to the file.
- **Relative Path** → Path relative to the *current working directory* (the folder where your Python script is running).

---

## **2. Example Folder Structure**

```
/Root
  /Work
    report.doc
    /Project
      talk.ppt
```

---

## **3. Absolute File Path**

An **absolute path** specifies the location of a file starting from the root directory.

Example:  
```
/Work/Project/talk.ppt
```

---

## **4. Relative File Path**

Relative paths are based on **where you currently are** (your working directory).

- If your **current folder** is `/Work/Project`:
    ```
    ./talk.ppt
    ```
    (`./` means “current folder”)

- If your **current folder** is `/Work`:
    ```
    ./Project/talk.ppt
    ```

- If you need to go **up one folder** from `/Work/Project` to `/Work`:
    ```
    ../report.doc
    ```
    (`../` means “go up one level”)

---

## **5. Visual Folder Navigation Guide**

```
📂 /Work
│
├── 📄 report.doc
│
└── 📂 Project
     └── 📄 talk.ppt
```

**Legend:**
- `./file` → Look for file in **current folder**.
- `../file` → Go **up one folder** and look there.

**Examples:**
1. Current folder = `/Work/Project` → `./talk.ppt`
2. Current folder = `/Work` → `./Project/talk.ppt`
3. Current folder = `/Work/Project` → `../report.doc`

---

## **6. Real-World Scenario**

> You are working in **Visual Studio Code**.  
> Your Python script is in **Drive D:** but you need to open a file from **Drive C:**.

**Python Code Example:**
```python
with open("C:/Users/YourName/Desktop/File_Name.txt", "r") as file:
    contents = file.read()
    print(contents)
```

---

## **7. Tips**
- Always use `/` (forward slash) in paths for cross-platform compatibility, even on Windows.
- You can check your **current working directory** in Python:
```python
import os
print(os.getcwd())
```
- You can also build paths dynamically:
```python
import os
path = os.path.join("Work", "Project", "talk.ppt")
print(path)  # Work/Project/talk.ppt
```

---

✅ **Key Takeaway:**  
- **Absolute paths** give the full location from root → file.  
- **Relative paths** are based on where your Python script is currently running.  
- Use `../` to go up a folder, `./` to stay in the current folder.
