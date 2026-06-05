---
title: "⏳ Continuous vs Procedural Assignment"
date: 2025-11-08
draft: false
---

Understanding the difference between **continuous** and **procedural** assignment is essential for designing reliable, audit-ready hardware systems. This note breaks down both styles with annotated clarity.

---

## 🔌 Continuous Assignment

> **Definition**: A declarative connection between a `wire` and a logic expression that is always active.

```verilog
wire y;
assign y = a & b;
```

> [!info] Syntax
> - `wire` refers to *literal wiring*
> - Paired with `assign` which is only used for continuous assignment 

### ✅ Characteristics
- **Always active**: updates instantly when inputs change.
- **Stateless**: does not store values.
- **Used for**: simple combinational logic, wiring, gates.

### 📌 Notes
- Only works with `wire` types.
- Cannot include `if`, `case`, or multi-step logic.
- Ideal for clean, declarative connections.

---

## 🔁 Procedural Assignment

> **Definition**: Imperative logic inside an `always` block that executes when triggered by a sensitivity list.

```verilog
reg y;
always @(*) begin
    y = a & b;
end
```

> [!info] Syntax
> - `reg` stands for *register* which points to storing values

### ✅ Characteristics
- **Triggered**: runs when inputs in sensitivity list change.
- **Can store state**: especially in clocked blocks.
- **Used for**: FSMs, conditional logic, multi-step computation.

### 📌 Notes
- Requires `reg` type for assigned variables
- Can include `if`, `case`, loops, and intermediate variables.
- Enables modeling of both combinational and sequential logic.

---

## 🧪 Comparison Table

| Feature                  | Continuous (`assign`) | Procedural (`always`) |
|--------------------------|------------------------|------------------------|
| Syntax                   | `assign y = ...`       | `always @(*) y = ...` |
| Target type              | `wire`                 | `reg`                  |
| Timing                   | Always active          | Event-driven           |
| State retention          | ❌ No                  | ✅ Yes (if clocked)     |
| Control flow             | ❌ Limited             | ✅ Full (`if`, `case`)  |
| Use case                 | Simple logic           | FSMs, counters, branching |

---

## 🧭 When to Use Each

### Use `assign` when:
- Logic is simple and stateless.
- You want direct wiring between signals.

### Use `always` when:
- Logic involves conditions, branching, or multi-step computation.
- You need to store state or react to clock edges.

---

## 🧰 Vault Notes

> [!tip] Rule of Thumb
> If you're modeling **wires**, use `assign`.  
> If you're modeling **behavior**, use `always`.

> [!example] FSM State Update
> ```verilog
> reg [1:0] state;
> always @(posedge clk) begin
>     if (rst)
>         state <= IDLE;
>     else
>         state <= next_state;
> end
> ```

> [!warning] Common Mistake
> Don’t use `assign` to drive a `reg`, and don’t assign to a `wire` inside an `always` block.
