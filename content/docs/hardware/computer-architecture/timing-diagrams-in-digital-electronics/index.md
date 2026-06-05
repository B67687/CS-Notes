---
title: ⏱ Timing Diagrams in Digital Electronics
date: 2025-11-08
draft: false
---

## 📜 Overview

A **timing diagram** is a graphical representation of the relationship between **digital signals** over time.
It shows when signals change from HIGH (`1`) to LOW (`0`) and how those transitions relate across multiple signals.

Timing diagrams are essential for:

- Understanding **sequential logic** behavior.
- Debugging signal interactions.
- Designing and verifying circuit timing requirements.

---

## 🧩 Components of a Timing Diagram

| Element                  | Description |
|--------------------------|-------------|
| **Time axis**            | Horizontal line showing time progression → left to right. |
| **Signal lines**         | Horizontal tracks for each signal (e.g., `CLK`, `DATA`, `ENABLE`). |
| **Logic levels**         | `HIGH` (1) is usually the upper position, `LOW` (0) is the lower position. |
| **Transitions**          | Vertical edges showing changes between logic levels. |
| **Pulse width**          | Duration a signal stays HIGH or LOW. |
| **Setup time**           | Time before the clock edge when data must be stable. |
| **Hold time**            | Time after the clock edge when data must remain stable. |
| **Propagation delay**    | Time taken for a change in input to reflect at the output. |

---

## ⏳ Example — Basic Clock & Data Relationship

**Clock signal (CLK) and data signal (D):**
