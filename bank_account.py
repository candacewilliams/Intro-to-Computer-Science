
class BankAccount:
    def __init__ (self, checkings, savings):
        self.checking = checkings
        self.savings = savings

            
    def deposit_into_checking(self, amount):
        self.checking = self.checking + amount
        my_account.print_my_account()

    def deposit_into_savings(self, amount):
        self.savings = self.savings + amount
        my_account.print_my_account()
        
    def withdraw(self, amount):
        if self.checking - amount > 0:
            self.checking = self.checking - amount
            my_account.print_my_account()

        elif self.checking - amount == 0:
            self.checking = self.checking - amount
            my_account.print_my_account()

        elif self.checking == 0:
            self.savings = self.savings - amount
            my_account.print_my_account()

        elif self.checking - amount < 0:
            self.savings = self.savings - (amount - self.checking)
            amount = amount - self.checking
            self.checking = self.checking - amount
            my_account.print_my_account()
            
    def print_my_account(self):
        print('Checking Account Balance :' , self.checking)
        print('Savings Account Balance :' , self.savings)

my_account = BankAccount(20,50)
my_account.print_my_account()
my_account.deposit_into_checking(20)
my_account.deposit_into_savings(10)
my_account.withdraw(80)
my_account.withdraw(50)





