# Python Modules: Advanced Notes and Assignment

## 4.1. Introduction to Python Modules

### 4.1.1. Learning Goals

By the end of this module, students should be able to:

- Understand the purpose and importance of modules in Python.
```
A module in Python is a file containing Python code (functions, classes, and variables) that can be reused in different programs. It allows for better code organization, reusability, and maintainability.
A module can be:
- A built-in module (e.g., math, os, sys)
- A user-defined module (a .py file with reusable code)
- A third-party module (installed via pip, e.g., numpy, pandas).
Purpose of Modules-
1. Code Reusability: Modules allow you to write code once and reuse it in multiple programs.
2. Better Organization: Breaking large programs into smaller modules makes code more structured and manageable.
3. Avoiding Code Duplication: Functions and classes defined in a module can be used in different scripts, reducing redundancy.
4. Encapsulation: Modules provide a way to encapsulate functionality, preventing unnecessary exposure of internal logic.
5. Namespace Management: Modules help in avoiding naming conflicts by providing separate namespaces.
```
- Differentiate between built-in, third-party, and custom modules.
```
1. Built-in Modules
- Provided by Python's standard library.
- No need to install separately.
- Used for common tasks like math operations, file - handling, and system interaction.
Example: math module
2. 2. Third-Party Modules
- Developed by others and available on the Python Package Index (PyPI).
- Require installation using pip.
- Used for data analysis, machine learning, web development, etc.
Example- request module
3. Custom Modules
- Created by developers for specific projects.
- A Python file (.py) containing functions, classes, or variables.
- Useful for organizing and reusing code.
```
- Master various techniques for importing modules.
```
1. Importing the Entire Module
- This imports the whole module, and we access its contents using the dot (.) notation.Example:
import math
print(math.sqrt(25))  # Output: 5.0
print(math.pi)   

2. Importing a Specific Function or Class
This imports only the needed functions/classes, reducing memory usage and improving readability.
from math import sqrt, pi
print(sqrt(25))  # Output: 5.0
print(pi)        # Output: 3.141592653589793
✅ Best for: When you only need a few functions to keep your code cleaner.

3. Importing Everything Using * (Wildcard Import)
This imports all public functions, variables, and classes from a module.
from math import *
print(sqrt(25))  # Output: 5.0
print(factorial(5))  # Output: 120

4. Importing a Module with an Alias (as)
You can rename a module for easier use.
import numpy as np
array = np.array([1, 2, 3])
print(array)  # Output: [1 2 3]

5. Importing Functions with an Alias
You can rename specific functions for clarity.

from math import sqrt as square_root
print(square_root(36))  # Output: 6.0
✅ Best for: When you want shorter or more meaningful names for imported functions.

6. Importing a Custom Module
You can import user-defined modules stored as .py files.
Step 1: Create my_module.py
# my_module.py
def greet(name):
    return f"Hello, {name}!"
def add(a, b):
    return a + b

7. Importing Using importlib (Dynamic Importing)
You can import modules dynamically using importlib.

import importlib
math_module = importlib.import_module('math')
print(math_module.sqrt(16))  # Output: 4.0

8. Importing Relative and Absolute Modules
Absolute Import (Using Full Path)
from package_name.module_name import function_name
```

- Apply advanced import strategies and avoid common pitfalls.

1️⃣ Optimize Imports for Performance

✅ Lazy Imports (Import Inside a Function)
Instead of importing modules at the top, import them inside functions only when needed. This reduces memory usage and speeds up script startup.
```python
def process_data():
    import pandas as pd 
    df = pd.DataFrame({"A": [1, 2, 3]})
    print(df)
process_data()
```

2️⃣ Reduce Namespace Clashes
❌ Bad Practice: from module import * (Wildcard Import)
```python
from math import *
from random import *
print(sqrt(25))  # Potential conflict: sqrt exists in both modules
```
This can cause name conflicts if two modules have functions with the same name.

3️⃣ Use if __name__ == "__main__" to Avoid Unintended Imports: 
If a script is both a module and a standalone program, using if __name__ == "__main__" prevents execution when imported.
```python
def greet():
    print("Hello, World!")

if __name__ == "__main__":
    greet()  # Runs only if script is executed directly
```
4️⃣ Use importlib for Dynamic Module Imports:
If you need to import a module dynamically (e.g., based on user input), use importlib.
```python
import importlib
module_name = "math"
math_module=importlib.import_module(module_name)
print(math_module.sqrt(16))  # Output: 4.0
```
✅ Best for: Plugins, dynamically loading modules.

