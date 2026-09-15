# Program to demonstrate Tuple Operations

numbers = (10, 20, 30, 40, 50)

# 1. Accessing an element
print("First element:", numbers[0])

# 2. Accessing the last element
print("Last element:", numbers[-1])

# 3. Slicing
print("Sliced tuple:", numbers[1:4])

# 4. Finding the length
print("Length:", len(numbers))

# 5. Counting an element
numbers2 = (10, 20, 10, 30, 10)
print("Count of 10:", numbers2.count(10))

# 6. Finding the index of an element
print("Index of 30:", numbers.index(30))

# 7. Checking if an element exists
print("Is 20 present?", 20 in numbers)

# 8. Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print("Concatenated tuple:", tuple1 + tuple2)

# 9. Repeating a tuple
print("Repeated tuple:", (1, 2) * 3)