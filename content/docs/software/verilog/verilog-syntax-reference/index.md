---
title: "📑 Verilog Syntax Reference"
date: 2025-11-08
draft: false
---

This notebook summarizes the core syntax elements of Verilog HDL. Each construct is annotated with its purpose, behavior, and contrast with similar features. Designed for semantic clarity, vault-grade pedagogy, and rapid onboarding into digital design workflows.

---

## 🧱 Module Declaration

```verilog
module my_module (
    input wire a, b,
    output wire y
);
    // internal logic
endmodule
```

- **Purpose**: Defines a reusable hardware block with named inputs/outputs.
- **Difference**: Unlike functions in software, modules describe physical logic and can be instantiated multiple times in a design hierarchy.

---

## 🔗 Data Types

| Type       | Usage                        | Notes |
|------------|------------------------------|-------|
| `wire`     | For continuous assignments   | Cannot hold state |
| `reg`      | For procedural assignments   | Can hold state in `always` blocks |
| `integer`  | Simulation-only counters     | Not synthesizable |
| `logic`    | SystemVerilog extension      | Combines `wire` and `reg` behavior |

---

## 📏 Vector Declaration

```verilog
wire [7:0] byte_data; // 8-bit bus
reg [3:0] nibble;
```

- MSB on the left, LSB on the right.
- **Match widths** during assignment to avoid synthesis errors.

---

## 🔁 Continuous Assignment

```verilog
assign y = a & b;
```

- **Purpose**: Describes combinational logic outside procedural blocks.
- **Difference**: Unlike `always` blocks, `assign` is static and updates automatically when inputs change.

---

## ⏰ Procedural Blocks

### Sequential Logic

```verilog
always @(posedge clk) begin
    q <= d;
end
```

- **Purpose**: Models flip-flop behavior triggered by clock edges.
- **Difference**: Uses non-blocking `<=` to avoid race conditions.

### Combinational Logic

```verilog
always @(*) begin
    y = a & b;
end
```

- **Purpose**: Describes logic that reacts to input changes.
- **Difference**: Uses blocking `=` and must include all relevant signals in sensitivity list.

---

## 🔄 Conditional Statements

```verilog
if (a > b)
    y = x;
else
    y = z;
```

- **Purpose**: Implements decision-making logic.
- **Difference**: Incomplete conditions may infer latches—use `else` or `default` to avoid.

{{< callout type="info" >}}
**Latch Inference — What It Means and Why It Matters**
In Verilog, a **latch** is inferred when a signal inside an `always @*` block is **not assigned in every possible condition**. This causes the synthesizer to generate hardware that **remembers** the last value—just like a physical latch.

The term **"latch"** comes from mechanical and electrical systems: a latch is a device that **holds its state** until explicitly changed. In digital logic, a latch behaves similarly—it remains transparent when enabled and retains its value when disabled.

**Example of latch inference:**

```verilog
always @* begin
  if (enable)
    q = d;  // ❌ No else → q retains previous value when enable is 0
end
```

This creates a level-sensitive latch because `q` is not updated when `enable` is false.

✅ **Best Practice**: Always assign outputs in all branches of conditional logic to avoid unintended latch behavior.
{{< /callout >}}
---

## 🔀 Case Statements

```verilog
case (sel)
    2'b00: y = a;
    2'b01: y = b;
    default: y = 1'bx;
endcase
```

- **Purpose**: Selects output based on discrete input values.
- **Difference**: More readable than nested `if` statements for multi-way branching.

---

## 🔣 Operators

| Operator            | Meaning            | Notes |
|---------------------|--------------------|-------|
| `~`                 | Bitwise NOT        | Inverts each bit |
| `&`                 | Bitwise AND        | ANDs each bit |
| <code>&#124;</code> | Bitwise OR         | ORs each bit |
| `^`                 | Bitwise XOR        | Exclusive OR |
| `==`, `!=`          | Equality           | Compares values |
| `<<`, `>>`          | Shift              | Logical shift |
| `?:`                | Ternary (if-else)  | Compact conditional |

---

## 🧩 Module Instantiation

### Named

```verilog
my_mod U1 (.a(A), .b(B), .y(Y));
```

### Ordered

```verilog
my_mod U1 (A, B, Y);
```

- **Purpose**: Reuses a module in another design.
- **Difference**: Named instantiation avoids port-order errors and improves readability.

---

## 🧪 Simulation Constructs

```verilog
initial begin
    $display("Start");
    #10 a = 1;
end
```

- **Purpose**: Used in testbenches to simulate behavior.
- **Difference**: Not synthesizable—only for simulation and debugging.

---

## 🧬 Concatenation, Replication & Width Behavior

### 🔗 Concatenation

```verilog
assign out = {a, b}; // Combines a and b into a wider vector
```

- `{}` joins multiple signals into a single vector.
- Order matters: MSB on the left.

### 🔁 Replication

```verilog
assign out = {4{a}}; // Replicates 'a' 4 times
```

- `{N{signal}}` repeats the signal N times.
- Useful for padding or pattern generation.

### ⚠️ Truncation

```verilog
wire [3:0] a;
assign a = 8'b10101010; // Only lower 4 bits assigned → a = 4'b1010
```

- **Higher bits are silently discarded**.

### 🧊 Zero-Padding

```verilog
wire [7:0] a;
assign a = 4'b1101; // a = 8'b00001101
```

- **Left side is padded with zeros**.

---

## 🧮 Parameters

### Declaring Parameters

```verilog
module adder #(parameter WIDTH = 8) (
    input wire [WIDTH-1:0] a, b,
    output wire [WIDTH-1:0] sum
);
```

- Parameters allow scalable, reusable modules.
- Can be overridden during instantiation.

### Overriding Parameters

```verilog
adder #(.WIDTH(16)) U1 (
    .a(a),
    .b(b),
    .sum(sum)
);
```

- Use `#(.NAME(VALUE))` syntax for named parameter override.

### Local Parameters

```verilog
localparam DEPTH = 32;
```

- Internal constants that can't be overridden.

---

## 🔀 Multiple `always` Blocks and Concurrency

- **All `always` blocks run concurrently**, regardless of their order in the file.
- **Order of appearance does not affect execution**—Verilog models parallel hardware.

```verilog
always @* begin
  a = b;
  c = m;
end

always @* begin
  y = ...;
  z = ...;
end
```

- **Best Practice**: Assign each signal from only one block.
- **Difference**: Unlike software, Verilog logic is synthesized as parallel hardware.

- **Exception**: Inside a single `always` block, **statement order matters**—last assignment wins.

```verilog
always @* begin
  y = a & b;
  y = x | c;  // Overrides previous y
end
```

---
