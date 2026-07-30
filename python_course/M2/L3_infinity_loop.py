# Infinite Loop with Break

while True:
    name = input("Enter your name (or type 'exit' to stop): ")

    if name.lower() == "exit":
        print("Loop terminated.")
        break

    print("Hello,", name)