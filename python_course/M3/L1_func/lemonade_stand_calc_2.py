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
7. Create a function calculate_change(paid, total) that returns the change.
8. Display the change due.
9. Create a function thank_you() that returns a thank-you message.
10. Display the final receipt.
"""

# Function with no arguments
def greet_customer():
    print("Welcome to the Lemonade Stand!")
    print("Enjoy our fresh lemonade.\n")

# Call the function
greet_customer()

# User Input
price = float(input("Enter price per cup: "))
cups = int(input("Enter number of cups sold: "))

# Function with arguments and return value
def calculate_total(price, cups):
    return price * cups

# Call the function
total = calculate_total(price, cups)

print("Total Cost:", round(total, 2))

# User Input
paid = float(input("Enter amount paid: "))

# Function with arguments and return value
def calculate_change(paid, total):
    return paid - total

# Call the function
change = calculate_change(paid, total)

print("Change Due:", round(change, 2))

# Function that returns a message
def thank_you():
    return "Thank you for visiting!"

# Final Receipt
print("\n===== RECEIPT =====")
print("Price Per Cup :", price)
print("Cups Sold     :", cups)
print("Total Cost    :", round(total, 2))
print("Amount Paid   :", paid)
print("Change Due    :", round(change, 2))
print(thank_you())
print("===================")