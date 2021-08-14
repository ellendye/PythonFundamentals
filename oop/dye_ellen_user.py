# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount

#create an instance that makes 3 deposits and 1 withdrawal then display balance
ellen = User("Ellen Dye", "ellen.m.dye@gmail.com")
ellen.make_deposit(5000)
ellen.make_deposit(10.50)
ellen.make_deposit(55)
ellen.make_withdrawal(150.75)
ellen.display_user_balance()

#create an instance that makes 2 deposits and 2 withdrawals then display balance
brad = User("Brad Thompson", "brad.thompson123@gmail.com")
brad.make_deposit(500)
brad.make_deposit(75)
brad.make_withdrawal(50)
brad.make_withdrawal(100)
brad.display_user_balance()

#create an instance that makes 1 deposit and 3 withdrawals then display balance
john = User("John Doe", "john.doe@aol.com")
john.make_deposit(300)
john.make_withdrawal(250)
john.make_withdrawal(40)
john.make_withdrawal(15)
john.display_user_balance()

#BONUS: add a transfer_money method and have the first user transfer mony to the third user and then print both balances
ellen.transfer_money(john, 100)
ellen.display_user_balance()
john.display_user_balance()