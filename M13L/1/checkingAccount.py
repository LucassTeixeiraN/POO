from account import Account

class CheckingAccount(Account):
    def __init__(self, name, document, accountNumber, balance, accountType):
        super().__init__(name, document, accountNumber, balance, accountType)

    def transfer(self, value):
        if self.checkBalance(value):
            self.setBalance(self.getBalance - value)
        else:
            print("Saldo insuficiente")

    def showAccount(self):
        print("Informações da conta")
        print(f"Nome: {self.getName()}")
        print(f"Tipo da conta: {self.getAccountType()}")
        print(f"Número da conta: {self.getAccountNumber()}")
        print(f"Documento: {self.getDocument()}")
        print(f"Saldo: R${self.getBalance():.2f}")
