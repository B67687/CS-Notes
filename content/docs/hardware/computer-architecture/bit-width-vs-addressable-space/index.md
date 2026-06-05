---
title: "🧠 Bit-Width vs Addressable Space"
date: 2025-11-08
draft: false
---

## 🔹 Bit-Width (Data Width)

Refers to the size of data units the processor natively handles.

| Property            | Meaning                                  | 16-bit Example                        |
|---------------------|-------------------------------------------|----------------------------------------|
| Register size       | How many bits each register holds         | AX = 16 bits = 2 bytes                 |
| ALU operand size    | Bit-width of arithmetic/logical operations| ADD AX, BX → operates on 16-bit values |
| Instruction encoding| Designed to work with 16-bit operands     | MOV AX, [1234h]                        |

🧩 Think of this as the **internal word size** — the granularity of computation.

---

## 🔹 Addressable Space (Memory Reach)

Refers to how many distinct memory locations the processor can reference.

| Property            | Meaning                                  | 16-bit Example                        |
|---------------------|-------------------------------------------|----------------------------------------|
| Address bus width   | Bits used to form memory addresses        | 16-bit address → 2¹⁶ = 65,536 addresses|
| Address granularity | Size of each addressable unit             | Typically 1 byte per address           |
| Total memory reach  | Maximum directly addressable memory       | 64 KB (if no segmentation/paging)      |

🧩 This is about **external reach** — how far the processor can point into memory.

---

### ✅ Summary

- "16-bit processor" → Refers to internal data width (registers, ALU, instruction operands)
- "2^16 bytes" → Refers to external memory reach via 16-bit address bus
- These are related but distinct: one is about **how wide**, the other is about **how far**
