from bankAccount import BankAccount
class User: 
    def __init__(self, name):
        self.accounts = [BankAccount(int_rate=0.02)] 
        self.name = name
    def make_deposit(self, amount, acc=0):
        self.accounts[acc].deposit(amount)
        return self

    def display_user_balance(self): 

        for a in self.accounts: 
            print(f"{self.name} -${a.balance:.2f}")

    def make_withdrawal(self, amount, acc=0): 
        self.accounts[acc].withdraw(amount)
        return self

    def transfer_money(self, other, amount, acc=0):

        self.make_withdrawal(amount, acc)
        other.make_deposit(amount,acc)
        return self
    
    def open_account(self, account = BankAccount()):
        self.accounts.append(account)
        return self

if __name__ == "__main__":
    user1 = User("Radek")
    user2 = User("Piotrek")
    user3 = User("Benek")

    user1.open_account().make_deposit(5, 1)
    user1.make_deposit(10).make_deposit(20).make_deposit(30).make_withdrawal(20).display_user_balance()

    user2.make_deposit(5).make_deposit(7).make_withdrawal(1).make_withdrawal(1).display_user_balance()

    user1.transfer_money(user3, 10).display_user_balance()
    user3.display_user_balance()
