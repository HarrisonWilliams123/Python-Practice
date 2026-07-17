class BankAccount:
    
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Balance after deposit: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print(f"Insufficient funds. Current balance: {self.balance}")
        else:
            self.balance = self.balance - amount
            print(f"Balance after withdrawal: {self.balance}")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)