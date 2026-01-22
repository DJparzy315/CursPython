class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # atribut privat

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Fonduri insuficiente")

    def get_balance(self):
        return self._balance


# exemplu de utilizare
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())
