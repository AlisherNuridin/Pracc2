class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
        return self.balance

balance, amount = map(int, input().split())
account = Account(balance)

print(account.withdraw(amount))
