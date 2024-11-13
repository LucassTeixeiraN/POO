from account import Account

class SavingAccount(Account):

    def __init__(self, name: str, document: str, accountNumber: str, balance: float, accountType: str, tax: float):
        super().__init__(name, document, accountNumber, balance, accountType)
        self.__tax = tax

    def calculateGain(self, time: int) -> float:
        return self.getBalance()*((1+self.__tax)**time)
    
    def showAccount(self) -> None:
        print("-"*60)
        print("Informações da conta")
        print(f"Nome: {self.getName()}")
        print(f"Tipo da conta: {self.getAccountType()}")
        print(f"Número da conta: {self.getAccountNumber()}")
        print(f"Documento: {self.getDocument()}")
        print(f"Saldo: R${self.getBalance():.2f}")
        print(f"Taxa aplicada ao mês: {self.__tax}")
        print("-"*60)
