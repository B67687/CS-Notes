---
title: "🔄 Fetch–Decode–Execute Cycle"
date: 2025-11-08
draft: false
---


## 📜 Definition

The **Fetch–Decode–Execute cycle** is the repeating process a CPU uses to run instructions.
It starts when the computer powers on and continues until shutdown, looping billions of times per second.

---

## 🧩 Stages

### 1️⃣ Fetch

- **PC → MAR**: Program Counter (PC) holds the address of the next instruction; copied into the Memory Address Register (MAR).
- **Memory Read**: Control Unit (CU) signals main memory to send the instruction at that address.
- **MDR → CIR**: Instruction is placed in the Memory Data Register (MDR), then copied to the Current Instruction Register (CIR).
- **PC++**: PC increments to point to the next instruction.

### 2️⃣ Decode

- CU interprets the **opcode** (operation) and identifies any **operands** (data or addresses).
- Determines which CPU components (ALU, registers, memory) will be involved.

### 3️⃣ Execute

- The CPU carries out the instruction:
  - Arithmetic/logic via ALU
  - Data transfer between registers/memory
  - Branch/jump to a new address
- Results may be written back to registers or memory.

---

## 🛠 Key Registers in Play

| Register | Role |
|----------|------|
| **PC** (Program Counter) | Address of next instruction |
| **MAR** (Memory Address Register) | Holds address to access in memory |
| **MDR** (Memory Data Register) | Holds data fetched from or to be written to memory |
| **CIR** (Current Instruction Register) | Holds the instruction being decoded/executed |

---

## ⚡ Performance Notes

- **Clock Speed**: Determines how many cycles per second.
- **Pipelining**: Modern CPUs overlap stages for multiple instructions to improve throughput.
- **Cache**: Reduces fetch latency by storing frequently used instructions/data close to the CPU.

---

## 📌 Related Notes

- [[Machine Code]]
- [[Bytecode]]
- [[Instruction Pipelining]]
