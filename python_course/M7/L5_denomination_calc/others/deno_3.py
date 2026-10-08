from tkinter import *
from tkinter import messagebox

# -------------------------------
# Calculate Denominations
# -------------------------------
def calculate():
    try:
        amount = int(amount_entry.get())

        denominations = [500, 200, 100, 50, 20, 10, 5, 1]

        # Create a top-level window
        result_window = Toplevel(root)
        result_window.title("Denomination Result")
        result_window.geometry("300x350")

        Label(
            result_window,
            text="Denomination Breakdown",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        for note in denominations:
            count = amount // note
            amount = amount % note

            Label(
                result_window,
                text=f"₹{note} : {count}"
            ).pack()

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


# -------------------------------
# Main Window
# -------------------------------
root = Tk()
root.title("Denomination Calculator")
root.geometry("400x250")

# Create widgets
title_label = Label(
    root,
    text="Denomination Calculator",
    font=("Arial", 16, "bold")
)

amount_label = Label(
    root,
    text="Enter Amount:"
)

amount_entry = Entry(root)

calculate_button = Button(
    root,
    text="Calculate",
    command=calculate
)

# Pack widgets
title_label.pack(pady=20)
amount_label.pack()
amount_entry.pack(pady=5)
calculate_button.pack(pady=20)

root.mainloop()