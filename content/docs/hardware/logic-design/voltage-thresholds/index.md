---
title: "🧱 Voltage Thresholds"
date: 2025-11-08
draft: false
---

In digital electronics, we aim to represent binary information—`0` and `1`—using physical voltages.

Devices like logic gates, microcontrollers, and memory chips must **interpret incoming voltages** as either LOW (`0`) or HIGH (`1`) and **produce output voltages** that other devices can reliably understand.

However, real-world voltages are **not perfectly clean**:

- Signals may be affected by electrical noise, voltage drops, or slow transitions.
- Devices may operate at different voltage levels (e.g. 3.3V vs 5V logic).
- Without clear boundaries, a voltage like 1.5V could be misinterpreted—some devices might treat it as HIGH, others as LOW.

{{< callout type="default" >}}
**Setting Boundaries**
To solve this, we define **voltage thresholds** for either **input** or **output** signals
> Where we **start** interpreting the voltage as **high**
> Where we **stop** interpreting the voltage as **low**
{{< /callout >}}
---

## 🧭 Naming Convention

Each label follows the format:

$V_{XY} (B)$

Where:

$V$ = Voltage

$X$ = Signal type  
> **I** = Input
> **O** = Output

$Y$ = Qualifier
> **H** = High
> **L** = Low

$B$ = Bound type
> **min** = Minimum acceptable value
> **max** = Maximum acceptable value

---

## ⚙️ Table of Voltage Thresholds

These thresholds define how a digital device (e.g. inverter, gate, microcontroller) interprets and produces binary signals. Each threshold sets a boundary for what counts as a valid HIGH or LOW signal, either at the input or output.

| Threshold       | Interpretation Logic                          |
|----------------|-----------------------------------------------|
| $V_{IL}$<br>(max) | **Maximum** Voltage for **Input** to be interpreted as **Low** <br><br>|
| $V_{IH}$<br>(min) | **Minimum** Voltage for **Input** to be interpreted as **High** <br><br>|
| $V_{OL}$<br>(max) | **Maximum** Voltage for **Output** to be interpreted as **Low** <br><br>|
| $V_{OH}$<br>(min) | **Minimum** Voltage for **Output** to be interpreted as **High** <br><br>|

> These thresholds create buffer zones that absorb noise and ensure reliable communication between devices.
>
> Output thresholds are **stricter** than input thresholds to guarantee signal integrity

---

## ⚙️ Why Output Thresholds Are Stricter Than Input Threholds

### 🔹 For HIGH Signals

- The **output device** must produce a voltage **≥ $V_{\text{OH}}$**, which is **higher** than the minimum required by the input device $V_{\text{IH}}$
- This ensures that even if the signal **degrades** (e.g. due to resistance, noise, or capacitance), it still remains **above** the input’s threshold and is interpreted as HIGH.
- If the signal becomes **even higher**, that’s fine—it remains safely in the HIGH zone.

### 🔹 For LOW Signals

- The **output device** must produce a voltage **≤ $V_{\text{OL}}$**, which is **lower** than the maximum tolerated by the input device $V_{\text{IL}}$.
- This ensures that even if the signal **rises slightly** due to noise or leakage, it still remains **below** the input’s threshold and is interpreted as LOW.
- If the signal becomes **even lower**, that’s fine—it remains safely in the LOW zone.
