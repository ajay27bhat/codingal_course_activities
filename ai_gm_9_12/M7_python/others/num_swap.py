# Take two numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap the numbers
a, b = b, a

print("\nAfter swapping:")
print("a =", a)
print("b =", b)