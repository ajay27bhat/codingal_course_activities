import math


def circumference(radius):
    return 2 * math.pi * radius

# Main program
r = float(input("Enter the radius of the circle: "))

c = circumference(r)

print("Circumference of the circle =", c)