import random

# Choices for the game
choices = ["rock", "paper", "scissors"]

while True:
    # Get the user's choice
    user = input("Enter rock, paper, or scissors: ").lower()

    # Get the computer's choice
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    # Check who wins
    if user == computer:
        print("It's a tie!")

    elif user == "rock" and computer == "scissors":
        print("Rock smashes scissors! You win!")

    elif user == "paper" and computer == "rock":
        print("Paper covers rock! You win!")

    elif user == "scissors" and computer == "paper":
        print("Scissors cuts paper! You win!")

    elif user in choices:
        print("You lose!")

    else:
        print("Invalid choice!")

    # Ask to play again
    play_again = input("Play again? (y/n): ")

    if play_again != "y":
        break




    #  if user == computer:
    #     print("It's a tie!")

    # elif (user == "rock" and computer == "scissors") or \
    #      (user == "paper" and computer == "rock") or \
    #      (user == "scissors" and computer == "paper"):
    #     print("You win!")

    # elif user in choices:
    #     print("You lose!")

    # else:
    #     print("Invalid choice!")

    # play_again = input("Play again? (y/n): ")

    # if play_again != "y":
    #     break

print("Thanks for playing!")







