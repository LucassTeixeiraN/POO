from components import Account

class CheckingAccount(Account):
    def __init__(self, name: str, document: str, accountNumber: str, balance: float, accountType: str):
        super().__init__(name, document, accountNumber, balance, accountType)

    def transfer(self, value: float) -> None:
        if self.checkBalance(value):
            self.setBalance(self.getBalance() - value)
            self.transactionLog(value, "Transação bancária")
            print("-"*60)
        else:
            print("Saldo insuficiente")
            print("-"*60)

    def showAccount(self) -> None:
        print("-"*60)
        print("Informações da conta")
        print(f"Nome: {self.getName()}")
        print(f"Tipo da conta: {self.getAccountType()}")
        print(f"Número da conta: {self.getAccountNumber()}")
        print(f"Documento: {self.getDocument()}")
        print(f"Saldo: R${self.getBalance():.2f}")
        print("-"*60)