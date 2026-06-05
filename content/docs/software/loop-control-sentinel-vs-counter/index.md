---
title: "🔁 Loop Control — Sentinel vs Counter"
date: 2025-11-08
draft: false
---

### 🛑 Sentinel-Controlled Loop

Used when the number of iterations is `unknown`. Loop continues until a special value (sentinel) is encountered.

```python
sentinel = -999
total = 0

num = int(input("Enter a number (-999 to stop): "))
while num != sentinel:
    total += num
    num = int(input("Enter a number (-999 to stop): "))

print("Total sum:", total)
```

> 🔍 Termination is **data-driven**, not count-driven.

---

### 🔢 Counter-Controlled Loop

Used when the number of iterations is `known in advance`. Loop runs a fixed number of times.

```python
total = 0

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    total += num

print("Total sum:", total)
```

> 🔍 Termination is **count-driven**, not data-triggered.

---

## 🧠 Semantic Summary

| Feature               | Sentinel-Controlled        | Counter-Controlled         |
|-----------------------|----------------------------|-----------------------------|
| Termination Trigger   | Special value (e.g., `-999`) | Fixed iteration count (e.g., `5`) |
| Predictability        | ❌ Unknown                 | ✅ Known                    |
| Use Case              | Stream/input processing    | Structured iteration        |
| Risk                  | Sentinel misplacement      | Off-by-one errors           |

> 🧩 Use sentinel loops for **indefinite repetition**, and counter loops for **bounded iteration**. Document clearly to avoid semantic drift.
