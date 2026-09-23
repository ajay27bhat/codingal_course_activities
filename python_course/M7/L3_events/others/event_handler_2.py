"""
Activity: Event Handler

Instructions:
1. Import Tkinter.
2. Create an application window.
3. Create a function to handle a keypress event.
4. Bind the keypress event to the function.
5. Create a button.
6. Create a function to handle the button click event.
7. Bind the button click event to the function.
8. Start the Tkinter application.
"""

from tkinter import *

# Create the main application window
app_window = Tk()
app_window.title("Event Handler")
app_window.geometry("250x150")


# Create a function to handle keyboard events
def handle_keypress(event):
    print("You pressed:", event.char)


# Connect the keyboard event to the function
app_window.bind("<Key>", handle_keypress)


# Create a function to handle button clicks
def handle_click(event):
    print("The button was clicked!")


# Create a button
button = Button(app_window, text="Click Me!")
button.pack(pady=30)


# Connect the button click event to the function
button.bind("<Button-1>", handle_click)


# Start the application
app_window.mainloop()