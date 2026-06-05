---
title: "📐 Euclidean Division"
date: 2025-11-08
draft: false
---


### 🧠 Definition
Euclidean division is the process of dividing one integer by another to obtain a **quotient** and a **remainder**, satisfying:

$$
a = bq + r \quad \text{where} \quad 0 \le r < |b|
$$

- `a`: dividend (integer)  
- `b`: divisor (non-zero integer)  
- `q`: quotient (integer)  
- `r`: remainder (integer)  

This is **not** fractional division—it's about decomposing integers.

---

### 🔢 Example

Let’s divide $a = 17$ by $b = 5$:

$$
17 = 5 \cdot 3 + 2
$$

- Quotient $q = 3$  
- Remainder $r = 2$  

✅ Check: $0 \le 2 < 5$

---

### 📊 Table of Examples

| Dividend $a$ | Divisor $b$ | Quotient $q$ | Remainder $r$ | Equation |
|--------------|-------------|--------------|----------------|----------|
| 17           | 5           | 3            | 2              | $17 = 5 \cdot 3 + 2$ |
| -17          | 5           | -4           | 3              | $-17 = 5 \cdot (-4) + 3$ |
| 23           | -4          | -6           | -1             | $23 = (-4) \cdot (-6) + (-1)$ |

> ℹ️ The remainder always satisfies $0 \le r < |b|$, regardless of the signs of $a$ or $b$.

---

### 🧩 Properties

- **Uniqueness**: For any integers $a$ and $b \ne 0$, there exists a *unique* pair $(q, r)$ such that:
  $$
  a = bq + r \quad \text{with} \quad 0 \le r < |b|
  $$
- **Used in**:
  - Modular arithmetic: $a \mod b = r$
  - Euclidean algorithm for GCD
  - Integer division logic in programming

---

### 🧮 Algorithm (Pseudocode)

```text
function euclidean_division(a, b):
    q = floor(a / b)
    r = a - b * q
    return (q, r)
```

> 🧠 `floor(a / b)` ensures the remainder is non-negative and less than `|b|`.

---

### 🧠 Visual Aid Suggestion

Consider adding a number line diagram showing:
- `a` as a point  
- `bq` as the nearest multiple of `b` ≤ `a`  
- `r` as the gap between `bq` and `a`
