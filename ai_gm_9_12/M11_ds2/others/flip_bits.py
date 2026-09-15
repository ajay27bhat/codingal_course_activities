num = int(input("Enter a number: "))

bits = num.bit_length()

mask = (1 << bits) - 1

result = num ^ mask

print("After flipping bits:", result)