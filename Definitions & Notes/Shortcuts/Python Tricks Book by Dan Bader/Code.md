# 📚 Python Tricks Notes

---

## Table of Contents

<details>
<summary><strong>Assert in Python</strong> — Chapter 2.1: Covering Your A** With Assertions</summary>

1. [Scenario: Assert in Python — An Example](#1-scenario-assert-in-python--an-example)  
2. [Function Overview](#2-function-overview)  
3. [Code Listing](#3-code-listing)  
4. [Inputs Explained](#4-inputs-explained)  
5. [Step-by-Step Calculation](#5-step-by-step-calculation)  
6. [Assertion Check](#6-assertion-check)  
7. [Examples](#7-examples)  
8. [Edge Cases & Gotchas](#8-edge-cases--gotchas)  
9. [Production-Safe Version (Refined)](#9-production-safe-version-refined)  
10. [Quick Tests (Doctest/Unit Test Snippets)](#10-quick-tests-doctestunit-test-snippets)  
11. [How to Extend These Notes](#11-how-to-extend-these-notes)  

</details>

---

# Assert in Python  
*Python Tricks — Chapter 2.1: Covering Your A\*\* With Assertions*

## 1. Scenario: Assert in Python — An Example
Suppose you’re building an online store in Python, adding discount coupon functionality.  
The `apply_discount` function should ensure the discounted price is **never less than $0** and **never greater than the original price**.

> **Example product**:  
```python
shoes = {'name': 'Fancy Shoes', 'price': 14900}  # price in cents
````

---

## 2. Function Overview

Applies a fractional discount to a product’s price, ensures validity via `assert`, and returns the final integer price.

---

## 3. Code Listing

```python
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price
```

---

## 4. Inputs Explained

* **`product`** → dict with `'price'` key, e.g., `{'name': 'Laptop', 'price': 1000}`
* **`discount`** → fraction between `0.0` and `1.0` (e.g., `0.2` = 20% off)

---

## 5. Step-by-Step Calculation

Example:

```python
product = {'name': 'Laptop', 'price': 1000}
discount = 0.2
```

1. `1.0 - discount` → `0.8`
2. Multiply by price → `1000 * 0.8 = 800.0`
3. Convert to int → `800`
4. ✅ Return `800`

---

## 6. Assertion Check

```python
assert 0 <= price <= product['price']
```

Guarantees:

* Price ≥ 0
* Price ≤ original

> ⚠️ Note: Assertions can be disabled with `python -O`

---

## 7. Examples

```python
product = {'name': 'Laptop', 'price': 1000}
print(apply_discount(product, 0.2))  # 800

product = {'name': 'Phone', 'price': 500}
print(apply_discount(product, 0.5))  # 250
```

---

## 8. Edge Cases & Gotchas

1. **`int()` truncates** → may under/overcharge by a cent
2. Validate discount bounds (0–1)
3. Floating-point precision issues
4. Assertions are not runtime-safe validation in production

---

## 9. Production-Safe Version (Refined)

```python
def apply_discount_safe(product: dict, discount: float) -> int:
    if not (0.0 <= discount <= 1.0):
        raise ValueError("Discount must be between 0.0 and 1.0")
    price = round(product['price'] * (1.0 - discount))
    if not (0 <= price <= product['price']):
        raise ValueError("Price out of bounds")
    return int(price)
```

---

## 10. Quick Tests (Doctest/Unit Test Snippets)

```python
assert apply_discount({'price': 1000}, 0.2) == 800
assert apply_discount({'price': 500}, 1.0) == 0
```

---

## 11. How to Extend These Notes

* Follow same structure: **Scenario → Function → Code → Steps → Checks → Examples → Edge Cases**
* Update TOC accordingly
* Keep anchors (`#heading-name`) consistent for easy GitHub navigation

````

---

✅ With this **`<details>` collapsible style**, you can later add more sections like:

```markdown
<details>
<summary><strong>Functions in Python</strong> — Chapter 3.1</summary>
...
</details>
````

and your GitHub README will stay neat with expandable sections.

Do you want me to now **set up a master template** with this TOC + collapsible format so that each future Python Tricks topic fits in automatically? That way you just paste your notes and it’s ready for GitHub.
