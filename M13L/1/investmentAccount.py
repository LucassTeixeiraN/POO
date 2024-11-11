from account import Account
import random

class InvestimentAccount(Account):
    def __init__(self, name, document, accountNumber, balance, accountType):
        super().__init__(name, document, accountNumber, balance, accountType)
        self.lastInvestment = 0

    def investment(self):
        self.lastInvestment = random.random()
    
    @staticmethod
    def winLose():
        return random.random() >= 0.5
    
    def calculateInvestment(self):
        self.investment()
        if self.winLose():
            self.setBalance(self.getBalance()*(1+self.lastInvestment))
        else:
            self.setBalance(self.getBalance()*(1-self.lastInvestment))

    def showAccount(self):
        print("Informações da conta")
        print(f"Nome: {self.getName()}")
        print(f"Tipo da conta: {self.getAccountType()}")
        print(f"Número da conta: {self.getAccountNumber()}")
        print(f"Documento: {self.getDocument()}")
        print(f"Saldo: R${self.getBalance():.2f}")
        print(f"Resultado do último investimento: R${self.lastInvestment:.2f}")