---
title: "🧮 Binary Complement Arithmetic"
date: 2025-11-08
draft: false
---

This module explores how **1’s complement** and **2’s complement** systems handle addition, subtraction, and multiplication in binary. These systems allow negative numbers to be encoded and manipulated using only addition and bitwise logic.

---

## 📌 1. Complement Basics

| Type            | Definition                          | Operation                        |
|-----------------|-------------------------------------|----------------------------------|
| 1’s Complement  | Flip all bits                       | `~A` (bitwise NOT)               |
| 2’s Complement  | Flip all bits, then add 1           | `~A + 1`                         |

---

## ➕ 2. Addition in Complement Systems

### ✅ 2’s Complement Addition

```text
  A =  0101   (5)
  B =  1110   (-2 in 2's complement)
------------------
A + B =  0011   (3)
```

- No special handling needed.
- Overflow is ignored unless sign bit flips unexpectedly.

### ✅ 1’s Complement Addition (with end-around carry)

```text
  A =  0101   (5)
  B =  1101   (-2 in 1's complement)
------------------
Sum =  10010  → drop overflow bit → 0010
Add carry: 0010 + 1 = 0011 (3)
```

{{< callout type="default" >}}
Overflow is ignored because we `specifically designed complements to ignore overflow`, it is by design, check [ Derivation of Complement Forms](../method-of-complements/) to understand why it was designed like so
{{< /callout >}}
---

## ➖ 3. Subtraction via Complement Addition

### ✅ 2’s Complement Subtraction

To compute `A - B`, do `A + (2’s complement of B)`:

```text
  A =  0101   (5)
  B =  0011   (3)
  ~B + 1 = 1100 + 1 = 1101 (-3)
------------------
A - B = 0101 + 1101 = 10010 → drop overflow → 0010 (2)
```

### ✅ 1’s Complement Subtraction

Use `A + (1’s complement of B) + 1`, then apply end-around carry:

```text
  A =  0101   (5)
  B =  0011   (3)
  ~B = 1100
------------------
Sum = 0101 + 1100 + 1 = 10010 → drop overflow → 0010
Add carry: 0010 + 1 = 0011 (2)
```

---

## ✖️ 4. Multiplication in Complement Systems

Multiplication is typically done using **unsigned logic**, then sign is handled separately.

### ✅ Example: 2’s Complement Multiplication

```text
  A =  1110   (-2)
  B =  0011   (3)
------------------
Unsigned: 2 × 3 = 6
Sign: Negative × Positive = Negative
Result: 11111010 (−6 in 8-bit 2’s complement)
```

### ⚠️ Notes

- Multiplication requires sign extension.
- Most systems use **Booth’s algorithm** or **signed multiplication logic**.

---

## 🧩 Summary Table

| Operation     | 1’s Complement | 2’s Complement |
|---------------|----------------|----------------|
| Addition      | Add + end-around carry | Add directly |
| Subtraction   | Add 1’s complement + 1 + carry | Add 2’s complement |
| Multiplication| Unsigned × Unsigned, then apply sign | Same, with sign logic |
