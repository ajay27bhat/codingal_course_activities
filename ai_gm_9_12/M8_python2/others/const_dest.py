# Program to demonstrate Constructor and Destructor

class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor called")

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    # Destructor
    def __del__(self):
        print("Destructor called")


# Creating an object
student1 = Student("John", 15)

# Calling the method
student1.display()

# Deleting the object
del student1