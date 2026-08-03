# Chore Countdown (While Loop)

# List of chores to complete
chores = ["Make your bed", "Feed the pet", "Take out the trash", "Wash the dishes"]

# Set the number of chores remaining and start with the first chore
remaining = len(chores)
index = 0

print("You have", remaining, "chores to finish today!\n")

# Repeat until there are no chores left
while remaining > 0:

    # Ask if the current chore is finished
    answer = input("Did you finish " + chores[index] + "? (yes/no): ")

    # Move to the next chore only if the current one is completed
    if answer == "yes":
        remaining -= 1
        index += 1
        print("Great job!")
    else:
        print("Finish it first!")

    # Display the countdown after each check
    print("Chores remaining:", remaining)
    print()

# Runs after all chores are completed
print("All chores are complete!")