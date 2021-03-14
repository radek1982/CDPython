class User: 
    def __init__(self, name): 
        self.name = name
        self.balance = 0
    def make_deposit(self, amount):
        self.balance+=amount

    def display_user_balance(self): 
        print(f"{self.name} - ${self.balance:.2f}")

    def make_withdrawal(self, amount): 
        self.balance-=amount

    def transfer_money(self, other, amount):

        self.make_withdrawal(amount)
        other.make_deposit(amount)
        

user1 = User("Radek")
user2 = User("Piotrek")
user3 = User("Benek")

user1.make_deposit(10)
user1.make_deposit(20)
user1.make_deposit(30)

user1.make_withdrawal(20)

user1.display_user_balance()

user2.make_deposit(5)
user2.make_deposit(7)
user2.make_withdrawal(1)
user2.make_withdrawal(1)

user2.display_user_balance()

user1.transfer_money(user3, 10)
user1.display_user_balance()
user3.display_user_balance()