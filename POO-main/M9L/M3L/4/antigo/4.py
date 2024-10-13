'''4. Crie uma versão nova da classe Account com um método chamado displayAccount,
que exiba o name e o balance de uma conta passada como parâmetro. Altere também
o main para, ao invés de imprimir diretamente o name e o balance da conta, use o
método displayAccount, passando a conta como parâmetro.'''
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Account:
    def __init__(self, name, saldo):
        self.saldo = saldo
        self.name = name

    def displayAccount(self, debito):
        if debito > self.saldo:
            print('Quantia de débito excedeu o saldo da conta.')
        else:
            self.saldo -= debito
            print(f"Nome: {self.name}, Saldo disponível: {locale.currency(self.saldo, grouping=True)}")

def main():
    conta = Account("Herba", 1000)
    conta.displayAccount(10000)

main()