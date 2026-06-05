---
title: "🧮 Matrix Multiplication and Dot Product"
date: 2025-11-08
draft: false
---


Fundamentally **matrices** are **sets of numbers grouped together in organised ways** where the axis represent the different factors we are grouping them by.

> [!info] Parallel in Computer Science
> In computer science, matrices resemble **arrays**—but in linear algebra, they are more strict with **preserving orientation**

---

## 🔧 Preserving Linearity in Arithmetic

Operations between numbers must **maintain the current level of abstraction** in order to remain **linear**.

- This includes **addition and subtraction**, which operate directly on values without changing their structural role:

$$
a + b = c \quad\text{and}\quad a - b = d
$$

- When we have **repeated addition/subtraction** between numbers, we simply **shorten its representation** and call it **multiplication**:

$$
a + a + a + \dots + a = a \cdot n
$$

> [!tip] Generalisation of Multiplication
> Even in its **generalized form**, multiplication remains semantically additive:
>
> - For **rational scalars**, multiplication represents repeated addition of fractional parts.
> - For **irrational scalars**, multiplication is defined via **limit-based additive constructions**—approximating the scalar through sequences of rational additions.
> - In analysis, multiplication by a real number corresponds to **continuous additive accumulation**, often formalized through **integration** or **area under a curve**.

---

## 🚫 Why Division Is Not Linear

**Scalar multiplication** applies a process to reach a result.

$$a \cdot n$$

> [!info] Abstraction-Preserving
> It stays within the abstraction as the **original number** is still **the one being dealt with**

**Division** finds **how many times the process was applied** to get to the result

$$\dfrac{c}{a} = n$$

> [!info] Abstraction Shift
> Division **shifts the abstraction** away from the original numbers
>
> Therefore, it is **not a linear operation**

---

## 🧮 Linearity in Matrix Operations

In linear algebra, we group numbers together in **organised rows and columns** called **matrices**.

> [!tip] Linearity of Matrices
> **Maintaining linearity in matrices** requires
>
> - Maintaining the **position of each number relative to one another**
> - Each number must also maintain their **relative magnitude to one another**
>
> Otherwise, matrices cannot be meaningfully be said to be the **direct transformation of its component numbers** after transformation

**Unique orientation of numbers** is what make matrices unique

---

### ➕ Matrix Addition

$$ A \pm B \in \mathbb{R}^{m \times n} $$

Linear operations on these groups are still just **addition and subtraction**, applied **element-wise** on matrices of the **same shape**

$$
\begin{bmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    a_{21} & a_{22} & \cdots & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
\pm
\begin{bmatrix}
    b_{11} & b_{12} & \cdots & b_{1n} \\
    b_{21} & b_{22} & \cdots & b_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    b_{m1} & b_{m2} & \cdots & b_{mn}
\end{bmatrix}
$$
$$
=
$$
$$
\begin{bmatrix}
    a_{11} \pm b_{11} & a_{12} \pm b_{12} & \cdots & a_{1n} \pm b_{1n} \\
    a_{21} \pm b_{21} & a_{22} \pm b_{22} & \cdots & a_{2n} \pm b_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m1} \pm b_{m1} & a_{m2} \pm b_{m2} & \cdots & a_{mn} \pm b_{mn}
\end{bmatrix}
$$

### ✖️ Scalar Multiplication

$$ kA \in \mathbb{R}^{m \times n} $$

Its notation shorthand for **repeated addition/subtraction** in matrices is also applied **element-wise** on matrices of the **same shape**

$$
k \cdot
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
=
\begin{bmatrix}
k a_{11} & k a_{12} & \cdots & k a_{1n} \\
k a_{21} & k a_{22} & \cdots & k a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
k a_{m1} & k a_{m2} & \cdots & k a_{mn}
\end{bmatrix}
$$

---

## 📚 Composition of Linear Operations in Matrices

The **composition** of these 2 linear operations are also linear, thus this is the only possible composition

