---
title: "⏱ Clock Cycles and Sequential Circuit Updates"
date: 2025-11-08
draft: false
---

This note attempts to explain **clock cycles**, and how it is used in **sequential circuits**

## 🔧 What Is a Clock Cycle?

A **clock cycle** is the fundamental timing unit in digital systems, especially **sequential circuits**. It defines the rhythm at which state changes (updates) are allowed to occur.

- **Clock signal**: A periodic square wave alternating between high and low.
- **Rising edge**: Transition from low to high.
- **Falling edge**: Transition from high to low.
- **Edge-triggered circuits**: Most sequential elements (like flip-flops) update their state **only on a specific edge**—usually the rising edge.

---

## 🔁 Update-and-No-Update Cycle

This cycle defines when updates are allowed and when they are ignored:

| Phase            | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Update phase** | On the triggering edge, the circuit samples inputs and updates its state.   |
| **No-update**    | Between edges, the state is held constant—no updates occur.                 |

Any signal changes that happen **between edges** are ignored unless they persist until the next triggering edge. Fast transients or glitches are missed.

---

## ⚡ Clock Speed and Update Rate

- **Clock frequency** (e.g., 3 GHz) = number of cycles per second.
- **Higher frequency** = shorter cycle period = **more updates per second**.
- This enables faster processing—more instructions or state transitions per unit time.

### ⚠️ Stability Caveat

- Signals must **settle** before the next edge.
- If not, you risk **setup/hold violations** or **metastability**.

---

## 🧠 Summary

> **Sequential circuits synchronize state updates to clock edges. The clock cycle defines the temporal resolution of valid updates**
>
> **Transients faster than the cycle period are ignored, and higher clock frequencies enable more frequent state transitions—provided signal stability is maintained**
