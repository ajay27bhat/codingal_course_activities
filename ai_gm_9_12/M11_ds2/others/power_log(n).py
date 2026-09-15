base = int(input("Enter base: "))
power = int(input("Enter power: "))

result = 1

while power > 0:
    if power & 1:
        result = result * base

    base = base * base
    power = power >> 1

print("Answer:", result)