> [!example] Fundamental Composition Form
> **Add** the **scaled** versions—$a_n$—of the **same size matrices**—$B_n$
> $$a_1 B_1 + a_2 B_2 + a_3 B_3 + \dots = C$$

> [!warning] Why POS Is Not a Valid Composition
> While this form is clearly a **Sum of Products (SOP)**, one might ask:
> Why not **Product of Sums (POS)**?
>
> In scalar arithmetic, **POS** expands into **SOP** due to distributivity.
>
> In matrix arithmetic, **POS** is not definable element-wise as it would apply **different scalings to different entries**, thus breaking their **relative proportion to one another**.
> > This is not meaningfully linear in organised groups of numbers.
>
> Matrix Multiplication on the other hand is defined through **SOP** as we will see

---

## 🧮 Dot Product

The simplest case is thus to have matrices of size $1 \times 1$

$$
a_1[b_1] + a_2[b_2] + a_3[b_3] + \dots = c
$$

Which is the same as just

$$
\boxed{
 \phantom{\biggr(}
 a_1 \cdot b_1 + a_2 \cdot b_2 + a_3 \cdot b_3 + \dots = c
 \phantom{\biggr)}
}
$$

> [!tip] Named Operation
> This combined multiplication with addition has a special name called a **dot product**,
>
> It is essentially a **sum of products**, or **SOP**, of related numbers in matrices

> [!info] Why "Dot Product"?
> “Dot Product” is named after the **dot notation** used to describe this **composite operation**
>
> $$A \cdot B$$
>
> *An undescriptive name this is*

---

## 📚 Generalizing the Dot Product

The general form is thus that this dot product can be done on multiple sets of numbers of that matrix—with the same length

> [!example] Basic Form
> $a_n$ is the $n^{th}$ constant
> $B_n$ is the $n^{th}$ matrix of the same shape
> $C$ is the matrix of the same size as $B$
>$$a_1 B_1 + a_2 B_2 + a_3 B_3 + \dots = C$$

If we want more sets of constants to apply to each matrix $B_m$, we can also add those to $a_n$ and make them matrices as well

> [!example] Generalised Form
> $A_n$ and $B_n$ is the $n^{th}$ matrix of the same shape within their respective matrix groups
> $C$ is a matrix—but we haven't standardised what it's size should be
>$$A_1 B_1 + A_2 B_2 + A_3 B_3 + \dots = C$$

---

## 🧭 Axis and Reading Order

How should the 2 matrices of data be represented?

> [!tip] Axes and Representation
> In order for the **resultant vector** to be **easily traced**, we make one matrix represent one axis and the other matrix represent the other axis
>
> This results in one of the matrix to be comprised of
> > **row matrices**—and therefore read by *row*
>
> And the other to be in
> > **column matrices**—and therefore read by *column*

Now we have to figure out which side the **matrix made of rows** and the **matrix made of columns** should be on

> [!info] Left-Right Arrangement
>
> Since we write equations like so:
>
> $$
> \begin{aligned}
> 2x + 3y &= 8 \\
> 4x + 1y &= 10 \\
> \end{aligned}
> $$
>
> - With coefficients on the left and the single constant on the right
> - Horizontally line-by-line (rows)
> - Stacked vertically (columns)
>
>
> We will continue this trend with:
>
> - **coefficients as rows (left)**
> - **constants as columns (right)**

Thus, we reached a form that is standard for use in matrix multiplication

> [!Example] Standard Form
> **Coefficients matrix** (left) → read by **row**
> **Constants matrix** (right) → read by **column**

---

## 🔵 Dot Product in Matrices

Each entry $c_{ij}$ in the **resultant matrix** is computed as a **dot product** between:

- The **$i^{\text{th}}$ row** of matrix $A$:
  $$
  \mathbf{a_{ip}} = [a_{i1},\ a_{i2},\ a_{i3}, \cdots,\ a_{ip},]
  $$

