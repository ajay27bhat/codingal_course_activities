import tkinter as tk
import random


def play(choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)

    if choice == computer:
        result = "It's a tie!"

    elif (
        (choice == "Rock" and computer == "Scissors")
        or (choice == "Paper" and computer == "Rock")
        or (choice == "Scissors" and computer == "Paper")
    ):
        result = "You win!"

    else:
        result = "Computer wins!"

    result_label.config(
        text=f"You: {choice}\nComputer: {computer}\n\n{result}"
    )


# Create window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x350")

# Heading
title_label = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)

# Instruction
instruction_label = tk.Label(
    window,
    text="Choose your move:"
)
instruction_label.pack(pady=5)

# Buttons
rock_button = tk.Button(
    window,
    text="Rock",
    width=12,
    command=lambda: play("Rock")
)
rock_button.pack(pady=5)

paper_button = tk.Button(
    window,
    text="Paper",
    width=12,
    command=lambda: play("Paper")
)
paper_button.pack(pady=5)

scissors_button = tk.Button(
    window,
    text="Scissors",
    width=12,
    command=lambda: play("Scissors")
)
scissors_button.pack(pady=5)

# Result
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14)
)
result_label.pack(pady=20)

# Start the application
window.mainloop()