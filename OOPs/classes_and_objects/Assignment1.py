class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("deposit amount must be positive.")
            self.balance += amount
            print(f"₹{amount} has been deposited successfully.")
        except ValueError as e:
            print(e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("withdrawal amount must be positive.")
            if amount > self.balance:
                raise ValueError("insufficient funds for withdrawal.")
            self.balance -= amount
            print(f"₹{amount} has been withdrawn successfully.")
        except ValueError as e:
            print(e)

    def check_balance(self):
        print(f"your current balance is: ₹{self.balance}")


if __name__ == "__main__":
    account = BankAccount(1000)
    account.check_balance()
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)  
    account.check_balance()