- The **$j^{\text{th}}$ column** of matrix $B$:
  $$
  \mathbf{b_{pj}} =
  \begin{bmatrix}
  b_{1j} \\
  b_{2j} \\
  b_{3j} \\
  \vdots \\
  b_{pj} \\
  \end{bmatrix}
  $$
- Where $p$ is a shared dimension

> [!tip] Matching Elements
> As the **number of elements in the row of the left matrix** must be the **same** as the **number of elements in the column of the right matrix** for **dot product** to work
>
> This is equivalent to just checking the **columns of the left matrix** and the **rows of the right matrix** respectively

> [!info] Dot Product Entry
> Each **entry** in the **resultant matrix** is represented by this
> $$
> \begin{aligned}
> c_{ij} &= \mathbf{a_{ip}} \cdot \mathbf{b_{pj}} \\
> &= a_{i1} \cdot b_{1j} + a_{i2} \cdot b_{2j} + a_{i3} \cdot b_{3j} + \cdots
> \end{aligned}
> $$

---

### 📌 Coefficients Matrix

Each **row** of the **left coefficients matrix** contributes to each row of the result

$$
\begin{bmatrix}
\textcolor{darkorange}{\boxed{\mathbf{2}}} & \textcolor{darkorange}{\boxed{\mathbf{3}}} \\
\textcolor{green}{\boxed{\mathbf{4}}} & \textcolor{green}{\boxed{\mathbf{1}}}
\end{bmatrix}
\cdot
\begin{bmatrix}
\textcolor{darkgray}{5} & \textcolor{darkgray}{6} \\
\textcolor{darkgray}{7} & \textcolor{darkgray}{8}
\end{bmatrix}
=
\begin{bmatrix}
\textcolor{darkorange}{
 \boxed{
  \textcolor{darkorange}{\mathbf{2}} \cdot \textcolor{darkgray}{5}
  \textcolor{darkgray}{+}
  \textcolor{darkorange}{\mathbf{3}} \cdot \textcolor{darkgray}{7}
 }
}&
\textcolor{darkorange}{
 \boxed{
  \textcolor{darkorange}{\mathbf{2}} \cdot \textcolor{darkgray}{6}
  \textcolor{darkgray}{+}
  \textcolor{darkorange}{\mathbf{3}} \cdot \textcolor{darkgray}{8}
 }
}\\
\textcolor{green}{
 \boxed{
  \textcolor{green}{\mathbf{4}} \cdot \textcolor{darkgray}{5}
  \textcolor{darkgray}{+}
  \textcolor{green}{\mathbf{1}} \cdot \textcolor{darkgray}{7}
 }
}&
\textcolor{green}{
 \boxed{
  \textcolor{green}{\mathbf{4}} \cdot \textcolor{darkgray}{6}
  \textcolor{darkgray}{+}
  \textcolor{green}{\mathbf{1}} \cdot \textcolor{darkgray}{8}
 }
}
\end{bmatrix}
=
\begin{bmatrix}
31 & 36 \\
27 & 32
\end{bmatrix}
$$

### 🎯 Constants Matrix

Each **column** of the **right constants matrix** contributes to each column of the result.

