arr = [2, 3, 4, 2, 4, 3, 4]

result = 0

for num in arr:
    result = result ^ num

print("Odd occurring number:", result)