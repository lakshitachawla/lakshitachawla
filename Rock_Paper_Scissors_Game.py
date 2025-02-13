import random

def play_game():
    print("\n🎮 Welcome to the Rock, Paper, Scissors Game! 🎮")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.\n")
    
    options = ["rock", "paper", "scissors"]
    scores = {"Player": 0, "Computer": 0, "Ties": 0}
    
    while True:
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
        
        # Validating input
        if user_choice not in options:
            print("❌ Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(options)
        
        # Display choices with emojis
        choices_emojis = {
            "rock": "🪨",
            "paper": "📄",
            "scissors": "✂️"
        }
        
        print(f"\nYou chose: {choices_emojis[user_choice]} ({user_choice.capitalize()})")
        print(f"Computer chose: {choices_emojis[computer_choice]} ({computer_choice.capitalize()})")
        
        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie! 🤝"
            scores["Ties"] += 1
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win! 🎉"
            scores["Player"] += 1
        else:
            result = "Computer wins! 💻"
            scores["Computer"] += 1
        
        # Display the result
        print(result)
        print(f"🏆 Scores ==> You: {scores['Player']} | Computer: {scores['Computer']} | Ties: {scores['Ties']}\n")
        print("-" * 50)
        ans = input("Do you want to play again? (Y/N): ").lower()
        if ans == 'n':
            print("\nThanks for playing!😊\nFinal scores:")
            print(f"🏆 You: {scores['Player']}")
            print(f"💻 Computer: {scores['Computer']}")
            print(f"🤝 Ties: {scores['Ties']}")
            break

# Start the game
play_game()
