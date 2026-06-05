---
title: "📂 Python File Modes"
date: 2025-11-08
draft: false
---

## 📌 Motivation

File modes define how Python interacts with files—whether reading, writing, appending, or combining operations. Understanding these modes is essential for safe I/O, audit clarity, and avoiding silent data loss.

---

## 🧩 Text Mode Variants

| Mode   | Read | Write | Truncate | Create | Pointer | Notes                          |
|--------|------|-------|----------|--------|---------|--------------------------------|
| `'r'`  | ✅   | ❌    | ❌       | ❌     | Start   | Fails if file doesn't exist    |
| `'r+'` | ✅   | ✅    | ❌       | ❌     | Start   | Read/write, no truncation      |
| `'w'`  | ❌   | ✅    | ✅       | ✅     | Start   | Overwrites file                |
| `'w+'` | ✅   | ✅    | ✅       | ✅     | Start   | Read/write with truncation     |
| `'a'`  | ❌   | ✅    | ❌       | ✅     | End     | Appends only                   |
| `'a+'` | ✅   | ✅    | ❌       | ✅     | End     | Read/append, pointer at end    |
| `'x'`  | ❌   | ✅    | ❌       | ✅     | Start   | Fails if file exists           |

---

## 🧬 Binary Mode Variants

| Mode    | Read | Write | Truncate | Create | Pointer | Notes                          |
|---------|------|-------|----------|--------|---------|--------------------------------|
| `'rb'`  | ✅   | ❌    | ❌       | ❌     | Start   | Binary read                    |
| `'rb+'` | ✅   | ✅    | ❌       | ❌     | Start   | Binary read/write              |
| `'wb'`  | ❌   | ✅    | ✅       | ✅     | Start   | Binary write, overwrites       |
| `'wb+'` | ✅   | ✅    | ✅       | ✅     | Start   | Binary read/write with truncation |
| `'ab'`  | ❌   | ✅    | ❌       | ✅     | End     | Binary append only             |
| `'ab+'` | ✅   | ✅    | ❌       | ✅     | End     | Binary read/append             |

---

## 🧬 Feature Definitions

### 📖 `Read`

- Grants permission to access file contents via `.read()`, `.readline()`, etc.
- If omitted, read operations raise `io.UnsupportedOperation`.

### ✍️ `Write`

- Grants permission to modify file contents via `.write()`, `.writelines()`.
- If omitted, write operations raise `io.UnsupportedOperation`.

### 🧨 `Truncate`

- Clears the file contents upon opening.
- Enabled in `'w'`, `'w+'`, `'wb'`, `'wb+'`.

### 🆕 `Create`

- Creates the file if it doesn’t exist.
- Enabled in `'w'`, `'w+'`, `'a'`, `'a+'`, `'x'`.

### 📍 `Pointer`

- Defines where the file cursor starts:
  - `'r'`, `'w'`, `'w+'` → Start of file
  - `'a'`, `'a+'` → End of file
- Affects `.seek()` and `.tell()` behavior.

---

## 🔍 Mode Behavior Summary

- `'r'` / `'rb'`: Read-only. File must exist.
- `'r+'` / `'rb+'`: Read/write. No truncation. File must exist.
- `'w'` / `'wb'`: Write-only. Truncates file. Creates if missing.
- `'w+'` / `'wb+'`: Read/write. Truncates file. Creates if missing.
- `'a'` / `'ab'`: Append-only. Pointer at end. Creates if missing.
- `'a+'` / `'ab+'`: Read/append. Pointer at end. Creates if missing.
- `'x'`: Exclusive creation. Fails if file exists.

---

## 🧠 Vault Integration Flags

- `FileMode::AccessMatrix`
- `Audit::TruncationRisk`
- `Pointer::Start vs End`
- `Binary::EncodingImplications`
- `Resilience::ExistenceCheck`
- `Vault::OpenModeAnchors`

---

🧩 Want to scaffold a module comparing file pointer behavior, or benchmark read/write performance across modes and buffer sizes?
