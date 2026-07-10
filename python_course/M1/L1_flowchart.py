# Flowchart:

#              ╭──────────────────╮
#              │      START       │
#              ╰──────────────────╯
#                       │
#                       ▼
#           ╱──────────────────────╲
#          ╱  Enter a number (n)    ╲
#          ╲────────────────────────╱
#                       │
#                       ▼
#       ┌────────────────────────────────┐
#       │ Call check_even(n) function    │
#       └────────────────────────────────┘
#                       │
#                       ▼
#               ◇────────────────◇
#              ◇   Is n % 2 == 0? ◇
#               ◇────────────────◇
#                 │            │
#              Yes│            │No
#                 ▼            ▼
#     ╱────────────────╲   ╱───────────────╲
#    ╱ Print "Even"     ╲ ╱ Print "Odd"     ╲
#    ╲──────────────────╱ ╲─────────────────╱
#                 │            │
#                 └──────┬─────┘
#                        │
#                        ▼
#              ╭──────────────────╮
#              │       STOP       │
#              ╰──────────────────╯

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