class Transaction:
    def __init__(self, amount, date, description):
        self.amount = amount
        self.date = date
        self.description = description

    def __repr__(self):
        return f"Transaction({self.amount}, '{self.date}', '{self.description}')"

    def __add__(self, other):
        if isinstance(other, Transaction):
            return Transaction(self.amount + other.amount, self.date, f"{self.description} + {other.description}")
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Transaction):
            return self.amount == other.amount
        return False

    def __lt__(self, other):
        if isinstance(other, Transaction):
            return self.amount < other.amount
        return False

    def __gt__(self, other):
        if isinstance(other, Transaction):
            return self.amount > other.amount
        return False
