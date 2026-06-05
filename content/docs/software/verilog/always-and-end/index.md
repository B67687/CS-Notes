---
title: "🔁 `always` and `end`"
date: 2025-11-08
draft: false
---

Understanding the role of `always` and `end` in Verilog is essential for modeling reactive logic and building audit-ready hardware systems. This note scaffolds their purpose, behavior, and relationship to control flow.

---

## 🔁 `always` Block

> **Definition**: A procedural block that executes when triggered by a sensitivity list.

```verilog
always @(*) begin
    y = a & b;
end
```

{{< callout type="info" >}}
**Behavior**
- Runs whenever any signal in the sensitivity list changes.
- Can describe **combinational** or **sequential** logic depending on the trigger.
- Acts like a **reactive container**, not a conditional.
{{< /callout >}}
### ✅ Characteristics
- **Event-driven**: triggered by changes or clock edges.
- **Encapsulates logic**: can include `if`, `case`, loops, assignments.
- **Used for**: FSMs, counters, decoders, ALUs.

### 📌 Notes
- `always @(*)` → combinational logic
- `always @(posedge clk)` → sequential logic
- Not a decision—it’s a **scope** for reactive behavior

---

## 🔚 `end` Keyword

> **Definition**: Closes a `begin` block or control structure.

```verilog
always @(*) begin
    if (sel)
        y = a;
    else
        y = b;
end
```

{{< callout type="info" >}}
**Behavior**
- Paired with `begin` to define multi-statement blocks.
- Also used to close `if`, `case`, `for`, and other control structures.
{{< /callout >}}
### ✅ Characteristics
- **Structural**: defines block boundaries.
- **Required** when using `begin` for multiple statements.
- **Optional** for single-line control flow.

---

## 🧪 Comparison Table

| Keyword   | Role                          | Required When…                      |
|-----------|-------------------------------|-------------------------------------|
| `always`  | Starts reactive logic block   | You want event-driven behavior      |
| `begin`   | Opens multi-statement block   | You have more than one statement    |
| `end`     | Closes the block              | Always paired with `begin`          |

---

## 🧭 Is `always` Like `if-else`?

{{< callout type="warning" >}}
**Misconception**
`always` is **not** a conditional—it’s a **reactive scope**.
{{< /callout >}}
### ✅ Clarification
- You write `if-else` **inside** an `always` block.
- The `always` block itself is **not a decision**, it’s a **triggered container**.

### 🧪 Example

```verilog
always @(*) begin
    if (sel)
        y = a;
    else
        y = b;
end
```

- This models a **multiplexer**.
- The block runs whenever `sel`, `a`, or `b` changes.
- The `if-else` is the decision logic; `always` is the reactive wrapper.

---

## 🧰 Vault Notes

{{< callout type="info" >}}
**Rule of Thumb**
Use `always` to define **when** logic should run.  
Use `if`, `case`, etc. inside to define **what** logic should run.

[!example] Combinational Decoder
```verilog
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
always @(posedge clk) begin
    if (rst)
        count <= 0;
    else
        count <= count + 1;
end
```

[!warning] Common Mistake
Don’t confuse `always` with `if`.  
`always` defines **when** logic runs—not **what** decision is made.
{{< /callout >}}