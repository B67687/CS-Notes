---
title: "📚 Combinational vs Sequential Circuits"
date: 2025-11-08
draft: false
---

Understanding the difference between **combinational** and **sequential** circuits is foundational to designing reliable, audit-ready hardware systems. This note breaks down both styles with annotated clarity.

---

## 🔌 Combinational Circuits

> **Definition**: Circuits whose outputs depend *only* on current inputs—no memory, no timing.

```verilog
assign y = a & b;
```

{{< callout type="info" >}}
**Behavior**
- Output updates *instantly* when inputs change.
- No concept of time or history.
{{< /callout >}}
### ✅ Characteristics
- **Stateless**: no internal memory.
- **Timing-independent**: output changes as soon as inputs do.
- **Used for**: logic gates, multiplexers, decoders, ALUs.

### 📌 Notes
- Can be written using `assign` or `always @(*)`.
- Ideal for pure logic transformations.
- Cannot model behavior that depends on past inputs.

---

## ⏱️ Sequential Circuits

> **Definition**: Circuits whose outputs depend on *current inputs and past states*—they store values across time.

```verilog
reg [3:0] counter;
always @(posedge clk) begin
    counter <= counter + 1;
end
```

{{< callout type="info" >}}
**Behavior**
- Output updates *only on clock edge* or *triggering event*
- Stores internal state using *flip-flops* or *latches*
{{< /callout >}}
### ✅ Characteristics
- **Stateful**: remembers past values.
- **Timing-dependent**: reacts to clock or control signals.
- **Used for**: FSMs, counters, registers, pipelines.

### 📌 Notes
- Requires `reg` and clocked `always` blocks.
- Enables modeling of time-aware systems.
- Essential for control flow, synchronization, and data retention.

---

## 🧪 Comparison Table

| Feature                  | Combinational Circuit     | Sequential Circuit         |
|--------------------------|---------------------------|-----------------------------|
| Depends on               | Current inputs only       | Inputs + stored state       |
| Timing                   | Instantaneous             | Clocked or event-driven     |
| Memory                   | ❌ None                   | ✅ Flip-flops, latches       |
| Syntax                   | `assign`, `always @(*)`   | `always @(posedge clk)`     |
| Use case                 | Logic gates, ALUs         | FSMs, counters, registers   |
| State retention          | ❌ No                     | ✅ Yes                       |

---

## 🧭 When to Use Each

### Use **combinational circuits** when:
- You need pure logic transformations.
- Output should reflect inputs immediately.
- No history or timing is involved.

### Use **sequential circuits** when:
- You need to store or remember values.
- Behavior depends on clock cycles or control signals.
- You're building FSMs, counters, or pipelines.

---

## 🧰 Vault Notes

{{< callout type="info" >}}
**Rule of Thumb**
If your circuit needs **memory or timing**, it's sequential.  
If it’s just **logic transformation**, it’s combinational.

[!example] Combinational Decoder
```verilog
reg [3:0] out;
always @(*) begin
    case (in)
        2'b00: out = 4'b0001;
        2'b01: out = 4'b0010;
        2'b10: out = 4'b0100;
        2'b11: out = 4'b1000;
    endcase
end
```

[!example] Sequential Counter
```verilog
reg [3:0] count;
always @(posedge clk) begin
    if (rst)
        count <= 0;
    else
        count <= count + 1;
end
```

[!warning] Common Mistake
Don’t use combinational logic to model behavior that depends on time or history—it will fail in synthesis or simulation.
{{< /callout >}}