"""
Activity: Simple Text Editor

Instructions:
1. Import Tkinter and the file dialog functions.
2. Create an application window with a title and size.
3. Create a Text widget to edit text.
4. Create an Open function to select and display a text file.
5. Create a Save function to save the text to a file.
6. Add Open and Save buttons.
7. Arrange the widgets using grid().
8. Start the Tkinter application.
"""

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Create the main application window
app_window = Tk()
app_window.title("Simple Text Editor")
app_window.geometry("600x500")

# Allow the text editor area to expand when the window is resized
app_window.rowconfigure(0, weight=1)
app_window.columnconfigure(1, weight=1)


# Create a function to open a file
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    # Clear the text editor
    text_editor.delete(1.0, END)

    # Read and display the file contents
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_editor.insert(END, text)

    app_window.title("Simple Text Editor - " + filepath)


# Create a function to save the file
def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    # Get the text from the editor and save it to the file
    with open(filepath, "w") as output_file:
        text = text_editor.get(1.0, END)
        output_file.write(text)

    app_window.title("Simple Text Editor - " + filepath)


# Create the text editor
text_editor = Text(app_window)

# Create a frame to hold the buttons
button_frame = Frame(app_window, relief=RAISED, bd=2)

# Create Open and Save buttons
open_button = Button(button_frame, text="Open", command=open_file)
save_button = Button(button_frame, text="Save As...", command=save_file)

# Arrange the buttons using grid()
open_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
save_button.grid(row=1, column=0, sticky="ew", padx=5)

# Arrange the frame and text editor
button_frame.grid(row=0, column=0, sticky="ns")
text_editor.grid(row=0, column=1, sticky="nsew")

# Start the Tkinter application
app_window.mainloop()