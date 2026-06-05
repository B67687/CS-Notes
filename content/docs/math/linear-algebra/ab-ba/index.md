---
title: "🔄 (AB)ᵀ = (Bᵀ)(Aᵀ)"
date: 2025-11-08
draft: false
---

Matrix multiplication has been standardized so that:

- The **left matrix** is interpreted as a collection of **row vectors**
- The **right matrix** is interpreted as a collection of **column vectors**
- The dot product is taken between each row of the left matrix and each column of the right matrix

Let the left matrix be $A$, and the right matrix be $B$.

---

## 🧩 Structure of AB

- Each **row of $AB$** is formed from the rows of $A$
- Each **column of $AB$** is formed from the columns of $B$

This reflects how matrix multiplication contracts across shared dimensions—row of $A$ meets column of $B$.

---

## 🔁 Transposing AB

When we transpose $AB$, we swap its rows and columns:

- Originally:
  → **row from $A$**, **column from $B$**

- After transpose:
  → **row from $B$**, **column from $A$**

{{< callout type="default" >}}
**Axis Role Flip**
Transposing $AB$ reverses the roles of $A$ and $B$ in how they contribute to the output matrix.
{{< /callout >}}
---

## 🔄 What Happens to A and B

To reconstruct this transposed structure:

- $A$ and $B$ must **swap places** to match the new row-column pairing
- Each must also be **transposed individually** to preserve the original elements while flipping their orientation

This results in:

- Left matrix: $B^\top$ (formerly the right matrix)
- Right matrix: $A^\top$ (formerly the left matrix)

Their product gives the transposed form:

$$
(AB)^\top = B^\top A^\top
$$

{{< callout type="info" >}}
**Semantic Reversal**
Transpose flips both the **order** and the **orientation** of the original matrices to preserve dot product semantics.
{{< /callout >}}
---

## ✅ Final Statement

$$
\boxed{
 \phantom{\big(}
 (AB)^\top = B^\top A^\top
 \phantom{\big)}
}
$$
