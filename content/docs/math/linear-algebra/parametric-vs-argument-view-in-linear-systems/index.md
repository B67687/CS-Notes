---
title: "🧭 Parametric vs Argument View in Linear Systems"
date: 2025-11-08
draft: false
---

## 🎯 Goal

Understand how the same solution can be written in two different styles:

- **Row form**: each variable is written separately.
- **Vector form**: the whole solution is written as a single vector made from parts.

---

## 🧮 Example

Given:
$$
x = -4t - 3s \\
y = t \\
z = s
$$

### 🧾 Row Form — *View by Parameter*

Each variable is written on its own line:

- $x = -4t - 3s$
- $y = t$
- $z = s$

🔍 This shows how each variable depends on $t$ and $s$.

---

### 📦 Vector Form — *View by Argument*

$$
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
= t \begin{bmatrix} -4 \\ 1 \\ 0 \end{bmatrix}
+ s \begin{bmatrix} -3 \\ 0 \\ 1 \end{bmatrix}
$$

🔍 This shows how the whole solution is built by combining two fixed vectors using $t$ and $s$.

---

## 🧠 Summary

| Style        | What it shows                          |
|--------------|----------------------------------------|
| Row form     | Each variable depends on parameters    |
| Vector form  | Whole solution built from fixed pieces |

---

## 🪄 Analogy

- **Row form**: Like writing a recipe for each ingredient.
- **Vector form**: Like mixing two colors to get a final shade.
