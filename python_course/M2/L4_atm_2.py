"""
Activity: ATM Cash Dispenser

Instructions:
1. Ask the user to enter their name.
2. Ask for the withdrawal amount.
3. Use a nested while loop to calculate the number of notes.
4. Display the notes given to the customer.
5. Ask if another customer wants to use the ATM.
6. After all customers are served, display:
   - Total customers served
   - Total money dispensed
"""

"""
OUTPUT:
=== ATM Cash Dispenser ===

Enter customer name: Ajay
Enter withdrawal amount: 100

Dispensing 100 units:

1 x 100 note(s)
Transaction complete!


Serve another customer? (yes/no): yes
Enter customer name: Rahul
Enter withdrawal amount: 125

Dispensing 125 units:

1 x 100 note(s)
1 x 20 note(s)
1 x 5 note(s)
Transaction complete!


Serve another customer? (yes/no): yes
Enter customer name: Chethan
Enter withdrawal amount: 107

Dispensing 107 units:

1 x 100 note(s)
1 x 5 note(s)
2 x 1 note(s)
Transaction complete!


Serve another customer? (yes/no): no

Customers Served : 3
Total Amount Dispensed : 332
ATM Closed
"""


print("=== ATM Cash Dispenser ===\n")

notes = [100, 50, 20, 10, 5, 1]
customers = 0
total_amount = 0

while True:
    name = input("Enter customer name: ")
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Please enter a valid amount.\n")
        continue

    print(f"\nDispensing {amount} units:\n")

    remaining = amount
    index = 0

    # Nested While Loop
    while index < len(notes):
        note = notes[index]
        count = remaining // note

        if count > 0:
            print(f"{count} x {note} note(s)")
            remaining = remaining % note

        index += 1

    print("Transaction complete!\n")

    customers += 1
    total_amount += amount

    choice = input("\nServe another customer? (yes/no): ").lower()

    if choice != "yes":
        break

print(f"\nCustomers Served : {customers}")
print(f"Total Amount Dispensed : {total_amount}")
print("ATM Closed")