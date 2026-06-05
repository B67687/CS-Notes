---
title: 💾 Flip-Flops
date: 2025-11-20
draft: false
---

Flip-flops are fundamental 1-bit memory elements in sequential logic, triggered by a clock edge. They solve the issues present in basic latches.

## 1. 🛑 SR Flip-Flop (Set-Reset)

-   **Purpose:** The foundational circuit for basic setting and resetting.
-   **Inputs:** $\text{S}$ (Set) and $\text{R}$ (Reset).
-   **Operation:**
    -   $\text{S=1, R=0} \to$ Set ($Q_{n+1}=1$)
    -   $\text{S=0, R=1} \to$ Reset ($Q_{n+1}=0$)
    -   $\text{S=0, R=0} \to$ Hold ($Q_{n+1}=Q_n$)
-   **Problem:** The **forbidden state** ($\text{S=1, R=1}$) leads to an unpredictable output upon the next clock cycle.

---

## 2. 🛡️ D Flip-Flop (Data or Delay)

-   **Purpose:** The most common flip-flop, it transfers data on clock edge. Used to **store 1 bit** of data and *eliminate the forbidden state in the SR Flip-Flop*
-   **Inputs:** $\text{D}$ (Data).
-   **Operation:** The output $Q$ simply becomes equal to the $D$ input after the clock edge.
-   **Characteristic Equation:** $Q_{n+1} = D$
-   **Advantage:** **Simple implementation** and no invalid states, making it the primary component for registers and computer memory.

---

## 3. 🧠 JK Flip-Flop (Jump-Kill)

-   **Purpose:** The most **versatile** flip-flop, solving the SR's forbidden state in the *SR Flip-Flop* by introducing a toggle function.
-   **Inputs:** $\text{J}$ (Set) and $\text{K}$ (Reset).
-   **Operation:**
    -   $\text{J=0, K=0} \to$ Hold ($Q_{n+1}=Q_n$)
    -   $\text{J=1, K=1} \to$ **Toggle** ($Q_{n+1}=\bar{Q}_n$)
-   **Characteristic Equation:** $Q_{n+1} = J\bar{Q}_n + \bar{K}Q_n$
-   **Advantage:** Can perform all modes (Set, Reset, Hold, Toggle) without an invalid state.

---

## 4. 🔄 T Flip-Flop (Toggle)

-   **Purpose:** Designed specifically for **toggling** or dividing the clock frequency by two.
-   **Inputs:** $\text{T}$ (Toggle).
-   **Operation:**
    -   $\text{T=0} \to$ Hold ($Q_{n+1}=Q_n$)
    -   $\text{T=1} \to$ **Toggle** ($Q_{n+1}=\bar{Q}_n$)
-   **Implementation:** Often constructed by *tying the $\text{J}$ and $\text{K}$ inputs of a JK flip-flop together*.
-   **Primary Use:** Binary counters and frequency division circuits.