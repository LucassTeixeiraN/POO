'''4. Crie uma versão nova da classe Account com um método chamado displayAccount,
que exiba o name e o balance de uma conta passada como parâmetro. Altere também
o main para, ao invés de imprimir diretamente o name e o balance da conta, use o
método displayAccount, passando a conta como parâmetro.'''

class Account:
    def __init__(self, name, saldo):
        self.saldo = saldo
        self.name = name

    def displayAccount(self):
        print(f"Nome: {self.name}, Saldo: {self.saldo:.2f}")

def main():
    conta = Account("Herba", 1000)
    conta.displayAccount()

main()
