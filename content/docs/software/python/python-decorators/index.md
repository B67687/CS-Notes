---
title: "🐍 Python Decorators"
date: 2025-11-08
draft: false
---

In short, its a function that returns a modified function

---

A decorator is a design pattern in Python that allows a user to add new functionality to an existing object (like a function or method) without modifying its structure. It's essentially syntactical sugar for passing a function to another function and executing the result.

The core confusion—why do we need an inner function (`wrapper`) inside the outer one (`decorator`)—is addressed by understanding **execution timing**.

---

## 1. Structure: The Two-Function Requirement

A standard decorator implementation requires two nested functions:

- **The Outer Function (The Decorator):**
    
    - **Job:** Accepts the original function as an argument.
        
    - **Timing:** Runs **once** when the decorated function is **defined** (parsed by the Python interpreter).
        
    - **Action:** Returns the inner function (the `wrapper`).
        
- **The Inner Function (The Wrapper):**
    
    - **Job:** Contains the actual logic (the "decoration") and a call to the original function.
        
    - **Timing:** Runs **every time** the decorated function is **called** by the program.
        
    - **Action:** Executes the extra logic and returns the original function's result.
        

## 2. Why the `wrapper` is Essential

If the outer function (`my_decorator`) simply contained the logic and returned the original function (`func`), the decorating logic would only execute once at definition time, not every time the function is called later.

The `wrapper` function is necessary to:

1. **Control Execution Time:** It delays the execution of the decoration logic until the function is explicitly called later in the code.
    
2. **Access Local Variables:** It uses a feature called **closures** to remember and access the `func` variable passed into the outer scope, allowing it to call the original function later.
    

## 3. Code Example

This example demonstrates how the `wrapper` adds timing functionality around the original function's execution.

```python
import time

# 1. THE DECORATOR (Runs only once at definition time)
def timer_decorator(func):
    """Adds timing logic around the execution of the decorated function."""
    
    # 2. THE WRAPPER (Runs every time the decorated function is called)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # --- PRE-EXECUTION LOGIC (The Decoration) ---
        print(f"[{func.__name__}]: Starting execution...")
        
        # --- CALLING THE ORIGINAL FUNCTION ---
        result = func(*args, **kwargs)
        
        # --- POST-EXECUTION LOGIC (The Decoration) ---
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"[{func.__name__}]: Finished in {elapsed:.4f} seconds.")
        
        return result
    
    # 3. The decorator RETURNS the wrapper function
    return wrapper

# --- USAGE ---

@timer_decorator # Equivalent to: calculate_sum = timer_decorator(calculate_sum)
def calculate_sum(n):
    """A function that takes time to execute."""
    total = 0
    for i in range(n):
        total += i
    return total

# When this is called, the 'wrapper' function is executed:
result = calculate_sum(100000)
print(f"Result: {result}") 
```

## 4. Key Takeaways

|Element|Role|Execution Timing|
|---|---|---|
|**Outer Function** (`timer_decorator`)|Setup and return|**Once** (at definition)|
|**Inner Function** (`wrapper`)|Execution of logic|**Many Times** (at runtime call)|
|**`@` Syntax**|Syntactic sugar|Tells Python to pass the next function into the outer function.|