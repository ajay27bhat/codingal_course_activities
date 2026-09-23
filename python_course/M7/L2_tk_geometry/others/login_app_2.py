"""
Activity: Create Account Form

Instructions:
1. Import Tkinter.
2. Create an application window with a title and size.
3. Create a frame to hold the form elements.
4. Add labels for name, email, and password.
5. Add Entry widgets to collect the user's details.
6. Create a function that gets the user's name and displays a message.
7. Add a button that calls the function when clicked.
8. Use a Text widget to display the message.
9. Arrange the widgets using place().
10. Start the Tkinter application.
"""

from tkinter import *

# Create the main application window
app_window = Tk()
app_window.title("Create Account")
app_window.geometry("400x400")


# Create a frame to organize the form
form_frame = Frame(app_window, height=200, width=360, bg="#d0efff")
form_frame.place(x=20, y=20)


# Add labels and input fields
name_label = Label(form_frame, text="Full Name", bg="green", fg="white")
email_label = Label(form_frame, text="Email ID", bg="green", fg="white")
password_label = Label(form_frame, text="Password", bg="green", fg="white")

name_entry = Entry(form_frame)
email_entry = Entry(form_frame)
password_entry = Entry(form_frame, show="*")


# Create a function to display the account message
def create_account():
    name = name_entry.get()

    message = "Hello " + name + "!\n"
    message += "Congratulations on creating your account!"

    message_box.insert(END, message)


# Add a button and message box
create_button = Button(
    app_window,
    text="Create Account",
    command=create_account,
    bg="red"
)

message_box = Text(app_window, height=5, width=40)


# Arrange the form widgets using place()
name_label.place(x=20, y=20)
name_entry.place(x=150, y=20)

email_label.place(x=20, y=70)
email_entry.place(x=150, y=70)

password_label.place(x=20, y=120)
password_entry.place(x=150, y=120)


# Place the button and message box
create_button.place(x=140, y=240)
message_box.place(x=20, y=280)


# Start the application
app_window.mainloop()