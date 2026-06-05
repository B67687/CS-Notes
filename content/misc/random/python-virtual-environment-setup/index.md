---
title: "Python Virtual Environment Setup"
date: 2025-11-08
draft: false
---

## Enter Terminal in Code Editors
```bash
ctrl + `            # VS Code/ Sublime Text/ Atom
Alt + F12           # Pycharm
Cmd + Shift + C     # Xcode  
```

## Commands to Execute
```bash
python -m venv .venv                           # Create virtual environment
source .venv/bin/activate                      # Activate (macOS/Linux)
.venv\Scripts\activate                         # Activate (Windows)
pip install jupyter pandas matplotlib seaborn  # Install packages
pip freeze > requirements.txt                  # Save environment snapshot
```

## Why Use `.venv` Instead of `venv`
- Dot prefix makes the folder hidden in Unix-like systems
- Keeps vaults clean and avoids accidental sync/edit
- Recognized by VS Code and Python tooling
- Easy to exclude via `.gitignore`

## What Dot Prefix Means in Filenames
| Prefix | Meaning            | Examples                             |
| ------ | ------------------ | ------------------------------------ |
| `.`    | Hidden file/folder | `.venv`, `.git`, `.obsidian`, `.env` |
| `..`   | Parent directory   | `../assets/`                         |
| `.`    | Current directory  | `./script.py`, `./data.csv`          |
