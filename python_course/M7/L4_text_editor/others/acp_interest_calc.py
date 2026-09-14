import tkinter as tk

def calculate_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())

    interest = (principal * rate * time) / 100

    result_label.config(
        text=f"Simple Interest = ₹{interest:.2f}"
    )


# Create window
window = tk.Tk()
window.title("Simple Interest Calculator")
window.geometry("400x350")

# Heading
title_label = tk.Label(
    window,
    text="Simple Interest Calculator",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

# Principal
principal_label = tk.Label(window, text="Principal Amount:")
principal_label.pack()

principal_entry = tk.Entry(window)
principal_entry.pack(pady=5)

# Rate
rate_label = tk.Label(window, text="Rate of Interest (%):")
rate_label.pack()

rate_entry = tk.Entry(window)
rate_entry.pack(pady=5)

# Time
time_label = tk.Label(window, text="Time (Years):")
time_label.pack()

time_entry = tk.Entry(window)
time_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(
    window,
    text="Calculate Interest",
    command=calculate_interest
)
calculate_button.pack(pady=15)

# Result
result_label = tk.Label(
    window,
    text="Result",
    font=("Arial", 14)
)
result_label.pack()

# Start the application
window.mainloop()
