# Program to:xtend the  BankAccount  class to create  SavingsAccount  and
# CheckingAccount  subclasses. Add unique features such as
# interest calculation, transaction limits, loan eligibility (based on
# transaction amounts), reward programs

class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amt):
        try:
            if amt <= 0:
                raise ValueError("deposit amount must be positive.")
            self.balance += amt
            print(f"₹{amt} deposited successfully.")
        except ValueError as e:
            print(e)

    def withdraw(self, amt):
        try:
            if amt <= 0:
                raise ValueError("withdrawal amount must be positive.")
            if amt > self.balance:
                raise ValueError("insufficient funds.")
            self.balance -= amt
            print(f"₹{amt} withdrawn successfully.")
        except ValueError as e:
            print(e)

    def check_balance(self):
        print(f"current balance: ₹{self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, holder, balance=0, rate=0.03):
        super().__init__(holder, balance)
        self.rate = rate

    def calc_interest(self):
        interest = self.balance * self.rate
        self.balance += interest
        print(f"₹{interest:.2f} interest added.")

    def check_balance(self):
        super().check_balance()
        print(f"interest rate: {self.rate * 100}%")

class CheckingAccount(BankAccount):
    def __init__(self, holder, balance=0, limit=50000):
        super().__init__(holder, balance)
        self.limit = limit
        self.points = 0

    def withdraw(self, amt):
        try:
            if amt > self.limit:
                raise ValueError(f"exceeds limit of ₹{self.limit}.")
            super().withdraw(amt)
            self.points += int(amt // 100)  # 1 point per ₹100
            print(f"reward points: {self.points}")
        except ValueError as e:
            print(e)

    def loan_eligibility(self):
        if self.balance > 10000:
            print("eligible for loan.")
        else:
            print("not eligible for loan.")

    def check_balance(self):
        super().check_balance()
        print(f"limit: ₹{self.limit}")
        print(f"reward points: {self.points}")

# Example usage:
if __name__ == "__main__":
    s_acc = SavingsAccount("John", 5000)
    s_acc.check_balance()
    s_acc.deposit(2000)
    s_acc.calc_interest()
    s_acc.check_balance()

    c_acc = CheckingAccount("Jane", 15000)
    c_acc.check_balance()
    c_acc.deposit(3000)
    c_acc.withdraw(10000)
    c_acc.loan_eligibility()
    c_acc.check_balance()
