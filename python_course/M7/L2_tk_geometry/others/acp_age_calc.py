import tkinter as tk
from datetime import date

# Create the window
window = tk.Tk()
window.title("Age Calculator")
window.geometry("400x300")


def calculate_age():
    birth_year = int(year_entry.get())
    birth_month = int(month_entry.get())
    birth_day = int(day_entry.get())

    today = date.today()
    birth_date = date(birth_year, birth_month, birth_day)

    age = today.year - birth_date.year

    # Check if birthday has happened this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    result_label.config(text=f"You are {age} years old.")


# Heading
title_label = tk.Label(
    window,
    text="Age Calculator",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)


# Day
day_label = tk.Label(window, text="Day:")
day_label.pack()

day_entry = tk.Entry(window)
day_entry.pack()


# Month
month_label = tk.Label(window, text="Month:")
month_label.pack()

month_entry = tk.Entry(window)
month_entry.pack()


# Year
year_label = tk.Label(window, text="Year:")
year_label.pack()

year_entry = tk.Entry(window)
year_entry.pack()


# Button
calculate_button = tk.Button(
    window,
    text="Calculate Age",
    command=calculate_age
)
calculate_button.pack(pady=15)


# Result
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14)
)
result_label.pack()


# Start the application
window.mainloop()