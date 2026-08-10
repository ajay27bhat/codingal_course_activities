numbers = [1, 2, 3, 4, 5]

def square(n):
    return n * n

result = list(map(square, numbers))

print("Numbers:", numbers)
print("Squares:", result)