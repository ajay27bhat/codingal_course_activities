# Program to merge two files

# Open the first file
file1 = open("file1.txt", "r")
content1 = file1.read()
file1.close()

# Open the second file
file2 = open("file2.txt", "r")
content2 = file2.read()
file2.close()

# Create the merged file
file3 = open("merged.txt", "w")

file3.write(content1)
file3.write("\n")
file3.write(content2)

file3.close()

print("Files merged successfully.")