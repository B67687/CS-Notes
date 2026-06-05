---
title: "🌓 Binary Search"
date: 2025-11-08
draft: false
---

This note reconstructs the logic behind binary search from first principles, showing why midpoint comparison is the optimal strategy for reducing search space in a sorted list.

---

## 🧠 Step-by-Step Derivation

1. **Goal:** We want to reduce the search space during searching.
2. **Requirement:** To reduce the space, we must know which side of the current number to discard.
3. **Implication:** This requires the list to be **sorted**, so comparisons are meaningful.
4. **Setup:** With a sorted list, we can compare a chosen number and eliminate either the left or right side.
5. **Question:** Which number should we choose for comparison?
6. **Observation:** If we choose any arbitrary number, one side may contain **more elements** than the other.
7. **Average Case:** Over many searches, the imbalance averages out — any position behaves like the middle.
8. **Best vs Worst Case:**
   - Choosing a number **far from the middle** improves the **best case** (faster if lucky).
   - But it worsens the **worst case** (slower if unlucky).
1. **Design Principle:** We prioritize **minimizing the worst case** over optimizing the best case.
2. **Optimal Strategy:** Choose the **middle element** to ensure both sides are **equally sized**.
3. **Result:** This guarantees that no matter which side the target lies on, the remaining search space is **at most half**.
4. **Conclusion:** Binary search achieves the **best possible worst-case performance** while maintaining a solid best case.

---

## 🧩 Why This Matters

- Binary search builds a **balanced decision tree**, ensuring logarithmic depth.
- Off-center comparisons risk **unbalanced partitions**, increasing worst-case depth.
- In systems design, we favor **predictable bounds** and **worst-case minimization** over rare best-case wins.

---

## 🧠 Summary

> Binary search is optimal because it guarantees that the remaining search space is never larger than half, minimizing worst-case depth while maintaining reasonable best-case performance.