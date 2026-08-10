name = input("Enter your name: ")

print("Hello", name)

choice = input("Do you want to exit? (yes/no): ")

if choice.lower() == "yes":
    print("Program terminated.")
    exit()

print("Program continues...")