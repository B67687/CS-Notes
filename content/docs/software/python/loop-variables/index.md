---
title: "♻️ Loop Variables"
date: 2025-11-08
draft: false
---


A common mistake in Python is assuming that the loop variable inside a `for` loop is an alias or a direct reference to the element in the original sequence.
> In Python, the loop variable is typically a **copy of the value** or a **new reference** that is local to the loop.

---

## 🛑 The Core Principle: Local Assignment

When a Python `for` loop iterates over a sequence (`x`):

- In each iteration, the loop creates a temporary variable (e.g., `i`).
- It assigns the **value** of the current element from the list (`x`) to this temporary variable (`i`).

When you perform an assignment *inside* the loop (`i = "e"`), you are simply reassigning the loop variable `i` to point to a new object (`"e"`). This assignment **does not affect** the elements stored in the original list `x`.

### Example of No Change

```python
x = [1, 2, 3, 4]

# 'i' gets the value 1.
# Then 'i' is reassigned to point to 'e'.
# The list 'x' is never touched.
for i in x:
    i = "e"

print(x)
# Output: [1, 2, 3, 4]
```

---

## 💡 How to Correctly Modify the List

To modify the original list (`x`), you must use the element's **index** to explicitly target its location in memory.

### Method 1: Iterating by Index (Recommended)

Use `range(len(x))` to generate the indices, then use those indices to modify the list directly.

```python
x = [1, 2, 3, 4]

# Loop through indices 0, 1, 2, 3
for index in range(len(x)):
    # Target the memory location x[index]
    x[index] = "e"

print(x)
# Output: ['e', 'e', 'e', 'e']
```

### Method 2: Using List Comprehension (Idiomatic Python)

For creating a *new* list based on transformations of the old one, list comprehension is the most concise method.

```python
x = [1, 2, 3, 4]

# Creates a NEW list where every element is "e"
new_x = ["e" for _ in x]

print(new_x)
# Output: ['e', 'e', 'e', 'e']
```

---

## ⚠️ Advanced Note: Mutability (The "Gotcha" Exception)

This rule applies to assignment (`i = "e"`). The exception is when the elements *themselves* are mutable (like a nested list) and you modify them **in place** using a method or index access.

- The loop variable `i` still references the mutable object.
- If you use a method that changes the object *i points to* (e.g., `i.append(10)`), the change **is visible** in the original list `x`.

```python
y = [[1], [2], [3]]

for i in y:
    # This modifies the list object 'i' points to (a nested list)
    i.append(100)

print(y)
# Output: [[1, 100], [2, 100], [3, 100]]
```
