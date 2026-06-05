---
title: "➕ Full Adder"
date: 2025-11-08
draft: false
---


Full Adders are the simplest forms of general adder circuits that are able to add a lot of numbers together

## 🍕 Sum Logic

Given **place-values** `A`, `B`, and the **carry-in** `C_in`

Through knowledge of [[🔢 Adders| half adders]] we would add `A` and `B` first then add the carry-in, `C_in` through `XOR`

$$
(A \oplus B) \oplus C_{in}
$$

But since `XOR` is associative, the sequence or grouping of addition doesn't matter

> [!tip] General Formula for Sum
> $$
> \text{Sum} = A \oplus B \oplus C_{in}
> $$

## 🏋️ Carry Logic

Carry is a little harder to find a general form so we start from an exhaustive form, where **any pair produces a carry**

$$
C_{out} = A + B + C_{in}
$$

> `A` and `B` produces a carry
>
> **OR**
>
> `A` and `C_in` produces a carry
>
> **OR**
>
> `B` and `C_in` produces a carry

> [!example] Why we find pairs
> Pairs are the simplest constructs of condition, we can **construct sums of more summands through sums of less**, and 2 is the least amount
>
> > i.e. We don't have to find if any 3 produces a carry, as that would be under satisfied under a simpler condition of **2 pairs**

Thus, we get the first Exhaustive Form:

> [!note] Exhaustive Form
> $$
> C_{out} = A \cdot B + A \cdot C_{in} + B \cdot C_{in}
> $$

We can factor the expression a bit more once we realise that 2 terms share `C_in` as a factor

> [!info]
> We can also factor the expression for the 2 terms that share $A$ as a factor, but we prefer grouping terms sharing `C_in` because we want the focus to be on the 2 main addition terms: **A** and **B**

> [!note] Intermediate Simplified Form
> $$
> C_{out} = A \cdot B + (A + B) \cdot C_{in}
> $$

But $A$ and $B$ both being `True` is already handled by $A \cdot B$——so we have to use `exclusive OR` for atomicity

> [!tip] General Formula for Sum
> $$C_{out} = A \cdot B + (A \oplus B) \cdot C_{in}$$
