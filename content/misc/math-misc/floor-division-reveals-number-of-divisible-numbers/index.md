---
title: "🤣 Floor Division Reveals Number of Divisible Numbers"
date: 2025-11-08
draft: false
---

Take something like $\lfloor \dfrac{13}{4} \rfloor$ for example

$$
1, \ 2, \ 3, \ 4, \ 5, \ 6,\ 7,\ 8,\ 9,\ 10,\ 11,\ 12, \ 13
$$

This will be grouped into boxes of size $4$

$$
\boxed{1, \ 2, \ 3, \ 4,} \ \boxed{5, \ 6,\ 7,\ 8,} \ \boxed{9,\ 10,\ 11,\ 12,} \ \boxed{13 \qquad \qquad \phantom{,} }
$$

Floor division will remove the groups that aren't full

$$
\boxed{1, \ 2, \ 3, \ 4,} \ \boxed{5, \ 6,\ 7,\ 8,} \ \boxed{9,\ 10,\ 11,\ 12,} \
\phantom{\boxed{13 \qquad \qquad \phantom{,} }}
$$

Then each multiple of $4$, will be the representing number for each group

$$
\boxed{1, \ 2, \ 3, \ \textcolor{darkgreen}{4},} \ \boxed{5, \ 6,\ 7,\ \textcolor{darkgreen}{8},} \ \boxed{9,\ 10,\ 11,\ \textcolor{darkgreen}{12},} \
\phantom{\boxed{13 \qquad \qquad \phantom{,} }}
$$

Thus, the *number of groups* is also the **number of numbers** divisible by $4$

---

This is a rule true for finding the number of numbers divisible by any number $m$, up to number $n$

$$
\text{Number of numbers divisible by m} = \lfloor \dfrac{n}{m} \rfloor
$$

---

And if we want to find the numbers between $n_{1}$ and $n_{2}$ divisible by $m$, given $n_2$ > $n_1$, we simply find the ***difference of the floor divisions***

$$
\text{Number of numbers divisible by m between} \ n_{2} \ \text{and} \ n_{1} = \lfloor \dfrac{n_2}{m} \rfloor - \lfloor \dfrac{n_1}{m} \rfloor
$$