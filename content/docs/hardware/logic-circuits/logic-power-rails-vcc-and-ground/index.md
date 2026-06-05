---
title: "🔌 Logic Power Rails — Vcc and Ground"
date: 2025-11-08
draft: false
---


### 🧠 What Are Vcc and GND?

- **Vcc** is the **positive voltage supply** for a logic device.
- **GND** (Ground) is the **reference point (0V)** where current returns or drains.
- Together, they form the **power rails** that energize digital logic circuits.

### 🔍 Why Is It Called Vcc?

- **Vcc** stands for **Voltage at the Common Collector**.
- Originates from **BJT (bipolar junction transistor)** circuits:
  - In NPN transistors, the **collector** is connected to the positive rail.
- Over time, Vcc became a general label for the **positive supply** in digital systems.

### ⚡ Related Voltage Labels

| Label | Stands For              | Used In              |
|-------|--------------------------|----------------------|
| Vcc   | Voltage at Common Collector | BJT (positive rail) |
| Vee   | Voltage at Common Emitter   | BJT (negative rail) |
| Vdd   | Voltage at Drain            | FET (positive rail) |
| Vss   | Voltage at Source           | FET (ground rail)   |

### 🧩 Semantic Roles

- **Vcc** defines **logic high (1)**
- **GND** defines **logic low (0)**
- These rails set the **binary voltage boundaries** for digital logic evaluation.

### ✅ Summary

- Every logic device needs a pair of **Vcc and GND** to operate.
- Without power rails, logic gates are electrically inert.
- Vcc and GND are foundational to all digital logic families (TTL, CMOS, etc.)
