---
title: "⚡ Active-High and Active-Low"
date: 2025-11-08
draft: false
---

> [!Why we invented this]
> Digital signals are binary—either `1` or `0`.
> But what those values **mean** depends on how the circuit is designed.
>
> We use **Active High** and **Active Low** to define whether a signal is considered “active” when it’s **electrically high** or **electrically low**.

> This is crucial for:
>
> - Naming signals (e.g., `RESET`, `ENABLE`, `READY̅`)
> - Designing logic gates and control flows
> - Interpreting truth tables and waveform behavior

---

### ✅ Definitions

| Term           | Meaning                                                  |
|----------------|-----------------------------------------------------------|
| **Active High** | Signal is considered active when it is **electrically high** (`1`) |
| **Active Low**  | Signal is considered active when it is **electrically low** (`0`) |

> [!Tip]
> “Active” means the signal is **interpreted as meaningful**—either triggering behavior (control) or indicating status (output).
> This interpretation depends on the signal’s **polarity**, not just its voltage level.

---

### 🧩 Semantic Anchors (Control Signals Only)

| Signal Name | Active High Interpretation       | Active Low Interpretation        |
|-------------|----------------------------------|----------------------------------|
| `RESET`     | `RESET = 1` → system resets      | `RESET = 0` → system resets      |
| `ENABLE`    | `ENABLE = 1` → output allowed    | `ENABLE = 0` → output allowed    |
| `READY`     | `READY = 1` → data is ready      | `READY = 0` → data is ready      |

> [!Note]
> Output flags like `ODD` or `EVEN` are **status indicators**, not control signals.
> Their polarity is defined by naming (e.g., `ODD_N`) if inversion is required.

---

### 📊 Truth Table Interpretation

> [!Audit Trigger]
> A signal’s **active polarity** determines when the circuit responds to other inputs.
> You can detect this by analyzing when the output starts reacting to changes in other signals.

#### Example 1: Active High Enable

| E | A | Z |
|---|---|---|
| 0 | X | 0 or Z |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

- When `E = 0`, output is disabled (e.g., forced to 0, held, or high-Z)
- When `E = 1`, output depends on `A` → circuit is **enabled**

✅ **Enable is active high**

---

#### Example 2: Active Low Enable

| E | A | Z |
|---|---|---|
| 1 | X | 0 or Z |
| 0 | 0 | 0 |
| 0 | 1 | 1 |

- When `E = 1`, output is disabled (e.g., forced to 0, held, or high-Z)
- When `E = 0`, output depends on `A` → circuit is **enabled**

✅ **Enable is active low**

> [!Tip]
> Always ask: *When does the output start responding to other inputs?*
> That’s when the enable signal is “active.”

---

### 🔧 Naming Convention

| Convention   | Meaning |
|--------------|---------|
| `SIGNAL`     | Active High |
| `SIGNAL_N`   | Active Low (suffix `_N` for “negated”) |
| `SIGNAL̅`     | Active Low (overbar notation, common in schematics) |

> [!Audit Flag]
> Always check whether a signal is **active high or low** before interpreting its behavior.
> Never assume `1 = active` or `0 = inactive` without polarity context.

---

### 🧠 Visual Analogy

> Imagine a smart light:
>
> - If it's **active high**, it turns on when the control signal is high (`1`)
> - If it's **active low**, it turns on when the control signal is low (`0`)
>
> The light still turns on—but the **trigger condition** is different.

---

### ✅ Summary

> ```plaintext
> Active High → signal is active when HIGH (1)
> Active Low → signal is active when LOW (0)
> ```
>
> - This affects how we name, interpret, and implement logic
> - It does **not** change the underlying truth table—just the **semantic layer**

> [!NOTE]
> Always annotate signal polarity in your vault to avoid misinterpretation during synthesis, debugging, or waveform analysis.
