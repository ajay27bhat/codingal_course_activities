"""
OUTPUT:
Snack Price: 25
Enter the amount paid: 32
Change Returned: 7
Thank you!
"""

# Snack Vending Machine

# Function to calculate change
def calculate_change(paid, price):
    return paid - price


# Main program
price = 25

print("Snack Price:", price)

paid = int(input("Enter the amount paid: "))

change = calculate_change(paid, price)

if change > 0:
    print("Change Returned:", change)
elif change == 0:
    print("No change to return.")
else:
    print("Insufficient amount!")

print("Thank you!")