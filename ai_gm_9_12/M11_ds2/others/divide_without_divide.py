dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

quotient = 0

while dividend >= divisor:
    temp = divisor
    multiple = 1

    while (temp << 1) <= dividend:
        temp = temp << 1
        multiple = multiple << 1

    dividend = dividend - temp
    quotient = quotient + multiple

print("Quotient:", quotient)