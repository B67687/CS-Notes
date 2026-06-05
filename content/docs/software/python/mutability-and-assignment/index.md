---
title: "🧠 Mutability and Assignment"
date: 2025-11-08
draft: false
---

Understanding mutability is essential for predicting how Python handles **assignment**, **modification**, and **shared references**.

---

## 🔢 Definitions

- **Immutable Types**: Cannot be changed after creation.
  - Examples: `int`, `float`, `str`, `tuple`, `frozenset`, `bool`
- **Mutable Types**: Can be changed in place.
  - Examples: `list`, `dict`, `set`

---

## 🟢 Mutable Behavior — Shared References

Mutable objects retain identity across assignments.

```python
list_a = [1, 2, 3]
list_b = list_a  # Both refer to the same object

list_b.append(4)
list_b[0] = 99

print(list_a)  # Output: [99, 2, 3, 4]
```

---

## 🔴 Immutable Behavior — New Object on Change

Immutable objects cannot be changed in place. Any "modification" creates a new object.

### String Example

```python
str_a = "hello"
str_b = str_a

str_b = "world"

print(str_a)  # hello
print(str_b)  # world
```

### Integer Example

```python
x = 5
y = x

x = 6

print(x, y)  # 6, 5
```

---

## 🔗 Variable Assignment = Name Binding

- `a = b = 0` → both `a` and `b` refer to the same object (`0`)
- Reassignment (`a = a + 1`) creates a **new object** for `a`
- Mutation (`a += [2]`) may modify the object **in place**

---

## 🧠 Addition and Equality Notation

There are 2 ways to modify a variable through the addition and equality notation:
> `a += i`
>
> `a = a + i`

### ⚠️ Immutable Types
>
> Let
> `a = 0`
>
> To increment, we do:
> `a += 1`
>
> It looks like the object is changing value in-place.
>
> But it is actually doing  `a = a + 1`, as for immutable types, a new object in memory has to be created for `a` to reference

{{< callout type="info" >}}
The changing of an object in memory using the same reference is called `rebinding`

[!Conclusion]
{{< /callout >}}
Thus, there is no difference between `a += 1` and `a = a + 1` for immutable types.
>
> In this case, `a += 1` is `syntactic sugar`

### ✅ Mutable Types
>
> Let
> `a = [1]`
>
> To add new value, we do:
> `a += [2]`
>
> This does in fact modify the list in place
> `a = [1, 2]` <----------- Memory `A`
>
> Which means the object in the same memory also changes

---
> With the same start
> `a = [1]`
>
> If we did this instead:
> `a = a + [2]`
>
> We will create a new object that now the same reference, `a`, newly refers to in memory
>
> `a = [1, 2]` <----------- Memory `B`

{{< callout type="default" >}}
Thus, for mutable types there is a difference between `a += 1` and `a = a + 1`
{{< /callout >}}
## ✅ Best Practices

| Type       | Use `a += i` when...            | Use `a = a + i` when...              |
|------------|----------------------------------|--------------------------------------|
| Immutable  | You want clean, idiomatic code   | You want to emphasize rebinding      |
| Mutable    | You intend to mutate in place    | You want a new object, avoid side effects |

In order to standardise the use of which for which,
> I would use `a = a + 1` strictly for immutable types
