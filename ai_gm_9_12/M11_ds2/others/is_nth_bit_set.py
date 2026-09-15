num = int(input("Enter a number: "))
n = int(input("Enter the bit position: "))

if num & (1 << n):
    print("Bit is set")
else:
    print("Bit is not set")