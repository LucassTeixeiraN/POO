from components import Account

class CheckingAccount(Account):
    def __init__(self, name: str, document: str, accountNumber: str, balance: float, accountType: str):
        super().__init__(name, document, accountNumber, balance, accountType)
        self.__oldBalance = 0
        self.__lastTransfer = 0

    def getOldBalance(self) -> float:
        return self.__oldBalance

    def setOldBalance(self, balance: float) -> None:
        self.__oldBalance = balance

    def getLastTransfer(self) -> float:
        return self.__lastTransfer

    def setLastTransfer(self, value: float) -> None:
        self.__lastTransfer = value 

    def transfer(self, value: float) -> None:
        if self.checkBalance(value):
            self.setOldBalance(self.getBalance())
            self.setBalance(self.getBalance() - value)
            self.setLastTransfer(abs(self.calculateTransfer(self.getBalance(), self.getOldBalance())))
            print("-"*60)
        else:
            print("Saldo insuficiente")
            print("-"*60)

    @staticmethod
    def calculateTransfer(value1: float, value2: float) -> float:
        return value1 - value2

    # def showResults(self):
    #     print(f"Tranferência de R${abs(self.calculateTransfer(self.getBalance(), self.getOldBalance())):.2f} feita")

    def showAccount(self) -> None:
        print("-"*60)
        print("Informações da conta")
        print(f"Nome: {self.getName()}")
        print(f"Tipo da conta: {self.getAccountType()}")
        print(f"Número da conta: {self.getAccountNumber()}")
        print(f"Documento: {self.getDocument()}")
        print(f"Saldo: R${self.getBalance():.2f}")
        print("-"*60)