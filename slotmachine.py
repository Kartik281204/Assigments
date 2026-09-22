import random


def spin_row():
    symbols = ['⭐', '🌸', '🍒', '🔔']
    return [random.choice(symbols) for symmbol in range(3)]


def print_row(row):
    print("***************************************")
    print(" | ".join(row))
    print("***************************************")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet*3
        elif row[0] == '🌸':
            return bet*4
        elif row[0] == '🔔':
            return bet*6
        elif row[0] == '⭐':
            return bet*10
    else:
        return 0


def main():
    bank_balance = 1000
    print("Welcome to the slot machine ")
    print("****************************")
    print("Symbols: ⭐ 🌸 🍒 🔔 ")
    print("****************************")
    while bank_balance >= 0:
        bet = input("Place your bet : ")
        if bet == "Exit".lower():
            print("Thank you for playing , Hope we see you again")
            break
        elif not bet.isdigit():
            print("Invalid input , please try again ")
        else:
            bet = int(bet)
            if bet > bank_balance:
                print(
                    "You lack sufficient funds to place a bet please deposit more funds to contiue playing ")
            elif bet == 0:
                print("Bet cannot be placed without funds ")
            else:
                bank_balance -= bet
                print(f"Your new Bank Balance is {bank_balance}")
                print("Bet placed !!")
                row = spin_row()
                print_row(row)
                payout = get_payout(row, bet)
                if payout > 0:
                    payout += bank_balance
                    print(
                        f"Congratulations you won , your balance is now {payout}")
                else:
                    continue


if __name__ == "__main__":
    main()
