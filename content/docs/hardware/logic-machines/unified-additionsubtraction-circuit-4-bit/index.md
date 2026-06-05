---
title: "🧮 Unified Addition–Subtraction Circuit (4-bit)"
date: 2025-11-08
draft: false
---

A **unified adder-subtractor** circuit performs both binary addition and subtraction using a single chain of full adders. Instead of building separate units for each operation, it uses **polarity control** to transform subtraction into addition through **conditional inversion** and a **$+1$ bias**.

---

## 🧮 Core Insight

Subtraction in binary is defined as:

$$
A - B = A + (\sim B + 1)
$$

This is called **two’s complement subtraction**, where:
- $\sim B$ is the **bitwise NOT** of $B$ (1’s complement)
- Adding $1$ completes the transformation into two’s complement

---

## ⚙️ Circuit Architecture

The unified circuit uses:

- **XOR gates** to conditionally invert each bit of $B$
- A **control signal** `Add/Sub` to select operation mode
- The same control signal as the **initial carry-in** to add the $+1$ for subtraction

### 🔧 XOR as Conditional Inverter

Each XOR gate computes:

$$
B_i \oplus S
$$

Where:
- $B_i$ is the $i$-th bit of operand $B$
- $S$ is the `Add/Sub` control signal

| Operation | $S$ | XOR Output |
|-----------|-----|-------------|
| Add       | 0   | $B_i$       |
| Subtract  | 1   | $\sim B_i$  |

### 🔧 Carry-in as $+1$ Bias

The same control signal $S$ is fed into the **least significant full adder** as the initial carry-in:

| Operation | Carry-in |
|-----------|-----------|
| Add       | 0         |
| Subtract  | 1         |

This adds the $+1$ needed for two’s complement subtraction.

---

## 🧠 Why It Works

When $S = 1$, the circuit computes:

$$
A + (\sim B + 1) = A - B
$$

When $S = 0$, it computes:

$$
A + B
$$

So the same adder chain handles both operations with no structural changes—just a polarity shift.

---

## 🧮 Symbolic Flow

```text
          x₃ x₂ x₁ x₀     ← Operand A
           │  │  │  │
           ▼  ▼  ▼  ▼
          FA FA FA FA     ← Full Adders
           ▲  ▲  ▲  ▲
           │  │  │  │
     y₃ y₂ y₁ y₀          ← Operand B
      \  \  \  \  
      XOR XOR XOR XOR     ← Conditional Inversion
       /   /   /   /
     Add/Sub (S)          ← Control signal
           │
         Carry-in         ← Also feeds FA₀
```

---

## ✅ Advantages

| Feature             | Benefit                          |
|---------------------|----------------------------------|
| Hardware reuse      | One adder chain for both ops     |
| Gate efficiency     | XOR gates are compact and fast   |
| Branchless logic    | No switching between units       |
| Conceptual clarity  | Subtraction is just inverted addition |

---

## 🧠 Philosophical Insight

> Subtraction is not a separate operation—it’s **addition under inverted polarity**.

This design reflects the deep symmetry of binary arithmetic, where polarity control unifies seemingly distinct operations.
