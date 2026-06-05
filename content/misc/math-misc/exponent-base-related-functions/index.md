---
title: "📊 Exponent-Base Related Functions"
date: 2025-11-08
draft: false
---

This note formalizes the distinctions between different classes of functions involving exponentiation, based on **where the variable appears** — in the base, the exponent, or both.

---

## 🧠 Core Taxonomy

| Function Form | Name | Variable Placement | Growth Behavior |
|---------------|------|--------------------|------------------|
| $x^k$ | **Power function** | Variable in base, constant exponent | Polynomial |
| $b^x$ | **Exponential function** | Constant base, variable exponent | Exponential |
| $x^x$ | **Super-exponential** | Same variable in base and exponent | Explosive |
| $x^y$ | **Bivariate exponentiation** /<br> **General exponentiated function** | Different variables | Context-sensitive |

---

## 🔍 Definitions

- **Power Function**:  
  A function of the form $f(x) = x^k$, where $k \in \mathbb{R}$ is constant.  
  Growth is polynomial and depends on the size of the base.

- **Exponential Function**:  
  A function of the form $f(x) = b^x$, where $b > 1$ is constant.  
  Growth is exponential — each unit increase in $x$ multiplies the output by $b$.

- **Super-Exponential Function**:  
  A function like $f(x) = x^x$, where the variable appears in both base and exponent.  
  Growth is faster than exponential and highly nonlinear.

- **Bivariate Exponentiation**:  
  A general form $f(x, y) = x^y$, where both base and exponent are independent variables.  
  Behavior depends on the interaction between $x$ and $y$.

---

## 🧩 Conceptual Distinctions

- **Exponentiated Function**:  
  General term for any function involving exponentiation, regardless of variable placement.

- **Polynomial vs Exponential**:  
  - Polynomial: Variable in base → $x^k$  
  - Exponential: Variable in exponent → $b^x$

- **Growth Comparison**:
  $$
  \log x \ll x \ll x^2 \ll x^x \ll 2^x \ll x^{x^x}
  $$

---

## 🧠 Analogy: Multiplication vs Repetition

- $x^3$: Fixed number of multiplications → polynomial growth  
- $2^x$: Growing number of multiplications → exponential growth  
- $x^x$: Both size and count of multiplications grow → super-exponential

---

## 📚 Notes

- In algorithm analysis, **exponential complexity** always refers to $O(b^n)$, not $n^k$.
- **Casual misuse** of “exponential” often refers to polynomial growth — clarify in onboarding materials.
- **Logarithmic growth** is the inverse of exponential: slow, efficient, and foundational in divide-and-conquer algorithms.