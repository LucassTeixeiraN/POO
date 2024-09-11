'''Crie uma classe Account que representa uma conta bancária. A classe deve fornecer
um método chamado debit para retirar dinheiro da conta. Assegure que a quantia de
débito não exceda o saldo de Account. Se exceder, o saldo deve ser deixado
inalterado e o método deve imprimir uma mensagem que indica “Quantia de débito
excedeu o saldo da conta”. Teste a classe implementada e seus métodos.'''
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Account:
    def __init__(self, saldo):
        self.saldo = saldo

    def debit(self, quantidade):
        if quantidade > self.saldo:
            print('Quantia de débito excedeu o saldo da conta.')
        else:
            self.saldo -= quantidade
        print(f'Saldo disponível: {locale.currency(self.saldo, grouping=True)}\n')

def main():
    conta = Account(1000)
    conta.debit(100)
    conta.debit(300)
    conta.debit(700)
    conta.debit(200)

main()