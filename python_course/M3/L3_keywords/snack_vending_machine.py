"""
Activity: Snack Vending Machine

Instructions:
1. Create a function to calculate the change.
2. Set the snack price and accepted coin values.
3. Keep accepting coins until enough money is inserted.
4. Reject any invalid coin using continue.
5. Stop accepting coins using break.
6. Calculate and display the change.
7. Use pass when there is no change to return.
8. Display the purchase summary.
"""

# Create a function that returns the change
def calculate_change(paid, price):
    return paid - price


# Set the snack price and accepted coin values
snack_price = 25
accepted_coins = [1, 5, 10, 25]

print("===== SNACK VENDING MACHINE =====")
print("Snack Price:", snack_price)
print("Accepted Coins:", accepted_coins)
print()

total_inserted = 0
coins_inserted = 0

# Keep accepting coins until enough money is inserted
while True:
    coin = int(input("Insert a coin: "))

    # Check whether the inserted coin is valid
    if coin not in accepted_coins:
        print("Invalid coin! Please try again.\n")
        continue

    total_inserted += coin
    coins_inserted += 1

    print("Total Inserted:", total_inserted)

    # Stop the loop once enough money has been inserted
    if total_inserted >= snack_price:
        break

# Calculate the change using the function
change_due = calculate_change(total_inserted, snack_price)

print("\nDispensing your snack...")

# Use pass when there is no change to return
if change_due == 0:
    pass
else:
    print("Change Returned:", change_due)

# Display the purchase summary
print("\n===== PURCHASE SUMMARY =====")
print("Snack Price    :", snack_price)
print("Coins Inserted :", coins_inserted)
print("Total Paid     :", total_inserted)
print("Change Given   :", change_due)
print("============================")
print("Thank you for your purchase!")