# Number Guessing Game

secret = 27
attempts = 0
max_attempts = 5

print("🎮 Welcome to the Number Guessing Game!")
print("Guess the secret number between 1 and 50.")
print("You have 5 attempts.\n")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret:
        print("🎉 Congratulations! You guessed the secret number!")
        break

    # Hint system
    difference = abs(secret - guess)

    if difference > 20:
        print("🧊 Ice Cold!")
    elif difference > 10:
        print("🥶 Cold!")
    elif difference > 5:
        print("🌡️ Warm!")
    else:
        print("🔥 Hot!")

    # Show remaining hearts
    hearts_left = max_attempts - attempts
    print("Remaining lives: ", end="")
    for i in range(hearts_left):
        print("❤️", end="")
    print("\n")

# Loss message
if attempts == max_attempts and guess != secret:
    print(f"😢 Game Over! The secret number was {secret}.")