# Student Grade Book

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Emma": 88
}

# Calculate class average using a for loop
total = 0

for score in students.values():
    total += score

average = total / len(students)

# Find top and bottom scorers
top_score = max(students.values())
bottom_score = min(students.values())

top_student = max(students, key=students.get)
bottom_student = min(students, key=students.get)

print("Class Average:", average)
print("Top Scorer:", top_student, "-", top_score)
print("Bottom Scorer:", bottom_student, "-", bottom_score)

# Look up a student's grade
name = input("Enter a student's name: ")
score = students.get(name)

if score is not None:
    print(name, "scored", score)
else:
    print("Student not found.")