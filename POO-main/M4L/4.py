'''4. Crie uma versão nova da classe Account com um método chamado displayAccount,
que exiba o name e o balance de uma conta passada como parâmetro. Altere também
o main para, ao invés de imprimir diretamente o name e o balance da conta, use o
método displayAccount, passando a conta como parâmetro.'''
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Account:
    def __init__(self, name, balance):
        self.__balance = balance
        self.__name = name

    def __insuficientBalance(self, debito):
        if debito > self.__balance:
            return True
        return False

    def __decreaseBalance(self, debit):
        self.__balance -= debit

    def __showBalance(self):
        return f"Nome: {self.__name}, Saldo disponível: {locale.currency(self.__balance, grouping=True)}"

    def displayAccount(self, debit):
        if self.__insuficientBalance(debit):
            print('Quantia de débito excedeu o saldo da conta.')
        else:
            self.__decreaseBalance(debit)
            print(self.__showBalance())
            

def main():
    conta = Account("Herba", 1000)
    conta.displayAccount(100)

main()