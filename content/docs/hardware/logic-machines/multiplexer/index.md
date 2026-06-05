---
title: "🎛️ Multiplexer"
date: 2025-11-08
draft: false
---

A **multiplexer** (MUX) is a digital logic device that selects **one input from many** and routes it to a **single output**, based on control signal called a **selector**

The multiplexer itself can be **thought of as a "selector"**, although the one that actually selects the output is **within the multiplexer**

```mermaid
graph TD
  subgraph Inputs
    I0["I₀"]
    I1["I₁"]
    I2["I₂"]
  end

  subgraph Select Lines
    S0["S₀"]
    S1["S₁"]
  end

  subgraph Multiplexer
    MUX["MUX (4-to-1)"]
  end

  subgraph Output
    Y["Output Y"]
  end

  I0 --> MUX
  I1 --> MUX
  I2 --> MUX
  S0 --> MUX
  S1 --> MUX
  MUX --> Y
```

{{< callout type="info" >}}

- **Inputs:** $n$ binary signals
- **Output:** 1

[!example] Notes
MUX is often called a **data selector**.

Can be built using logic gates or hierarchical MUX trees.

In programming, MUX behavior resembles a **switch-case** or **if-else chain**
{{< /callout >}}
---

## ⚙️ Applications

- Data routing and bus control
- Function selection in ALUs
- Signal switching in communication systems
- Logic minimization and conditional operations
