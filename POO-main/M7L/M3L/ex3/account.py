import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Account:
    def __init__(self, saldo):
        self.saldo = saldo

    def debit(self, quantidade, function):
        if function(self, quantidade):
            print(f'Débito de {locale.currency(quantidade, grouping=True)} realizado.')
        else:
            print('Quantia de débito excedeu o saldo da conta.')

    def __str__(self):
        return f'Saldo disponível: {locale.currency(self.saldo, grouping=True)}\n'

def regular_debit(account, quantidade):
    if quantidade <= account.saldo:
        account.saldo -= quantidade
        return True
    return False

def premium_debit(account, quantidade):
    '''Permite ter saldo negativo'''
    account.saldo -= quantidade
    return True
