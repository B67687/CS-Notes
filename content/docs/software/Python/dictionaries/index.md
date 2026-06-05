---
title: "📚 Dictionaries"
date: 2025-11-08
draft: false
---


A dictionary (`dict`) is a built-in Python data structure that stores data in **key-value pairs**. It is designed for **fast, flexible lookups** using an associated **key** (label) rather than a positional index.

---

## ⚡️ Core Concepts & Access Speed

- **Mapping, Not Sequence:** Dictionaries map keys to values; they are not sequential like lists.
- **Key-Based Lookup:** Values are retrieved using their unique key, not a numerical index.
- **Constant Time ($O(1)$):** Dictionary access (lookup) is extremely fast, taking roughly the same amount of time regardless of dictionary size. This is achieved using **hashing** where the key's hash value points directly to the value's location in memory.

### Time Complexity Analogy

| Structure | Access Type | Lookup Time Complexity |
| :--- | :--- | :--- |
| **List** | Positional Index | $O(1)$ |
| **List** | Value Search | $O(n)$ |
| **Dictionary** | Key Lookup | $O(1)$ |

The formula for constant time is often denoted as: $T(n) = O(1)$.

---

## 🔑 Accessing Dictionary Values

There are two primary ways to retrieve values from a dictionary:

### 1. Square Brackets `[]` (Direct Access)

- **Syntax:** `my_dict[key]`
- **Behavior:** Returns the value associated with the key.
- **Error Handling:** If the key does not exist, it raises a **`KeyError`**.

``` python
student = {"id": 101, "name": "Ava"}

# Accessing a value
student_id = student["id"]
# Output: 101

# Attempting to access a missing key raises a KeyError
# major = student["major"]
```

### 2. The `.get()` Method (Safe Access)

- **Syntax:** `my_dict.get(key, default_value)`
- **Behavior:** Returns the value if the key exists.
- **Error Handling:** If the key does not exist, it returns the `default_value` (or `None` if no default is provided), preventing the program from crashing.

``` python
student = {"id": 101, "name": "Ava"}

# Key exists
name = student.get("name")
# Output: 'Ava'

# Key does not exist, returns None
major = student.get("major")
# Output: None

# Key does not exist, returns custom default
gpa = student.get("gpa", "N/A")
# Output: 'N/A'
```

{{< callout type="info" >}}
**Why No Positional Access?**
**The Need for Speed:**

- Dictionaries are optimized for $\mathbf{O(1)}$ (constant time) lookups using the **key** and hashing.
- Accessing an item by its *positional index* (e.g., the 5th item) would require iterating through the previous items, making the operation $\mathbf{O(n)}$ (linear time) and sacrificing the primary performance benefit of the dictionary.

> **While positional access *could* be technically implemented, Python avoids it to maintain the conceptual integrity of the data type and prevent unnecessary complexity.**

**Conceptual Clarity:**

- Dictionaries are a **mapping** of labels (keys) to values, not a **sequence** of ordered positions. Positional access is the defining feature of a `list`.

**Fragility:**

- If Python allowed access by position, deleting a key would shift the index of all subsequent items, making code that relies on those indices unstable and error-prone.
{{< /callout >}}
---

## 📚 Iteration & Order

### Insertion Order (Python 3.7+)

- The standard Python `dict` officially **preserves the order of insertion**.
- When iterating or printing the dictionary, the key-value pairs will appear in the order they were originally added.

### Retrieving Collections

Use built-in methods to get iterable views of the dictionary's contents:

- **Keys:** `my_dict.keys()` - returns a view of all keys (in insertion order).
- **Values:** `my_dict.values()` - returns a view of all values (in insertion order).
- **Items:** `my_dict.items()` - returns a view of all key-value pairs as tuples `(key, value)`.

```python
data = {"a": 10, "b": 20, "c": 30}

# Iterating over items
for key, value in data.items():
    print(f"{key}: {value}")
# Output:
# a: 10
# b: 20
# c: 30
```

---

## ⚙️ Advanced Ordering (`collections.OrderedDict`)

- While the standard `dict` is ordered, the `collections.OrderedDict` subclass still exists for specific use cases.
- **Key Differences:**
  - **Order-Sensitive Equality:** Two `OrderedDict` instances are only equal if their keys, values, *and* insertion order match.
  - **Dynamic Reordering:** Provides the `.move_to_end(key)` method, which is ideal for implementing LRU (Least Recently Used) Caching logic.

```python
from collections import OrderedDict
d = OrderedDict([('x', 1), ('y', 2)])

# Move 'x' to the end of the order
d.move_to_end('x')
# OrderedDict([('y', 2), ('x', 1)])
```
