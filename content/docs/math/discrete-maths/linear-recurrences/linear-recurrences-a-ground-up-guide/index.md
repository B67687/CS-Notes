---
title: "🔁 Linear Recurrences — A Ground-Up Guide"
date: 2025-11-08
draft: false
---

A **recurrence relation** defines each term of a sequence using previous terms.  
It’s like a recipe: to get the next value, mix earlier ones in a fixed way.

Example:

$$
a_n = a_{n-1} + a_{n-2}
$$

This says: “To get term $a_n$, add the two previous terms.”

---

## 🧠 What Makes It Linear?

A recurrence is **linear** if:

- Each term appears to the **first power**
- Terms are **not multiplied together**
- No functions like $\log(a_{n-1})$ or $\sqrt{a_{n-2}}$

Example of linear:

$$
a_n = 2a_{n-1} - 3a_{n-2}
$$

Nonlinear (not allowed):

$$
a_n = a_{n-1}^2 + 1
$$

---

## 🔒 What Are Constant Coefficients?

The recurrence has **constant coefficients** if the numbers multiplying each term don’t change with $n$.

Example:

$$
a_n = 5a_{n-1} - 6a_{n-2}
$$

Here, 5 and −6 are constants.

---

## ✅ Why This Class Is Special

If a recurrence is:

- Linear
- Homogeneous (no extra terms like $+f(n)$)
- Has constant coefficients

Then we can **always** solve it using a method called the **characteristic equation**.

---

## 📐 The Characteristic Equation Method

1. **Assume** a solution of the form $a_n = r^n$
2. **Substitute** into the recurrence
3. **Simplify** to get a polynomial in $r$
4. **Solve** for the roots $r_1, r_2, \dots$
5. **Build** the general solution using those roots
6. **Apply** initial conditions to find constants

---

### 🧮 Example

Recurrence:

$$
a_n - 3a_{n-1} + 2a_{n-2} = 0
$$

Step 1: Assume $a_n = r^n$

Step 2: Plug in:

$$
r^n - 3r^{n-1} + 2r^{n-2} = 0
$$

Divide by $r^{n-2}$:

$$
r^2 - 3r + 2 = 0
$$

Solve:

$$
r = 1,\quad r = 2
$$

General solution:

$$
a_n = C_1 \cdot 1^n + C_2 \cdot 2^n = C_1 + C_2 \cdot 2^n
$$

Use initial values to solve for $C_1$, $C_2$.

---

## 🔍 Why Use $r^n$?

Because exponential sequences $r^n$ are **eigenfunctions** of the recurrence operator.  
They preserve their form under the recurrence—just like special vectors that don’t rotate under a matrix.

---

## 🧠 Summary

| Concept | Meaning |
|--------|--------|
| Linear | Terms appear to the first power |
| Constant Coefficients | Multipliers don’t change with $n$ |
| Homogeneous | No extra $f(n)$ on the right-hand side |
| Characteristic Equation | Polynomial whose roots build the solution |
| Exponential Basis | $r^n$ sequences span the solution space |
