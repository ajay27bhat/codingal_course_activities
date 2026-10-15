"""
Activity: Lemonade Stand

Instructions:
1. Create a function named greet_customer() that displays a welcome message.
2. Call the function.
3. Ask the user to enter:
   - Price per cup
   - Number of cups sold
4. Create a function calculate_total(price, cups) that returns the total cost.
5. Call the function and display the total cost using round().
6. Ask the user to enter the amount paid.
10. Display the final receipt.
"""

"""
OUTPUT:

Welcome to the Lemonade Stand!
Price per cup is 10

Enter number of cups you want: 4

===== RECEIPT =====
Price Per Cup : 10
Cups sold     : 4
Total Cost    : 40
===================
"""

# Function with arguments and return value
def calculate_total(price, cups):
    return price * cups


# Define price per cup
price = 10

print("Welcome to the Lemonade Stand!")
print(f"Price per cup is {price}")

# User Input
cups = int(input("Enter number of cups you want: "))

# Call the function
total = calculate_total(price, cups)

# Final Receipt
print("\n===== RECEIPT =====")
print("Price Per Cup :", price)
print("Cups Sold     :", cups)
print("Total Cost    :", total)
print("===================")