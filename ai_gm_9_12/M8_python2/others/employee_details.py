# Program to display Employee Details

class Employee:

    # Constructor
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    # Method to display employee details
    def display(self):
        print("Employee Details")
        print("----------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Salary:", self.salary)


# Create an employee object
employee1 = Employee("John", 25, "IT", 50000)

# Display employee details
employee1.display()