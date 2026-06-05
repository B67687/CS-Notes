---
title: "💻 Procedures vs Functions"
date: 2025-11-08
draft: false
---

Understanding the distinction between procedures and functions is foundational in programming, logic design, and algorithmic reasoning.

---

## 🧩 Core Distinctions

| Feature                  | Procedure                              | Function                                |
|--------------------------|----------------------------------------|-----------------------------------------|
| **Return Value**         | No return value (void)                 | Returns a value                         |
| **Purpose**              | Executes a sequence of actions         | Computes and returns a result           |
| **Side Effects**         | Often modifies state or performs I/O   | Ideally pure (no side effects)          |
| **Composability**        | Harder to compose                      | Easily composable in expressions        |
| **Auditability**         | Requires tracing external effects      | Return value can be logged/tested       |
| **Mathematical Analogy**| Imperative statement                   | Mathematical function (f(x) = y)        |

---

## 🧠 Semantic Resonance Map

```mermaid
    graph TD
        A[Procedure] -->|Action-oriented| B[State Mutation]
        A -->|Often void| C[No Return]
        D[Function] -->|Value-oriented| E[Return Value]
        D -->|Composable| F[Expression Embedding]
        B --> G[Side Effects]
        E --> H[Pure Logic]
```

```python
    # Procedure
    def log_message(msg):
        print(f"Log: {msg}")  # Side effect: console output

    # Function
    def square(x):
        return x * x  # Pure computation
```

---

## 🧭 When to Use

- ✅ Use **procedures** for tasks like logging, file I/O, or system calls.
- ✅ Use **functions** for deterministic computations, transformations, and logic encapsulation.
