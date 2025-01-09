# program to : Write a robust ATM transaction simulator that includes options for
# checking balances, depositing, withdrawing money, and exiting.
# Handle invalid inputs and edge cases

def atm_simulator():
    balance = 1000.0

    def check_balance():
        print(f"your current balance is: ₹{balance:.2f}")

    def deposit_money():
        try:
            amount = float(input("enter the amount to deposit: "))
            if amount <= 0:
                print("please enter a positive amount.")
            else:
                nonlocal balance
                balance += amount
                # .2f for upto the two decimal places
                print(f"₹{amount:.2f} has been successfully deposited.")
                check_balance()
        except ValueError:
            print("invalid input! please enter a valid number.")

    def withdraw_money():
        try:
            amount = float(input("enter the amount to withdraw: "))
            if amount <= 0:
                print("please enter a positive amount.")
            elif amount > balance:
                print("insufficient balance! transaction declined.")
            else:
                nonlocal balance
                balance -= amount
                print(f"₹{amount:.2f} has been successfully withdrawn.")
                check_balance()
        except ValueError:
            print("invalid input! please enter a valid number.")

    while True:
        print("\natm menu:")
        print("1. check balance")
        print("2. deposit money")
        print("3. withdraw money")
        print("4. exit")
        choice = input("please choose an option (1-4): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            print("thank you! have a nice day!")
            break
        else:
            print("invalid choice! please select a valid option from 1 to 4.")

if __name__ == "__main__":
    atm_simulator()
