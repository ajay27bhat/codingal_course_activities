# Sum of Natural Numbers using While Loop

n = int(input("Enter a positive number: "))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum of first", n, "natural numbers =", sum)