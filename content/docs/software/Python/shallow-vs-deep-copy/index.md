---
title: "🌊 Shallow vs Deep Copy"
date: 2025-11-08
draft: false
---

When working with lists, especially lists containing other lists (or dictionaries/sets), simply copying the list can lead to unexpected side effects due to **shallow copies**.

## 1. 👶 Shallow Copy (The Standard Method)

A shallow copy creates a new object for the outermost container, but it populates it with **references** to the elements found in the original object.

- **Methods:** Slicing (`my_list[:]`), `list()`, `.copy()`

- **Effect:** The new list is independent of the original, **UNLESS** the elements themselves are mutable (e.g., nested lists).

### The Shallow Copy Pitfall

If you modify a nested mutable element in the copy, the change is reflected in the original list because both lists share the reference to that inner object.

```python

import copy

original = [10, [1, 2], 30]

shallow = original[:] # Shallow Copy

# 1. Modify the top-level (immutable int 30) - NO shared effect
shallow[2] = 999

# 2. Modify the NESTED list (mutable object) - SHARED effect
shallow[1].append(5)

print(f"Original: {original}")
print(f"Shallow: {shallow}")

## Output:
# Original: [10, [1, 2, 5], 30] <- Nested list changed!
# Shallow: [10, [1, 2, 5], 999] <- Top level change is unique.
```

## 2. 🌲 Deep Copy (The Safe Method)

A deep copy creates a new container object **recursively** and then inserts copies of the objects found in the original.

- **Method:** `copy.deepcopy()`.

- **Effect:** The new list is **completely independent** of the original, even for nested mutable objects.

### When to use Deep Copy

Use `deepcopy()` whenever you have a nested mutable structure (list of lists, dictionary of lists) and you need to ensure that modifications to the copy **do not** affect the original.

```python

import copy

original = [10, [1, 2], 30] deep = copy.deepcopy(original) # Deep Copy

# Modify the NESTED list (mutable object) - NO shared effect

deep[1].append(5)

print(f"Original: {original}") print(f"Deep: {deep}")

# Output:

# Original: [10, [1, 2], 30] <- Original nested list is safe!

# Deep: [10, [1, 2, 5], 30]
```

## 3. 📝 Summary Table

|Feature|Shallow Copy (`[:]`)|Deep Copy (`deepcopy()`)|
|---|---|---|
|**Outermost Object**|New Object|New Object|
|**Nested Immutable Objects**|Copied (Safe)|Copied (Safe)|
|**Nested Mutable Objects**|**Shared Reference (Dangerous)**|**Copied Recursively (Safe)**|
