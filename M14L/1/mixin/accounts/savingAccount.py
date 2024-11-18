from components import Account, GainMixIn

class SavingAccount(Account, GainMixIn):

    def __init__(self, name: str, document: str, accountNumber: str, balance: float, accountType: str, tax):
        super().__init__(name, document, accountNumber, balance, accountType)
        self.tax = tax

    def gain(self):
        print(self.calculateGain())
        