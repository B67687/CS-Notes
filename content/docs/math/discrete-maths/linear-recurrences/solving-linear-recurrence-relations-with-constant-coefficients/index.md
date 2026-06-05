---
title: "🔁 Solving Linear Recurrence Relations with Constant Coefficients"
date: 2025-11-08
draft: false
---

## 🧩 Problem Statement

Solve the recurrence:

$$
a_n - 8a_{n-1} + 16a_{n-2} = 0
\quad \text{with} \quad a_0 = 4,\quad a_1 = 16
$$

---
#### **Step 1: Form the Characteristic Equation**

Assume a solution of the form $a_n = r^n$. Substituting into the recurrence:

$$
r^n - 8r^{n-1} + 16r^{n-2} = 0
\Rightarrow r^{n-2}(r^2 - 8r + 16) = 0
$$

Characteristic equation:

$$
r^2 - 8r + 16 = 0
\Rightarrow (r - 4)^2 = 0
\Rightarrow r = 4 \quad \text{(double root)}
$$

---

#### **Step 2: General Solution Form**

For a repeated root $r$ of multiplicity 2, the general solution is:

$$
a_n = (C_1 + C_2n) \cdot r^n
\Rightarrow a_n = (C_1 + C_2n) \cdot 4^n
$$

This form ensures linear independence of the two solutions $4^n$ and $n \cdot 4^n$.

---

#### **Step 3: Apply Initial Conditions**

- $a_0 = (C_1 + C_2 \cdot 0) \cdot 4^0 = C_1 = 4$
- $a_1 = (C_1 + C_2 \cdot 1) \cdot 4^1 = (4 + C_2) \cdot 4 = 16 \Rightarrow C_2 = 0$

---

### ✅ Final Closed-Form Solution

$$
\boxed{a_n = 4 \cdot 4^n}
$$

---

## 🔍 Why Assume $a_n = r^n$?

- The recurrence is a **linear operator** with constant coefficients.
- Exponential sequences $r^n$ are **eigenfunctions** of this operator.
- Plugging $r^n$ into the recurrence yields a **characteristic polynomial**.
- Roots of this polynomial correspond to **basis solutions** of the recurrence.

---

## 🧠 Why the General Solution Includes $n \cdot r^n$

- Repeated roots require **generalized eigenfunctions** for linear independence.
- For multiplicity $m$, the solution includes terms like $n^k \cdot r^n$ for $k = 0, 1, \dots, m-1$.
- This mirrors the Jordan block structure in linear algebra and differential equations.

---

## 📐 Summary Table

| Concept | Explanation |
|--------|-------------|
| Characteristic Equation | Converts recurrence into algebraic form |
| Exponential Ansatz $r^n$ | Natural eigenfunctions of constant-coefficient operators |
| Repeated Roots | Require polynomial correction for independence |
| General Solution | $a_n = \sum P_i(n) \cdot r_i^n$, where $P_i(n)$ is a polynomial |

---

## 🧮 Analogy: Linear Algebra Perspective

Let $L$ be the recurrence operator:

$$
L(a_n) = a_n - c_1 a_{n-1} - \dots - c_k a_{n-k}
$$

We solve $L(a_n) = 0$. The null space of $L$ is spanned by exponential sequences $r^n$, extended by $n^k r^n$ for repeated roots.
