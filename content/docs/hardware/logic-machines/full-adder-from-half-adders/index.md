---
title: "🧮 Full Adder from Half Adders"
date: 2025-11-08
draft: false
---

A full adder computes the sum of three binary inputs: `A`, `B`, and `C_in` (carry-in), producing:

- `Sum`
- `C_out` (carry-out)

This notebook shows how to construct a full adder using **two half adders** and **one OR gate**.

---

## 🔧 Logic Expressions

### Full Adder Logic

- `Sum = A ⊕ B ⊕ Cin`
- `Cout = (A ⊕ B)·Cin + A·B`

---

## 🧱 Construction Using Half Adders

### Step 1: First Half Adder

- **Inputs**: `A`, `B`
- **Outputs**:
  - `Sum1 = A ⊕ B`
  - `Carry1 = A · B`

### Step 2: Second Half Adder

- **Inputs**: `Sum1`, `Cin`
- **Outputs**:
  - `Sum = Sum1 ⊕ Cin`
  - `Carry2 = Sum1 · Cin`

### Step 3: Final Carry Output

- `Cout = Carry1 + Carry2`

---

## 🔌 Gate-Level Implementation

| Component     | Inputs         | Output     | Function         |
|---------------|----------------|------------|------------------|
| XOR Gate 1    | A, B           | Sum1       | A ⊕ B            |
| AND Gate 1    | A, B           | Carry1     | A · B            |
| XOR Gate 2    | Sum1, Cin      | Sum        | Sum1 ⊕ Cin       |
| AND Gate 2    | Sum1, Cin      | Carry2     | Sum1 · Cin       |
| OR Gate       | Carry1, Carry2 | Cout       | Carry1 + Carry2  |

---

## 🧪 Verilog Structural Module

```verilog
module full_adder (
    input wire A,
    input wire B,
    input wire Cin,
    output wire Sum,
    output wire Cout
);

    wire Sum1, Carry1, Carry2;

    // First half adder
    xor xor1 (Sum1, A, B);
    and and1 (Carry1, A, B);

    // Second half adder
    xor xor2 (Sum, Sum1, Cin);
    and and2 (Carry2, Sum1, Cin);

    // Final carry output
    or or1 (Cout, Carry1, Carry2);

endmodule
```
