# Program to remove a line from a file

# Read all lines from the file
file = open("sample.txt", "r")
lines = file.readlines()
file.close()

# Remove the second line
lines.pop(1)

# Write the remaining lines back to the file
file = open("sample.txt", "w")
file.writelines(lines)
file.close()

print("Line removed successfully.")