# Python Modules: Advanced Notes and Assignment

## 4.1. Introduction to Python Modules

### 4.1.1. Learning Goals

By the end of this module, students should be able to:

- Understand the purpose and importance of modules in Python.
- Differentiate between built-in, third-party, and custom modules.
- Master various techniques for importing modules.
- Apply advanced import strategies and avoid common pitfalls.

### 4.1.2. Objectives

- Comprehend modular programming concepts.
- Practice importing modules in multiple ways.
- Explore the Python Standard Library.
- Understand namespace management and circular imports.

---

## 4.2. Modules

A module is a Python file containing reusable code like functions, classes, or variables. Modular programming improves code organization and reusability.

## Types of Modules

1. **Built-in Modules**: Pre-installed with Python (e.g., `math`, `os`, `sys`).
2. **User-defined Modules**: Created by the user, like `math_operations` above.
3. **Third-party Modules**: Installed using `pip` (e.g., `numpy`, `pandas`).

### 4.2.1. Importing Modules

Python provides several ways to import modules:

1. **Import the entire module:**

```python
import math
print(math.sqrt(16))
```

2. **Import with an alias:**

```python
import numpy as np
print(np.array([1, 2, 3]))
```

3. **Import specific attributes:**

```python
from math import sqrt, pi
print(sqrt(25), pi)
```

4. **Import all attributes (Not recommended):**

```python
from math import *
print(sin(pi / 2))
```

5. **Custom Modules:**
   Create a file `mymodule.py` with the following content:

```python
def greet(name):
    return f"Hello, {name}!"
```

Import it in another file:

```python
import mymodule
print(mymodule.greet("Alice"))
```

6. **Relative Imports:** (Used within packages)

```python
from .subpackage import mymodule
```

7. **Dynamic Imports:**

```python
module_name = 'math'
import importlib
math = importlib.import_module(module_name)
print(math.sqrt(49))
```

## Special Module Attributes

- `__name__`: Returns the name of the module.
- `__file__`: Returns the path to the module.
- `__doc__`: Returns the module's documentation string.

Example:

```python
print(math.__name__)  # Output: math
print(math.__doc__)   # Shows documentation for the math module
```

## Module's Private Namespace

Each module has its own private namespace, which serves as the global namespace for all functions within that module. This avoids accidental clashes with other global variables.

```python
# Accessing global variables in a module
fibo.some_global_variable = 100
print(fibo.some_global_variable)  # Outputs: 100
```

## Running a Module as a Script

You can run the module as a script by adding the following at the end of `fibo.py`:

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

Then, run it from the command line:

```sh
python fibo.py 50
```

If imported, the code under `if __name__ == "__main__":` will not run.

## Compiling Modules

Python compiles modules to `.pyc` files to speed up loading times, not execution. You can optimize with `-O` or `-OO`:

```sh
python -O fibo.py
```

For mass compilation, use `compileall`:

```sh
python -m compileall .
```

## Packages

A **package** is a collection of modules organized in a directory with an `__init__.py` file, which can be empty or contain initialization code.
Example package structure:

```
sound/
    __init__.py
    effects/
        __init__.py
        echo.py
        surround.py
    filters/
        __init__.py
        equalizer.py
```

Importing from a package:

```python
from sound.effects import echo
echo.apply_echo()
```

Packages help prevent name conflicts and organize large codebases.

### Best Practices:

- Avoid `from module import *` to prevent namespace pollution.
- Keep imports organized (standard library, third-party, custom).
- Use aliases for frequently-used modules.

---

### 1. Investigate Circular Imports

Fix the circular import problem between `module_a.py` and `module_b.py`.

#### module_a.py:

```python
import module_b

def func_a():
    return "Function A"

print(module_b.func_b())
```

#### module_b.py:

```python
import module_a

def func_b():
    return "Function B"
```

**Task:** Resolve the circular dependency.

### 2. Dynamic Module Loading

Write a program that dynamically imports and executes a function from any module specified by the user.
Example:

```shell
Enter module name: math
Enter function name: sqrt
Enter argument: 25
Output: 5.0
```

### 3. Custom Module with Exception Handling

Create a custom module `calculator.py` that handles division by zero and invalid inputs gracefully.

```python
# calculator.py
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"
```

Import and use this module.

### 4. Advanced Import Strategies

Write a script that:

- Imports a module.
- Checks if a function exists.
- Executes it if available, otherwise gracefully handles the error.

### 5. Optimize Import Time

Use `time` module to measure import time for different methods (single import vs. importing everything).

```python
import time
start = time.time()
import math
end = time.time()
print(f"Import time: {end - start}")
```

### 6. Module Creation and Distribution

1. Create a Python package structure with `__init__.py`.
2. Write a `setup.py` to make it installable.
3. Install your package locally.
4. Import and test your package.

### 7. Investigate sys.path

Explore `sys.path` and add a custom directory to import modules from an unconventional path.

```python
import sys
sys.path.append('/custom/path/to/modules')
import mymodule
```

### 8. Mocking Modules for Testing

Write a unit test for a function that imports a module. Use `unittest.mock` to mock the imported module.

```python
from unittest import mock
with mock.patch('math.sqrt', return_value=100):
    print(math.sqrt(25))  # Should print 100
```

### 9. Import Side Effects

Investigate modules that run code at import time. Create a module that prints something as soon as it’s imported.

```python
print("This runs on import!")
```

### 10. Investigate Python’s Import Caching

Explore `sys.modules` to understand how Python caches imports and how to reload modules.

```python
import sys
import mymodule
print(sys.modules['mymodule'])
```

#### Additional Resources:

- [Official Python Documentation](https://docs.python.org/3/tutorial/modules.html)
- [Real Python: Modules and Packages](https://realpython.com/python-modules-packages/)
- [PEP 8 - Imports](https://peps.python.org/pep-0008/#imports)

---

# I highly recommend checking out the official Python documentation for modules:

- [👉 Python Official Docs](https://docs.python.org/3/tutorial/modules.html)

## Submission Guidelines:

- Submit solutions in a `modules_assignment` folder.
- Include `README.md` explaining your approach.
- Ensure code is properly commented.

Happy Coding! 🚀