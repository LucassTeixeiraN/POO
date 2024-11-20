from components import Account, GainMixIn
import random

class InvestmentAccount(Account, GainMixIn):
    def __init__(self, name: str, document: str, accountNumber: str, balance: float, accountType: str):
        super().__init__(name, document, accountNumber, balance, accountType)
        self.__lastBalance = 0
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
    
    def calculateInvestment(self) -> None:
        self.investment()
        print("Investimento feito")
        gain = self.calculateGain(self.getBalance(), self.getTax(), 1)
        self.transactionLog(gain - self.getBalance(), "Resultado de investimento")
        self.setBalance(gain)
        print("-"*60)

    def lastResultCalculate(self) -> int:
        return self.getBalance() - self.getLastBalance() 

    def showAccount(self) -> None:
        print("-"*60)
        print("Informações da conta")
        print(f"Nome: {self.getName()}")
        print(f"Tipo da conta: {self.getAccountType()}")
        print(f"Número da conta: {self.getAccountNumber()}")
        print(f"Documento: {self.getDocument()}")
        print(f"Saldo: R${self.getBalance():.2f}")
        print("-"*60)