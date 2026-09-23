"""
Activity: Resizable Number Pad

Instructions:
1. Import Tkinter.
2. Create an application window with a title and size.
3. Create a nested list containing the number pad values.
4. Use nested for loops to create the number pad.
5. Use grid() to arrange the buttons in rows and columns.
6. Configure the rows and columns so they expand when the window is resized.
7. Start the Tkinter application.
"""

from tkinter import *

# Create the main application window
app_window = Tk()
app_window.title("Number Pad")
app_window.geometry("300x400")


# Store the number pad values in a nested list
numbers = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
    ["#", 0, "*"]
]


# Make the columns and rows expand with the window
for column in range(3):
    app_window.columnconfigure(column, weight=1)

for row in range(4):
    app_window.rowconfigure(row, weight=1)


# Use nested loops to create the number pad
for row in range(4):

    for column in range(3):

        # Create a frame for each number
        number_frame = Frame(
            app_window,
            relief=SUNKEN,
            borderwidth=1
        )
        number_frame.grid(
            row=row,
            column=column,
            sticky="nsew"
        )

        # Display the number inside the frame
        number_label = Label(
            number_frame,
            text=numbers[row][column],
            font=("Arial", 20)
        )
        number_label.pack(expand=True)


# Start the application
app_window.mainloop()