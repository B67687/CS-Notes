---
title: "🔢 Adders"
date: 2025-11-08
draft: false
---

Adders circuits are foundational in any complex logic circuit

## ⚙️ Half Adder

```
Carry
	    A
+       B
------------
        Sum
```

> [!info] Logic Equations
> $\text{Sum} = A \oplus B$
>
> $\text{Carry} = A \cdot B$

> [!tip] Notes
>
> - No carry-in input
> - Cannot be chained directly for multi-bit addition
> - Gate count: **1 XOR**, **1 AND**

| A | B | Sum (A⊕B) | Carry (A·B) |
|---|---|-----------|-------------|
| 0 | 0 |     0     |      0      |
| 0 | 1 |     1     |      0      |
| 1 | 0 |     1     |      0      |
| 1 | 1 |     0     |      1      |

More on [[🔢 Subtractors| Subtractors]]

---

## 🧠 Full Adder

```
Carry-out   Carry-in
	        A
+           B
-------------------
		    Sum
```

> [!info] Logic Equations
> $\text{Sum} = A \oplus B \oplus C_{in}$
>
> $C_{out} = A \cdot B + (A \oplus B) \cdot C_{in}$

> [!tip] Notes
>
> - Can be chained for multi-bit addition
> - Minimal logic avoids redundancy using XOR
> - Exhaustive logic is more intuitive but less gate-efficient
> - Gate count (minimal): **2 XOR**, **2 AND**, **1 OR**

| A | B | Cin | Sum | Cout |
|---|---|-----|-----|--------|
| 0 | 0 |  0  |  0  |   0    |
| 0 | 0 |  1  |  1  |   0    |
| 0 | 1 |  0  |  1  |   0    |
| 0 | 1 |  1  |  0  |   1    |
| 1 | 0 |  0  |  1  |   0    |
| 1 | 0 |  1  |  0  |   1    |
| 1 | 1 |  0  |  0  |   1    |
| 1 | 1 |  1  |  1  |   1    |

More on [[➕ Full Adder | Full Adders]]
