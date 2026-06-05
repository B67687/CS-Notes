---
title: "🔁 Recursive Functions"
date: 2025-11-08
draft: false
---

Recursion is a foundational technique in algorithm design, enabling elegant solutions to problems that exhibit self-similarity. A recursive function solves a problem by **reducing it to smaller instances of itself**, often leading to concise, expressive, and mathematically aligned code.

---

## 🧠 Core Anatomy of Recursion

### 🧩 Base Case

- The **termination condition** that stops recursion.
- Must be simple and directly solvable.
- Prevents infinite loops and stack overflows.

### 🧩 Recursive Case

- The part where the function **calls itself** with a smaller or simpler input.
- Should always move toward the base case.

### 🧩 Call Stack

- Each recursive call is pushed onto the stack.
- When the base case is hit, calls begin to **unwind**, returning results back up the chain.

```pseudo
function factorial(n):
    if n == 0:
        return 1          # Base case
    else:
        return n * factorial(n - 1)  # Recursive case
```

---

## 🔄 Types of Recursion

| Type              | Description                                      | Example Use Case               |
|-------------------|--------------------------------------------------|--------------------------------|
| Direct            | Function calls itself                            | Factorial, Fibonacci           |
| Indirect          | Function A calls B, which calls A                | Mutual recursion               |
| Tail Recursion    | Recursive call is the last operation             | Optimizable to iteration       |
| Tree Recursion    | Multiple recursive calls per invocation          | Tree traversal, divide & conquer |
| Structural        | Recursion follows data structure shape           | Linked lists, trees            |

---

## ⚙️ Performance Considerations

| Factor            | Recursive Impact                                 | Notes                          |
|-------------------|--------------------------------------------------|--------------------------------|
| Time Complexity   | Often exponential without memoization            | Fibonacci naive: O(2ⁿ)         |
| Space Complexity  | Stack grows with depth                           | O(n) for linear recursion      |
| Optimization      | Tail recursion can be flattened to iteration     | Language-dependent             |
| Memoization       | Caches results to avoid redundant calls          | Key in dynamic programming     |

---

## 🧩 Recursive Thinking Patterns

- **Divide and Conquer**: Break problem into subproblems, solve recursively, combine.
- **Backtracking**: Explore paths recursively, undo when invalid.
- **Structural Mapping**: Traverse or transform data structures recursively.
