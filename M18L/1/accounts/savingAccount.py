from components import Account, GainOperations

class SavingAccount(Account, GainOperations):

    def __init__(self, name: str, document: str, accountNumber: str, balance: float, accountType: str, tax: float):
        super().__init__(name, document, accountNumber, balance, accountType)
        self.__tax = tax
        self.__gainOperations = GainOperations()

    def getTax(self) -> float:
        return self.__tax

    def estimateGain(self, time: int) -> None:
        gain = self.__gainOperations.calculateGain(self.getBalance(), self.getTax(), time)
        self.showResults("Rendimento estimado", self.__gainOperations.calculateDifference(gain, self.getBalance()))

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


        