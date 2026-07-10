# Program to find the square root of a number
# using two different methods

import math

# Get input from the user
num = float(input("Enter a number: "))

# Method 1: Using the ** operator
sqrt1 = num ** 0.5

# Method 2: Using math.sqrt()
sqrt2 = math.sqrt(num)

# Display the results
print("Square root using ** operator =", sqrt1)
print("Square root using math.sqrt() =", sqrt2)