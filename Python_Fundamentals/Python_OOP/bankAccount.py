# The BankAccount class should have a balance. When a new BankAccount instance is created, 
# if an amount is given, the balance of the account should initially be set to that amount; 
# otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. 
# For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. 
# (Hint: when using default values in parameters, the order of parameters matters!)

# The class should also have the following methods:
#     deposit(self, amount) - increases the account balance by the given amount
#     withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
#     display_account_info(self) - print to the console: eg. "Balance: $100"
#     yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

# Create a BankAccount class with the attributes interest rate and balance

class BankAccount():
    
    bankAccounts = []
     
    def __init__(self, interest_rate, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance
        # we wamt to add the instantiated account to the list
        BankAccount.bankAccounts.append(self)
    
    # Add a deposit method to the BankAccount class
    # deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self
    
    # Add a withdraw method to the BankAccount class
    # withdraw(self, amount) - decreases the account balance by the given amount 
    # if there are sufficient funds; if there is not enough money, 
    # print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print ("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
            
    # Add a display_account_info method to the BankAccount class
    def display_account_info(self):
        print(f'Balance: {self.balance}')
        return self
    
    # Add a yield_interest method to the BankAccount class
    # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self
    
# Create 2 accounts
savings = BankAccount(.01)
checking = BankAccount(.01, 100)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
savings.deposit(10).deposit(20).deposit(40).withdraw(600).yield_interest().display_account_info()