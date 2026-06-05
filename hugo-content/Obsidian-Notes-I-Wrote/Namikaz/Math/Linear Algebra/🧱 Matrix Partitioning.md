---
title: "🧱 Matrix Partitioning"
date: 2025-11-08
draft: false
---

The concept of a **block matrix** (or **partitioned matrix**) is a way to interpret a large matrix by dividing it into smaller matrices, called **blocks** or **submatrices**.

It does **not** change the value of the original coefficients, but provides a new **perspective** that is useful for calculation and representation.

> [!tip] **The Role of Coefficients**
> The individual coefficients (numbers) within the blocks still **retain their original meaning**, but they are now grouped into structured units that are **treated as single elements during block-level operations**

---

## 🔑 Key Purposes

**Simplification of Operations:**
Complex calculations like multiplication, inversion, and finding the determinant can be performed by treating the blocks as if they were scalars, which is often computationally faster and conceptually cleaner.

$$
\begin{aligned}
  \begin{bmatrix} \mathbf{A} & \mathbf{B} \\ \mathbf{C} & \mathbf{D} \end{bmatrix} \begin{bmatrix} \mathbf{E} \\ \mathbf{F} \end{bmatrix} = \begin{bmatrix} \mathbf{AE} + \mathbf{BF} \\ \mathbf{CE} + \mathbf{DF} \end{bmatrix}
  \end{aligned}
$$
​
**Highlighting Structure:**
Partitioning helps to expose the internal structure of the matrix, especially when dealing with:

- **Sparse Matrices:**

> Matrices with large sections of zeros, which can be grouped into 0 blocks.

- **Block Diagonal/Triangular Matrices:**

> Matrices where structure simplifies algorithms
>
> - (e.g. Inverting a block diagonal matrix is just inverting the diagonal blocks).

---

## 🧱 Partitioning Forms

### General

$$
A =
\left[
\begin{array}{c|cc}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
\hline
a_{31} & a_{32} & a_{33} \\
a_{41} & a_{42} & a_{43} \\
a_{51} & a_{52} & a_{53}
\end{array}
\right]
=
\begin{bmatrix}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{bmatrix}
$$

### By Column

$$
A =
\left[
\begin{array}{c|c|c}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} \\
a_{41} & a_{42} & a_{43} \\
a_{51} & a_{52} & a_{53}
\end{array}
\right]
=
[\mathbf{c}_1 \mid \mathbf{c}_2 \mid \mathbf{c}_3]
$$

### By Row

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
\hline a_{21} & a_{22} & a_{23} \\
\hline a_{31} & a_{32} & a_{33} \\
\hline a_{41} & a_{42} & a_{43} \\
\hline a_{51} & a_{52} & a_{53}
\end{bmatrix} =
\begin{bmatrix}
\mathbf{r}_1 \\
\hline \mathbf{r}_2 \\
\hline \mathbf{r}_3 \\
\hline \mathbf{r}_4 \\
\hline \mathbf{r}_5
\end{bmatrix}
$$

## 🎯 Meaning in a System of Equations (Ax=b)

Partitioning relates directly to the variables (x) and the equations (rows of A):

- **Column Partitioning:** Groups the **variables**.

- **Row Partitioning:** Groups the **equations** (or constraints).
