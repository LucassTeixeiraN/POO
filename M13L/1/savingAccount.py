from account import Account

class SavingAccount(Account):

    def __init__(self, name, document, accountNumber):
        super().__init__(name, document, accountNumber)