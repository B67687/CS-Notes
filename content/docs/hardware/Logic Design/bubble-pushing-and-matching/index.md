---
title: "🔁 Bubble Pushing and Matching"
date: 2025-11-08
draft: false
---


We want to make logic gates more understandable to us by

- Shifting **NOT** gates **away from outputs**,
- Eliminating **NOT** gates that **face each other** from *OUTPUT* of one to the *INPUT* of another.

We will end up with an **input-priority**, simplified logic circuit

---

## 🧪 Shift NOT Gates away from Output

We can do this through shifting the negation from the output to the inputs,
while also switching to the other fundamental logic gate (AND, OR)

> This is the **De Morgan’s Law**

| Original Expression | Transformed Expression |
|---------------------|------------------------|
| $\overline{A \cdot B}$ | $\overline{A} + \overline{B}$ |
| $\overline{A + B}$ | $\overline{A} \cdot \overline{B}$ |

We want to remove the negations on all the logic gates:

- Because negations from outputs can always pass **backwards** to their inputs,
  while it **cannot always pass forwards** to another input
- We will start from the **ending logic gate** and do negation flipping
  all the way until we reach the **starting logic gates**

{{< callout type="default" >}}
**Name Drop**
This is also known as **Bubble Pushing**
{{< /callout >}}
---

## 🫧 Eliminate NOT gates Facing Each Other

Sometimes negations at an **output** of a gate flows to the negation of the **input** of another

As negation works in a system of only 2 states, applying negations in pairs will result in **no net change**

{{< callout type="info" >}}
**Optimisation**
We can **eliminate both the negations** at the output of one and at where it flows into the input of another to **reduce the number of unnecessary gates**

[!note] Name Drop
This is also known as **Bubble Matching**
{{< /callout >}}