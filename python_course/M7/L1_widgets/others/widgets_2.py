"""
Activity: Welcome Application

Instructions:
1. Import Tkinter and the date module.
2. Create a window with a title and size.
3. Add a heading using a Label.
4. Add an Entry widget so the user can enter their name.
5. Create a function that gets the name and displays a welcome message.
6. Add a Button that calls the function when clicked.
7. Add a Text widget to display the message.
8. Arrange all the widgets using pack().
9. Start the Tkinter application.
"""

from tkinter import *
from datetime import date

# Create the main application window
app_window = Tk()
app_window.title("Welcome Application")
app_window.geometry("400x300")


# Add the heading and name input widgets
heading = Label(app_window, text="Welcome to My Application")
name_label = Label(app_window, text="Enter your name:")
name_entry = Entry(app_window)


# Create a function to display the welcome message
def display_message():
    name = name_entry.get()

    text_box.insert(END, "Hello " + name + "!\n")
    text_box.insert(END, "Welcome to the Application!\n")
    text_box.insert(END, "Today's date is: " + str(date.today()))


# Add a button and a text box
button = Button(app_window, text="Begin", command=display_message)
text_box = Text(app_window, height=5, width=40)


# Arrange the widgets in the window
heading.pack()
name_label.pack()
name_entry.pack()
button.pack()
text_box.pack()


# Start the application
app_window.mainloop()