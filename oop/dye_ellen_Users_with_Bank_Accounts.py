class User:
    def __init__(self, name, email, type):
        self.name = name
        self.email = email
        self.account = {}
        self.type = type
        self.account[self.type] = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self,amount,type):
        self.account[type].deposit(amount)
        return self
    def make_withdrawal(self,amount,type):
        self.account[type].withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name}")
        print("ACCOUNTS")
        for account in self.account:
            print(f'{account}: ${round(self.account[account].balance, 2)}')
        print('\n')
        return self
    def transfer_money(self,other_user,amount,mytype,yourtype):
        self.account[mytype].balance -= amount
        other_user.account[yourtype].balance += amount
        return self
    def add_account(self, type):
        self.account[type] = BankAccount(int_rate=0.02, balance=0)
        return self


class BankAccount:
    bank_name = "Dojo Bank"
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=.02, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else: 
            return True
    def display_account_info(self):
        print(f"Balance: ${round(self.balance,2)}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()


# create an instance that makes 3 deposits and 1 withdrawal then display balance
ellen = User("Ellen Dye", "ellen.m.dye@gmail.com", 'Checking')
ellen.make_deposit(1000,'Checking')


#create an instance that makes 2 deposits and 2 withdrawals then display balance
brad = User("Brad Thompson", "brad.thompson123@gmail.com", 'Checking')
brad.add_account('Savings').add_account('Retirement')
brad.make_deposit(500,'Savings').make_deposit(1300,'Checking').make_deposit(75,'Retirement').make_withdrawal(50,'Checking').make_withdrawal(100,'Checking').display_user_balance()

#create an instance that makes 1 deposit and 3 withdrawals then display balance
john = User("John Doe", "john.doe@aol.com", 'Checking')
john.make_deposit(300,'Checking').make_withdrawal(40,'Checking').make_withdrawal(15,'Checking').display_user_balance()

#BONUS: add a transfer_money method and have the first user transfer mony to the third user and then print both balances
ellen.transfer_money(john, 100,'Checking','Checking').display_user_balance()
john.display_user_balance()


ellen.add_account('Savings').make_deposit(1000,'Savings').make_deposit(500,'Checking').display_user_balance()

BankAccount.all_balances()