"""
Activity: School Store Inventory

Instructions:
1. Create a list of items and their stock quantities.
2. Create a dictionary by pairing each item with its stock.
3. Display the items that are currently in stock.
4. Ask the customer which item they want to buy.
5. Check whether the item is available.
6. Create a list of prices for the items.
7. Find and display the price of the selected item.
8. Reduce the stock by 1 after the purchase.
9. Display the updated inventory.
"""

# Create lists of items, stock quantities, and prices
items = ["pencil", "eraser", "notebook", "sharpener", "glue"]
stock = [12, 0, 8, 5, 3]
prices = [10, 5, 40, 15, 20]

# Create a dictionary by pairing each item with its stock
inventory = dict(zip(items, stock))

print("Inventory:", inventory)

# Find the items that are currently in stock
in_stock = [item for item in items if inventory[item] > 0]
print("Items in stock:", in_stock)

# Ask the customer which item they want to buy
chosen_item = input("Which item do you want to buy? ").lower()

# Check whether the item exists and is in stock
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print("Sorry, this item is not available.")
    exit()

# Find the price of the selected item
index = items.index(chosen_item)
price = prices[index]

print("Price of", chosen_item, ":", price)

# Reduce the stock after the purchase
inventory[chosen_item] -= 1

print("Purchase successful!")
print("Remaining stock:", inventory[chosen_item])

# Display the final summary
print("\n===== SCHOOL STORE SUMMARY =====")
print("Item Bought      :", chosen_item)
print("Price Paid       :", price)
print("Updated Inventory:", inventory)
print("================================")