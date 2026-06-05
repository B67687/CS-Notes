---
title: "🔪 Sequence Slicing"
date: 2025-11-08
draft: false
---

Slicing extracts a **subset of elements** from sequences (like Lists, Strings, Tuples) using a compact, expressive syntax:

$$
\text{seq} \space
[
    \underbrace{\text{start} \vphantom{\text{stop}}}_{\text{inclusive}}
    :
    \underbrace{\text{stop}}_{\text{exclusive}}
    :
    \underbrace{\text{step}}_{\text{jump size}}
]
$$

- **start (inclusive):** Where slicing begins

> Default: `0`

- **stop (exclusive):** Where slicing ends (not included)

> Default: end of sequence

- **step (interval):** Jump size between elements.

> Default: `1`

Slicing defaults to **left-to-right** traversal with `step = +1`

---

## 🔄 The Direction Rule (Crucial)

The direction of the slice is determined **entirely** by the sign of the `step` value.

1. **Positive Step (`step > 0`):** Slicing moves **Left-to-Right** (increasing index).

    - Requires: `start < stop` (or defaults must meet this).

2. **Negative Step (`step < 0`):** Slicing moves **Right-to-Left** (decreasing index).

    - Requires: `start > stop` (or defaults must meet this).

If the starting point is already "past" the stopping point for the given direction, the result is an **empty list** (`[]`).

## 📐 Positive Step

```python
data = [10, 20, 30, 40, 50]
```

| Slice | Meaning | Result |
| :--- | :--- | :--- |
| `data[1:4]` | Index 1 to before 4 | `[20, 30, 40]` |
| `data[:3]` | Start to before 3 | `[10, 20, 30]` |
| `data[2:]` | From index 2 to end | `[30, 40, 50]` |
| `data[::2]` | Every 2nd item | `[10, 30, 50]` |

---

## ⏪ Negative Indices

> Negative indices count from the end:
>
> - `-1` → last element
> - `-2` → second-to-last

```python
data = [10, 20, 30, 40, 50]
```

| Slice | Meaning | Result |
| :--- | :--- | :--- |
| `data[-3:]` | From 3rd-to-last to end | `[30, 40, 50]` |
| `data[:-1]` | Start to before last | `[10, 20, 30, 40]` |
| `data[-4:-2]` | From 4th-to-last to before 2nd-to-last | `[20, 30]` |

---

## 🔄 Negative Step — Backward Slicing

> A **negative step** goes from right-to-left on the list
>
> `step > 0` → L→R
>
> - **start < stop** for non-empty list
>
> `step < 0` → R→L
>
> - **stop < start** for non-empty list

```python
data = [10, 20, 30, 40, 50]
```

| Slice | Step | Result | Why |
| :--- | :--- | :--- | :--- |
| `data[::-1]` | -1 | `[50, 40, 30, 20, 10]` | Full reverse |
| `data[4:1:-1]` | -1 | `[50, 40, 30, 20]` | Valid R→L |
| `data[1:4:-1]` | -1 | `[]` | Invalid R→L (1 < 4) |
| `data[:: -3]` | -3 | `[50, 20]` | Every 3rd in reverse |

---

## 🔢 Negative Indices + Negative Step

```python
data = [10, 20, 30, 40, 50]
```

| Slice | Meaning | Result |
| :--- | :--- | :--- |
| `data[-1:-4:-1]` | From last to before 4th-to-last | `[50, 40, 30]` |
| `data[-4:-1:1]` | From 2nd to before last | `[20, 30, 40]` |
| `data[-1:0:-1]` | Reverse from last to before first | `[50, 40, 30, 20, 10]` |

---

## 🛠️ Slicing for Copying, Modification, and Deletion

### 🔁 Shallow Copy

```python
new_list = old_list[:]
```

> Creates a new list with the same contents.

### ✏️ In-Place Replacement

```python
nums = [1, 2, 3, 4]
nums[1:3] = [200, 300, 400]
# → [1, 200, 300, 400, 4]
```

> Slice assignment replaces the section. Lengths can differ.

### ❌ Deletion

```python
del nums[1:3]
# Deletes items at index 1 and 2
```

> Only works on mutable sequences (`list`, `dict`, `set`).
