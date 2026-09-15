# Program to find duplicate lines in a file

file = open("sample.txt", "r")

lines = file.readlines()
file.close()

duplicates = []

for line in lines:
    line = line.strip()

    if lines.count(line + "\n") > 1 and line not in duplicates:
        duplicates.append(line)

print("Duplicate Lines:")

for line in duplicates:
    print(line)