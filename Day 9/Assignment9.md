# **Conditionals**

## **7.1. Intro: What We Can Do with Turtles and Conditionals**

### **7.1.1. Learning Goals**

- Understand how conditionals work in programming.
- Explore the use of turtles in Python to illustrate conditional logic.
- Learn to write conditional statements for decision-making in programs.

### **7.1.2. Objectives**

- Implement conditional execution using `if`, `if-else`, and `elif`.
- Utilize Boolean expressions and logical operators.
- Understand the precedence of operators.
- Apply conditionals in problem-solving and simulations.

## **7.2. Boolean Values and Boolean Expressions**

- Boolean values: `True` and `False`.
- Boolean expressions evaluate to `True` or `False`.
- Examples:
  ```python
  x = 10
  print(x > 5)  # True
  print(x == 5)  # False
  ```

## **7.3. Logical Operators**

- `and`, `or`, `not`
- Examples:
  ```python
  x = 5
  print(x > 2 and x < 10)  # True
  print(x > 10 or x == 5)  # True
  print(not(x == 5))  # False
  ```

### **7.3.1. Smart Evaluation**

- Also known as short-circuit evaluation.
- In `and`, if the first condition is `False`, the second condition is not evaluated.
- In `or`, if the first condition is `True`, the second condition is not evaluated.
- Example:

  ```python
  def check():
      print("Function executed")
      return True

  print(False and check())  # Function is not executed
  print(True or check())  # Function is not executed
  ```

## **7.4. The `in` and `not in` Operators**

- Used to check membership in lists, tuples, and strings.
- Example:
  ```python
  fruits = ["apple", "banana", "cherry"]
  print("apple" in fruits)  # True
  print("grape" not in fruits)  # True
  ```

## **7.5. Precedence of Operators**

- `not` > `and` > `or`
- Example:
  ```python
  print(True or False and False)  # True
  print((True or False) and False)  # False
  ```

## **7.6. Conditional Execution: Binary Selection**

- The `if-else` structure allows decision-making.
- Example:
  ```python
  age = 18
  if age >= 18:
      print("You can vote.")
  else:
      print("You cannot vote.")
  ```

## **7.7. Omitting the Else Clause: Unary Selection**

- `if` without `else` executes only when the condition is `True`.
- Example:
  ```python
  x = 10
  if x > 5:
      print("X is greater than 5")
  ```

## **7.8. Nested Conditionals**

- `if` inside another `if`.
- Example:
  ```python
  num = 10
  if num > 0:
      if num % 2 == 0:
          print("Positive even number")
  ```

## **7.9. Chained Conditionals**

- Using `elif` for multiple conditions.
- Example:
  ```python
  score = 85
  if score >= 90:
      print("A grade")
  elif score >= 80:
      print("B grade")
  else:
      print("C grade")
  ```

## **7.10. The Accumulator Pattern with Conditionals**

- Used to accumulate values conditionally.
- Example:
  ```python
  numbers = [1, 5, 3, 8, 2]
  total = 0
  for num in numbers:
      if num % 2 == 0:
          total += num
  print(total)  # 10
  ```

### **7.10.1. Accumulating the Max Value**

- Example:
  ```python
  numbers = [3, 7, 2, 9, 5]
  max_value = numbers[0]
  for num in numbers:
      if num > max_value:
          max_value = num
  print(max_value)  # 9
  ```

## **7.11. 👩💻 Setting Up Conditionals**

### **7.11.1. Choosing Your Type of Conditional**

- Use `if` for a single condition.
- Use `if-else` for two possible outcomes.
- Use `if-elif-else` for multiple conditions.
- Example:
  ```python
  temperature = 30
  if temperature > 35:
      print("It's too hot!")
  elif temperature < 15:
      print("It's too cold!")
  else:
      print("The weather is pleasant.")
  ```

---

## **7.12. Exception Handling with Conditionals**

- Using `try-except` blocks to handle conditional errors.
- Example:
  ```python
  try:
      num = int(input("Enter a number: "))
      if num < 0:
          raise ValueError("Negative numbers not allowed!")
  except ValueError as e:
      print("Error:", e)
  ```

---

### **Problem 6: Bank Loan Eligibility System**

- Create a program to check if a user is eligible for a bank loan based on salary, age, and credit score using nested conditionals.

### **Problem 7: AI Chatbot with Conditional Responses**

- Design a simple chatbot that responds differently based on user input (e.g., greetings, questions, or farewell messages).

### **Problem 8: Traffic Light Simulation**

- Simulate a traffic light system using conditionals and loops.

### **Problem 9: Smart Home Automation**

- Implement a conditional-based smart home system where temperature, humidity, and motion sensors determine actions (e.g., turning lights and fans on/off).

### **Problem 10: Stock Market Trend Analysis**

- Write a program to analyze stock prices and predict buy/sell signals based on historical trends using conditionals.

---

### **1. Employee Attendance Tracker**

- Implement a system that tracks employee attendance.
- Use loops to process multiple employees and conditionals to check attendance.
- Mark employees as "Needs Attention" if absent for more than 3 consecutive days.

### **3. Password Strength Checker**

- Classify passwords as "Weak", "Medium", or "Strong" based on length, numbers, uppercase/lowercase letters, and special characters.
- Loop until a "Strong" password is entered.

### **5. Banking System with ATM Functionality**

- Simulate an ATM system for checking balance, withdrawal, and deposit.
- Use loops for multiple transactions and conditionals to prevent overdraft.