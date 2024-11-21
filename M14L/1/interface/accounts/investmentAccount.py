from components import Account, Application
import random

class InvestmentAccount(Account, Application):
    def __init__(self, name: str, document: str, accountNumber: str, balance: float, accountType: str):
        super().__init__(name, document, accountNumber, balance, accountType)
        self.__tax = 0

    def getTax(self) -> float:
        return self.__tax
    
    def setTax(self, tax) -> None:
        self.__tax = tax

    def investment(self) -> None:
        self.setTax(random.random())
    
    @staticmethod
    def winLose() -> bool:
        return random.random() >= 0.5
    
    def calculateGain(self, time: int) -> float:
        self.investment()
        if self.winLose():
            return self.getBalance() * ((1 + self.getTax())**time)
        return self.getBalance() * ((1 - self.getTax())**time)
    
    def showResults(self, gain: float) -> None:
        print(f"Resultado do investimento de R${(gain - self.getBalance()):.2f}")

    def InvestmentApplication(self):
        gain = self.calculateGain(1)
        self.showResults(gain)
        self.setBalance(gain)    

    def showAccount(self) -> None:
        print("-"*60)
        print("Informações da conta")
        print(f"Nome: {self.getName()}")
        print(f"Tipo da conta: {self.getAccountType()}")
        print(f"Número da conta: {self.getAccountNumber()}")
        print(f"Documento: {self.getDocument()}")
        print(f"Saldo: R${self.getBalance():.2f}")
        print("-"*60)