$$
\begin{bmatrix}
\textcolor{darkgray}{2} & \textcolor{darkgray}{3} \\
\textcolor{darkgray}{4} & \textcolor{darkgray}{1}
\end{bmatrix}
\cdot
\begin{bmatrix}
\textcolor{blue}{\boxed{\mathbf{5}}} & \textcolor{red}{\boxed{\mathbf{6}}} \\
\textcolor{blue}{\boxed{\mathbf{7}}} & \textcolor{red}{\boxed{\mathbf{8}}}
\end{bmatrix}
=
\begin{bmatrix}
\textcolor{blue}{
 \boxed{
  \textcolor{darkgray}{2} \cdot \textcolor{blue}{\mathbf{5}}
  \textcolor{darkgray}{+}
  \textcolor{darkgray}{3} \cdot \textcolor{blue}{\mathbf{7}}
 }
}&
\textcolor{red}{
 \boxed{
  \textcolor{darkgray}{2} \cdot \textcolor{red}{\mathbf{6}}
  \textcolor{darkgray}{+}
  \textcolor{darkgray}{3} \cdot \textcolor{red}{\mathbf{8}}
 }
} \\
\textcolor{blue}{
 \boxed{
  \textcolor{darkgray}{4} \cdot \textcolor{blue}{\mathbf{5}}
  \textcolor{darkgray}{+}
  \textcolor{darkgray}{1} \cdot \textcolor{blue}{\mathbf{7}}
 }
}&
\textcolor{red}{
 \boxed{
  \textcolor{darkgray}{4} \cdot \textcolor{red}{\mathbf{6}}
  \textcolor{darkgray}{+}
  \textcolor{darkgray}{1} \cdot \textcolor{red}{\mathbf{8}}
 }
}
\end{bmatrix}
=
\begin{bmatrix}
31 & 36 \\
27 & 32
\end{bmatrix}
$$

---
### 🌐 Combined Matrix

$$
\begin{bmatrix}
\textcolor{darkorange}{\boxed{2}} & \textcolor{darkorange}{\boxed{3}} \\
\textcolor{green}{\boxed{4}} & \textcolor{green}{\boxed{1}}
\end{bmatrix}
\cdot
\begin{bmatrix}
\textcolor{blue}{\boxed{5}} & \textcolor{red}{\boxed{6}} \\
\textcolor{blue}{\boxed{7}} & \textcolor{red}{\boxed{8}}
\end{bmatrix}
=
\begin{bmatrix}
	\textcolor{darkorange}{2} \cdot \textcolor{blue}{5}
	+\,
	\textcolor{darkorange}{3} \cdot \textcolor{blue}{7}&
	\textcolor{darkorange}{2} \cdot \textcolor{red}{6}
	+\,
	\textcolor{darkorange}{3} \cdot \textcolor{red}{8}\\
	\textcolor{green}{4} \cdot \textcolor{blue}{5}
	+\,
	\textcolor{green}{1} \cdot \textcolor{blue}{7}&
	\textcolor{green}{4} \cdot \textcolor{red}{6}
	+\,
	\textcolor{green}{1} \cdot \textcolor{red}{8}
\end{bmatrix}
=
\begin{bmatrix}
31 & 36 \\
27 & 32
\end{bmatrix}
$$

---

## 🔮 What is Matrix Multiplication

And thus **Matrix Multiplication** is the **standardised** application of **dot products** where its numbers are **organised** in rows and columns

> [!info] Overview
> Each entry in the result matrix is a **related sum of products**—a dot product—between:
>
> - A **row** from the **left coefficient matrix**
> - A **column** from the **right constant matrix**
>
> Where
>
> - **Number of columns in the left matrix = Number of rows in the right matrix**

---

# 🏪 Linear Combination of Columns

Similarly, matrix multiplication is also a *linear combination of columns of the left matrix*

Where each **column** on the **right constant matrix** determines the **corresponding column in the resultant matrix** 
- A linear combination of **columns in the left coefficient matrix**

$$
\begin{align*}
\begin{pmatrix} 
	2 & 3 \\ 4 & 1 
\end{pmatrix} 
\begin{pmatrix} 
	\textcolor{blue}{\mathbf{5}} & \textcolor{red}{\mathbf{6}} \\ 
	\textcolor{blue}{\mathbf{7}} & \textcolor{red}{\mathbf{8}} 
\end{pmatrix} &=
\begin{pmatrix}
  \begin{pmatrix} 
	  2 \\ 4 
  \end{pmatrix}
  \textcolor{blue}{\mathbf{5}}
  + 
  \begin{pmatrix} 
  3 \\ 1 
  \end{pmatrix}
  \textcolor{blue}{\mathbf{7}} &
  \begin{pmatrix} 
  2 \\ 4 
  \end{pmatrix}
  \textcolor{red}{\mathbf{6}} 
  + 
  \begin{pmatrix} 
  3 \\ 1 
  \end{pmatrix}
  \textcolor{red}{\mathbf{8}}
