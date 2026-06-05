---
title: "📦 Mutable Default Arguments"
date: 2025-11-08
draft: false
---

This is one of the most unexpected "gotchas" in Python, specifically related to the interaction between mutable objects and function definitions.

## Default Arguments are Evaluated Once

In Python, the default values for function arguments are calculated and stored **only once**—when the function is defined (when the Python interpreter first reads the file).

If you use a **mutable** object (like a `list` or `dict`) as a default value, every time the function is called without that argument, it uses the _exact same_ list object stored in the function's definition.

### The Pitfall Example

The `results` list is created once when `add_item` is defined.

```python
def add_item(item, results=[]): # DANGEROUS DEFAULT
 results.append(item)
 return results

# First call: uses the original, empty list object
list_1 = add_item("apple") print(f"List 1: {list_1}") # List 1: ['apple']

# Second call: uses the SAME list object, which now contains 'apple'
list_2 = add_item("banana") print(f"List 2: {list_2}") # List 2: ['apple', 'banana'] - NOT a new list!

# This side effect is almost never desired.
```

## 2. ✅ The Solution: Use `None` and an Explicit Check

The standard and safe practice is to use `None` as the default value for mutable arguments, and then check if the argument is `None` inside the function body.

- `None` is immutable, so it is safe to use as a default.

- Inside the function, if the argument is `None`, a **new mutable object** (a fresh `list` or `dict`) is created every time the function is called.

### The Correct Implementation

```python
def add_item_safe(item, results=None): # SAFE DEFAULT
 if results is None: # Check if a new list needs to be created
  results = []

 results.append(item)
 return results

# First call: creates a NEW list []
list_1_safe = add_item_safe("apple")
print(f"List 1 Safe: {list_1_safe}") # List 1 Safe: ['apple']

# Second call: creates another NEW list []
list_2_safe = add_item_safe("banana")
print(f"List 2 Safe: {list_2_safe}") # List 2 Safe: ['banana']
```

## 3. 📝 Summary

|Type of Default Argument|Behavior|Safe?|
|---|---|---|
|**Immutable** (`int`, `str`, `tuple`)|Evaluated once,<br>but creates a new variable pointing to a fixed value.|**YES**|
|**Mutable** (`list`, `dict`, `set`)|Evaluated once,<br>and _all_ calls share the _same_ underlying object.|**NO**|
