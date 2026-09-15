# Program to demonstrate Read Operations

# Open the file in read mode
file = open("sample.txt", "r")

# 1. Read the entire file
print("Entire file:")
print(file.read())

file.close()


# Open the file again
file = open("sample.txt", "r")

# 2. Read one line
print("\nFirst line:")
print(file.readline())

file.close()


# Open the file again
file = open("sample.txt", "r")

# 3. Read all lines
print("All lines:")
print(file.readlines())

file.close()