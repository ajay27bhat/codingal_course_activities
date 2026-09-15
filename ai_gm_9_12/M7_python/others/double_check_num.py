# Program to check a double number

number = input("Enter a number: ")

if len(number) == 2 and number[0] == number[1]:
    print("It is a double number.")
else:
    print("It is not a double number.")