---
title: "🔗 Noise Margin"
date: 2025-11-08
draft: false
---

Digital signals travel across wires, buses, and PCB traces—but the real world is noisy. Voltage levels can fluctuate due to:

- Crosstalk from nearby signals
- Power supply ripple
- Electromagnetic interference
- Capacitive loading and reflections

Even if a signal is meant to be HIGH or LOW, it might **degrade** in transit. We need a way to **absorb imperfections** without misinterpreting the signal.

{{< callout type="default" >}}
**Noise Margin**
Noise margin defines how much **voltage error** a signal can tolerate **without flipping its logical meaning**
{{< /callout >}}
---

## ⚙️ Noise Margin Depends on Voltage Thresholds

We calculate noise margin by comparing:

- What the **output guarantees**
- What the **input requires**

| Margin Type       | Formula                          | Meaning |
|-------------------|----------------------------------|---------|
| **High-side margin** | $NM_H = V_{OH} - V_{IH}$ | How much HIGH signal can degrade before being misread |
| **Low-side margin**  | $NM_L = V_{IL} - V_{OL}$ | How much LOW signal can rise before being misread |

> These margins define **safe zones** between output and input thresholds
>
> The final **noise margin** is the **minimum** of these two values.

---

## 🧠 Why Noise Margin Matters

- Prevents misinterpretation due to voltage droop or spikes
- Ensures reliable logic even in electrically noisy environments
- Allows interoperability across devices with different drive strengths
- Critical for long traces, high-speed buses, and mixed-voltage systems
