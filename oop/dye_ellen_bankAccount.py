class BankAccount:
    bank_name = "Dojo Bank"
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0): 
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
    def display_account_info(self):
        print(f"Balance: ${round(self.balance,2)}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else: 
            return True
    #NINJA BONUS
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()


account1 = BankAccount(.05,40)
account1.deposit(400).deposit(20).deposit(45.5).withdraw(23).yield_interest().display_account_info()

account2 = BankAccount(int_rate=.01)
account2.deposit(3000).deposit(42).withdraw(100).withdraw(250).withdraw(24.34).withdraw(33.20).yield_interest().display_account_info()

#NINJA BONUS
BankAccount.all_balances()