import turtle

t = turtle.Turtle()

side = int(input("Enter the side length: "))

for i in range(4):
    t.forward(side)
    t.right(90)

turtle.done()