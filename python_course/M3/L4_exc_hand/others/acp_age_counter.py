def age_counter():
    try:
        age = int(input("Enter your age: "))
        print("Your age is:", age)
    except ValueError:
        print("Invalid input! Please enter a number.")


# Main program
age_counter()