# Age Eligibility Check using Nested If-Else

age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18:
    if citizen.lower() == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible because you are not a citizen.")
else:
    if age >= 16:
        print("You are not eligible to vote yet. Wait until you turn 18.")
    else:
        print("You are too young to vote.")