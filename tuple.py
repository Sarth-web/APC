#1---------------------------------------
numbers = (1,2,3,4,5)
print("Tuples of Numbers: ", numbers)
print("_______________________________________")

#2.---------------------------------------
cities = ("kohapur", "Mumbai", "Pune", "Bangaloare")
print("Cities are: ", cities)

print("_______________________________________")
print()


#3.-----------------------------------------
students = ("Student1", "Student2", "Student3", "Student4")
print(students.__len__())
print("_______________________________________")
print()

#4.-----------------------------------------
colors = ("yellow", "red", "blue", "purple")
if "pink" in colors:
    print("pink is present in tuple")
else:
    print("pink is in tuple")
print("_______________________________________")
print()

#5--------------------------------------------------------

fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

print("\n1. Fruits:")
for fruit in fruits:
    print(fruit)


#6------------------------------------------------------------------

numbers = (10, 20, 10, 30, 10, 40, 20, 10)

print("\n2. Count of 10:")
print(numbers.count(10))


#7-------------------------------------------

employee_ids = (101, 102, 103, 104, 105)
given_id = 103

print("\n3. Index of employee ID 103:")
print(employee_ids.index(given_id))

#8---------------------------------------------------------------

tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)

result = tuple1 + tuple2

print("\n4. Concatenated tuple:")
print(result)


#9----------------------------------------------------------------

numbers = (1, 2, 3)

result = numbers * 4

print("\n5. Repeated tuple:")
print(result)

#10-----------------------------------------------------------------------

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("\n6. Tuple operations:")
print("First five elements:", numbers[:5])
print("Last five elements:", numbers[5:])
print("Middle four elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse tuple:", numbers[::-1])


#11----------------------------------------------------------------------

fruits = ("Apple", "Banana", "Mango")

fruit_list = list(fruits)
fruit_list.append("Orange")

print("\n7. List after adding new element:")
print(fruit_list)


#12----------------------------------------------------------------------------

numbers_list = []

print("\n8. Enter five numbers:")

for i in range(5):
    num = int(input("Enter number: "))
    numbers_list.append(num)

numbers_tuple = tuple(numbers_list)

print("Tuple:", numbers_tuple)

#13-------------------------------------------------------------------------------------

numbers = (10, 20, 30, 40)

number_list = list(numbers)

number_list[1] = 25

numbers = tuple(number_list)

print("\n9. Modified tuple:")
print(numbers)

#14-------------------------------------------------------------------------

numbers = (1, 2, 3, 4, 5)

print("\n10. Tuple before deletion:")
print(numbers)

del numbers

print("Tuple deleted successfully")


#15.---------------------------------------------------------------------------

students = (
    (101, "Rahul", "Computer Science"),
    (102, "Priya", "Information Technology"),
    (103, "Amit", "Mechanical")
)

print("\n11. Student records:")

for student in students:
    print("Roll Number:", student[0])
    print("Name:", student[1])
    print("Department:", student[2])
    print()

#16----------------------------------------------------------------------

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

total = sum(numbers)

print("\n12. Sum of numbers:")
print(total)

#17------------------------------------------------------------------------
numbers = (25, 10, 45, 5, 60, 30)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("\n13. Largest number:", largest)
print("Smallest number:", smallest)

#18----------------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

total = sum(numbers)
average = total / len(numbers)

print("\n14. Average:")
print(average)

#19----------------------------------------------------------------------

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\n15. Even and Odd count:")
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

#20-------------------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

num = int(input("\n16. Enter a number to search: "))

if num in numbers:
    print("Number exists in the tuple")
else:
    print("Number does not exist in the tuple")


#21------------------------------------------------------------------------------

student = (101, "Rahul", "Computer Science", 85)

print("\n17. Student Details:")
print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])
#---------------------------------------------------------------------------




