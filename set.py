# 1. Create a set containing five integers and display elements
print("\n--- 1. Set of Five Integers ---")

numbers = {10, 20, 30, 40, 50}

print("Set:", numbers)

for num in numbers:
    print(num)


# 2. Convert list with duplicates into a set
print("\n--- 2. Remove Duplicates Using Set ---")

numbers = [10, 20, 10, 30, 20, 40, 30]

result = set(numbers)

print("Original list:", numbers)
print("Set:", result)


# 3. Add two new fruits
print("\n--- 3. Add Fruits ---")

fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

fruits.add("Pineapple")
fruits.add("Watermelon")

print("Updated set:", fruits)


# 4. Remove a specified number
print("\n--- 4. Remove Number from Set ---")

numbers = {10, 20, 30, 40, 50}

num = int(input("Enter number to remove: "))

if num in numbers:
    numbers.remove(num)
    print("Number removed.")
else:
    print("Number not found.")

print("Updated set:", numbers)


# 5. Check whether student exists
print("\n--- 5. Student Search ---")

students = {"Rahul", "Amit", "Priya", "Sneha", "Karan"}

name = input("Enter student name: ")

if name in students:
    print("Student exists in the set.")
else:
    print("Student does not exist.")


# 6. Total number of cities
print("\n--- 6. Number of Cities ---")

cities = {"Pune", "Mumbai", "Delhi", "Chennai", "Kolkata"}

print("Cities:", cities)
print("Total number of cities:", len(cities))


# 7. Display programming languages using for loop
print("\n--- 7. Programming Languages ---")

languages = {"Python", "Java", "C", "C++", "JavaScript"}

for language in languages:
    print(language)


# 8. Remove duplicate numbers using set
print("\n--- 8. Remove Duplicate Numbers ---")

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique_numbers = set(numbers)

print("Original list:", numbers)
print("After removing duplicates:", unique_numbers)


# 9. Union of two sets
print("\n--- 9. Union of Sets ---")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)


# 10. Common elements of two sets
print("\n--- 10. Common Elements ---")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common = set1.intersection(set2)

print("Common elements:", common)


# 11. Difference between two sets
print("\n--- 11. Difference of Sets ---")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

first_only = set1 - set2
second_only = set2 - set1

print("Elements in first set but not second:", first_only)
print("Elements in second set but not first:", second_only)


# 12. Elements in either set but not both
print("\n--- 12. Symmetric Difference ---")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

result = set1.symmetric_difference(set2)

print("Elements in either set but not both:", result)


# 13. Check subset
print("\n--- 13. Subset ---")

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

if set1.issubset(set2):
    print("First set is a subset of second set.")
else:
    print("First set is not a subset of second set.")


# 14. Check superset
print("\n--- 14. Superset ---")

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

if set1.issuperset(set2):
    print("First set is a superset of second set.")
else:
    print("First set is not a superset of second set.")


# 15. Check whether sets have no common elements
print("\n--- 15. Disjoint Sets ---")

set1 = {1, 2, 3}
set2 = {4, 5, 6}

if set1.isdisjoint(set2):
    print("The sets have no elements in common.")
else:
    print("The sets have common elements.")


# 16. Check whether two sets are equal
print("\n--- 16. Equal Sets ---")

set1 = {1, 2, 3, 4}
set2 = {4, 3, 2, 1}

if set1 == set2:
    print("Both sets are equal.")
else:
    print("Both sets are not equal.")


# 17. Subjects selected by two students
print("\n--- 17. Common Subjects ---")

student1 = {"Python", "Maths", "English", "Physics"}
student2 = {"Java", "Maths", "Physics", "Chemistry"}

common_subjects = student1.intersection(student2)

print("Student 1 subjects:", student1)
print("Student 2 subjects:", student2)
print("Subjects studied by both:", common_subjects)


# 18. Unique words in a sentence
print("\n--- 18. Unique Words ---")

