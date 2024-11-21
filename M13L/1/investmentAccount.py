from account import Account
import random

class InvestimentAccount(Account):
    def __init__(self, name: str, document: str, accountNumber: str, balance: float, accountType: str):
        super().__init__(name, document, accountNumber, balance, accountType)
        self.__tax = 0

    def getLastBalance(self) -> int:
        return self.__lastBalance
    
    def setLastBalance(self, balance: int) -> None:
        self.__lastBalance = balance

    def investment(self) -> None:
        self.__tax = random.random()
    
    @staticmethod
    def winLose() -> bool:
        return random.random() >= 0.5
    
    def calculateInvestment(self) -> None:
        self.investment()
        print("Investimento feito")
        self.__lastBalance = self.getBalance()
        if self.winLose():
            self.setBalance(self.getBalance()*(1+self.__tax))
            print(f"+R${self.lastResultCalculate():.2f}")
        else:
            self.setBalance(self.getBalance()*(1-self.__tax))
            print(f"-R${self.lastResultCalculate():.2f}")
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
        print(f"Resultado do último investimento: R${self.lastResultCalculate():.2f}")
        print("-"*60)
