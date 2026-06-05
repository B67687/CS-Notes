---
title: "🔌 How to use `wire`"
date: 2025-11-08
draft: false
---

{{< callout type="info" >}}
**Information**
`wire` declares a **combinational signal** — a continuously driven connection between logic elements.  

It models a **physical wire** or **net** in hardware.
{{< /callout >}}
---

### 🔁 Key Properties
- **No storage**: `wire` holds no state.
- **Continuously driven**: Must be assigned via `assign` or module outputs.
- **Fan-out allowed**: One `wire` can feed multiple destinations.
- **Fan-in restricted**: Only one driver unless explicitly resolved (e.g., tri-state).

---

### ✅ Usage Example
```verilog
wire a, b, y;

assign a = in1 & in2;
assign b = in3 | in4;
assign y = a ^ b;
```

- `a`, `b`, and `y` are **combinational signals**.
- Each is driven by a single expression.
- They can be read by multiple downstream logic blocks.

---

### ⚠️ Restrictions
- ❌ Cannot be assigned inside `always` blocks.
- ❌ Cannot store values across clock cycles (use `reg` or `logic` for that).

---

### 🧩 Rule of Thumb
> Use `wire` for **pure signal flow** — when you want to connect logic, not store state.
