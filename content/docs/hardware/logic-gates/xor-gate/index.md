---
title: "🔀 XOR Gate"
date: 2025-11-08
draft: false
---


| A | B | A ⊕ B |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   0    |

- **XOR outputs 1 only when inputs differ between 2-inputs**
- Acts as a **bitwise difference detector**

---

### Conditional Inverter

- `A ⊕ 0` → preserves A
- `A ⊕ 1` → inverts A

This makes XOR ideal for circuits where inversion is **controlled by a single flag**, like `Add/Sub`.

### Parity Checker

- XOR of all bits in a word → 1 if odd number of 1s
- Used in error detection and parity generation

### Bit Masking

- Toggle specific bits using XOR with a mask
- Example: `value ⊕ 0xFF` → bitwise inversion

---

## 🔧 Application: Add/Subtract Circuit

| Component     | Role in Addition | Role in Subtraction |
|---------------|------------------|----------------------|
| XOR gates     | Pass-through Y   | Invert Y             |
| Carry-in      | 0                | 1 (adds the +1)      |
| Full adders   | Add X and Y'     | Add X and \( \overline{Y} + 1 \) |

- XOR gates conditionally invert Y based on `Add/Sub`
- Carry-in completes the two’s complement transformation

---

## 🧠 Motivation Summary

- XOR is **not just a logic gate**—it’s a semantic switch
- Enables **minimal, elegant control logic** without branching
- Perfect for **arithmetic, masking, toggling, and parity**