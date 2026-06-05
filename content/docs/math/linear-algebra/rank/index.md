---
title: "📐 Rank"
date: 2025-11-08
draft: false
---

Rank tells us **how much independent information** a matrix contains.

- In systems of equations: rank tells us how many equations are truly useful (not duplicates).
- In geometry: rank tells us how many directions the matrix spans.
- In data: rank tells us how much redundancy exists.

If a matrix has full rank, it means:
> Every row or column contributes something new. No duplicates. No wasted space.

---

## 🔍 What Is Rank?

The **rank** of a matrix is:

> The number of linearly independent rows or columns.

This is always equal to the number of **pivot positions** after row reduction.

$$
\text{rank}(A) = \text{number of pivot rows}
$$

---

## 🧮 How Do You Find Rank?

### Step-by-step:

1. Start with matrix $A$
2. Apply **Gaussian elimination** to reduce it to row echelon form
3. Count the number of **pivot rows** (rows with leading non-zero entries)

That count is the **rank**.

### Example:

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
1 & 1 & 1
\end{bmatrix}
\quad \Rightarrow \quad
\text{rank}(A) = 2
$$

(Row 2 is a multiple of Row 1 → not independent)

---

## 📐 Role of Rank in Linear Algebra

| Context | What Rank Tells You |
|--------|----------------------|
| Solving $Ax = b$ | Whether a solution exists (via Rouché–Capelli) |
| Geometry | How many dimensions the matrix spans |
| Data compression | How much redundancy is present |
| Matrix invertibility | Whether a square matrix is invertible (full rank) |
| Column space | Dimension of the space spanned by columns |
| Row space | Dimension of the space spanned by rows |

---

## 🔭 Geometric Interpretation

- Rank 1 → all columns lie on a line
- Rank 2 → columns span a plane
- Rank 3 → columns span full 3D space

Each pivot adds a new direction.  
No pivot → no new direction → redundancy.

---

## 💡 Callouts

{{< callout type="info" >}}
**Rank = Number of Pivots**
After row reduction, each pivot row counts toward the rank.

[!tip] Rank Is the Bridge  
Rank connects equations, geometry, and solvability.

[!example] Rouché–Capelli Theorem  
A system $Ax = b$ has a solution **iff** $\text{rank}(A) = \text{rank}([A \mid b])$
{{< /callout >}}