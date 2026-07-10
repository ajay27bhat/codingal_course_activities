# Program to check BMI category using AND, OR, and NOT operators

# Get input from the user
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI
print("Your BMI is:", round(bmi, 2))

# Check BMI category using logical operators
if bmi >= 18.5 and bmi <= 24.9:
    print("You have a Normal weight.")
elif bmi < 18.5 or bmi == 18.5:
    print("You are Underweight.")
elif not (bmi >= 18.5 and bmi <= 24.9):
    print("You are Overweight.")