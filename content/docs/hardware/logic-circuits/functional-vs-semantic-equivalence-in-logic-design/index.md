---
title: "🧠 Functional vs Semantic Equivalence in Logic Design"
date: 2025-11-08
draft: false
---

Functional equivalence tells you two designs compute the same Boolean function; semantic equivalence tells you their signals mean the same thing (polarity, assertion, interface). Hardware breaks when we conflate the two.

---

## 🧩 Concepts and Definitions

- **Boolean function:** Maps inputs to outputs regardless of naming or polarity. Example:
  
$$
F = (A \lor \overline{C}) \land (\overline{B} \lor D)
$$


- **Signal polarity and assertion:**
  - **Active-high signal X:** Asserted when 
$$
X = 1
$$
. No bubble at the pin.
  - **Active-low signal X\*:** Asserted when 
$$
X = 0
$$
. Bubble at the pin. Algebraically, treat 
$$
X^*
$$
 as 
$$
\overline{X}
$$
.

- **Bubble logic convention:**
  - **Bubble on input:** The gate internally inverts that pin before applying its operation.
  - **Bubble on output:** The output is inverted relative to the gate’s core operation.
  - **Bubble-matching rule:** Bubbles should connect to bubbles when chaining inverted polarities, preserving semantic readability.

- **Interface contract:**
  - **What it encodes:** Polarity, assertion level, legal voltage ranges, timing, reset sense.
  - **Why it matters:** Violating the contract can be functionally fine in isolation but unsafe, misleading, or error-prone in systems.

---

## 🔧 Canonical Example: Translating Mixed Polarity Spec to Bubble-Correct Schematic

- **Spec (verbal):** F\* is asserted only when either A or C\* is asserted, and either B or D\* is negated.
- **Translate to logic conditions:**
  - Either A or C\* asserted → 
$$
A = 1
$$
 or 
$$
C = 0
$$
 → 
$$
A \lor \overline{C}
$$

    - Either B or D\* negated → 
$$
B = 0
$$
 or 
$$
D = 1
$$
 → 
$$
\overline{B} \lor D
$$

- **Active-high function:**
  
$$
F = (A \lor \overline{C}) \land (\overline{B} \lor D)
$$


- **Active-low output:**
  
$$
F^* = \overline{F} = \overline{(A \lor \overline{C}) \land (\overline{B} \lor D)}
$$


- **Bubble-matched realization:**
  - OR1: A (non-bubble) + C (bubble input) → 
$$
A \lor \overline{C}
$$

  - OR2: B (bubble input) + D (non-bubble) → 
$$
\overline{B} \lor D
$$

  - AND gate with bubble output → 
$$
F^*
$$

  - ✅ Semantic clarity preserved

- **Functionally correct but semantically noisy variant:**
  - NAND gate with non-bubble inputs → computes 
$$
F^*
$$
 but violates bubble matching
  - ❌ Fails semantic audit

---

## 🔄 Transformation Recipes: Preserve Function While Switching Semantics

- **De Morgan’s Laws:**
  
$$
\overline{X \land Y} = \overline{X} \lor \overline{Y}
$$

  
$$
\overline{X \lor Y} = \overline{X} \land \overline{Y}
$$


- **Polarity flips:**
  - Flip input sense → add bubble + rename net
    Flip output sense → push inversion through using De Morgan

- **Gate family normalization:**
  - All-NAND: push bubbles to inputs, use NANDs with bubble outputs
  - All-NOR: push bubbles to outputs, use NORs with bubble inputs

- **Equivalence proof sketch:**
  
$$
F^* = \overline{(A \lor \overline{C}) \land (\overline{B} \lor D)}
$$

  Apply De Morgan:
  
$$
F^* = \overline{A \lor \overline{C}} \lor \overline{\overline{B} \lor D} = (\overline{A} \land C) \lor (B \land \overline{D})
$$

  ✅ Functionally equivalent, semantically shifted

---

## 🧪 Audit Checklist and Semantic Flags

| Audit Layer | Criteria | Pass/Fail |
|-------------|----------|-----------|
| Polarity | Bubbles match signal names (e.g. C\* has bubble) | ✅/❌ |
| Bubble Matching | Outputs of gates match input bubbles | ✅/❌ |
| Functional Logic | Boolean expression matches spec | ✅ |
| Interface Contract | Signal names, bubbles, and assertion levels align | ✅/❌ |

**Semantic Flags:**

- **S1:** Bubble mismatch at module boundary
- **S2:** Active-low net drawn without bubble
- **S3:** Asterisk naming disagrees with pin bubble
- **S4:** Output sense incorrect (F vs F\*)

---

## ⚠️ Pitfalls and Remedies

- **Pitfall:** Treating bubbles as cosmetic
  **Remedy:** Enforce interface contracts

- **Pitfall:** Hiding inversions inside logic
  **Remedy:** Pull to boundaries using De Morgan

- **Pitfall:** Mixed gate families causing stranded polarity
  **Remedy:** Normalize to NAND/NOR, restore bubbles at interfaces

- **Pitfall:** Renaming without updating symbols
  **Remedy:** Rename + redraw bubbles consistently

---

## 🧠 Practice Prompts

- **P1:** Given 
$$
F = (\overline{X} \lor Y) \land (Z \lor \overline{W})
$$
, draw bubble-matched schematic with 
$$
F^*
$$
 output
- **P2:** From 
$$
F^* = \overline{A \land \overline{B}}
$$
, draw all-NAND and bubble-matched OR-AND version
- **P3:** Convert 
$$
F^* = \overline{P \lor \overline{Q}}
$$
 into NOR-centric schematic

**Answer Sketches:**

- **P1:** 
$$
F^* = \overline{(\overline{X} \lor Y) \land (Z \lor \overline{W})} = (X \land \overline{Y}) \lor (\overline{Z} \land W)
$$

- **P2:** 
$$
F^* = \overline{A \land \overline{B}} = \overline{A} \lor B
$$

- **P3:** 
$$
F^* = \overline{P \lor \overline{Q}} = \overline{P} \land Q
$$

