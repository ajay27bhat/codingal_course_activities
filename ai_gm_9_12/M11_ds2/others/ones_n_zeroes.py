num = int(input("Enter a number: "))

ones = 0
zeros = 0

while num > 0:
    if num & 1:
        ones += 1
    else:
        zeros += 1

    num = num >> 1

print("Number of ones:", ones)
print("Number of zeros:", zeros)