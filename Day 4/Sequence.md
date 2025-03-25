# Sequences in Python: Comprehensive Notes

## 5.1 Introduction: Sequences

In Python, a **sequence** is an ordered collection of items. The order of elements is preserved, and each element is accessible via its index. The main types of sequences in Python are:

- Strings
- Lists
- Tuples

### 5.1.1 Learning Goals

- Understand different types of sequences.
- Learn how to manipulate sequences.
```
1. Accessing Elements
Python allows accessing elements of a sequence using indexing.
2. Slicing a Sequence
Slicing extracts a portion of a sequence.
- Perform operations like slicing, concatenation, and repetition.
3. Modifying Sequences
Lists are mutable, meaning you can change their elements.
4. Adding and Removing Elements
5. Iterating Over a Sequence
Using a loop to iterate over elements.
6. List Comprehension
A concise way to create and modify lists.
7. Sorting and Reversing
8. Unpacking Sequences
```
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
Answer:
```
A sequence in Python is an ordered collection of elements where each element is assigned a unique position (index). Sequences allow indexing, slicing, and iteration over their elements.
Types of Sequences in Python -
Python provides several built-in sequence types:
1. Immutable Sequences (Cannot be changed after creation)
- Strings (str)
- Tuples (tuple)
- Range (range)
2. Mutable Sequences (Can be modified after creation)
- Lists (list)
- Byte Arrays (bytearray)
```
2. How are strings, lists, and tuples different from each other?
Answer:
```
 1. Strings (str) - Immutable
- A sequence of characters.
- Cannot be modified after creation.
- Can be concatenated, sliced, and indexed.
2. Lists (list) - Mutable
- Ordered collection of elements.
- Can store different data types.
- Can be modified (adding, removing, or changing elements).
3. Tuples (tuple) - Immutable
- Ordered collection of elements like a list.
- Cannot be modified after creation (Immutable).
- Used when data should not change.
```
3. Explain how indexing works in Python with an example.
```
Indexing is the process of accessing elements in a sequence (such as strings, lists, and tuples) using their position.
Python uses zero-based indexing, meaning the first element has an index of 0, the second has an index of 1, and so on.
Negative indexing allows access from the end, where -1 refers to the last element, -2 refers to the second-last, etc.Example:
# String indexing
text = "Python"
print(text[0])   # Output: 'P'  (First character)
print(text[-1])  # Output: 'n'  (Last character)

# List indexing
fruits = ["apple", "banana", "cherry"]
print(fruits[1])   # Output: 'banana'
print(fruits[-2])  # Output: 'banana'

# Tuple indexing
numbers = (10, 20, 30, 40)
print(numbers[2])   # Output: 30
print(numbers[-1])  # Output: 40
```
4. Write code to access the last character of a string.
```
Accessing the Last Character of a String in Python: You can access the last character of a string using negative indexing (-1) or by calculating the length of the string.Example:
text = "Python"
last_char = text[-1]  # Accessing the last character
print(last_char)  # Output: 'n'
```
5. Create a list of numbers and access the third element.
```
You can access the third element of a list using zero-based indexing (index = 2).
```
6. What is the result of `len([1, [2, 3], 4])` and why?
```
The len() function counts the number of top-level elements in the list.The output is 3.
```
7. Explain slicing with a practical example.
```
Slicing is used to extract a portion of a sequence (string, list, or tuple) using the syntax:
sequence[start:stop:step]
start → The index where slicing begins (default = 0).
stop → The index where slicing ends (not included in the result).
step → The interval between elements (default = 1).
```
8. How would you reverse a string using slicing?
```
text = "Python"
# Reverse the string using slicing
reversed_text = text[::-1]
print(reversed_text)  # Output: "nohtyP"

```
9. Demonstrate list concatenation and repetition with examples.
```
Lists in Python support concatenation (+) and repetition (*) for combining and repeating elements.
Example:
1. list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Concatenating two lists
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

2. nums = [7, 8, 9]
# Repeating the list 3 times
repeated_list = nums * 3
print(repeated_list)  # Output: [7, 8, 9, 7, 8, 9, 7, 8, 9]

```
10. Write code to count the occurrences of an element in a list.
```
numbers = [1, 2, 3, 2, 4, 2, 5, 2]
# Count occurrences of 2
count_2 = numbers.count(2)
print("Count of 2:", count_2)  # Output: Count of 2: 4

```
11. What will `my_tuple = (1, 2, 3); print(my_tuple[1:])` output?
```
Output:(2, 3)
```
12. Explain the difference between `list.append()` and `list.extend()`.
```
1️⃣ list.append(x) → Adds an element as a single item
Appends the entire element (including lists, tuples, etc.) as a single entity.
✅ Use append() when you want to add a single element (e.g., another list, tuple, or object).
✅ Use extend() when you want to merge elements from another iterable.
```
13. Write code to split the sentence: "Learn Python, step by step!" into words.
```
sentence = "Learn Python, step by step!"
words = sentence.split()  # Splits based on spaces by default
print(words)

```
14. Join a list `['Python', 'is', 'fun']` into a single string.
```
words = ['Python', 'is', 'fun']
sentence = " ".join(words)  # Joins elements with a space
print(sentence)
```
15. Given a list `numbers = [1, 2, 2, 3, 4, 2]`, find the index of the first `2`.
```
numbers = [1, 2, 2, 3, 4, 2]
first_index = numbers.index(2)  # Finds the index of the first '2'
print("Index of first 2:", first_index)

```
16. Write code to check if a string is a palindrome.
```
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Compare string with its reverse

# Example usage
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
```
17. Implement a function that returns the length of the longest word in a sentence.
```
def longest_word_length(sentence):
    words = sentence.split()  # Split sentence into words
    if not words:
        return 0  # Return 0 if the sentence is empty
    return max(len(word) for word in words)  # Find the max word length

# Example usage
sentence = input("Enter a sentence: ")
print("Length of the longest word:", longest_word_length(sentence))
```
18. Demonstrate nested list indexing.
```
Nested lists in Python are lists within lists. You can access elements using multiple indices.

# Creating a nested list
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(nested_list[0][0])  # Output: 1 (First row, first column)
print(nested_list[1][2])  # Output: 6 (Second row, third column)
print(nested_list[2][1])  # Output: 8 (Third row, second column)

# Modifying an element
nested_list[1][1] = 50
print(nested_list)  # Updated list

```
19. How do you convert a list of characters into a string?
```
# List of characters
char_list = ['H', 'e', 'l', 'l', 'o']

# Convert to string
result = ''.join(char_list)

# Output the result
print(result)  # Output: Hello

```
20. Write code to remove duplicates from a list while preserving order.
```
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5, 6]
```
21. Write a function that takes a list of tuples and sorts it by the second element of each tuple.
```
def sort_by_second_element(lst):
    return sorted(lst, key=lambda x: x[1])

# Example usage
tuples_list = [(1, 3), (4, 1), (2, 5), (6, 2)]
print(sort_by_second_element(tuples_list))
```

