from components import Account, LiquidValueAcc
import random

class InvestmentAccount(Account, LiquidValueAcc):
    def __init__(self, name: str, document: str, accountNumber: str, balance: float, accountType: str):
        super().__init__(name, document, accountNumber, balance, accountType)
        self.__tax = 0

    def getTax(self) -> float:
        return self.__tax
    
    def setTax(self, tax) -> None:
        self.__tax = tax

    def investment(self) -> None:
        if self.winLose:
            self.setTax(random.random())
        else:
            self.setTax(random.random()*(-1))

    
    @staticmethod
    def winLose() -> bool:
        return random.random() >= 0.5
    

    def showAccount(self) -> None:
        print("-"*60)
        print("Informações da conta")
        print(f"Nome: {self.getName()}")
        print(f"Tipo da conta: {self.getAccountType()}")
        print(f"Número da conta: {self.getAccountNumber()}")
        print(f"Documento: {self.getDocument()}")
        print(f"Saldo: R${self.getBalance():.2f}")
        print("-"*60)