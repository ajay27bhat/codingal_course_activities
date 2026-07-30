import turtle

t = turtle.Turtle()

sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of each side: "))

angle = 360 / sides

for i in range(sides):
    t.forward(length)
    t.left(angle)

turtle.done()