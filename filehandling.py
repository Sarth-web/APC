# 1. Create and write to a file
file = open("student.txt", "w")
file.write("Name: Parshwa\n")
file.write("Roll No: 101\n")
file.write("Course: Computer Science\n")
file.close()

print("Data written successfully.")

# 2. Read the complete file
file = open("student.txt", "r")
data = file.read()
print("\nComplete file content:")
print(data)
file.close()

# 3. Read the file line by line
file = open("student.txt", "r")
print("First line:")
print(file.readline())
file.close()

# 4. Read all lines as a list
file = open("student.txt", "r")
print("All lines:")
print(file.readlines())
file.close()

# 5. tell() - shows current position of file pointer
file = open("student.txt", "r")
print("Current file pointer position:", file.tell())

# 6. seek() - moves file pointer to a specific position
file.seek(10)
print("File pointer after seek(10):", file.tell())

file.close()