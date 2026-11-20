from tkinter import *

window = Tk()
window.title("APP")
window.geometry("400x300")


# Store the number pad values in a nested list
numbers = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
    ["#", 0, "*"]
]

# Make the columns and rows expand with the window
for column in range(3):
    window.columnconfigure(column, weight=1)

for row in range(4):
    window.rowconfigure(row, weight=1)

for row in range(4):
    for column in range (3):
        frame = Frame (window, relief = "sunken", borderwidth = 1)
        frame.grid(row = row , column = column , sticky = "nsew")
        lable = Label(frame, text = numbers[row][column] )
        lable.pack(expand = True)

window.mainloop()