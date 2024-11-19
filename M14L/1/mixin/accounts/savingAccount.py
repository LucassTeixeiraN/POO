from components import Account, GainMixIn

class SavingAccount(Account, GainMixIn):

    def __init__(self, name: str, document: str, accountNumber: str, balance: float, accountType: str, tax):
        super().__init__(name, document, accountNumber, balance, accountType)
        self.tax = tax

    # def gain(self, time: int) -> float:
    #     return self.calculateGain(time)

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


        