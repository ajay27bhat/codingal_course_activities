arr = [2, 4, 7, 2, 4, 7, 9, 9, 9, 9, 5, 5, 5]

xor = 0

# XOR all numbers
for num in arr:
    xor ^= num

# Find the rightmost set bit
bit = xor & -xor

num1 = 0
num2 = 0

# Divide numbers into two groups
for num in arr:
    if num & bit:
        num1 ^= num
    else:
        num2 ^= num

print("Odd occurring numbers:", num1, num2)