# Program to demonstrate Python Operators

a = 10
b = 3

# 1. Arithmetic Operators
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# 2. Comparison Operators
print("\nComparison Operators:")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)

# 3. Logical Operators
x = True
y = False

print("\nLogical Operators:")
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)

# 4. Assignment Operators
number = 10

print("\nAssignment Operators:")
number += 5
print("After +=:", number)

number -= 3
print("After -=:", number)

number *= 2
print("After *=:", number)

number /= 4
print("After /=:", number)

# 5. Membership Operators
text = "Python"

print("\nMembership Operators:")
print("'P' in text:", "P" in text)
print("'z' not in text:", "z" not in text)