\end{pmatrix} \\
&=
\begin{pmatrix}
  \begin{pmatrix} 10 \\ 20 \end{pmatrix} + \begin{pmatrix} 21 \\ 7 \end{pmatrix} &
  \begin{pmatrix} 12 \\ 24 \end{pmatrix} + \begin{pmatrix} 24 \\ 8 \end{pmatrix}
\end{pmatrix} \\
&=
\begin{pmatrix} 31 & 36 \\ 27 & 32 \end{pmatrix}
\end{align*}
$$

---

# 🚣 Linear Combination of Rows

Matrix multiplication is also a *linear combination of rows of the right matrix*

Each **row** on the **left coefficient matrix** determines the **corresponding row in the resultant matrix** 
- A linear combination of **rows in the right constant matrix**

$$
\begin{align*}
	\begin{pmatrix} 
		\mathbf{\textcolor{darkorange}{2}} & \mathbf{\textcolor{darkorange}{3}} \\ 
		\mathbf{\textcolor{green}{4}} & \mathbf{\textcolor{green}{1}} 
	\end{pmatrix} 
	\begin{pmatrix} 
		5 & 6 \\ 
		7 & 8 
	\end{pmatrix} 
	&=
	\begin{pmatrix}
		\mathbf{\textcolor{darkorange}{2}} 
		\begin{pmatrix} 
			5 & 6 
		\end{pmatrix} 
		+ \mathbf{\textcolor{darkorange}{3}} 
		\begin{pmatrix} 
			7 & 8 
		\end{pmatrix} \\
		\mathbf{\textcolor{green}{4}} 
		\begin{pmatrix} 
			5 & 6 
		\end{pmatrix}
		+ \mathbf{\textcolor{green}{1}} 
		\begin{pmatrix} 
			7 & 8 
		\end{pmatrix}
	\end{pmatrix} \\
&=
\begin{pmatrix}
  \begin{pmatrix} 10 & 12 \end{pmatrix} + \begin{pmatrix} 21 & 24 \end{pmatrix} \\
  \begin{pmatrix} 20 & 24 \end{pmatrix} + \begin{pmatrix} 7 & 8 \end{pmatrix}
\end{pmatrix} \\
&=
\begin{pmatrix} 31 & 36 \\ 27 & 32 \end{pmatrix}
\end{align*}
$$

---

## Outer Product Form

From analysing the original dot product form, we can also see this pattern

$$
\begin{align*}
\begin{bmatrix}
\textcolor{darkorange}{2} & \textcolor{darkorange}{3} \\
\textcolor{green}{4} & \textcolor{green}{1}
\end{bmatrix}
\begin{bmatrix}
\textcolor{blue}{5} & \textcolor{red}{6} \\
\textcolor{blue}{7} & \textcolor{red}{8}
\end{bmatrix}
&=
\underbrace{
    \begin{bmatrix} \textcolor{darkorange}{2} \\ \textcolor{green}{4} \end{bmatrix}
    \begin{bmatrix} \textcolor{blue}{5} & \textcolor{red}{6} \end{bmatrix}
}_{\text{Rank 1 Matrix 1}}
+
\underbrace{
    \begin{bmatrix} \textcolor{darkorange}{3} \\ \textcolor{green}{1} \end{bmatrix}
    \begin{bmatrix} \textcolor{blue}{7} & \textcolor{red}{8} \end{bmatrix}
}_{\text{Rank 1 Matrix 2}} \\
&=
\begin{bmatrix}
  \textcolor{darkorange}{2} \cdot \textcolor{blue}{5} & \textcolor{darkorange}{2} \cdot \textcolor{red}{6} \\
  \textcolor{green}{4} \cdot \textcolor{blue}{5} & \textcolor{green}{4} \cdot \textcolor{red}{6}
