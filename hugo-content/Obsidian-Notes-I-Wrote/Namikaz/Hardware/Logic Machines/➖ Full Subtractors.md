---
title: "➖ Full Subtractors"
date: 2025-11-08
draft: false
---

Full Subtractors are the simplest forms of general subtractor circuits that are able to subtract multi-bit numbers in chains

## 🧮 Difference Logic

Given **place-values** `A`, `B`, and the **borrow-in** `B_in`

Through knowledge of [[🔢 Subtractors| half subtractors]] we would subtract `B` from `A` first, then subtract the borrow-in, `B_in` through `XOR`

$$
(A \oplus B) \oplus B_{in}
$$

Since `XOR` is associative, the sequence or grouping of subtraction doesn't matter

> [!tip] General Formula for Difference
> $$
> \text{Diff} = A \oplus B \oplus B_{in}
> $$

---

## 🏋️ Borrow Logic

Borrow is a little harder to find a general form, so we start from an **exhaustive form**, where **any pair of conditions triggers a borrow**

$$
B_{out} = \overline{A} + B + B_{in}
$$

> `A` is 0 and `B` is 1 → need to borrow  
>
> **OR**
>
> `A` is 0 and `B_in` is 1 → still need to borrow  
>
> **OR**
>
> `B` is 1 and `B_in` is 1 → subtracting 2 from 1 or 0 → need to borrow

> [!example] Why we find pairs
> Pairs are the simplest constructs of condition, we can **construct subtractions of more terms through subtractions of less**, and 2 is the least amount
>
> > i.e. We don't have to check if all 3 inputs cause a borrow, since any 2 already do

Thus, we get the first Exhaustive Form:

> [!note] Exhaustive Form
> $$
> B_{out} = \overline{A} \cdot B + \overline{A} \cdot B_{in} + B \cdot B_{in}
> $$

We can factor the expression a bit more once we realize that 2 terms share $B_{in}$ as a factor

> [!info]
> We can also factor the expression for the 2 terms that share $\overline{A}$ as a factor, but we prefer grouping terms sharing $B_{in}$ because we want the focus to be on the 2 main subtraction terms: **A** and **B**

> [!note] Intermediate Simplified Form
> $$
> B_{out} = \overline{A} \cdot B + (\overline{A} + B) \cdot B_{in}
> $$

But $\overline{A}$  and $B$ both being `True` is already handled by $\overline{A} \cdot B$——so we have to use `exclusive OR` for atomicity

> [!tip] General Formula for Borrow
> $$
> B_{out} = \overline{A} \cdot B + (\overline{A} \oplus B) \cdot B_{in}
> $$

This form is minimal, symmetric, and suitable for chaining full subtractors across multi-bit logic.
