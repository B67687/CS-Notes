---
title: "📏 Inclusive Range Counting"
date: 2025-11-08
draft: false
---

> [!tip]
> The **difference between two numbers is exclusive** — it doesn’t count the starting point.  
> To include both endpoints, you must **add 1** if we took the *negative difference* or **subtract 1** if we took the *positive difference*

---

## 🧩 Examples

### Case 1: From 31 down to 24
```text
[31, 30, 29, 28, 27, 26, 25, 24]
```
- Difference: `31 - 24 = 7`
- ✅ Total count: `31 - 24 + 1 = 8`

---

### Case 2: Starting at 1, want 8 numbers
```text
[1, 2, 3, 4, 5, 6, 7, 8]
```
- Final number: `1 + 8 - 1 = 8`
- ✅ Range: `[1:8]` → total count = 8

---

## 🧠 Why This Matters in HDL and Indexing

### ✅ Verilog slicing:
```verilog
in[31:24]  // ✅ 8 bits: 31 - 24 + 1
```

### ✅ Looping:
```verilog
for (i = 0; i < 8; i++)  // ✅ 8 iterations
```

### ✅ Array indexing:
```verilog
mem[0:7]  // ✅ 8 elements
```