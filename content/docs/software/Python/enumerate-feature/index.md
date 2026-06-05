---
title: "🏷️ Enumerate Feature"
date: 2025-11-08
draft: false
---


The `enumerate()` function is the Pythonic way to iterate over a sequence while simultaneously gaining access to both the **index** and the **value** of the element.

## ⚙️ Syntax and Structure

`enumerate()` takes an iterable sequence and returns a sequence of 2-item **tuples**: `(index, value)`.

$$
\text{for index, value in enumerate} (\text{sequence}, \text{start}):
$$

|Parameter|Default|Purpose|
|---|---|---|
|**sequence**|N/A (Required)|The iterable you wish to loop through.|
|**start_index**|0|The number from which the index count should begin.|

### Basic Usage (Default Start)

```python
data = ["A", "B", "C"]

for i, item in enumerate(data): # i = index, item = value
 print(f"Item {i}: {item}")

## Output:
# Item 0: A
# Item 1: B
# Item 2: C
```

## 🚀 Customizing the Start Index

The `start` parameter is useful when you want the index to represent something other than the technical list index, such as a ranking or a line number.

```python
scores = [95, 88, 92]

# Start the count from 1 instead of 0
for rank, score in enumerate(scores, start=1): print(f"Rank {rank}: {score}")

## Output:
# Rank 1: 95
# Rank 2: 88
# Rank 3: 92
```

## 📝 When to Choose `enumerate()` vs. `range(len())`

|Feature|`enumerate(data)`|`range(len(data))`|
|---|---|---|
|**Code Readability**|**High:** Explicitly gets index and value.|**Lower:** Requires two steps: get index, then look up value (`data[i]`).|
|**Access to Value**|Directly provided as the second loop variable.|Must be looked up via indexing (`data[i]`).|
|**Modification Capability**|**CANNOT** modify the element in place (similar to standard `for...in` loop).|**CAN** modify the element in place (`data[i] = new_val`).|

### Rule of Thumb

1. **Read Only:** If you only need the index for display or reference, use `enumerate()`.

2. **Modify:** If you need to change the value of the element in the original list, you **must** use `range(len())`.
