---
title: "➕ BCD Addition"
date: 2025-11-08
draft: false
---


- BCD (Binary-Coded Decimal) represents **decimal digits 0–9** using 4-bit binary codes.
- Although 4 bits can encode 16 values (0–15), **only 0000 to 1001** are valid in BCD.
- Values from **1010 to 1111 (10–15)** are unused and considered **invalid BCD**.

---

### 🔢 BCD Encoding Table

| Decimal | BCD     | Valid? |
|---------|---------|--------|
| 0       | 0000    | ✅     |
| 1       | 0001    | ✅     |
| 2       | 0010    | ✅     |
| 3       | 0011    | ✅     |
| 4       | 0100    | ✅     |
| 5       | 0101    | ✅     |
| 6       | 0110    | ✅     |
| 7       | 0111    | ✅     |
| 8       | 1000    | ✅     |
| 9       | 1001    | ✅     |
| 10–15   | 1010–1111 | ❌   |

---

### 🧠 Addition Logic

BCD addition mimics **place-value decimal addition**:
- Add digits column-wise (units, tens, etc.)
- If the result exceeds 9, it spills into the **invalid BCD zone (10–15)** or overflows into **16–18**
- These results **cannot be represented directly in BCD**

---

### ⚠️ Correction Mechanism

To restore valid BCD:
- **Add 6 (0110)** to any sum > 9
- This bumps the result into the next valid BCD digit and triggers a **carry to the next place-value**

#### Example: 7 + 8
```
  0111 (7)
+ 1000 (8)
= 1111 (15) → invalid
+ 0110 (6)
= 1 0101 → result = 0101 (5), carry = 1
```

---

### 🧩 Symbolic Interpretation

There are two ways to interpret the correction:

#### 1. **Recount from Zero**
- Find the difference between 9 (1001) and the overflow value (e.g. 11)
- Recount from 0 to find the valid BCD digit
- Carry the excess into the next place-value

#### 2. **Bump by the Gap**
- Add the difference between the last valid BCD (9) and the last 4-bit value (15)
- This difference is always **6**
- Adding 6 pushes the result into the next BCD digit and triggers a carry

---

### 🔢 Carry Boundaries

- Max sum of two single-digit decimals: **9 + 9 = 18**
- Binary: `10010` (5 bits)
- Only **1 carry bit** is needed
- This rule holds for **any base**: the sum of two max digits always fits within one carry

---

### 🧠 Philosophical Note: Overflow as Symbolic Transition

- BCD overflow isn’t just arithmetic—it’s a **semantic shift** across digit boundaries
- The unused zone (10–15) acts as a **symbolic buffer** between valid digits and overflow
- Correction by adding 6 is a **structural bridge** between binary encoding and decimal semantics

---

### ✅ Summary Table

| Sum | Binary | Valid BCD? | Correction | Result | Carry |
|-----|--------|------------|------------|--------|-------|
| 9   | 1001   | ✅         | None       | 1001   | 0     |
| 10  | 1010   | ❌         | +0110      | 0000   | 1     |
| 11  | 1011   | ❌         | +0110      | 0001   | 1     |
| 12  | 1100   | ❌         | +0110      | 0010   | 1     |
| 13  | 1101   | ❌         | +0110      | 0011   | 1     |
| 14  | 1110   | ❌         | +0110      | 0100   | 1     |
| 15  | 1111   | ❌         | +0110      | 0101   | 1     |
