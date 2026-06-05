---
title: "🧩 Interpreter vs Compiler"
date: 2025-11-08
draft: false
---

- **Source code** stays in high-level form (sometimes pre-tokenized into intermediate bytecode).
- **Interpreter** reads one chunk at a time → translates to machine instructions → executes immediately.
- Execution largely **follows source order**, so fewer global optimizations.
- Structure remains close to original source, making reverse-engineering easier.

---

## Compiler Flow

- Reads the **entire source** before execution.
- Builds an **Abstract Syntax Tree (AST)** and performs multiple analysis/optimization passes.
- Emits a **platform-specific machine code binary** (or VM bytecode).
- Can reorder instructions, inline functions, unroll loops, and strip dead code — final binary may differ greatly from source order for performance.

---

## 🔍 Key Takeaway

- **Interpreter →** Portability & immediacy (no build step, same source runs anywhere with the right runtime).
- **Compiler →** Performance & optimization (cost: platform‑specific binaries and a compile step).

---

## 🛠 Compiled vs Interpreted in Terms of Portability

| Feature             | Compiled Program                                         | Interpreted Program                                 |
|---------------------|----------------------------------------------------------|-----------------------------------------------------|
| **How it runs**     | Source → compiler → machine code **specific** to CPU/OS   | Source stays high‑level, run by an interpreter      |
| **Portability**     | Must **recompile** for each target platform               | Same source runs anywhere with correct interpreter  |
| **Dependencies**    | No interpreter needed — just the compiled binary          | Interpreter required                                |
| **Performance**     | Very fast after compilation                               | Slower — runtime translation overhead               |

---

## 💡 Summary

High‑level languages trade raw execution speed for:

- Developer productivity
- Maintainability
- Portability
- Safety
