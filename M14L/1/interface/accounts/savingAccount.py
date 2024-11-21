from components import Account, Application

class SavingAccount(Account, Application):

    def __init__(self, name: str, document: str, accountNumber: str, balance: float, accountType: str, tax: float):
        super().__init__(name, document, accountNumber, balance, accountType)
        self.__tax = tax

    def getTax(self) -> float:
        return self.__tax
    
    def calculateGain(self, time: int) -> float:
         return self.getBalance() * ((1 + self.getTax())**time)
    
    def showResults(self, gain: float) -> None:
        print(f"Ganho estimado de R${(gain - self.getBalance()):.2f}")

    def savingApplication(self, time: int):
        gain = self.calculateGain(time)
        self.showResults(gain)

    def showAccount(self) -> None:
        print("-"*60)
        print("Informações da conta")
        print(f"Nome: {self.getName()}")
        print(f"Tipo da conta: {self.getAccountType()}")
        print(f"Número da conta: {self.getAccountNumber()}")
        print(f"Documento: {self.getDocument()}")
        print(f"Saldo: R${self.getBalance():.2f}")
        print(f"Taxa aplicada ao mês: {self.getTax()}")
        print("-"*60)


        