---
title: "⚡ TTL and CMOS"
date: 2025-11-08
draft: false
---

We already understand how **[ transistors](../transistors/)** work as switches . Now we ask:

> ❓ Why do we need logic families like **TTL** and **CMOS**?

---

## ✅ What Do Logic Gates Need?

To build reliable digital systems, logic gates must:

| Requirement                 | Why It Matters                                                                 |
|----------------------------|--------------------------------------------------------------------------------|
| **Clear HIGH/LOW states**  | So 1s and 0s are unambiguous and noise-resistant                              |
| **Default output behavior**| So outputs don’t “float” when inputs are disconnected or undefined             |
| **Fast switching**         | So logic operations happen quickly                                            |
| **Low power consumption**  | Especially important for battery-powered or high-density systems              |
| **Scalability**            | So we can build millions of gates on a single chip                            |

---

## 🔌 Pull-Up and Pull-Down: Default State Control

{{< callout type="info" >}}
**Why Pull-Up / Pull-Down?**
Transistors don’t “know” what to output unless we **define a default**.

- **Pull-Up**: Ensures output defaults to **HIGH** when not actively pulled LOW
- **Pull-Down**: Ensures output defaults to **LOW** when not actively pulled HIGH
{{< /callout >}}
Using **resistors** for this is slow and power-hungry. So we use **transistors** to actively pull HIGH or LOW.

---

## ⚙️ TTL——Using BJTs for Logic

TTL uses **BJTs** to:

- Pull outputs `HIGH` or `LOW`
- Amplify and switch signals
- Provide default states via **internal transistor configurations**

{{< callout type="warning" >}}
TTL **always draws current**, even when idle, due to **base current** in BJTs
{{< /callout >}}
---

## ⚡ CMOS——Using Complementary MOSFETs

CMOS uses **both nMOS and pMOS** transistors:

| Role         | Transistor | Behavior                                  |
|--------------|------------|-------------------------------------------|
| Pull-Up      | **pMOS**   | Conducts when input is LOW → output HIGH  |
| Pull-Down    | **nMOS**   | Conducts when input is HIGH → output LOW  |

{{< callout type="info" >}}
**Complementary Action**
- Only **one transistor conducts at a time**
- No direct path from `VDD` to `GND`
- **No static power draw** when idle
- **Fast switching** via electric fields
{{< /callout >}}
This is why CMOS is called **Complementary**—it uses **both types** of MOSFETs to define output behavior.

---

## 🧠 Analogy: Logic Gates as Tug-of-War

Imagine the output wire is a rope:

- **TTL**: One team (BJTs) is always pulling. Even when idle, someone’s tugging.
- **CMOS**: Two teams (nMOS and pMOS) take turns. Only one pulls at a time. When neither pulls, the rope stays still—no energy wasted.

---

## 🧩 Summary

| Feature               | TTL (BJT)                      | CMOS (MOSFET)                    |
|-----------------------|--------------------------------|----------------------------------|
| Default Behavior      | Achieved via BJT configuration | Achieved via complementary action |
| Pull-Up / Pull-Down   | Done with BJTs                 | Done with pMOS / nMOS pair       |
| Power Usage           | Constant                       | Only during switching            |
| Switching Speed       | Fast                           | Very Fast                        |
| Scalability           | Limited                        | Excellent                        |
