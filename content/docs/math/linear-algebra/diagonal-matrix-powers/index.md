---
title: "📏  Diagonal Matrix Powers"
date: 2025-11-08
draft: false
---

If $D$ is a diagonal matrix, then raising it to a power $k$ is equivalent to raising each diagonal entry to the same power:

$$
D^k = \text{diag}(d_1^k, d_2^k, \dots, d_n^k)
$$

This works because diagonal matrix multiplication is element-wise on the diagonal.

---

## 🧩 Example

Let:

$$
D = \begin{bmatrix}
2 & 0 & 0 \\
0 & 3 & 0 \\
0 & 0 & 5
\end{bmatrix}
\Rightarrow
D^2 = \begin{bmatrix}
4 & 0 & 0 \\
0 & 9 & 0 \\
0 & 0 & 25
\end{bmatrix}
$$

Each diagonal entry is squared independently.

---

## 🔍 Why This Matters

- Diagonal matrices are **trivially exponentiated**
- Used in **diagonalization**:
  $$
  A = P D P^{-1} \Rightarrow A^k = P D^k P^{-1}
  $$
- Powers of matrices become easy once diagonalized
- Matrix exponentials simplify:
  $$
  e^{D t} = \text{diag}(e^{d_1 t}, e^{d_2 t}, \dots)
  $$

---

## ✅ Validator Summary

| Operation | Result |
|----------|--------|
| $D^k$ | Raise each diagonal entry to power $k$ |
| $A^k$ via diagonalization | $P D^k P^{-1}$ |
| Matrix exponential $e^{D t}$ | Apply exponential to each diagonal entry |

---

## 🧠 Related Concepts

- Diagonalization
- Eigenvalue powers
- Matrix exponentials
- Spectral decomposition
