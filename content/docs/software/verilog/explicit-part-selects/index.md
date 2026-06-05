---
title: "🪢 Explicit Part-Selects"
date: 2025-11-08
draft: false
---

{{< callout type="info" >}}
**TL:DR**
A **part-select** extracts or assigns a contiguous slice of bits from a vector.  
Syntax: `vector[high:low]` — must match the **direction** of the declaration.
{{< /callout >}}
---

## ✅ Why Use Explicit Part-Selects?

| Benefit               | Description                                      |
|------------------------|--------------------------------------------------|
| 🧩 Symbolic trace clarity | Makes bit ranges visible and auditable           |
| 📚 Onboarding-friendly  | Easier for new readers to follow intent          |
| 🔐 Refactor-safe        | Protects against silent errors if widths change |
| 🧠 Directional safety   | Enforces correct slicing semantics               |

---

## 🧩 Examples of Explicit Part-Selects

### ✅ Extracting a slice
```verilog
wire [15:0] word;
wire [3:0] nibble;

assign nibble = word[11:8];  // ✅ Extract middle nibble
```

### ✅ Assigning to a slice
```verilog
reg [15:0] word;
reg [3:0] nibble;

assign word[11:8] = nibble;  // ✅ Overwrite middle nibble
```

### ✅ Safe inversion with part-select
```verilog
input  [2:0] a, b;
output [5:0] out_not;

assign out_not[2:0] = ~a[2:0];  // ✅ Invert a explicitly
assign out_not[5:3] = ~b[2:0];  // ✅ Invert b explicitly
```

---

## ⚠️ Common Pitfall: Implicit Width Assumptions

```verilog
assign out_not[2:0] = ~a;  // ⚠️ Relies on knowing a is [2:0]
```

- Works if `a` is `[2:0]`, but less explicit
- Risky if `a` changes width later

---

## 🧠 Directional Reminder

### Declaration
```verilog
wire [0:7] data;  // Ascending index
```

### Legal part-select
```verilog
data[0:3];  // ✅ Matches declaration direction
```

### Illegal part-select
```verilog
data[3:0];  // ❌ Direction mismatch
```