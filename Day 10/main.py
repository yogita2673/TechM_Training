## Basics codes:-

# Open the file in read mode
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

# Open the file in read mode
with open("poem.txt", "r") as file:
    lines = file.readlines()  
print("Number of lines:", len(lines))

# List of tasks
tasks = [
    "Complete homework",
    "Buy groceries",
    "Call mom",
    "Go for a walk",
    "Read a book"
]
with open("reminder.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

# New task to add
new_task = "Water the plants"
with open("reminder.txt", "a") as file:
    file.write(new_task + "\n")

import os
if os.path.exists("data.txt"):  # Check if file exists
    with open("data.txt", "r") as file:
        content = file.read()
        print("File contents:")
        print(content)
else:
    print("data.txt does not exist.")


# Intermediate codes:-

# Remove Blank Lines
with open("input.txt", "r") as file:
    lines = file.readlines()

cleaned_lines = [line for line in lines if line.strip() != ""]

with open("cleaned.txt", "w") as file:
    file.writelines(cleaned_lines)

# Find and Replace
with open("article.txt", "r") as file:
    content = file.read()

updated_content = content.replace("Python", "PYTHON")

with open("article.txt", "w") as file:
    file.write(updated_content)

# Uppercase Writer
with open("input.txt", "r") as file:
    content = file.read()

with open("output.txt", "w") as file:
    file.write(content.upper())

# Student Report Generator
with open("students.txt", "r") as file:
    lines = file.readlines()

report = []
for line in lines:
    name, marks = line.strip().split(",")
    marks = int(marks)
    status = "Pass" if marks >= 50 else "Fail"
    report.append(f"{name}: {status}\n")

with open("report.txt", "w") as file:
    file.writelines(report)

# Reverse File Lines
with open("quotes.txt", "r") as file:
    lines = file.readlines()

with open("reversed_quotes.txt", "w") as file:
    file.writelines(reversed(lines))


# # Advance codes:- ,

# Log File Analyzer
with open("server.log", "r") as file:
    lines = file.readlines()

error_lines = [line for line in lines if "ERROR" in line]
error_count = len(error_lines)

print(f"Total ERRORs found: {error_count}")

with open("errors_only.log", "w") as file:
    file.writelines(error_lines)

log_data = """INFO: Server started successfully.
ERROR: Failed to connect to database.
INFO: New connection established.
ERROR: Timeout while fetching data.
WARNING: Disk space low.
INFO: Server running.
ERROR: Unexpected shutdown detected."""

with open("server.log", "w") as file:
    file.write(log_data)


# Word Frequency Counter
with open("story.txt", "r") as file:
    text = file.read()

words = text.lower().split()
frequency = {}

for word in words:
    word = word.strip(".,!?\"'()")  # Remove punctuation
    frequency[word] = frequency.get(word, 0) + 1

with open("frequency.txt", "w") as file:
    for word, count in frequency.items():
        file.write(f"{word}: {count}\n")

# CSV Reader + Filter
import csv

with open("sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    high_sales = [header]

    for row in reader:
        if row and int(row[1]) > 10000:  # Assuming amount is in column 2
            high_sales.append(row)

with open("high_sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(high_sales)

csv_content = """Date,Item,Amount
2024-04-01,Laptop,95000
2024-04-02,Mouse,750
2024-04-03,Monitor,12500
2024-04-04,Keyboard,2500
2024-04-05,Chair,10500
2024-04-06,Table,8900
2024-04-07,Headphones,12000"""

with open("sales.csv", "w") as file:
    file.write(csv_content)

# Merge Multiple Files
filenames = ["chapter1.txt", "chapter2.txt", "chapter3.txt"]
with open("full_book.txt", "w") as outfile:
    for fname in filenames:
        with open(fname, "r") as infile:
            outfile.write(infile.read() + "\n")


chapters = {
    "chapter1.txt": "Chapter 1: The Beginning\nOnce upon a time in a small town, there lived a curious cat named Luna.",
    "chapter2.txt": "Chapter 2: The Adventure\nLuna wandered far from home and discovered a hidden cave filled with glowing crystals.",
    "chapter3.txt": "Chapter 3: The Return\nWith a heart full of stories, Luna returned to the town and became a legend."
}

for filename, content in chapters.items():
    with open(filename, "w") as file:
        file.write(content)


# Directory File Scanner
import os

folder_path = "."  # current directory
files = os.listdir(folder_path)

for file in files:
    if file.endswith(".txt") or file.endswith(".csv"):
        print(file)









  