sentence = input("Enter a sentence: ")

words = sentence.split()

unique_words = set(words)

print("Unique words:", unique_words)


# 19. Morning and afternoon sessions
print("\n--- 19. Session Attendance ---")

morning = {
    "Rahul",
    "Amit",
    "Priya",
    "Sneha"
}

afternoon = {
    "Priya",
    "Sneha",
    "Karan",
    "Rohan"
}

both_sessions = morning & afternoon
morning_only = morning - afternoon
afternoon_only = afternoon - morning
at_least_one = morning | afternoon

print("Students present in both sessions:", both_sessions)
print("Students only in morning:", morning_only)
print("Students only in afternoon:", afternoon_only)
print("Students in at least one session:", at_least_one)


# 20. Students enrolled in Python and Java
print("\n--- 20. Course Enrollment ---")

python_students = {
    "Rahul",
    "Amit",
    "Priya",
    "Sneha"
}

java_students = {
    "Priya",
    "Sneha",
    "Karan",
    "Rohan"
}

print("Python students:", python_students)
print("Java students:", java_students)


# 21. Students in both courses and only one course
print("\n--- 21. Course Comparison ---")

python_students = {
    "Rahul",
    "Amit",
    "Priya",
    "Sneha"
}

java_students = {
    "Priya",
    "Sneha",
    "Karan",
    "Rohan"
}

both_courses = python_students & java_students
only_one_course = python_students ^ java_students

print("Students enrolled in both courses:", both_courses)
print("Students enrolled in only one course:", only_one_course)


# 22. Technical skills of two employees
print("\n--- 22. Employee Skills ---")

employee1 = {
    "Python",
    "Java",
    "SQL",
    "Git"
}

employee2 = {
    "Python",
    "C++",
    "SQL",
    "Docker"
}

common_skills = employee1 & employee2
unique_employee1 = employee1 - employee2
unique_employee2 = employee2 - employee1
all_skills = employee1 | employee2

print("Common skills:", common_skills)
print("Skills unique to Employee 1:", unique_employee1)
print("Skills unique to Employee 2:", unique_employee2)
print("All available skills:", all_skills)


# 23. Available books and requested books
print("\n--- 23. Book Availability ---")

available_books = {
    "Python Programming",
    "Data Structures",
    "Database Systems",
    "Computer Networks"
}

requested_books = {
    "Python Programming",
    "Operating Systems",
    "Database Systems",
    "Machine Learning"
}

available_requested = available_books & requested_books

print("Requested books:", requested_books)
print("Books that are available:", available_requested)


# 24. Visitor IDs from two different days
print("\n--- 24. Visitor IDs ---")

day1 = {
    101,
    102,
    103,
    104,
    105
}

day2 = {
    103,
    104,
    105,
    106,
    107
}

unique_visitors = day1 | day2
returning_visitors = day1 & day2
first_day_only = day1 - day2
second_day_only = day2 - day1

print("Unique visitors across both days:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors only on first day:", first_day_only)
print("Visitors only on second day:", second_day_only)


# 24 (continued). Products belonging to different categories
print("\n--- 24. Products in Both Categories ---")

category1 = {
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
}

category2 = {
    "Keyboard",
    "Monitor",
    "Printer",
    "Scanner"
}

common_products = category1 & category2

print("Products in both categories:", common_products)


# 25. Friends of two users
print("\n--- 25. Friends of Two Users ---")

user1 = {
    "Rahul",
    "Amit",
    "Priya",
    "Sneha",
    "Karan"
}

user2 = {
    "Priya",
    "Sneha",
    "Rohan",
    "Vikas",
    "Karan"
}

mutual_friends = user1 & user2
unique_user1 = user1 - user2
unique_user2 = user2 - user1
total_unique_friends = user1 | user2

print("Mutual friends:", mutual_friends)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total unique friends:", total_unique_friends)
print("Total number of unique friends:", len(total_unique_friends))