22. Implement a program to flatten a nested list of arbitrary depth.
```
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):  # Check if the item is a list
            flat_list.extend(flatten_list(item))  # Recursively flatten
        else:
            flat_list.append(item)  # Append non-list items
    return flat_list

# Example usage
nested_list = [1, [2, [3, 4], 5], [6, 7], 8]
print(flatten_list(nested_list))
```
23. Create a function that rotates a list to the right by k steps.
```
def rotate_list(lst, k):
    k = k % len(lst)  # Handle cases where k is greater than list length
    return lst[-k:] + lst[:-k]  # Slice and concatenate

# Example usage
numbers = [1, 2, 3, 4, 5]
k = 2
print(rotate_list(numbers, k))  # Output: [4, 5, 1, 2, 3]

```
24. Given two strings, write a function that returns True if they are anagrams.
```
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)  # Sort and compare

# Example usage
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False
```
25. Create a function to split a list into chunks of a specified size.
```
def split_into_chunks(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
print(split_into_chunks(numbers, chunk_size))

```
26. Implement a function that merges two sorted lists into one sorted list.
```
def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)  # Merge and sort

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists(list1, list2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
```
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
 Answer:
 ```python
 def validate_pipelines(pipelines, threshold):
   
    # Find the longest pipeline
    longest_pipeline = max(pipelines, key=lambda x: x[1])[0]

    # Find pipelines exceeding the threshold
    exceeding_pipelines = [name for name, time in pipelines if time > threshold]

    print(f"Longest Pipeline: {longest_pipeline}")
    print(f"Pipelines exceeding threshold: {exceeding_pipelines}")

# Example usage
pipelines = [
    ("Data Ingestion", 30),
    ("Preprocessing", 45),
    ("Model Training", 120),
    ("Evaluation", 20)
]
threshold = 40

validate_pipelines(pipelines, threshold)

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
```python
import re

def extract_error_codes(logs):
    # Use regex to find all error codes (digits after "ERROR ")
    error_codes = set(re.findall(r"ERROR (\d+)", logs))
    
    print(f"Unique Error Codes: {sorted(error_codes)}")  # Sort for consistency

