import tkinter as tk

# -------------------------------
# Calculate Denominations
# -------------------------------
def calculate():
    amount = int(amount_entry.get())

    denominations = [500, 200, 100, 50, 20, 10, 5, 1]

    # Create a top-level window
    result_window = tk.Toplevel(root)
    result_window.title("Denomination Result")
    result_window.geometry("300x350")

    tk.Label(
        result_window,
        text="Denomination Breakdown",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    for note in denominations:
        count = amount // note
        amount = amount % note

        tk.Label(
            result_window,
            text=f"₹{note} : {count}"
        ).pack(anchor="w", padx=60)


# -------------------------------
# Main Window
# -------------------------------
root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("400x250")

tk.Label(
    root,
    text="Denomination Calculator",
    font=("Arial", 16, "bold")
).pack(pady=20)

tk.Label(root, text="Enter Amount:").pack()

amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

tk.Button(
    root,
    text="Calculate",
    command=calculate
).pack(pady=20)

root.mainloop()