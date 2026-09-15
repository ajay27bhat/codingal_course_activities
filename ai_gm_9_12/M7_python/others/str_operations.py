# Program to demonstrate String Operations

text = "Hello Python"

# 1. Concatenation
first_name = "Hello"
last_name = "Python"
print("Concatenation:", first_name + " " + last_name)

# 2. Repetition
print("Repetition:", "Hi " * 3)

# 3. Length
print("Length:", len(text))

# 4. Indexing
print("First character:", text[0])
print("Last character:", text[-1])

# 5. Slicing
print("Slicing:", text[0:5])

# 6. Uppercase
print("Uppercase:", text.upper())

# 7. Lowercase
print("Lowercase:", text.lower())

# 8. Replace
print("Replace:", text.replace("Python", "World"))

# 9. Check if a string exists
print("Is 'Python' present?", "Python" in text)

# 10. Remove extra spaces
name = "   Ajay   "
print("After removing spaces:", name.strip())

# 11. Split
sentence = "Python is easy"
print("Split:", sentence.split())

# 12. Join
words = ["Python", "is", "easy"]
print("Join:", " ".join(words))