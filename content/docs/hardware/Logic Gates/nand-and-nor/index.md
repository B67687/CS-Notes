---
title: NAND and NOR
date: 2025-11-08
draft: false
---

The fundamental gate types are **NOT**, **AND**, **OR**.

We want to find a gate that contains at these **fundamental gates**, so that we can **express any circuit** using just this gate

---

## ✅ Minimal Requirements for Completeness

To express all Boolean functions, we need:

- **Negation**: the ability to invert a signal (`NOT`)
- **Binary composition**: either `AND` or `OR` suffices, since they are duals via De Morgan's laws

{{< callout type="info" >}}
**Complete Gates>**
Thus, both NAND and NOR can express all Boolean logic

In other words, these gates are **functionally complete**
{{< /callout >}}
---

## 🔧 NAND-Only Logic Constructions

{{< callout type="info" >}}
Primitive: $$A \uparrow B = \neg(A \land B)$$
{{< /callout >}}
| Operation | NAND-Only Construction                  | Explanation                             |
|-----------|-----------------------------------------|-----------------------------------------|
| `NOT` A     | $$A \uparrow A$$                        | `NOT` `(`A `AND` A`)`<br><br>--> Negation of [ Idempotency](../boolean-algebra/#idempotent-law) |
| A `AND` B   | $$(A \uparrow B) \uparrow (A \uparrow B)$$ | **`NOT`**`{`<br>$\quad$`NOT` `(`A `AND` B`)`<br>**`AND`**<br>$\quad$`NOT` `(`A `AND` B`)`<br>`}`<br><br>--> [ Double-Negation](../boolean-algebra/#fundamental-laws) through [ Idempotency](../boolean-algebra/#idempotent-law)<br> |
| A `OR` B    | $$(A \uparrow A) \uparrow (B \uparrow B)$$ | **`NOT`**`{`<br>$\quad$`NOT` `(`A `AND` A`)`<br>**`AND`**<br>$\quad$`NOT` `(`B `AND` B`)`<br>`}`<br><br>--> [ DeMorgan's Law](../boolean-algebra/#fundamental-laws) through [ Idempotency](../boolean-algebra/#idempotent-law)<br> |

---

## 🔧 NOR-Only Logic Constructions

{{< callout type="info" >}}
Primitive: $$A \downarrow B = \neg(A \lor B)$$
{{< /callout >}}
| Operation | NOR-Only Construction | Explanation |
|-----------|------------------------|-------------|
| `NOT` A     | $$A \downarrow A$$ | `NOT` `(`A `OR` A`)`<br><br>--> Negation of [ Idempotency](../boolean-algebra/#idempotent-law) |
| A `OR` B    | $$(A \downarrow B) \downarrow (A \downarrow B)$$ | **`NOT`**`{`<br>$\quad$`NOT` `(`A `OR` B`)`<br>**`OR`**<br>$\quad$`NOT` `(`A `OR` B`)`<br>`}`<br><br>--> [ Double-Negation](../boolean-algebra/#fundamental-laws) through [ Idempotency](../boolean-algebra/#idempotent-law)<br> |
| A `AND` B   | $$(A \downarrow A) \downarrow (B \downarrow B)$$ |  **`NOT`**`{`<br>$\quad$`NOT` `(`A `OR` A`)`<br>**`OR`**<br>$\quad$`NOT` `(`B `OR` B`)`<br>`}`<br><br>--> [ DeMorgan's Law](../boolean-algebra/#fundamental-laws) through [ Idempotency](../boolean-algebra/#idempotent-law)<br> |

---

{{< callout type="default" >}}
Find out more about primitive NAND $(\uparrow)$  and NOR $(\downarrow)$ expressions at [ Sheffer Stroke and Pierce Arrow](../sheffer-stroke-and-pierce-arrow/)
{{< /callout >}}