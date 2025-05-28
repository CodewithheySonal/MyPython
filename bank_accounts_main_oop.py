# OOPS project to take input from bank_account file

from bank_accounts import *

# For taking input from bank_accounts.py
Sonal = BankAccount("Sonal", 1000)
Radha = BankAccount("Radha", 2000)

# Now to check bank account balance
Sonal.get_balance()
Radha.get_balance()

# Now to deposit some amount
Sonal.deposit(5000)
Radha.deposit(2000)

# withdrawl 
Sonal.withdraw(60)

# Transfer
Sonal.transfer(100, Radha)

# Transfer with Interest Rewards Account
Manoj = InterestRewardsAcct("Manoj", 5000)
Manoj.get_balance()
Manoj.deposit(1000)

# Transfer from savings account
Sagar = SavingsAcct("Sagar", 10000)
Sagar.get_balance()
Sagar.deposit(200)

Sagar.transfer(100000, Manoj)
Sagar.transfer(1000, Sonal)
