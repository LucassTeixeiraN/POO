from account import Account

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account: Account):
        self.accounts.append(account)
        account.customer = self 

    def show_accounts(self):
        for account in self.accounts:
            print(account)