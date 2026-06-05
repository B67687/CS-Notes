---
title: "🔧 Tail Call Elimination (TCE)"
date: 2025-11-08
draft: false
---

Tail Call Elimination is a **programmer-level technique** that simulates [[🚀 Tail Call Optimisation (TCO)| Tail Call Optimisation]] by **refactoring recursion into iteration**. It enables deep recursion in languages that don’t support TCO (e.g. Python, Java) by avoiding stack growth altogether.

---

## 🧠 Core Concept

### 🧩 Tail-Recursive Function

A function is tail-recursive if the recursive call is the **last operation**.
> `acc` stands for `accumulator`

```python
def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n - 1, acc * n)  # ✅ Tail call
```

### 🧩 Elimination Strategy

Replace recursion with a loop that **mutates parameters**:

```python
def factorial(n):
    acc = 1
    while n > 0:
        acc *= n
        n -= 1
    return acc
```

- No recursion
- No stack growth
- Same logic, constant space

---

## 🧩 Trampolining (Advanced TCE)

Trampolining transforms recursion into iteration **without discarding the recursive structure**. Instead of executing recursive calls directly, each step returns a **call object**—a `lambda` or thunk—that represents the next step. These thunks are then executed iteratively by a `bounce()` function.

This approach preserves the **recursive shape** of the function while avoiding stack growth. The recursion is no longer driven by the call stack—it’s driven by a loop that unwraps deferred calls one by one.

---

Use a loop to execute **returned lambdas** instead of direct recursion:

```python
def bounce(f):
    while callable(f):
        f = f()
    return f

def factorial(n, acc=1):
    if n == 0:
        return acc
    return lambda: factorial(n - 1, acc * n)

result = bounce(lambda: factorial(1000))
```

- Each step returns a function
- `bounce()` executes them iteratively
- Simulates recursion without stack frames

---

### 🔍 Key Insight

> By returning `lambda: factorial(n - 1, acc * n)`, we’re not making a recursive call—we’re **deferring** it.
>
> The `lambda` acts as a **call object**, holding the next step without executing it.
>
> The `bounce()` function then **iteratively executes** these lambdas, simulating recursion in constant space.

This means:

- The function **looks recursive** and retains its self-referential elegance.
- But the actual execution is **iterative**, controlled by the trampoline.
- The stack doesn’t grow—each step is a bounce, not a dive.

## ⚙️ Benefits

- Works in any language
- Full control over memory and flow
- Enables recursion-like logic in imperative environments
- Improves auditability and debugging

---

## 🚫 Tradeoffs

- Requires manual refactoring
- Less elegant than native recursion
- May obscure original recursive intent
