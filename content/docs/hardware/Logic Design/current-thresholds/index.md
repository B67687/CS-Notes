---
title: "🧱 Current Thresholds"
date: 2025-11-08
draft: false
---

In digital electronics, current thresholds define how much **electrical current** a device can **source**, **sink**, or **tolerate** at its input or output pins. While voltage thresholds determine **signal interpretation**, current thresholds govern **physical drive strength and loading limits**.

{{< callout type="default" >}}
**Setting Boundaries**
To ensure safe and reliable operation, we define **current thresholds** for input and output pins:
> How much **current** an output can safely **source** or **sink**
> How much **current** an input can safely **draw** or **leak**
{{< /callout >}}
---

## 🧭 Naming Convention

Each label follows the format:

$I_{XY} (B)$

Where:

$I$ = Current

$X$ = Signal type
> **I** = Input
> **O** = Output

$Y$ = Direction
> **H** = Source (current flows **out**)
> **L** = Sink (current flows **in**)

$B$ = Bound type
> **max** = Maximum safe current  
> **min** = Minimum guaranteed current (rarely used)

---

## ⚙️ Table of Current Thresholds

These thresholds define how much current a digital device can **handle or deliver** at its pins. They are critical for ensuring that outputs can drive loads and inputs are not overloaded.

| Threshold       | Interpretation Logic                          |
|----------------|----------------------------------------------|
| $I_{IL}$<br>(max) | **Maximum** current allowed into input when LOW voltage is applied |
| $I_{IH}$<br>(max) | **Maximum** current allowed into input when HIGH voltage is applied |
| $I_{OL}$<br>(max) | **Maximum** current the output can **sink** while maintaining LOW voltage |
| $I_{OH}$<br>(max) | **Maximum** current the output can **source** while maintaining HIGH voltage |

> These thresholds define **electrical stress limits**, not logic levels.
> Exceeding them can cause voltage droop, signal distortion, or permanent damage.

---

## 🧠 What Do “Source” and “Sink” Mean?

| Direction | Current Flow | Typical Role |
|-----------|--------------|--------------|
| **Source** | Current flows **out of the pin** | Output driving HIGH |
| **Sink**   | Current flows **into the pin**   | Output pulling LOW or input loading |

- **Output HIGH** → sources current to downstream load
- **Output LOW** → sinks current from downstream load
- **Input pins** → draw small leakage or bias currents depending on voltage level
