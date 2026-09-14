import tkinter as tk

def convert_length():
    value = float(entry.get())

    if unit.get() == "Meters to Kilometers":
        result = value / 1000
        result_label.config(text=f"{result} km")

    elif unit.get() == "Kilometers to Meters":
        result = value * 1000
        result_label.config(text=f"{result} m")

    elif unit.get() == "Centimeters to Meters":
        result = value / 100
        result_label.config(text=f"{result} m")

    elif unit.get() == "Meters to Centimeters":
        result = value * 100
        result_label.config(text=f"{result} cm")


# Create window
window = tk.Tk()
window.title("Length Converter")
window.geometry("400x300")

# Heading
title_label = tk.Label(
    window,
    text="Length Converter",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)

# Input
entry = tk.Entry(window)
entry.pack(pady=5)

# Dropdown
unit = tk.StringVar()
unit.set("Meters to Kilometers")

options = [
    "Meters to Kilometers",
    "Kilometers to Meters",
    "Centimeters to Meters",
    "Meters to Centimeters"
]

dropdown = tk.OptionMenu(window, unit, *options)
dropdown.pack(pady=5)

# Button
button = tk.Button(
    window,
    text="Convert",
    command=convert_length
)
button.pack(pady=15)

# Result
result_label = tk.Label(
    window,
    text="Result",
    font=("Arial", 14)
)
result_label.pack()

# Start the app
window.mainloop()
