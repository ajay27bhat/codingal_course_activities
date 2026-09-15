# Program to append content to a file

# Open the file in append mode
file = open("sample.txt", "a")

# Add new content
file.write("\nThis is new content.")
file.write("\nThis content was appended to the file.")

# Close the file
file.close()

print("Content appended successfully.")