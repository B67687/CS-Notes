---
title: "🌐 Unicode"
date: 2025-11-08
draft: false
---

Unicode solves the chaos of incompatible encodings by defining a single, consistent catalog of characters for every language, symbol, and emoji. It’s not an encoding—it’s the **semantic backbone** that encoding schemes like UTF-8, UTF-16, and UTF-32 rely on.

## 🔢 Code Points

- Each character is assigned a unique number: `U+XXXX`
- Example: `'A'` → `U+0041`, `'π'` → `U+03C0`, `'😀'` → `U+1F600`

## 🧩 Planes & Ranges

| Plane Name               | Range             | Notable Content                  |
|--------------------------|-------------------|----------------------------------|
| Basic Multilingual Plane | U+0000–U+FFFF     | Most common scripts, symbols     |
| Supplementary Multilingual | U+10000–U+1FFFF | Historic scripts, rare symbols   |
| Supplementary Ideographic | U+20000–U+2FFFF  | Rare CJK ideographs              |
| Supplementary Special    | U+E0000–U+EFFFF   | Tags, variation selectors        |
| Private Use Areas        | U+E000–U+F8FF, etc| Custom characters (non-standard) |

> 🔍 Unicode currently defines over 143,000 characters across 159 scripts.

## 🧬 Character Properties

- **General Category**: Letter, Number, Symbol, Punctuation, etc.
- **Combining Class**: Used for accents and diacritics
- **Bidirectional Class**: Controls rendering for RTL scripts
- **Script**: Latin, Cyrillic, Arabic, Han, etc.

## 🔄 Normalization Forms

| Form   | Description                            | Use Case                        |
|--------|----------------------------------------|----------------------------------|
| NFC    | Composed form                          | Web, file systems                |
| NFD    | Decomposed form                        | Canonical comparison             |
| NFKC   | Compatibility composed                 | Search, indexing                 |
| NFKD   | Compatibility decomposed               | Audit, equivalence checking      |

> ⚠️ `'é'` can be `U+00E9` (composed) or `U+0065 U+0301` (decomposed). Normalization ensures consistency.

## 🧰 Use Cases

- **Multilingual Text**: Enables consistent rendering across languages
- **Emoji Support**: Unicode defines emoji sequences and modifiers
- **Search & Indexing**: Normalization ensures accurate matching
- **Security Audits**: Prevents spoofing via visually similar characters

## 🧮 Unicode vs Encoding

| Layer         | Role                          | Example                        |
|---------------|-------------------------------|--------------------------------|
| Unicode       | Defines characters             | `'π'` → `U+03C0`               |
| UTF-8         | Encodes Unicode in bytes       | `U+03C0` → `0xCF 0x80`         |
| UTF-16        | Encodes Unicode in 2–4 bytes   | `U+1F600` → `0xD83D 0xDE00`    |
| UTF-32        | Encodes Unicode in 4 bytes     | `U+1F600` → `0x0001F600`       |