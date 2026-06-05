---
title: "🧮 Matrices"
date: 2025-11-08
draft: false
---

A **matrix** is a rectangular array of numbers.

Each number is called an **entry** or **element** of the matrix.

### 🔢 Examples
>
> **General** matrix:

$$
\begin{bmatrix}
4 & 3 & 0 & 6 & -1 & 0 \\
0 & 2 & -4 & -7 & 1 & 3 \\
-6 & 1 & 5 & -12 & 0 & 1
\end{bmatrix}
$$

---

## 📏 Matrices

The **size** of a matrix is denoted by $n \times m$, where:

- $n$ = number of **rows**
- $m$ = number of **columns**

| Type            | Shape       | Example                          |
|-----------------|-------------|----------------------------------|
| General Matrix  | $n \times m$ | $\begin{bmatrix} 4 & 3 & 0 & 6 & -1 & 0 \\ 0 & 2 & -4 & -7 & 1 & 3 \\ -6 & 1 & 5 & -12 & 0 & 1 \end{bmatrix}$ |
| Square Matrix   | $n \times n$ | $\begin{bmatrix} 7 & 10 \\ 8 & 0 \end{bmatrix}$ |
| Column Matrix   | $n \times 1$ | $\begin{bmatrix} 4 \\ 2 \\ -1 \\ 9 \\ 5 \end{bmatrix}$ |
| Row Matrix      | $1 \times m$ | $\begin{bmatrix} 1 & -5 \end{bmatrix}$ |
| Scalar Matrix   | $1 \times 1$ | $[-2]$ |

{{< callout type="info" >}}
Often when dealing with `1 x 1` matrices we will **drop the surrounding brackets** and just write -2.

[!Warning] What vector means
Note that sometimes **column matrices** and **row matrices** are called **column vectors** and **row vectors** respectively

We do need to be careful with the word vector however as in later chapters the word vector will be used to denote something much more general than a column or row matrix
{{< /callout >}}
---

## 🟦 Square Matrices & Main Diagonal

The **main diagonal** of a square matrix consists of entries:
$$
a_{11},\ a_{22},\ \dots,\ a_{nn}
$$
These run from the top-left to bottom-right of the matrix:
$$
\begin{bmatrix}
\color{blue}{a_{11}} & a_{12} & \cdots & a_{1n} \\
a_{21} & \color{blue}{a_{22}} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & \color{blue}{a_{nn}}
\end{bmatrix}
$$

---

## 🧾 Entry Notation

To refer to a specific entry in a matrix $A$, use:
> $a_{ij}$ or $(A)_{ij}$
>
> - $i$ = row index
> - $j$ = column index

{{< callout type="default" >}}
**General Use Case**
**Upper case letters** are generally used to refer to **matrices**
(e.g., $A$, $B$, $C$)

**Lower case letters** generally are used to refer to **numbers**/**entries**
(e.g., $a_{ij}$, $b_{ij}$)
{{< /callout >}}
---

## 🧰 General Matrix Representation

A general $n \times m$ matrix $A$ can be written as:

### 🔣 Subscript Notation

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1m} \\
a_{21} & a_{22} & \cdots & a_{2m} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nm}
\end{bmatrix}
$$

### ...with size denoted

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1m} \\
a_{21} & a_{22} & \cdots & a_{2m} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nm}
\end{bmatrix}_{n \times m}
$$

{{< callout type="info" >}}
**Note**
We don’t generally subscript the size of the matrix as we did in the second case, but on occasion it may be useful to make the size clear.
{{< /callout >}}
---

### 🧭 Vector Notation

- Column matrix (vector): $\mathbf{a}$ or $\vec{a}$
$$
\mathbf{\vec{a}} = \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix}

$$
- Row matrix (vector): $\mathbf{b}$ or $\vec{b}$
$$
\mathbf{\vec{b}} = [b_1, b_2, \dots, b_m]
$$

{{< callout type="default" >}}
In written documents, vectors are often **bolded**

On chalkboards, **arrows** are used due to visibility constraints.

The convention in this notes will be **bolded arrows** for **maximum readability**
> Following both conventions at the same time for **less ambiguity**
{{< /callout >}}
---

## 🧭 Summary

| Convention        | Meaning / Use Case                          |
|------------------|---------------------------------------------|
| $n \times m$      | Matrix size: rows × columns                 |
| $a_{ij}$          | Entry in row $i$, column $j$ of matrix $A$ |
| $\mathbf{\vec{a}}$      | Column matrix (vector)                      |
| $\mathbf{\vec{b}}$      | Row matrix (vector)                         |
| Square matrix     | $n = m$                                     |
| Scalar matrix     | $1 \times 1$                                |
