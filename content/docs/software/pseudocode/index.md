---
title: "🔮 Pseudocode"
date: 2025-11-08
draft: false
---

Pseudocode is a plain-language way to describe algorithms and logic without worrying about programming syntax.

It’s ideal for planning, teaching, and auditing workflows.

---

## 🛠️  Features

| Principle             | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **Language-agnostic** | Avoid specific programming syntax; use plain English                        |
| **Structured**        | Use control flow keywords (IF, FOR, WHILE, etc.)                            |
| **Readable**          | Indent blocks and use whitespace for clarity                                |
| **Declarative**       | Focus on *what* the algorithm does, not *how* it’s implemented              |
| **Consistent**        | Maintain uniform naming and formatting throughout                           |

---

## ✅ Best Practices

- `START` and `END` to denote blocks of code
  - The start and end of the whole code
  - The start and end of functions, loops and conditionals (*e.g. FUNCTION ... END FUNCTION, FOR ... END FOR, IF ... END IF*)
- `DECLARE` for introducing new variables (*e.g., DECLARE x*)
- `SET` for assigning values to variables (*e.g., SET x to 5*)
- `NOT`, `AND`, `OR` for readable logic operators
- `MOD`, `DIV` for readable arithmetic operators
- `IF`, `ELSE`, `ELSE IF` for conditionsls
- `WHILE`, `FOR`, `IN`, `OF` for looping (*e.g. FOR each item IN list, FOR key IN dictionary*)
- `REPEAT ... UNTIL condition` can alternatively be used
- `EXIT`/`BREAK` to leave the loop early, `CONTINUE` to skip to the next iteration
- `INPUT`/`OUTPUT` or `PRINT` to define user input and function output
- `//` for comments, to explain non-obvious steps
- `TRY`, `CATCH`, `RAISE ERROR` for error-handling
- `FUNCTION (params)` and `RETURN` to define reusable logic
- `CALL` to invoke a function
- Avoid data types, semicolons, or language-specific syntax
- Use indentation and spacing for readability
- Use section headers (`// --- Section Name ---`) for long logic blocks

---

## 🌸 Example

```plaintext

// --- Function Definition ---
FUNCTION computeAverage(sum, quantity)
  TRY
    IF quantity == 0 THEN
      RAISE ERROR "Division by zero"
    ELSE
      SET average to sum DIV quantity
      PRINT "Average of even numbers: " + average
    END IF
  CATCH error
    PRINT "Error: " + error
  END TRY
END FUNCTION

START
  // --- Input ---
  INPUT numberList

  // --- Processing ---
  DECLARE total
  DECLARE count
  SET total to 0
  SET count to 0

  FOR each number IN numberList
    IF number MOD 2 == 0 THEN
      SET total to total + number
      SET count to count + 1
    END IF
  END FOR

  // --- Output ---
  IF count == 0 THEN
    PRINT "No even numbers found."
  ELSE
    CALL computeAverage(total, count)
  END IF
END

```
