# Algorithm: Check Whether a Number is Even Using a Function

# Step 1: Start the program.
# Step 2: Define a function named check_even(num).
# Step 3: Inside the function, check if the number is divisible by 2 using the modulus operator (%).
# Step 4: If the remainder is 0, display "The number is Even."
# Step 5: Otherwise, display "The number is Odd."
# Step 6: Ask the user to enter a number.
# Step 7: Call the check_even() function and pass the entered number as an argument.
# Step 8: Stop the program.

# Function to check whether a number is even or odd
def check_even(num):
    # Check if the number is divisible by 2
    if num % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")

# Take input from the user
number = int(input("Enter a number: "))

# Call the function
check_even(number)