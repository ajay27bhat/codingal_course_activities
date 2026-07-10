# Program to swap three values

# Get input from the user
a = input("Enter first value: ")
b = input("Enter second value: ")
c = input("Enter third value: ")

# Display original values
print("Before swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

# Swap the values
a, b, c = c, a, b

# Display swapped values
print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)