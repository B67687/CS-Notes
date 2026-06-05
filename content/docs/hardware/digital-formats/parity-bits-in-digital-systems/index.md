---
title: "🧮 Parity Bits in Digital Systems"
date: 2025-11-08
draft: false
---


## 🧠 Motivation

> [!Why we invented this]
> Parity bits offer a lightweight method for **error detection** in digital communication and storage.
>
> By encoding the **evenness or oddness** of 1s in a binary word, parity bits help verify data integrity without heavy computational overhead.

---

## 🔣 What Is a Parity Bit?

A **parity bit** is an extra bit appended to a binary word to encode whether the total number of 1s is **even** or **odd**.

- ✅ **Even Parity**: Parity bit is set so that the total number of 1s (including the parity bit) is even.
- 🧨 **Odd Parity**: Parity bit is set so that the total number of 1s (including the parity bit) is odd.

---

## 📊 Examples

| Data Bits | Even Parity Bit | Odd Parity Bit |
|-----------|------------------|----------------|
| `1010`    | `0`              | `1`            |
| `1101`    | `1`              | `0`            |
| `1001`    | `0`              | `1`            |

---

## ⚙️ How Parity Is Computed

### 🔧 XOR Method (Efficient)

Parity bit = XOR of all data bits

For 8-bit data:

```text
P = D₀ ⊕ D₁ ⊕ D₂ ⊕ D₃ ⊕ D₄ ⊕ D₅ ⊕ D₆ ⊕ D₇
```

- Even parity: use result directly
- Odd parity: invert the result

### 🧮 Counting Method (Conceptual)

Count the number of 1s:

- If even → parity bit = 0 (for even parity)
- If odd → parity bit = 1 (for even parity)

---

## 🧷 Visual Anchor: XOR Cascade for 8-bit Parity

```text
D₀ ─┬─ XOR ─┬─ XOR ─┬─ XOR ─┬─ XOR ─┬─ XOR ─┬─ XOR ─┬─ XOR ─► Parity Bit
    │       │       │       │       │       │       │
    D₁      D₂      D₃      D₄      D₅      D₆      D₇
```

---

## 🛡️ Error Detection Using Parity

### ✅ Detection Steps

1. Generate parity bit at sender
2. Transmit data + parity bit
3. Receiver recomputes parity from received data
4. Compare with received parity bit

### ⚠️ Limitations

- Can detect **odd bitflips**
- Cannot detect **even bitflips**
- Cannot **correct** errors—only detect
