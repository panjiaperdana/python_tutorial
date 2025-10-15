import random


def input_values(operand):
    value_1 = random.randint(1, 100)
    value_2 = random.randint(1, 100)
    while True:
        try:
            answer = int(input(f'What is {value_1} {operand} {value_2}? '))
            break  # exit loop if conversion worked
        except ValueError:
            print("Please enter a valid number.")
    match operand:
        case '+':
            finalize(value_1 + value_2, answer)
        case '-':
            finalize(value_1 - value_2, answer)
        case '*':
            finalize(value_1 * value_2, answer)
        case '/':
            finalize(value_1 / value_2, answer)

def finalize(a, b):
    if a == b:
        print('Correct!')
    else:
        print(f'Incorrect!, the correct answer is {a}')

def main():
    print('Welcome to Quiz')
    while True:
        confirm = input('Do you want to play Arithmetic Game (y/n)? ')
        if confirm.lower() != 'y':
            quit()
        else:
            print('Ok, let’s play')

        # validate operand input
        valid_ops = {"+", "-", "*", "/"}
        operand = input("Which one do you choose +, -, *, / ? ").strip()
        if operand in valid_ops:
            input_values(operand)
        else:
            print("Invalid choice. Please enter only +, -, * or /.")

# standard Python entry point
if __name__ == "__main__":
    main()