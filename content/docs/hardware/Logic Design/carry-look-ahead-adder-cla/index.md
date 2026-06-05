---
title: "⚡ Carry Look-Ahead Adder (CLA)"
date: 2025-11-08
draft: false
---

## 🧠 Overview

The Carry Look-Ahead Adder (CLA) is a fast binary adder architecture that computes carry signals in parallel using **generate** and **propagate** logic. Unlike ripple carry adders, which wait for each carry to ripple through sequentially, CLA predicts carry outcomes based on input bits—enabling faster addition.

---

## 🔣 Bitwise Inputs

Let `A = AₙAₙ₋₁...A₀` and `B = BₙBₙ₋₁...B₀` be two n-bit binary numbers.
Each bit position `i` has:

- `Aᵢ`, `Bᵢ`: input bits
- `Gᵢ`: generate signal
- `Pᵢ`: propagate signal
- `Cᵢ`: carry-in to bit `i`
- `Sᵢ`: sum output

---

## ⚙️ Generate and Propagate Logic

### 🔧 Definitions

- **Generate**: `Gᵢ = Aᵢ · Bᵢ`
  → Carry is generated if both inputs are 1.
- **Propagate**: `Pᵢ = Aᵢ ⊕ Bᵢ`
  → Carry is propagated if exactly one input is 1.

### 📊 Truth Table

| Aᵢ | Bᵢ | Gᵢ | Pᵢ | 🧩 Interpretation             |
|----|----|----|----|------------------------------|
| 0  | 0  | 0  | 0  | No carry generated or propagated |
| 0  | 1  | 0  | 1  | Carry will propagate if present |
| 1  | 0  | 0  | 1  | Carry will propagate if present |
| 1  | 1  | 1  | 0  | Carry is generated locally     |

---

## 🔁 Carry Computation

### 🧮 Recursive Carry Logic

Given initial carry-in `C₀`, the carry-out for each bit is:

- `C₁ = G₀ + P₀ · C₀`
- `C₂ = G₁ + P₁ · C₁ = G₁ + P₁ · (G₀ + P₀ · C₀)`
- `C₃ = G₂ + P₂ · C₂ = G₂ + P₂ · (G₁ + P₁ · (G₀ + P₀ · C₀))`
- General form:
  `Cᵢ₊₁ = Gᵢ + Pᵢ · Cᵢ`

### ➕ Sum Logic

- `Sᵢ = Pᵢ ⊕ Cᵢ`

---

## 🧷 CLA Block Diagram (Visual Anchor)

```text
           ┌────────────┐
   Aᵢ ─────▶            │
           │   AND      ├─────► Gᵢ = Aᵢ · Bᵢ
   Bᵢ ─────▶            │
           └────────────┘

           ┌────────────┐
   Aᵢ ─────▶            │
           │   XOR      ├─────► Pᵢ = Aᵢ ⊕ Bᵢ ─┐
   Bᵢ ─────▶            │                     │
           └────────────┘                     ▼
                                        ┌────────────┐
                                Cᵢ ─────▶            │
                                        │   AND      ├─────► Pᵢ · Cᵢ
                                Pᵢ ─────▶            │
                                        └────────────┘

           ┌────────────┐
   Gᵢ ─────▶            │
           │   OR       ├─────► Cᵢ₊₁ = Gᵢ + Pᵢ · Cᵢ
Pᵢ · Cᵢ -──▶            │
           └────────────┘

           ┌────────────┐
   Pᵢ ─────▶            │
           │   XOR      ├─────► Sᵢ = Pᵢ ⊕ Cᵢ
   Cᵢ ─────▶            │
           └────────────┘
```

---

## ✅ Advantages

- ⚡ **Speed**: Parallel carry computation eliminates ripple delay
- 🧩 **Scalability**: Suitable for wider bit-width adders
- 🧱 **Modularity**: Can be chained for 8-bit, 16-bit, or 32-bit addition

---

## ⚠️ Tradeoffs

- 🧮 **Gate Count**: Requires more gates than ripple carry
- 🧠 **Complexity**: Carry logic grows with bit-width
- 🔋 **Power**: Higher power consumption due to parallel logic

---
