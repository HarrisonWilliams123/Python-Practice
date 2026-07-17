class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Invalid balance. Must be non-negative.")
        else:
            self.__balance = amount

    def deposit(self, amount):
        self.balance = self.__balance + amount

account = BankAccount(1000)
print("Current balance:", account.balance)

account.deposit(500)
print("Current balance:", account.balance)

account.balance = -200
