import random

# Emoji mapping for display
OPTIONS = {
    'rock': "🪨",
    'scissors': "✂",
    'paper': "📃"
}

def is_user_winner(user, comp):
    """Return True if user beats computer."""
    return (
        (user == 'rock' and comp == 'scissors') or
        (user == 'scissors' and comp == 'paper') or
        (user == 'paper' and comp == 'rock')
    )

def get_valid_round_number():
    """Prompt user for a valid round number."""
    while True:
        try:
            round_num = int(input("How many rounds would you like to play? ").strip())
            if round_num > 0:
                return round_num
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

def get_user_choice():
    """Prompt user for a valid move."""
    while True:
        choice = input("Choose rock, scissors, or paper: ").strip().lower()
        if choice in OPTIONS:
            return choice
        print("Invalid choice, please try again.")

def fight(round_num):
    user_win = 0
    comp_win = 0
    round_index = 0

    while round_index < round_num:
        print(f"\n🎮 Round {round_index + 1} start!")
        user_pick = get_user_choice()
        comp_pick = random.choice(list(OPTIONS.keys()))

        print(f"🧑 You chose {OPTIONS[user_pick]} | 🤖 Computer chose {OPTIONS[comp_pick]}")

        if user_pick == comp_pick:
            print("⚖️ It's a draw! Replay this round.")
            continue

        if is_user_winner(user_pick, comp_pick):
            user_win += 1
            print("✅ You won this round!")
        else:
            comp_win += 1
            print("❌ You lost this round!")

        print(f"Score: 🧑 {user_win} — 🤖 {comp_win}")
        round_index += 1

    print("\n🏁 Game Over!")
    print(f"Final Score: 🧑 User {user_win} — {comp_win} Computer 🤖")

def main():
    print("🎉 Welcome to the Rock 🪨, Scissors ✂, Paper 📃 Game!")
    while True:
        confirm = input("Do you want to play (y/n)? ").strip().lower()
        if confirm != 'y':
            print("👋 Goodbye!")
            break

        print("Let's get started!")
        round_num = get_valid_round_number()
        fight(round_num)

if __name__ == '__main__':
    main()