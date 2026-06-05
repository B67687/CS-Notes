---
title: "🔍 Implicit Nets in Verilog"
date: 2025-11-08
draft: false
---


Verilog **silently creates `wire` nets** when you reference undeclared signals.
- This leads to:
  - ❌ Width mismatches
  - ❌ Simulation/synthesis drift
  - ❌ Onboarding confusion

### Example:
```verilog
assign b = a;  // 'b' is undeclared → Verilog creates wire b implicitly
```

### Patch:
```verilog
`default_nettype none  // ✅ Prevents implicit net creation
```

> ✅ This is a **patch**, not a fix — the language still allows the behavior unless explicitly disabled.

---

## 🧩 Why Verilog Allowed It

| Reason              | Rationale                                 |
|---------------------|--------------------------------------------|
| Netlist-first design| Wires were assumed from schematics         |
| Speed over safety   | Quick modeling > strict typing             |
| Legacy inertia      | Old tools and IP rely on it                |
| Minimalist spec     | Fewer rules, more freedom                  |

---

## ✅ SystemVerilog: The Fix

SystemVerilog is the **modern HDL** that **fills the hole** Verilog left open.

### Key Improvements:
- **No implicit nets** by default
- **Strong typing**: `logic`, `bit`, `int`, `struct`, `enum`
- **Unified assignment semantics**: `logic` replaces `reg`/`wire` confusion
- **Native support for**:
  - Interfaces
  - Assertions
  - Multidimensional arrays
  - Classes and OOP constructs

### Example:
```systemverilog
logic [3:0] a;
assign a = 4'b1010;  // ✅ Explicit, safe, typed
```