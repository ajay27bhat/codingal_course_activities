# Program to check whether the entered character is an alphabet

# Get input from the user
ch = input("Enter a character: ")

# Check if it is an alphabet
if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
    print(ch, "is an alphabet.")
else:
    print(ch, "is not an alphabet.")