There are 2 ways to find min and max:
- 1. Either all of them compare with on another pairwise
- 2. Or all of the compare with one that is assumed first to be the smallest

The method where they compare with each other will take $(n-1)^2$ comparisons if unmodified

If modified to skip comparing with the one that it previously compared to, then it will take 

$$
(n-1) + (n-2) + \cdots + 2 + 1 + 0 = \dfrac{n(n-1)}{2}
$$

comparisons.

If modified to stop comparing once it hits an invalid value, then it will take even less time, with $\dfrac{n(n-1)}{2}$ as the maximum time