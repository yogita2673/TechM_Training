# Sequences in Python: Comprehensive Notes

## 5.1 Introduction: Sequences

In Python, a **sequence** is an ordered collection of items. The order of elements is preserved, and each element is accessible via its index. The main types of sequences in Python are:

- Strings
- Lists
- Tuples

### 5.1.1 Learning Goals

- Understand different types of sequences.
- Learn how to manipulate sequences.
- Perform operations like slicing, concatenation, and repetition.

### 5.1.2 Objectives

- Identify and use strings, lists, and tuples.
- Access elements using indexing and slicing.
- Perform operations like count, index, split, and join.

---

## 5.2 Strings, Lists, and Tuples

### 5.2.1 Strings

A **string** is an immutable sequence of characters.

```python
text = "Hello, World!"
```

- Access elements using indexes:

```python
print(text[0])  # Output: H
```

### 5.2.2 Lists

A **list** is a mutable sequence used to store items of different types.

```python
numbers = [1, 2, 3, 4, 5]
numbers[0] = 10  # Lists are mutable
```

### 5.2.3 Tuples

A **tuple** is an immutable sequence.

```python
tuple_example = (1, 2, 3)
# tuple_example[0] = 10  # Raises TypeError
```

---

## 5.3 Index Operator: Working with the Characters of a String

The index operator (`[]`) allows accessing elements by index.

```python
text = "Python"
print(text[1])  # Output: y
```

### 5.3.1 Index Operator: Accessing Elements of a List or Tuple

```python
my_list = [10, 20, 30]
print(my_list[2])  # Output: 30
```

---

## 5.4 Disambiguating []: Creation vs Indexing

- **Creation:**

```python
my_list = []  # Empty list
```

- **Indexing:**

```python
value = my_list[0]  # Access first element
```

---

## 5.5 Length

Use `len()` to get the number of elements:

```python
my_list = [1, 2, 3, 4]
print(len(my_list))  # Output: 4
```

---

## 5.6 The Slice Operator

Slicing extracts a portion of the sequence.

```python
my_list = [0, 1, 2, 3, 4]
print(my_list[1:4])  # Output: [1, 2, 3]
```

