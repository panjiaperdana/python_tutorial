import tkinter as tk
import random

from scipy.constants import value

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS, COLS = 3, 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:   # break on mismatch
                break
        else:  # this else belongs to the for-loop, runs only if no break
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# GUI Logic
class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine 🎰")
        self.balance = 0

        # Deposit
        tk.Label(root, text='Deposit:').grid(row=0, column=0)
        self.deposit_entry = tk.Entry(root)
        self.deposit_entry.grid(row=0, column=1)
        tk.Button(root, text='Set Balance', command=self.set_balance).grid(row=0, column=2)

        # Bet & Lines
        tk.Label(root, text='Bet per line:').grid(row=1, column=0)
        self.bet_entry = tk.Entry(root)
        self.bet_entry.grid(row=1, column=1)

        tk.Label(root, text='Lines (1-3):').grid(row=2, column=0)
        self.line_entry = tk.Entry(root)
        self.line_entry.grid(row=3, column=1)

        # Spin Button
        tk.Button(root, text='Spin', command=self.spin).grid(row=3, column=0, columnspan=3)

        # Balance & Result
        self.balance_label = tk.Label(root, text='Balance: $0')
        self.balance_label.grid(row=4, column=0, columnspan=3)

        self.result_label = tk.Label(root, text='')
        self.result_label.grid(row=5, column=0, columnspan=3)

        # Slot Grid
        self.slot_labels = [[tk.Label(root, text=' ', width=5, height=2, relief='ridge') for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                self.slot_labels[r][c].grid(row=6+r, column=c)

    def set_balance(self):
        try:
            self.balance = int(self.deposit_entry.get())
            self.update_balance()
        except ValueError:
            self.result_lable.config(text='Balance must be a number.')

    def update_balance(self):
        self.balance_label.config(text=f'Balance: ${self.balance}')

    def spin(self):
        try:
            bet = int(self.bet_entry.get())
            lines = int(self.line_entry.get())
        except ValueError:
            self.result_label.config(text="Enter valid bet and lines.")
            return

        if not (1 <= lines <= ROWS):
            self.result_label.config(text=f"Lines must be between 1 and {ROWS}.")
            return

        total_bet = bet * lines
        if total_bet > self.balance:
            self.result_label.config(text='Not enough balance')
            return

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        for r in range(ROWS):
            for c in range(COLS):
                self.slot_labels[r][c].config(text=slots[c][r])

        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        self.balance += winnings - total_bet
        self.update_balance()
        self.result_label.config(text=f"Won ${winnings} on lines {winning_lines}" if winnings > 0 else "No win.")

# Run the App
root = tk.Tk()
app = SlotMachineApp(root)
root.mainloop()