---
title: "🔁 Subtraction Through Addition — Method of Complements"
date: 2025-11-08
draft: false
---

> [!Info] Why we invented this
> The method of complements exists to optimise for addition by optimising subtraction in places where there is subtraction
>
> Computers can only **add** can still perform subtraction if we introduce a redundant term that can be easily removed—such as the next bigger place-value
>
> Turning the ***subtracted term*** into an ***addition term***
>
> Thus, we have managed to generalise the problem of subtracting ***through addition in modular arithmetic*** plus removal of leading digit

## 📜 Example of how this works

```text
Goal: Make Subtractions be in terms of Addition
==> A - B, where A >= B
```
$$
\begin{align}
	&73 - 47 \\ 
	= \space & 73 - 47 + 100 - 100 \\
	= \space & 73 + (100 - 47) - 100 \\
	= \space & 73 + 53 - 100 \\
	= \space & 126 - 100 \\
	= \space & 26
\end{align}
$$

```json
(100 - 47) is the 10's complement of 73
(-100) is the remover of the leading digit, 
```

If we extend this idea further, **removing the leading digit** is the same as caring about ***grouping numbers within a fixed range***
- `mod` is a math sign invented to mean *"keep only the digits within this range"*

This concept is then extended for **calculations** involving fixed ranges, called **modulo arithmetic**
- In this case, removing `100` from the answer is equivalent to keeping the digits within `100`
- So instead of `-100`, we could generally do `... mod 100`

And since we group numbers according to a fixed range, when numbers **exceed the range**, it will *appear to loop back to the start* of this fixed range

Thus, circular properties are present in systems using fixed ranges to represent numbers.

For example, the *2's complement system for representing binary numbers in computers*

In the following sections, we will extend the explanation more generally

---

## 🔧 Successor to the Most-Significant Value

Let `S(x)` be the next significant place,  where the `S` stands for **Successor of place-value**
i.e.

```plaintext
If x is some number where r is the radix, and n is highest power of that radix

Then S(x) = r^(n + 1)
```

Where

```plaintext
S(13)   = 100
S(99)   = 100
S(123)  = 1000
S(1234) = 10000
```

## 🧮 Subtraction Setup Using S(A)

We set up `MSV Redundancy` by doing this

```plaintext
A − B
= A − B + S(A) − S(A)
```

Which allows us to convert `- S(A)` to `mod S(A)`

```plaintext
A − B
= A − B + S(A) − S(A)
--------------------------
= [A − B + S(A)] mod S(A)
```

Then we group the subtractive components together, that will be used for pre-calculation

```plaintext
A − B
= A − B + S(A) − S(A)
= [A − B + S(A)] mod S(A)
------------------------------
= {A + [ S(A) − B ]} mod S(A)
```

Let `S(A) − B` be the `r`'s complement of `B`, denoted `B'`.

> [!Note]
> $r^{n+1} - B$ is known as the `Radix Complement`
>
> - We take the difference between `the number that represents the next level of grouping` and the `subtrahend`

```plaintext
A − B
= A − B + S(A) − S(A)
= A − B + S(A) mod S(A)
= {A + [ S(A) − B ]} mod S(A)
------------------------------
= (A + B') mod S(A)
```

We have thus converted it to just **addition** and the **removal of the MSV**

### ✅ Subtraction through Radix Complement

```plaintext
A − B
= (A + B') mod S(A)
```
> Where `B'` , which is `S(A) - B`, is the `Radix Complement`—— $\boxed{ \phantom{\big(} r^{n+1} - B \phantom{\big)}}$

---

## ⚙️ Optimizing for Per-Place Operation

Since, we still want the convenience of `removing the MSV after calculation`, we will keep using the `MSV redundancy technique`

However, instead of taking `subtraction directly from the MSV`,  we can instead `subtract from MSV - 1` for its convenient place-value calculation——as we simply subtract from `radix - 1` at every place-value.

- The extra `1` that is taken out of `MSV` must be accounted for

Here's how it goes:

We set up `MSV Redundancy` by doing this

```plaintext
A − B
= A − B + S(A) − S(A)
```

Which allows us to convert `- S(A)` to `mod S(A)`

```plaintext
A − B
= A − B + S(A) − S(A)
--------------------------
= [A − B + S(A)] mod S(A)
```

Then we set up for `subtraction from MSV - 1` by balancing the `1`s like so

```plaintext
A − B
= A − B + S(A) − S(A)
= [A − B + S(A)] mod S(A)
--------------------------------------
= {[ A − B + S(A) - 1 ] mod S(A)} + 1
```

> [!Note]
> We can do `{... mod S(A)} + 1` because `S(A)` is always going to be bigger than `1`, which is also the smallest place-unit that exists—`r^0`
>
> >`S(A)` is minimally going to be `r^1` which is `r` itself
> >
> > Or honestly you could just account for it before applying `modulo`

Then we group the subtractive components together, that will be used for pre-calculation

```plaintext
A − B
= A − B + S(A) − S(A)
= [A − B + S(A)] mod S(A)
= {[ A − B + S(A) - 1 ] mod S(A)} + 1
----------------------------------------
= [{ A + [S(A) - 1 - B] } mod S(A)] + 1
```

Where now `B' = S(A) − 1 − B`, which we will call the `r - 1`'s complement of `B`

> [!Note]
> This form:  `r^(n+1) - 1 - B` is known as the `Diminished Radix Complement`,
>
> - We take the difference between `the maximum representable value in n+1 digits`——the number of digits is always `1` more than the highest place-value power——and the `subtrahend`

```plaintext
A − B
= A − B + S(A) − S(A)
= [A − B + S(A)] mod S(A)
= {[ A − B + S(A) - 1 ] mod S(A)} + 1
= [{ A + [S(A) - 1 - B] } mod S(A)] + 1
----------------------------------------
= [ (A + B') mod S(A) ] + 1
```

Thus, we reached the optimal setup for per-place operation that maximises addition-only operations, by pre-calculating one subtraction. And adding `1` at the end.

### ✅ Subtraction through Diminished Radix Complement
>
> ```plaintext
> A − B
> = [ (A + B') mod S(A) ] + 1
> ```
>
> Where `B'`, which is `S(A) - 1 - B`, is the `Diminished Radix Complement`—— $\boxed{ \phantom{\big(} r^{n+1} - 1 - B \phantom{\big)}}$

## Conclusion

> [!NOTE]
> **Radix Complement—————————** `r^(n+1) - B`
> **Diminished Radix Complement————** `r^(n+1) - 1 - B`
>
> - Thus we notice that also:
 > `Diminished Radix Complement` = `Radix Complement` - `1`

> - Or similarly:
 > `Radix Complement` = `Diminished Radix Complement` + `1`
