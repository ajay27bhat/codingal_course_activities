# Program to display odd lines from a file

# Open the file
file = open("sample.txt", "r")

lines = file.readlines()

# Display odd-numbered lines
print("Odd Lines:")

for i in range(0, len(lines), 2):
    print(lines[i].strip())

file.close()