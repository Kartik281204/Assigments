def deposits():
    amount = float(input("Enter the amount youd like deposit : "))
    if amount < 0:
        print("Invalid amount please enter again : ")
    else:
        print("---------------------------------")
        print(
            f"Your deposit of Rs {amount:.2f} has been successfully deposioted into your account")
        return amount


def balance(balance_):
    print(f"Your balance is Rs.{balance_:.2f} ")


def withdraw(balance_):
    amount = float(input("Enter the amount youd like to withdraw : "))
    if amount > balance_:
        print("Invalid amount please ")
        return 0
    else:
        print("---------------------------------")
        print(
            f"Your withdrawal of Rs {amount:.2f} has been successfully processed")
        return amount


def main():
    is_running = True
    balance_ = 20000
    while is_running:
        print("Welcome to the banking system",
              "A : Show my balance",
              "B : Deposit money",
              "C : Withdraw money",
              "D : Exit", sep="\n"
              )
        option = input("Enter what option you want to choose:")
        match option:
            case "A":
                balance()
            case "B":
                balance_ += deposits(balance_)
            case "C":
                balance_ -= withdraw(balance_)
            case "D":
                is_running = False
            case _:
                print("Invalid option ,, please try again")


print("Thank you have a nice")
if __name__ == "__main__":
    main()
