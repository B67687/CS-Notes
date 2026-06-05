Binary is a base-2 number system, meaning each digit (bit) is either:

- `0` → represents absence
- `1` → represents presence

This minimal digit set gives binary a unique advantage in multiplication.

## 🔢 Multiplication Rules in Binary

- `0 × anything = 0`
- `1 × anything = that thing`

This means:

- If a digit in the multiplier is `0`, the entire row becomes zeros.
- If it's `1`, the row is a **copy** of the multiplicand, just shifted left according to its position.

## 🧮 Example: Multiply `1011 × 110`

```text

      1011   (multiplicand)
   ×   110   (multiplier)
   -------
      0000   ← 0 × 1011 (shifted 0 places)  (full row clear)
     1011    ← 1 × 1011 (shifted 1 place)   (copy of the multiplicand)
+   1011     ← 1 × 1011 (shifted 2 places)  (copy of the multiplicand)
---------
   110110   (final result)

Each row is either:
- All zeros (if the multiplier bit is 0)
- A shifted copy of the multiplicand (if the bit is 1)
```

## 🧭 Why This Doesn’t Work in Other Bases

In other bases (e.g., base 10, base 5), digits range from `0` to `base - 1`. So:

- You can't just copy the multiplicand.
- You must **scale** it by the digit value (e.g., `3 × 245`), which involves actual multiplication and carries.
- Each row becomes a **new computation**, not a simple copy.

## 🔌 Hardware Analogy

In digital circuits:

- A `1` bit acts like a **switch** that connects the multiplicand.
- A `0` bit disconnects it.
- This makes binary multiplication **extremely efficient** in hardware.

## 🧠 Summary

- Binary multiplication is special because of the **identity property of 1**.
- It allows for **row copying** instead of recalculating.
- This shortcut is unique to binary and is one reason it's the foundation of modern computing.

---

> “Binary turns multiplication into a game of switches—copy or ignore. No other base makes it this simple.”
