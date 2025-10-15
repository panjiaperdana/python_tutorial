import random

# 2. Consume by input_values()
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# 1. From main() goes here
def input_values(operand, level):
    # define ranges for each level
    leveling = {
        'easy':   (1, 10),
        'medium': (10, 50),
        'hard':   (50, 100),
    }

    # pick the right range based on level
    min_val, max_val = leveling[level]

    # generate numbers within that range
    value_1, value_2 = (random.randint(min_val, max_val) for _ in range(2))

    # ask the question
    answer = get_number(f"What is {value_1} {operand} {value_2}? ")

    # compute the correct result
    operations = {
        '+': value_1 + value_2,
        '-': value_1 - value_2,
        '*': value_1 * value_2,
        '/': value_1 / value_2,
    }

    finalize(operations[operand], answer)

# 3. Passing Parameter from input_values()
def finalize(correct, user):
    if correct == user:
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is {correct}")

def main():
    print("Welcome to Quiz")
    while True:
        confirm = input("Do you want to play Arithmetic Game (y/n)? ")
        if confirm.lower() != 'y':
            quit()
        print("Ok, let’s play")

        valid_ops = {"+", "-", "*", "/"}
        valid_lev = {"easy", "medium", "hard"}  # normalize to lowercase

        while True:
            operand = input("Which one do you choose +, -, *, / ? ").strip()
            level = input("Which level of game do you choose Easy, Medium, Hard? ").strip().lower()

            if operand in valid_ops and level in valid_lev:
                break

            if operand not in valid_ops:
                print("Invalid operator. Please enter only +, -, * or /.")
            if level not in valid_lev:
                print("Invalid level. Please choose Easy, Medium, or Hard.")

        input_values(operand, level)

if __name__ == "__main__":
    main()