5️⃣ Organize Imports Properly
Follow the Import Order
- Standard Library Imports
- Third-Party Modules
- Custom Modules

6️⃣ Avoid Circular Imports

✅ Solutions:Move imports inside functions (Lazy Import)

7️⃣ Use sys.path to Import Modules from Other Directories: 
Python searches for modules in sys.path. You can modify it to import from a specific location.

### 4.1.2. Objectives
- Comprehend modular programming concepts.

Modular programming is a software design technique that emphasizes breaking a program into smaller, independent, and reusable modules. Each module handles a specific functionality, making the code more organized, maintainable, and scalable.

🔹 Benefits of Modular Programming:
 
✅ Code Reusability – Write once, use multiple times.

✅ Improved Readability – Clean, structured, and easy-to-understand code.

✅ Easier Debugging – Fix bugs in one module without affecting others.

✅ Efficient Collaboration – Different team members can work on separate modules.

✅ Scalability – Add new features without modifying the entire codebase.

Implementing Modular programming in python:

    - Using function,Package,Modules.

- Practice importing modules in multiple ways.
- Explore the Python Standard Library.
```
The Python Standard Library is a collection of built-in modules that provide ready-to-use functionalities, eliminating the need to install external packages. These modules cover file handling, math operations, networking, data manipulation, debugging, and much more.
1. OS module (Operating System Interactions)
2. Sys module(System-Specific Parameters & Functions)
3. Math Module (Mathematical Functions)
4. Random Module (Generating Random Numbers) 
5. Datetime Module (Working with Dates & Time)
6. JSON Module (Handling JSON Data)
7. Collections Module (Advanced Data Structures)
8. Re module(Regular Expression)
9. Statistics Module (Statistical Calculations)
```
- Understand namespace management and circular imports.
```
A namespace in Python is a mapping between variable names and objects. It ensures that variable names do not conflict with each other.
Types of Namespaces---------
Python maintains different types of namespaces:
Local-	Variables inside a function (valid only within that function).
Enclosing Variables -in enclosing functions (for nested functions).
Global	Variables - defined at the module level, accessible throughout the script.
Built-in- Names from Python’s built-in functions and modules (e.g., print(), len()).
```
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
Answer:

```python
import importlib
def dynamic_function_call():
    try:
        module_name = input("Enter module name: ").strip()
        function_name = input("Enter function name: ").strip()
        argument = input("Enter argument: ").strip()
        module = importlib.import_module(module_name)
        function = getattr(module, function_name, None)

        if function is None:
            print(f"Error: Function '{function_name}' not found in module '{module_name}'.")
            return
        if argument.isdigit():
            argument = int(argument)
        else:
            try:
                argument = float(argument)
            except ValueError:
                print("Error: Invalid argument type.")
                return
        result = function(argument)
        print(f"Output: {result}")
    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found.")
    except TypeError:
        print("Error: Function argument mismatch.")
    except Exception as e:
        print(f"An error occurred: {e}")
dynamic_function_call()

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
```python
import calculator.py
a = input("Enter first number: ")
b = input("Enter second number: ")

try:
    a = float(a)
    b = float(b)
    result = calculator.divide(a, b)
    print("Result:", result)
except ValueError:
    print("Error: Invalid input. Please enter numbers.")

```
### 4. Advanced Import Strategies

Write a script that:
- Imports a module.
- Checks if a function exists.
- Executes it if available, otherwise gracefully handles the error.

```python
import importlib
module_name = input("Enter module name: ")
function_name = input("Enter function name: ")
try:
    module = importlib.import_module(module_name)
    function = getattr(module, function_name, None)
    if function:
        result = function()
        print("Output:", result)
    else:
        print(f"Error: Function '{function_name}' not found.")
except ModuleNotFoundError:
    print(f"Error: Module '{module_name}' not found.")
except Exception as e:
    print(f"Error: {e}")
```


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
Answer:
1. Create a file named mymodule.py
```python
print("This runs on import!")

def greet():
    return "Hello from mymodule!"
```
2. Import the Module and Observe-(main.py)
```python
import mymodule
print("Module imported successfully!")
print(mymodule.greet())

```
### 10. Investigate Python’s Import Caching

Explore `sys.modules` to understand how Python caches imports and how to reload modules.

```python
import sys
import mymodule
print(sys.modules['mymodule'])
```
Answer:
1. Create a module name mymodule.py:
```python 
def greet():
    return "Hello from mymodule!"
```
2. In the main.py
```python
import sys
import mymodule
print(sys.modules['mymodule'])  # Prints the cached module object
print(mymodule.greet())         # Output: Hello from mymodule!

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