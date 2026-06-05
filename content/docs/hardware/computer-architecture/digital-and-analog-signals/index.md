---
title: "Digital and Analog Signals"
date: 2025-11-08
draft: false
---


- **Digital signals**: Represent information using discrete levels (commonly two: 0 and 1).
- **Analog signals**: Represent information using continuous variation over time.

### My understanding

- In practice, digital is only *relatively* discrete and analog is only *relatively* continuous — perfect separation doesn’t exist due to physical limitations like noise, quantization errors, and bandwidth limits.
- We can **treat** digital signals as discrete and analog signals as continuous for design purposes.
- Digital signals are threshold-controlled:
  - Any value above the high threshold is treated as logic 1.
  - Any value below the low threshold is treated as logic 0.
- This makes digital signals not easily affected by small noise.

### Analog noise susceptibility

- Analog signals record the exact amplitude at every moment, so even tiny changes (from electrical noise, interference, or distortion) directly change the output.
- No threshold protection — a small variation is still a real change in the analog value.
- Over long distances or processing steps, noise accumulates and degrades quality.

---

# Codes

## Binary-Coded Decimal (BCD)

- **Definition**: Each decimal digit (0–9) is represented separately in binary using **4 bits**.
- **My understanding**:
  - Instead of converting the whole number to binary, each digit is converted individually.
  - Requires 4 bits because the highest decimal digit `9` is `1001` in binary.
  - The nearest power of 2 less than 9 is 8 (2³), so we need an extra bit to represent 9 → total of 4 bits.
  - This makes conversion and decimal arithmetic simpler in hardware at the expense of more storage.

### Carry adjustment rule in addition

- After `1001` (9), the next binary value is `1010` (10), which is invalid in BCD.
- The difference between 2⁴ (16) and the next valid decimal after 9 is **6**.
- In BCD arithmetic, if a 4-bit group exceeds `1001`, we **add 6** to reset the count and carry over.

---

# Serial vs. Parallel Transmission

## My understanding

### Serial transmission

- Data is transmitted within the same line, one after another.
- **(+)** Easy to ensure predictable ordered arrival.
- **(-)** Slower per clock cycle since all bits use the same “highway”.
- **(+)** Simpler single-cable setup → easier long-range maintenance.

### Parallel transmission

- More than one channel for transmission.
- **(-)** Less predictable timing due to multiple channels.
- **(++)** Faster by multiples of total channels used.
- **(-)** Requires reassembly and authentication at the end.
- **(-)** Maintenance cost scales with cable count.

## Where each is preferred

- **Serial**: Long-distance, high-speed links (PCIe, SATA, USB, DisplayPort) where multiple synchronized wires would be too costly.
- **Parallel**: Short-distance, high-speed internal connections like DDR RAM between CPU and memory controller, where skew is manageable.
- **Parallel (low-speed)**: Cheap way to boost speed where complexity is easy to handle (e.g., old printer ports).

---

# Clock Cycles / Oscillations

- A **clock signal** is a repeating electrical pulse that synchronizes data transfer and operations.
- Oscillations = clock cycles in this context — they keep time and rhythm so transistors know when to read/send bits.
- Synchronous systems operate on specific clock edges (rising/falling).
- Higher clock = more ops/sec but harder timing design.

---

# Historical Shift Table

| Era           | Interface               | Type     | Notes                                  |
| ------------- | ----------------------- | -------- | -------------------------------------- |
| 1970s–1990s   | Centronics printer port | Parallel | Short distance, low speed (~150 kbps)  |
| 1980s–2000s   | IDE / ATA               | Parallel | 16-bit bus; replaced by SATA           |
| 1990s         | AGP (graphics)          | Parallel | Short, fast GPU link; replaced by PCIe |
| 2000s–present | DDR RAM                 | Parallel | Still used due to short distance       |
| 2000s–present | PCI Express (PCIe)      | Serial   | Multiple high-speed serial lanes       |
| 2003–present  | SATA                    | Serial   | Faster, thinner, longer cables         |
| 1996–present  | USB                     | Serial   | Universal connector, up to 40 Gbps     |
| 2006–present  | DisplayPort / HDMI      | Serial   | High-speed video/audio                 |
