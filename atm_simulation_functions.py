def check_balance(balance):
    print(f"\nYour Current Balance: Rs/-{balance}")
    return balance


def deposit_money(balance):
    deposit = float(input("Enter Your Deposit Amount: Rs/- "))
    if deposit > 0:
        balance += deposit
        print(f"Rs/-{deposit} Deposited Successfully!")
    else:
        print("Invalid deposit amount.")
    return balance


def withdraw_money(balance):
    withdraw = float(input("Enter Withdrawal Amount: Rs/- "))
    if withdraw<= balance and withdraw >0:
        balance -= withdraw
        print(f"Rs/-{withdraw} Withdrawn Successfully!")
    else:
        print("Insufficient balance or invalid amount.")
    return balance


def atm_menu():
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")


def atm_machine():
    balance = 100000
    pin = 70911
    attempts = 3

    print("\n----- Welcome to ATM Machine -----")

    while attempts > 0:
        entered_pin = int(input("Enter your PIN: "))

        if entered_pin == pin:
            print("PIN Verified Successfully")

            while True:
                atm_menu()
                choice = input("Enter Your Choice (1-4): ")

                if choice == "1":
                    balance = check_balance(balance)

                elif choice == "2":
                    balance = deposit_money(balance)

                elif choice == "3":
                    balance = withdraw_money(balance)

                elif choice == "4":
                    print("\nThank You.Visit Again!")
                    return

                else:
                    print("Invalid Choice. Please select 1-4.")

        else:
            attempts -= 1
            print(f"Invalid PIN. Attempts left:{attempts}")

    print("\nCard Blocked. Please contact your bank.")


atm_machine()
