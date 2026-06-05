---
title: "🧵 Gray Codes"
date: 2025-11-08
draft: false
---


**Unit-distance codes** are where numbers in a number system steps by a fixed number of place-values

**Gray codes** is one particular unit-distance code that works in binary sequences, where only one bit changes between consecutive values.

This minimizes ambiguity in digital transitions, simplifies Karnaugh map adjacency, and reduces error in hardware systems like rotary encoders and ADCs.

---

## Canonical Gray Code (Reflected Binary)

Definition:
A sequence of 2^n binary numbers where each successive value differs from the previous by exactly one bit.

Recursive Generation:

1. Start with 1-bit codes: 0, 1
2. Reflect the sequence
3. Prefix original with 0, reflected with 1

Example (3-bit):

```text
000
001
011
010
110
111
101
100
```

Refer to [ Derivation of Reflected Binary Form](../gray-code-reflected-form/)

---

## Binary to Gray Conversion

Given binary B = b₂ b₁ b₀, Gray code G = g₂ g₁ g₀ is:

```text
g₂ = b₂
g₁ = b₂ XOR b₁
g₀ = b₁ XOR b₀
```

Example:
Binary 101 → Gray 111

---

## Variants of Gray Code

| Variant                  | One-Bit Change | Wraparound | Balanced | Parity | Use Case                     |
|--------------------------|----------------|------------|----------|--------|------------------------------|
| Reflected Binary (BRGC)  | Yes            | Optional   | No       | No     | K-maps, logic simplification |
| Circular Gray Code       | Yes            | Yes        | No       | No     | Rotary encoders              |
| Balanced Gray Code       | Yes            | No         | Yes      | No     | EMI-sensitive hardware       |
| Monotonic Gray Code      | Yes            | No         | No       | No     | ADCs, niche logic            |
| Non-Reflected Gray Code  | Yes            | No         | No       | No     | Custom logic, puzzles        |
| Gray Code with Parity    | Yes            | No         | No       | Yes    | Communication systems        |

---

## Use in Karnaugh Maps

Gray code ordering ensures adjacent cells differ by one variable, enabling:

- Safe variable elimination
- Visual grouping of minterms
- Simplified Boolean expressions

---

## Generator Logic (Reflected Binary)

```python
def generate_gray(n):
    if n == 0:
        return ['']
    prev = generate_gray(n - 1)
    return ['0' + x for x in prev] + ['1' + x for x in reversed(prev)]
```

---

## Semantic Implications

- Adjacency: Guarantees logical proximity in K-maps
- Auditability: One-bit transitions simplify error tracing
- Hardware Safety: Reduces glitches in physical transitions

---

## Suggested Extensions

- Map Gray code sequences to truth table rows
- Benchmark adjacency graphs for each variant
- Scaffold parity-enhanced Gray codes for fault-tolerant systems
