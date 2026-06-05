
> [!Summary]
> Signed multiplication in 2’s complement systems behaves like normal multiplication—with a few critical architectural quirks.
> These quirks arise from modular arithmetic, bit-width constraints, and the encoding of negative values.
> This notebook documents the four foundational principles that govern signed multiplication.

---

## 🔢 Multiplication with Quirks

- We multiply bitwise as usual: partial products, shifts, and accumulation
- But signed systems introduce:
  - **Sign correction logic**
  - **Bit-width overflow planning**
  - **Negative weight propagation**
- These quirks are not exceptions—they’re **architectural features** of 2’s complement arithmetic

---

## 📏 Maximum Bit-Length Is $m + n$

> [!Why this matters]
> Multiplying an $m$-bit number by an $n$-bit number yields a product of **at most $m + n$ bits**

> ### Derivation
>
> - Max value of $m$-bit number: $r^m - 1$
> - Max value of $n$-bit number: $r^n - 1$
> - Max product: $(r^m - 1)(r^n - 1) = r^{m+n} - r^m - r^n + 1 < r^{m+n} \quad (\forall \space m,n \ge 0)$ 
> - Numbers less than $r^{m+n}$ has $m+n$ [[🔣 Numbers Represented by N Places | bits]]

Thus, we always allocate $m + n$ bits to avoid overflow

> [!info]
> This holds in **any base**, not just binary

---

## 🧮 Sign Extension Preserves Value via Modular Arithmetic

> [!Why it works]
> Extending the sign bit (MSB) preserves the value because 2’s complement is a **modular system**

### Formal Insight

- $x$ in $n$ bits → interpreted modulo $2^n$
- Extend to $m$ bits ($m > n$): replicate MSB
- Value remains congruent modulo $2^m$

### Example

- $1101_4$ = $-3$
- Sign-extended: $11111101_8$ = still $-3$

---

## ⚙️ Signed Bit Triggers 2’s Complement Correction

> [!Why we use 2’s complement]
> The signed bit (MSB of multiplier) represents **negative weight**.
> We can’t multiply it like a normal digit—it contributes a **−2ⁿ** term.

### Correction Strategy

- Use 2’s complement of multiplicand
- Shift appropriately
- Add/subtract based on sign logic (e.g., Booth’s transitions)

### Semantic Insight

- 2’s complement lets us **encode subtraction as addition**
- This enables clean accumulation of negative partial products

---

## ✅ Flags

| Principle                 | Semantic Role               |
| ------------------------- | --------------------------- |
| Normal multiplication     | Structural baseline         |
| Max bit-width $m + n$     | Overflow planning           |
| Sign extension            | Modular integrity           |
| 2’s complement correction | Negative weight propagation |

