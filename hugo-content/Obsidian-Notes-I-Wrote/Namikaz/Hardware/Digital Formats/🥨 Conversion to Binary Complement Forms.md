---
title: "🥨 Conversion to Binary Complement Forms"
date: 2025-11-08
draft: false
---

> [!notes] Preface
> When we represent signed integers in binary, we want to optimise it for addition
>
> As seen in [[🔁 Method of Complements| derived expression]], we have 2 ways to achieve it, through finding **radix complement** or the **diminished radix complement**
>
> Would we be able to do **subtraction through addition** through **ignoring carry-overs at place-values bigger than the numbers in operation**
>
> While the **positive binary numbers** can be represented in its original form, the **negative binary numbers** are to be represented in their **complement forms**
>
> As we will see, being binary allows conversion to `1s complement` and `2s complement` to be **no more than simple bit inversion**

## 🧠 Signed Binary Representation via Radix Complements

For signed numbers in binary, since we want to represent them in 1's complement or 2's complement form, we always represent the **absolute value** of that number in either form.

The **sign** is fixed to be `0` or `1` to represent positive or negative.

---

## 🔁 1's Complement

We compute:

```text
2^(n+1) - 1  MINUS  the binary number
```

This is a string of all 1s—same length as the binary number—minus the binary number itself.

```text
11111...111
```

Because the differences between `1` and the **numbers in base 2** are:

```text
1 - 1 = 0
1 - 0 = 1
```

The result is always the **bit-flipped version** of the original number, which is equivalent to the **NOT logical operation**.

Because **bit-flipping at MSB** also turns *positive sign* to *negative sign*
> We can disregard treating the magnitude part separately from the sign.

> [!note] Converting to Negative with Signed Bit
> Notice that **polarity change**——flipping from *positive* to *negative*——is only a feature because the number is expressed in **signed form**
>
> - It is an **optimisation** we make in **binary signed-forms** where the bits exactly represent 2 states——correlating with *positive* and *negative* for the **signed bit**
> - Thus we can directly take the *positive binary number* and convert it to its *negative complement form*
>
> This isn't an inherent property of complements, its just a specific to hardware optimisation specific to **binary signed-forms**

> [!tip] Reversal and Binary
> Because it is just `bitflips` , its `reversal` is also the same procedure

## 🐬 1's Complement Conversion Procedure
>
> [!example] 1's Complement Conversion—and Reversal
> Flip every bit of the number (including the sign bit)

---

## 🔁 2's Complement

Since 2's complement is `1` **more than 1's complement**:

We can simply
> Perform the 1's complement——flip every bit (including the sign bit)
> Add 1 to the result

### 🌊 Ripple Carry Optimisation

> Addition of `1` at the **LSB** causes a **ripple carry** that flips the string of `1`s from the **LSB** rightwards until it hits the first `0`

```text
From ...0111...111
To   ...1000...000
```

Since we performed a **full number bitflip** in the first step

> All the bits that were **consecutive 0s from the LSB up to the first 1**, won't have `net change` because it would have:
>
> - **Bit flip the first time** to a string of 1s from LSB up to the first 0
> - **Bit flip back** to the string of 0s from LSB up to the first 1—when adding one.
>
> The **bits that are after the first 1**, will only have flipped once and thus will have net change——bit-flip

> [!Fun Fact] Permanent Bit
> Because succession——adding 1——is always a bitflip, the `LSB will always flip twice`, and therefore is the only bit that is always preserved in `2's complement conversions`

> [!tip] Reversal and Binary
> Because it is just `bitflips` , its `reversal` is also the same procedure

## 🐬 2's Complement Conversion Procedure

> [!example] 2's Complement Conversion—and Reversal
>
> 1. **Scan** from LSB toward MSB
> 2. **Preserve** all bits up to and including the first `1` encountered
   —**The LSB is always preserved**
> 3. **Flip all remaining bits** to the left (including the sign bit)

---

## 🧩 Philosophical Closure

Such simplicity arises from applying the **method of complements using radixes**, and then applying it to the design of signed binary values.

This is thus no trick, but a intertwined series of optimisations from the properties of *complements* and *binary*
