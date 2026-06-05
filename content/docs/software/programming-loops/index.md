---
title: "🔁 Programming Loops"
date: 2025-11-08
draft: false
---


## 🧠 Core Purpose

Loops allow repeated execution of a block of code based on a condition or iterator. They are essential for automation, iteration, and control flow.

---

## 🔹 General Loop Anatomy

| Phase        | Description                                      | Example (Python)             |
|--------------|--------------------------------------------------|------------------------------|
| Initialize   | Set up loop control variables                    | `i = 0`                      |
| Test         | Evaluate condition to continue looping           | `while i < 5:`               |
| Loop Body    | Execute logic if condition is true               | `print(i)`               |
| Update       | Modify control variables for next iteration      | `i += 1`                 |

> 🧠 This structure applies to most loop types: `while`, `for`, and even low-level assembly loops.

---

## 🔸 Loop Types Across Languages

### 1. `while` Loop

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

- Condition checked **before** each iteration
- May execute **zero** times

### 2. `for` Loop (Python)

```python
for i in range(5):
    print(i)
```

- Uses an **iterator** or range
- Implicit initialization, test, and update

### 3. `for` Loop (C-style)

```c
for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
}
```

- Explicit control over all loop phases

### 4. `do...while` Loop (C/C++)

```c
int i = 0;
do {
    printf("%d\n", i);
    i++;
} while (i < 5);
```

- Condition checked **after** loop body
- Guarantees **at least one** execution

---

## 🔍 Semantic Comparison

| Loop Type     | Pre-Test | Post-Test | Iterator-Based | Guaranteed Execution |
|---------------|----------|-----------|----------------|----------------------|
| `while`       | ✅       | ❌        | ❌             | ❌                   |
| `for` (Python)| ✅       | ❌        | ✅             | ❌                   |
| `for` (C)     | ✅       | ❌        | ❌             | ❌                   |
| `do...while`  | ❌       | ✅        | ❌             | ✅                   |

---

## 🧩 Vault Integration Tip

When documenting loops:

- Always annotate **control flow phases** (init, test, body, update)
- Use **language-specific examples** to highlight semantic differences
- Consider adding **flowcharts** or **truth tables** for loop conditions

> 🔒 Loops are control flow primitives—document them with clarity to avoid semantic drift in algorithm design.
