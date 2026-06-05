---
title: "🧨 Caching  — Dynamic Programming"
date: 2025-11-08
draft: false
---

Dynamic programming (DP) is an unnecessarily fancy name for **caching results**—either on-demand or proactively,  to avoids redundant computation.

---

## 🫙 Top-Down Caching —— **Memoization**
- **Execution**: Recursive
- **Trigger**: Compute subproblem only when needed
- **Storage**: Cache results as they’re encountered
- **Symbolic trace**: Annotated recursive tree
- **Example**:
  ```python
  memo = {}
  def fib(n):
      if n in memo: return memo[n]
      if n <= 1: return n
      memo[n] = fib(n-1) + fib(n-2)
      return memo[n]
  ```

---

## 🫙 Bottom-Up Caching —— **Tabulation**
- **Execution**: Iterative
- **Trigger**: Precompute all subproblems in order
- **Storage**: Fill table from base cases upward
- **Symbolic trace**: Linear table evolution
- **Example**:
  ```python
  def fib(n):
      dp = [0, 1] + [0]*(n-1)
      for i in range(2, n+1):
          dp[i] = dp[i-1] + dp[i-2]
      return dp[n]
  ```

---

## 🏷️ Etymology

| Term         | Origin Meaning                     | Symbolic Behavior                     |
|--------------|-------------------------------------|----------------------------------------|
| **Memoization** | “Memo” = note-to-self               | Tag answers during recursive descent   |
| **Tabulation**  | “Table” = structured ledger         | Build answers from base cases upward   |

---

## 🧠 Why “Dynamic Programming”?

- Coined by **Richard Bellman** in the 1950s.
- “Programming” meant **planning**, not coding.
- “Dynamic” referred to **multi-stage decisions evolving over time**.
- The term was partly chosen to sound important and non-threatening to funders.

| Term                  | Original Meaning                     | Modern Interpretation              |
|-----------------------|---------------------------------------|------------------------------------|
| **Dynamic**           | Time-evolving decisions               | Recursive or iterative dependency  |
| **Programming**       | Planning or optimization              | Algorithm design                   |
