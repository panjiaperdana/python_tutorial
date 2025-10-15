import random


# Centralized configuration for levels
LEVELS = {
    'easy':   {'range': (1, 5),  'attempts': 3},
    'medium': {'range': (1, 10), 'attempts': 5},
    'hard':   {'range': (1, 15), 'attempts': 5},
}

def guess_start(level: str):
    """Start the guessing game for a given difficulty level."""
    min_val, max_val = LEVELS[level]['range']
    guess_num = random.randint(min_val, max_val)
    guess_count = LEVELS[level]['attempts']
    play_round(guess_num, guess_count, min_val, max_val)

def play_round(guess_num: int, guess_count: int, min_val: int, max_val: int):
    """Run one round of guessing attempts."""
    for i in range(1, guess_count + 1):
        while True:
            try:
                answer_num = int(input(
                    f'Attempt {i}/{guess_count} => Guess a number ({min_val} to {max_val}): '
                ))

                # ✅ validate range
                if not (min_val <= answer_num <= max_val):
                    print(f"Please enter a number between {min_val} and {max_val}.")
                    continue  # retry without consuming attempt

                # ✅ check correctness
                if answer_num == guess_num:
                    print("🎉 Congratulations! You are the Winner")
                    return
                else:
                    print(f"❌ Wrong answer {answer_num}, try again!")
                break  # valid input, move to next attempt

            except ValueError:
                print("Please enter a valid number.")

    print(f"Out of attempts! The correct number was {guess_num}.")

def main():
    print("Welcome to the Guess Game!")
    while True:
        confirm = input("Would you like to play Guess Number Game (y/n)? ").strip().lower()
        if confirm != "y":
            print("Goodbye!")
            break

        print("Let's get started!")

        # ✅ validate difficulty choice
        while True:
            level = input("Choose difficulty (easy, medium, hard): ").strip().lower()
            if level in LEVELS:
                break
            print("Invalid difficulty! Please try again.")

        guess_start(level)

if __name__ == "__main__":
    main()