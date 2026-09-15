# Program to display Student Details

class Student:

    # Constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to display student details
    def display(self):
        print("Student Details")
        print("----------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)


# Create a student object
student1 = Student("John", 15, 10)

# Display student details
student1.display()