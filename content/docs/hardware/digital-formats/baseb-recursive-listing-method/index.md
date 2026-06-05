---
title: "📊 Base‑b Recursive Listing Method"
date: 2025-11-08
draft: false
---


## 🧠 Concept

- **Idea:** Because of positional representation, each digit “switches” every power of the base according to how far it is from the smallest unit.
- **Implication:** For base $b$, the $2^\text{nd}$ row (from the top) changes every $b$ entries, the $3^\text{rd}$ row every $b^2$ entries, etc.
- **Result:** To list all combinations up to some digit depth, draw blocks whose sizes are powers of $b$ and recursively split each block into $b$ parts.

---

## 🔢 Example: base $3$, up to the $3^\text{rd}$ digit (MSD → LSD)

- **First row (MSD):**
  - **Block size:** $3^2=9$
  - **Action:** Write each digit $0,1,2$ exactly $9$ times in sequence.

- **Second row (middle digit):**
  - **Inside each MSD block of $9$:** split into $3$ parts of size $3$ and label them $0,1,2$.

- **Third row (LSD):**
  - **Inside each size‑$3$ block:** split into $3$ single entries and label them $0,1,2$.

This produces every ternary triple from $000$ to $222$ in lexicographic order.

---

## 🧭 General method (base‑agnostic)
>
> $b$ for base

- At the **Most Significant Digit** (leftmost digit),
  - List $b^{(\text{positions from the first digit})}$
    - Incrementally from $0$ to $(\text{base}-1)$,
  - Then split each part into $b$ parts recursively until you reach the LSD.

> Recursively here means you **do the same splitting for each sub-part**
