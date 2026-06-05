---
title: "🧮 Solving Linear Equations"
date: 2025-11-08
draft: false
---

Solving a system of linear equations means **isolating each variable** without changing the system’s meaning

A system of linear equations is simplified by **moving the focus away from the variables of the system of equations** by organising the coefficients by their variables into a [ matrix](../matrices/)

Coefficients and constants are separated by a line in this matrix, known as the [ augmented matrix](../augmented-matrix/)

To simplify and solve the system, we apply [ Elementary Row Operations](../elementary-row-operations/) and reduce the variables systematically until all but one of each variable is left

---

## 🧭 Directionality and Convention

Because we write **left to right, top to bottom**, matrix reduction follows the same ergonomic flow:

- Start at the **top-left**
- Move **rightward** and **downward**
- At each step, keep the current coefficient representing the variable and **eliminate the rest** above and below it

{{< callout type="info" >}}
**The Pivot**
The coefficient of the variable that we isolate for each row is called the **pivot**

The term “pivot” comes from its **role** in elimination:

- It’s the **anchor** used to eliminate entries below (and in RREF, above) it.
- In Gaussian elimination, we “pivot” around this entry to clear its column.
- It acts like a **hinge** or **fulcrum**—the transformation rotates around it.
{{< /callout >}}
This naturally leads to a **staggered structure** that looks like an echelon arranged by row, thus it is called **row-echelon form**, or **REF** for short

{{< callout type="default" >}}
**What is "Echelon"?**
The term **echelon** comes from military formation—soldiers arranged in a **staggered diagonal pattern**.
{{< /callout >}}
---

## 🔄 Reduction Pipeline

Reducing both directions at once is rather disorienting, thus we have preferred to go in **one direction preferred at a time**

Since we start top-left, we naturally eliminate **downwards** first (forward-substitution), to remove all the variables **below the leading variable of each row**

{{< callout type="info" >}}
**Row-Echelon Form**

$$
\left[
\begin{array}{ccc|c}
2 & 4 & 6 & 8 \\
0 & 3 & 9 & 6 \\
0 & 0 & 5 & 15
\end{array}
\right]
$$

1. All nonzero rows are above any rows of all zeros.
2. Each pivot is to the **right** of the pivot in the row above.
3. All entries **below** a pivot are zeros.

[!note] Elimination Checkpoint
Elimination that stops here is called **Gaussian Elimination**
{{< /callout >}}
Once we hit the bottom we eliminate **upwards** (backward-substitution), to remove the all the variables **above the leading variable of each row**

Then afterwards, we make the coefficients of each isolated variable into 1, and we have reached the solution to the system of linear equations

{{< callout type="info" >}}
**Reduced Row Echelon Form**
At this point, the diagonal of isolated coefficients of 1 with the rest of the matrix being 0, is called the **Reduced Row-Echelon Form**, basically **Reduced REF**, or just **RREF**

$$
\left[
\begin{array}{ccc|c}
1 & 0 & 0 & 9 \\
0 & 1 & 0 & -7 \\
0 & 0 & 1 & 3
\end{array}
\right]
$$

1. Each pivot is **1**
2. Each pivot is the **only nonzero entry** in its column

[!note] Elimination Endpoint
Elimination that reaches here is called **Jordan-Gauss Elimination**
{{< /callout >}}
---

## 🧠 General Strategy for Solving to REF or RREF

Here’s a robust tactic for reducing any matrix:

1. 🔁 **Swap rows** to move already solved rows (with pivot = 1) to the top.
2. 🔽 **Work top-down**, row by row.
3. 🧹 **Eliminate entries below the pivot** using row operations.
4. 🔁 Repeat for the next row and pivot column.
5. 🧼 For RREF: After reaching REF, eliminate entries **above** each pivot and normalize pivots to 1.

{{< callout type="default" >}}
**Normalize each pivot to 1 immediately** before using it to eliminate other rows

- This leads to cleaner arithmetic and aligns naturally with RREF goals.

**Favor additive operations over scalar multiplication**

- Instead of computing $cR_1$, use $R_2 + cR_1$ or $R_1 + cR_2$ to eliminate—this keeps the original row intact and avoids unnecessary scaling.
{{< /callout >}}
---

### ✏️ Example: Normalizing First for Cleaner Elimination

Start with:

$$
\begin{bmatrix}
3 & -4 & 10 \\
-5 & 8 & -17 \\
-3 & 12 & -12
\end{bmatrix}
$$

Step-by-step:

1. Normalize $R_1$:
   $$ R_1 \rightarrow \frac{1}{3}R_1 $$

2. Eliminate below using clean multiples:
   $$ R_2 + 5R_1,\quad R_3 + 3R_1 $$

3. Normalize $R_2$:
   $$ R_2 \rightarrow \frac{3}{4}R_2 $$

4. Eliminate below again:
   $$ R_3 - 8R_2 $$

Final REF:

$$
\begin{bmatrix}
1 & -\frac{4}{3} & \frac{10}{3} \\
0 & 1 & -\frac{1}{4} \\
0 & 0 & 0
\end{bmatrix}
$$

{{< callout type="info" >}}
This method avoids fractional multipliers like $\frac{5}{3}R_1$ and keeps operations visually clean and semantically aligned with pivot logic.
{{< /callout >}}
---

## 🧠 Interpreting the Final Augmented Matrix: 3 Possibilities

After reducing the augmented matrix (via REF or RREF), there are **three possible outcomes**:

### ✅ 1. Unique Solution

- Every variable has a pivot.
- No contradictions.
- Final matrix has one solution.

{{< callout type="info" >}}
$$
\begin{bmatrix}
1 & 0 & 0 & \vert & 2 \\
0 & 1 & 0 & \vert & -1 \\
0 & 0 & 1 & \vert & 3
\end{bmatrix}
$$
{{< /callout >}}
→ Solution:
$x = 2$, $y = -1$, $z = 3$

---

### ♾️ 2. Infinitely Many Solutions

- Some variables are **free** (no pivot in their column).
- No contradictions.
- Final matrix leads to parametric form.

{{< callout type="info" >}}
$$
\begin{bmatrix}
1 & 0 & 2 & \vert & 5 \\
0 & 1 & -1 & \vert & 3 \\
0 & 0 & 0 & \vert & 0
\end{bmatrix}
$$
{{< /callout >}}
→ Let $z = t$ (free variable)
Then:
$x = 5 - 2t$
$y = 3 + t$

→ Parametric solution:
$(x, y, z) = (5 - 2t,\ 3 + t,\ t)$

---

### ❌ 3. No Solution

- A row like:
  $$ [0 \quad 0 \quad 0 \mid c] \quad \text{where } c \neq 0 $$
- This represents a contradiction (e.g., $0 = 5$).
- System is **inconsistent**.

{{< callout type="info" >}}
$$
\begin{bmatrix}
1 & 2 & -1 & \vert & 4 \\
0 & 1 & 3 & \vert & 2 \\
0 & 0 & 0 & \vert & 7
\end{bmatrix}
$$
{{< /callout >}}
→ Contradiction in last row: $0 = 7$
→ ❌ No solution
