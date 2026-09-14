import tkinter as tk


def check_password():
    password = password_entry.get()

    if len(password) < 8:
        result_label.config(text="Password is too short!")

    elif not any(char.isdigit() for char in password):
        result_label.config(text="Add at least one number!")

    elif not any(char.isupper() for char in password):
        result_label.config(text="Add at least one uppercase letter!")

    else:
        result_label.config(text="Password is strong!")


# Create window
window = tk.Tk()
window.title("Password Checker")
window.geometry("400x300")

# Heading
title_label = tk.Label(
    window,
    text="Password Checker",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)

# Password input
password_label = tk.Label(
    window,
    text="Enter your password:"
)
password_label.pack()

password_entry = tk.Entry(
    window,
    show="*"
)
password_entry.pack(pady=10)

# Check button
check_button = tk.Button(
    window,
    text="Check Password",
    command=check_password
)
check_button.pack(pady=10)

# Result
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 13)
)
result_label.pack(pady=10)

# Start the app
window.mainloop()
