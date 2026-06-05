---
title: "🚀 Tail Call Optimisation (TCO)"
date: 2025-11-08
draft: false
---


Tail Call Optimisation is a compiler/runtime technique that transforms certain recursive calls into **constant-space operations**. It allows deep recursion without stack overflow by **reusing the current stack frame** when the recursive call is the final action.

---

## 🧠 Core Concept

### 🧩 Tail Call

A **tail call** occurs when a function calls another (or itself) as its **last operation**, with no further computation afterward.

```scheme
(define (fact-tail x acc)
  (if (= x 0)
      acc
      (fact-tail (- x 1) (* x acc)))  ; ✅ Tail call
)
```

### 🧩 Optimization Mechanism

- Normally, each recursive call adds a new stack frame.
- With TCO, the compiler **reuses** the current frame:
  - Updates parameters
  - Jumps to the start of the function
  - No need to preserve the caller’s frame

---

## ⚙️ Requirements for TCO

| Condition                     | Must Be Met for TCO |
|------------------------------|---------------------|
| Recursive call is last action | ✅ Yes              |
| No computation after call     | ✅ Yes              |
| No need to return to caller   | ✅ Yes              |
| Language/compiler supports TCO | ✅ Yes              |

---

## 🧩 Benefits

- **Space Efficiency**: Reduces space complexity from O(n) to O(1)
- **Performance**: Avoids stack management overhead
- **Safety**: Prevents stack overflow in deep recursion
- **Functional Elegance**: Enables recursion-heavy logic without imperative loops

---

## 🚫 Limitations

- Not supported in all languages (e.g. Python, Java)
- Debugging becomes harder (stack trace is flattened)
- Only applies to **tail calls**, not general recursion
