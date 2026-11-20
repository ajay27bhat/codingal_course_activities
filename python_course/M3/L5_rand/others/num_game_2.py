import random

# Generate a random number from 0 to 9
number = str(random.randint(0, 9))

print("Guess the number between 0 and 9!")

# Keep asking until the user guesses correctly
while True:
    guess = input("Enter your guess: ")

    if guess == number:
        print("You win the game!")
        print("The number was", number)
        break
    else:
        print("Wrong guess! Try again.")