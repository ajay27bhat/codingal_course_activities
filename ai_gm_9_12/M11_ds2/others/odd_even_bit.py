number = int(input("Enter a number: "))

# Check the last bit
if number & 1 == 0:
    print("Even number")
else:
    print("Odd number")