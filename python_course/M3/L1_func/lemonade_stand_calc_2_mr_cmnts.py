"""
Activity: Lemonade Stand

Instructions:
1. Create a function to greet the customer.
2. Ask the user to enter the price per cup and number of cups sold.
3. Create a function to calculate the total cost.
4. Display the total cost.
5. Ask the user to enter the amount paid.
6. Create a function to calculate the change.
7. Display the final receipt.
"""

# Create a function with no arguments
def greet_customer():
    print("Welcome to the Lemonade Stand!")
    print("Enjoy our fresh lemonade.\n")

# Call the function
greet_customer()

# Get user input
price = float(input("Enter price per cup: "))
cups = int(input("Enter number of cups sold: "))

# Create a function with arguments that returns the total cost
def calculate_total(price, cups):
    return price * cups

# Call the function and store the returned value
total = calculate_total(price, cups)

print("Total Cost:", round(total, 2))



# Create a function that returns a thank-you message
def thank_you():
    return "Thank you for visiting!"

# Display the final receipt
print("\n===== RECEIPT =====")
print("Price Per Cup :", price)
print("Cups Sold     :", cups)
print("Total Cost    :", round(total, 2))
print(thank_you())
print("===================")