\end{bmatrix}
+
\begin{bmatrix}
  \textcolor{darkorange}{3} \cdot \textcolor{blue}{7} & \textcolor{darkorange}{3} \cdot \textcolor{red}{8} \\
  \textcolor{green}{1} \cdot \textcolor{blue}{7} & \textcolor{green}{1} \cdot \textcolor{red}{8}
\end{bmatrix} \\
&=
\begin{bmatrix}
  10 & 12 \\
  20 & 24
\end{bmatrix}
+
\begin{bmatrix}
  21 & 24 \\
  7 & 8
\end{bmatrix} \\
&=
\begin{bmatrix}
  10+21 & 12+24 \\
  20+7 & 24+8
\end{bmatrix} \\
&=
\begin{bmatrix} 31 & 36 \\ 27 & 32 \end{bmatrix}
\end{align*}
$$

---
## 🟧 Block Multiplication

Not only does individual elements work, but it also extends to matrices themselves to be multiplied like elements in matrix multiplication. 
> I will use the same example here which is not very descriptive, but it is very complicated to do a proper example. 
> 
> But this example will show you a picture of how it is

$$
\begin{align*}
\begin{bmatrix}
\textcolor{darkorange}{2} & \textcolor{darkorange}{3} \\
\textcolor{green}{4} & \textcolor{green}{1}
\end{bmatrix}
\cdot
\begin{bmatrix}
\textcolor{blue}{5} & \textcolor{red}{6} \\
\textcolor{blue}{7} & \textcolor{red}{8}
\end{bmatrix}
&=
\begin{bmatrix}
    \textcolor{darkorange}{\mathbf{A}_{11}}\textcolor{blue}{\mathbf{B}_{11}} + \textcolor{darkorange}{\mathbf{A}_{12}}\textcolor{blue}{\mathbf{B}_{21}} & \textcolor{darkorange}{\mathbf{A}_{11}}\textcolor{red}{\mathbf{B}_{12}} + \textcolor{darkorange}{\mathbf{A}_{12}}\textcolor{red}{\mathbf{B}_{22}} \\
    \textcolor{green}{\mathbf{A}_{21}}\textcolor{blue}{\mathbf{B}_{11}} + \textcolor{green}{\mathbf{A}_{22}}\textcolor{blue}{\mathbf{B}_{21}} & \textcolor{green}{\mathbf{A}_{21}}\textcolor{red}{\mathbf{B}_{12}} + \textcolor{green}{\mathbf{A}_{22}}\textcolor{red}{\mathbf{B}_{22}}
\end{bmatrix} \\
&=
\begin{bmatrix}
    (\textcolor{darkorange}{2} \cdot \textcolor{blue}{5}) + (\textcolor{darkorange}{3} \cdot \textcolor{blue}{7}) & (\textcolor{darkorange}{2} \cdot \textcolor{red}{6}) + (\textcolor{darkorange}{3} \cdot \textcolor{red}{8}) \\
    (\textcolor{green}{4} \cdot \textcolor{blue}{5}) + (\textcolor{green}{1} \cdot \textcolor{blue}{7}) & (\textcolor{green}{4} \cdot \textcolor{red}{6}) + (\textcolor{green}{1} \cdot \textcolor{red}{8})
\end{bmatrix} \\
&=
\begin{bmatrix}
    (\textcolor{darkorange}{10} + \textcolor{darkorange}{21}) & (\textcolor{darkorange}{12} + \textcolor{darkorange}{24}) \\
    (\textcolor{green}{20} + \textcolor{green}{7}) & (\textcolor{green}{24} + \textcolor{green}{8})
\end{bmatrix} \\
&=
\begin{bmatrix}
    31 & 36 \\
    27 & 32
\end{bmatrix} \\
&= 
\begin{bmatrix} 
	\mathbf{C}_{11} & \mathbf{C}_{12} \\ 
	\mathbf{C}_{21} & \mathbf{C}_{22} 
\end{bmatrix}
\end{align*}
$$