### 5.6.1 List Slices

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [2, 3, 4]
```

### 5.6.2 Tuple Slices

```python
tuple_example = (10, 20, 30, 40)
print(tuple_example[1:3])  # Output: (20, 30)
```

---

## 5.7 Concatenation and Repetition

- **Concatenation:**

```python
list1 = [1, 2]
list2 = [3, 4]
result = list1 + list2  # [1, 2, 3, 4]
```

- **Repetition:**

```python
my_list = [0] * 5  # [0, 0, 0, 0, 0]
```

---

## 5.8 Count and Index

### 5.8.1 Count

Counts occurrences of an item:

```python
my_list = [1, 2, 2, 3]
print(my_list.count(2))  # Output: 2
```

### 5.8.2 Index

Finds the index of the first occurrence:

```python
print(my_list.index(2))  # Output: 1
```

---

## 5.9 Splitting and Joining Strings

- **Splitting:**

```python
sentence = "Python is awesome"
words = sentence.split()  # ['Python', 'is', 'awesome']
```

- **Joining:**

```python
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)  # 'Python is awesome'
```

---

## Assignment Questions

1. Define a sequence. What types of sequences exist in Python?
2. How are strings, lists, and tuples different from each other?
3. Explain how indexing works in Python with an example.
4. Write code to access the last character of a string.
5. Create a list of numbers and access the third element.
6. What is the result of `len([1, [2, 3], 4])` and why?
7. Explain slicing with a practical example.
8. How would you reverse a string using slicing?
9. Demonstrate list concatenation and repetition with examples.
10. Write code to count the occurrences of an element in a list.
11. What will `my_tuple = (1, 2, 3); print(my_tuple[1:])` output?
12. Explain the difference between `list.append()` and `list.extend()`.
13. Write code to split the sentence: "Learn Python, step by step!" into words.
14. Join a list `['Python', 'is', 'fun']` into a single string.
15. Given a list `numbers = [1, 2, 2, 3, 4, 2]`, find the index of the first `2`.
16. Write code to check if a string is a palindrome.
17. Implement a function that returns the length of the longest word in a sentence.
18. Demonstrate nested list indexing.
19. How do you convert a list of characters into a string?
20. Write code to remove duplicates from a list while preserving order.
21. Write a function that takes a list of tuples and sorts it by the second element of each tuple.
22. Implement a program to flatten a nested list of arbitrary depth.
23. Create a function that rotates a list to the right by k steps.
24. Given two strings, write a function that returns True if they are anagrams.
25. Create a function to split a list into chunks of a specified size.
26. Implement a function that merges two sorted lists into one sorted list.

# 🚀 Questions on Sequences in Python

1. **Data Pipeline Validator**

   - **Task**: Identify the longest pipeline and return pipelines taking more than a given threshold time.
   - **Input**:
     ```python
     pipelines = [
         ("Data Ingestion", 30),
         ("Preprocessing", 45),
         ("Model Training", 120),
         ("Evaluation", 20)
     ]
     threshold = 40
     ```
   - **Expected Output**:
     ```
     Longest Pipeline: Model Training
     Pipelines exceeding threshold: ['Preprocessing', 'Model Training']
     ```

2. **Log File Parser**
   - **Task**: Extract unique error codes from a log file.
   - **Input**:
     ```python
     logs = """ERROR 404: Not Found
     INFO: Connection established
     ERROR 500: Internal Server Error
     ERROR 404: Not Found
     """
     ```
   - **Expected Output**:
     ```
     Unique Error Codes: ['404', '500']
     ```

---

## 5.2. Strings, Lists, and Tuples

3. **Config File Reader**

   - **Task**: Parse key-value pairs from a configuration string.
   - **Input**:
     ```python
     config = "host=127.0.0.1;port=8080;mode=debug"
     ```
   - **Expected Output**:
     ```
     [('host', '127.0.0.1'), ('port', '8080'), ('mode', 'debug')]
     ```

4. **Social Media Data Cleaner**
   - **Task**: Extract unique hashtags from a social media post.
   - **Input**:
     ```python
     post = "Loving the new #Python course! #Coding #Python #Learning"
     ```
   - **Expected Output**:
     ```
     ['#Python', '#Coding', '#Learning']
     ```

---

## 5.3. Index Operator: Working with Characters

5. **Secret Code Decoder**

   - **Task**: Extract every third character from a string.
   - **Input**:
     ```python
     secret_message = "hweollrolwd"
     ```
   - **Expected Output**:
     ```
     'hello world'
     ```

6. **Inventory Tracker**
   - **Task**: Find the product with the highest quantity.
   - **Input**:
     ```python
     inventory = [
         ("Apples", 50),
         ("Oranges", 75),
         ("Bananas", 30)
     ]
     ```
   - **Expected Output**:
     ```
     'Oranges'
     ```

---

## 5.4. Disambiguating `[]`: Creation vs Indexing

7. **Survey Data Analyzer**

   - **Task**: Extract scores from a survey string and find min/max.
   - **Input**:
     ```python
     survey_data = "5,3,4,1,2"
     ```
   - **Expected Output**:
     ```
     Max Score: 5, Min Score: 1
     ```

8. **Access Control Manager**
   - **Task**: Manage user access levels using lists and tuples.
   - **Input**:
     ```python
     users = ["Alice", "Bob", "Charlie"]
     roles = ("Admin", "Editor", "Viewer")
     ```
   - **Expected Output**:
     ```
     Alice: Admin, Bob: Editor, Charlie: Viewer
     ```

---

## 5.5. Length

9. **Customer Support Ticket System**

   - **Task**: Categorize tickets based on message length.
   - **Input**:
     ```python
     message = "My account is locked, please help!"
     ```
   - **Expected Output**:
     ```
     Category: Medium
     ```

10. **Product Catalog Manager**

- **Task**: Find the product with the longest name.
- **Input**:
  ```python
  products = ["Laptop", "Smartphone", "Wireless Headphones"]
  ```
- **Expected Output**:
  ```
  'Wireless Headphones'
  ```

---

## 5.6. The Slice Operator

11. **Sensor Data Analyzer**

- **Task**: Extract the last 10 sensor readings and calculate the average.
- **Input**:
  ```python
  sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]
  ```
- **Expected Output**:
  ```
  Average: 22
  ```

12. **Transaction Reverser**

- **Task**: Reverse the list of transactions.
- **Input**:
  ```python
  transactions = [100, -50, 200, -150, 50]
  ```
- **Expected Output**:
  ```
  [50, -150, 200, -50, 100]
  ```

---

## 5.7. Concatenation and Repetition

13. **Log Formatter**

- **Task**: Format logs with timestamps.
- **Input**:
  ```python
  logs = ["System Boot", "Network Connected", "User Login"]
  timestamp = "2025-03-20"
  ```
- **Expected Output**:
  ```
  ['2025-03-20: System Boot', '2025-03-20: Network Connected', '2025-03-20: User Login']
  ```

14. **Pattern Generator**

- **Task**: Generate patterns with repetition.
- **Input**:
  ```python
  symbol = "*"
  count = 5
  ```
- **Expected Output**:
  ```
  '* * * * *'
  ```

---

## 5.8. Count and Index

15. **Customer Feedback Analyzer**

- **Task**: Count keyword occurrences.
- **Input**:
  ```python
  feedback = "The product is excellent, absolutely excellent!"
  ```
- **Expected Output**:
  ```
  'excellent' count: 2
  ```

16. **Sentence Index Finder**

- **Task**: Find the index of the first occurrence of "error".
- **Input**:
  ```python
  log = "INFO: All systems go. ERROR: Failed to start service."
  ```
- **Expected Output**:
  ```
  Index: 21
  ```

---

## 5.9. Splitting and Joining Strings

17. **CSV Parser**

- **Task**: Parse CSV data into lists.
- **Input**:
  ```python
  csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"
  ```
- **Expected Output**:
  ```
  [['Alice', '25', 'Engineer'], ['Bob', '30', 'Doctor'], ['Charlie', '22', 'Artist']]
  ```

18. **Username Generator**

- **Task**: Generate usernames from full names.
- **Input**:
  ```python
  names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]
  ```
- **Expected Output**:
  ```
  ['AWonderland', 'BBuilder', 'CChaplin']
  ```

---

## Bonus Advanced Problems

19. **Chat Log Analyzer**

- **Task**: Count messages per user from chat logs.
- **Input**:
  ```python
  chat_logs = [
      "Alice: Hi!",
      "Bob: Hello!",
      "Alice: How are you?",
      "Bob: I’m good, thanks!"
  ]
  ```
- **Expected Output**:
  ```
  Alice: 2 messages, Bob: 2 messages
  ```

20. **Data Compressor**

- **Task**: Compress recurring substrings.
- **Input**:
  ```python
  data = "abababababab"
  ```
- **Expected Output**:
  ```
  'ab' repeated 6 times
  ```

---