# 1. Create student.txt and write student details

name = input("Enter student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Branch: " + branch + "\n")
file.write("Semester: " + semester + "\n")

file.close()

print("Student details saved successfully.")


# 2. Open a text file and display complete contents

file = open("student.txt", "r")

data = file.read()

print(data)

file.close()


# 3. Append additional information without deleting old data

file = open("student.txt", "a")

file.write("College: ABC College\n")
file.write("City: Pune\n")

file.close()

print("Additional information added successfully.")


# 4. Read a text file line by line

file = open("student.txt", "r")

for line in file:
    print(line.strip())

file.close()


# 5. Count total number of lines in a text file

file = open("student.txt", "r")

lines = file.readlines()

print("Total number of lines:", len(lines))

file.close()


# 6. Count total number of words in a text file

file = open("student.txt", "r")

data = file.read()

words = data.split()

print("Total number of words:", len(words))

file.close()


# 7. Count total number of characters including spaces

file = open("student.txt", "r")

data = file.read()

print("Total number of characters:", len(data))

file.close()


# 8. Read a text file and display lines in reverse order

file = open("student.txt", "r")

lines = file.readlines()

for line in reversed(lines):
    print(line.strip())

file.close()


# 9. Count vowels and consonants in a text file

file = open("student.txt", "r")

data = file.read()

vowels = 0
consonants = 0

for ch in data:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

file.close()


# 10. Count alphabets, digits, spaces and special characters

file = open("student.txt", "r")

data = file.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in data:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

file.close()


# 11. Find the longest word in a text file

file = open("student.txt", "r")

data = file.read()

words = data.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

file.close()


# 12. Count how many times each word occurs using dictionary

file = open("student.txt", "r")

data = file.read().lower()

words = data.split()

word_count = {}

for word in words:
    word = word.strip(".,!?")

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")

for word, count in word_count.items():
    print(word, ":", count)

file.close()


# 13. Search for a word and display occurrences and line numbers

file = open("student.txt", "r")

search_word = input("Enter word to search: ")

count = 0
line_numbers = []

for line_number, line in enumerate(file, start=1):
    words = line.lower().split()

    for word in words:
        word = word.strip(".,!?")

        if word == search_word.lower():
            count += 1
            line_numbers.append(line_number)

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)

file.close()


# 14. Replace a word with another word and save in new file

file = open("student.txt", "r")

data = file.read()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

data = data.replace(old_word, new_word)

file.close()

new_file = open("modified.txt", "w")

new_file.write(data)

new_file.close()

print("Modified text saved in modified.txt")


# 15. Remove single-line comments from a Python source file

file = open("program.py", "r")
new_file = open("without_comments.py", "w")

for line in file:
    if not line.strip().startswith("#"):
        new_file.write(line)

file.close()
new_file.close()

print("Comments removed successfully.")



# 16. Create another file containing text in uppercase

file = open("student.txt", "r")

data = file.read()

file.close()

new_file = open("uppercase.txt", "w")

new_file.write(data.upper())

new_file.close()

print("Uppercase file created successfully.")


# 17. Student records
# Format: RollNo,Name,Marks

file = open("students.txt", "w")

file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")

file.close()

# Display all records

file = open("students.txt", "r")

print("All Student Records:")

for line in file:
    print(line.strip())

file.close()

# Read records

file = open("students.txt", "r")

students = []

for line in file:
    roll, name, marks = line.strip().split(",")
    students.append((roll, name, int(marks)))

file.close()

# Highest marks

highest = max(students, key=lambda x: x[2])

print("\nStudent with highest marks:")
print(highest[1], "-", highest[2])

# Average marks

total = 0

for student in students:
    total += student[2]

average = total / len(students)

print("Average marks:", average)

# Students scoring more than 80

print("\nStudents scoring more than 80:")

for student in students:
    if student[2] > 80:
        print(student[1], "-", student[2])


# 18. Employee records

file = open("employees.txt", "w")

file.write("101,Amit,IT,50000\n")
file.write("102,Priya,HR,45000\n")
file.write("103,Rahul,IT,60000\n")

file.close()


def display_employees():
    file = open("employees.txt", "r")

    for line in file:
        print(line.strip())

    file.close()


def highest_salary():
    file = open("employees.txt", "r")

    employees = []

    for line in file:
        emp_id, name, dept, salary = line.strip().split(",")
        employees.append((emp_id, name, dept, int(salary)))

    file.close()

    highest = max(employees, key=lambda x: x[3])

    print("Highest-paid employee:", highest[1])
    print("Salary:", highest[3])


