class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        self.balance-=amount

        return self
    def yield_interest(self):
        self.balance+=self.balance*self.int_rate
        return self
    def display_account_info(self):

        print (f"balance: ${self.balance:.2f}")
        return self




account1 = BankAccount(balance=10).deposit(3).deposit(2).deposit(1).withdraw(6).yield_interest().display_account_info()
account2 = BankAccount().deposit(100.25).deposit(50.0).withdraw(10).withdraw(10).withdraw(5).withdraw(5).yield_interest().display_account_info()
