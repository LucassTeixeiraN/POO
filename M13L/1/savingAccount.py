from account import Account

class SavingAccount(Account):

    def __init__(self, name, document, accountNumber, balance, accountType, tax):
        super().__init__(name, document, accountNumber, balance, accountType)
        self.tax = tax

    def calculateGain(self, time):
        return self.getBalance()*((1+self.tax)**time)
    
    def showAccount(self):
        print("Informações da conta")
        print(f"Nome: {self.getName()}")
        print(f"Tipo da conta: {self.getAccountType()}")
        print(f"Número da conta: {self.getAccountNumber()}")
        print(f"Documento: {self.getDocument()}")
        print(f"Saldo: R${self.getBalance():.2f}")
        print(f"Taxa aplicada ao mês: {self.tax}")
