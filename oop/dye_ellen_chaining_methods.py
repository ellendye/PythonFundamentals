#USER ASSIGNMENT BUT WITH CHAINED METHODS
class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

#create an instance that makes 3 deposits and 1 withdrawal then display balance
ellen = User("Ellen Dye", "ellen.m.dye@gmail.com")
ellen.make_deposit(5000).make_deposit(10.50).make_deposit(55).make_withdrawal(150.75).display_user_balance()

#create an instance that makes 2 deposits and 2 withdrawals then display balance
brad = User("Brad Thompson", "brad.thompson123@gmail.com")
brad.make_deposit(500).make_deposit(75).make_withdrawal(50).make_withdrawal(100).display_user_balance()

#create an instance that makes 1 deposit and 3 withdrawals then display balance
john = User("John Doe", "john.doe@aol.com")
john.make_deposit(300).make_withdrawal(250).make_withdrawal(40).make_withdrawal(15).display_user_balance()

#BONUS: add a transfer_money method and have the first user transfer mony to the third user and then print both balances
ellen.transfer_money(john, 100).display_user_balance()
john.display_user_balance()