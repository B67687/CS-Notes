---
title: "🌐 UTF-8"
date: 2025-11-08
draft: false
---

ASCII was elegant—but limited. UTF-8 solves the multilingual bottleneck while preserving backward compatibility. It’s the default encoding for the web, APIs, and most modern systems. Understanding its byte structure is essential for debugging, protocol design, and semantic integrity.

## 🧠 Core Principles

- **Variable-Length Encoding**: UTF-8 uses 1–4 bytes per character.
- **ASCII-Compatible**: First 128 characters (0–127) are identical to ASCII.
- **Self-Synchronizing**: No byte ambiguity—each byte signals its role.
- **Endian-Agnostic**: Unlike UTF-16/UTF-32, byte order doesn’t matter.

## 🧮 Byte Structure

| Byte Count | Range (Hex)     | Binary Prefix | Code Point Range     | Example Char |
|------------|-----------------|---------------|-----------------------|--------------|
| 1 byte     | 00–7F           | 0xxxxxxx      | U+0000 to U+007F      | A, 1, !       |
| 2 bytes    | C2–DF + 80–BF   | 110xxxxx 10xxxxxx | U+0080 to U+07FF  | é, ç          |
| 3 bytes    | E0–EF + 2x 80–BF| 1110xxxx 10xxxxxx 10xxxxxx | U+0800 to U+FFFF | 中, π         |
| 4 bytes    | F0–F4 + 3x 80–BF| 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx | U+10000 to U+10FFFF | 🧠, 🐉 |

> 🔍 Each start byte identifies the byte-length of the character
> 🔍 Each continuation byte starts with `10`, ensuring no overlap with leading bytes.

## 🧭 Semantic Zones

- **BMP (Basic Multilingual Plane)**: U+0000 to U+FFFF — most common characters.
- **Supplementary Planes**: U+10000+ — emojis, historic scripts, rare symbols.
- **Control & Format Characters**: Invisible but critical (e.g., `ZWJ`, `BOM`).

## 🧰 Use Cases

- **Web Pages**: HTML defaults to UTF-8 (`<meta charset="UTF-8">`)
- **APIs & JSON**: UTF-8 ensures consistent parsing across platforms.
- **Filesystem & CLI**: UTF-8 filenames, logs, and shell output.
- **Multilingual Apps**: Enables global character support without encoding chaos.

## 🧩 UTF-8 vs Other Encodings

| Feature         | UTF-8         | UTF-16        | ASCII         |
|----------------|---------------|---------------|---------------|
| Bit Width      | 8–32 bits     | 16–32 bits    | 7 bits        |
| Compatibility  | ASCII subset  | Not ASCII     | Legacy only   |
| Endianness     | Irrelevant    | Required (BOM)| N/A           |
| Size Efficiency| High for English | High for Asian scripts | Minimal |