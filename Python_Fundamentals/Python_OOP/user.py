class User:
    
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    # have this method increase the user's balance by the amount specified
    def make_deposit(self, amount):
        self.balance += amount
    
    # have this method decrease the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.balance -= amount
    
    # have this method print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        print(f'Name: {self.name} | Balance: ${self.balance}')
    
    # have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        self.other_user += amount
        
    # BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
    def transfer_money(self,other_user,amount):
        self.balance -= amount
        other_user.balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
    
# Create 3 instances of the User class
user1 = User("James")
user2 = User("Kaitlyn")
user3 = User("Lorelei")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
user1.make_deposit(100)
user1.make_deposit(100)
user1.make_deposit(100)
user1.make_withdrawal(100)
user1.display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
user2.make_deposit(100)
user2.make_deposit(100)
user2.make_withdrawal(100)
user2.make_withdrawal(100)
user2.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
user3.make_deposit(500)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.display_user_balance()

user1.transfer_money(user2,1000)