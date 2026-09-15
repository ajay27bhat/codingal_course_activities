# Program to demonstrate File Handling Operations

# 1. Create and write to a file
file = open("sample.txt", "w")
file.write("Hello Python!\n")
file.write("This is a file handling program.")
file.close()

print("Data written to the file.")

# 2. Read the file
file = open("sample.txt", "r")
data = file.read()
print("\nFile Contents:")
print(data)
file.close()

# 3. Append data to the file
file = open("sample.txt", "a")
file.write("\nThis line was added later.")
file.close()

print("\nData appended to the file.")

# 4. Read the updated file
file = open("sample.txt", "r")
print("\nUpdated File Contents:")
print(file.read())
file.close()