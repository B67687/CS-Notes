---
title: "🧭 Git Commands"
date: 2025-11-08
draft: false
---

Git is a version controls system, and here are the commands that you ought to know to navigate this control system effectively

---

### 🔰 1. Initialization & Setup
| Command | Purpose |
|--------|---------|
| `git init` | Create a new Git repo locally |
| `git clone <url>` | Clone a remote repo |
| `git remote -v` | View remote URLs (`origin`, `upstream`) |
| `git remote add origin <url>` | Link local repo to GitHub |
| `git remote remove upstream` | Remove noisy upstream tracking |

---

### 📦 2. Staging & Committing
| Command | Purpose |
|--------|---------|
| `git status` | See current changes and branch state |
| `git add <file>` | Stage a file for commit |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit staged changes with a message |
| `git log` | View commit history |

---

### 🚀 3. Pushing & Pulling
| Command | Purpose |
|--------|---------|
| `git push origin main` | Push local commits to GitHub |
| `git pull origin main` | Pull latest changes from GitHub |
| `git fetch` | Update remote tracking info without merging |
| `git merge origin/main` | Merge fetched changes into local branch |

---

### 🌿 4. Branching
| Command | Purpose |
|--------|---------|
| `git branch` | List local branches |
| `git branch <name>` | Create a new branch |
| `git checkout <name>` | Switch to a branch |
| `git switch -c <name>` | Create and switch to a branch (modern) |
| `git push origin <branch>` | Push new branch to GitHub |
| `git branch -d <name>` | Delete local branch |
| `git branch --set-upstream-to=origin/main` | Rebind tracking to your own repo |

---

### 🧹 5. Undo & Cleanup
| Command | Purpose |
|--------|---------|
| `git restore <file>` | Undo changes to a file |
| `git reset HEAD <file>` | Unstage a file |
| `git reset --hard` | Reset everything to last commit (⚠️ destructive) |
| `git clean -fd` | Remove untracked files and folders (⚠️ destructive) |

---

### 🧪 6. Validator Audit & Diff
| Command | Purpose |
|--------|---------|
| `git diff` | See unstaged changes |
| `git diff --cached` | See staged changes |
| `git show <commit>` | Inspect a specific commit |
| `git blame <file>` | See who changed each line |
