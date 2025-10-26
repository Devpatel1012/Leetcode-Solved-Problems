# class Bank:
#     def __init__(self, balance):
#         # Create dictionary {1: balance[0], 2: balance[1], ...}
#         self.accounts = {i + 1: bal for i, bal in enumerate(balance)}

#     def transfer(self, account1, account2, money) :
#         # Check validity of both accounts
#         if account1 not in self.accounts or account2 not in self.accounts:
#             return False
#         # Check sufficient balance
#         if self.accounts[account1] < money:
#             return False
#         # Perform transfer
#         self.accounts[account1] -= money
#         self.accounts[account2] += money
#         return True

#     def deposit(self, account, money):
#         # Check valid account
#         if account not in self.accounts:
#             return False
#         # Add money
#         self.accounts[account] += money
#         return True

#     def withdraw(self, account, money):
#         # Check valid account
#         if account not in self.accounts:
#             return False
#         # Check balance
#         if self.accounts[account] < money:
#             return False
#         # Subtract money
#         self.accounts[account] -= money
#         return True

class Bank(object):

    def __init__(self, balance):
        # Store balances in a list
        self.balance = balance

    def is_valid(self, account):
        # Check if account number is valid (1-indexed)
        return 1 <= account <= len(self.balance)

    def transfer(self, account1, account2, money):
        # Validate accounts
        if not self.is_valid(account1) or not self.is_valid(account2):
            return False
        # Check if enough balance exists
        if self.balance[account1 - 1] < money:
            return False
        # Perform transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        # Validate account
        if not self.is_valid(account):
            return False
        # Add money
        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        # Validate account
        if not self.is_valid(account):
            return False
        # Check balance
        if self.balance[account - 1] < money:
            return False
        # Subtract money
        self.balance[account - 1] -= money
        return True
