---
title: "🔗 Fan-Out"
date: 2025-11-08
draft: false
---

In digital systems, one output pin often connects to **multiple input pins**—for example, a clock signal distributed to several flip-flops. But every input draws a small amount of current, and every output has a limit to how much current it can source or sink.

> [!note] Fan-Out
> Fan-out defines the **maximum number of inputs** that a single output can drive **without violating voltage thresholds**

---

## ⚙️ Fan-Out Depends on Current Thresholds

To calculate fan-out, we compare:

| Role       | Symbol         | Meaning |
|------------|----------------|---------|
| **Output** | $I_{OH}$, $I_{OL}$ | Max current the output can source/sink while maintaining valid voltage |
| **Input**  | $I_{IH}$, $I_{IL}$ | Current drawn by each input when HIGH or LOW |

---

### 🔹 Fan-Out Formula

For HIGH signals:

$$
\text{Fan-out}_{\text{HIGH}} = \left\lfloor \frac{I_{OH(\text{max})}}{I_{IH(\text{max})}} \right\rfloor
$$

For LOW signals:

$$
\text{Fan-out}_{\text{LOW}} = \left\lfloor \frac{I_{OL(\text{max})}}{I_{IL(\text{max})}} \right\rfloor
$$
> The final fan-out is the **minimum** of these two values.

---

## 🧠 Why Fan-Out Matters

- Ensures output voltage stays within valid HIGH/LOW thresholds
- Prevents signal degradation due to excessive loading
- Critical for bus design, clock distribution, and logic tree fan-in

---

## 📜 Typical Values (TTL vs CMOS)

| Logic Family | \( I_{OH} \) | \( I_{IH} \) | Fan-out |
|--------------|--------------|--------------|---------|
| **TTL**      | ~400 µA      | ~40 µA       | ~10     |
| **CMOS**     | ~1 mA        | ~1 µA        | ~1000+  |

> CMOS has much higher fan-out due to lower input current draw
