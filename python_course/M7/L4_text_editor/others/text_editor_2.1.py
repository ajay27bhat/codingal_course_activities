from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Create window
window = Tk()
window.title("Simple Text Editor")
window.geometry("600x500")


# Open a file
def open_file():
    filename = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("Allfiles", "*.*")]
    )

    if filename:
        with open(filename, "r") as file:
            text = file.read()

        txt_edit.delete(1.0, END)
        txt_edit.insert(END, text)


# Save a file
def save_file():
    filename = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if filename:
        with open(filename, "w") as file:
            text = txt_edit.get(1.0, END)
            file.write(text)


# Text box
txt_edit = Text(window)
txt_edit.pack(fill="both", expand=True)


# Buttons
btn_open = Button(window, text="Open", command=open_file)
btn_open.pack(side="left", padx=10, pady=10)

btn_save = Button(window, text="Save", command=save_file)
btn_save.pack(side="left", padx=10, pady=10)


# Start the application
window.mainloop()