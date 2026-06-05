---
title: "🧠 Truth Tables"
date: 2025-11-08
draft: false
---


Truth tables are used to represent the output of logical expressions for all possible input combinations. Each row corresponds to a unique input state, and the columns show the resulting output.

---

## 🔤 Notation Legend

| Symbol | Meaning                  |
|--------|--------------------------|
| `¬A`   | NOT A (negation)         |
| `A ∧ B`| A AND B (conjunction)    |
| `A ∨ B`| A OR B (disjunction)     |
| `A ⊕ B`| A XOR B (exclusive OR)   |
| `A → B`| A IMPLIES B              |
| `A ↔ B`| A IFF B (biconditional)  |

---

## ✅ Basic Truth Tables

### 1️⃣ NOT (Negation)

| A | ¬A |
|---|----|
| 0 | 1  |
| 1 | 0  |

### 2️⃣ AND (Conjunction)

| A | B | A ∧ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |

### 3️⃣ OR (Disjunction)

| A | B | A ∨ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   1   |

### 4️⃣ XOR (Exclusive OR)

| A | B | A ⊕ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   0   |

---

## 🔁 Compound Expressions

### Example: `(A ∧ B) ∨ ¬C`

| A | B | C | A ∧ B | ¬C | (A ∧ B) ∨ ¬C |
|---|---|---|--------|----|--------------|
| 0 | 0 | 0 |   0    |  1 |      1       |
| 0 | 0 | 1 |   0    |  0 |      0       |
| 0 | 1 | 0 |   0    |  1 |      1       |
| 0 | 1 | 1 |   0    |  0 |      0       |
| 1 | 0 | 0 |   0    |  1 |      1       |
| 1 | 0 | 1 |   0    |  0 |      0       |
| 1 | 1 | 0 |   1    |  1 |      1       |
| 1 | 1 | 1 |   1    |  0 |      1       |

---

## 🧩 Tips for Building Truth Tables

- List all input combinations using binary counting.
- Compute intermediate columns for sub-expressions.
- Use consistent notation and spacing for clarity.
- Highlight final output column for emphasis.

Check: [📊 Base‑b Recursive Listing Method](../baseb-recursive-listing-method/)

---

## 🧮 Expandable Framework

To add more operators or multi-bit logic, duplicate the table structure and extend with additional columns. For example:

- NAND: `¬(A ∧ B)`
- NOR: `¬(A ∨ B)`
- XNOR: `¬(A ⊕ B)`
- Majority: `(A ∧ B) ∨ (A ∧ C) ∨ (B ∧ C)`

---

## 🧠 Set-Theoretic Analogy (Optional)

- `A ∧ B` → Intersection: $ A \cap B $
- `A ∨ B` → Union: $ A \cup B $
- `¬A` → Complement: $ A^c $
- `A ⊕ B` → Symmetric Difference: $ A \triangle B $

---