# Example usage
logs = """ERROR 404: Not Found
INFO: Connection established
ERROR 500: Internal Server Error
ERROR 404: Not Found
"""

extract_error_codes(logs)
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
Answer:
```python
def parse_config(config):
    return [tuple(pair.split('=')) for pair in config.split(';')]

# Example usage
config = "host=127.0.0.1;port=8080;mode=debug"
print(parse_config(config))

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
Answer:
```python
import re

def extract_hashtags(post):
    hashtags = re.findall(r'#\w+', post) 
    return list(set(hashtags))  

post = "Loving the new #Python course!
print(extract_hashtags(post))

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
```python
def decode_secret(secret_message):
    return secret_message[::3]  
secret_message = "hweollrolwd"
decoded_message = decode_secret(secret_message)
print(decoded_message)  # Output: 'horw'

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

```python
def highestQty(inventory):
  return max(inventory,key=lambda x:x[1])[0]
inventory = [
    ("Apples", 50),
    ("Oranges", 75),
    ("Bananas", 30)
]
print(highestQty(inventory))
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
```python
def analyze_survey(survey_data):
    scores = list(map(int, survey_data.split(",")))  
    print(f"Max Score: {max(scores)}, Min Score: {min(scores)}")  

survey_data = "5,3,4,1,2"
analyze_survey(survey_data)
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
Answer:
```python
def manage_access(users, roles):
    access_list = zip(users, roles)  
    for user, role in access_list:
        print(f"{user}: {role}") 
users = ["Alice", "Bob", "Charlie"]
roles = ("Admin", "Editor", "Viewer")
manage_access(users, roles)
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
```python
def categorize_ticket(message):
    length = len(message)
    if length < 20:
        category = "Short"
    elif 20 <= length <= 50:
        category = "Medium"
    else:
        category = "Long"
    
    print(f"Category: {category}")
message = "My account is locked, please help!"
categorize_ticket(message)
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
```python
def longest_name(products):
  return max(products,key=lambda x:x[0])
products = ["Laptop", "Smartphone", "Wireless Headphones"]
longest_name(products)
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
```python
def last_ten_avg(sensor_readings):
   last_10_readings = readings[-10:] 
   avg = sum(last_10_readings) // len(last_10_readings)
   print(f"Average: {avg}")
sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]
average_last_10(sensor_readings)
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
```python
transactions = [100, -50, 200, -150, 50]
print(transactions[::-1])
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
```python
def format_logs(logs, timestamp):
    return [f"{timestamp}: {log}" for log in logs]  
logs = ["System Boot", "Network Connected", "User Login"]
timestamp = "2025-03-20"

formatted_logs = format_logs(logs, timestamp)
print(formatted_logs)

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
```python
def generate_pattern(symbol, count):
    return ' '.join([symbol] * count)
symbol = "*"
count = 5

pattern = generate_pattern(symbol, count)
print(pattern)

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
 ```python
 def count_keyword(feedback, keyword):
    count = feedback.lower().split().count(keyword.lower()) 
    print(f"'{keyword}' count: {count}")
feedback = "The product is excellent, absolutely excellent!"
keyword = "excellent"
count_keyword(feedback, keyword)
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
```python
  def first_occ(word,log):
    return log.lower().index(word.lower())-1
  log = "INFO: All systems go. ERROR: Failed to start service."
  word="error"
  print(first_occ(word,log))
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
```python
def csv_to_list(csv_data):
    return [row.split(",") for row in csv_data.split("\n")]
csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"
print(csv_to_list(csv_data))
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
```python
def generate_usernames(names):
    return [f"{name.split()[0][0]}{name.split()[1]}" for name in names] 
names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]
usernames = generate_usernames(names)
print(usernames)
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
```python
from collections import Counter
def count_messages(chat_logs):
    message_counts = Counter(log.split(":")[0] for log in chat_logs)  
    return ", ".join(f"{user}: {count} messages" for user, count in message_counts.items())
chat_logs = [
    "Alice: Hi!",
    "Bob: Hello!",
    "Alice: How are you?",
    "Bob: I’m good, thanks!"
]

result = count_messages(chat_logs)
print(result)

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
```python
def compress_data(data):
    for i in range(1, len(data) // 2 + 1):  
        substring = data[:i] 
        if data == substring * (len(data) // len(substring)): 
            return f"'{substring}' repeated {len(data) // len(substring)} times"
    return "No repeating pattern found"
data = "abababababab"
result = compress_data(data)
print(result)
```
---