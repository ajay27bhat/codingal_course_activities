# Electricity Bill using Nested If-Else

units = int(input("Enter electricity units consumed: "))
customer = input("Customer type (domestic/commercial): ")

if customer.lower() == "domestic":
    if units <= 100:
        bill = units * 2
    else:
        bill = (100 * 2) + ((units - 100) * 3)
else:
    if units <= 100:
        bill = units * 4
    else:
        bill = (100 * 4) + ((units - 100) * 5)

print("Total Electricity Bill = $", bill)