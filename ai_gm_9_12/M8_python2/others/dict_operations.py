# Program to demonstrate Dictionary Operations

student = {
    "name": "John",
    "age": 15,
    "grade": 10
}

# 1. Accessing a value
print("Name:", student["name"])

# 2. Adding a new item
student["city"] = "Bangalore"
print("After adding:", student)

# 3. Updating a value
student["age"] = 16
print("After updating:", student)

# 4. Removing an item
student.pop("city")
print("After removing:", student)

# 5. Getting all keys
print("Keys:", student.keys())

# 6. Getting all values
print("Values:", student.values())

# 7. Getting key-value pairs
print("Items:", student.items())

# 8. Checking if a key exists
print("Is 'name' present?", "name" in student)