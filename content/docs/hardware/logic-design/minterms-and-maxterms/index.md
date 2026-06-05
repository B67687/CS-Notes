---
title: "💡 Minterms and Maxterms"
date: 2025-11-08
draft: false
---

Any system has `inputs` and `outputs`, and can have outputs that represent `ON` or `OFF` states

Our goal is to derive Boolean expression(s) that fully reflects the relationship between the `inputs` of a system to its active states——`ON` or `OFF`

---

## ☯️ ON and OFF States

A function’s output is either **ON** or **OFF**

{{< callout type="info" >}}
**Defining a System**
We can represent the system through

- All input combinations that turn it **ON**
- Or all combinations that turn it **OFF**
{{< /callout >}}
Defining one automatically defines the other—this is the [Principle of Duality](../principle-of-duality/)

We only need to choose one side to work with.

---

## 🔌Importance of Active States

When designing systems that has active states——`ON` and `OFF`——we have to determine which **state we want to focus on** that will **represent the behaviour of the system**
> As the same system cannot be represented by both `ON` and `OFF` at the same time
>
> They must be **represented separately**

For us, we would prefer to think of **existence** as a more meaningful and important state than **non-existence**

So we will focus on which what represents existence——`ON`——to represent systems with active states

---

## 💈Strictness of Active States

We also prefer to have the state that we care about——`ON`——to have a stricter condition

This is such that we can **control exactly** which **combinations of inputs** in our systems will definitely **lead to its activation**

In the same vein, `OFF` will be treated as the more lenient condition

---

## 📐Activation in Binary

The binary numbers picked for activation is also reflected as what we prefer to be active, where `1` represents `High Electrical Signal` and `0` represents `Low Electrical Signal`

The convention used for representing activation states is also called [ Active High](../active-high-and-active-low/)

---

## 🧱 Representation of Each Input Combination by Active State

All the states of a system can be listed out in what we call a [ Truth Table](../truth-tables/)

| A | B | C | F |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

Each row of such a table contains a **unique input combination** of the system——`A`,`B`,`C` in this case——that relates to its corresponding **output**——either `1` representing `ON` or `0` representing `OFF`

{{< callout type="info" >}}
**Strictness of Combinations**
Thus each `ON` state of the system can be represented by **strict combination of all its corresponding inputs**

And each `OFF` state of the system can be represented by **lenient combination of all its corresponding inputs**
{{< /callout >}}
These concepts will be coined and explained in further detail in the below sub-sections

---

## 🔹 Minterm

The **strict combination of all the corresponding inputs** that causes the output to have an `ON` state, is called a `Minterm`

{{< callout type="info" >}}
**Etymology**
It is also the **minimum combination-of-inputs condition** for the system to be considered `ON`

Thus, the **term** representing such a combination of inputs is called the **Minimum Term**

Or the `Minterm`
{{< /callout >}}
**Strictness** is represented by the `AND` operator, so its inputs will be `AND-ed` to represent the `ON` state

Since `AND` requires all its inputs to be `True` for the `AND` expression to be `True`, the inputs that are `0` in that row are represented through the `complement` of that input variable

{{< callout type="info" >}}
For $A=1$, $B=0$, $C=1$, the minterm is:
$$A \cdot B' \cdot C$$
This is only true when A is `True`, B is `False`, and C is `True`
{{< /callout >}}
---

## 🔸 Maxterm

The **lenient combination of all the corresponding inputs** that causes the output to have an `OFF` state, is called a `Maxterm`

{{< callout type="info" >}}
**Etymology**
It is also the **maximum combination-of-inputs condition** for the system to be considered `OFF`

Thus, the **term** representing such a combination of inputs is called the **Maximum Term**

Or the `Maxterm`
{{< /callout >}}
**Lenience** is represented by the `OR` operator, so its inputs will be `OR-ed` to represent the `OFF` state

Since `OR` requires none of its inputs to be `True` for the `OR` expression to be `False`, the inputs that are `1` in that row are represented through the `complement` of that input variable

{{< callout type="info" >}}
For $A=1$, $B=0$, $C=1$, the maxterm is:
$$A' + B + C'$$
This is only false when A is `True`, B is `False`, and C is `True`
{{< /callout >}}
---

## 🧮 Representation of the System by Active State

Now that we have an expression representing each `ON` state of the system through the **strict combination of all its corresponding inputs**——the `minterm`

And also an expression representing each `OFF` state of the system through the **lenient combination of all its corresponding inputs**——the `maxterm`

We can represent the system itself through the **combinations of all of either**
> the expressions representing the `ON` states of the system——`minterms`
>
> OR
>
> the expressions representing the `OFF` states of the system——`maxterms`

