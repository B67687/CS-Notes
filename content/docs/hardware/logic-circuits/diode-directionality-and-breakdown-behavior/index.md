---
title: "🔁 Diode Directionality and Breakdown Behavior"
date: 2025-11-08
draft: false
---

## 🧠 Motivation

> [!Why we care]
> Diodes are designed to favor current flow in one direction (forward bias), but under extreme reverse bias, they can conduct in the opposite direction—triggering breakdown mechanisms that are crucial in voltage regulation and protection circuits.

---

## 🔌 Directional Behavior of a PN Junction Diode

| Bias Type      | Behavior                          | Carrier Movement              |
|----------------|-----------------------------------|-------------------------------|
| **Forward Bias** | Easy current flow (P → N)         | Electrons from N recombine with holes in P |
| **Reverse Bias** | Minimal current (leakage only)    | Minority carriers drift slowly |
| **Breakdown**    | Sudden large reverse current      | High-energy carriers trigger bond breakage |

---

## ⚡ Breakdown Mechanisms

### 🔬 Zener Breakdown

- Occurs in **heavily doped diodes** with narrow depletion regions
- High electric field causes **quantum tunneling** of electrons
- Used intentionally in **Zener diodes** for voltage regulation

### 🌪️ Avalanche Breakdown

- Occurs in **lightly doped diodes** with wider depletion regions
- Minority carriers gain enough energy to **knock loose more electrons**
- Leads to a **chain reaction** of carrier multiplication

> 🧠 Both mechanisms allow reverse current to flow—but only after overcoming a **critical voltage threshold**.