def average_salary():
    file = open("employees.txt", "r")

    total = 0
    count = 0

    for line in file:
        data = line.strip().split(",")
        total += int(data[3])
        count += 1

    file.close()

    print("Average salary:", total / count)


def above_salary(amount):
    file = open("employees.txt", "r")

    print("Employees earning above", amount)

    for line in file:
        data = line.strip().split(",")

        if int(data[3]) > amount:
            print(data[1], "-", data[3])

    file.close()


print("All Employees:")
display_employees()

highest_salary()

average_salary()

above_salary(50000)


# 19. Student attendance records
# Format: RollNo,Name,PresentDays,TotalDays

file = open("attendance.txt", "w")

file.write("101,Amit,80,100\n")
file.write("102,Priya,90,100\n")
file.write("103,Rahul,70,100\n")

file.close()

file = open("attendance.txt", "r")

print("Students having attendance below 75%:")

for line in file:
    roll, name, present, total = line.strip().split(",")

    present = int(present)
    total = int(total)

    percentage = (present / total) * 100

    print(name, ":", percentage, "%")

    if percentage < 75:
        print("Below 75%:", name)

file.close()


# 20. Deposits and withdrawals
# Format:
# Deposit,5000
# Withdrawal,1000

file = open("transactions.txt", "w")

file.write("Deposit,5000\n")
file.write("Withdrawal,1000\n")
file.write("Deposit,3000\n")
file.write("Withdrawal,500\n")

file.close()

file = open("transactions.txt", "r")

total_deposit = 0
total_withdrawal = 0
largest = 0

for line in file:
    transaction, amount = line.strip().split(",")

    amount = int(amount)

    if transaction == "Deposit":
        total_deposit += amount
    elif transaction == "Withdrawal":
        total_withdrawal += amount

    if amount > largest:
        largest = amount

file.close()

final_balance = total_deposit - total_withdrawal

print("Total deposits:", total_deposit)
print("Total withdrawals:", total_withdrawal)
print("Final balance:", final_balance)
print("Largest transaction:", largest)


# 21. Book Management System
# Format: BookID,Title,Author,Status

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    file = open("books.txt", "a")
    file.write(book_id + "," + title + "," + author + ",Available\n")
    file.close()

    print("Book added successfully.")


def search_book():
    search_id = input("Enter book ID: ")

    file = open("books.txt", "r")

    found = False

    for line in file:
        data = line.strip().split(",")

        if data[0] == search_id:
            print("Book ID:", data[0])
            print("Title:", data[1])
            print("Author:", data[2])
            print("Status:", data[3])
            found = True

    file.close()

    if not found:
        print("Book not found.")


def issue_book():
    book_id = input("Enter book ID to issue: ")

    file = open("books.txt", "r")

    lines = file.readlines()

    file.close()

    file = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "Issued"
            line = ",".join(data) + "\n"

        file.write(line)

    file.close()

    print("Book issued.")


def return_book():
    book_id = input("Enter book ID to return: ")

    file = open("books.txt", "r")

    lines = file.readlines()

    file.close()

    file = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "Available"
            line = ",".join(data) + "\n"

        file.write(line)

    file.close()

    print("Book returned.")


def available_books():
    file = open("books.txt", "r")

    print("Available Books:")

    for line in file:
        data = line.strip().split(",")

        if data[3] == "Available":
            print(data[0], data[1], data[2])

    file.close()


# Example operations

add_book()
search_book()
issue_book()
return_book()
available_books()


# 22. Combine contents of two text files into third file

file1 = open("file1.txt", "r")
data1 = file1.read()
file1.close()

file2 = open("file2.txt", "r")
data2 = file2.read()
file2.close()

file3 = open("file3.txt", "w")

file3.write(data1)
file3.write("\n")
file3.write(data2)

file3.close()

print("Two files combined successfully.")


# 23. Compare two text files

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

if lines1 == lines2:
    print("Both files have identical contents.")
else:
    print("Files are different.")

    limit = min(len(lines1), len(lines2))

    found = False

    for i in range(limit):
        if lines1[i] != lines2[i]:
            print("First different line:", i + 1)
            print("File 1:", lines1[i].strip())
            print("File 2:", lines2[i].strip())
            found = True
            break

    if not found:
        print("Files have different number of lines.")