{{< callout type="info" >}}
**The System Represented Through `ON` States**
Since each separate condition for the `ON` state is `strict`, we only **need either of them** for the whole system to be `ON`

> Thus, the representation of the system through all the `ON` states is `lenient`

[!tip] The System Represented Through `OFF` States
Since each separate condition for the `OFF` state is `lenient`, we must **exclude all of them** for the whole system to be `OFF`

> Thus, the representation of the system through all the `OFF` states is `strict`
{{< /callout >}}
These concepts will be coined and explained in further detail in the below sub-sections

---

## ➕ Sum of Minterms

The system represented by `ON` state, through the **lenient combination** of **minterms**, is called the `Sum of Minterms`

It is named so because a **lenient combination** is what `OR` represents, which written out in [ Boolean Algebraic Form](../boolean-algebra/) uses the `+` sign to represent `OR`

Take the same Truth Table shown earlier

| A | B | C | F |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

The `Sum of Minterms` will be represented and calculated like this

$$
\begin{align}
F(A, B, C) &= \sum m(1,3,4,6,8) \\
&= m_1 + m_3 + m_4 + m_6 + m_8 \\
&= A'B'C' + A'BC' + A'BC + AB'C + ABC
\end{align}
$$

> This is read as:
>
> The general function, `F`, with input variables, `A`,`B`,`C`, is the sum, `Σ`, of minterms, `m`, in rows `1`,`3`,`4`,`6`,`8`

This **full exhaustive form** is known as the **Canonical Form**, as it contains all the **terms** that contain all the **input variables**

This expression is thus more aptly known as the `Sum of Products`, or `SOP` for short
{{< callout type="warning" >}}
Take note that *Sum* here is **NOT the arithmetic sum** used in Maths, but a **borrowed symbol** to represent `OR` in Logic

The **structural similarity** between logical `OR` and arithmetic sum——such as *associativity*, *commutativity*, and *distributivity*——is why the symbol was borrowed
{{< /callout >}}
Any further simplification of `Sum of Products` can be done through an optimised method, leveraging visualisation, called [ Karnaugh Maps](../karnaugh-maps/)

---

## ✖️ Product of Maxterms

The system represented by `OFF` state, through the **strict combination** of **maxterms**, is called the `Product of Maxterms`

It is named so because a **strict combination** is what `AND` represents, which written out in [ Boolean Algebraic Form](../boolean-algebra/) uses the `⋅` sign to represent `AND`

Take the same Truth Table shown earlier

| A | B | C | F |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

The `Product of Maxterms` will be represented and calculated like this

$$
\begin{align}
F(A, B, C) &= \prod M(2,5,7) \\
&= M_2 \cdot M_5 \cdot M_7 \\
&= (A + B + C') \cdot (A + B' + C) \cdot (A' + B + C)
\end{align}
$$

> This is read as:
>
> The general function, `F`, with input variables, `A`,`B`,`C`, is the product, `Π`, of maxterms, `M`, in rows `2`,`5`,`7`

This **full exhaustive form** is known as the **Canonical Form**, as it contains all the **terms** that contain all the **input variables**

This expression is thus more aptly known as the `Product of Sums`, or `POS` for short
{{< callout type="warning" >}}
Take note that *Product* here is **NOT the arithmetic product** used in Maths, but a **borrowed symbol** to represent `AND` in Logic

The **structural similarity** between logical `AND` and arithmetic product——such as *associativity*, *commutativity*, and *distributivity*——is why the symbol was borrowed
{{< /callout >}}
Any further simplification of `Product of Sums` can be done through an optimised method, leveraging visualisation, called [ Karnaugh Maps](../karnaugh-maps/)

---

## ⚖️ De Morgan Laws

Both `SOP` and `POS` represent the same function—just from opposite perspectives.

{{< callout type="info" >}}
****De Morgan’s Laws****
De Morgan's Laws allow us to interchange `AND`/`OR` operations transform between `SOP` and `POS`

$$(A \cdot B)' = A' + B'$$
$$(A + B) = A' \cdot B'$$
{{< /callout >}}
---

## 📋 Summary Table

| Logic Basis        | Concept | Primary Goal              | Operator for Terms | Operator to Combine Terms |
|--------------------|---------|----------------------------|--------------------|----------------------------|
| Active High Logic  | **Sum of Minterms**<br>*OR*<br>Sum of Products or **SOP** | Describe all "ON" states (1s)  | **AND** (strict)    | **OR** (inclusive)         |
| Active High Logic  | **Product of Maxterms**<br>*OR*<br>Product of Sums or **POS** | Describe all "OFF" states (0s) | **OR** (less strict)| **AND** (strict)           |
