---
title: "💥 Integer Overflow"
date: 2025-11-08
draft: false
---

## 🧠 Motivation

> [!Why we care]
> Integer overflow is a semantic mismatch between mathematical expectation and hardware constraints.
>
> In modular arithmetic, overflow is benign. In fixed-width binary systems, it can flip signs, corrupt logic, or cause unintended wraparound.

---

## 🔣 What Is Integer Overflow?

Integer overflow occurs when the result of an arithmetic operation exceeds the **maximum value representable** within a fixed number of bits.

- In **unsigned** systems: values wrap from `2ⁿ − 1` back to `0`
- In **signed (2’s complement)** systems: values wrap from `+2ⁿ⁻¹ − 1` to `−2ⁿ⁻¹`

---

## 🧮 Example: 4-bit Signed Overflow

| A     | B     | A + B | Expected | Actual | Interpretation |
|-------|-------|-------|----------|--------|----------------|
| `0111` (+7) | `0001` (+1) | `1000` | +8       | −8     | Overflow occurred |

> MSB flipped → system interprets result as negative

---

## 🔁 Why It Happens

### ✅ Mathematical View

- You expect: `7 + 1 = 8`
- In modular arithmetic:
  `8 mod 16 = 8` ✅ (still valid within modulus `2⁴ = 16`)

### ❌ Hardware View

- 4-bit signed integers range from `−8 to +7`
- `1000` is interpreted as `−8`
- Result is **semantically incorrect**, even if **bitwise correct**

---

## ⚠️ Overflow Detection Logic

### 🔧 Signed Addition Overflow

Occurs when:

- Adding two **positive numbers** yields a **negative result**
- Adding two **negative numbers** yields a **positive result**

### 🧠 Detection Formula

```text
Overflow = C_in_MSB ⊕ C_out_MSB
```

Where:

- `C_in_MSB`: carry into most significant bit
- `C_out_MSB`: carry out from most significant bit

---

## 📊 Visual Anchor: 4-bit Signed Wraparound

```text
+7 → 0111 +8 → 1000 ← interpreted as −8
+9 → 1001 ← interpreted as −7
...
+15 → 1111 ← interpreted as −1
```
