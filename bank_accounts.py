# Creating a OOP Project for Bank Accounts

class BankException(Exception): # exception pass krne se  
    pass

class BankAccount:
    def __init__(self, account_name, balance):
        self.account_holder = account_name
        self.balance = balance
        print(f"\nAccount created for '{self.account_holder}'\nBalance = {self.balance:.2f} Rupees")
    
    def get_balance(self):
        print(f"\nCurrent balance for {self.account_holder} is {self.balance:.2f} Rupees")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"\nAmount Deposited Sucessfully!\nAccount Balance for '{self.account_holder}'= {self.balance:.2f} Rupees")

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BankException(
                f"\nInsufficient balance! You have only {self.balance:.2f} Rupees in your account."
            )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BankException as error:
            print(f'\nWithdraw interrupted: {error}')

    # when you want to transfer amount from one account to another

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer.. 🚀')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! ✅\n\n**********')
        except BankException as error: 
            print(f'\nTransfer interrupted. ❌ {error}')

# This is a Subclass of bankaccount that adds interest to the deposit amount.
# It overrides the deposit method to add 5% interest on the deposited amount.
# ye ek esa account banata hai jisme deposit amount par 5% interest milta hai.

class InterestRewardsAcct(BankAccount): 
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()

# Savings Account bnaya jo InterestRemardsAcct ka subclass hai. jisme withdrawl par 5 rupees ka fee lagta hai.

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, account_name, balance): 
        super().__init__(account_name, balance)
        self.fee = 5

    def withdraw(self, amount): 
        try: 
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee) 
            print("\nWithdraw completed.")
            self.get_balance() 
        except BankException as error: 
            print(f'\nWithdraw interrupted: {error}')