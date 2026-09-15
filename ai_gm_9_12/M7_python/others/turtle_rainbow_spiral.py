import turtle

# Create the turtle
t = turtle.Turtle()
t.speed(0)

# List of rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw the rainbow spiral
for i in range(100):
    t.pencolor(colors[i % 7])
    t.forward(i * 3)
    t.right(59)

# Keep the window open
turtle.done()