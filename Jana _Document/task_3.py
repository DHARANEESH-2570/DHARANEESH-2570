import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def display_scores(user_score, computer_score):
    print(f"\nScores:")
    print(f"User: {user_score}")
    print(f"Computer: {computer_score}")

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions:")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to end the game.\n")

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice == "exit":
            print("Thank you for playing!")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        display_scores(user_score, computer_score)

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    play_game()
