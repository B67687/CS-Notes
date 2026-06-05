---
title: "📘 Absolute vs Relative Imports"
date: 2025-11-08
draft: false
---

{{< callout type="info" >}}
**Motivation**
In Python, **absolute imports** refer to import paths that begin at the top-level package, regardless of the importing module’s location.

This often causes confusion when importing sibling modules.
{{< /callout >}}
### 🔍 Common Misconception
>
> “If I’m importing a sibling module, that must be a relative import.”

**Not true.** Even if `test.py` and `randlist.py` live in the same folder, writing:

```python
import sort_utils.randlist
```

is still an **absolute import**, because it starts from the package root (`sort_utils`),
not from the current file’s location.

### ✅ True Relative Import Syntax

To use a relative import, you’d write:

```python
from . import randlist
from .randlist import generate_list
```

The leading dot (`.`) means “from the current package/module,” and this is what Python formally defines as a **relative import**.

---

### 🧠 Summary Table

| Syntax                          | Type      | Resolves From                 |
|----------------------------------|-----------|-------------------------------|
| `import sort_utils.randlist`     | Absolute  | From package root             |
| `from . import randlist`         | Relative  | From current module’s package |
| `import sorting.sort_utils.randlist` | Absolute  | From higher-level package root |
