import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock-Paper-Scissors ---")
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()

        if user_choice == "quit":
            print("\nFinal Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = get_winner(user_choice, computer_choice)
        print(result)

        # this is a small function for counting the score
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

play_game()