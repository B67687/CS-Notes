---
title: "👾 Width Units"
date: 2025-11-08
draft: false
---

There are many **units** used in **Typography**, this note explains them all from their **naming scheme** to its relation to **what it means**

---

## 📐 Etymology and Behavior

| Unit   | Literal Meaning        | Relation to Behavior |
|--------|------------------------|-------------------------------|
| `px`   | **Pixel** = “picture element” | Represents a fixed dot on the screen. The name reflects its atomic role in raster graphics—each `px` is a screen-addressable unit. |
| `em`   | **M-width** (typography) | Historically the width of the letter “M” in the current font. In CSS, it scales with the font size of the parent—mirroring how “M” was a typographic standard for spacing. |
| `rem`  | **Root em**             | Same as `em`, but relative to the root (`html`) font size. The name reflects its inheritance logic: “root-relative M-width.” |
| `%`    | **Percent** = “per hundred” | Directly reflects its behavior: 50% of parent width means half. The name is mathematically literal. |
| `vh`   | **Viewport height**     | 1vh = 1% of the visible screen height. The name is a direct spatial reference to the browser’s vertical dimension. |
| `vw`   | **Viewport width**      | 1vw = 1% of the visible screen width. Again, the name is spatially literal. |
| `pt`   | **Point** (print unit)  | 1pt = 1/72 inch. The name reflects its origin in physical typesetting—used for print precision. |
| `ch`   | **Character width**     | Width of the “0” character. The name reflects its use in monospace layout—ideal for input fields or code blocks. |
| `ex`   | **x-height**            | Height of lowercase “x”. The name reflects its typographic role in vertical rhythm and font metrics. |