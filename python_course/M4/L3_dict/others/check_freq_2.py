"""
Activity: Count Students with a Particular Mark

Instructions:
1. Create a dictionary containing student names and their marks.
2. Ask the user for a mark to search for.
3. Use a for loop to check each student's mark.
4. Count how many students have the selected mark.
5. Display the result.
"""

# Store student names and their marks in a dictionary
marks = {
    "Aman": 80,
    "Riya": 90,
    "Rahul": 80,
    "Sneha": 75,
    "Arjun": 90
}

print("Student Marks:", marks)

# Ask the user which mark they want to count
search_mark = int(input("Enter a mark to search for: "))

count = 0

# Count how many students have the selected mark
for name in marks:
    if marks[name] == search_mark:
        count += 1

print("Number of students with", search_mark, "marks:", count)