---
title: "⚠️ Overflow Detection in 2’s Complement Arithmetic"
date: 2025-11-08
draft: false
---

This module explains how **overflow** works in 2’s complement binary arithmetic, why it matters, and how to detect it using **sign bit logic** rather than carry-out flags.

---

## 🧠 What Is Overflow?

In 2’s complement systems:

- The **MSB (most significant bit)** represents the **sign**.
- Overflow occurs when the result of an addition **flips the sign unexpectedly**, violating the expected polarity based on the operands.

---

## 🔍 Overflow Detection Rule

Overflow occurs **only** when:

| Operand A | Operand B | Expected Sign | Result Sign | Overflow? |
|-----------|-----------|----------------|--------------|-----------|
| +         | +         | +              | −            | ✅ Yes     |
| −         | −         | −              | +            | ✅ Yes     |
| +         | −         | Mixed          | Any          | ❌ No      |
| −         | +         | Mixed          | Any          | ❌ No      |

---

## ➕ Example 1: No Overflow

```text
  A =  0100   (+4)
  B =  0011   (+3)
------------------
Sum = 0111   (+7) → MSB = 0 → ✅ No overflow
```

---

## ❌ Example 2: Overflow

```text
  A =  0100   (+4)
  B =  0101   (+5)
------------------
Sum = 1001   (−7) → MSB flipped → ❌ Overflow
```

Expected a positive result, but got a negative due to sign bit flip.

---

## ➖ Example 3: Negative Overflow

```text
  A =  1100   (−4)
  B =  1101   (−3)
------------------
Sum = 1001   (+9) → MSB flipped → ❌ Overflow
```

Expected a negative result, but got a positive due to sign bit flip.

---

## 🧩 Overflow vs Carry-Out

| System         | Carry-Out Matters? | Sign Bit Matters? |
|----------------|--------------------|--------------------|
| Unsigned Binary| ✅ Yes              | ❌ No              |
| 2’s Complement | ❌ No               | ✅ Yes             |

In 2’s complement, **carry-out from MSB is ignored**. Only the **sign bit** determines overflow.

---

## 🛠️ Vault Integration Ideas

- Diagram sign bit logic for overflow detection
- Compare unsigned vs signed overflow flags
- Annotate ALU behavior for addition and subtraction
- Embed truth tables for overflow conditions

---

## 🔬 Bonus: Hardware-Friendly Overflow Check

```text
Overflow = (A_sign == B_sign) AND (Result_sign ≠ A_sign)
```

This logic gate formula can be implemented directly in digital circuits.`
