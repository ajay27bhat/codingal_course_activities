# Program to demonstrate Lines in a File

# Create and write lines to a file
file = open("sample.txt", "w")

file.write("Python is easy to learn.\n")
file.write("Python is used for many applications.\n")
file.write("Python is a popular programming language.\n")

file.close()

# Read the file line by line
file = open("sample.txt", "r")

print("Lines in the file:")

for line in file:
    print(line.strip())

file.close()