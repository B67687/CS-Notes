---
title: "⚙️ Compiler Types"
date: 2025-11-08
draft: false
---

A compiler translates **human‑readable source code** into **machine code** that the CPU can execute.
Different strategies decide **when** and **how** this translation happens.

---

## 🚀 Just‑In‑Time (JIT) Compilation

**When:** At runtime, while the program is running.
**How:**

- Source code → (optional) intermediate bytecode → compiled to native machine code **on the fly**.
- The runtime monitors execution, identifies “hot” code paths, and optimizes them dynamically.

**Pros:**

- Adaptive optimization based on *actual* runtime behavior.
- Can inline, unroll, or specialize code for the current workload.
- Often faster than pure interpretation once warmed up.

**Cons:**

- Startup delay while code is compiled.
- Runtime overhead for profiling and compilation.
- Less time for deep optimizations compared to offline compilers.

**Examples:**
Java HotSpot JVM, .NET CLR, V8 JavaScript engine.

---

## 🏗 Ahead‑Of‑Time (AOT) Compilation

**When:** Before the program runs (build time).
**How:**

- Source code → native machine code → shipped as an executable.

**Pros:**

- No runtime compilation overhead → fast startup.
- Allows heavy, time‑consuming optimizations.
- Easier to deploy without requiring a runtime JIT.

**Cons:**

- No runtime profiling → optimizations are based on predictions, not actual usage.
- Less adaptable to changing workloads.

**Examples:**
C, C++, Rust, Go.

---

## 📜 Interpretation

**When:** At runtime, line‑by‑line or statement‑by‑statement.
**How:**

- Source code (or bytecode) is read and executed directly by an interpreter.

**Pros:**

- Immediate execution — great for scripting and rapid prototyping.
- Highly portable — just need the interpreter for the target platform.

**Cons:**

- Slower execution due to repeated parsing/translation.
- No persistent native code output.

**Examples:**
Python (CPython), Ruby (MRI), Bash.

---

## 🔄 Hybrid Models

Some languages mix strategies:

- **Bytecode + JIT**: Java, C#, JavaScript (modern engines).
- **AOT + JIT**: .NET Native, GraalVM.
- **Interpreted + JIT**: Python with PyPy.

---

## 📌 TL;DR Table

| Feature                | JIT Compilation                  | AOT Compilation                  | Interpretation                  |
|------------------------|-----------------------------------|-----------------------------------|----------------------------------|
| **Compile Time**       | During execution                  | Before execution                  | No full compile step             |
| **Optimization Basis** | Runtime profiling                 | Static analysis                   | None or minimal                  |
| **Startup Speed**      | Slower (warm‑up needed)           | Fast                              | Fast                             |
| **Adaptability**       | High                              | Low                               | High (but slower execution)      |
| **Examples**           | Java HotSpot, .NET CLR, V8        | C, C++, Rust, Go                  | Python, Ruby, Bash               |

---
