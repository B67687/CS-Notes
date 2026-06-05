---
title: "☯️ XNOR vs NXOR"
date: 2025-11-08
draft: false
---

The gate commonly known as **XNOR** is logically the **negation of XOR**, but its name introduces semantic confusion.

Linguistically, “XNOR” implies “exclusive NOR,” which is a contradiction—**NOR already implies total exclusion**, and cannot be made exclusive.

The correct logical name should be **NXOR**, following the pattern of NAND and NOR.

---

## ✌️ Gates in 2-inputs

| Gate Name | Logical Meaning                 |
|-----------|---------------------------------|
| AND       | All True                        |
| OR        | At least one True               |
| NOT       | Flip Truth Value                |
| NAND      | At least one False              |
| NOR       | All False                       |
| XOR       | **Opposite Truth Values**       |
| XNOR      | Same Truth Values               |

## 🔍 Gates Generalised

| Gate Name | Logical Meaning                 |
|-----------|---------------------------------|
| AND       | All True                        |
| OR        | At least one True               |
| NOT       | Flip Truth Value                |
| NAND      | At least one False              |
| NOR       | All False                       |
| XOR       | **Odd Number of Truths**        |
| XNOR      | Same Truth Values               |

## 🚅Derivation of Naming Scheme

`OR` means both of them included
`NOR` means not `OR`, so none of them are included
`XOR` means only one of them is included at the same time
`XNOR` should mean only one of them is excluded at one time

### 🌴Diversion of Linguistics

But that's not what `XNOR` means formally, `XNOR` formally means both of them must be included or excluded

Moreover, logically, **only one of them is excluded** is the same thing as **only one of them is included**, which is what we call `XOR` already

So by the way of naming things, `XNOR` and `XOR` should have been the same meaning

### ⚓ Practical Solution

If we want something that is the opposite of `XOR`, we will have to negate `XOR` from the outer scope, which gets us `NXOR`
> `NXOR` is the logical way the opposite of `XOR` should've been named

### 🌐 Reality

But `XNOR` perhaps looked nicer to us than `XNOR`, so `XNOR` became to mean what `NXOR` does mean——`inputs` are equal
