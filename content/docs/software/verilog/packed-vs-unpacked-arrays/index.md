---
title: "📚 Packed vs Unpacked Arrays"
date: 2025-11-08
draft: false
---

Basically **packed arrays** are the size of each element and **unpacked arrays** is *how many of these elements* there are

### ✅ Packed Array
- Declared **before** the variable name: `[N:0] var`
- Represents a **bit vector** — tightly packed bits
- Treated as a **single unit** in memory
- Can be sliced, indexed, and used in arithmetic

```verilog
reg [7:0] byte;       // Packed: 8 bits in one unit
byte[3] = 1'b1;       // ✅ Bit-level access
```

- Used for **bit-level operations**, **arithmetic**, **protocols**
- Example: `reg [31:0] instruction;`

---

### ✅ Unpacked Array
- Declared **after** the variable name: `var [M:0]`
- Represents an **array of elements**
- Each element is a separate packed unit (or scalar)
- Indexed like a traditional array

```verilog
reg [7:0] mem [255:0];  // Unpacked: 256 elements, each 8 bits
mem[42] = 8'b10101010;  // ✅ Element-level access
```

- Used for **storage**, **indexing**, **looping**
- Example: `reg [7:0] memory [0:255];`
---

## 🧩 Example

```verilog
reg [7:0] mem [255:0];
```

| Layer        | Meaning                                |
|--------------|----------------------------------------|
| `[7:0]`      | Packed: each element is 8 bits         |
| `mem`        | Variable name                          |
| `[255:0]`    | Unpacked: 256 elements                 |

So:
- `mem[42]` → 8-bit packed word
- `mem[42][3]` → bit 3 of that word