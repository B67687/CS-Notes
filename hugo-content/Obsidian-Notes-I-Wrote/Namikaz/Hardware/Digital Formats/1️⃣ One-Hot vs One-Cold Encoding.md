---
title: "1️⃣ One-Hot vs One-Cold Encoding"
date: 2025-11-08
draft: false
---

**One-hot** and **one-cold** are binary encoding schemes used to represent **exclusive activation state** in digital logic and machine learning

## 🔥 One-Hot Encoding
>
> A binary vector where exactly one bit is $1$ and all others are $0$.

- Used in decoders, finite state machines, and categorical encoding
- Ensures mutual exclusivity
- Example: `[0, 0, 1, 0, 0]`

## 🧊 One-Cold Encoding
>
> A binary vector where exactly one bit is $0$ and all others are $1$.

- Rarely used—sometimes in error detection or contrastive encoding
- Inverse of one-hot
- Example: `[1, 1, 0, 1, 1]`

> [!example] Notes
> One-hot is the **dominant convention** in logic design due to clarity and exclusivity
>
> One-cold is **valid but rare**, and typically used in niche or contrastive contexts
>
> Both are **binary activation patterns** with exactly one bit flipped from the rest
