---
title: "🔢 Signed Number Representations in Binary"
date: 2025-11-08
draft: false
---


### 🧠 What Are Signed Numbers?

> Signed numbers allow binary systems to represent both positive and negative values.
> The most significant bit (MSB) typically acts as the **sign bit**:
>
> - `0` → positive
> - `1` → negative

---

### 🔧 Common Encoding Schemes

#### 1️⃣ Sign-Magnitude

```plaintext
+5 → 0101
−5 → 1101
```

- MSB is the sign; remaining bits are magnitude
- Two representations of zero: `0000` (+0), `1000` (−0)

#### 2️⃣ One’s Complement

```plaintext
+5 → 0101
−5 → 1010  (bitwise NOT of +5)
```

- Negative numbers are bitwise inverses of positives
- Two zeros: `0000` (+0), `1111` (−0)
- Requires end-around carry in addition

#### 3️⃣ Two’s Complement ✅ (Most Common)

```plaintext
+5 → 0101
−5 → 1011  (bitwise NOT of +5 → 1010, then +1)
```

- Single representation of zero: `0000`
- Clean arithmetic: no special rules for subtraction
- Range: `−2ⁿ⁻¹` to `2ⁿ⁻¹ − 1`

---

### 🧮 Range Comparison (4-bit)

| Encoding        | Min Value | Max Value | Zero Count |
|----------------|-----------|-----------|------------|
| Sign-Magnitude  | −7        | +7        | 2          |
| One’s Complement| −7        | +7        | 2          |
| Two’s Complement| −8        | +7        | 1 ✅        |
