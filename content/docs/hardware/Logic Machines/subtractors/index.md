---
title: "🔢 Subtractors"
date: 2025-11-08
draft: false
---

Subtractor circuits are foundational in any complex logic circuit

## ⚙️ Half Subtractor

```
Borrow
	    A
-       B
-------------
        Diff
```


{{< callout type="info" >}}
**Logic Equations**
$\text{Diff} = A \oplus B$  
$\text{Borrow} = \overline{A} \cdot B$

[!tip] Notes

- No borrow-in input
- Cannot be chained directly for multi-bit subtraction
- Gate count: **1 XOR**, **1 AND**, **1 NOT**
{{< /callout >}}
| A | B | Diff (A⊕B) | Borrow ($\overline{A} \cdot B$) |
|---|---|-------------|-------------------------------|
| 0 | 0 |     0       |             0                 |
| 0 | 1 |     1       |             1                 |
| 1 | 0 |     1       |             0                 |
| 1 | 1 |     0       |             0                 |

More on [ Adders](../adders/)

---

## 🧠 Full Subtractor
```
Borrow-out   Borrow-in
	         A
-            B
------------------------
		     Diff
```
{{< callout type="info" >}}
**Logic Equations**
$\text{Diff} = A \oplus B \oplus B_{in}$  
$B_{out} = B \cdot B_{in} + \overline{A} \cdot (B \oplus B_{in})$

[!tip] Notes

- Can be chained for multi-bit subtraction
- Minimal logic avoids redundancy using XOR
- Exhaustive logic is more intuitive but less gate-efficient
- Gate count (minimal): **2 XOR**, **2 AND**, **1 OR**, **1 NOT**
{{< /callout >}}
| A | B | Bin | Diff | Bout |
|---|---|-----|------|------|
| 0 | 0 |  0  |  0   |  0   |
| 0 | 0 |  1  |  1   |  1   |
| 0 | 1 |  0  |  1   |  1   |
| 0 | 1 |  1  |  0   |  1   |
| 1 | 0 |  0  |  1   |  0   |
| 1 | 0 |  1  |  0   |  0   |
| 1 | 1 |  0  |  0   |  0   |
| 1 | 1 |  1  |  1   |  1   |

More on [ Full Subtractors](../full-subtractors/)
