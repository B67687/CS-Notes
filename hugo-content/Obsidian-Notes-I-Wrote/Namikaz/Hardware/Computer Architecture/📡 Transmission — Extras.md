---
title: "📡 Transmission — Extras"
date: 2025-11-08
draft: false
---

## 🧩 Framing

- **📝 Definition:**
  Adding extra bits or patterns to a data packet so the receiver knows:
  - 🔓 Where the data starts
  - 🛑 Where it ends
  - 📏 Sometimes extra info like packet length or error checks

- **💡 Example (asynchronous):**
  A UART byte might be framed like this:

```
⏱ Start bit | 📦 Data bits | ✅ Parity bit (optional) | 🛑 Stop bit(s)
```

- This ensures the receiver can lock onto each byte without a shared clock

- **📉 Framing overhead:**
These extra bits do not carry payload data, so they reduce overall efficiency.

---

## 🔗 Multi-drop

- **📝 Definition:**
A communication bus where multiple devices share the same physical set of wires, and any device can communicate (one at a time).

- **🔌 Examples:**
- 🧠 **I²C**: Many sensors and controllers share the same clock and data lines
- 🏭 **RS-485**: Multiple industrial controllers on one twisted-pair cable

- **📌 Key point:**
Only one device “drives” the bus at a time, others remain idle.

- 🪝 Called *multi-drop* because the cable is like a long backbone with “drops” to multiple devices.

---

## ⏰ Phase-Locked Loop (PLL)

- **📝 Definition:**
An electronic circuit that locks the phase and frequency of a local oscillator to a reference signal.

- **📡 In data transmission:**
- 🔄 Adjusts the receiver’s internal clock to align with the sender’s bit timing
- 🧭 Compensates for clock drift and jitter to keep sampling accurate

- **👣 Analogy:**
Like running next to someone and adjusting your stride to match their footsteps — you stay in sync without a fixed schedule.
