import tkinter as tk
from tkinter import ttk, messagebox


# Menu items and prices
menu_items = {
    "FRIES MEAL": 2,
    "LUNCH MEAL": 2,
    "BURGER MEAL": 3,
    "PIZZA MEAL": 4,
    "CHEESE BURGER": 2.5,
    "DRINKS": 1
}

entries = {}


# Place order
def place_order():

    total = 0
    summary = "Order Summary:\n"

    for item, entry in entries.items():

        quantity = entry.get()

        if quantity.isdigit():
            quantity = int(quantity)

            if quantity > 0:
                price = menu_items[item]
                cost = quantity * price

                total += cost

                summary += f"{item}: {quantity} x ${price} = ${cost}\n"

    if total > 0:
        summary += f"\nTotal Cost: ${total}"
        messagebox.showinfo("Order Placed", summary)
    else:
        messagebox.showerror(
            "Error",
            "Please order at least one item."
        )


# Main window
root = tk.Tk()
root.title("Restaurant Order Management")
root.geometry("800x600")

# Canvas for background
canvas = tk.Canvas(root, width=800, height=600, bg="darkgreen")
canvas.pack()


# Frame
frame = ttk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# Heading
ttk.Label(
    frame,
    text="Restaurant Order Management",
    font=("Arial", 20, "bold")
).grid(row=0, columnspan=2, padx=10, pady=10)


# Menu items
for row, (item, price) in enumerate(menu_items.items(), start=1):

    ttk.Label(
        frame,
        text=f"{item} (${price})",
        font=("Arial", 14)
    ).grid(row=row, column=0, padx=10, pady=5)

    entry = ttk.Entry(frame, width=5, font=("Arial", 14))
    entry.grid(row=row, column=1, padx=10, pady=5)

    entries[item] = entry
 

# Connect button to function
ttk.Button(
    frame,
    text="Place Order",
    command=place_order
).grid(row=7, columnspan=2, pady=10)


# Start the application
root.mainloop()