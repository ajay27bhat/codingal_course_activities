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

window = tk.Tk()
window.title("Resturant manager")
window.geometry("800x600")

# Canvas with bg
canvas = tk.Canvas(window, width=800, height=600, bg="darkgreen")
canvas.pack()

frame = ttk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

heading = ttk.Label(frame, text="Order", font=("Arial", 20, "bold"))
heading.grid(row=0, columnspan=2, padx=10, pady=10)

entries = {}

for row, (item, price) in enumerate(menu_items.items(), start=1):
    ttk.Label(
        frame,
        text=f"{item} (${price})",
        font=("Arial", 14)
    ).grid(row=row, column=0, padx=10, pady=5)

    entry = ttk.Entry(frame, width=5, font=("Arial", 14))
    entry.grid(row=row, column=1, padx=10, pady=5)

    entries[item] = entry




def calculate():
    total = 0
    summary = "Order Summary:\n"

    for item, entry in entries.items():
        quantity = int(entry.get())

        if quantity > 0:
            price = menu_items[item]
            cost = quantity * price

            total += cost

            summary += f"{item}: {quantity} x ${price} = ${cost}\n"
        
        if total > 0:
            summary += f"Total Cost: ${total}"
            messagebox.showinfo("Order Placed", summary)
        else:
            messagebox.showerror("Error", "Please order atlase 1 item")

            # menu_items = {
            #     "FRIES MEAL": 2,
            #     "LUNCH MEAL": 2,
            #     "BURGER MEAL": 3,
            #     "PIZZA MEAL": 4,
            #     "CHEESE BURGER": 2.5,
            #     "DRINKS": 1
            # }



button = ttk.Button(frame, text="Place Order", command=calculate)
button.grid(row=7, columnspan=2, pady=10, padx=5)

window.mainloop()