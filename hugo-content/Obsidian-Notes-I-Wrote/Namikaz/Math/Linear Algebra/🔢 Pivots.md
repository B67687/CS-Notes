---
title: "🔢 Pivots"
date: 2025-11-08
draft: false
---

A **pivot** is the leading non-zero entry in a row after applying Gaussian elimination. It marks a position where a variable is constrained or a row is linearly independent.

- Each pivot corresponds to a **linearly independent row or column**
- Pivot positions determine the **rank** of a matrix

---

## 📐 Structural Limits

Let $A \in \mathbb{R}^{m \times n}$. Then:

- **Max number of pivots** = $\min(m, n)$
- You can’t have more than one pivot per row or column
- If $m > n$, at least $m - n$ rows will be **pivotless** (i.e. dependent)

---

## 🧮 Pivot ↔ Rank ↔ Independence

| Structure | Pivot Present | Interpretation |
|-----------|----------------|----------------|
| Column    | ✅ Yes         | Linearly independent |
| Column    | ❌ No          | Linearly dependent |
| Row       | ✅ Yes         | Adds a new constraint |
| Row       | ❌ No          | Redundant (dependent) |

---

## 📊 Example: Row Reduction

Let:

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
0 & 1 & 4 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix}
$$

- Pivot positions: (1,1), (2,2)
- Rank = 2
- Rows 3 and 4 are dependent (no new constraints)

---

## 📐 Deriving the Rouché–Capelli Theorem from Pivot Logic

Let $Ax = b$ be a system of $m$ equations in $n$ unknowns.  
Form the **augmented matrix** $[A \mid b]$.

### Step-by-step:

1. Row reduce both $A$ and $[A \mid b]$
2. Count pivot rows in each
3. Compare:

$$
Ax = b \text{ has a solution} \iff \operatorname{rank}(A) = \operatorname{rank}([A \mid b])
$$

### Why?

- Each pivot row in $A$ corresponds to an independent constraint
- If $b$ introduces a new pivot in $[A \mid b]$, it means $b$ is **not** in the column space of $A$
- That makes the system **inconsistent**

> ✅ If ranks match → $b$ lies in the column space → solution exists  
> ❌ If ranks differ → $b$ is outside the column space → no solution

---

## 🧭 Geometric Interpretation

> Pivot rows define the **dimension of the row space**  
> Pivot columns define the **dimension of the column space**

Imagine each pivot as a new direction in space. Non-pivot rows/columns lie **within the span** of earlier ones—they don’t expand the space.

---

## 💡 Callouts

> [!info] Pivotless Rows  
> Any row without a pivot is a **linear combination** of earlier pivot rows. It contributes no new constraint.

> [!tip] Rank via Pivot Count  
> The number of pivot positions equals the **rank** of the matrix.

> [!example] Overdetermined System  
> A $4 \times 3$ matrix can have at most 3 pivots → at least one row is dependent → not all $b \in \mathbb{R}^4$ are reachable.

> [!quote] Rouché–Capelli Theorem  
> A system $Ax = b$ is solvable **if and only if** $\operatorname{rank}(A) = \operatorname{rank}([A \mid b])$