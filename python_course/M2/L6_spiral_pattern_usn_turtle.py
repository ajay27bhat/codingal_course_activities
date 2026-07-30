import turtle

t = turtle.Turtle()

t.speed(0)  # Fastest speed

for i in range(100):
    t.forward(i * 5)
    t.right(90)

turtle.done()