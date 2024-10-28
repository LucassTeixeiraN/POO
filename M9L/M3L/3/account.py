import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Account:
    def __init__(self, saldo):
        self.saldo = saldo
        self.customer = None

    def debit(self, quantidade):
        if quantidade > self.saldo:
            print('Quantia de débito excedeu o saldo da conta.')
        else:
            self.saldo -= quantidade
        print(f'Saldo disponível: {locale.currency(self.saldo, grouping=True)}\n')

    def __str__(self):
        return f'Conta de {self.customer.name} - Saldo: {locale.currency(self.saldo, grouping=True)}'
