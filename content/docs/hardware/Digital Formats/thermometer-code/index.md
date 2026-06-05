---
title: "🌡️ Thermometer Code"
date: 2025-11-08
draft: false
---

**Thermometer code** is a **unary-style binary encoding** where the number of active bits (1s) directly represents the value

It resembles a rising column in a thermometer——more 1s mean a higher value——thusly named

{{< callout type="info" >}}
**Notes**

Thermometer code is not unary in the **purist** way since it uses 0s, but it still **counts in unary**, thusly named **unary-style**

It always counts in one direction, either up or down i.e. **monotonic**.
Thus, there is no such thing as `0s` appearing between `1s`

Application is in **fast, simple comparisons** and **analog signal quantization**
{{< /callout >}}
---

## 📘 Definition
>
> A binary vector where the first $N$ bits are $1$, and the remaining bits are $0$, representing the value $N$.

- The 1s form a **contiguous block** at the start.
- There are **no 0s between 1s**—gaps are invalid.

| Value | Thermometer Code |
|--------|------------------|
| 0      | `0000`           |
| 1      | `1000`           |
| 2      | `1100`           |
| 3      | `1110`           |
| 4      | `1111`           |

It can count up **in either direction**, left-to-right or right-to-left, it just has to count in a **single direction**
