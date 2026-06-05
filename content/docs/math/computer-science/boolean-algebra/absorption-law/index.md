---
title: "🌪️ Absorption Law"
date: 2025-11-26
draft: false
---

The Absorption Law describes how a set interacting with a union or intersection of itself with another set simplifies back to the original set. 

This is often intuitively understood by considering **strictness** (Intersection, $\cap$) and **leniency** (Union, $\cup$).

---

## 🧭 Foundational Concepts

- Unions ($\cup$, Inclusive OR) are minimally validated by the **less strict** (more lenient) condition.
- Intersections ($\cap$, AND) are minimally validated by the **more strict** condition.

When using these binary operators, we compare two items, for example:
- $F \cap G$
- $F \cup G$

---

## 🥇 The Intersection Form (The Stricter Condition Prevails)

Consider the expression:


$$
A \cap (A \cup B)
$$


- $A$ is **more strict** than $(A \cup B)$, since for $(A \cup B)$, satisfying $A$ **or** $B$ makes it true.
- Since this expression hinges around $\cap$ (AND), the operation is seeking the common elements. The common elements must satisfy the **stricter** condition, which is $A$.
- Thus, $A \cap (A \cup B)$ is actually just the same as the simpler expression $A$.


$$
A \cap (A \cup B) = A
$$


---

## 🥈 The Union Form (The Lenient Condition Prevails)

Consider a similar expression:


$$
A \cup (A \cap B)
$$


- $A$ is **more lenient** than $(A \cap B)$, since for $(A \cap B)$, **both** $A$ and $B$ must be met to make it true.
- Since this expression hinges around $\cup$ (OR), the operation is seeking all elements from either side. The result will be defined by the **most lenient** condition, which is $A$.
- Thus, $A \cup (A \cap B)$ is actually just the same as the simpler expression $A$.


$$
A \cup (A \cap B) = A
$$


---

## ✨ The Absorption Law

The two patterns derived above form the **Absorption Law**:

- $A \cap (A \cup B) = A$
- $A \cup (A \cap B) = A$

This pattern is known as the **Absorption Law**, as the more favorable condition (A) is preferred, and it, in a sense, "absorbs" away the less favorable condition ($A \cup B$ or $A \cap B$).

- In $A \cap (A \cup B)$, $\cap$ (AND) is the root operator, thus the **stricter** condition is favored, which is $A$.
- In $A \cup (A \cap B)$, $\cup$ (OR) is the root operator, thus the **lenient** condition is favored, which is $A$.

In both expressions, $A$ turns out to be the more favorable condition.

---

## 🔄 Final Observation

As a result of the Absorption Law, these two expressions are, of course, equal to each other:


$$
A \cap (A \cup B) = A \cup (A \cap B)
$$
