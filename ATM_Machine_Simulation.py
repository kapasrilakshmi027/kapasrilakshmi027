pin_number = 70911
balance = 10000000
attempts = 3

print("----- Welcome to ATM Machine -----")

while attempts > 0:
    pin_entered = int(input("Enter your PIN number: "))

    if pin_entered == pin_number:
        print("\n PIN verified successfully")

       
        while True:
            print("\n----- ATM MENU -----")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                print(f"Your Balance: Rs/- {balance}")

            elif choice == 2:
                deposit = int(input("Enter deposit amount: "))
                balance += deposit
                print(f"Rs/- {deposit} deposited successfully")

            elif choice == 3:
                withdraw = int(input("Enter withdraw amount: "))
                if withdraw <= balance:
                    balance -= withdraw
                    print(f"Rs/- {withdraw} withdrawn successfully")
                else:
                    print("Insufficient Balance")

            elif choice == 4:
                print("Thank you for visiting our ATM.")
                break   

            else:
                print("Invalid choice")

        break  

    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts left: {attempts}")
    if attempts == 0:
          print("Card Blocked. Too many wrong attempts.")


