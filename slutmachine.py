import os
import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 1000

ROWS = 3
COLS = 3

symbols = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8, }
symbols_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2, }


def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings, winning_lines


def get_all_symbols(cols, rows, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    current_symbols = all_symbols[:]
    for col in range(cols):
        column = []
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])


def deposit():
    while True:
        amount = input("Enter the amount you'd like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter an amount greater than 0")
        else:
            print("Invalid input, enter a number")
    print("Amount deposited to your balance")
    return amount


def balance():
    pass


def get_numberoflines():
    while True:
        lines = input("Enter the number of lines you want: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Invalid number, enter a valid number")
    print("Lines applied")
    return lines


def get_bet():
    while True:
        bet = input("Enter the amount you'd like to bet: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                print("Bet placed")
                break
            else:
                print(
                    f"Bet amount must be between ${MIN_BET} and ${MAX_BET}"
                )
        else:
            print("Invalid input. Enter a valid input")
    return bet


def spin(balance):
    lines = get_numberoflines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"Insufficient balance. "
                f"Your bet is too large | Current balance: ${balance}"
            )
        else:
            print(
                f"Current balance: ${balance} | "
                f"Lines: {lines} | "
                f"Bet per line: ${bet}"
            )
            print(f"Your total bet = ${total_bet}")
            break
    slot = get_all_symbols(COLS, ROWS, symbols)

    print_slot_machine(slot)
    winning, winning_lines = check_winning(slot, lines, bet, symbols_values)
    print(f"you won : $ {winning}")
    print("you won on :", *winning_lines)
    return winning - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        answer = input("Press enter to start the game and Q to quit")
        if answer.lower() == "q":
            break
        else:
            balance += spin(balance)
        print("You left with : ${balance}")


if __name__ == "__main__":
    main()
