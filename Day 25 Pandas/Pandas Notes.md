
````markdown
# Beginner’s Guide to Python Data Analysis with Pandas

Welcome! This guide explains essential Python code snippets for working with tabular data using [Pandas](https://pandas.pydata.org/). It covers everything from reading CSV files to analyzing and exporting data, with detailed comments at each step so even absolute beginners can follow along.

---

## What is Pandas?

**Pandas** is a powerful Python library designed for data manipulation and analysis. It simplifies tasks like reading and writing spreadsheet data, calculating statistics, filtering information, and more.

### Why Use Pandas?

- Handles large datasets efficiently.
- Provides intuitive ways to access, modify, and analyze data.
- Supports many file formats: CSV, Excel, SQL, and more.

### Basic Example

```python
import pandas as pd

# Load data from a CSV file
data = pd.read_csv("weather_data.csv")
print(data)
````

---

## Section 1: Reading and Creating Data with Pandas

### Reading CSV Data

```python
import pandas

data = pandas.read_csv("weather_data.csv")
```

**Explanation:**

* `pandas.read_csv("filename.csv")`: Reads a CSV file and loads its content into a *DataFrame* (like a spreadsheet table).
* `data`: Now contains the table of weather data.

### Exploring Columns

```python
print(data["temp"])      # Access by column name
print(data.temp)         # Access by attribute
```

* Both lines display the "temp" column (temperature readings) from your data.
* Great for quickly inspecting column contents.

### Converting DataFrame to Dictionary

```python
data_dict = data.to_dict()
```

* Converts the whole table into a Python dictionary structure (handy for advanced manipulation).

---

## Section 2: Calculating Statistics

### Find Mean/Average Value

```python
temp_list = data["temp"].to_list()
average = sum(temp_list) / len(temp_list)
print(average)
```

* `to_list()`: Converts a column into a regular Python list.
* Calculates average temperature manually.

```python
print(data["temp"].mean())
```

* `.mean()`: Pandas method that directly computes the average for you.

> **Tip:** You can perform powerful calculations with just a single Pandas method!

### Find Maximum Value

```python
print(data["temp"].max())
```

* `.max()`: Finds the largest value in the column.

---

## Section 3: Filtering Data with Pandas

### Filter Rows by Value

```python
print(data[data.day == "Monday"])
```

* Returns only the rows where `"day"` is `"Monday"`.

### Filter for Maximum Value

```python
print(data[data.temp == data.temp.max()])
```

* Displays the row(s) with the highest temperature.

---

## Section 4: Creating DataFrames from Scratch

```python
data_dict = {
  "Students": ["Vinay", "Angela", "Varun"],
  "Scores": ["76", "56", "65"]
}

data = pandas.DataFrame(data_dict)
data.to_csv("Pandas_dict.csv")
```

* `pandas.DataFrame(dict)`: Creates a table from a Python dictionary.
* `to_csv("filename.csv")`: Saves the table as a new CSV file.

---

## Section 5: Analyzing Squirrel Colors

Suppose you want to count how many Central Park squirrels have different fur colors.

```python
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
```

**Step-by-Step Explanation:**

1. Read the big squirrel data file with Pandas.
2. `data[data["Primary Fur Color"] == "Gray"]`: Filters only squirrels that are gray.
3. `len(...)`: Counts how many rows matched (i.e., number of gray squirrels).
4. Repeat for "Cinnamon" and "Black" fur colors.

### Collating the Results

```python
data_dict = {
  "Fur Color": ["Gray", "Cinnamon", "Black"],
  "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("Squirrel_Count.csv")
```

**What’s Happening Here?**

* All the results are combined into a dictionary and then into a DataFrame.
* DataFrame is exported as `"Squirrel_Count.csv"` — a summary of squirrel colors and their counts.

---

## Section 6: Useful Pandas Functions Explained

| Function               | What it Does                                    | Example Usage                         |
| ---------------------- | ----------------------------------------------- | ------------------------------------- |
| `read_csv`             | Loads data from a CSV file                      | `pd.read_csv("data.csv")`             |
| `to_list`              | Converts column/Series to a regular Python list | `data["col"].to_list()`               |
| `mean()`               | Calculates the average value of a column/Series | `data["score"].mean()`                |
| `max()`                | Finds the maximum value in column/Series        | `data["score"].max()`                 |
| `DataFrame(data_dict)` | Creates a table from a Python dictionary        | `pd.DataFrame({"names": ["A", "B"]})` |
| `to_csv`               | Saves DataFrame to a CSV file                   | `data.to_csv("filename.csv")`         |
| Filtering              | Select rows by condition                        | `data[data["color"] == "Gray"]`       |

---

## Full Example Output

Given the squirrel color counting code above, your CSV, `"Squirrel_Count.csv"` looks like:

| Fur Color | Count |
| --------- | ----- |
| Gray      | 2,473 |
| Cinnamon  | 392   |
| Black     | 103   |

---

> **Tip:** Pandas allows for very powerful and concise data operations. Whenever possible, use Pandas built-in methods—they are optimized and well-tested.

---

## Final Thoughts

* Pandas makes working with spreadsheet-style data in Python much easier.
* Start by loading data with `read_csv`, then use Pandas methods for all your calculations and filters.
* Export results as needed with `to_csv`.
* Don’t be afraid to experiment—Pandas is widely used in data science and makes so many tasks straightforward.
---
