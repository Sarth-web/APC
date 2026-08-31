
#1---------------------------------------------------------------------------------
fruits = ["apple", "mango", "banana", "kiwi", "watermelon"] #list of fruitss
print(fruits)
print()

#2---------------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5,] #list for numbers
print(numbers)
print()

print(fruits[0])
print(fruits[4])
print(fruits[2])
print()

#3--------------------------------------------------------------------
colors = ["red", "purple", "blue", "voilet"]

print(colors) 
print()

colors[2] = "yellow" #replacing third elemement

print(colors) #updated list
print()
#4---------------------------------------------------------------
print("inserting at beginning: ",numbers.insert(0, 10))
print()
print("inserting at end:  ", numbers.append(10))
print()

print("inserting at specific position 3rd: ", numbers.insert(2, 5))
print()
#5-------------------------------------------------------------------
students = ["jarvis", "tony stark" "captain america", "hulk", "hoakeye" "thor"]
print("removed first element: ",students.pop(0))
print("removed last element: ",students.pop())
print("removed specified position element: ", students.pop(1))
print()

#6------------------------------------------------------

smallest = numbers[0]
largest = numbers[0]

for num in numbers[1:]:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
print("ssmallest = ", smallest)
print("largest = ", largest)
print()

#7--------------------------------------------------------

NumbersAgain = []
for n in range(3):
    n = int(input("enters numbers"))
    NumbersAgain.append(n)

print(NumbersAgain)

#8 count even and odd-------------------------

numbers = [10, 21, 32, 43, 54, 65, 76, 87, 98, 11, 22, 33, 44, 55, 66]

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers =", even)
print("Odd numbers =", odd)

#10 Reverse a list without using reverse() ------------------------------
numbers = [10, 20, 30, 40, 50]

reverse = []

for i in numbers:
    reverse.insert(0, i)

print("Original list:")
print(numbers)

print("Reverse list:")
print(reverse)

