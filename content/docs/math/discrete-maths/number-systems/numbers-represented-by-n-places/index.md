---
title: "🔣 Numbers Represented by N Places"
date: 2025-11-08
draft: false
---

{{< callout type="info" >}}
**Numbers Represented by $n$ Places**
In any positional number system of base $b$, using $n$ places allows representation of exactly $b^n$ distinct values.
{{< /callout >}}
## 🎯 Derivation through Combinatorics
Every place value has choices ranging from `0` to the base number `b-1`, which is `b` choices

$$
0, \space 1, \space 2, \space 3, \cdots, \space b-2, \space b-1
$$

And with `n` places, we have a combined outcome of `n` outcomes

$$
\underline{\phantom{()} \text{n}^{th} \space \text{place}} 
\quad 
\underline{\text{n-1}^{th} \space \text{place}} 
\quad
\cdots 
\quad 
\underline{\text{2}^{nd} \space \text{place}}
\quad 
\underline{\text{1}^{st} \space \text{place}}
$$

Since each outcome there are `b` choices, and we have `n` outcomes, totalling to $b^n$ outcomes

$$
b^n = \underbrace{b \times b \times b \times \cdots \times b \times b}_{\text{n times}}
$$

We have a total of **$b^n$  possible numbers**

## 🎯 Derivation through Number System

Counting from `1` to the **maximum value of the base** `b` for `n` digits

$$
(b-1)b^{n-1} + (b-1)b^{n-2} + \cdots + (b-1)b^1 + (b-1)b^0
$$

Which is also the same as the place value of the next place minus 1

$$
b^n - 1
$$

Then we count `0` as the unaccounted representation

$$
(b^n - 1) + 1
$$

We get

$$
b^n
$$
