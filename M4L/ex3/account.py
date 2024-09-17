import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Account:
    def __init__(self, saldo):
        self.saldo = saldo

    def __imprimeSaldo(self):
        print(f'Saldo disponível: {locale.currency(self.saldo, grouping=True)}\n')

    def __validaSaldo(self, quantidade):
        if quantidade > self.saldo:
            print('Quantia de débito excedeu o saldo da conta.')
            return False
        return True

    def debit(self, quantidade):
        if not self.__validaSaldo(quantidade):
            self.saldo -= quantidade
        self.__imprimeSaldo()